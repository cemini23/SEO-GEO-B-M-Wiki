---
title: "Aggarwal et al. 2024 — GEO: Generative Engine Optimization (KDD '24)"
type: source
tags: [seo, geo-aeo, academic-paper, foundational, hub]
keywords: [GEO, generative engine optimization, AEO, citation visibility, GEO-bench, position-adjusted word count, quotation addition, statistics addition]
related:
  - concepts/generative-engine-optimization.md
  - concepts/content-strategy-local.md
  - concepts/schema-markup-local.md
  - entities/tools/geo-seo-claude.md
  - sources/vishwakarma-2026-competitive-geo-sigir.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/citation-verification-aeo.md
  - sources/arxiv-caption-injection-2511.04080-2026-06-08.md
maturity: validated
read_status: deep-read
created: 2026-05-07
updated: 2026-06-08
---

## Relations

- @concepts/generative-engine-optimization.md
- @concepts/content-strategy-local.md
- @concepts/schema-markup-local.md
- @entities/tools/geo-seo-claude.md
- @sources/vishwakarma-2026-competitive-geo-sigir.md — SIGIR '26 competitive citation preference
- @concepts/competitive-geo-citation-factors.md
- @concepts/citation-verification-aeo.md — visibility vs claim–source accuracy
- @sources/arxiv-caption-injection-2511.04080-2026-06-08.md — replicates Aggarwal baselines on MRAMG; statistics/quotation underperformed in that benchmark (domain-alignment caveat)

## Raw Concept

- **Title**: GEO: Generative Engine Optimization
- **Authors**: Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande
- **Affiliations**: IIT Delhi, Princeton University, independent researchers
- **Venue**: KDD '24 (30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining), Barcelona, August 2024
- **Type**: peer-reviewed academic paper
- **DOI**: 10.1145/3637528.3671900
- **arXiv**: 2311.09735v3
- **Pages**: 12
- **Filename**: `GEO- Generative Engine Optimization.pdf`
- **Location**: `raw-sources/` (laptop-local; gitignored)
- **Retrieved**: 2026-05-07
- **Read status**: deep-read

This is the **seminal academic paper that defines the field of GEO** (Generative Engine Optimization). When this wiki references "GEO" in the generative-engine sense, this paper is the canonical reference.

## Narrative

The paper introduces GEO as the first formal framework for optimizing web content visibility within generative-engine responses (AI engines that synthesize answers from multiple sources with inline citations — e.g. ChatGPT browsing, Perplexity, Google AI Overviews, BingChat). Traditional keyword-based SEO does NOT translate to generative engines; the paper provides empirical evidence for which optimization tactics actually work and which fail.

### Definitions and framework

A **Generative Engine (GE)** is a system that:
1. Takes a user query and returns a natural-language response with inline citations
2. Combines a search engine (for source retrieval) with one or more generative LLMs (for query reformulation, summarization, and final response generation)
3. Returns a structured response with citations rather than a ranked list of links

The authors propose **impression metrics** specifically designed for generative engines (since traditional ranked-list metrics don't apply):

- **Word Count Impression** — fraction of the response's word count attributable to a given source
- **Position-Adjusted Word Count** — same, but weighted with exponentially decaying weight by position (earlier sentences count more)
- **Subjective Impression** — composite of relevance, influence, uniqueness, subjective position, click-likelihood, diversity (evaluated via G-Eval / GPT-3.5)

### Experimental setup

- **Benchmark**: GEO-bench, 10K queries across 9 datasets (MS Marco, ORCAS-1, Natural Questions, AllSouls, LIMA, Davinci-Debate, Perplexity Discover, ELI-5, GPT-4 generated). Tagged across 25 domains, 9 query types.
- **Generative engine setup**: top-5 sources from Google → GPT-3.5-turbo response generation
- **Real-world validation**: also tested on Perplexity.ai (deployed engine)
- **9 GEO methods evaluated** vs unmodified-baseline (`No Optimization`)

### Headline results — what works, what fails

| Method | Position-Adjusted Word Count (vs baseline 19.3) | Verdict |
|---|---|---|
| **Quotation Addition** | 27.2 (+41%) | **Best** — credible quotes from cited sources |
| **Statistics Addition** | 25.2 (+31%) | **High** — quantitative stats over qualitative claims |
| **Fluency Optimization** | 24.7 (+28%) | **High** — improve readability of existing text |
| **Cite Sources** | 24.6 (+27%) | **High** — add citations to credible sources |
| **Technical Terms** | 22.7 (+18%) | Moderate — domain-specific terminology |
| **Easy-to-Understand** | 22.0 (+14%) | Moderate — simpler language |
| **Authoritative** | 21.3 (+10%) | Modest — persuasive/authoritative tone |
| **Unique Words** | 20.5 (+6%) | Negligible |
| **Keyword Stuffing** | 17.7 (-8%) | **NEGATIVE** — traditional SEO tactic *backfires* |

### Most important finding for small / local businesses

GEO methods **disproportionately help lower-ranked websites**. Table 2 of the paper shows that on Cite Sources:

- Rank-1 source: **-30.3%** visibility (top sites lose share)
- Rank-2 source: +2.5%
- Rank-3 source: +20.4%
- Rank-4 source: +15.5%
- Rank-5 source: **+115.1%** visibility

The authors explicitly frame this as **democratizing**: traditional SEO favors big sites with backlink budgets; GEO favors *content quality* (citations, statistics, fluency), which a small barbershop's website can match without a SEM budget.

### Domain-specific top-performers

Different GEO methods work best for different content categories:

| Method | Top categories |
|---|---|
| Authoritative | Debate, History, Science |
| Fluency Optimization | **Business**, Science, Health |
| Cite Sources | Statement, Facts, Law & Gov. |
| Quotation Addition | People & Society, Explanation, History |
| Statistics Addition | Law & Gov., Debate, Opinion |

For a barbershop website (which falls under "Business"), **Fluency Optimization is the primary lever**, with Quotation Addition + Statistics Addition + Cite Sources as the secondary stack.

### Combination findings

Combining GEO methods amplifies effect:
- Best pair: **Fluency Optimization + Statistics Addition** (+35.8% combined)
- Cite Sources is most useful in combination with other methods (avg +31.4% across pairs)
- Single best method tops out at +41%; combined methods can exceed this (Section 5.3, Figure 4)

### Real-world Perplexity.ai validation

The paper re-ran on Perplexity.ai (a deployed engine) and found:
- Quotation Addition: +22% (still the best)
- Statistics Addition: +37% on Subjective Impression
- Keyword Stuffing: **-10% worse than baseline** (replicated negative finding)

This generalizes the lab findings to a real production engine.

### What the paper does NOT cover (gaps for our wiki to track)

- Local-business-specific queries — the GEO-bench benchmark is general-domain; effectiveness on geo-bounded local queries (`barbershop davie fl`) is **not directly tested** `[NEEDS VERIFICATION 2026-05-07]`
- Schema markup (JSON-LD) — the paper focuses on prose-level content edits; how `LocalBusiness` / `BarberShop` schema interacts with the measured methods is not in scope. See @concepts/schema-markup-local.md.
- Engine-by-engine differences — only GPT-3.5-turbo (in-house GE) and Perplexity tested. Behavior on Google AI Overviews, Claude, Gemini may differ
- Decay over time — whether visibility lifts persist across engine retraining is not measured

## Snippets

> "Our top-performing methods, Cite Sources, Quotation Addition, and Statistics Addition, achieved a relative improvement of 30-40% on the Position-Adjusted Word Count metric and 15-30% on the Subjective Impression metric." [Source: aggarwal-2024-geo-paper p.6 §4]

> "Lower-ranked websites, which typically struggle for visibility, benefit significantly more from GEO. ... Cite Sources method led to a substantial 115.1% increase in visibility for websites ranked fifth in SERP, while on average, the visibility of the top-ranked website decreased by 30.3%." [Source: aggarwal-2024-geo-paper p.7 §5.2]

> "[We] evaluate keyword stuffing, i.e., adding more relevant keywords to website content. While widely used for Search Engine Optimization, we find such methods offer little to no improvement on generative engine's responses. This underscores the need for website owners to rethink optimization strategies for generative engines, as techniques effective in search engines may not translate to success in this new paradigm." [Source: aggarwal-2024-geo-paper p.7 §4]

> "[T]he combination of Generative Engine Optimization methods can enhance performance, with the best combination (Fluency Optimization and Statistics Addition) outperforming any single GEO strategy by more than 5.5%." [Source: aggarwal-2024-geo-paper p.8 §5.3]
