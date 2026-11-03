# Cost on the family

> What is asked: a candidate cost of a tree of topics, computed on the README trees of the eight
> reader-ergonomics repositories. Done when one table gives each tree's cost and its costliest topic, and every
> number can be recomputed from the files by one program. Nothing validates the cost yet.

**Shape:** [report](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/shapes/report.md), a problem solved in steps.
**What this tests:** [a computed cost with provisional weights](../../principles/expressiveness/computed-cost.md).

## Caution

**Nothing validates this number.** No study has tested a cost of a tree of topics against a reader's effort
([review](review.md), strand 4). The number borrows the shape of Cognitive Complexity (Campbell 2023), which correlates with
comprehension time for code (Muñoz Barón 2020, secondary). Whether it does so for topics is the open question.

Read the table as a description of the trees, not as a ranking of quality. Grade: **not found** for topics.

## The plan

1. Fix the tree, so that every repository gives the same kind of tree.
2. Read four components from each topic.
3. Combine them into a cost, as Cognitive Complexity combines nesting and breaks.
4. Run it on the eight trees.
5. Read what the table shows, and no more.

## Step 1: Fix the tree

The model is the topic's check. Every markdown file is a topic; its parent is the README of the nearest folder above it.
The contributor guide, the changelog, translations and the checks folder are out.
The program is [checks/local/topic_cost.py](../../checks/local/topic_cost.py), the choice is
[decision 0003](../../decisions/0003-a-candidate-cost-of-a-tree-of-topics.md).

## Step 2: Read four components from each topic

- **Depth:** the parents between the topic and the root.
- **Children:** the topics whose parent it is.
- **Run:** the words of prose before its first list or table.
- **Sentence:** the words of its longest sentence.

Trap: counting headings, code and link addresses as words. They are left out of the run and the sentence.

## Step 3: Combine them

- **Breaks:** a child beyond 7, each 60 words of run beyond 60, each 10 words of sentence beyond 35.
- **Cost of a topic:** its depth, plus its breaks, each weighted by 1 plus the depth.
- **Cost of a tree:** the sum over its topics.
- **Weights and thresholds:** all PROVISIONAL, in checks/config.toml, and kept so by the check `topic-cost`.

Predict before running: which tree is costliest by total, and which by mean? The total follows the number of topics,
so the largest tree should lead it. The mean should barely move.

## Step 4: Run it on the eight trees

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

## Step 5: Read what the table shows

- **Extremes of the total:** software-design is highest (323.7) and blueprint lowest (66.1). The total follows the number of topics.
- **Extremes of the mean:** learning is highest (3.31) and blueprint lowest (2.75). The spread is small.
- **Costliest topic:** the decisions folder of the topic repository, at 19.0, because it lists 16 records, nine past the free 7.
- **Depth dominates.** Depth accounts for 76 to 90 percent of each tree's cost. The break terms matter only in a few topics.
- **Sentences:** the standard and learning hold four topics each with a sentence past 35 words, blueprint and software-design one each; the longest is 74 words.
- **Runs:** 5 to 19 topics per repository open with more than 60 words before a list or table; the longest is 366 words.

Trap: reading the mean as quality. The Caution above applies to every row.

## Checks

- **Unit tests:** `python3 -m unittest discover -s checks` tests each component, the combination, the tree and the
  check `topic-cost`. CI runs them.
- **A limit case:** a root with seven children has a cost of 0 of its own, and with eight it costs 1 (a unit test).
- **Not done: validation.** The cost has not been compared with readers. A reader study would have three steps.

1. **Material:** take topics from the family and rewrite each tree at several costs, the content held fixed.
2. **Tasks:** readers find a fact and answer a question about the tree. Record the time and the correctness.
3. **Test:** a rank correlation of cost with time and with errors, then each component dropped in turn, against two baselines: the count of topics alone, and the count of words alone.

The study is Muñoz Barón 2020's design carried from code to topics. A measure that does not beat the counts is not a measure.

**If you meet this again:** compute the number and tag its weights PROVISIONAL before anyone ranks trees by it.
A cost that has not beaten the count of topics and the count of words has not earned a verdict.
