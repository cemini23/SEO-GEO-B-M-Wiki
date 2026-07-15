---
title: "Geng 2026 - DeepSearch-World self-distillation for deep search agents (arXiv 2607.07820)"
type: source
tags: [source, arxiv, geo-aeo, agentic-search, self-distillation, k139]
keywords: [2607.07820, DeepSearch-World, DeepSearch-Evolve, BrowseComp, GAIA, HotpotQA, entity hit, scaffold, verifiable environment]
related:
  - concepts/process-verified-agentic-search-geo.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/generative-engine-optimization.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/geo-visibility-measurement.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/content-strategy-local.md
  - sources/arxiv-ye-2026-ecogeo-trajectory-aware-evidence-ecosystems-2605.12887-2026-07-04.md
  - sources/score-2026-self-evolving-deep-research.md
  - sources/ptah-2026-verifiable-multimodal-deep-research.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-15-daily.md
maturity: validated
read_status: read
created: 2026-07-15
updated: 2026-07-15
---

## Relations

- @concepts/process-verified-agentic-search-geo.md - SEO operator playbook from this paper
- @concepts/evidence-ecosystem-geo.md - pairs with EcoGEO trajectory evidence graphs
- @concepts/generative-engine-optimization.md - GEO/AEO hub
- @concepts/adaptive-rag-internal-linking-geo.md - multi-hop evidence routing
- @concepts/geo-visibility-measurement.md - entity-hit / progress proxies
- @concepts/ai-citation-sourcing-geo.md - source layer agents must hit
- @concepts/content-strategy-local.md - hub/support pages agents traverse
- @sources/arxiv-ye-2026-ecogeo-trajectory-aware-evidence-ecosystems-2605.12887-2026-07-04.md - trajectory GEO companion (K138)
- @sources/score-2026-self-evolving-deep-research.md - self-evolving research cluster
- @sources/ptah-2026-verifiable-multimodal-deep-research.md - verifier-harness cluster
- @concepts/federated-daily-research-digest.md - K139 ingest routing
- @sweeps/2026-07-15-daily.md - overnight inbox drop
- Cross-wiki (already ingested): `@osint-wiki/sources/arxiv-deepsearch-world-2607.07820-2026-07-13.md`, `@osint-wiki/concepts/deepsearch-world-self-evolution.md`, `@gambling-wiki/sources/arxiv-2607.07820-deepsearch-world-self-distillation-2026-07-13.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment |
| **Authors** | Xinyu Geng, Xuanhua He, Sixiang Chen, Yanjing Xiao, Fan Zhang, Shijue Huang, Haitao Mi, Zhenwen Liang, Tianqing Fang, Yi R. Fung (HKUST / Tencent / HKUST(GZ)) |
| **arXiv** | 2607.07820v2 (v1 retrieved in inbox; v2 2026-07-13) |
| **Filename** | `arxiv-2607.07820-2607-07820v1-deepsearch-world-self-distillation.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.07820-2607-07820v1-deepsearch-world-self-distillation.pdf` |
| **Retrieved** | 2026-07-15 (SEO digest inbox); federated ingest elsewhere 2026-07-13 |
| **Read status** | read (abstract, intro, method §3, results §4, limitations, ethics) |
| **Code/Data** | Promised (env + 420K pool + DeepSearch-Val + 9B model + code) — **not released on GitHub/HF at ingest** |

## Narrative

DeepSearch-World is a **deterministic offline Wikipedia environment** for long-horizon search agents: BM25 search snippets + SQLite visit/read, ~10M entities, **420K** multi-hop QA tasks built from entity-level random walks. The environment maintains an order-free **completed entity set** after each tool call and injects staged grounded reflection on failures (soft on first miss; stronger hints on repeated misses).

DeepSearch-Evolve runs iterative self-distillation: scaffold teacher rollout (Plan / Act / End with working memory) → rejection sampling / quality filter → scaffold-to-ReAct conversion → evolving SFT (11 rounds from Qwen3.5-9B). No stronger proprietary teacher trajectories. Optional GRPO bridge on ~1,600 live SerpAPI + Jina instances to shrink offline→web gap.

### Benchmark results `[CONFIRMED]` within paper Table 1

| Model | BrowseComp | BrowseComp-ZH | HLE | GAIA | xbench | HotpotQA |
|-------|------------|---------------|-----|------|--------|----------|
| Qwen3.5-9B-Instruct | 7.4 | 13.5 | 16.7 | 23.9 | 20.0 | 45.3 |
| DeepSearch-World-9B | **31.2** | **36.4** | **25.7** | **61.5** | **49.0** | **93.4** |
| Δ | +23.8 | +22.9 | +9.0 | +37.6 | +29.0 | +48.1 |

Competitive with strong open-source deep-research agents that often rely on frontier distillation. Larger task pool (420K vs 100K) raised validation plateau and entity-hit / tool-success curves across rounds.

### Operator translation `[TENTATIVE]`

For local GEO, steal the **process lens**, not the Wikipedia env:

1. **Entity-hit progress** — agents improve when intermediate tool calls can confirm shop/service/location entities. Inconsistent NAP / service names look like failed entity hits → reformulation or abandonment.
2. **Failure recovery** — if the first crawl misses booking/hours/services, a clear reformulation path (FAQ, location page, GBP) should exist; do not bury the fact only on one orphan URL.
3. **Scaffold memory fields** — owned content should expose completed facts / next-hop proof (hours → booking → reviews) the way the teacher tracks completed_list / todo_list / information.
4. **Do not** invent synthetic evidence graphs (same ethic as EcoGEO). Real coordinated facts only.

**Phase-0:** REFERENCE / Watch — academic; code+420K corpus not released; corpus would exceed local <500 MB adoption budget even if released. Hands-on: `briefs/2026-07-15_k139-entity-hit-agent-path-audit-hands-on.md`. Poker core loop already shipped OSINT K161; SEO adds GEO delta only.

## Snippets

> "Without distillation from more capable models, DeepSearch-World-9B achieves competitive performance compared with open-source agents, reaching 31.2% on BrowseComp, 61.5% on GAIA, and 93.4% on HotpotQA."

> "A tool response ot is considered successful if it matches any unresolved entity in Ti \\ St … Failed calls trigger staged rule-based reflection toward the next unresolved entity."

> "Although the backend is restricted to Wikipedia, the tool schema is aligned with real web tools: search maps queries to ranked snippets and URLs, while visit maps URLs to page content."

[Source: arXiv 2607.07820v2 (retrieved 2026-07-15)]
