---
title: "Bushnell 2026 - IndelFreeAligner streaming genomics aligner (arXiv 2607.27291) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, genomics, bioinformatics, k149]
keywords: [2607.27291, IndelFreeAligner, BBTools, streaming aligner, CRISPR, metagenomics]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-31-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-31
updated: 2026-07-31
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — genomics / BBTools; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K149 digest
- @sweeps/2026-07-31-daily.md — overnight fetch

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | IndelFreeAligner: A Streaming Aligner for Comprehensive Gapless Alignment Against Terabase-Scale References |
| **Authors** | Brian Bushnell (DOE JGI / LBNL) |
| **arXiv** | 2607.27291 |
| **Filename** | `arxiv-2607.27291-indelfreealigner-a-streaming-aligner-for-compreh.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.27291-indelfreealigner-a-streaming-aligner-for-compreh.pdf` |
| **Retrieved** | 2026-07-31 |
| **Code** | Open-source via BBTools (https://github.com/bbushnell/BBTools); SEO OUT-OF-SCOPE — no adopt |

## Narrative

Streaming indel-free aligner for small query sets vs terabase-scale references (CRISPR spacer analysis, metagenomics). Indexed + brute-force modes; memory independent of total reference size. Large speedups vs Bowtie1/BLAST+ on small-query / huge-ref workloads.

**SEO remit:** q-bio.GN false positive from `local-seo-paper` arXiv API bleed. Overflow only. Atto / TipDrop / poker / prod: no hook.

**Phase-0:** OUT-OF-SCOPE for SEO. Do not clone BBTools into this wiki (wrong domain; suite size irrelevant to GEO).

## Snippets

> "By processing reference sequences on-the-fly, IndelFreeAligner supports user-specified mismatch thresholds up to the full query length and maintains memory usage independent of total reference size." [Source: arXiv 2607.27291 Abstract]
