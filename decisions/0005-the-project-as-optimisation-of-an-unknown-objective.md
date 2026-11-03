# 0005: The project as the optimisation of an unknown objective

**Decision:** The repository reads a project as the optimisation of an unknown objective. The stopping rule is derived from the value of information: stop when the expected gain is below the cost of a step.

**Status:** accepted, 2026-11-03. Supersedes the framing of the [convergence frame](../evidence/convergence/frame.md), which framed only the stopping rule. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/shapes/decision-record.md).

## Context

- The maintainer's framing is a study whose goal is to maximise a function nobody knows: gather data, let several agents each build an estimate, then take the next step.
- The convergence review framed stopping as satisficing and anytime behaviour, and found no rule for one run with an unknown distribution.
- The [Bayesian optimisation review](../evidence/bayesian-optimisation/README.md) found the field's name for the whole loop, and a stopping rule that uses the surrogate as the distribution (Makarova 2022).
- The family's own experiments are sequential: the brief test in two rounds, then the method comparison. Each is a step of the loop.

## Decision

- **The frame is Bayesian optimisation:** a surrogate, an acquisition function and a stopping rule, with cost and cheap evaluators as extensions.
- **The stopping rule stays, now derived.** A project stops when the expected gain over the remaining use is below the cost of a step. The written criterion of done and the tolerance on the gap remain the tests a program can run.
- **The principle [stop at acceptable](../principles/convergence/stop-at-acceptable.md) gains the derivation** and keeps its grade. The review earned no stronger grade: the proofs assume normal beliefs and known noise, and one toy model on eight points is not a test.
- **No new principle is added.** The card in [standard.md](../standard.md) is unchanged.
- **The baseline is named:** a Gaussian-process surrogate with noisy expected improvement, UCB1 as the simpler policy, random search as the null, and the terminator of Makarova 2022 for the stop ([baseline](../evidence/bayesian-optimisation/baseline.md)).
- **The topic folder is named `bayesian-optimisation`,** the field's word, in place of `next-step`.

## Consequences

- The convergence topic points to the new topic; its findings stand.
- A later experiment can be planned as a step: its cost, the gain it could bring and the policy that chose it are written before the run.
- **Bad:** the worked model rests on eight points, a guessed kernel and the maintainer's value of a pass. Its stop flips at 237 future runs.
- **Bad:** no reference implementation was run, so the model's choices agree with none yet.
- **Not chosen:** a new principle graded convention, which would add a rule with nothing to check; and leaving the convergence framing as it was, which would keep the stop without its derivation.

## See also

[Decisions](README.md); [the review](../evidence/bayesian-optimisation/README.md); [the worked model](../evidence/bayesian-optimisation/worked-model.md); [0004](0004-which-findings-became-principles.md).
