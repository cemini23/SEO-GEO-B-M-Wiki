---
title: "Smirnov et al. 2026 - ERank latent-space image richness (arXiv 2607.19315) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, vision, data-selection, k144]
keywords: [2607.19315, ERank, effective rank, image complexity, IC9600, OCR, super-resolution]
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

- @concepts/corpus-overflow-out-of-scope.md — vision richness metric; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K144 digest fetch
- @sweeps/2026-07-22-daily.md — overnight inbox drop
- Cross-wiki briefs: `../Image gen/briefs/2026-07-22_k144-erank-image-richness-from-seo.md`; tipdrop `~/Desktop/projects/tipdrop-workspace-kit/briefs/2026-07-22_k144-erank-data-selection-david.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ERank in Latent Space as an Image-Complexity and Richness Measure |
| **Authors** | Maksim Smirnov, Grigory Kononov, Anastasiia Linich, Egor Surkov, Egor Shvetsov |
| **arXiv** | 2607.19315 |
| **Filename** | `arxiv-2607.19315-erank-in-latent-space-as-an-image-complexity-and.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.19315-erank-in-latent-space-as-an-image-complexity-and.pdf` |
| **Retrieved** | 2026-07-22 |
| **Code** | None linked at ingest |

## Narrative

**ERank** = effective rank of channel covariance of a frozen encoder’s feature map — label-free per-sample visual richness (one forward pass). Correlates with human complexity on IC9600 (r=0.72) and with bitrate/sharpness/edge density. As data-selection: drop low-ERank → better super-resolution; drop high-ERank → better OCR; no help for classification/segmentation/denoising.

**SEO remit:** no GBP/GEO playbook — overflow. Federation: Image Gen + TipDrop/David (dataset curation by richness).

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. No public code.

## Snippets

> "ERank is thus a cheap richness signal, useful exactly when task difficulty is governed by input richness." [Source: arXiv 2607.19315 Abstract]
