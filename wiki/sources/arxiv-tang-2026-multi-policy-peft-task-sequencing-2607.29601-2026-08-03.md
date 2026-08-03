---
title: "Tang et al. 2026 - Multi-policy PEFT task sequencing (arXiv 2607.29601) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, llm, peft, qlora, k150]
keywords: [2607.29601, PEFT, QLoRA, multi-policy, task sequencing, TRACE]
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

- @concepts/corpus-overflow-out-of-scope.md — PEFT training organization; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K150 digest fetch
- @sweeps/2026-08-03-daily.md — overnight inbox drop
- Cross-wiki brief: `../Cemini claude code CCC/briefs/2026-08-03_k150-multi-policy-peft-task-sequencing-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Parts Are Greater Than the Sum: Automated Task Sequencing for Efficient Training of Multi-Policy LLMs |
| **Authors** | Jiajia Tang, Sizhe Yuen, Francisco Gomez Medina, Yali Du, Adam Sobey (Alan Turing Institute / Southampton / KCL) |
| **arXiv** | 2607.29601 |
| **Filename** | `arxiv-2607.29601-the-parts-are-greater-than-the-sum-automated-tas.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.29601-the-parts-are-greater-than-the-sum-automated-tas.pdf` |
| **Retrieved** | 2026-08-03 |
| **Code** | None linked at ingest |

## Narrative

Automatic **multi-policy PEFT**: group heterogeneous tasks by optimization compatibility, assign each group an independent QLoRA path, then sequence tasks within each policy to cut transition cost / forgetting. On TRACE, auto multi-policy hits **44.78** OP under a fixed trainable budget — better than raising adapter capacity alone.

**SEO remit:** cs.LG PEFT false positive — overflow. Steal shape for CCC: organize heterogeneous fine-tune tasks into compatible policies before training; sequencing matters as much as rank.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. No public code → REFERENCE via CCC brief only. **Atto / TipDrop / poker / prod:** SKIP.

## Snippets

> "This suggests that optimization-path organization is more effective than simply increasing adapter capacity for heterogeneous parameter-efficient fine-tuning." [Source: arXiv 2607.29601 Abstract]
