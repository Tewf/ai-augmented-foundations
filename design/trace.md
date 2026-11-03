# The trace: every job of two days

The first dataset of the guide: one row per job of the family's two days, 2026-11-02 and 2026-11-03, read from the maintainer's log of two days and the notes each job left. The rows are in [guide/trace.toml](../guide/trace.toml); the table below is printed from that file by [guide/replay.py](../guide/replay.py) and a test fails if the two differ.

## How to read it

- **Wave:** the cluster of jobs launched together. Wave 0 is the afternoon of the first day; waves 1 to 7 follow in order. A wave is a decision point of the maintainer.
- **Kind:** the kind of step, defined in [the guide](guide.md), part one.
- **Agents and tokens:** the agent runs in the row, and thousands of tokens on the subscription. Two counts are recorded in the log (250 and 326 thousand). The log gives a range of 137 to 326 for ten agents; every other row carries 230, the middle of that range, marked est.
- **Moved:** 1 if a later job or record names this job's output as the reason for a change that stands at the end of the log. **Kept:** 1 if the job's headline result stands at the end of the log. Both are the reading of whoever wrote the file, not the maintainer's judgment. A blank is an outcome not yet known, or work outside the family.
- **Not in the table:** the person's time, which the log does not record.
- **Not in the table either:** spend on a paid API, recorded in two rows: 0.28 dollars for the spike's last measure and 0.31 for the method comparison.

## The rows

| Wave | Job | Kind | Agents | Tokens (k) | Produced | What it changed | Moved | Kept |
|---|---|---|---|---|---|---|---|---|
| 0 | family-setup | setup | 1 | 230 est. | nine public repositories with their skeleton, pins and Pages | nothing that existed | 0 | 1 |
| 0 | tsp-baselines (outside) | build | 1 | 230 est. | three baseline solvers and their tests, on coursework | the conventions for how code is generated |  |  |
| 0 | logo-bottles (outside) | build | 1 | 230 est. | a logo and bottle models for a business project | a design register entry |  |  |
| 1 | ide-review | review | 1 | 230 est. | a review of 28 sources and a named baseline (an open extension) | two earlier notes were corrected; the build would start from the baseline | 1 | 1 |
| 1 | project-review | review | 1 | 250 | a review of 39 sources; the field name human-AI teaming kept | the design document of the method; one push held for a hook until the maintainer allowed one cited title | 1 | 1 |
| 1 | agents-review | review | 1 | 230 est. | a review of 35 sources; baseline the arrangement of 2026-10-29 | its third finding (the brief has a convention and no test) set the brief test | 1 | 1 |
| 1 | foundations-review | review | 1 | 230 est. | a review of 34 sources in two topics; baseline the maintainer's exact optimisation | set the cost measure, and later the reframe as an unknown objective | 1 | 1 |
| 1 | project-method-review | review | 1 | 230 est. | a review of 38 sources; baseline the six design-science activities | set the project shape and its check | 1 | 1 |
| 1 | hub-review | review | 1 | 230 est. | a review of 23 sources; the name kept; an overlap check, 24 tests | the overlap check later gained a semantic pass | 1 | 1 |
| 1 | cases-review | review | 1 | 326 | a review of 37 sources and a first case with a measures program | the second case reused the program | 1 | 1 |
| 1 | family-rules | build | 1 | 230 est. | six rule pages, a weekly audit of every member, 17 tests | nothing later cites a change it caused | 0 | 1 |
| 2 | project-design | design | 1 | 230 est. | a design document of the method, with a figure | revised after the IDE design named four gaps in it: a brief shape, a start-file name, ten file kinds | 1 | 1 |
| 2 | blueprint-first-build | build | 1 | 230 est. | a proof as topics, a Lake project, a link check with 18 tests; the proof was not run here (the cache did not download) | the proof was checked later in CI | 0 | 1 |
| 2 | cases-second-case | experiment | 1 | 230 est. | a second case: 33 commits, 16 records, 6 decisions that reached the person, 5 stalls | an optional argument added to the measures program | 0 | 1 |
| 2 | review-audits | audit | 7 | 959 est. | a claim audit of seven reviews | about 67 rows correct, 14 imprecise and 2 wrong fixed, about 30 unverifiable | 1 | 1 |
| 2 | foundations-cost-measure | build | 1 | 230 est. | a candidate cost of a tree of topics, computed on eight trees, 27 tests | found that depth gives 76 to 90 percent of the cost; nothing validates the measure | 0 | 1 |
| 2 | brief-test-1 | experiment | 1 | 230 est. | 30 free calls to a hosted small model: 0, 0 and 5 of 10 passed across three briefs | the headline (naming the checks lets a cheap model pass) was withdrawn by the second round | 1 | 0 |
| 2 | project-shape | build | 1 | 230 est. | a project shape and a check, 19 tests | no later change cites it | 0 | 1 |
| 3 | blueprint-rest | build | 1 | 230 est. | a comparator, a challenge file and an agreement file, 42 tests | the audit column was split in two when the maintainer said he cannot read the proof language | 0 | 1 |
| 3 | ide-design | design | 1 | 230 est. | a design document for a thin extension, with a one-day spike of five measures | named four gaps in the method's design and one in the standard | 1 | 1 |
| 4 | ide-spike | build | 1 | 230 est. | readers, three views, a hand-over note; measures 1 to 3 pass; 4 and 5 run later | measure 5 failed on a 7B model and passed on two cloud models: the design kept its decision with a model-size condition | 1 | 1 |
| 4 | cards | build | 7 | 1610 est. | a card of principles, shapes and checks in each of seven repositories | found that the card generator drops hand-written lines in llms.txt, passed to the standard's owner | 1 | 1 |
| 4 | agent-style | build | 1 | 230 est. | a reader style for an agent, five overrides from the family's own evidence | every member's contributor file now names it | 0 | 1 |
| 4 | release | upkeep | 3 | 690 est. | nine repositories released at 0.1.0 with tests in CI | stale citation abstracts fixed | 0 | 1 |
| 4 | apply-here | upkeep | 1 | 230 est. | the family's shapes applied to the maintainer's own machine configuration | the shapes were then widened because the real practice failed them | 0 | 1 |
| 4 | shapes-meet-practice | build | 1 | 230 est. | memory shapes widened after 492 refusals on 164 real memories | the practice here wins over the shape | 1 | 1 |
| 5 | method-comparison | experiment | 1 | 230 est. | 30 sessions on a small cloud model: 0 of 15 alone, 15 of 15 with the method, confounded | the next measurement is the bare arm given the same information | 1 | 1 |
| 5 | brief-test-2 | experiment | 1 | 230 est. | 180 calls, two tiers, a held-out judge: 0, 30 and 29 of 60 | round one's 5 of 10 was fitting visible tests; the grade was lowered in five places | 1 | 1 |
| 5 | standard-changes | build | 1 | 230 est. | the standard released at 1.20.0: a verdicts file and a hand marker, 137 tests | every member's pin was raised to it | 1 | 1 |
| 5 | overlap-semantic | build | 1 | 230 est. | a semantic pass on scope rows, threshold 0.70, 8 tests | one pair flagged | 0 | 1 |
| 5 | review-depth | audit | 7 | 1610 est. | forward citations and a second grey rater on seven reviews; agreement kappa 0 to 0.25 | two to nine forward works added each | 0 | 1 |
| 5 | topic-records | audit | 1 | 230 est. | a check of two records numbered alike | nothing: the finding was stale | 0 | 1 |
| 6 | ide-build | build | 1 | 230 est. | the extension: three views, five commands, 18 reader tests and 9 view tests | publishing waits for the maintainer | 0 | 1 |
| 6 | public-repos-audit | audit | 1 | 230 est. | an audit of fourteen older public repositories | dead links, a stale status, a red CI and a truncated DOI fixed | 1 | 1 |
| 6 | machine-obeys-standards | upkeep | 1 | 230 est. | the maintainer's machine loads the cards each session, and a hook refuses a broken start file | nothing cited later | 0 | 1 |
| 7 | org-rework (outside) | upkeep | 1 | 230 est. | a split of a business project's notes into an organisation | not read: outside the family |  |  |
| 7 | foundations-next-step | review | 1 | 230 est. | a review of 39 sources on Bayesian optimisation and a worked model on eight points | the stop is now derived from the value of information; one principle gained its derivation | 1 | 1 |
| 7 | three-more-repos | setup | 1 | 230 est. | three public repositories, scope only | both hubs updated | 0 | 1 |
| 7 | guide-design | design | 1 | 230 est. | this document and the replay | not yet |  |  |

## Totals by kind

| Kind | Rows | Tokens (k) | Moved | Rows with an outcome | Kept |
|---|---|---|---|---|---|
| audit | 4 | 3029 | 2 | 4 | 4 |
| build | 12 | 4140 | 4 | 12 | 12 |
| design | 3 | 690 | 2 | 2 | 2 |
| experiment | 4 | 920 | 3 | 4 | 3 |
| review | 8 | 1956 | 8 | 8 | 8 |
| setup | 2 | 460 | 0 | 2 | 2 |
| upkeep | 3 | 1150 | 0 | 3 | 3 |

- **Reading:** every review moved something; no upkeep step did; the experiments moved something three times in four. The costs are estimates, so the table is a count of steps more than of spend.
- **Caution:** this is one trace of two days by one maintainer. The scale of the replay in the guide is the size of this table.
