---
title: "Žatuchin 2026 — LLM brand reputation sourcing across languages (arXiv 2606.25787)"
type: source
tags: [source, arxiv, geo-aeo, citation, earned-media, multilingual, k130]
keywords: [2606.25787, citation sourcing, owned vs third-party, Wikipedia, earned media, Rankfor.AI, Zipf]
related:
  - concepts/ai-citation-sourcing-geo.md
  - sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md
  - concepts/multilingual-geo-audit.md
  - concepts/citation-building.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/geo-visibility-measurement.md
  - concepts/generative-engine-optimization.md
  - entities/tools/rankfor-ai.md
  - sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-26-daily.md
  - sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md
maturity: validated
read_status: read
created: 2026-06-26
updated: 2026-07-16
---

## Relations

- @sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md — K140 Martinez GEO survey
- @concepts/ai-citation-sourcing-geo.md — operator playbook hub (source-side layer)
- @sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md — companion paper (what AI **says**); this paper = what AI **cites**
- @concepts/multilingual-geo-audit.md — language × market citation patterns
- @concepts/citation-building.md — earned third-party co-citation discipline
- @concepts/competitive-geo-citation-factors.md — winning citation slots after retrieval
- @concepts/geo-visibility-measurement.md — audit cited domains, not only answer text
- @concepts/generative-engine-optimization.md — GEO hub
- @entities/tools/rankfor-ai.md — author/vendor; Rankfor.AI datasets
- @sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md — production mention + source-class telemetry
- @concepts/federated-daily-research-digest.md — K130 ingest
- @sweeps/2026-06-26-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | How Large Language Models Source Brand Reputation Across Languages and Markets |
| **Author** | Dmitrij Žatuchin (EUAS; Rankfor.AI) |
| **arXiv** | 2606.25787 |
| **Zenodo** | 10.5281/zenodo.20829524 |
| **Data** | open.rankfor.ai/index-2026 |
| **Filename** | `arxiv-2606.25787-how-large-language-models-source-brand-reputatio.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2606.25787-how-large-language-models-source-brand-reputatio.pdf` |
| **Retrieved** | 2026-06-26 |
| **Read status** | read (abstract, §3.1–3.5, methodology notes) |

## Narrative

**Source-side companion** to @sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md — measures **citation URLs** beneath grounded answers, not answer sentiment/recommendation share.

Merged Rankfor.AI datasets: **128 brands**, **13 languages**, **12 markets**, **167,551** URL-grounded citations (189,974 attribution rows total).

### Four corpus findings `[CONFIRMED in Žatuchin panel]`

1. **Third-party dominance** — **85.7%** citations to non-owned domains vs **14.3%** owned (NB backbone, 131,514 URL citations). AI reads third parties **4–6×** more often than owned site.
2. **Long-tail concentration** — 80% of citations from **18.2%** of domains; Zipf fit α=**0.86**, R²=0.983.
3. **Wikipedia near-universal** — top-cited domain in **11/12** languages; Lithuanian exception: **vz.lt** edges Wikipedia (4.38%).
4. **Market-specific mixes** — Poland: **YouTube** #1 (2,289 citations, 6.4%); HR/careers portals **2.1×** Polish Wikipedia citation count.

### Owned-site reality

| Pattern | Detail |
|---------|--------|
| B2B owned share | 13.1% |
| B2C owned share | 15.7% |
| High self-citation brands | Tatra Banka 34.4%, ESET 33.2%, Wise 32.4% owned |
| Zero owned citations | Some brands (e.g. Kiwi.com): AI **never** grounds in owned site |

### Model differences (NB backbone, post Gemini redirector fix)

| Model | Citations | Domains | Owned (domain) |
|-------|-----------|---------|----------------|
| Perplexity Sonar Pro | 90,276 | 15,995 | 16.8% |
| GPT-5.4 | 18,206 | 3,284 | 12.9% |
| Gemini 3.1 Pro | 23,032 | 6,568 | 5.8% |

**Methodology note:** 17.5% of NB Gemini rows used `vertexaisearch.cloud.google.com` redirectors; real domains recovered from citation-title field — load-bearing for domain rankings.

### Local-operator translation `[TENTATIVE]`

GEO visibility is **earned-media weighted**: chamber sites, local news, Yelp/listicles, YouTube (market-dependent) outweigh owned-site copy tweaks alone (@concepts/citation-building.md). Pair answer-text audits (@concepts/multilingual-geo-audit.md) with **cited-domain inventory**.

**Phase-0:** REFERENCE — Rankfor.AI author/vendor; Zenodo deposit + open.rankfor.ai index. No independent SaaS audit `[NEEDS VERIFICATION 2026-06-26]`.

## Snippets

> "85.7% of citations point to sites the brand does not own and 14.3% point to owned domains." [Source: arxiv-2606.25787 §3.1]

> "Wikipedia is the most-cited domain in 11 of 12 languages." [Source: arxiv-2606.25787 Abstract]

> "A brand's own website is a minority source even for the best self-cited brand, and a non-source for many." [Source: arxiv-2606.25787 §3.1]
