# Review: what the literature says, by strand

Step 2. Surveys first. Numbers come from abstracts or records unless stated, and are marked (secondary). Grades: measured, supported with caveat, convention, not supported.

## Strand 0: existing reviews

- Ferguson 1989 reviews the secretary problem and its subfields (secondary).
- Zilberstein 1996 is the overview of anytime algorithms in intelligent systems (secondary, title).
- Marler 2004 surveys multi-objective methods for engineering (secondary, record only).
- Silva 2017 is a systematic review of the definition of done in agile projects (secondary, title).
- No review joins stopping, anytime behaviour and the structure of a document collection.

## Strand 1: satisficing and bounded rationality

- Simon 1955 and Simon 1956 set the idea: a chooser with limited information and computation looks for a result above an aspiration level, not for the best.
- Schwartz 2002: maximisers report less happiness, optimism and life satisfaction, and more regret, than satisficers, in 4 studies (secondary). Grade: measured, correlational, on consumer decisions.
- Baumann 2022: in two studies people adapted their acceptance threshold to the spread of the options and to the length of the sequence. They adapted less than the optimal rule would (secondary, abstract). Grade: measured, laboratory choices.
- Reading: stopping at an acceptable result is a model of choice with a long history, with a cost to the maximiser. People do it with a threshold that moves. It says nothing yet about project structure.

## Strand 2: optimal stopping

- Ferguson 1989: the secretary problem has no recall and a known number of candidates in its classic form.
- Weitzman 1979 treats search with a cost per look and gives a reservation value for each option. Searching stops when the best result so far beats every remaining reservation value (secondary, record only).
- Correa 2023: when the decision maker sees a sample of items first, with each item sampled with probability p, the optimal competitive ratio is found for every p (secondary, abstract). The distribution need not be known, but a sample from it is needed. Grade: proved, for single selection.
- Reading: the classic rules need a known distribution of what the next look will bring. With a sample, a rule exists. A project has neither for the next restructuring. Grade: supported with caveat, theorems with assumptions that do not hold here.

## Strand 3: anytime algorithms and metareasoning

- Dean 1988 analyses planning when the time available changes the value of the plan (secondary, title).
- Zilberstein 1996 gives the anytime algorithm: a result whose quality grows with time, with a profile of quality against time (secondary).
- Russell 1991 treats the choice of when to stop computing as a decision with a value (secondary, title).
- Russell 1995 defines bounded optimality: the best program for a given machine in a given environment (secondary).
- Lieder 2020 applies the same idea to minds (secondary).
- Svegliato 2020: a model-free method, learned by reinforcement, decides when to interrupt an anytime algorithm, with a proof of optimality; it was tested on benchmarks and a mobile robot (secondary, abstract). Grade: proved and measured, for repeated planning tasks.
- Sung 2021: learned stopping rules, model-based and model-free, for anytime motion planners, compared with baselines in simulation (secondary, abstract). Grade: measured in simulation, for robot planning.
- Reading: the field already has the frame this repository needs: quality as a function of time, and stopping as a decision. Grade: supported with caveat for algorithms; for projects, convention.

## Strand 4: several objectives

- Marler 2004 surveys methods. Deb 2002 introduces NSGA-II, with a cost of order M times N squared per generation for M objectives and a population of N (secondary).
- Praditwong 2011 splits cohesion and coupling into separate objectives for module clustering, on 17 real systems (secondary).
- Bagnall 2001 and Zhang 2007 pose the next release problem: which requirements to build when customers want different ones. Zhang 2007 finds NSGA-II suited to it (secondary).
- Arrow 1950: no rule that aggregates several rankings meets a short list of fair conditions (secondary, record only).
- Reading: when readers, writers and checkers differ, the field's answer is a front of trade-offs, not an optimum, and then a choice among its points.

## Strand 5: the cost of a hierarchy, and the maintainer's formulation

- Dasgupta 2016 gives a cost on hierarchies over pairwise similarities. Cohen-Addad 2019 gives an axiomatic account of such objectives, linked.
- Hogemo 2021: the total-depth variant of the partition-tree parameters corresponds to Dasgupta's objective. It is intractable like the maximum-depth ones. It has polynomial algorithms on caterpillars and trees with few leaf neighbours, and a 2-approximation on trees. Read in the arXiv abstract. Grade: proved.
- Mitchell 2006 and Candela 2016 are linked. Candela 2016 asks whether the cohesion-coupling optimum is what developers want, on 100 systems and 29 developers (secondary).
- OR-Tools 2026, grey, 12 of 20 after a second rating (page dated 2024-08-28): the solver returns a status that tells an optimal result from a feasible one when a time limit stops the run.
- The maintainer's practice, written down for this review, is in [baseline](baseline.md).

## Strand 6: done

- Schwaber 2020, grey, 10 of 20 after a second rating: the definition of done is a formal description of the state of an increment that meets the quality measures required. A result that meets it counts as finished.
- Silva 2017 reviews its use (secondary, title only).
- Reading: practice sets done by a criterion fixed beforehand, not by an optimum. A program can test a criterion that is written as a check.
