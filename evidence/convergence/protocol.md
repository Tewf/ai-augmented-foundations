# Protocol: how the pool on convergence was built

Below are the strings and counts behind the convergence pool, with the terms in [frame](frame.md) and the included works in [sources](sources.md). Rules common to both topics: [method](../README.md#method).

## 1. Why grey literature

Answers yes to questions 1 to 6 of Garousi 2019, Table 4 (question 7 not measured). The meaning of done is set in practice guides, no study of stopping a documentation project was found, and the solver statuses are documented by the solver's makers.

## 2. Questions

V1 to V4 of [frame](frame.md).

## 3. Existing reviews

- Surveys met and used: Ferguson 1989 (secretary problem), Zilberstein 1996 (anytime algorithms), Marler 2004 (multi-objective methods), Silva 2017 (definition of done, systematic review), Cohen-Addad 2019 (hierarchical clustering objectives, linked).
- No review joining stopping, anytime behaviour and file or topic structure was found.

## 4. Formal search

Counts were taken on 2026-11-02 by the method in the evidence README.

| Id | String | OpenAlex | arXiv | Result |
|---|---|---|---|---|
| V1 | satisficing | 4660 | 156 | Simon 1956 and Schwartz 2002 by the lists; survey noise |
| V2 | bounded rationality | 12661 | 428 | Simon 1955 |
| V3 | secretary problem | 843 | 203 | Ferguson 1989 |
| V4 | optimal stopping | 5665 | 941 | noise: finance and statistics; Weitzman 1979 by title |
| V5 | anytime algorithm | 918 | 145 | Dean 1988, Zilberstein 1996 |
| V6 | metareasoning | 285 | 26 | Russell 1991 |
| V7 | bounded optimality | 369 | 159 | Russell 1995 |
| V8 | resource-rational analysis | 43 | 2 | Lieder 2020 |
| V9 | multi-objective optimization | 83334 | 2274 | Deb 2002 |
| V10 | Pareto front | 19296 | 1135 | no concept added after 5 results |
| V11 | next release problem | 140 | 9 | Bagnall 2001, Zhang 2007 |
| V12 | software module clustering | 97 | 3 | Praditwong 2011, linked |
| V13 | hierarchical clustering objective | 9 | 4 | Hogemo 2021; Cohen-Addad 2019 |
| V14 | definition of done | 130 | 9 | Silva 2017 |
| V15 | optimality gap | 3973 | 927 | noise: other fields |
| V16 | CP-SAT | 870 | 93 | no concept added; solver documents are grey |
| V17 | social choice impossibility | 8 | 0 | Arrow 1950 recalled by name |

- Zero or low counts from strings that were too specific: "multi-objective optimization survey" (1), "optimum release time software" (1). The first was widened to V9. The second was dropped: one result.
- Snowballing: Dasgupta 2016, Mitchell 2006 and Candela 2016 were taken from the maintainer's earlier public-source list of clustering work and verified by DOI against Crossref.

## 5. Grey search

- By producer: the Scrum Guide for done, and the documentation of the constraint solver for the statuses a time-limited run returns.
- Not searched: forums, Q/A sites, blogs on time-boxing, project-management standards (PMBOK, ISO 21500). Practice here is a sample of two.

## 6. Stopping, selection, scoring, synthesis and limits

As in the evidence README. The stopping rule ended the strings V4, V10, V15 and V16. The scores of grey sources are in [sources](sources.md).

## 7. Forward citations (2026-11-03)

Six sources are cited twice in the review. Three seeds were chosen among them: Ferguson 1989, Zilberstein 1996 and Silva 2017. Each is a review of its field with a large body of citing work. Citing works were listed from OpenAlex, filtered to works published after 2019.

| Id | Seed | Filter on citing works | Matching and screened by title |
|---|---|---|---|
| F1 | Ferguson 1989 | published after 2019 | 181 |
| F2 | Zilberstein 1996 | published after 2019 | 137 |
| F3 | Silva 2017 | published after 2019 | 35 |

- Total: 353 citing works, all screened by title. Five abstracts were opened. Four works were added: Correa 2023 and Baumann 2022 (from F1), Svegliato 2020 and Sung 2021 (from F2). Nothing from F3 was added.
- The one work not added, a 2022 survey study of the definition of done, has an empty abstract in the records read.
- Each added work changes or sharpens a finding in [review](review.md), strand 1, 2 or 3, or in [against](against.md) and [position](position.md). Every number read from an abstract is marked secondary.
- Not searched: citing works before 2020, other seeds, a second index.

## 8. A second rater on the grey sources (2026-11-03)

The method is the one in section 8 of the [expressiveness protocol](../expressiveness/protocol.md), which also holds the agreement figures for all four grey sources. The rows for this topic follow.

| Source | Review, first | Second rater: A, M, O, D, P, N, I, T | Second rater, total | Difference | Review, after |
|---|---|---|---|---|---|
| Schwaber 2020 | 13.5 | 0, 1, 0, 1, 0, 0, 0, 1 | 3 | 10.5 | 10 |
| OR-Tools 2026 | 12.5 | 0, 3, 0, 1, 0, 0, 0, 1 | 5 | 7.5 | 12 |

Rereading, with the reason:

- **Schwaber 2020, O 3 to 1:** the guide is a rule set by the authors of the method, who teach it. It states no data and no limits, so O3 and O4 do not hold.
- **Schwaber 2020, P 1 to 0:** the guide discusses no related source. It says that other descriptions of tactics exist elsewhere and names none.
- **Schwaber 2020, N 1 to 0.5:** it is the definition of the method, adding to the field's practice only in part.
- **OR-Tools 2026, N 1 to 0.5:** the page documents a list of solver statuses with a small example. It adds little beyond the solver's other pages.
- **OR-Tools 2026, D stays 1:** the page prints "Last updated 2024-08-28". The bibliography said the page was undated, which was wrong, and is corrected.


Agreement over the four sources of both topics: [expressiveness protocol](../expressiveness/protocol.md), section 8.

Agreement for this topic alone: mean absolute difference 9, both sources above the threshold for the review and below it for the second rater.
