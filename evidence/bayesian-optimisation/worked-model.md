# A worked model: the family's runs as evaluations of an unknown objective

A small program, [worked_model.py](worked_model.py), reads the runs of the family's two sequential experiments as the first evaluations of an unknown objective. It fits a simple surrogate and prints the next step each policy would choose and whether the loop should stop. It cannot say much with so few points, and the last section says what.

## How to run it

- Needs Python 3.11 or later and numpy. Run `python3 worked_model.py`; it prints the tables below.
- Inputs and tunables are in [worked-model.toml](worked-model.toml). Every tunable is tagged PROVISIONAL.
- Tests: `python3 -m unittest test_worked_model`. Two of them recount the pass rates from the experiments' own records when the sibling repositories sit beside this one.

## The unknown objective

- An **arm** is a way of delegating a task: a model tier, an information level and an interface.
- **Tier:** a small hosted model (0) or Haiku (1).
- **Information level:** 0 the task sentence alone; 1 the convention brief; 2 the brief plus the list of checks; 3 that plus a start file and a memory index.
- **Interface:** one call to the model's API (0), or a coding agent in a folder (1).
- The **pass rate** p(x) of an arm is the share of runs that pass hidden tests. It is unknown and is learned.
- The **net value** of a run is B times the pass rate minus its cost in tokens. B, the tokens a passing run is worth, is the maintainer's judgment, set to 100000 and PROVISIONAL.

## The evaluations

Each row is a point. Pass rates are hidden-test passes, from the [brief test](https://github.com/Tewf/ai-augmented-agents/blob/master/experiments/brief-test/results-2.md) (stages 1 and 2) and the [method comparison](https://github.com/Tewf/ai-augmented-project/blob/master/experiments/method-comparison/results.md) (stage 3).

| Arm | Passes | Cost of a run (tokens) | Stage |
|---|---|---|---|
| small model, API, task alone | 0/40 | 960 | 1 and 2 |
| small model, API, convention brief | 8/40 | 1112 | 1 and 2 |
| small model, API, brief and checks | 9/40 | 1288 | 1 and 2 |
| Haiku, API, task alone | 0/30 | 960 | 2 |
| Haiku, API, convention brief | 22/30 | 1112 | 2 |
| Haiku, API, brief and checks | 21/30 | 1288 | 2 |
| Haiku, agent, task alone | 0/15 | 46900 | 3 |
| Haiku, agent, the method | 15/15 | 39650 | 3 |

- **Cost of an API run** is an estimate: the prompt length in characters divided by four, plus 930 tokens for the reply. The 930 is the mean reply of the 30 replies of round one. The brief test recorded no cost.
- **Cost of an agent run** is measured in the method comparison: fresh input plus output tokens, mean of 15 sessions. Cache reads are left out because they are cheap.
- Six arms were never run: the small model in the agent at four levels, and Haiku in the agent at levels 1 and 2. Level 2 for Haiku is the brief without the start file, the arm the method comparison names as its next.

## The surrogate and the policies

- **Surrogate:** a Gaussian process on the pass rate, with a squared-exponential kernel over (tier, level, interface), a prior mean of 0.25 and observation noise from the binomial. All settings are PROVISIONAL.
- **Step:** ten runs of one arm, as in both experiments. Its cost is ten times the cost of a run.
- **Stop:** when the expected gain, over the future runs still planned, is below the cost of the step. The future runs are 200 and PROVISIONAL.

| Policy | Chooses the arm that maximises | Reference |
|---|---|---|
| EI | expected improvement of the net value over the best posterior value | Jones 1998 |
| EI per cost | expected improvement divided by the cost of the step | Snoek 2012 |
| knowledge gradient | the expected rise of the best posterior net value after the step | Frazier 2009 |
| GP-UCB | posterior mean plus two standard deviations | Srinivas 2010 |
| UCB1 | an upper bound on each arm alone; an unrun arm first, the cheapest first | Auer 2002 |
| Thompson | the probability of being best, with independent Beta beliefs | Russo 2018 |

## What the model picks

After stage 3, with 240 runs in 8 arms:

| Policy | Next step | Gain over 200 runs (tokens) | Cost of the step (tokens) | Stop? |
|---|---|---|---|---|
| EI | Haiku, API, brief and checks | 608883 | 12880 | no |
| EI per cost | Haiku, API, brief and checks | 608883 | 12880 | no |
| knowledge gradient | Haiku, agent, brief and checks | 364919 | 432750 | yes |
| GP-UCB | Haiku, agent, brief and checks | 364919 | 432750 | yes |
| UCB1 | small model, agent, the method | 608903 | 396500 | no |
| Thompson | Haiku, API, convention brief | 608903 | 11120 | no |

- **The next step the model picks is the knowledge gradient's:** Haiku in the agent with the brief and the list of checks, without the start file or the memory index. It is the arm the method comparison names as its next arm, found here by a different route.
- **The loop should stop on that step, narrowly.** The gain is 365 thousand tokens and the step costs 433 thousand. The two meet at 237 future runs.
- **EI never stops.** It re-measures the arm that is already best, because with noise there is always a chance its true value is higher. A step of 13 thousand tokens then pays back at 4 future runs. EI at the incumbent is a known fault of the naive form.
- **For UCB1 and Thompson the gain is the expected value of perfect information** among the independent beliefs, the same number for both.
- **The bandit policies disagree.** UCB1 can only try unrun arms in order of cost. Thompson sampling re-measures the cheap Haiku arm. Neither uses the closeness of arms.
- **The benefit of a pass changes the choice.** At 10000 tokens a pass, the knowledge gradient picks the cheap API arm and stops. At a million it picks the agent arm and goes on.

## Replaying the two earlier decisions

Policies given only the runs up to a stage, to see what they would have chosen then.

| After stage | EI | knowledge gradient | Thompson | Run next by the maintainer |
|---|---|---|---|---|
| 1: 30 runs, small model only | Haiku, API, checks | Haiku, API, checks | Haiku, API, checks | Haiku added, with two more tasks |
| 2: 210 runs in 6 arms | Haiku, API, checks | Haiku, agent, checks | Haiku, API, convention | the agent, task alone against the method |

- After stage 1 all the policies point at Haiku, the tier the maintainer added. Three decisions cannot validate a policy.
- After stage 2 UCB1 picks the method arm in the agent. That follows from its tie-break by cost and is not a prediction.

## What it cannot say

- **Eight points cannot fit a surrogate.** Each observed arm was predicted from the other seven.
- Two predictions missed by about two standard deviations or more.
- Haiku with the convention brief was observed at 0.73 and predicted at 0.37. Haiku with the task alone was observed at 0 and predicted at 0.42.
- **The arms are not points in a space.** The kernel treats levels as ordered and equally spaced; they are not, and the lengths are guesses.
- **Pass rates are pooled over tasks.** The brief test shows pass rates from 15% to 90% across its three tasks at the same level.
- **The two experiments differ in more than the arm.** The interface, the harness, the tasks run and the day all differ, as their own protocols say.
- **The cost of an API run is an estimate.** The benefit of a pass and the number of future runs are judgments, and the stop flips at 237 runs.
- **The objective is bounded and nearly met.** The best arm passes 15 of 15. The remaining question is cost and generality, which hidden tests on three small parsers do not measure.
- **No reference implementation was run.** The expected improvement and the knowledge gradient here are written for the review. Comparing them with BoTorch is the first thing to do next ([baseline](baseline.md)).
- **It says nothing about the person.** The judging person's utility is the number B, set by hand.
