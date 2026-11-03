"""Tests of checks/local/topic_cost.py. Run: python3 -m unittest discover -s checks"""
import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
SPEC = importlib.util.spec_from_file_location("topic_cost", HERE.parent / "local" / "topic_cost.py")
tc = importlib.util.module_from_spec(SPEC)
sys.modules["topic_cost"] = tc
SPEC.loader.exec_module(tc)

S = dict(tc.DEFAULTS)


def words(n: int) -> str:
    return " ".join(["Word"] * n) + "."


class Reading(unittest.TestCase):
    def test_run_counts_prose_before_the_first_list(self):
        text = f"# T\n\n{words(10)}\n\n- item one\n\n{words(50)}\n"
        self.assertEqual(tc.read_file(text).run, 10)

    def test_run_stops_at_a_table(self):
        text = f"# T\n\n{words(5)}\n\n| a | b |\n|---|---|\n\n{words(9)}\n"
        self.assertEqual(tc.read_file(text).run, 5)

    def test_no_list_counts_all_prose(self):
        text = f"# T\n\n{words(5)}\n\n## H\n\n{words(7)}\n"
        self.assertEqual(tc.read_file(text).run, 12)

    def test_code_html_badges_and_headings_do_not_count(self):
        text = ("# Title here\n\n[![a](b)](c)\n\n```\none two three four\n```\n\n"
                f"<details>\n<summary>x y z</summary>\n\n```dot\na b c\n```\n\n</details>\n\n{words(4)}\n")
        self.assertEqual(tc.read_file(text).run, 4)

    def test_link_addresses_do_not_count(self):
        self.assertEqual(tc.read_file("# T\n\nSee [the page](http://a.b/c/d/e) now.\n").run, 4)

    def test_longest_sentence(self):
        text = f"# T\n\n{words(3)} {words(12)} {words(5)}\n"
        self.assertEqual(tc.read_file(text).sentence, 12)

    def test_abbreviation_does_not_split(self):
        self.assertEqual(tc.read_file("# T\n\nOne thing, e.g. two more things.\n").sentence, 6)

    def test_lists_are_not_sentences(self):
        text = f"# T\n\nShort one.\n\n- {words(80)}\n"
        self.assertEqual(tc.read_file(text).sentence, 2)

    def test_front_matter_is_dropped(self):
        self.assertEqual(tc.read_file("---\ntitle: a b c d\n---\n# T\n\nOne two.\n").run, 2)

    def test_empty_file(self):
        self.assertEqual(tc.read_file(""), tc.Reading(0, 0))


class Cost(unittest.TestCase):
    def test_within_thresholds_a_root_costs_nothing(self):
        self.assertEqual(tc.break_cost(0, 7, tc.Reading(60, 35), S), 0)

    def test_depth_alone(self):
        self.assertEqual(tc.break_cost(3, 0, tc.Reading(0, 0), S), 3)

    def test_each_child_beyond_free_is_one_break(self):
        self.assertEqual(tc.break_cost(0, 10, tc.Reading(0, 0), S), 3)

    def test_run_break_is_per_step(self):
        self.assertEqual(tc.break_cost(0, 0, tc.Reading(120, 0), S), 1)

    def test_sentence_break_is_per_step(self):
        self.assertAlmostEqual(tc.break_cost(0, 0, tc.Reading(0, 55), S), 2)

    def test_nesting_multiplies_the_break(self):
        shallow = tc.break_cost(0, 8, tc.Reading(0, 0), S)
        deep = tc.break_cost(2, 8, tc.Reading(0, 0), S)
        self.assertEqual(shallow, 1)
        self.assertEqual(deep, 2 + 3 * 1)

    def test_weights_apply(self):
        s = {**S, "fan_weight": 2.0}
        self.assertEqual(tc.break_cost(0, 8, tc.Reading(0, 0), s), 2)

    def test_monotone_in_every_component(self):
        base = tc.break_cost(1, 7, tc.Reading(60, 35), S)
        for args in [(2, 7, tc.Reading(60, 35)), (1, 8, tc.Reading(60, 35)),
                     (1, 7, tc.Reading(90, 35)), (1, 7, tc.Reading(60, 45))]:
            self.assertGreater(tc.break_cost(*args, S), base)


class Tree(unittest.TestCase):
    TEXTS = {
        "README.md": "# Root\n\nSummary.\n\n| [a](a/) | x |\n",
        "a/README.md": "# A\n\nSummary.\n",
        "a/note.md": "# Note\n\nSummary.\n",
        "a/b/README.md": "# B\n\nSummary.\n",
        "top.md": "# Top\n\nSummary.\n",
    }

    def test_depth_and_children(self):
        by = {t.path: t for t in tc.measure(Path("."), None, self.TEXTS)}
        self.assertEqual(by["README.md"].depth, 0)
        self.assertEqual(by["README.md"].children, 2)
        self.assertEqual(by["a/README.md"].depth, 1)
        self.assertEqual(by["a/README.md"].children, 2)
        self.assertEqual(by["a/note.md"].depth, 2)
        self.assertEqual(by["a/b/README.md"].depth, 2)
        self.assertEqual(by["top.md"].depth, 1)

    def test_no_root_gives_nothing(self):
        self.assertEqual(tc.measure(Path("."), None, {"a/README.md": "# A\n"}), [])

    def test_fan_out_raises_the_tree_cost(self):
        flat = dict(self.TEXTS)
        for i in range(10):
            flat[f"x{i}.md"] = "# X\n\nSummary.\n"
        low = tc.summarise("t", tc.measure(Path("."), None, self.TEXTS)).total
        high = tc.summarise("t", tc.measure(Path("."), None, flat)).total
        self.assertGreater(high, low)

    def test_summary_row(self):
        tree = tc.summarise("t", tc.measure(Path("."), None, self.TEXTS))
        self.assertEqual((tree.topics, tree.max_depth, tree.max_children), (5, 2, 2))
        self.assertEqual(tree.total, 0 + 1 + 2 + 2 + 1)

    def test_empty_summary(self):
        self.assertEqual(tc.summarise("t", []).topics, 0)


class OnDisk(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.root)

    def test_scope_excludes_translations_and_checks(self):
        for path in ["README.md", "README.fr.md", "AGENTS.md", "checks/README.md", "d/README.md"]:
            (self.root / path).parent.mkdir(parents=True, exist_ok=True)
            (self.root / path).write_text("# T\n\nSummary.\n")
        paths = [t.path for t in tc.measure(self.root)]
        self.assertEqual(paths, ["README.md", "d/README.md"])

    def test_config_overrides_defaults(self):
        cfg = self.root / "c.toml"
        cfg.write_text("[topic_cost]\nfan_free = 1\n")
        self.assertEqual(tc.load_settings(cfg)["fan_free"], 1)
        self.assertEqual(tc.load_settings(cfg)["run_free"], 60)
        self.assertEqual(tc.load_settings(None)["fan_free"], 7)

    def test_the_repository_config_loads_with_every_key(self):
        settings = tc.load_settings(HERE.parent / "config.toml")
        for key in ["depth_weight", "nesting_weight", "fan_free", "fan_weight", "run_free", "run_step", "run_weight",
                    "sentence_free", "sentence_step", "sentence_weight", "topic_budget"]:
            self.assertIn(key, settings)

    def test_every_tunable_is_tagged(self):
        text = (HERE.parent / "config.toml").read_text()
        block = text.split("[topic_cost]")[1].split("\n[")[0]
        lines = [l for l in block.splitlines() if "=" in l]
        self.assertEqual(len(lines), 11)
        self.assertTrue(all("PROVISIONAL" in l for l in lines))


class TheCheck(unittest.TestCase):
    CONFIG = "[topic_cost]\nfan_free = 7  # PROVISIONAL: a guess\nfan_weight = 1.0\n[other]\nrun_free = 1\n"

    def test_it_is_a_check(self):
        self.assertEqual(tc.NAME, "topic-cost")
        self.assertFalse(tc.EXACT)

    def test_an_untagged_tunable_is_named_with_its_line(self):
        self.assertEqual(tc.untagged(self.CONFIG), [(3, "fan_weight")])

    def test_other_tables_and_comments_are_not_read(self):
        self.assertEqual(tc.untagged("[topic_cost]\n# fan_free = 1\n[other]\nfan_free = 1\n"), [])

    def test_the_repository_config_has_no_untagged_tunable(self):
        self.assertEqual(tc.untagged((HERE.parent / "config.toml").read_text()), [])

    def test_every_tunable_has_a_default(self):
        for key in tc.TUNABLES:
            self.assertIn(key, tc.DEFAULTS)

    def test_the_check_reports_an_error_and_a_warning(self):
        root = Path(tempfile.mkdtemp())
        try:
            (root / "checks").mkdir()
            (root / "checks" / "config.toml").write_text(self.CONFIG)
            (root / "README.md").write_text("# Root\n\nSummary.\n")
            for i in range(10):
                (root / f"t{i}.md").write_text("# T\n\nSummary.\n")
            found = tc.check(root, {"topic_cost": {"topic_budget": 2.0}})
            self.assertEqual([f.kind for f in found], ["error", "warning"])
            self.assertEqual((found[0].path, found[0].line), ("checks/config.toml", 3))
            self.assertEqual(found[1].path, "README.md")
        finally:
            shutil.rmtree(root)

    def test_a_tree_within_budget_is_silent(self):
        root = Path(tempfile.mkdtemp())
        try:
            (root / "README.md").write_text("# Root\n\nSummary.\n")
            self.assertEqual(tc.check(root, {}), [])
        finally:
            shutil.rmtree(root)


if __name__ == "__main__":
    unittest.main()
