"""Replay of the guide on the family's trace of two days: which next step each policy would propose, and where the value
of information would have stopped it.

The trace is trace.toml, one row per job. An arm is a kind of job (setup, review, audit, design, build, experiment,
upkeep). Before each wave of jobs the policies see only the rows of earlier waves, propose one kind, and the proposal is
compared with the kinds the maintainer ran in that wave. Standard library only; run: python3 replay.py [--outcome moved|kept]
Every tunable is in trace.toml's sibling table below and is PROVISIONAL. A replay on one trace proves little.
"""
import argparse
import math
import random
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent
KINDS = ("audit", "build", "design", "experiment", "review", "setup", "upkeep")
POLICIES = ("random", "greedy", "UCB1", "Thompson", "KG per cost")

# PROVISIONAL: nothing sets these; the write-up shows what moves when they move.
BENEFIT = 600.0         # thousands of tokens one step that moved something is worth (about 2.6 agent jobs)
PRIOR_COST = 230.0      # thousands of tokens of one agent run when no row of the history gives a cost
DRAWS = 2000            # Thompson draws
SEED = 20261103
METER_POINTS = 15.0     # weekly-meter points the two days moved (12 to 27, all models), spread by tokens: crude


def load(path=None):
    with open(path or HERE / "trace.toml", "rb") as f:
        return tomllib.load(f)["job"]


def family(jobs):
    return [j for j in jobs if j.get("in_family", True)]


def cost(job):
    """Thousands of tokens the job's agents spent on the subscription."""
    return job["agents"] * job["tokens_k"]


def outcome(job, which):
    return job.get(which)


class Belief:
    """What the history says of one arm: a Beta belief on the chance a step of it has the outcome, and a mean cost."""

    def __init__(self, kind, history, which, default_cost):
        rows = [j for j in history if j["kind"] == kind]
        seen = [j for j in rows if outcome(j, which) is not None]
        self.kind = kind
        self.a = 1.0 + sum(outcome(j, which) for j in seen)
        self.b = 1.0 + sum(1 - outcome(j, which) for j in seen)
        self.runs = len(rows)
        self.cost = sum(cost(j) for j in rows) / len(rows) if rows else default_cost

    @property
    def mean(self):
        return self.a / (self.a + self.b)

    @property
    def value(self):
        """Posterior mean of the net value of one step: benefit times the chance, minus the cost."""
        return BENEFIT * self.mean - self.cost


def beliefs(history, which):
    fam = [j for j in history]
    default = sum(cost(j) for j in fam) / len(fam) if fam else PRIOR_COST
    return [Belief(k, history, which, default) for k in KINDS]


def best_value(bs):
    return max(b.value for b in bs)


def knowledge_gradient(bs, i):
    """Expected rise of the best posterior net value after one step of arm i (exact, two outcomes)."""
    b = bs[i]
    p = b.mean
    others = max([x.value for j, x in enumerate(bs) if j != i], default=-math.inf)
    total = 0.0
    for y, prob in ((1, p), (0, 1 - p)):
        new_mean = (b.a + y) / (b.a + b.b + 1.0)
        new_value = BENEFIT * new_mean - b.cost
        total += prob * max(new_value, others)
    return total - best_value(bs)


def propose(policy, bs, history, rng):
    n_total = max(1, sum(b.runs for b in bs))
    if policy == "greedy":
        return max(bs, key=lambda b: (b.value, -KINDS.index(b.kind))).kind
    if policy == "UCB1":
        def index(b):
            if b.runs == 0:
                return (math.inf, -b.cost, -KINDS.index(b.kind))
            return (b.value + BENEFIT * math.sqrt(2 * math.log(n_total) / b.runs), 0, -KINDS.index(b.kind))
        return max(bs, key=index).kind
    if policy == "Thompson":
        wins = [0] * len(bs)
        for _ in range(DRAWS):
            vals = [BENEFIT * rng.betavariate(b.a, b.b) - b.cost for b in bs]
            wins[vals.index(max(vals))] += 1
        return bs[wins.index(max(wins))].kind
    if policy == "KG per cost":
        gains = [knowledge_gradient(bs, i) / b.cost for i, b in enumerate(bs)]
        return bs[gains.index(max(gains))].kind
    raise ValueError(policy)


def stop_verdict(bs, remaining):
    """The value-of-information stop: no step pays back its cost over the jobs still to come."""
    kgs = [knowledge_gradient(bs, i) for i in range(len(bs))]
    worth = [kg * remaining - b.cost for kg, b in zip(kgs, bs)]
    i = max(range(len(bs)), key=lambda j: worth[j])
    return {"arm": bs[i].kind, "gain": kgs[i] * remaining, "cost": bs[i].cost, "stop": worth[i] <= 0,
            "exploit_only": best_value(bs) <= 0}


def waves(jobs):
    return sorted({j["wave"] for j in jobs})


def replay(jobs, which="moved"):
    """One record per wave from the second on: the history, each policy's proposal, the kinds the maintainer ran."""
    fam = family(jobs)
    out = []
    for w in waves(fam)[1:]:
        history = [j for j in fam if j["wave"] < w]
        nxt = [j for j in fam if j["wave"] == w]
        bs = beliefs(history, which)
        rng = random.Random(SEED + w)
        remaining = len([j for j in fam if j["wave"] >= w])
        ran = sorted({j["kind"] for j in nxt})
        rec = {"wave": w, "ran": ran, "jobs": len(nxt), "tokens": sum(cost(j) for j in nxt),
               "stop": stop_verdict(bs, remaining), "best": max(bs, key=lambda b: b.value).kind, "proposal": {}, "step_cost": {}}
        for p in POLICIES:
            if p == "random":
                rec["proposal"][p] = None
                continue
            kind = propose(p, bs, history, rng)
            rec["proposal"][p] = kind
            rec["step_cost"][p] = next(b.cost for b in bs if b.kind == kind)
        out.append(rec)
    return out


def hit(rec, policy):
    """1 if the policy's proposed kind is among the kinds run in the wave. For random, the expected hit chance."""
    if policy == "random":
        return len(rec["ran"]) / len(KINDS)
    return 1.0 if rec["proposal"][policy] in rec["ran"] else 0.0


def agreement(records):
    return {p: sum(hit(r, p) for r in records) for p in POLICIES}


def disagreed_tokens(jobs, records):
    """Per policy: thousands of tokens of the jobs whose kind the policy did not propose before their wave."""
    fam = family(jobs)
    res = {}
    for p in POLICIES:
        if p == "random":
            continue
        total = 0.0
        for r in records:
            total += sum(cost(j) for j in fam if j["wave"] == r["wave"] and j["kind"] != r["proposal"][p])
        res[p] = total
    return res


def missed_cost(records):
    """Per policy: thousands of tokens of the steps it proposed in the waves where the maintainer ran none of that kind."""
    return {p: sum(r["step_cost"][p] for r in records if not hit(r, p)) for p in POLICIES if p != "random"}


def first_stop(records):
    for r in records:
        if r["stop"]["stop"]:
            return r["wave"]
    return None


def stop_ceiling(jobs, wave):
    """Thousands of tokens of every family job from `wave` on: the most that stopping at `wave` could have saved."""
    return sum(cost(j) for j in family(jobs) if j["wave"] >= wave)


def points(tokens, jobs):
    total = sum(cost(j) for j in family(jobs))
    return METER_POINTS * tokens / total


# ---- output -------------------------------------------------------------------------------------------------------

def table(jobs):
    """The trace as a markdown table: design/trace.md holds this text under its header."""
    lines = ["| Wave | Job | Kind | Agents | Tokens (k) | Produced | What it changed | Moved | Kept |",
             "|---|---|---|---|---|---|---|---|---|"]
    for j in jobs:
        tok = f"{cost(j):.0f}" + ("" if j["tokens_source"] == "recorded" else " est.")
        name = j["id"] + ("" if j.get("in_family", True) else " (outside)")
        mv = "" if j.get("moved") is None else str(j["moved"])
        kp = "" if j.get("kept") is None else str(j["kept"])
        lines.append(f"| {j['wave']} | {name} | {j['kind']} | {j['agents']} | {tok} | {j['produced']} | "
                     f"{j['changed']} | {mv} | {kp} |")
    return "\n".join(lines) + "\n"


def by_kind(jobs):
    rows = []
    for k in KINDS:
        js = [j for j in family(jobs) if j["kind"] == k]
        seen = [j for j in js if j.get("moved") is not None]
        rows.append((k, len(js), sum(cost(j) for j in js), sum(j["moved"] for j in seen), len(seen),
                     sum(j["kept"] for j in seen)))
    return rows


def report(jobs, which):
    recs = replay(jobs, which)
    ag = agreement(recs)
    dis = disagreed_tokens(jobs, recs)
    lines = [f"Outcome: {which}. Waves replayed: {len(recs)} (from the second)."]
    lines.append("")
    lines.append("| Wave | Kinds run | Best now | " + " | ".join(p for p in POLICIES if p != "random") + " | Stop? |")
    lines.append("|---|---|---|" + "---|" * 4 + "---|---|")
    for r in recs:
        s = r["stop"]
        cells = []
        for p in POLICIES:
            if p == "random":
                continue
            mark = "yes" if hit(r, p) else "no"
            cells.append(f"{r['proposal'][p]} ({mark})")
        stop = f"{'yes' if s['stop'] else 'no'}: gain {s['gain']:.0f} vs {s['cost']:.0f}"
        lines.append(f"| {r['wave']} | {', '.join(r['ran'])} | {r['best']} | " + " | ".join(cells) + f" | {stop} |")
    lines.append("")
    miss = missed_cost(recs)
    lines.append("| Policy | Hits | Of | Tokens of jobs it did not propose (k) | Cost of its missed proposals (k) |")
    lines.append("|---|---|---|---|---|")
    for p in POLICIES:
        h = ag[p]
        d = "" if p == "random" else f"{dis[p]:.0f}"
        m = "" if p == "random" else f"{miss[p]:.0f}"
        hs = f"{h:.1f}" if p == "random" else f"{h:.0f}"
        lines.append(f"| {p} | {hs} | {len(recs)} | {d} | {m} |")
    fs = first_stop(recs)
    lines.append("")
    if fs is None:
        lines.append("The value-of-information stop never fired.")
    else:
        ceil = stop_ceiling(jobs, fs)
        lines.append(f"The stop first fired before wave {fs}. Ceiling of what it could save: {ceil:.0f}k tokens, "
                     f"about {points(ceil, jobs):.1f} meter points of {METER_POINTS:.0f}.")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outcome", choices=("moved", "kept"), default="moved")
    ap.add_argument("--table", action="store_true", help="print the trace as a markdown table")
    ap.add_argument("--kinds", action="store_true", help="print the totals by kind")
    ap.add_argument("--benefit", type=float, help="override BENEFIT, thousands of tokens a moving step is worth")
    args = ap.parse_args()
    if args.benefit is not None:
        global BENEFIT
        BENEFIT = args.benefit
    jobs = load()
    if args.table:
        print(table(jobs), end="")
    elif args.kinds:
        for row in by_kind(jobs):
            print(row)
    else:
        print(report(jobs, args.outcome), end="")


if __name__ == "__main__":
    main()
