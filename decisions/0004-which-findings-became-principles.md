# 0004: Which findings became principles

**Decision:** Three findings became principles, the ones that give a writer a rule a program can test; the other findings stay findings, and the cost measure becomes a check.

**Status:** accepted, 2026-11-03. Supersedes the last bullet of [0003](0003-a-candidate-cost-of-a-tree-of-topics.md), "A measure, not a check". **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/shapes/decision-record.md).

## Context

- The extension contract asks a card, `standard.md`, built from principle files, each with a claim, a grade, evidence and a check ([extending.md](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/extending.md)).
- The two reviews graded their findings. A principle may not claim more than its review, and `principle-coverage` fails one that names no registered check.
- A finding that gives a writer nothing to do is knowledge, not a rule.

## Decision

Became a principle:

| Finding | Principle | Grade | Check |
|---|---|---|---|
| a tree plus m minus n plus c links encodes any graph | [Links beside the tree](../principles/expressiveness/links-beside-the-tree.md) | exact count; supported with caveat; convention | `links` |
| no cost of a tree of topics is validated | [A computed cost with provisional weights](../principles/expressiveness/computed-cost.md) | measured for code only; untested for topics | `topic-cost`, `provisional-tags` |
| stop at acceptable, the optimum as a bound | [Stop at acceptable, with the optimum as a bound](../principles/convergence/stop-at-acceptable.md) | supported with caveat; convention for documents | `optimality-gap` |

- **Two checks are new.**
  - `topic-cost` is `checks/local/topic_cost.py`, which gains a name and a check function.
  - Its missing tag is an error and its budget a warning, so it fails no repository for its number.
  - `optimality-gap` is `checks/local/optimality_gap.py`, with a record of the three runs the baseline reports.
- **The validated-cost gap is a rule about how to hold a number**, so it is a principle with the finding as its limit, not a finding with no rule.
- **The done criterion and the tolerance** (review finding 5) are inside the third principle, since a check tests them together.

Stayed a finding:

- **Hierarchical decomposition has formal language classes** (Höller 2014, supported with caveat): no writer's rule follows from it.
- **Working memory holds three to five chunks** (Cowan 2001, measured): the standard's rules on depth and breadth already cite it, so it is linked, not copied.
- **Keep the objectives apart and report the front** (Praditwong 2011, supported with caveat for module clustering): the review lists it as a candidate rule, not adopted.
  - Its check would need several objectives, and no run here has them.
- **The field says expressive power and anytime stopping** (the frame step): a naming result.
- **No stopping rule for one run with an unknown distribution, and no problem that fits neither a tree nor a graph**: absences, not graded claims.

## Consequences

- The standard's checks now test three rules in this repository, and CI runs the unit tests of both new checks.
- **Bad:** `topic-cost` warns on a number nobody has validated; the warning says so and `topic_budget` is PROVISIONAL.
- **Bad:** `optimality-gap` cannot tell that a tolerance was fixed before the search; only the history of the file shows it.
- **Not chosen:** a principle for each graded finding, which would turn Cowan 2001 and Höller 2014 into rules with nothing to check; and a card with no principles, which hides what the reviews support.

## See also

[Decisions](README.md); [0003](0003-a-candidate-cost-of-a-tree-of-topics.md); [the card](../standard.md).
