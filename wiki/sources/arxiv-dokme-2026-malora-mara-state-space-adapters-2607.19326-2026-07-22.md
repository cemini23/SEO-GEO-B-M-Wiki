---
title: "Dokme & Heck 2026 - MaLoRA/MaRA selective state-space adapters (arXiv 2607.19326) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, llm, peft, retrieval, k144]
keywords: [2607.19326, MaLoRA, MaRA, Mamba, LoRA, multi-hop QA, MuSiQue]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-22-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — PEFT / retrieval adapters; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K144 digest fetch
- @sweeps/2026-07-22-daily.md — overnight inbox drop
- Cross-wiki briefs: `../OSINT WORKSPACE/briefs/2026-07-22_k144-malora-mara-state-space-adapters-from-seo.md`; `../Cemini claude code CCC/briefs/2026-07-22_k144-mara-evidence-selection-adapters-from-seo.md`; poker `../OSINT WORKSPACE/agents/devfun-poker-arena/briefs/2026-07-22_k144-mara-segment-select-delta.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Selective State-Space Adaptation and Retrieval for Language Model Reasoning |
| **Authors** | Atahan Dokme, Larry Heck (Georgia Tech AVA Lab) |
| **arXiv** | 2607.19326 |
| **Filename** | `arxiv-2607.19326-selective-state-space-adaptation-and-retrieval-f.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.19326-selective-state-space-adaptation-and-retrieval-f.pdf` |
| **Retrieved** | 2026-07-22 |
| **Code** | None linked at ingest |

## Narrative

**MaLoRA** = Mamba-modulated LoRA (token-level recurrent adapter scaling). **MaRA** = Mamba Retrieval Adapter (context-level segment selection before generation). On frozen Qwen/Llama/Gemma + MuSiQue/2WikiMultihopQA: +6.8 F1 avg over LoRA (+10.5% rel), up to +9.3 F1 on hardest cell.

**SEO remit:** no local-search playbook — overflow. Steal shape: select relevant evidence segments *before* generating (pairs with agent RAG / HL brief filtering).

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. No public code → REFERENCE only via routed briefs. **No prod scp** (advisory; nothing to install).

## Snippets

> "At the context level, MaRA (Mamba Retrieval Adapter) tracks cross-segment state and selects the segments most relevant to the query, before the modulated language model generates its answer." [Source: arXiv 2607.19326 Abstract]
