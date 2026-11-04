# Changelog

The releases this repository pins, newest first, in the form of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
A pin move is recorded here, not in decisions/.

## [Unreleased]

### Added

- 2 tests that the replay reads the trace extended by the job record (ai-augmented-project, shapes/job-record.md) as it read the trace before.

## [0.1.1] - 2026-11-04

### Added

- Pinned reader-ergonomics v1.21.0 (`2e5b6f0`), from v1.20.0 (`4f99372`): duplication skips the lines a declared shape prescribes
- A third topic of the literature review, Bayesian optimisation: a project as the optimisation of an unknown objective.
  It has 39 new sources, a named baseline, and a worked model on the family's own runs, a program with its inputs and 20 unit tests.
- Decision 0005, which reads the project as Bayesian optimisation and derives the stopping rule from the value of information.
- A step in the checks workflow that runs the worked model's unit tests.
- A design of a guide that proposes the next step: the problem modelled, the field's solutions mapped onto the setup, the guide designed, and a verdict ([design](design/guide.md)).
- A trace of the family's first two days, 39 rows ([trace](design/trace.md)), and a replay program on it with 36 unit tests ([replay](design/replay.md)).
- Decision 0006, which does not build the guide yet and states the bar for a spike.

### Changed

- The principle stop-at-acceptable gains its derivation and keeps its grade.
- Pinned reader-ergonomics v1.20.0 (`4f99372`), from v1.19.2 (`b9732b9`): the runner's verdicts file (`--out`), and hand-written llms.txt lines kept through a rebuild
- Tag v0.1.1 and a GitHub release of the same name.

## [0.1.0] - 2026-11-03

First release. What it holds:

### Added

- A first literature review in two topics, expressiveness and convergence, each with its frame, protocol, sources,
  review, case against, state of the art, position and baseline, and the shared bibliography.
- A candidate cost of a tree of topics, computed on the family's eight trees; nothing validates it.
- A card of three principles in two groups, each with its grade and a check.
- Two checks, `topic-cost` and `optimality-gap`, and 49 unit tests of them.
- Four decision records, the checks workflow (unit tests, then the standard's checks, with a weekly syntax and
  reference job) and the site workflow.
- Pinned reader-ergonomics v1.19.2 (`b9732b9`), the same in both workflows.

## 2026-11-02

### Added

- Pinned reader-ergonomics v1.19.2 (`b9732b9`), at the repository's start: the standard's pin, link, changelog and
  decision-record checks, which this skeleton is written to pass.
