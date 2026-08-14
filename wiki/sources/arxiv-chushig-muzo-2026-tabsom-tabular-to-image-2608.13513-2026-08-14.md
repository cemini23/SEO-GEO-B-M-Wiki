---
title: "Chushig-Muzo et al. 2026 - TabSOM tabular-to-image encoding via self-organizing maps (arXiv 2608.13513) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, computer-vision, tabular-to-image, cs-cv, k158]
keywords: [2608.13513, TabSOM, self-organizing map, SOM, tabular-to-image, interpretability, partial-dependence]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-14-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — tabular-to-image ML encoding; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K158 digest fetch
- @sweeps/2026-08-14-daily.md — overnight inbox drop
- Cross-wiki: `../Image gen/briefs/2026-08-14_k158-tabsom-tabular-to-image-from-seo.md` (Image Gen thin)
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-14_k158-amalthai-and-tabsom-from-seo.md` (CCC thin note)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | TabSOM: A tabular-to-image encoding method based on self-organizing maps |
| **Authors** | David Chushig-Muzo, María Ángeles Rodríguez de Cara, Eva Milara, Francisco J. Lara-Abelenda, Luis Zhinin-Vera, Diego H. Peluffo-Ordóñez |
| **arXiv** | 2608.13513 (cs.CV / cs.LG) |
| **Filename** | `arxiv-2608.13513-tabsom-a-tabular-to-image-encoding-method-based.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.13513-tabsom-a-tabular-to-image-encoding-method-based.pdf` |
| **Retrieved** | 2026-08-14 |
| **Code** | No public GitHub located in skim → **Watch** (no clone) |

## Narrative

TabSOM converts tabular data into image representations so CNNs and vision transformers can be applied, but unlike prior tabular-to-image methods (t-SNE/UMAP/PCA fixed pixel layouts) that encode only marginal feature values, it is built on a **Self-Organizing Map (SOM)**: (i) each feature occupies a fixed canvas position derived from its component plane via **collision-free Hungarian assignment**, and (ii) a **graph captures pairwise feature relationships** from the SOM component planes. The resulting image stacks two multi-scale node channels — one encoding feature values at fixed scales, the other pairwise feature interactions as spatial connections. Two SOM-derived interpretability approaches: a prototype-inspired **partial dependence plot** and a **class-separation importance score**. Benchmarked against twelve tabular-to-image methods, TabSOM ranks first or second on every public binary-classification dataset with the lowest variance. Interpretability agrees with Random Forest / XGBoost / SHAP on top-ranked features while adding complementary structural signal.

**SEO remit:** cs.CV/cs.LG false positive — not local SEO/GEO. Federation: **Image Gen thin** (SOM-based canvas layout / tabular-to-image encoding note) + optional **CCC thin**. Code: no public repo located → **Watch**.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "We propose TabSOM, a tabular-to-image encoding built on the Self-Organizing Map (SOM), which provides: (i) a spatial layout in which every input feature occupies a fixed canvas position derived from its component plane via collision-free Hungarian assignment; and (ii) a graph that captures pairwise feature relationships derived from the SOM component planes." [Source: arXiv 2608.13513 Abstract]
