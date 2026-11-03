# Baseline: what this repository's claims on expressiveness are compared against

Step 5. The review is finished because three baselines can be named.

**Shape:** [baseline](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/baseline.md)

## B1: a tree with reference edges

- What it is: the practice of DITA-style maps with reuse by reference, held by the topic's document-model review, and SKOS with broader and related links (Miles 2009).
- How to compare: for a collection of topics, count the reference edges and compare with the cyclomatic number m minus n plus c of the full graph. A collection whose links all fit a spanning tree has none left over.
- Grade of the baseline: convention, untested.

## B2: the language class of the decomposition

- What it is: the classification of hierarchical decomposition problems by formal language (Höller 2014), with complexity by network conditions (Erol 1994).
- How to compare: place a typed tree of topics in the nearest class, and state which checks that class allows.
- Grade: supported with caveat, proved for planning.

## B3: Cognitive Complexity, for the cost

- What it is: the one code metric with a meta-analytic validation (Muñoz Barón 2020), defined by Campbell 2023.
- How to compare: compute a nesting-weighted count over a tree of topics and test it against reader effort. A broad set of 121 metrics failed this test for code (Scalabrino 2021), so the test must be run, not assumed.
- Grade: measured for code, not found for topics.

## What the baseline says today

- Expressiveness: any graph fits a tree plus reference edges, so completeness holds trivially. The real question is what a program can check.
- Cost: no baseline number exists for topics. The first measurement is the test in B3.
