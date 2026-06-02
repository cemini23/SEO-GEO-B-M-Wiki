---
title: "Dong et al. 2025 — SafeSearch: Red-Teaming LLM-Based Search Agents"
type: source
tags: [geo-aeo, academic-paper, record-only, search-agents, safety]
keywords: [SafeSearch, search agent, misinformation, prompt injection, unreliable search results]
related:
  - concepts/generative-engine-optimization.md
  - sweeps/2026-06-01-daily.md
  - sources/ptah-2026-verifiable-multimodal-deep-research.md
  - sources/dong-2025-safesearch-red-teaming.md
  - @cybersecurity-wiki/sources/dong-2025-safesearch-red-teaming.md
maturity: draft
read_status: skimmed
created: 2026-06-01
updated: 2026-06-01
cross-wiki-routed: cybersecurity-wiki
---

## Relations

- @concepts/generative-engine-optimization.md — AI answer engines retrieve open-web sources; unreliable pages can skew citations
- @cybersecurity-wiki/sources/dong-2025-safesearch-red-teaming.md — primary home (agent safety / red teaming)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SafeSearch: Automated Red-Teaming of LLM-Based Search Agents |
| **Authors** | Jianshuo Dong et al. |
| **arXiv** | 2509.23694 |
| **Code** | https://github.com/jianshuod/SafeSearch |
| **Filename** | `arxiv-2509.23694-safesearch-automated-red-teaming-of-llm-based-se.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-01 |
| **Read status** | skimmed — routed from digest local-seo query lane; primary domain is agent security |

## Narrative

**Record-only in this wiki.** SafeSearch benchmarks how LLM search agents fail when **benign queries** retrieve **unreliable web results** (misinformation, prompt injection, bias, etc.). 300 test cases; up to 90.5% attack success rate on some model/scaffold pairs.

**Why it appears here:** answer engines (ChatGPT Search, Perplexity, Google AI Overviews) share the same retrieval→synthesis pipeline GEO operators optimize for. Low-quality or manipulable sources in the retrieval set can distort citations — adjacent to spam/fake-review attack surfaces documented in @concepts/reviews-reputation-management.md.

**Primary routing:** security evaluation methodology → @cybersecurity-wiki/sources/dong-2025-safesearch-red-teaming.md.

## Snippets

> "Unreliable search results can mislead agents into producing unsafe outputs… 4.3% of top-ranked results come from content farms or similarly low-credibility websites." — §1 Introduction [Source: arxiv.org/abs/2509.23694 (retrieved 2026-06-01)]
