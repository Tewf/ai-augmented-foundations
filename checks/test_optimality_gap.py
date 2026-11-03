"""Tests of checks/local/optimality_gap.py. Run: python3 -m unittest discover -s checks"""
import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
SPEC = importlib.util.spec_from_file_location("optimality_gap", HERE.parent / "local" / "optimality_gap.py")
og = importlib.util.module_from_spec(SPEC)
sys.modules["optimality_gap"] = og
SPEC.loader.exec_module(og)

GOOD = {"name": "r", "objective": 423, "bound": 353, "status": "feasible"}
ACCEPTED = {**GOOD, "accepted": True, "criterion": "the checks pass", "tolerance": 0.2}


class Gap(unittest.TestCase):
    def test_gap_is_relative_to_the_objective(self):
        self.assertAlmostEqual(og.gap(423, 353), 70 / 423)
        self.assertEqual(og.gap(10, 10), 0)

    def test_a_consistent_record_has_no_problem(self):
        self.assertEqual(og.problems(GOOD, None), [])
        self.assertEqual(og.problems(ACCEPTED, None), [])

    def test_bound_above_objective(self):
        self.assertTrue(og.problems({**GOOD, "bound": 500}, None))

    def test_optimal_needs_equal_bound(self):
        self.assertTrue(og.problems({**GOOD, "status": "optimal"}, None))
        self.assertEqual(og.problems({**GOOD, "status": "optimal", "bound": 423}, None), [])

    def test_non_positive_objective(self):
        self.assertTrue(og.problems({**GOOD, "objective": 0}, None))

    def test_missing_numbers(self):
        self.assertTrue(og.problems({"name": "x"}, None))

    def test_accepted_needs_a_criterion(self):
        self.assertTrue(og.problems({**ACCEPTED, "criterion": " "}, None))

    def test_accepted_needs_a_tolerance_from_the_record_or_the_config(self):
        bare = {k: v for k, v in ACCEPTED.items() if k != "tolerance"}
        self.assertTrue(og.problems(bare, None))
        self.assertEqual(og.problems(bare, 0.2), [])

    def test_accepted_past_the_tolerance_needs_a_waiver(self):
        late = {**ACCEPTED, "tolerance": 0.1}
        self.assertTrue(og.problems(late, None))
        self.assertEqual(og.problems({**late, "waiver": "the optimum answers another question"}, None), [])

    def test_a_run_not_accepted_is_not_held_to_a_tolerance(self):
        self.assertEqual(og.problems({**GOOD, "tolerance": 0.01}, None), [])


class OnDisk(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.root)

    def run_check(self, text, config):
        (self.root / "runs.toml").write_text(text)
        return og.check(self.root, config)

    def test_nothing_declared_nothing_checked(self):
        self.assertEqual(self.run_check("[[run]]\nobjective = -1\nbound = 0\n", {}), [])

    def test_records_are_read_and_reported(self):
        config = {"optimality_gap": {"records": ["runs.toml"]}}
        found = self.run_check('[[run]]\nname = "a"\nobjective = 1\nbound = 2\n', config)
        self.assertEqual(len(found), 1)
        self.assertEqual((found[0].check, found[0].path, found[0].kind), ("optimality-gap", "runs.toml", "error"))

    def test_the_default_tolerance_is_read_from_the_config(self):
        config = {"optimality_gap": {"records": ["runs.toml"], "tolerance": 0.2}}
        text = '[[run]]\nname = "a"\nobjective = 10\nbound = 9\naccepted = true\ncriterion = "c"\n'
        self.assertEqual(self.run_check(text, config), [])

    def test_invalid_toml_is_a_finding(self):
        config = {"optimality_gap": {"records": ["runs.toml"]}}
        self.assertEqual(len(self.run_check("[[run", config)), 1)


class Repository(unittest.TestCase):
    def test_the_records_of_this_repository_are_consistent(self):
        import tomllib
        root = HERE.parent.parent
        config = tomllib.loads((HERE.parent / "config.toml").read_text())
        self.assertEqual(og.check(root, config), [])


if __name__ == "__main__":
    unittest.main()
