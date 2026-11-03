# Evidence

The first review of this repository, in three topics, and the bibliography of every work it cites. The reviews follow
the method the topic's reviews share, which is not repeated here ([the topic's evidence](https://github.com/Tewf/reader-ergonomics-topic/blob/master/evidence/README.md)).

## Contents

| Part | Summary |
|---|---|
| [expressiveness](expressiveness/) | 20 new sources: what a tree or graph of topics encodes, and whether a program can compute what it costs a reader |
| [convergence](convergence/) | 23 new sources: when a project stops, at an acceptable result or the best, and what an optimum is with several wanting parties |
| [bayesian-optimisation](bayesian-optimisation/) | 39 new sources: a project read as the optimisation of an unknown objective, the choice of the next step, the stop that follows, and a worked model on the family's own runs |
| [cost on the family](expressiveness/cost-on-the-family.md) | the candidate cost of a tree of topics, computed on eight trees, not validated |
| [bibliography](bibliography.md) | every work cited, once, with a stable link |

## Shape

The three topics hold the same eight files: frame, protocol, sources, review, state of the art, position, against and
baseline. Each ends on its baseline. Grey sources are scored on Garousi 2019.

- One grey source of the third topic fell below the threshold and is an example of practice only.
- The third topic adds a worked model, a program with its inputs and tests.

## Method

The topics are first passes by one reviewer, run on 2026-11-02 and 2026-11-03, to Garousi 2019.

- **Counts:** OpenAlex (`title_and_abstract.search`, no key, no account) and the arXiv API. Semantic Scholar answered with a rate-limit reply and is not used.
- **Stopping rule:** top 6 results of each string by citations; a string stops after 5 consecutive results that add no concept.
- **Selection:** include a formal result or a practice document on the topic's questions; exclude other fields that share a word.
- **Grey sources:** scored on the 20 criteria of Garousi 2019, Table 7, in eight groups: authority, methodology, objectivity, date, position, novelty, impact and outlet tier. The threshold is 10 of 20.
- **Reading:** a number read in an abstract or a record is marked (secondary). No formal source was read in full.
- **Limits:** no second rater; counts change on a repeat; Scopus, Web of Science and publisher search boxes were not searched; no non-English literature.
