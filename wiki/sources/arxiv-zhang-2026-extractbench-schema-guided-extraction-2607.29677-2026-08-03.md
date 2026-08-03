---
title: "Zhang et al. 2026 - ExtractBench schema-guided enterprise extraction (arXiv 2607.29677) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, agents, document-ie, schema, k150]
keywords: [2607.29677, ExtractBench, schema-guided extraction, LlamaExtract, grounding, enterprise docs]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-03-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-03
updated: 2026-08-03
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — enterprise document IE; **not** schema.org local SEO markup
- @concepts/federated-daily-research-digest.md — K150 digest fetch
- @sweeps/2026-08-03-daily.md — overnight inbox drop
- Cross-wiki briefs: `../atto/briefs/2026-08-03_k150-extractbench-schema-guided-extraction.md`; `../Cemini claude code CCC/briefs/2026-08-03_k150-extractbench-agent-extraction-eval-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction |
| **Authors** | Boyang Zhang, Adrian Lyjak, Eli Stewart, Zhaoqi Li, Simon Suo (LlamaIndex / runllama.ai) |
| **arXiv** | 2607.29677 |
| **Filename** | `arxiv-2607.29677-extractbench-a-benchmark-for-schema-guided-enter.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.29677-extractbench-a-benchmark-for-schema-guided-enter.pdf` |
| **Retrieved** | 2026-08-03 |
| **Release (claimed)** | HuggingFace `llamaindex/ExtractBench`; GitHub `run-llama/ExtractBench` — **404 / empty at ingest** → Watch |

## Narrative

Benchmark for **schema-guided extraction**: (document, JSON Schema) → schema-valid JSON + evidence boxes. 370 docs / 4,869 pages / 67 types / 8 domains; scores value F1, word- + page-level grounding, and ¢/page cost. VLMs strong on short docs but collapse on long lists (e.g. Gemini 3.5 Flash 87.9% → 27.9%); LlamaExtract Agentic Plus more consistent (~96% short / ~94% long) at lower cost than Codex-class coding agents. Name collision warning: this is **user-defined JSON Schema for IE**, not Google/schema.org LocalBusiness markup.

**SEO remit:** false positive on “schema” keyword — overflow. Federation: **Atto** (civil-record / Antenati schema extraction + grounding) + **CCC** (agent extraction eval). Do not wire into `@concepts/schema-markup-local.md`.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. Dataset/code not publicly resolvable at ingest → **Watch / no pull**. **TipDrop / poker / prod:** SKIP.

## Snippets

> "We present ExtractBench, a benchmark for schema-guided extraction, and, to our knowledge, conduct the first evaluation to report value accuracy, record completeness at scale, grounding, and measured cost together." [Source: arXiv 2607.29677 Abstract]
