---
title: "Kaur et al. 2026 - UI-VISA vascular DSA segmentation (arXiv 2609.01598) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, medical-imaging, computer-vision, k168]
keywords: [2609.01598, UI-VISA, U-Net, vascular segmentation, DSA, region growing]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-02-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-02
updated: 2026-09-02
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — medical imaging segmentation; not local-pack SEO
- @concepts/federated-daily-research-digest.md — K168 digest fetch
- @sweeps/2026-09-02-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | UI-VISA: U-Net Initialized Vascular Image Segmentation Architecture |
| **Authors** | Asees Kaur, Suzanne S. Sindi, Erica M. Rutter |
| **arXiv** | 2609.01598 (cs.CV) |
| **Filename** | `arxiv-2609.01598-ui-visa-u-net-initialized-vascular-image-segment.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.01598-ui-visa-u-net-initialized-vascular-image-segment.pdf` |
| **Retrieved** | 2026-09-02 |
| **Code** | No public repo URL in abstract → Watch / 0 MB |

## Narrative

Vascular segmentation in digital subtraction angiography (DSA) is hard because vessels are thin, elongated, and branching. U-Net gives strong pixel-wise performance but can fragment fine vessels; region growing preserves connectivity but is seed-sensitive and costly.

**UI-VISA** hybridizes both: U-Net foreground predictions seed a CNN-guided region-growing pass that enforces local connectivity and recovers fine details. Evaluated on 26 DSA images with 5-fold CV vs standalone U-Net and prior VISA: highest mean Dice and clDice; Wilcoxon signed-rank shows clDice improvement significant (p=0.023); Dice improvement not significant (p=0.104).

**SEO remit:** geo-aeo digest false positive — clinical cs.CV OOD. **Phase-0:** overflow only. **Federation:** none. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "UI-VISA uses U-Net's foreground predictions as informed seed points for a CNN-guided region growing algorithm, which then iteratively refines the segmentation by enforcing local connectivity." [Source: arXiv 2609.01598 Abstract]

> "UI-VISA achieves the highest mean Dice and clDice scores across folds, and a paired Wilcoxon signed-rank test shows the improvement in clDice is statistically significant (p=0.023)." [Source: arXiv 2609.01598 Abstract]
