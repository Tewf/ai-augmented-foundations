# Position: what is known, what is not, and what this repository adds

Step 4. "Nobody has done this" and "we have not done this here" are kept apart.

## What is known

- A tree with reference edges encodes any finite graph. The number of reference edges is at least the cyclomatic number.
- The field measures how tree-like a graph is by treewidth (Bodlaender 1998). A tree has width 1.
- Hierarchical decomposition has formal language classes (Höller 2014), and its complexity depends on what the networks may contain (Erol 1994).
- Standards for thesauri keep a tree and add links beside it (Miles 2009).
- Working memory holds three to five chunks (Cowan 2001).

## What is not known

- Nobody was found who states what a tree of topics, with typed content, can and cannot encode. This is "not found in this search", not "nobody".
- No cost measure for a tree of topics has been validated. For code, a count has partial support and a wide set had none.
- The same shape of question for documentation has the topic's reviews, which are about storing and showing, not about completeness.

## What this repository adds, and does not

- The completeness question as asked here is nearly trivial without types: a single topic holding the whole text encodes anything.
- The question becomes real when content is typed and a program checks it. Then the class of the checkable fragment matters (Höller 2014 is the nearest model).
- The repository can state which checks a tree allows, and which a graph needs. It cannot claim a new result: the parts are known.
- A cost measure of its own is open. The code metrics are the baseline, not an answer.

## Candidate rules, not adopted

- Count reference edges beside depth and breadth. Grade: convention, untested.
- Report the cyclomatic number of a collection as the price of its links. Grade: convention, untested.
