# Protocol: how the pool on expressiveness and cost was built

Search strings and counts for the expressiveness pool follow. Defined terms: [frame](frame.md). Included works: [sources](sources.md). Shared rules: [method](../README.md#method).

## 1. Why grey literature

Answers yes to questions 1 to 6 of Garousi 2019, Table 4 (question 7 not measured). Thesaurus and documentation models come from standards, no study of a tree of topics was found, and the code metrics sit in industrial tools whose validation is separate.

## 2. Questions

X1 to X4 of [frame](frame.md).

## 3. Existing reviews

- The topic's three reviews were read first and are linked, not repeated.
- Surveys met and used: Angles 2008 (graph models), Bodlaender 1998 (treewidth), Sweller 1998 and Paas 2003 (cognitive load), Cowan 2001 (capacity).
- No review of the expressiveness of a tree of topics was found.

## 4. Formal search

Counts were taken on 2026-11-02 by the method in the evidence README.

| Id | String | OpenAlex | arXiv | Result |
|---|---|---|---|---|
| E1 | HTN planning | 509 | 33 | Erol 1994 found through the list |
| E2 | hierarchical task network | 774 | 45 | same |
| E3 | hierarchical planning | 1821 | 236 | noisy, Höller 2014 met by its own title |
| E4 | treewidth | 4655 | 1667 | Bodlaender 1998 |
| E5 | tree decomposition | 2197 | 541 | same |
| E6 | monadic second-order logic | 1266 | 266 | Courcelle 1990 |
| E7 | graph database models | 110 | 7 | Angles 2008 |
| E8 | directed hypergraph | 593 | 122 | read, none kept: held by the topic |
| E9 | unranked trees | 189 | 22 | no concept added |
| E10 | XML schema languages | 177 | 2 | Murata 2005, linked |
| E11 | minimal DAG | 16 | 5 | Bousquet-Mélou 2014 |
| E12 | AND/OR graph | 669 | 151721 | arXiv counts the logical connective, so noise; held by the topic |
| E13 | cognitive load theory | 6206 | 51 | Sweller 1998 |
| E14 | cognitive load measurement | 265 | 7 | Paas 2003 |
| E15 | cognitive complexity | 4804 | 121 | noise: psychology of personality |
| E16 | code comprehension | 976 | 198 | no concept added after 5 results |
| E17 | hypertext | 22911 | 164 | noise: web and search engines |
| E18 | hypertext disorientation | 3 | 0 | no concept added |
| E19 | formality considered harmful | 3 | 0 | Shipman 1999 |
| E20 | knowledge organization system | 1464 | 39 | the SKOS reference found |
| E21 | tree-structured knowledge | 25 | 5 | no concept added |
| E22 | formal representations | 1199 | 248 | noise |

- Strings that returned zero because they were too long or mis-quoted: "HTN planning expressiveness", "expressive power of tree and graph query languages", "cognitive complexity understandability", "code understandability metrics". Zero here is a statement about the query. The two last were retried by title on arXiv and found Muñoz Barón 2020.
- Snowballing: the code-metric pair (Scalabrino 2021, Muñoz Barón 2020) was met as each other's comparison. De Jong 2010 was found by title as the standard critique of cognitive load theory.

## 5. Grey search

- One search by producer, not by string: the W3C Recommendations list for thesauri (SKOS), and the white paper of the best-known code metric.
- Not searched: forums and Q/A sites, talks, engineering blogs, note-taking communities. A reader of this review should treat practice here as a sample of two standards-grade sources.

## 6. Stopping, selection, scoring, synthesis and limits

As in the evidence README. The stopping rule ended the strings E9, E16, E18 and E21. The scores of grey sources are in [sources](sources.md).
