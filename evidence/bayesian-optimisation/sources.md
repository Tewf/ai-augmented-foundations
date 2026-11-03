# Sources: the pool on Bayesian optimisation

Thirty-nine works were added on 2026-11-03. See [protocol](protocol.md) for the searches and [frame](frame.md) for the terms. A grey source below 10 of 20 is an example of practice only.

## Flow

| Stage | Count |
|---|---|
| Strings run | 18, counted in OpenAlex |
| Opened | the abstract or record of 36 formal works; 3 documentation pages in part |
| Included as new | 39: 36 formal, 3 grey |
| Linked from sibling reviews, not screened again | 3 (Weitzman 1979, Ferguson 1989, Vaccaro 2024) |
| In the review | 42 |

## Formal sources

The Quality column says what was read.

| Key | Kind | Found via | Quality | Used in |
|---|---|---|---|---|
| Shahriari 2016 | formal, survey | B1 | survey; abstract | review 0 |
| Frazier 2018 | formal, tutorial | seed | tutorial; abstract | review 0 |
| Garnett 2023 | formal, book | B1 | textbook; abstract | review 0 |
| Greenhill 2020 | formal, survey | B1 | survey; abstract | review 0, 4 |
| Bubeck 2012 | formal, survey | B5 | survey; abstract | review 0, 3 |
| Lattimore 2020 | formal, book | seed | textbook; record only | review 0, 3 |
| Russo 2018 | formal, tutorial | B18 | tutorial; abstract | review 0, 3 |
| Settles 2009 | formal, survey | B7 | survey; record only | review 0, 4 |
| Chaloner 1995 | formal, survey | B8 | decision-theoretic review; abstract | review 0, 4 |
| Rainforth 2024 | formal, survey | B8 | survey; abstract | review 0, 4 |
| Peherstorfer 2018 | formal, survey | B10 | survey; abstract | review 0, 5 |
| Mockus 1975 | formal, conference | seed | model; record only | review 1 |
| Jones 1998 | formal, journal | seed | method; record only | review 1 |
| Snoek 2012 | formal, conference | recalled | measured on benchmarks; abstract | review 1, 5 |
| Bergstra 2012 | formal, journal | recalled | measured and proved; abstract in part | review 1, against |
| Turner 2021 | formal, competition report | B1 | measured: a held-out challenge; abstract | review 1, state of the art |
| Frazier 2008 | formal, journal | B4 | proved results; abstract | review 2 |
| Frazier 2009 | formal, journal | B4 | proved bound and tests; abstract | review 2 |
| Howard 1966 | formal, journal | recalled | theory; opening of the abstract | review 2 |
| Auer 2002 | formal, journal | B5 | proved regret bounds; record only | review 3 |
| Srinivas 2010 | formal, conference | B6 | proved regret bounds, tested on sensor data; abstract | review 3 |
| Gittins 1979 | formal, journal | recalled | theory; abstract | review 3, 6 |
| Li 2018 | formal, journal | recalled | measured on benchmarks; abstract | review 3, 5 |
| Kennedy 2000 | formal, journal | B9 | model with one example; abstract | review 5 |
| Kandasamy 2016 | formal, conference | B9 | proved regret and tests; abstract | review 5 |
| Lee 2020 | formal, preprint | B14 | measured on 20 problems; abstract | review 5 |
| Xie 2024 | formal, conference | B14 | proved link and tests; abstract | review 5, 6 |
| Makarova 2022 | formal, conference | B12 | measured on tuning problems; abstract | review 6 |
| Nguyen 2017 | formal, conference | B13 | proved regret for EI; abstract in part | review 6 |
| Bogunovic 2016 | formal, conference | B6 | proved regret, tested on two data sets; abstract | review 7 |
| Astudillo 2020 | formal, conference | B15 | method with experiments; abstract | review 7 |
| Liu 2024c | formal, conference | B16 | measured; abstract | review 7 |
| Yang 2023 | formal, conference | B16 | measured on prompts; abstract | review 7 |
| Lu 2024b | formal, preprint | recalled | system with cost per paper; abstract | review 7 |
| Zheng 2023b | formal, benchmark | recalled | measured agreement with humans; abstract | review 7, against |
| Balandat 2020 | formal, conference | recalled | software paper; abstract | review 8 |
| Weitzman 1979 | formal, linked | linked | held by sibling reviews | review 6 |
| Ferguson 1989 | formal, linked | linked | held by sibling reviews | review 6 |
| Vaccaro 2024 | formal, linked | linked | held by the agents review | against |

## Grey sources

Score out of 20 by the eight groups of Garousi 2019, Table 7: authority, methodology, objectivity, date, position, novelty, impact and outlet tier.

| Key | Kind | Found via | Score | Used in |
|---|---|---|---|---|
| BoTorch 2026 | grey tier 2, framework documentation | by producer | 10: 3, 2, 1.5, 1, 0.5, 1, 0.5, 0.5 | review 8, baseline |
| Optuna 2026 | grey tier 2, framework documentation | by producer | 10.5: 3, 2, 2, 1, 0.5, 1, 0.5, 0.5 | review 6, 8 |
| Ax 2026 | grey tier 2, platform documentation | by producer | 8: 3, 1, 1, 1, 0.5, 0.5, 0.5, 0.5 (below 10: an example of practice only) | review 8 |

- The documents are their makers' claims about their own software. None states a limit of its method.
- The Optuna page marks its terminator module as deprecated since version 4.9.0 and planned for removal in 6.0.0, so the stopping rule it implements may leave the main package.

## Left out, with the reason

- Option pricing and finance work on optimal stopping: another field.
- Application papers of a tuner on one data set: no concept added.
- The works listed as found and not added in [protocol](protocol.md), section 4.
