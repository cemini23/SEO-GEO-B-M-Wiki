---
title: "Tamang et al. 2026 - Beyond Top-K READ document ops (arXiv 2608.06305) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, rag, mcp, document-ops, k154]
keywords: [2608.06305, READ, top-k, embedding-free, MCP, financial RAG, BM25]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-07-daily.md
  - entities/tools/denseon-lateon.md
  - concepts/adaptive-rag-internal-linking-geo.md
maturity: draft
read_status: skimmed
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — long-doc RAG/MCP paper; not local SEO operator playbook
- @concepts/federated-daily-research-digest.md — K154 digest fetch
- @sweeps/2026-08-07-daily.md — overnight inbox drop
- @entities/tools/denseon-lateon.md — thin GEO steal: when dense top-k fails on layout/tabular meaning
- @concepts/adaptive-rag-internal-linking-geo.md — MCP document ops vs chunk-embed contract
- Cross-wiki: `../atto/briefs/2026-08-07_k154-read-document-ops.md`; `../Cemini claude code CCC/briefs/2026-08-07_k154-read-mcp-document-ops-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations |
| **Authors** | Sagar Tamang, Ayush Vyas, Tabarakul Hazarika (IIT Patna / TwoSpoon) |
| **arXiv** | 2608.06305 |
| **Filename** | `arxiv-2608.06305-beyond-top-k-replacing-black-box-retrieval-with.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.06305-beyond-top-k-replacing-black-box-retrieval-with.pdf` |
| **Retrieved** | 2026-08-07 |
| **Code** | Paper claims Markdown repro ships with code; **no public GitHub URL located** 2026-08-07 → **Watch** |

## Narrative

READ (Reliable Embedding-free Agentic Document-search) replaces chunk–embed–top-k with three deterministic MCP tools over an intact document: normalized lexical search, structural outline/navigation, and bounded span reads. Eval on a 780-page government finance report (86.8% table rows; units inherited from headers a median 13 lines above figures). READ 58.8% vs dense 15.7% (tuned dense 35.3%); same loop with a top-k tool only 27.5% — gain attributed to the interface, not iteration. **BM25 ≈ READ** (statistically indistinguishable) at ~⅓ cost — result separates embedding-based from embedding-free retrieval, not MCP loops from lexical search.

**SEO remit:** not GBP/local-pack. Thin GEO steal only: dense passage probes can fail when meaning lives in layout/headers (pairs DenseOn/LateOn caution). Federation: **CCC** (MCP document ops + replayable trajectories) + **Atto** (long PDF/table source docs) + **OSINT** (financial-statement RAG).

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. Code **Watch** (no public repo URL). **GuruWatcher / TipDrop / poker / prod:** SKIP. Local SEO adopt disk: **0 MB**.

## Snippets

> "We also report what the evidence does not support: BM25 is statistically indistinguishable from READ, so our result separates embedding-based from embedding-free retrieval, not agentic from lexical search." [Source: arXiv 2608.06305 Abstract]
