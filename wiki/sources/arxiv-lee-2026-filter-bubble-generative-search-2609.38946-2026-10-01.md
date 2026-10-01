---
title: "Lee et al. 2026 - Generative AI search diversifies collective attention (arXiv 2609.38946)"
type: source
tags: [source, arxiv, geo-aeo, field-experiment, zero-click, citations, attention, k284]
keywords: [2609.38946, filter bubble, Washington Post, AI overviews, RAG search, shared information, topic concentration, cited sources]
related:
  - concepts/generative-engine-optimization.md
  - concepts/geo-visibility-measurement.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sources/housingwire-2026-answer-engine-optimization-zero-click-gbp-2026-06-29.md
  - sources/newsletter-rss-sparktoro-2026-08-14-zero-click.md
  - sources/aggarwal-2024-geo-paper.md
  - sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md
  - sweeps/2026-10-01-daily.md
maturity: validated
read_status: deep-read
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- @concepts/generative-engine-optimization.md — GEO/AEO hub; zero-click evidence with a causal design
- @concepts/geo-visibility-measurement.md — consumption as an outcome, not just citation share
- @concepts/ai-citation-sourcing-geo.md — cited sources win the click
- @concepts/evidence-ecosystem-geo.md — the cited-article layer as a distinct surface
- @sources/housingwire-2026-answer-engine-optimization-zero-click-gbp-2026-06-29.md — practitioner zero-click stats; this is the controlled version
- @sources/newsletter-rss-sparktoro-2026-08-14-zero-click.md — "website is the permanent home"; this paper prices the click loss
- @sources/aggarwal-2024-geo-paper.md — GEO's original single-turn framing
- @sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md — K283 AX: readability at the drill-down
- @concepts/corpus-overflow-out-of-scope.md — K284 sibling stubs
- @concepts/federated-daily-research-digest.md — K284 digest fetch
- @sweeps/2026-10-01-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Breaking News Out of the Filter Bubble: Generative AI Search Diversifies Collective Attention and Raises Shared Information Consumption |
| **Authors** | Heeseung Andrew Lee (UT Dallas), Dokyun (DK) Lee (Boston University), Gwanhoo Lee (American University), Dongwon Lee (HKUST) |
| **Status** | **Working paper** — not peer reviewed |
| **arXiv** | 2609.38946v1 [cs.CY], 30 Sep 2026 |
| **Pages** | 31 (8-page main paper + supplementary) |
| **Filename** | `arxiv-2609.38946-breaking-news-out-of-the-filter-bubble-generativ.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.38946-breaking-news-out-of-the-filter-bubble-generativ.pdf` |
| **Retrieved** | 2026-10-01 |
| **Code / data** | None stated — proprietary newsroom archive, 37,561 readers |

## Narrative

**The design.** A **38-day randomized field experiment** (1 October – 7 November 2024) with **37,561 readers at The Washington Post**, run **before the public launch of "Ask The Post AI"**. Assignment used a browser cookie at each reader's first on-site search. Both groups searched the *same archive*; treatment readers additionally received **AI answers with article citations above the conventional results**. Consumption is measured across both displayed answers and opened articles. This is a rare causal design in the AI-search literature — most GEO evidence is observational or a fixed-benchmark test.

**Finding 1 — AI search raises shared information consumption.** Per-reader consumption of *shared* information (topics popular across the audience) rises **+69%** (P<0.001). The share of readers reached by shared information rises from **37% to 55%**. Counting articles alone gives 36.9% control vs 35.1% treatment — **including the AI answers is what produces the lift** (+20.3 pp, to 55.4%).

**Finding 2 — total consumption rises, mostly via the answer.** Total information consumed per reader rises **+82%**, decomposed into **29% more searches** and **41% more information per search**. Time on site rises only 13%, so consumption **per minute rises 62%**. Word counts: 1,710 → 1,953 per reader (+14.2%), of which **126.1 words come from AI answers**.

**Finding 3 — consumption becomes less concentrated and shifts to less-popular topics.** Aggregate effective number of topics rises **44.4 → 46.4**. The mean individual share on the ten most popular topics falls **4.0 pp** (40.7% → 36.7%); the aggregate share falls 4.4 pp. Among treatment readers who opened articles, the effective number of topics rises from **3.81** (articles alone) to **5.48** (articles + answers).

**Finding 4 — the AI answer, not the article, drives the shift.** AI answers account for **98.0%** of the increase in shared-information consumption and **89.2%** of the increase in non-core-information consumption. The mechanism is stated plainly: answers summarise multiple cited-source articles within a single search.

**Finding 5 — clicks move from conventional results to cited sources.** Compared with control: conventional-result clicks fall **21 pp**, browsing **5 pp**; **cited-source clicks rise 14 pp**; and **follow-up searches without an article click rise 11 pp**. So the AI answer both redistributes the click and captures information delivery that used to require one.

**Finding 6 — no demand-side or supply-side explanation.** The authors find no evidence that treatment readers searched for less-popular topics, or that cited-source lists offered less-popular articles than conventional results. The shift comes from the answer layer.

**SEO remit for this wiki:** this is the **controlled** version of the zero-click claim already in the wiki from practitioner sources. It gives GEO work a measured outcome (consumption, reach, concentration) alongside citation share. Two operator-relevant readings:

1. **Cited-source clicks are the growth channel; conventional-result clicks shrink.** Being *in* the AI answer's citation set is what converts, and it converts better than ranking below it. This is the click-side counterpart to K283's readability finding (@sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md).
2. **The answer now carries the information.** 98% of the shared-information gain arrives without an article click. A business whose facts live only behind a click reaches fewer people than one whose facts are in the answer. That is the practical argument for the canonical-facts work in @concepts/canonical-business-facts-geo.md.

**Publisher-side note:** the paper's headline is *counter* to the filter-bubble hypothesis — AI search **diversified** collective attention and raised overlap. Read carefully: that is a statement about a news archive with a professional editorial layer, not about an open web of commercial listings.

## Caveats

- **Working paper, not peer reviewed.**
- **One newsroom, one archive.** A single major newspaper; results may not generalize to other publishers, to open-web search, or to commercial/local queries. **No local, geographic, or near-me queries.**
- **Treatment is a specific UI**: AI answers *with article citations* displayed **above** conventional results. A different placement or answer format could move differently.
- **Topic model dependence.** Results are checked under an alternative topic model and with politics excluded (differences shrink but hold). Concentration differences *within* individual readers are small and not significant when only articles are counted.
- **Consumption ≠ belief.** The paper measures what was displayed and opened, not what readers learned or believed.
- Local-service generalization: `[NEEDS VERIFICATION 2026-10-01]`.

## Snippets

> "We find that AI search expands the reach of widely read topics and increases overlap in readers' topic consumption." [Source: arXiv 2609.38946 Abstract]

> "AI answers account for most of the increase in shared information, delivering it without requiring article clicks and broadening exposure beyond the articles readers open." [Source: arXiv 2609.38946 Abstract]

> "AI answers account for 98.0% of the increase in shared information consumption and 89.2% of the increase in non-core information consumption." [Source: arXiv 2609.38946 — Table S5]

> "Compared with Control, conventional-result clicks fall by 21 percentage points and browsing by 5 points, while cited-source clicks rise by 14 points and follow-up searches without an article click rise by 11 points." [Source: arXiv 2609.38946 — Results]

> "Total information consumption per reader rises by 82%, reflecting both 29% more searches and 41% more information per search." [Source: arXiv 2609.38946 — Results]

## Phase-0 (tool audit)

**No tool to audit.** Field experiment + proprietary newsroom dataset. No repository, no released code, no software artifact. 0 SEO Adopt, 0 MB runtime.

## Phase-1 (wire)

**policy_wired** into @concepts/generative-engine-optimization.md (zero-click, causally measured). No new hands-on brief — the operator action is already covered by the citation-sourcing and canonical-facts workflows. No runtime wire, no MCP, no `settings.json` change.
