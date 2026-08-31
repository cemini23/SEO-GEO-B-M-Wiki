---
title: "Constable et al. 2026 - PULSAR pooled late-interaction visual document RAG (arXiv 2608.28572) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, late-interaction, visual-rag, enterprise, k166]
keywords: [2608.28572, PULSAR, ColPali, late-interaction, MaxSim, visual document RAG, enterprise]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - sweeps/2026-08-31-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-31
updated: 2026-08-31
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — enterprise visual document RAG; not local-pack SEO
- @concepts/federated-daily-research-digest.md — K166 digest fetch
- @concepts/adaptive-rag-internal-linking-geo.md — **thin GEO steal** (vision-first late-interaction vs OCR verbalisation; pairs K148)
- @sweeps/2026-08-31-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-31_k166-pulsar-late-interaction-from-seo.md` (CCC **primary** — pooled MaxSim index; no public code)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG |
| **Authors** | Benjamin Constable (Microsoft), Anup Roy, Vishal Sharma, et al. (Inception42 / Mubadala) |
| **arXiv** | 2608.28572 (cs.IR / cs.AI) |
| **Filename** | `arxiv-2608.28572-pulsar-pooled-unified-late-interaction-search-an.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.28572-pulsar-pooled-unified-late-interaction-search-an.pdf` |
| **Retrieved** | 2026-08-31 |
| **Code** | No public PULSAR repo URL in paper → Watch / 0 MB |

## Narrative

Institutional investors search visually dense pitch decks and diligence PDFs that change hourly near deal closing. OCR + figure verbalisation is costly to refresh and loses chart detail. **PULSAR** (production at Mubadala since March 2026) indexes **page images** with a frozen ColPali-style backbone and a **pooled two-stage late-interaction index**: compact page summaries for initial retrieval, then exact MaxSim rescoring over a finer pooled representation. On ViDoRe V3: **15.1×** lower median vector-search latency vs unpooled with <0.01 absolute NDCG@10 / Recall@10 loss; production median 156 ms; ~**88×** higher QPS under load. Ingestion ~**20×** cheaper per page than OCR+verbalisation baseline; **2×** answer-fact recall at production top-K. Served 78k documents / ~2.4M pages across 3k+ deals.

**SEO remit:** enterprise visual RAG false positive — no GBP ranking playbook. Federation: **thin GEO steal** on adaptive RAG (vision-first page unit beats lossy OCR chunking for chart/table-heavy pages; pairs K148 DenseOn/LateOn + K255 READ tabular caveat). **CCC primary** — pooled late-interaction serving (pairs K163 Chimera infra vocabulary).

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "PULSAR indexes page images with a frozen ColPali-style backbone and uses a pooled two-stage late-interaction index: compact page summaries support initial retrieval, followed by exact MaxSim rescoring over a finer pooled representation." [Source: arXiv 2608.28572 Abstract]

> "The event-driven ingestion path is estimated to be approximately 20 times cheaper per page than the OCR+verbalisation baseline it replaced." [Source: arXiv 2608.28572 §1 Introduction]
