# Frame: a project as the optimisation of an unknown objective

Step 1, read on 2026-11-03. It states the problem of the loop and the field's names for its parts.

## The problem in one sentence

A project takes steps; each step costs tokens, time or money and returns a noisy reading of an objective nobody can write down; which step should come next, and when should the project stop?

## The maintainer's framing

- The maintainer's framing is a study whose goal is to maximise a function nobody knows.
- So the work is data gathering, then several agents acting as researchers, each building an estimate, and then the next step.
- The [convergence topic](../convergence/frame.md) framed only the stopping rule. This topic frames the whole loop, and the stopping rule falls out of it.

## Names

| Term | What the field means by it | Source |
|---|---|---|
| **Bayesian optimisation** | optimising an expensive black-box function by keeping a probabilistic model of it and choosing each evaluation from the model | Mockus 1975; Jones 1998; Shahriari 2016 |
| **surrogate** | the cheap model of the unknown function, usually a Gaussian process | Shahriari 2016; Frazier 2018 |
| **acquisition function** | the score of a candidate next evaluation under the surrogate | Frazier 2018; Garnett 2023 |
| **expected improvement** (EI) | the expected gain over the best value so far | Mockus 1975; Jones 1998 |
| **knowledge gradient** (KG) | the expected rise in the best posterior value after one more measurement | Frazier 2008; Frazier 2009 |
| **upper confidence bound** (UCB, GP-UCB) | mean plus a multiple of the standard deviation | Auer 2002; Srinivas 2010 |
| **multi-armed bandit** | choosing among options with unknown payoffs, balancing exploring and exploiting | Bubeck 2012; Lattimore 2020 |
| **regret** | the payoff lost against always playing the best option | Bubeck 2012 |
| **Gittins index** | the value of an option in a bandit that makes the optimal policy an index rule | Gittins 1979 |
| **active learning** | choosing which labels to ask for, to learn a model with few of them | Settles 2009 |
| **Bayesian experimental design** | choosing the next experiment to maximise expected information or utility | Chaloner 1995; Rainforth 2024 |
| **multi-fidelity** | optimising when cheap approximations of the objective exist beside the dear one | Kennedy 2000; Kandasamy 2016; Peherstorfer 2018 |
| **value of information** | the expected gain in decision value from learning something before deciding | Howard 1966 |
| **optimal stopping** | choosing when to stop a sequence of observations | Ferguson 1989 |
| **Pandora's box** | search with a cost per opened option, solved by an index | Weitzman 1979; Xie 2024 |
| **preference-based optimisation** | optimising a utility the decision maker can only compare, not state | Astudillo 2020 |
| **time-varying optimisation** | optimising an objective that drifts while it is searched | Bogunovic 2016 |

## What practice calls it

- Practitioners say **hyperparameter tuning**, **sweep**, **A/B test**, **adaptive experimentation** and **autotuning**.
- Tool makers say **study** and **trial** (Optuna 2026) or **experiment** and **trial** (Ax 2026).
- The field says Bayesian optimisation for the whole loop, and the three parts keep their own names: surrogate, acquisition and stopping.

## The topic's name against the field's

- The topic was staged as `next-step`, the maintainer's word for the choice after data gathering.
- The field's word is **Bayesian optimisation**, with **cost-aware**, **multi-fidelity** and **stopping** as its extensions. The folder is renamed `bayesian-optimisation`.
- The repository's name is unchanged; the frame step of the first review found no reason to rename it, and this one finds none.

## Sub-questions

| Id | Sub-question | Answers |
|---|---|---|
| N1 | Given the runs so far, which step should come next? | the choice of a step |
| N2 | How do cheap and dear evaluators enter the choice? | multi-fidelity, cost |
| N3 | When does a step buy reward, and when information only? | bandits, active learning, experimental design |
| N4 | When does the loop stop? | value of information, stopping |
| N5 | What does a project have that a benchmark function lacks? | steps that change the function, agents with biases, a judging person |
| N6 | Which policy is the baseline, and with what reference implementation? | the baseline |

## Links, not repeated

- Agents as evaluators of each other's output: [run the checks at the lead](https://github.com/Tewf/ai-augmented-agents/blob/master/principles/result/run-the-checks-at-the-lead.md) in the agents standard.
- Stopping as satisficing, anytime behaviour and the optimality gap: [convergence](../convergence/README.md).
