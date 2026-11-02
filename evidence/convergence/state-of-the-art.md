# State of the art, per sub-question

Two records are kept apart: most adopted and best evidence. Upper bounds (achieved) are kept apart from lower bounds (impossible).

| Sub-question | Most adopted | Best evidence | Measured how |
|---|---|---|---|
| V1 When to stop a search | a time-box and a definition of done (Schwaber 2020) | Weitzman 1979, Ferguson 1989: stopping rules under known distributions | theorems |
| V1 Quality against time | solver time limits with a status and a gap (OR-Tools 2026) | Zilberstein 1996: the performance profile | theory, no field study of projects |
| V2 Optimum against what people accept | none | Candela 2016: the cohesion-coupling optimum is not what developers say they balance | 100 systems, 29 developers (secondary) |
| V3 Several wanting parties | a ranked backlog | Marler 2004, Deb 2002: a Pareto front; Arrow 1950: no fair aggregation | surveys, theorems |
| V4 Can a program tell done | a written criterion checked by tests | none for a tree of topics | none |

## Upper bounds (achieved)

- A time-limited solver run returns either a proved optimum or a feasible result with a bound, so a gap is computable.
- Multi-objective methods give a front, not one result (Deb 2002; Praditwong 2011 on 17 systems, secondary).
- Maximisers report less satisfaction than satisficers in 4 studies (Schwartz 2002, secondary).

## Lower bounds (impossible, or hard)

- Minimising the total-depth objective on partition trees is intractable in general (Hogemo 2021).
- No rule that aggregates rankings meets Arrow's fair conditions (Arrow 1950, secondary).
- The classic stopping rules need a known distribution of future observations. No source gives a rule when the distribution is unknown (secondary, from abstracts).

## The two records

- Most adopted: a fixed criterion for done. Best evidence: stopping theorems and anytime theory. They are held by different sources, and neither is a study of document collections.
