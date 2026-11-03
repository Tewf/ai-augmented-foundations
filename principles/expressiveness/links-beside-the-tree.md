# Links beside the tree

**Claim:** a relation the tree of topics does not hold is a typed link beside it, and a tree plus m minus n plus c such links encodes any finite graph.

- **Grade:** exact by construction for the count of links; supported with caveat for treewidth, read in abstracts; convention, untested, for keeping a tree and adding links.
- **Evidence:** [expressiveness review](../../evidence/expressiveness/review.md), strands 2 and 3 (Bodlaender 1998, Courcelle 1990, Miles 2009); [state of the art](../../evidence/expressiveness/state-of-the-art.md), row X1; [position](../../evidence/expressiveness/position.md).
- **Check:** `links` (exact: every link resolves, so every reference edge exists). Counting the links beyond the tree has no program yet: judgment. A program could list the links between topics that are not parent and child, and print the count m minus n plus c.
- **Reader styles:** none.

## What it asks

- Give each topic one parent, the README of its folder.
- Write a relation that is not parent and child as a link in the text, with the words that say what the relation is.
- Count the links beyond the tree. A tree has none. Each one is a price the reader pays to follow the relation.

## Why

- A graph with n nodes, m edges and c components leaves m minus n plus c edges out of any spanning forest. A tree plus those edges is the graph. This is exact (Bodlaender 1998 gives the field's measure of the same idea, treewidth, where a tree has width 1).
- The widest practice in this pass keeps a tree and adds links beside it: SKOS has `broader` and `narrower` for the hierarchy and `related` for the rest (Miles 2009). No problem that needs neither a tree nor a graph was found.

## Limits

- Without types the question is nearly trivial: one topic holding all the text encodes anything. Typed content is where it bites, and Höller 2014 is the nearest model, for plans.
- Treewidth is proved for graphs, and applied to topics here by analogy.
- Every link costs the reader a decision. The standard's [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/principles/collection/one-place-per-fact.md) says where that trade stops.
