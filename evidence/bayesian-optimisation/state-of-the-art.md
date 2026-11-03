# State of the art, per sub-question

Step 3. The most adopted practice is kept apart from the best evidence, and what has been achieved from what is impossible or hard.

| Sub-question | Most adopted | Best evidence | Measured how |
|---|---|---|---|
| N1 Next step | a Gaussian-process surrogate with expected improvement (BoTorch 2026; Optuna 2026) | Turner 2021: Bayesian optimisation beat random search on held-out tuning tasks | a challenge on tuning, not on projects |
| N2 Cheap and dear evaluators | none found | Kandasamy 2016: better regret than ignoring cheap approximations | theorem and benchmarks |
| N2 Cost of a step | none found | Snoek 2012; Lee 2020; Xie 2024: improvement per cost, a cost-cooled phase, a Gittins index | benchmarks, 20 problems in Lee 2020 |
| N3 Reward or information | upper confidence bound and Thompson sampling | Srinivas 2010: regret bounded by information gain | theorem |
| N4 When to stop | the Terminator of Optuna 2026, now deprecated | Makarova 2022: stop when room for improvement is below statistical error | real tuning problems |
| N5 A function the steps change | none found | Bogunovic 2016 for drift outside the policy | theorem and two data sets |
| N5 Biased evaluators | language-model judges | Zheng 2023b: over 80% agreement with humans, with named biases | benchmarks and votes |
| N5 A judging person | none found | Astudillo 2020: learn the utility from pairs and keep its uncertainty | experiments |
| N6 Baseline | random search, then Bayesian optimisation | Bergstra 2012 and Turner 2021 | experiments |

## Upper bounds (achieved)

- Regret of GP-UCB is bounded by information gain, and sublinear for common kernels (Srinivas 2010).
- Multi-fidelity beats ignoring fidelity, in regret and in tests (Kandasamy 2016).
- The knowledge gradient is optimal at one step and in the limit, and has bounded suboptimality with correlated beliefs (Frazier 2008; Frazier 2009).
- Hyperband reports an order-of-magnitude speedup on a suite (Li 2018, secondary).

## Lower bounds (impossible, or hard)

- The knowledge gradient is myopic: its optimality is proved at one step, in the limit and in special cases, not in general (Frazier 2008).
- Bayesian optimisation is best on fewer than 20 dimensions and continuous domains (Frazier 2018).
- Convergence rates for expected improvement were proved under mild assumptions or without noise (Nguyen 2017, abstract in part).
- A classic stopping rule needs a known distribution (Ferguson 1989, linked). With a surrogate the distribution is the surrogate's belief, and the rule is as wrong as the surrogate.

## The two records

- Most adopted: a Gaussian-process surrogate with expected improvement, and random search as the null.
- Best evidence: held-out tuning tasks, bandit regret theorems and the knowledge gradient's optimality results.
- None of them is a study of a project whose steps change the function.
