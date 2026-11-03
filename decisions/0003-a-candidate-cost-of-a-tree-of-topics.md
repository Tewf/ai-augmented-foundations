# 0003: A candidate cost of a tree of topics

**Decision:** The cost of a tree of topics is computed from four components, combined as Cognitive Complexity combines nesting and breaks. Every weight is PROVISIONAL.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/shapes/decision-record.md).

## Context

- The expressiveness review found no validated cost of a tree of topics ([review](../evidence/expressiveness/review.md), strand 4).
- Cognitive Complexity is the one code count with a meta-analytic validation (Muñoz Barón 2020, secondary), and it is the baseline B3.
- A measure that is computed can be tested; one that is argued cannot. A weight set by no study must say so.

## Decision

- **Tree:** the model of reader-ergonomics-topic's check. Every markdown file is a topic and its parent is the README of the nearest folder above it. Translations, the contributor guide, the changelog and the checks folder are out.
- **Four components.** Each is the unit the standard already reasons about:
  - depth, the shallow outline;
  - children, browsable folders;
  - the run before the first list or table, signal the structure and overview first;
  - the longest sentence, even information density and shallow nesting.
- **Combination:** a break is a step past what a reader holds for free. It costs 1 plus the depth, as a nested branch does in Cognitive Complexity. A topic also pays its depth. A tree pays the sum.
- **Weights:** all 1.0, thresholds 7 children, 60 words and 35 words, each tagged PROVISIONAL in checks/config.toml. The 60 and the 35 are the topic's summary bound and the family's sentence rule; the 7 is Miller's number, untested for topics.
- **A measure, not a check.** It carries no check name, so the standard's runner skips it. It fails no repository.

## Consequences

- The number can be recomputed on any tree and compared with a reader study when one is run ([the family table](../evidence/expressiveness/cost-on-the-family.md)).
- **Bad:** depth supplies 76 to 90 percent of the cost on the family, so the measure mostly counts levels until the weights are set.
- **Bad:** a long run of prose that is not a list can be a good explanation; the measure cannot tell.
- **Not chosen:** word count alone, which is the baseline the study must beat; and a count of links, which this first version leaves out.

## See also

[Decisions](README.md); [the family table](../evidence/expressiveness/cost-on-the-family.md); [the baseline B3](../evidence/expressiveness/baseline.md).
