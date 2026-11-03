# Position: what is known, what is not, and what this repository adds

Step 4. "Nobody has done this" and "we have not done this here" are kept apart.

## What is known

- Stopping at an acceptable result is a model with a name, satisficing (Simon 1956), and a formal sibling, bounded optimality (Russell 1995).
- Quality as a function of time has a theory, the anytime algorithm and its profile (Zilberstein 1996).
- Several wanting parties give a front of trade-offs (Marler 2004), and no fair rule picks one point (Arrow 1950).
- A hierarchy has a cost with known hardness (Dasgupta 2016; Hogemo 2021).
- Practice declares done by a fixed criterion (Schwaber 2020).

## What is not known

- No source was found that applies stopping theory or anytime theory to the structure of a document collection. Not found in this search.
- No study measures how far people accept a structure from the optimum of a stated cost, outside code (Candela 2016 is code).
- No stopping rule was found for a one-off project whose next change has an unknown distribution. Rules exist when a sample is available (Correa 2023) or when the same task is repeated and the rule can be learned (Svegliato 2020; Sung 2021).

## What this repository adds, and does not

- The frame is not new: anytime quality, a gap and a criterion fit the problem as stated.
- The new part is the case: one exact optimum on a real collection, read against what its owner built (see [baseline](baseline.md)).
- Done can be defined as: the written checks pass, and the solver's gap is below a stated tolerance, or the optimum is proved. A program can tell both.
- The repository cannot claim that acceptable is better than optimal in general. It has one case.

## Candidate rules, not adopted

- State a tolerance for the optimality gap before running an exact search. Grade: convention, untested.
- Keep the objectives apart and report the front. Grade: supported with caveat for module clustering.
