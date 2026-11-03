"""The family's runs as the first evaluations of an unknown objective, and the next step each policy would choose.

An arm is a way of delegating a task: a model tier, an information level and an interface. The objective is the net value
of one run, benefit_per_pass * pass rate - cost in tokens. The pass rate is unknown and is learned from the recorded runs.
Inputs are in worked-model.toml; every tunable there is PROVISIONAL. Needs numpy; run: python3 worked_model.py
"""
import math
import sys
import tomllib
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
POLICIES = ("EI", "EI per cost", "knowledge gradient", "GP-UCB", "UCB1", "Thompson")


def load(path=None):
    with open(path or HERE / "worked-model.toml", "rb") as f:
        return tomllib.load(f)


def features(arm):
    return np.array([arm["tier"], arm["info"] / 3.0, arm["interface"]], dtype=float)


def cost_of(arm, cfg):
    """Tokens of one run of the arm. The agent's cost is measured for two arms and assumed between them."""
    m = cfg["model"]
    if arm["interface"] == 0:
        return arm["prompt_tokens"] + m["output_tokens_api"]
    lo, hi = m["agent_tokens_alone"], m["agent_tokens_method"]
    return {0: lo, 3: hi}.get(arm["info"], (lo + hi) / 2.0)


def counts(cfg, upto):
    """Passes and runs per arm, pooled over the stages up to and including `upto`."""
    k = {a["id"]: 0 for a in cfg["arm"]}
    n = dict(k)
    for r in cfg["run"]:
        if r["stage"] <= upto:
            k[r["arm"]] += r["k"]
            n[r["arm"]] += r["n"]
    return k, n


def kernel(xa, xb, cfg):
    m = cfg["model"]
    ls = np.array([m["length_tier"], m["length_info"], m["length_interface"]])
    d = (xa[:, None, :] - xb[None, :, :]) / ls
    return m["amplitude"] * np.exp(-0.5 * (d ** 2).sum(-1))


def posterior(cfg, upto, drop=None):
    """Gaussian-process posterior of the pass rate on every arm: mean, covariance. `drop` leaves one arm's runs out."""
    arms = cfg["arm"]
    x = np.stack([features(a) for a in arms])
    k, n = counts(cfg, upto)
    seen = [i for i, a in enumerate(arms) if n[a["id"]] > 0 and a["id"] != drop]
    mu0 = cfg["model"]["prior_mean"]
    kxx = kernel(x, x, cfg)
    if not seen:
        return np.full(len(arms), mu0), kxx
    ids = [arms[i]["id"] for i in seen]
    phat = np.array([(k[i] + 0.5) / (n[i] + 1.0) for i in ids])
    noise = np.array([p * (1 - p) / (n[i] + 1.0) for p, i in zip(phat, ids)])
    ks = kxx[np.ix_(seen, seen)] + np.diag(noise)
    kc = kxx[:, seen]
    mean = mu0 + kc @ np.linalg.solve(ks, phat - mu0)
    cov = kxx - kc @ np.linalg.solve(ks, kc.T)
    return mean, cov


def step_cost(arm, cfg):
    return cfg["model"]["runs_per_step"] * cost_of(arm, cfg)


def norm_pdf(z):
    return math.exp(-0.5 * z * z) / math.sqrt(2 * math.pi)


def norm_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def expected_improvement(mean, sd, best):
    if sd <= 1e-12:
        return max(mean - best, 0.0)
    z = (mean - best) / sd
    return sd * (z * norm_cdf(z) + norm_pdf(z))


def knowledge_gradient(mean, cov, j, value, cfg, nodes=61):
    """One step of n runs of arm j: expected rise of the best net value in the posterior mean (Frazier 2009, discrete)."""
    b = cfg["model"]["benefit_per_pass"]
    p = min(max(mean[j], 0.02), 0.98)
    var_obs = p * (1 - p) / cfg["model"]["runs_per_step"]
    scale = cov[:, j] / math.sqrt(cov[j, j] + var_obs)
    z, w = np.polynomial.hermite_e.hermegauss(nodes)
    w = w / w.sum()
    best_after = np.array([np.max(value + b * scale * zi) for zi in z])
    return float(w @ best_after - value.max())


def thompson(cfg, upto, rng):
    """Independent Beta posteriors: P(best) of each arm in net value, and the expected value of perfect information."""
    arms = cfg["arm"]
    k, n = counts(cfg, upto)
    b = cfg["model"]["benefit_per_pass"]
    cost = np.array([cost_of(a, cfg) for a in arms])
    draws = np.stack([rng.beta(k[a["id"]] + 1, n[a["id"]] - k[a["id"]] + 1, cfg["model"]["thompson_draws"])
                      for a in arms], axis=1)
    value = b * draws - cost
    best = np.bincount(value.argmax(1), minlength=len(arms)) / len(value)
    evpi = float(value.max(1).mean() - value.mean(0).max())
    return best, evpi


def choose(cfg, upto):
    """The arm each policy picks given the runs up to stage `upto`, with its expected gain per future run and its step cost."""
    arms = cfg["arm"]
    m = cfg["model"]
    mean, cov = posterior(cfg, upto)
    sd = np.sqrt(np.clip(np.diag(cov), 0, None))
    cost = np.array([cost_of(a, cfg) for a in arms])
    value = m["benefit_per_pass"] * mean - cost
    best = value.max()
    ei = np.array([expected_improvement(value[i], m["benefit_per_pass"] * sd[i], best) for i in range(len(arms))])
    kg = np.array([knowledge_gradient(mean, cov, j, value, cfg) for j in range(len(arms))])
    sc = np.array([step_cost(a, cfg) for a in arms])
    ucb = value + m["benefit_per_pass"] * m["ucb_beta"] * sd
    k, n = counts(cfg, upto)
    total = sum(n.values())
    ucb1 = np.array([math.inf if n[a["id"]] == 0 else
                     m["benefit_per_pass"] * (k[a["id"]] / n[a["id"]] + math.sqrt(2 * math.log(total) / n[a["id"]]))
                     - cost[i] for i, a in enumerate(arms)])
    # Unobserved arms all tie at infinity: the cheapest goes first.
    ucb1_pick = min((i for i in range(len(arms)) if math.isinf(ucb1[i])), key=lambda i: cost[i], default=int(ucb1.argmax()))
    pbest, evpi = thompson(cfg, upto, np.random.default_rng(m["seed"]))
    picks = {"EI": (int(ei.argmax()), ei), "EI per cost": (int((ei / np.maximum(sc, 1e-9)).argmax()), ei),
             "knowledge gradient": (int(kg.argmax()), kg), "GP-UCB": (int(ucb.argmax()), kg),
             "UCB1": (ucb1_pick, None), "Thompson": (int(pbest.argmax()), None)}
    rows = []
    for name in POLICIES:
        i, gain = picks[name]
        g = float(gain[i]) if gain is not None else evpi
        rows.append({"policy": name, "arm": arms[i]["id"], "gain_per_run": g, "gain": g * m["future_runs"],
                     "step_cost": float(sc[i]), "stop": g * m["future_runs"] < sc[i],
                     "break_even_runs": sc[i] / g if g > 0 else math.inf})
    return rows, {"mean": mean, "sd": sd, "value": value, "cost": cost, "ei": ei, "kg": kg, "pbest": pbest, "evpi": evpi}


def leave_one_out(cfg, upto):
    """Predict each seen arm from the others; return (arm, observed rate, predicted mean, predicted sd, z)."""
    k, n = counts(cfg, upto)
    arms = cfg["arm"]
    out = []
    for i, a in enumerate(arms):
        if n[a["id"]] == 0:
            continue
        mean, cov = posterior(cfg, upto, drop=a["id"])
        obs = k[a["id"]] / n[a["id"]]
        s = math.sqrt(max(cov[i, i], 1e-12))
        out.append((a["id"], obs, float(mean[i]), s, (obs - mean[i]) / s))
    return out


def report(cfg):
    m = cfg["model"]
    lines = []
    for stage in (1, 2, 3):
        rows, info = choose(cfg, stage)
        k, n = counts(cfg, stage)
        lines.append(f"Stage {stage}: {sum(n.values())} runs in {sum(1 for v in n.values() if v)} arms")
        lines.append("| Policy | Next step | Gain over the future runs (tokens) | Cost of the step (tokens) | Stop? | Break-even future runs |")
        lines.append("|---|---|---|---|---|---|")
        for r in rows:
            be = "never" if math.isinf(r["break_even_runs"]) else f"{r['break_even_runs']:.0f}"
            lines.append(f"| {r['policy']} | {r['arm']} | {r['gain']:.0f} | {r['step_cost']:.0f} | "
                         f"{'yes' if r['stop'] else 'no'} | {be} |")
        lines.append("")
    rows, info = choose(cfg, 3)
    arms = cfg["arm"]
    lines.append("Posterior after stage 3 (pass rate, net value per run in tokens, probability of being the best arm)")
    lines.append("| Arm | Runs | Mean | SD | Net value | P(best), independent arms |")
    lines.append("|---|---|---|---|---|---|")
    k, n = counts(cfg, 3)
    for i, a in enumerate(arms):
        lines.append(f"| {a['id']} | {k[a['id']]}/{n[a['id']]} | {info['mean'][i]:.2f} | {info['sd'][i]:.2f} | "
                     f"{info['value'][i]:.0f} | {info['pbest'][i]:.2f} |")
    lines.append("")
    lines.append("Leave one arm out, stage 3: observed rate against the surrogate's prediction")
    lines.append("| Arm | Observed | Predicted | SD | z |")
    lines.append("|---|---|---|---|---|")
    for arm, obs, pred, s, z in leave_one_out(cfg, 3):
        lines.append(f"| {arm} | {obs:.2f} | {pred:.2f} | {s:.2f} | {z:+.1f} |")
    lines.append("")
    lines.append("Sensitivity of the stage 3 choice to the benefit of a pass (tokens)")
    lines.append("| Benefit per pass | EI | knowledge gradient | Thompson | Stop (KG) |")
    lines.append("|---|---|---|---|---|")
    for b in (10_000, 100_000, 1_000_000):
        c = {**cfg, "model": {**m, "benefit_per_pass": b}}
        r, _ = choose(c, 3)
        d = {x["policy"]: x for x in r}
        lines.append(f"| {b} | {d['EI']['arm']} | {d['knowledge gradient']['arm']} | {d['Thompson']['arm']} | "
                     f"{'yes' if d['knowledge gradient']['stop'] else 'no'} |")
    return "\n".join(lines)


if __name__ == "__main__":
    print(report(load(sys.argv[1] if len(sys.argv) > 1 else None)))
