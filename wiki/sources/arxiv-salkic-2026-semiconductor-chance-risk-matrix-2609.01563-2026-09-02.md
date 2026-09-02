---
title: "Salkić et al. 2026 - Semiconductor chance-and-risk matrix from LLM filings (arXiv 2609.01563) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, supply-chain, document-extraction, k168]
keywords: [2609.01563, semiconductor supply chain, chance-and-risk matrix, LLM extraction, knowledge graph]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-02-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-02
updated: 2026-09-02
cross-wiki-routed: osint-wiki
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — semiconductor supply-chain analytics; not local-pack SEO
- @concepts/federated-daily-research-digest.md — K168 digest fetch
- @sweeps/2026-09-02-daily.md — overnight inbox drop
- OSINT brief (repo root, not wiki/): `../../OSINT WORKSPACE/briefs/2026-09-02_k168-semiconductor-chance-risk-from-seo.md` (**thin**)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | A systematic Approach to constructing a Chance-and-Risk Matrix for Semiconductor Supply Chains |
| **Authors** | Ema Salkić, Alexander Fichtl, Philipp Ulrich, Hans Ehm, Marta Bonik, Georg Groh |
| **arXiv** | 2609.01563 (cs.CL) |
| **Filename** | `arxiv-2609.01563-a-systematic-approach-to-constructing-a-chance-a.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.01563-a-systematic-approach-to-constructing-a-chance-a.pdf` |
| **Retrieved** | 2026-09-02 |
| **Code** | No public repo URL in abstract → Watch / 0 MB |

## Narrative

Semiconductor supply chains face geopolitical, geographic-concentration, and technology-shift risks. The paper presents an end-to-end pipeline: retrieve corporate documents for semiconductor companies; use LLMs to extract described risks and opportunities; organize items in a knowledge graph (category, sources, related events); merge duplicates; rank with a three-layer mechanism (algorithmic formula + LLM relevance adjustment + expert validation).

Applied to five value-chain companies: **76,207** scored items; independent check finds **92.6%** valid. Automated rankings match expert judgment at Spearman **0.55** (risks) and **0.72** (opportunities). Trade restrictions emerge as the dominant cross-company risk.

**SEO remit:** geo-aeo digest false positive — no GBP or citation playbook. Federation: **OSINT thin steal** (LLM structured extraction from public filings → ranked intelligence graph). **Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "We present an end-to-end pipeline that retrieves corporate documents for semiconductor companies and uses large language models (LLMs) to extract the risks and opportunities they describe." [Source: arXiv 2609.01563 Abstract]

> "Applied to five companies across the value chain, the pipeline produces 76,207 scored items, of which an independent check finds 92.6% valid." [Source: arXiv 2609.01563 Abstract]
