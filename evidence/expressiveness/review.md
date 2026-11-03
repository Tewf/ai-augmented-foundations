# Review: what the literature says, by strand

Step 2. Surveys first, then the works they lead to. Numbers come from abstracts or records unless a source is named as read in part, and are marked (secondary). Grades: measured, supported with caveat, convention, not supported.

**Shape:** [review](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/review.md)

## Strand 0: existing reviews

- No review of the expressiveness of a tree of topics was found.
- Closest are Angles 2008 (graph database models), Bodlaender 1998 (graphs of bounded treewidth), Sweller 1998 and Paas 2003 (cognitive load). None speaks of topics.

## Strand 1: hierarchical decomposition as a formal language

- Erol 1994 shows that the complexity of HTN planning varies with the conditions put on the task networks (secondary).
- Höller 2014 studies the plans an HTN problem generates, as a language (secondary).
  - Such languages are always context-sensitive.
  - Some subclasses are regular or context-free.
  - A class with preconditions and effects omitted lies strictly between context-free and context-sensitive.
- Reading for this repository: a hierarchy that decomposes tasks is not a free-for-all. It has a place in the Chomsky classes, and the place sets what a program can check.
- Grade: supported with caveat. Proved for planning problems, applied to topics by analogy.
- The schema side is the topic's: Murata 2005 classes DTD, XML Schema and RELAX NG as local, single-type and regular tree languages (secondary).

## Strand 2: how tree-like a graph is

- Bodlaender 1998 is a survey of graphs with bounded treewidth. A tree decomposition covers a graph by groups of nodes arranged in a tree; the width is the largest group minus one (frame).
- Courcelle 1990 gives a logic of graphs (MSO) whose statements are recognisable on sets of finite graphs (secondary).
- Reading for this repository: treewidth is the field's measure of how far a graph is from a tree. A tree has width 1. A clique of n nodes has width n minus 1.
- The cheaper number is the **cyclomatic number**. Any spanning forest of a graph leaves out exactly m minus n plus c edges. A tree plus that many reference edges encodes the graph. This is an elementary fact, not a finding.
- Grade: supported with caveat for treewidth (theorems, abstracts only); the cyclomatic count is exact by construction.
- Sharing: Bousquet-Mélou 2014 studies XML trees written as DAGs that share equal subtrees (secondary, title and record). The saving is the topic's finding.
- Gima 2024 (letter, abstract) gives a lower bound on treewidth from the second smallest eigenvalue of the graph's Laplacian. It slightly improves an earlier bound of the same kind from 2003 (secondary).
- Reading: the abstract gives a computable lower bound on treewidth, not the width itself. Grade: proved, for graphs; a bound on a graph is not a cost for a reader.

## Strand 3: graph models in practice

- Angles 2008 surveys models in which schema and instances are graphs, with their query languages and integrity constraints (secondary).
- Miles 2009 (grey, 16 of 20 after a second rating) is the W3C model for thesauri. It has `broader` and `narrower` for hierarchy and `related` for links that are not hierarchy, and a separate transitive property for `broader`.
- Reading: practice with the widest standard adoption in this pass keeps a tree and adds links beside it, as the family does.
- Grade: convention, untested. A standard's design is not a study.

## Strand 4: cognitive cost

- Cowan 2001: working memory holds three to five chunks, not seven (secondary). Grade: measured, many experiments.
- Sweller 1998 and Paas 2003 review cognitive load theory and its measurement (secondary, records and abstract).
- Scalabrino 2021: 121 metrics, 444 human ratings from 63 developers. None captured code understandability (secondary). Grade: measured, a negative result for code.
- Muñoz Barón 2020: a meta-analysis of about 24,000 ratings of 427 snippets. Cognitive Complexity correlates with comprehension time and subjective ratings, with mixed results for correctness (secondary). Grade: measured, code only.
- Campbell 2023 (grey, 11 of 20 after a second rating) defines Cognitive Complexity: a count that adds for each break in linear flow and adds more for each level of nesting. The author's company sells the tool that reports it.
- Krieglstein 2022 (meta-analysis of four subjective load questionnaires): internal consistency is satisfactory. Correlations among the three load types partly contradict the theory (secondary, abstract). Grade: measured, in multimedia learning, not on topics.
- Quintero-Manes 2024: a Spanish instrument for three kinds of load, validated by factor analysis on 1,162 students (secondary, abstract). Grade: measured, self-report, programming students.
- Ledneva 2021: in digital text, fewer navigation cues raised scan-path complexity, search time and fixations, in 20 participants (secondary, abstract). Grade: supported with caveat, one small experiment on navigation.
- Berssanette 2021: a systematic review of cognitive load theory in programming teaching (abstract, read in part). Grade: supported with caveat, a review of use, not of validity.
- Reading: a program can count depth and breadth of a tree of topics today. Whether the count predicts a reader's effort has not been tested for topics. For code, one count has partial support and a broad set had none. The forward citations add that self-report load has reliable scales and a validated instrument for programming, while their validity is partly contradicted. None of the sources tests a count on topics.
