# Frame: how fast a project converges, to what, and what an optimum is

Step 1, read on 2026-11-02: the problem, the terms, and the names the field uses.

## The problem in one sentence

When a project built from a tree of topics should stop, given that it can accept a result or search on for the best, and that readers, writers and checkers want different things.

## Names

| Term | What the field means by it | Source |
|---|---|---|
| **satisficing** | choosing the first option that meets an aspiration level instead of searching for the best | Simon 1956 |
| **bounded rationality** | rational choice under limits of information and computation | Simon 1955 |
| **optimal stopping** | choosing the moment to stop a sequence of observations to maximise a reward | Ferguson 1989 |
| **secretary problem** | the classic stopping problem: accept or reject candidates in order, with no recall | Ferguson 1989 |
| **reservation value** | the threshold above which searching stops, in a search with a cost per look | Weitzman 1979 |
| **anytime algorithm** | an algorithm that returns a result whose quality grows with the time it is given | Dean 1988; Zilberstein 1996 |
| **performance profile** | the curve of expected quality against computation time | Zilberstein 1996 |
| **metareasoning** | reasoning about how long to reason | Russell 1991 |
| **bounded optimality** | the best program a given machine can run, not the best action in the abstract | Russell 1995 |
| **resource-rational analysis** | modelling a mind as the best use of limited computation | Lieder 2020 |
| **maximiser**, satisficer | a person who seeks the best, a person who accepts good enough | Schwartz 2002 |
| **Pareto optimum** | a result no objective can improve without another getting worse | Marler 2004 |
| **multi-objective optimisation** | optimisation of several objectives kept apart, giving a front of trade-offs | Deb 2002; Marler 2004 |
| **optimality gap** | the distance between the best result found and a proved bound on the optimum | OR-Tools 2026 |
| **definition of done** | a formal description of the state a result must reach to count as finished | Schwaber 2020 |
| **Dasgupta cost** | a cost of a hierarchy over pairwise similarities: each pair pays the size of the smallest cluster holding both | Dasgupta 2016 |
| **social choice** | the aggregation of several people's rankings into one | Arrow 1950 |

## What practice calls it

- Practitioners say **good enough**, **done** and **definition of done**, **time-box** and **diminishing returns**. The field says satisficing, stopping rule and anytime algorithm.
- Practitioners say **trade-off** and **stakeholder conflict**. The field says multi-objective optimisation and the next release problem (Bagnall 2001).

## The repository's name against the field's

- The repository says **converges** and **optimum**. Convergence in the field is a property of an iteration. The nearer names are **anytime behaviour** and **stopping**.
- No rename is proposed. The mismatch is reported.

## Sub-questions

| Id | Sub-question | Answers |
|---|---|---|
| V1 | When does the field say a search for a result should stop? | front page: Done |
| V2 | What does the gap between an exact optimum and what people accept look like? | front page: Acceptable or optimal |
| V3 | What is an optimum with several wanting parties? | front page: Acceptable or optimal |
| V4 | Can a program tell that a project is done? | front page: Done |

## Links, not repeated

- Depth and breadth for a reader are graded in [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/collection/browsable-folders.md).
- The loop whose convergence is asked is [reader-ergonomics-blueprint](https://github.com/Tewf/reader-ergonomics-blueprint).
