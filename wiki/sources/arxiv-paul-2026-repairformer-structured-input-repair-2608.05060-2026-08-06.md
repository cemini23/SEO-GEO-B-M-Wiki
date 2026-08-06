---
title: "Paul et al. 2026 - RepairFormer structured input repair (arXiv 2608.05060) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, software-engineering, transformers, k153]
keywords: [2608.05060, RepairFormer, JSON repair, CodeT5, LoRA, structured inputs]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-06-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — SE tool demo; not local SEO/GEO or schema.org
- @concepts/federated-daily-research-digest.md — K153 digest fetch
- @sweeps/2026-08-06-daily.md — overnight inbox drop
- Cross-wiki: `../atto/briefs/2026-08-06_k153-repairformer-structured-input-repair.md`; `../Cemini claude code CCC/briefs/2026-08-06_k153-repairformer-structured-repair-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | RepairFormer: Automated Repair of Structured Inputs Using Transformers |
| **Authors** | Ovi Paul, Tom J King, Ali Shokri (University of Houston) |
| **arXiv** | 2608.05060 |
| **Filename** | `arxiv-2608.05060-repairformer-automated-repair-of-structured-inpu.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.05060-repairformer-automated-repair-of-structured-inpu.pdf` |
| **Retrieved** | 2026-08-06 |
| **Code** | https://github.com/pass-uh/RepairFormer (MIT; ISSTA 2026 Tool Demo) |

## Narrative

Transformer (CodeT5 + optional LoRA) repairs malformed structured files (JSON, INI, DOT, OBJ, S-expression, TinyC) via supervised seq2seq + boundary-localized windows. Claims ~88% repair / 94% recovery; 97.57% repair / 94.29% recovery and 5× faster vs prior on their benchmark. Content-preserving vs delete-heavy search (ddmax / εREPAIR).

**SEO remit:** “structured” ≠ schema.org LocalBusiness — overflow. Federation: **Atto** (corrupt JSON/GEDCOM/config salvage) + **CCC** (harness input repair).

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. MIT repo ~1 MB → **GO Adopt on Atto** (`.local/adopts/RepairFormer`). **GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "In evaluation, RepairFormer achieves a 88% in repair and 94% in recovery, showing strongest content preservation when repairs are successful." [Source: arXiv 2608.05060 Abstract]
