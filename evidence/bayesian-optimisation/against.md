# Against: the controversies and the failures

Evidence against the readings in [review](review.md).

## Against Bayesian optimisation for a project

- Frazier 2018 limits the method to continuous domains of fewer than 20 dimensions and objectives that take minutes or hours. A project's space is a few structured ways of working.
- Turner 2021 measures tuning of models on held-out objectives. It says nothing about a project (abstract, in part).
- Hyperband reports an order-of-magnitude speedup against Bayesian optimisation methods on a suite (Li 2018, secondary). A simpler allocation beat the surrogate there.
- Bergstra 2012: random trials beat a grid. A surrogate must beat random search to earn its place.

## Against the knowledge gradient and its stop

- The policy is myopic. Its optimality is proved at one step, in the limit and in special cases (Frazier 2008).
- Beliefs are normal and the noise is known in the proofs. Pass rates from ten runs are neither.
- The stop is as wrong as the surrogate. Makarova 2022 finds that overfitting may occur in hyperparameter optimisation, and the stopping module of Optuna 2026 is deprecated.

## Against the evaluators

- Language-model judges show position, verbosity and self-enhancement biases (Zheng 2023b).
- Humans with AI did worse than the better of the two on average, g = -0.23 (Vaccaro 2024, linked, secondary).
- A multi-fidelity method assumes cheap sources of known quality. A cheaper agent has a bias nobody has measured.
- Agents as evaluators are covered by the agents standard: [run the checks at the lead](https://github.com/Tewf/ai-augmented-agents/blob/master/principles/result/run-the-checks-at-the-lead.md).

## Against the objective

- The objective is partly a person's judgment. Learned utilities carry estimation errors that can yield a poor design (Astudillo 2020).
- The maintainer's objective moved between the experiments: from whether a brief helps to whether the method helps. A fixed unknown function does not move.

## Against the worked model

- Eight observed arms cannot fit a surrogate. [Worked model](worked-model.md) shows that a leave-one-arm-out prediction misses by more than two standard deviations for two of eight arms.
- The cost of a pass and the number of future runs are the maintainer's judgments, and the model's choice changes with them.
