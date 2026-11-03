# Expressiveness: what a tree or graph of topics encodes, and what it costs a reader

The first review of this repository: which problems a tree of topics encodes, which need a graph, and whether a program can compute the cost of reading either.

- Pool: 15 new sources: 13 formal, 2 grey; 1 more is linked from a sibling review.
- Grey scores are in the sources file, all above 10 of 20.
- A first pass: abstracts and records.

## Files

| File | Role |
|---|---|
| [frame](frame.md) | step 1: the problem and the field's names |
| [protocol](protocol.md) | how the pool was searched and scored |
| [sources](sources.md) | the pool and its quality |
| [review](review.md) | step 2: strands, surveys first |
| [state of the art](state-of-the-art.md) | step 3: records and bounds |
| [position](position.md) | step 4: known, unknown, added |
| [against](against.md) | the evidence against |
| [baseline](baseline.md) | step 5: the named baselines |
| [cost on the family](cost-on-the-family.md) | the candidate cost of a tree of topics, computed on eight trees, not validated |

## Claims

| Claim | Grade | Where |
|---|---|---|
| A tree plus m minus n plus c reference edges encodes any finite graph | supported with caveat (elementary construction) | review.md, strand 2 |
| Treewidth measures how tree-like a graph is | supported with caveat (theorems, abstracts only) | review.md, strand 2 |
| HTN plan languages are always context-sensitive | supported with caveat (secondary) | review.md, strand 1 |
| Standards for thesauri keep a tree and add links beside it | convention, untested | review.md, strand 3 |
| Working memory holds three to five chunks | measured (secondary) | review.md, strand 4 |
| 121 code metrics did not capture understandability | measured (secondary) | review.md, strand 4 |
| Cognitive Complexity correlates with comprehension time | measured, code only (secondary) | review.md, strand 4 |
| A validated cost measure for a tree of topics | not found | position.md |
| A problem that needs neither a tree nor a graph | not found | position.md |
