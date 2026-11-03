"""Tests of worked_model.py: the recorded counts, the acquisition formulas, the stopping rule, and determinism."""
import copy
import json
import math
import unittest
from pathlib import Path

import numpy as np

import worked_model as wm

HERE = Path(__file__).resolve().parent
FAMILY = HERE.parents[2]  # the folder holding the sibling repositories, when present
BRIEF = FAMILY / "ai-augmented-agents" / "experiments" / "brief-test" / "results-2.jsonl"
METHOD = FAMILY / "ai-augmented-project" / "experiments" / "method-comparison" / "results.jsonl"


class Counts(unittest.TestCase):
    def setUp(self):
        self.cfg = wm.load()

    def test_total_runs_by_stage(self):
        self.assertEqual(sum(wm.counts(self.cfg, 1)[1].values()), 30)
        self.assertEqual(sum(wm.counts(self.cfg, 2)[1].values()), 210)
        self.assertEqual(sum(wm.counts(self.cfg, 3)[1].values()), 240)

    def test_pooled_small_tier(self):
        k, n = wm.counts(self.cfg, 3)
        self.assertEqual((k["api-small-2"], n["api-small-2"]), (9, 40))

    @unittest.skipUnless(BRIEF.exists(), "the sibling repository is not beside this one")
    def test_round_two_counts_match_the_record(self):
        rows = [json.loads(line) for line in BRIEF.read_text().splitlines() if line.strip()]
        k, n = wm.counts(self.cfg, 3)
        for tier, name in (("small", "small"), ("paid", "haiku")):
            for arm, info in (("none", 0), ("convention", 1), ("full", 2)):
                ok = [r for r in rows if r["tier"] == tier and r["arm"] == arm and not r["error"]]
                got = sum(bool(r["hidden"]) for r in ok)
                round_one = {("small", 0): 0, ("small", 1): 0, ("small", 2): 1}.get((name, info), 0)
                self.assertEqual(k[f"api-{name}-{info}"], got + round_one)

    @unittest.skipUnless(METHOD.exists(), "the sibling repository is not beside this one")
    def test_method_comparison_counts_match_the_record(self):
        rows = [json.loads(line) for line in METHOD.read_text().splitlines() if line.strip()]
        k, n = wm.counts(self.cfg, 3)
        for arm, arm_id in (("alone", "agent-haiku-0"), ("method", "agent-haiku-3")):
            ok = [r for r in rows if r["arm"] == arm and not r["error"]]
            self.assertEqual((k[arm_id], n[arm_id]), (sum(bool(r["verdict"]["hidden"]) for r in ok), len(ok)))


class Acquisition(unittest.TestCase):
    def test_ei_is_zero_without_uncertainty_below_the_best(self):
        self.assertEqual(wm.expected_improvement(1.0, 0.0, 2.0), 0.0)

    def test_ei_without_uncertainty_above_the_best_is_the_gap(self):
        self.assertEqual(wm.expected_improvement(3.0, 0.0, 2.0), 1.0)

    def test_ei_at_the_best_is_sd_over_root_two_pi(self):
        self.assertAlmostEqual(wm.expected_improvement(2.0, 0.5, 2.0), 0.5 / math.sqrt(2 * math.pi))

    def test_ei_grows_with_uncertainty(self):
        self.assertGreater(wm.expected_improvement(1.0, 2.0, 2.0), wm.expected_improvement(1.0, 1.0, 2.0))

    def test_knowledge_gradient_is_never_negative(self):
        cfg = wm.load()
        mean, cov = wm.posterior(cfg, 3)
        value = cfg["model"]["benefit_per_pass"] * mean - np.array([wm.cost_of(a, cfg) for a in cfg["arm"]])
        for j in range(len(cfg["arm"])):
            self.assertGreaterEqual(wm.knowledge_gradient(mean, cov, j, value, cfg), -1e-6)

    def test_knowledge_gradient_is_zero_for_an_arm_known_exactly(self):
        cfg = wm.load()
        mean = np.array([0.5, 0.2])
        cov = np.zeros((2, 2))
        value = np.array([10.0, 5.0])
        self.assertAlmostEqual(wm.knowledge_gradient(mean, cov + 1e-18, 0, value, cfg), 0.0, places=6)


class Posterior(unittest.TestCase):
    def setUp(self):
        self.cfg = wm.load()

    def test_covariance_is_symmetric_and_variances_non_negative(self):
        mean, cov = wm.posterior(self.cfg, 3)
        self.assertTrue(np.allclose(cov, cov.T, atol=1e-9))
        self.assertTrue((np.diag(cov) > -1e-9).all())

    def test_an_arm_with_many_runs_is_close_to_its_rate(self):
        mean, _ = wm.posterior(self.cfg, 3)
        ids = [a["id"] for a in self.cfg["arm"]]
        self.assertAlmostEqual(mean[ids.index("api-haiku-1")], 22 / 30, delta=0.12)

    def test_without_data_the_prior_mean_is_returned(self):
        mean, _ = wm.posterior(self.cfg, 0)
        self.assertTrue(np.allclose(mean, self.cfg["model"]["prior_mean"]))

    def test_an_unseen_arm_is_more_uncertain_than_a_seen_one(self):
        _, cov = wm.posterior(self.cfg, 3)
        ids = [a["id"] for a in self.cfg["arm"]]
        self.assertGreater(cov[ids.index("agent-small-3"), ids.index("agent-small-3")],
                           cov[ids.index("api-haiku-1"), ids.index("api-haiku-1")])


class Stopping(unittest.TestCase):
    def test_more_future_runs_can_only_turn_a_stop_into_a_go(self):
        cfg = wm.load()
        seen = []
        for runs in (1, 100, 100_000):
            c = copy.deepcopy(cfg)
            c["model"]["future_runs"] = runs
            rows, _ = wm.choose(c, 3)
            seen.append({r["policy"]: r["stop"] for r in rows})
        for policy in wm.POLICIES:
            flags = [s[policy] for s in seen]
            self.assertEqual(flags, sorted(flags, reverse=True))

    def test_break_even_is_the_step_cost_over_the_gain(self):
        rows, _ = wm.choose(wm.load(), 3)
        for r in rows:
            self.assertAlmostEqual(r["break_even_runs"] * r["gain_per_run"], r["step_cost"], places=3)

    def test_a_free_step_is_never_a_stop(self):
        cfg = wm.load()
        cfg["model"]["agent_tokens_alone"] = 0
        cfg["model"]["agent_tokens_method"] = 0
        cfg["model"]["output_tokens_api"] = 0
        for a in cfg["arm"]:
            if "prompt_tokens" in a:
                a["prompt_tokens"] = 0
        rows, _ = wm.choose(cfg, 3)
        self.assertTrue(all(not r["stop"] for r in rows))


class Determinism(unittest.TestCase):
    def test_same_inputs_same_report(self):
        self.assertEqual(wm.report(wm.load()), wm.report(wm.load()))

    def test_probabilities_of_being_best_sum_to_one(self):
        _, info = wm.choose(wm.load(), 3)
        self.assertAlmostEqual(float(info["pbest"].sum()), 1.0)

    def test_cost_of_the_two_measured_agent_arms(self):
        cfg = wm.load()
        costs = {a["id"]: wm.cost_of(a, cfg) for a in cfg["arm"]}
        self.assertEqual(costs["agent-haiku-0"], 46900)
        self.assertEqual(costs["agent-haiku-3"], 39650)
        self.assertEqual(costs["agent-haiku-1"], (46900 + 39650) / 2)


if __name__ == "__main__":
    unittest.main()
