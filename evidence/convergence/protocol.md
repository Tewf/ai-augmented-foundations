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
