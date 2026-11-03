# Bayesian optimisation: a project as the optimisation of an unknown objective

The third review of this repository. It asks how a project should choose its next step, and when to stop, if its goal is a function nobody can write down. It reads the loop of gathering data, estimating and taking the next step as Bayesian optimisation, and it builds a worked model on the family's own experiments.

- Pool: 39 new sources: 36 formal, 3 grey; 3 more are linked from sibling reviews.
- Grey scores are in the sources file; two are at or above 10 of 20, one is below.
- A first pass: abstracts and records. No full text was read.
- The topic was first called `next-step`; the field's word is Bayesian optimisation.

## Files

| File | Role |
|---|---|
| [frame](frame.md) | step 1: the problem and the field's names |
| [protocol](protocol.md) | how the pool was searched and scored |
| [sources](sources.md) | the pool and its quality |
| [review](review.md) | step 2: strands, surveys first |
| [state of the art](state-of-the-art.md) | step 3: records and bounds |
| [position](position.md) | step 4: known, unknown, added |
| [against](against.md) | the evidence against |
| [baseline](baseline.md) | step 5: the policy to compare against |
| [worked model](worked-model.md) | the family's runs as evaluations, with [a program](worked_model.py), [its inputs](worked-model.toml) and [its tests](test_worked_model.py) |

## Claims

| Claim | Grade | Where |
|---|---|---|
| Choosing the next evaluation of an expensive unknown function has a surrogate, an acquisition function and a stopping rule | supported with caveat, measured on tuning problems | review.md, strand 1 |
| A measurement is worth what it changes in the decision, and a step should stop when that falls below its cost | proved under normal beliefs; convention for projects | review.md, strand 2 |
| A stopping rule for one run exists once a surrogate supplies the distribution of the next gain | supported with caveat | review.md, strand 6 |
| Cheap evaluators and cost enter the policy through multi-fidelity and per-cost scores | supported with caveat, proved and tested on benchmarks | review.md, strand 5 |
| A project's steps change the objective | not found in the literature | position.md |
| Evaluators that are agents carry biases | measured for language-model judges | review.md, strand 7 |
| The objective is partly a person's judgment, learned from comparisons | supported with caveat | review.md, strand 7 |
| The baseline is a Gaussian-process surrogate with noisy expected improvement, and UCB1 as the simpler policy | convention, a record of practice | baseline.md |
| On the family's eight arms the knowledge gradient picks the agent with the brief and its checks, and the loop stops narrowly | a toy model, eight points | worked-model.md |
