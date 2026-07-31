---
title: DenseOn / LateOn — LightOn open dense + late-interaction retrieval
type: entity
tags: [tool, geo-aeo, retrieval, embeddings, foss, k148]
keywords: [DenseOn, LateOn, LightOn, ColBERT, PyLate, FastPLAID, BEIR, ModernBERT]
related:
  - sources/arxiv-sourty-2026-denseon-lateon-open-retrieval-2607.27178-2026-07-30.md
  - concepts/generative-engine-optimization.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/geo-visibility-measurement.md
  - entities/tools/geo-optimizer-skill.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-30-daily.md
maturity: draft
created: 2026-07-30
updated: 2026-07-31
wire_status: policy_wired
wire_target: .cursor/rules/cemini-phase1-seo-geo-wires.mdc
---

## Relations

- @sources/arxiv-sourty-2026-denseon-lateon-open-retrieval-2607.27178-2026-07-30.md — paper + Phase-0 provenance
- @concepts/generative-engine-optimization.md — retrieval layer under answer engines
- @concepts/adaptive-rag-internal-linking-geo.md — when dense vs late-interaction routing matters
- @concepts/evidence-ecosystem-geo.md — evidence must be retrievable by dense/late models
- @concepts/geo-visibility-measurement.md — probe whether passages retrieve
- @entities/tools/geo-optimizer-skill.md — complementary GEO audit CLI
- @concepts/federated-daily-research-digest.md — K148 digest
- @sweeps/2026-07-30-daily.md — overnight fetch

## Raw Concept

Open retrieval stack from LightOn (arXiv 2607.27178): DenseOn (dense) + LateOn (late-interaction), Apache-2.0 weights on Hugging Face; PyLate / FastPLAID MIT tooling for ColBERT-style serving.

## Narrative

### Phase-0 verdict (2026-07-30)

| Artifact | License | Disk | Decision |
|----------|---------|------|----------|
| `lightonai/DenseOn` weights | Apache-2.0 | ~600 MB | **Watch** (over 500 MB adopt cap) |
| `lightonai/LateOn` weights | Apache-2.0 | ~600 MB+ ONNX | **Watch** |
| Pretrain/finetune HF datasets | — | multi-GB | **Watch / no pull** |
| `lightonai/pylate` | MIT | ~2.6 MB shallow | **GO Adopt** → `raw-sources/tools/pylate` |
| `lightonai/fast-plaid` | MIT | ~4.4 MB shallow | **GO Adopt** → `raw-sources/tools/fast-plaid` |

### Operator use (local SEO / GEO)

1. Encode shop FAQ / service-page passages with DenseOn (when pulled outside this wiki disk budget) and run a small BEIR-style probe set of “best [service] in [city]” queries.
2. Prefer LateOn-style late-interaction when pages are long (token-level match) — PyLate is the local entry point.
3. Multilingual: late-interaction generalize better beyond translate-train languages — relevant if operator markets bilingual.

### Failure modes

- Treating DenseOn as a Google ranking factor (it is not) — use only as **answer-engine retrieval probe**
- Pulling full embedding datasets into laptop disk
- Confusing API closed embedders (Voyage, etc.) with this open recipe

## Snippets

- Collection: https://huggingface.co/collections/lightonai/denseon-and-lateon
- Blog: https://huggingface.co/blog/lightonai/denseon-lateon
