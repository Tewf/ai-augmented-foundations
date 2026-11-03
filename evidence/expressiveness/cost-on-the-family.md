# Cost on the family

A candidate cost of a tree of topics, computed on the README trees of the eight reader-ergonomics repositories. Nothing validates it yet.

## Caution

**Nothing validates this number.** No study has tested a cost of a tree of topics against a reader's effort
([review](review.md), strand 4). The number borrows the shape of Cognitive Complexity (Campbell 2023), which correlates with
comprehension time for code (Muñoz Barón 2020, secondary). Whether it does so for topics is the open question.

Read the table as a description of the trees, not as a ranking of quality. Grade: **not found** for topics.

## The measure

The program is [checks/local/topic_cost.py](../../checks/local/topic_cost.py), the choice is [decision 0003](../../decisions/0003-a-candidate-cost-of-a-tree-of-topics.md).

- **Tree:** the model of the topic's check. Every markdown file is a topic; its parent is the README of the nearest folder above it.
- **Components:** depth, children, words before the first list or table (the run), and the longest sentence.
- **Breaks:** a child beyond 7, each 60 words of run beyond 60, each 10 words of sentence beyond 35.
- **Cost of a topic:** its depth, plus its breaks, each weighted by 1 plus the depth.
- **Cost of a tree:** the sum over its topics.
- **Weights and thresholds:** all PROVISIONAL, in checks/config.toml.

## The table

The eight members of the reader-ergonomics family, at the commits checked out on 2026-11-03. Sorted by mean cost.

| Repository | Topics | Depth | Children | Total | Mean | Costliest topic | Its cost |
|---|---|---|---|---|---|---|---|
| reader-ergonomics-learning | 63 | 3 | 10 | 208.7 | 3.31 | `evidence/practice-questions/README.md` | 11.0 |
| reader-ergonomics-presentations | 59 | 3 | 8 | 186.2 | 3.16 | `decisions/0007-diagrams-are-drawn-with-graphviz.md` | 7.2 |
| reader-ergonomics-academic | 36 | 3 | 8 | 113.2 | 3.14 | `evidence/reports/README.md` | 6.5 |
| reader-ergonomics-topic | 49 | 3 | 16 | 150.1 | 3.06 | `decisions/README.md` | 19.0 |
| reader-ergonomics-software-design | 106 | 3 | 12 | 323.7 | 3.05 | `decisions/README.md` | 11.0 |
| reader-ergonomics | 111 | 3 | 9 | 319.9 | 2.88 | `principles/collection/README.md` | 8.0 |
| reader-ergonomics-project | 25 | 3 | 8 | 70.2 | 2.81 | `shapes/examples/first-job/review.md` | 6.3 |
| reader-ergonomics-blueprint | 24 | 3 | 8 | 66.1 | 2.75 | `evidence/autoformalization/frame.md` | 7.7 |

Columns Depth and Children are the maxima over the tree.

## What the table shows

- **Extremes of the total:** software-design is highest (323.7) and blueprint lowest (66.1). The total follows the number of topics.
- **Extremes of the mean:** learning is highest (3.31) and blueprint lowest (2.75). The spread is small.
- **Costliest topic:** the decisions folder of the topic repository, at 19.0, because it lists 16 records, nine past the free 7.
- **Depth dominates.** Depth accounts for 76 to 90 percent of each tree's cost. The break terms matter only in a few topics.
- **Sentences:** the standard and learning hold four topics each with a sentence past 35 words, blueprint and software-design one each; the longest is 74 words.
- **Runs:** 5 to 19 topics per repository open with more than 60 words before a list or table; the longest is 366 words.

## What would validate it

A reader study, in three steps.

1. **Material:** take topics from the family and rewrite each tree at several costs, the content held fixed.
2. **Tasks:** readers find a fact and answer a question about the tree. Record the time and the correctness.
3. **Test:** a rank correlation of cost with time and with errors, then each component dropped in turn, against two baselines: the count of topics alone, and the count of words alone.

The study is Muñoz Barón 2020's design carried from code to topics. A measure that does not beat the counts is not a measure.
