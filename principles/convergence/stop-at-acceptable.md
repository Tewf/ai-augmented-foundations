# Stop at acceptable, with the optimum as a bound

**Claim:** a project stops when a written criterion of done passes and the gap to the optimum is within a tolerance stated beforehand; the optimum is a bound, not a goal.

- **Grade:** supported with caveat for algorithms (Zilberstein 1996, secondary); measured, correlational, for satisficing on consumer choices (Schwartz 2002, secondary); convention, untested, for document collections, where one case supports it.
- **Evidence:** [convergence review](../../evidence/convergence/review.md), strands 1, 3, 5 and 6 (Simon 1956, Zilberstein 1996, Russell 1995, Schwartz 2002, Candela 2016, OR-Tools 2026, Schwaber 2020).
- **Derived in:** [Bayesian optimisation review](../../evidence/bayesian-optimisation/review.md), strands 2 and 6, and [decision 0005](../../decisions/0005-the-project-as-optimisation-of-an-unknown-objective.md).
- **Also read:** [state of the art](../../evidence/convergence/state-of-the-art.md), rows V1 and V2; [position](../../evidence/convergence/position.md); [baseline](../../evidence/convergence/baseline.md) and the runs in [runs.toml](../../evidence/convergence/runs.toml); [against](../../evidence/convergence/against.md).
- **Check:** `optimality-gap` (exact: for each recorded run, the gap is arithmetic that holds, an accepted run has a written criterion and a tolerance, and its gap is within the tolerance or carries a waiver).
- **Reader styles:** none.

## What it asks

- Write the criterion of done before the search: the checks that must pass.
- State a tolerance on the optimality gap before running an exact search. The gap is (objective minus bound) over objective.
- Record each run with its objective, its proved bound and its status, so that a feasible result is told from an optimal one.
- Stop when the criterion passes and the gap is within the tolerance. A result accepted past the tolerance says why.

## Derivation

- A step is worth what it is expected to change in the best decision (Howard 1966; Frazier 2009), and it costs tokens, time or money.
- Stop when the expected gain over the uses still to come is below the cost of one step. The surrogate supplies the distribution of the gain (Makarova 2022).
- The written criterion and the gap tolerance are the tests of that rule that a program can run today. The expected gain itself is a model, and [the worked model](../../evidence/bayesian-optimisation/worked-model.md) shows how much a guess moves it.
- The grade does not change: the proofs assume normal beliefs and known noise.

## Why

- Stopping at a result above an aspiration level is a model with a name, satisficing (Simon 1956), and a formal sibling, bounded optimality (Russell 1995). The field has the frame this needs: a profile of quality against time, and the choice of when to stop as a decision.
- The optimum can answer another question than the owner's: one run's optimum and the owner's tree were grouped differently ([baseline](../../evidence/convergence/baseline.md)). For code, Candela 2016 asks whether developers pursue the cohesion-coupling optimum (secondary).
- A bound is useful even when the optimum is not wanted: a time-limited solver returns either a proved optimum or a feasible result with a gap, so the distance is known (OR-Tools 2026).

## Limits

- One case supports this for a document collection. It is not a general result, and the repository cannot claim that acceptable beats optimal.
- The classic stopping rules need a known distribution of what the next look will bring. A project has none for its next restructuring, and the rule found for the unknown case needs a surrogate, which is only as good as its fit ([against](../../evidence/convergence/against.md); [Bayesian optimisation](../../evidence/bayesian-optimisation/against.md)).
- Satisficing is a model of what people do, and a trait measured on consumers does not show that a maximiser's results are worse.
- Several wanting parties give a front of trade-offs, and choosing a point on it is a social choice (Arrow 1950): `optimality-gap` checks one objective.
- The tolerance in `checks/config.toml` is PROVISIONAL, and the check cannot tell that it was fixed before the search.
