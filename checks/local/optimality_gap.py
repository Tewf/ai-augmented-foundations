"""Optimality gap: a run that stops at an acceptable result states its criterion and its tolerance, and the gap holds.

A run of an exact search that was cut short leaves a result (the objective, to be minimised) and a proved lower
bound. The gap is (objective - bound) / objective. The files `[optimality_gap] records` names are TOML files of
`[[run]]` tables, with:

- `name`, `objective`, `bound` (numbers) and `status`, "optimal" or "feasible";
- `accepted` (true when the run's result was taken as done), and then `criterion`, the written test of done;
- `tolerance`, the largest gap accepted, per run or as the default `tolerance` of the config table;
- `waiver`, a sentence saying why a result past the tolerance was accepted anyway.

Rules, each certain (errors):
- the objective is positive and the bound does not pass it (a bound above the result cannot be a lower bound);
- a run marked optimal has a bound equal to its objective;
- an accepted run has a non-empty criterion and a tolerance, stated in the record or in the config;
- an accepted run has a gap within its tolerance, or a waiver.

What a run guarantees: for every record, the arithmetic of the gap and the presence of the criterion and the
tolerance. What it does not: that the criterion is a good test of done, that the bound was proved, or that the
tolerance was fixed before the search began (that last is a commitment the history of the file shows, not a program).
A repository with no records declared has nothing to check, and the check says nothing.
Time O(records).
"""
import tomllib
from pathlib import Path

try:
    from framework.check_api import Finding, files_in_scope, matches_any
except ModuleNotFoundError:  # run by the tests, without the standard's checks on the path
    from dataclasses import dataclass
    import fnmatch

    @dataclass(frozen=True)
    class Finding:
        check: str
        path: str
        line: int
        message: str
        kind: str = "error"

    def files_in_scope(root, config, suffixes=None):
        return sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file())

    def matches_any(path, patterns):
        return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)

NAME = "optimality-gap"
EXACT = True


def gap(objective: float, bound: float) -> float:
    return (objective - bound) / objective


def problems(run: dict, default_tolerance: float | None) -> list[str]:
    """What is wrong with one run, in words; empty when the record is consistent."""
    name = run.get("name", "(unnamed)")
    try:
        objective, bound = float(run["objective"]), float(run["bound"])
    except (KeyError, TypeError, ValueError):
        return [f"{name}: objective and bound must be numbers"]
    if objective <= 0:
        return [f"{name}: the objective must be positive to have a relative gap"]
    found = []
    if bound > objective:
        found.append(f"{name}: the bound {bound:g} is above the objective {objective:g}, so it is not a lower bound")
    if run.get("status") == "optimal" and bound != objective:
        found.append(f"{name}: marked optimal, but the bound {bound:g} differs from the objective {objective:g}")
    if run.get("accepted"):
        tolerance = run.get("tolerance", default_tolerance)
        if not str(run.get("criterion", "")).strip():
            found.append(f"{name}: accepted with no written criterion of done")
        if tolerance is None:
            found.append(f"{name}: accepted with no stated tolerance on the gap")
        elif gap(objective, bound) > tolerance and not str(run.get("waiver", "")).strip():
            found.append(f"{name}: accepted at a gap of {gap(objective, bound):.3f}, past the tolerance {tolerance:g}, with no waiver")
    return found


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("optimality_gap", {})
    patterns = settings.get("records", [])
    default = settings.get("tolerance")
    findings = []
    for path in files_in_scope(root, config, {".toml"}):
        if not matches_any(path, patterns):
            continue
        try:
            data = tomllib.loads((root / path).read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as error:
            findings.append(Finding(NAME, path, 0, f"not valid TOML: {error}"))
            continue
        for run in data.get("run", []):
            findings += [Finding(NAME, path, 0, message) for message in problems(run, default)]
    return findings
