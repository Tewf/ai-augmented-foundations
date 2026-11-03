"""Tests of replay.py: the trace file, the beliefs, each policy on a toy history, the stop and the counts."""
import random
import unittest
from pathlib import Path

import replay

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def job(kind, wave, moved=None, kept=None, agents=1, tokens=100, family=True):
    j = {"id": f"{kind}-{wave}", "wave": wave, "kind": kind, "agents": agents, "tokens_k": tokens,
         "tokens_source": "estimate", "produced": "p", "changed": "c"}
    if moved is not None:
        j["moved"] = moved
    if kept is not None:
        j["kept"] = kept
    if not family:
        j["in_family"] = False
    return j


class TraceFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.jobs = replay.load()

    def test_every_row_has_its_fields(self):
        for j in self.jobs:
            for key in ("id", "wave", "kind", "agents", "tokens_k", "tokens_source", "produced", "changed"):
                self.assertIn(key, j, j["id"])

    def test_kinds_and_sources_are_known(self):
        for j in self.jobs:
            self.assertIn(j["kind"], replay.KINDS)
            self.assertIn(j["tokens_source"], ("recorded", "estimate"))

    def test_ids_are_unique(self):
        ids = [j["id"] for j in self.jobs]
        self.assertEqual(len(ids), len(set(ids)))

    def test_outcomes_are_binary_or_absent(self):
        for j in self.jobs:
            for key in ("moved", "kept"):
                self.assertIn(j.get(key), (None, 0, 1), j["id"])

    def test_a_moved_comes_with_a_kept(self):
        for j in replay.family(self.jobs):
            self.assertEqual("moved" in j, "kept" in j, j["id"])

    def test_waves_run_from_zero_without_a_gap(self):
        w = replay.waves(self.jobs)
        self.assertEqual(w, list(range(len(w))))

    def test_the_recorded_costs_are_the_logged_ones(self):
        rec = {j["id"]: j["tokens_k"] for j in self.jobs if j["tokens_source"] == "recorded"}
        self.assertEqual(rec, {"project-review": 250, "cases-review": 326})

    def test_the_trace_page_matches_the_program(self):
        text = (ROOT / "design" / "trace.md").read_text()
        self.assertIn(replay.table(self.jobs), text)


class Beliefs(unittest.TestCase):
    def test_empty_history_is_the_prior(self):
        bs = replay.beliefs([], "moved")
        self.assertTrue(all(b.mean == 0.5 and b.runs == 0 for b in bs))
        self.assertTrue(all(b.cost == replay.PRIOR_COST for b in bs))

    def test_counts_move_the_belief(self):
        h = [job("review", 0, 1, 1), job("review", 0, 1, 1), job("review", 0, 0, 1)]
        b = {x.kind: x for x in replay.beliefs(h, "moved")}["review"]
        self.assertEqual((b.a, b.b, b.runs), (3.0, 2.0, 3))
        self.assertAlmostEqual(b.mean, 0.6)

    def test_a_row_without_outcome_counts_as_run_not_learned(self):
        h = [job("review", 0)]
        b = {x.kind: x for x in replay.beliefs(h, "moved")}["review"]
        self.assertEqual((b.a, b.b, b.runs), (1.0, 1.0, 1))

    def test_cost_is_agents_times_tokens_averaged_by_kind(self):
        h = [job("audit", 0, 1, 1, agents=7, tokens=100), job("audit", 0, 1, 1, agents=1, tokens=100)]
        b = {x.kind: x for x in replay.beliefs(h, "moved")}["audit"]
        self.assertEqual(b.cost, 400.0)

    def test_value_is_benefit_times_chance_minus_cost(self):
        h = [job("build", 0, 1, 1, tokens=100)]
        b = {x.kind: x for x in replay.beliefs(h, "moved")}["build"]
        self.assertAlmostEqual(b.value, replay.BENEFIT * (2 / 3) - 100)


class Policies(unittest.TestCase):
    def setUp(self):
        self.rng = random.Random(1)
        self.history = [job("review", 0, 1, 1), job("review", 0, 1, 1), job("build", 0, 0, 1)]
        self.bs = replay.beliefs(self.history, "moved")

    def test_greedy_takes_the_best_mean_value(self):
        best = max(self.bs, key=lambda b: b.value).kind
        self.assertEqual(replay.propose("greedy", self.bs, self.history, self.rng), best)

    def test_ucb1_tries_an_unrun_arm_first(self):
        pick = replay.propose("UCB1", self.bs, self.history, self.rng)
        self.assertNotIn(pick, ("review", "build"))

    def test_ucb1_with_every_arm_run_prefers_the_less_tried(self):
        h = [job(k, 0, 1, 1) for k in replay.KINDS] + [job("review", 0, 1, 1) for _ in range(30)]
        pick = replay.propose("UCB1", replay.beliefs(h, "moved"), h, self.rng)
        self.assertNotEqual(pick, "review")

    def test_thompson_is_deterministic_for_a_seed(self):
        a = replay.propose("Thompson", self.bs, self.history, random.Random(7))
        b = replay.propose("Thompson", self.bs, self.history, random.Random(7))
        self.assertEqual(a, b)

    def test_thompson_follows_a_dominant_arm(self):
        h = [job("review", 0, 1, 1) for _ in range(40)] + [job("build", 0, 0, 1) for _ in range(40)]
        pick = replay.propose("Thompson", replay.beliefs(h, "moved"), h, random.Random(3))
        self.assertEqual(pick, "review")

    def test_kg_is_never_negative(self):
        for i in range(len(self.bs)):
            self.assertGreaterEqual(replay.knowledge_gradient(self.bs, i), -1e-9)

    def test_kg_matches_a_hand_calculation(self):
        h = [job("setup", 0, None, None, tokens=100)]
        bs = replay.beliefs(h, "moved")
        i = [b.kind for b in bs].index("setup")
        others = max(b.value for j, b in enumerate(bs) if j != i)
        up = replay.BENEFIT * (2 / 3) - 100
        down = replay.BENEFIT * (1 / 3) - 100
        want = 0.5 * max(up, others) + 0.5 * max(down, others) - max(bs[i].value, others)
        self.assertAlmostEqual(replay.knowledge_gradient(bs, i), want)

    def test_kg_is_zero_when_one_step_cannot_change_the_best(self):
        h = [job("review", 0, 1, 1) for _ in range(50)]
        for k in replay.KINDS:
            if k != "review":
                h += [job(k, 0, 0, 0, tokens=1000) for _ in range(50)]
        bs = replay.beliefs(h, "moved")
        for i in range(len(bs)):
            self.assertAlmostEqual(replay.knowledge_gradient(bs, i), 0.0, places=6)

    def test_unknown_policy_is_refused(self):
        with self.assertRaises(ValueError):
            replay.propose("oracle", self.bs, self.history, self.rng)


class Stop(unittest.TestCase):
    def test_no_remaining_jobs_means_stop(self):
        bs = replay.beliefs([job("review", 0, 1, 1)], "moved")
        self.assertTrue(replay.stop_verdict(bs, 0)["stop"])

    def test_a_long_horizon_with_little_known_means_go_on(self):
        h = [j for j in replay.family(replay.load()) if j["wave"] == 0]
        self.assertFalse(replay.stop_verdict(replay.beliefs(h, "moved"), 40)["stop"])

    def test_the_same_belief_stops_when_the_horizon_is_short(self):
        h = [j for j in replay.family(replay.load()) if j["wave"] == 0]
        self.assertTrue(replay.stop_verdict(replay.beliefs(h, "moved"), 0)["stop"])

    def test_exploit_only_flag_when_nothing_pays(self):
        h = [job(k, 0, 0, 0, tokens=5000) for k in replay.KINDS for _ in range(5)]
        bs = replay.beliefs(h, "moved")
        self.assertTrue(replay.stop_verdict(bs, 10)["exploit_only"])


class Replay(unittest.TestCase):
    def test_the_replay_starts_at_the_second_wave(self):
        jobs = [job("review", 0, 1, 1), job("build", 1, 1, 1), job("audit", 2, 0, 1)]
        recs = replay.replay(jobs)
        self.assertEqual([r["wave"] for r in recs], [1, 2])
        self.assertEqual(recs[0]["ran"], ["build"])
        self.assertEqual(recs[0]["jobs"], 1)

    def test_outside_the_family_is_left_out(self):
        jobs = [job("review", 0, 1, 1), job("build", 1, 1, 1), job("audit", 1, 1, 1, family=False)]
        self.assertEqual(replay.replay(jobs)[0]["ran"], ["build"])

    def test_hit_and_random_expectation(self):
        rec = {"ran": ["build", "review"], "proposal": {"greedy": "build", "UCB1": "audit"}}
        self.assertEqual(replay.hit(rec, "greedy"), 1.0)
        self.assertEqual(replay.hit(rec, "UCB1"), 0.0)
        self.assertAlmostEqual(replay.hit(rec, "random"), 2 / len(replay.KINDS))

    def test_the_two_outcomes_can_give_different_proposals(self):
        jobs = replay.load()
        a = replay.replay(jobs, "moved")
        b = replay.replay(jobs, "kept")
        self.assertNotEqual([r["proposal"] for r in a], [r["proposal"] for r in b])

    def test_replay_is_reproducible(self):
        jobs = replay.load()
        self.assertEqual(replay.replay(jobs), replay.replay(jobs))

    def test_disagreed_tokens_sum_the_other_kinds(self):
        jobs = [job("review", 0, 1, 1), job("build", 1, 1, 1, tokens=100), job("audit", 1, 1, 1, tokens=50)]
        recs = replay.replay(jobs)
        recs[0]["proposal"]["greedy"] = "build"
        self.assertEqual(replay.disagreed_tokens(jobs, recs)["greedy"], 50)

    def test_missed_cost_counts_only_the_misses(self):
        jobs = [job("review", 0, 1, 1), job("build", 1, 1, 1, tokens=100), job("audit", 2, 1, 1, tokens=50)]
        recs = replay.replay(jobs)
        for r in recs:
            r["proposal"]["greedy"] = "build"
            r["step_cost"]["greedy"] = 7
        self.assertEqual(replay.missed_cost(recs)["greedy"], 7)

    def test_stop_ceiling_counts_the_jobs_from_the_wave_on(self):
        jobs = [job("review", 0, 1, 1, tokens=10), job("build", 1, 1, 1, tokens=20), job("audit", 2, 1, 1, tokens=30)]
        self.assertEqual(replay.stop_ceiling(jobs, 1), 50)
        self.assertAlmostEqual(replay.points(60, jobs), replay.METER_POINTS)

    def test_the_report_names_every_policy(self):
        text = replay.report(replay.load(), "moved")
        for p in replay.POLICIES:
            self.assertIn(p, text)

    def test_by_kind_totals_the_family(self):
        jobs = replay.load()
        self.assertEqual(sum(r[1] for r in replay.by_kind(jobs)), len(replay.family(jobs)))


if __name__ == "__main__":
    unittest.main()
