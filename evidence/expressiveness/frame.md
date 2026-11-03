# Frame: what a tree or graph of topics can encode, and what the field calls it

Step 1, read on 2026-11-02: the problem, the terms, and the names the field uses.

**Shape:** [frame](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/frame.md)

## The problem in one sentence

Which problems can be written down as a tree of topics, which need a graph, and what a person pays in attention to read either.

## Names

One row per term. A source is where this review first met the term.

| Term | What the field means by it | Source |
|---|---|---|
| **expressiveness**, expressive power | the class of objects a model can describe, compared with another model's class | Murata 2005; Höller 2014 |
| **succinctness** | how much smaller one model writes the same object than another | Bousquet-Mélou 2014 |
| **tree of topics** | the repository's unit: every topic has one parent and may hold topics of its own type | the family's topic template |
| **reference edge** | a link from one topic to a topic that is not its child | this review |
| **cyclomatic number** | m minus n plus c for a graph with m edges, n nodes and c components: the number of edges a spanning forest leaves out | this review, elementary |
| **tree decomposition**, **treewidth** | a tree of node groups that covers a graph; the width is the largest group minus one | Bodlaender 1998 |
| **monadic second-order logic (MSO)** | a logic over graphs that can state many properties; on graphs of bounded treewidth it is decidable efficiently | Courcelle 1990 |
| **HTN planning** | planning by decomposing tasks into subtasks in a network | Erol 1994; Höller 2014 |
| **graph database model** | a data model whose schema and instances are graphs | Angles 2008 |
| **cognitive load** | the demand a task puts on a limited working memory | Sweller 1998; Paas 2003 |
| **chunk** | a unit held in working memory; capacity is three to five | Cowan 2001 |
| **understandability metric** | a number computed from code that is meant to predict how hard it is to understand | Scalabrino 2021; Muñoz Barón 2020 |
| **Cognitive Complexity** | a code metric that adds a cost for each break in flow and for each level of nesting | Campbell 2023 |
| **SKOS** | a W3C model for thesauri: concepts with broader, narrower and related links | Miles 2009 |

## What practice calls it

- Practitioners say **hierarchy versus network**, **taxonomy versus ontology** and **tree versus graph notes**. The field says expressive power, succinctness and treewidth.
- Practitioners say **too complex** or **hard to follow**. The field says cognitive load (education) and understandability (software).

## The repository's name against the field's

- The repository says **complete**. No source in this pass uses that word for a model of topics. The field says **expressive power**, and for a language class, **language classification**.
- No single field owns the problem. It is split between formal language theory (what a model can describe), graph theory (how tree-like a graph is) and cognitive science (what a reader bears).
- The repository keeps its provisional name. The mismatch is reported, not repaired.

## Sub-questions

| Id | Sub-question | Answers |
|---|---|---|
| X1 | What does a tree encode, and what does it need a graph for? | front page: Expressiveness |
| X2 | Is there a problem that needs neither? | front page: Expressiveness |
| X3 | What formal classes do hierarchical decomposition models fall in? | X1 |
| X4 | What is a computable measure of cognitive cost, and how well is it graded? | front page: Cost |

## Links, not repeated

- The node model, reuse by reference, cycles and schema classes are in [the topic's document-model review](https://github.com/Tewf/reader-ergonomics-topic/tree/master/evidence/document-model).
- Depth and its display are in [the topic's progressive-disclosure review](https://github.com/Tewf/reader-ergonomics-topic/tree/master/evidence/progressive-disclosure).
- Folder breadth and depth for a reader are graded in [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/principles/collection/browsable-folders.md).
