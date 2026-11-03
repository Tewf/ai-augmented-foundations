# Baseline: the policy a project's next step is compared against

Step 5. The review is finished because the baseline can be named.

**Shape:** [baseline](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/baseline.md)

## The baseline

- **Standard policy:** a Gaussian-process surrogate with noisy expected improvement. Reference implementation: BoTorch (Balandat 2020; BoTorch 2026), the acquisition `qLogNoisyExpectedImprovement`, driven through Ax for an experiment loop (Ax 2026, below the grey threshold).
- **Simpler policy:** a bandit over the arms, UCB1 (Auer 2002) or Thompson sampling (Russo 2018). Both are a few lines; [worked_model.py](worked_model.py) holds a version of each.
- **Null policy:** random search (Bergstra 2012), in Optuna 2026 as `RandomSampler`.
- **Stopping rule:** stop when the estimated room for improvement is below the statistical error (Makarova 2022), in Optuna 2026 as the `Terminator`, deprecated since version 4.9.0.

## The maintainer's practice

Written down for this review, with nothing private cited.

- The next step is chosen by the maintainer after reading the last result.
- A protocol with a written prediction comes before each run, and the run is judged by a program.
- The loop stops when the question of the run is answered, or when a first pass is done.
- Two sequences are on record: the brief test in two rounds, and the method comparison.

## How to compare

| Id | Formulation | Source | How to compare |
|---|---|---|---|
| B1 | the maintainer's practice | the record above | the tokens spent to reach the best arm found |
| B2 | random search over the arms | Bergstra 2012 | the same, over repeated draws |
| B3 | UCB1 or Thompson over the arms | Auer 2002; Russo 2018 | the same, and the arm picked at each stage |
| B4 | surrogate with noisy expected improvement | Jones 1998; BoTorch 2026 | the same, with the surrogate fitted on the arms |
| B5 | surrogate with the knowledge gradient | Frazier 2009; BoTorch 2026 (`qKnowledgeGradient`) | the same |
| B6 | B4 or B5 with improvement per cost | Snoek 2012; Lee 2020; Xie 2024 | the same, in tokens |
| B7 | B4 or B5 stopped by the terminator | Makarova 2022 | the stage at which each stops |

- The measure is regret in net value per run against the best arm known, summed over the steps, and the tokens spent. Both are computed from a recorded sequence.
- A recorded sequence has three stages, so a comparison is a replay, not a test. [Worked model](worked-model.md) is the first replay.

## What the baseline says today

- The standard policy has a reference implementation and a stopping rule with one. The family has not run either.
- The program of [worked model](worked-model.md) re-implements expected improvement and the knowledge gradient on eight arms. It agrees with no reference implementation yet.
- The first measurement still to make is B4 and B5 in BoTorch on the same eight arms, against B2.
