# A computed cost with provisional weights

**Claim:** the cost of a tree of topics is computed by a program, every weight is tagged PROVISIONAL, and no one ranks trees by it until a reader study has validated it.

- **Grade:** measured for code only (Muñoz Barón 2020 and Scalabrino 2021, both secondary); untested for topics, where every weight is a guess.
- **Evidence:** [expressiveness review](../../evidence/expressiveness/review.md), strand 4 (Cowan 2001, Scalabrino 2021, Muñoz Barón 2020, Campbell 2023); [state of the art](../../evidence/expressiveness/state-of-the-art.md), row X4; [cost on the family](../../evidence/expressiveness/cost-on-the-family.md), the measure computed on eight trees; [decision 0003](../../decisions/0003-a-candidate-cost-of-a-tree-of-topics.md).
- **Check:** `topic-cost` (an error for a weight not tagged PROVISIONAL in `checks/config.toml`; a warning for a topic past its budget) and `provisional-tags` (an old tag becomes a question).
- **Reader styles:** none.

## What it asks

- Compute the cost with the program, from the files, so that it is the same on every run.
- Tag each weight and threshold PROVISIONAL where it lives, in the config. At present these are: `depth_weight`, `nesting_weight`, `fan_free`, `fan_weight`, `run_free`, `run_step`, `run_weight`, `sentence_free`, `sentence_step`, `sentence_weight` and `topic_budget`.
- Put the caution beside any table of costs: nothing validates it, and it describes trees, it does not rank their quality.

## Why

- A measure that is computed can be tested against readers, and one that is argued cannot. The shape borrows Cognitive Complexity, the one code count with a meta-analysis behind it.
- A broad set of code metrics failed to capture understandability, so a plausible count proves nothing. A measure that does not beat the count of topics and the count of words is not a measure.
- Each component is a unit the standard already reasons about: [shallow outline](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/document/shallow-outline.md), [browsable folders](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/collection/browsable-folders.md), [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/page/signal-the-structure.md) and [even information density](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/sentence/even-information-density.md).

## Limits

- Depth supplies 76 to 90 percent of the cost on the family's eight trees, so the number mostly counts levels until the weights are set.
- A long run of prose that is not a list can be a good explanation, and the measure cannot tell.
- The `topic-cost` warning is a prompt to read a topic, not a verdict. The study that would validate the cost is described in [cost on the family](../../evidence/expressiveness/cost-on-the-family.md).
