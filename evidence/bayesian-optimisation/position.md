# Position: what is known, what is not, and what this repository adds

Step 4. "Nobody has done this" and "we have not done this here" are kept apart.

**Shape:** [position](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/position.md)

## What is known

- Choosing the next evaluation of an expensive unknown function has a full theory and tools: a surrogate, an acquisition function and a stopping rule (Shahriari 2016; Frazier 2018; Garnett 2023).
- A step has a cost, and cheap approximations can steer dear evaluations (Snoek 2012; Kandasamy 2016; Xie 2024).
- A measurement is worth what it changes in the decision (Howard 1966; Frazier 2009).
- A stopping rule exists once a surrogate gives the distribution of the next gain (Makarova 2022; Nguyen 2017).
- A drifting objective, a learned utility and a language model in the loop each have a method (Bogunovic 2016; Astudillo 2020; Liu 2024c).

## What is not known

- No source was found for an objective that the steps themselves change. Not found in this search.
- No source was found that combines evaluators with unknown biases, a cost per evaluator and a utility held by a person.
- No study of a project's steps as evaluations of an unknown objective was found, outside tuning of models.
- Whether a surrogate on a handful of ways of working predicts anything is untested here and in the pool.

## What a project adds that a benchmark function lacks

| Difference | Benchmark function | Project | Nearest source |
|---|---|---|---|
| the function | fixed | changed by the steps: a brief with checks changes what a later pass rate means | Bogunovic 2016, for drift outside the policy |
| the evaluators | exact, or noisy with a known law | agents with their own biases, and tiers that differ | Zheng 2023b; Vaccaro 2024 |
| the objective | written in code | partly the person's judgment, learned from comparisons | Astudillo 2020 |
| the domain | continuous, under 20 dimensions | a few structured ways of working | Frazier 2018 |
| the step | one evaluation | a batch of runs with a cost in tokens | Snoek 2012 |

## What this repository adds, and does not

- The frame is not new. A surrogate, an acquisition function and a stopping rule fit the problem as stated.
- The new part is the case: the family's own two sequential experiments, read as the first evaluations of an unknown objective in [worked-model](worked-model.md).
- The stopping rule of the first review, a criterion plus a gap, can now be derived: stop when the expected gain over the remaining use is below the cost of a step.
- The repository cannot claim that the policy picks well. It has eight observed arms, in three stages.

## Candidate rules, not adopted

- Choose a step by the expected gain from a surrogate per unit of cost, and stop when the gain over the remaining use is below the cost. Grade: supported with caveat for tuning problems, convention for projects.
- Write the prediction before each step, as both experiments did. Grade: convention, untested.
