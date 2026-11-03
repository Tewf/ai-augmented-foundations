# Stop at acceptable, with the optimum as a bound

**Claim:** a project stops when a written criterion of done passes and the gap to the optimum is within a tolerance stated beforehand; the optimum is a bound, not a goal.

- **Grade:** supported with caveat for algorithms (Zilberstein 1996, secondary); measured, correlational, for satisficing on consumer choices (Schwartz 2002, secondary); convention, untested, for document collections, where one case supports it.
- **Evidence:** [convergence review](../../evidence/convergence/review.md), strands 1, 3, 5 and 6 (Simon 1956, Zilberstein 1996, Russell 1995, Schwartz 2002, Candela 2016, OR-Tools 2026, Schwaber 2020).
- **Also read:** [state of the art](../../evidence/convergence/state-of-the-art.md), rows V1 and V2; [position](../../evidence/convergence/position.md); [baseline](../../evidence/convergence/baseline.md) and the runs in [runs.toml](../../evidence/convergence/runs.toml); [against](../../evidence/convergence/against.md).
- **Check:** `optimality-gap` (exact: for each recorded run, the gap is arithmetic that holds, an accepted run has a written criterion and a tolerance, and its gap is within the tolerance or carries a waiver).
- **Reader styles:** none.

## What it asks

- Write the criterion of done before the search: the checks that must pass.
- State a tolerance on the optimality gap before running an exact search. The gap is (objective minus bound) over objective.
- Record each run with its objective, its proved bound and its status, so that a feasible result is told from an optimal one.
- Stop when the criterion passes and the gap is within the tolerance. A result accepted past the tolerance says why.

## Why

- Stopping at a result above an aspiration level is a model with a name, satisficing (Simon 1956), and a formal sibling, bounded optimality (Russell 1995). The field has the frame this needs: a profile of quality against time, and the choice of when to stop as a decision.
- The optimum can answer another question than the owner's: one run's optimum and the owner's tree were grouped differently ([baseline](../../evidence/convergence/baseline.md)). For code, Candela 2016 asks whether developers pursue the cohesion-coupling optimum (secondary).
- A bound is useful even when the optimum is not wanted: a time-limited solver returns either a proved optimum or a feasible result with a gap, so the distance is known (OR-Tools 2026).

## Limits

- One case supports this for a document collection. It is not a general result, and the repository cannot claim that acceptable beats optimal.
- The classic stopping rules need a known distribution of what the next look will bring. A project has none for its next restructuring, and no rule was found for the unknown case ([against](../../evidence/convergence/against.md)).
- Satisficing is a model of what people do, and a trait measured on consumers does not show that a maximiser's results are worse.
- Several wanting parties give a front of trade-offs, and choosing a point on it is a social choice (Arrow 1950): `optimality-gap` checks one objective.
- The tolerance in `checks/config.toml` is PROVISIONAL, and the check cannot tell that it was fixed before the search.
