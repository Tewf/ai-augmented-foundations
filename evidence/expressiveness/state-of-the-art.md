# State of the art, per sub-question

Two records are kept apart: most adopted (what people use) and best evidence (what a study or theorem gives). Upper bounds (what is achieved) are kept apart from lower bounds (what is impossible).

**Shape:** [state of the art](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/state-of-the-art.md)

| Sub-question | Most adopted | Best evidence | Measured how |
|---|---|---|---|
| X1 What a tree encodes | tree plus links: SKOS broader and related (Miles 2009) | Bodlaender 1998 for how tree-like a graph is | theorems on graphs |
| X2 A problem that needs neither | none found | none found | none |
| X3 Classes of hierarchical decomposition | HTN task networks | Höller 2014: always context-sensitive; Erol 1994: complexity varies with conditions | proofs |
| X4 Cost a program can compute | Cognitive Complexity in industrial tools (Campbell 2023) | Muñoz Barón 2020 for code; Cowan 2001 for the capacity | meta-analysis; experiments |

## Upper bounds (achieved)

- Cognitive Complexity correlates with comprehension time and subjective ratings of understandability, over about 24,000 ratings (Muñoz Barón 2020, secondary).
- A tree plus m minus n plus c reference edges encodes any finite graph with m edges, n nodes and c components. This is exact.

## Lower bounds (impossible, or not shown)

- No set of 121 code metrics captured understandability in 444 ratings (Scalabrino 2021, secondary).
- HTN plan languages are not contained in the context-free languages in general (Höller 2014, secondary).
- No measure of cognitive cost has been validated for a tree of topics. Nothing in this pass tried.

## The two records

- Most adopted: a tree with links beside it. Best evidence: theorems for graphs and experiments for code. They are different records and held by different sources.
