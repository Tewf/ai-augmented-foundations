# Protocol: how the pool on expressiveness and cost was built

Search strings and counts for the expressiveness pool follow. Defined terms: [frame](frame.md). Included works: [sources](sources.md). Shared rules: [method](../README.md#method).

**Shape:** [protocol](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/protocol.md)

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

## 7. Forward citations (2026-11-03)

The three sources the review cites most were taken as seeds: Sweller 1998, Paas 2003 and Bodlaender 1998. Each has 2 keys in [review](review.md), tied with Angles 2008. The three with the largest bodies of citing work were kept. Citing works were listed from OpenAlex, with the filter "published after 2019" and, for the two large seeds, a title-and-abstract term.

| Id | Seed | Filter on citing works | Matching | Retrieved and screened by title |
|---|---|---|---|---|
| F1 | Bodlaender 1998 | published after 2019, abstract mentions treewidth | 115 | 115 |
| F2 | Sweller 1998 | published after 2019, abstract mentions cognitive load | 1104 | 300, the most cited |
| F3 | Paas 2003 | published after 2019, abstract mentions cognitive load measurement | 79 | 79 |

- Total: 1,298 matching, 494 retrieved and screened by title. Six abstracts were opened: five works were added and one was not (a 2020 Festschrift volume on treewidth: the abstract names no result).
- Added: Gima 2024 (from F1); Krieglstein 2022 and Berssanette 2021 (from F2); Quintero-Manes 2024 and Ledneva 2021 (from F3). Each changes or sharpens a finding in [review](review.md), strand 2 or 4, or in [against](against.md).
- Every number read from an abstract is marked secondary in the review.
- Not searched: citing works before 2020, the 804 matching works of F2 that were not retrieved, and a second index.

## 8. A second rater on the grey sources (2026-11-03)

Each grey source was scored again, independently, by a second rater.

- The rater was a language model, one source per call.
- It was given the 20 criteria of Garousi 2019, Table 7, and the rule that a part it cannot see scores 0.
- It received the cleaned text of the source and returned the eight subtotals.
- Disagreements of more than 3 points on the total were settled by rereading the source.
- A score changes only with the reason written.

| Source | Review, first | Second rater: A, M, O, D, P, N, I, T | Second rater, total | Difference | Review, after |
|---|---|---|---|---|---|
| Miles 2009 | 17.5 | 2, 2, 1, 1, 0, 0, 0, 1 | 7 | 10.5 | 16 |
| Campbell 2023 | 14 | 1, 4, 0, 1, 0, 1, 0, 1 | 9 | 5 | 11 |

The second rater's subtotals for Campbell 2023 sum to 8 and it wrote a total of 9. Both are recorded as given, and the difference uses its total of 9.

Rereading, with the reason:

- **Miles 2009, A 4 to 3:** the text names two editors with their institutions, which holds A1 and A2. It shows neither their other work nor their expertise, which the first score had credited.
- **Miles 2009, O 4 to 3:** a specification has no data to follow, so O4 does not hold.
- **Miles 2009, D 0.5 to 1:** the Recommendation prints its date, 2009-08-18.
- **Campbell 2023, A 3 to 1.5:** the text names the author and the company, and shows nothing else about her work.
- **Campbell 2023, M 3 to 4.5:** the white paper states its aim, its rules for counting and worked examples, which the first score had undervalued.
- **Campbell 2023, O 2 to 0:** the producer sells the tool that reports the metric, so O3 is 0, and the paper gives no data on readers' judgments.
- **Campbell 2023, I 1 to 0:** the text shows no citation or adoption signal.


Agreement over the four grey sources of both topics, on the totals out of 20:

- **Mean absolute difference:** 8.4 points ((10.5 + 5 + 7.5 + 10.5) / 4 = 8.375). After the rereading below, 6.3.
- **Kappa on the threshold decision (10 of 20):** 0. The review put all four above the threshold and the second rater put all four below, so observed agreement is 0 and so is the agreement expected by chance. With four sources and no variation in either rater, the figure shows no agreement and little more.
- **Review decisions:** all four stay above the threshold after the rereading. Schwaber 2020, in the convergence topic, now sits at the threshold itself.
- **Reading:** the second rater scored low on every source and gave 0 to whatever it could not see in the excerpt. Its totals show how much of each score rests on facts outside the page text, such as authorship and adoption. They do not show that the review's scores were wrong.

Limits: four sources; one rating each; the second rater saw an excerpt, not the whole document, in a single call per source.

Agreement for this topic alone: mean absolute difference 7.75, both sources above the threshold for the review and below it for the second rater.
