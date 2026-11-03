# The AI-augmented foundations standard

What two reviews of the family's setup found, as far as the evidence goes:

- Can a tree or graph of topics encode a project's problems at a cost a person bears?
- When is a project that runs this way done?

It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/standard.md): read that one first.
This page adds only the three rules the reviews graded, each with its evidence and the check that tests it.

Grades mean what they mean in [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/standard.md#grades): measured, supported with caveat,
convention, not supported. Each principle states its grade and never claims more.

## Principles

<!-- principles:start -->

### Expressiveness: what a tree of topics holds and costs

| Principle | Claim | Grade |
|---|---|---|
| [A computed cost with provisional weights](principles/expressiveness/computed-cost.md) | the cost of a tree of topics is computed by a program, every weight is tagged PROVISIONAL, and no one ranks trees by it until a reader study has validated it. | measured for code only (Muñoz Barón 2020 and Scalabrino 2021, both secondary); untested for topics, where every weight is a guess |
| [Links beside the tree](principles/expressiveness/links-beside-the-tree.md) | a relation the tree of topics does not hold is a typed link beside it, and a tree plus m minus n plus c such links encodes any finite graph. | exact by construction for the count of links; supported with caveat for treewidth, read in abstracts; convention, untested, for keeping a tree and adding links |

### Convergence: when a project stops

| Principle | Claim | Grade |
|---|---|---|
| [Stop at acceptable, with the optimum as a bound](principles/convergence/stop-at-acceptable.md) | a project stops when a written criterion of done passes and the gap to the optimum is within a tolerance stated beforehand; the optimum is a bound, not a goal. | supported with caveat for algorithms (Zilberstein 1996, secondary); measured, correlational, for satisficing on consumer choices (Schwartz 2002, secondary); convention, untested, for document collections, where one case supports it |

<!-- principles:end -->

## Where the evidence is

Every principle links its review in [evidence/](evidence/README.md), and every work cited is listed once in the
[bibliography](evidence/bibliography.md). The choice of which findings became principles is
[decision 0004](decisions/0004-which-findings-became-principles.md).
