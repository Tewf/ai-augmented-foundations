# Protocol: how the pool on Bayesian optimisation was built

Below are the strings and counts behind the pool, with the terms in [frame](frame.md) and the included works in [sources](sources.md). Rules common to the topics: [method](../README.md#method).

## 1. Why grey literature

Answers yes to questions 1 to 6 of Garousi 2019, Table 4 (question 7 not measured). The reference implementations of the policies are software, and their makers document what they implement and how they stop.

## 2. Questions

N1 to N6 of [frame](frame.md).

## 3. Existing reviews

- Surveys and tutorials used, on Bayesian optimisation: Shahriari 2016, Frazier 2018, Garnett 2023 and Greenhill 2020.
- On bandits: Bubeck 2012, Lattimore 2020 and Russo 2018.
- On active learning and experimental design: Settles 2009, Chaloner 1995 and Rainforth 2024.
- On multi-fidelity methods: Peherstorfer 2018.
- No review joins Bayesian optimisation with a loop whose evaluators are agents and whose objective is partly a person's judgment.

## 4. Formal search

Counts were taken on 2026-11-03 from OpenAlex (`title_and_abstract.search`, no key, no account). Works were then verified by title lookup in OpenAlex and by the arXiv API for preprints.

| Id | String | OpenAlex | Result |
|---|---|---|---|
| B1 | Bayesian optimization | 57414 | top by citation was noise (a 1963 least-squares paper); Garnett 2023 and Greenhill 2020 by the list |
| B2 | Bayesian optimisation | 3733 | no concept added |
| B3 | expected improvement | 209091 | noise: other fields; Jones 1998 by title |
| B4 | knowledge gradient | 46836 | noise: medicine and ecology; Frazier 2008 and Frazier 2009 by title |
| B5 | multi-armed bandit | 7768 | Bubeck 2012, Auer 2002 by title |
| B6 | Gaussian process bandit | 382 | Srinivas 2010 |
| B7 | active learning | 432441 | Settles 2009 by title |
| B8 | Bayesian experimental design | 10702 | Chaloner 1995, Rainforth 2024 |
| B9 | multi-fidelity optimization | 12882 | Kandasamy 2016, Kennedy 2000 by title |
| B10 | multifidelity | 1375 | Peherstorfer 2018 |
| B11 | value of information | 1463072 | noise: every field; Howard 1966 by title |
| B12 | optimal stopping Bayesian optimization | 192 | Makarova 2022 |
| B13 | Bayesian optimization stopping criterion | 92 | Nguyen 2017 |
| B14 | cost-aware Bayesian optimization | 523 | Lee 2020, Xie 2024 |
| B15 | Bayesian optimization human preference | 210 | Astudillo 2020 |
| B16 | Bayesian optimization large language model | 867 | Liu 2024c |
| B17 | black-box optimization survey | 365 | no concept added |
| B18 | Thompson sampling | 8975 | Russo 2018 |

- Seeds named by the maintainer: Mockus, Jones, Shahriari, Frazier and Lattimore. Others were recalled by name and verified by record: Kennedy 2000, Gittins 1979, Auer 2002, Bergstra 2012, Snoek 2012 and Howard 1966.
- Not run: forward citations of the surveys, a second index, and Semantic Scholar.
- Found and not added, for the cap of 40: three entropy-search papers, multi-information-source optimisation and non-stochastic best-arm identification.
- Also not added: an earlier tutorial, trust-region optimisation in high dimensions, Bayesian active learning for classification, the original Thompson paper and Lindley's measure of information.
- Not found: a 2023 stopping criterion from the gap of expected minimum simple regrets. Its record did not come up.
- Unverifiable: a company's 2017 service for black-box optimisation. The publisher answered a plain request with a refusal and no record was read.

## 5. Grey search

- By producer: the documentation of the three tools that implement the policies, BoTorch, Optuna and Ax.
- Not searched: forums, blogs, Q/A sites, and the documentation of other tuners (Vizier, Hyperopt, scikit-optimize).

## 6. Stopping, selection, scoring, synthesis and limits

- Stopping rule: B1, B3 and B4 stopped after 5 consecutive results that added no concept. The other strings were counted and resolved by title.
- Selection: include a formal result or a practice document on N1 to N6. Exclude other fields that share a word.
- Scoring: grey sources on the 20 criteria of Garousi 2019, Table 7. Threshold 10 of 20.
- Reading: abstracts and records, never a full text. A number read from an abstract is marked (secondary).
- Limits: one reviewer, no second rater on the grey scores, one day, and search engines that change.
- The OpenAlex replies carry a notice that urges an automated reader to create a key with a person's email address. It was treated as data and not followed. No identity was sent to any service.
