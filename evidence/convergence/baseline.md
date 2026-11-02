# Baseline: what this repository's claims on convergence are compared against

Step 5. The review is finished because the baseline can be named.

## The baseline run

The maintainer's own exact optimisation, written down for this review. It is a practice with run records, not a publication; the numbers below were read in those records and not rerun.

- Formulation: a cost J equal to space plus lambda times time over a containment tree of files.
  - Space is the total size of the content once nothing is held twice.
  - Time is Dasgupta's cost (Dasgupta 2016): each reference between two files pays the number of files under the smallest folder holding both.
  - Hard constraints: at most three levels, a breadth ceiling, a minimum number of children per folder, and imports that do not descend into a sibling subtree.
  - Lambda and a lexical-similarity weight are provisional.
- Method: an exact constraint-programming model (OR-Tools 2026) on small instances.
- Results, in the records:
  - At three levels the model proved optimality at 17 files in 1.8 seconds and at 101 files in 29.5 seconds, without the lexical term. Cost 406 against 1031 for the hand-made tree.
  - At two levels and 101 files, 180 seconds gave a feasible 423 against a proved bound of 353.
  - With the lexical term, 300 seconds gave a feasible 1108 against a bound of 495.
  - Where references existed, the optimum recovered 5 of the owner's clusters. 47 files with no references were placed arbitrarily.
  - The lexical term raised the share of edge-free files placed with their name or kind from 0.58 to 1.00. Distance to the owner's tree moved from 64 to 65.
  - The optimum was grouped by product. The owner's tree was grouped by stage.

## What it says on the front page's questions

- Gap between optimum and accepted: large on this case, and not in cost only. The optimum answered a different question from the owner's. Candela 2016 found the same kind of gap in code.
- Which to stop at: acceptable for the tree, with the optimum used as a bound that certifies the gap. One case supports this; it is not a general result.

## The best formulation found, to compare against

| Id | Formulation | Source | How to compare |
|---|---|---|---|
| B1 | the hand-made tree | the owner | cost J and acceptance of the top moves |
| B2 | Dasgupta's cost alone, by average linkage | Dasgupta 2016; Cohen-Addad 2019 | cost J and distance to B1 |
| B3 | modularisation quality by hill climbing | Mitchell 2006 | partition distance to B1, J |
| B4 | cohesion and coupling as separate objectives | Praditwong 2011 | the front against the single J |
| B5 | total-depth objective with depth bounds | Hogemo 2021 | exact value on small trees against the maintainer's model |

- The nearest formulation to the maintainer's is B5: a depth-bounded Dasgupta-type cost. It adds no merge or factor moves, so it is a sub-problem of the baseline run.
- The comparison that would show the cost is calibrated: the optimum lowers J and its moves are accepted by the owner. The run shows the first, not the second.

## What the baseline says today

- An exact optimum exists for small instances and a bound for large ones.
- Done can be tested as: checks pass and the gap is below a stated tolerance.
- The first measurement still to make is B2 and B3 on the same instances.
