# The replay: what the guide would have proposed on the trace

This page reports the first test of [the guide](guide.md): the program [guide/replay.py](../guide/replay.py) run on [the trace](trace.md). It is a replay on one trace of two days, and proves little. The section "What it cannot say" comes last.

## How it was run

- **Arms:** the seven kinds of step defined in [the guide](guide.md). An arm is a kind, not a repository.
- **Decision points:** the seven waves from the second. Before each, a policy sees only the rows of earlier waves.
- **Belief:** a Beta belief on the chance that a step of the kind has the outcome, from the rows of that kind. Unrun kinds start at 1 and 1.
- **Net value of a step:** B times that chance, minus the mean cost of the kind. B is 600 thousand tokens and PROVISIONAL.
- **Outcome:** moved, or kept, as the trace defines them. Both are the reading of the writer, not the maintainer's judgment.
- **Policies:** greedy on the net value, UCB1, Thompson sampling, the knowledge gradient per cost, and random as the null. The first four are the [baseline's](../evidence/bayesian-optimisation/baseline.md) B3 to B6, written again here for kinds.
- **Hit:** the proposed kind is among the kinds the maintainer ran in that wave. Random hits with the chance of a kind being among them.
- **Stop:** the guide stops when no step has an expected gain over the jobs still to come above its cost. The jobs to come are counted from the trace, which is hindsight.
- Run: `python3 guide/replay.py [--outcome kept] [--benefit 1200]`. Thirty-six tests are in [guide/test_replay.py](../guide/test_replay.py).

## What each policy proposed

Outcome moved, B at 600. In brackets: whether the kind was among those the maintainer ran.

| Wave | Kinds the maintainer ran | Greedy | UCB1 | Thompson | Knowledge gradient per cost | Stop? |
|---|---|---|---|---|---|---|
| 1 | build, review | audit (no) | audit (no) | experiment (no) | audit (no) | no |
| 2 | audit, build, design, experiment | review (no) | audit (yes) | review (no) | review (no) | yes |
| 3 | build, design | review (no) | upkeep (no) | review (no) | review (no) | yes |
| 4 | build, upkeep | review (no) | upkeep (yes) | review (no) | review (no) | yes |
| 5 | audit, build, experiment | review (no) | setup (no) | review (no) | review (no) | yes |
| 6 | audit, build, upkeep | review (no) | setup (no) | review (no) | review (no) | yes |
| 7 | design, review, setup | review (yes) | setup (yes) | review (yes) | review (yes) | yes |

## The agreement

| Policy | Hits of 7, moved | Hits of 7, kept | Hits of 7, moved, B from 200 to 3000 |
|---|---|---|---|
| random | 2.7 | 2.7 | 2.7 |
| greedy | 1 | 1 | 1 |
| UCB1 | 3 | 3 | 3 to 4 |
| Thompson | 1 | 2 | 1 |
| knowledge gradient per cost | 1 | 2 | 1 to 3 |

- **Three policies hit less than random.** Greedy, Thompson and the knowledge gradient hit once, at wave 7, where the maintainer ran a review.
- **They propose a review at almost every wave.** Every review in the trace moved something, so a review is the best kind by the data, wave after wave.
- **The maintainer ran no review from wave 2 to wave 6.** Each repository had its review; a second review of the same repository was not worth the same. At wave 7 the review was a new question. The steps changed the function.
- **UCB1 hits three times, by exploring.** It tries a kind never run, cheapest first. That is a tie-break, not a prediction.
- **The benefit B moves the knowledge gradient from 1 to 3 hits.** It does not move the other two.

## What it would have saved or spent

| Policy | Tokens of the jobs it did not propose (k) | Cost of its proposals that missed (k) |
|---|---|---|
| greedy | 11885 | 1463 |
| UCB1 | 10006 | 973 |
| Thompson | 11885 | 1463 |
| knowledge gradient per cost | 11885 | 1463 |

- **The first column is not a saving.** The maintainer needed those jobs. Of 12115 thousand tokens in the seven waves, 98 percent were jobs of a kind greedy did not propose.
- **The second column is what the missed proposals would have added**, one mean step of the proposed kind per miss.
- For greedy that is 1463 thousand tokens, about 1.8 meter points of the 15 the two days moved.
- **The stop fired before wave 2.** The most it could have saved is every job after it, 10159 thousand tokens, 12.3 points. No one would claim that. The stop says that, on this data, no step has a gain above its cost for choosing among kinds, because the best kind is clear and the rest cannot overtake it.
- **The meter conversion is crude.** The 15 points are spread by tokens, and most tokens are estimates.

## What it cannot say

- **One trace, 36 rows, one maintainer.** The agreement of 1 or 3 in 7 does not tell a policy from chance.
- **The outcome is the writer's reading.** The person's judgment, which is the objective, is not recorded per job.
- **Reviews saturate, and the model does not know it.** The Beta belief treats a kind as stationary, so it cannot learn that a second review of the same repository pays less.
- **The menu was every kind at every wave.** In practice the state decides what is possible: a build waits on a design, a review on a repository without one.
- **The stop uses the future count.** A real guide does not know how many jobs will come.
- **The costs are estimates**, except two. A different cost per kind would move the net values.
