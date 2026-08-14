---
title: "Chatzisavvas et al. 2026 - AmalthAI open-source CV platform for cultural heritage (arXiv 2608.13343) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, computer-vision, cultural-heritage, cs-cv, k158]
keywords: [2608.13343, AmalthAI, TEXTaiLES, cultural heritage, Grad-CAM, VLM, HITL, Kubeflow, Katib]
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

- @concepts/corpus-overflow-out-of-scope.md — computer-vision cultural-heritage platform; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K158 digest fetch
- @sweeps/2026-08-14-daily.md — overnight inbox drop
- Cross-wiki: `../atto/briefs/2026-08-14_k158-amalthai-cultural-heritage-cv.md` (Atto **primary**)
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-14_k158-amalthai-and-tabsom-from-seo.md` (CCC thin)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AmalthAI: An Open-Source Computer Vision Platform for Cultural Heritage |
| **Authors** | Christos Chatzisavvas, Stelios Alvanos, Efstratios Politis, Panagiotis Rigas, Thomas Pappas, Ioannis Giannoukos, Nikolaos Mitianoudis, Agata Ulanowska, Katarzyna Żebrowska, Nazarij Buławka, Christina Margariti, George Pavlidis, Chairi Kiourt, Anestis Koutsoudis, Vassilis Katsouros, George Ioannakis |
| **arXiv** | 2608.13343 (cs.CV) |
| **Filename** | `arxiv-2608.13343-amalthai-an-open-source-computer-vision-platform.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.13343-amalthai-an-open-source-computer-vision-platform.pdf` |
| **Retrieved** | 2026-08-14 |
| **Code** | `github.com/TEXTaiLES/AmalthAI` — AGPL-3.0, ~6.5MB → `.local/adopts/AmalthAI` REFERENCE clone (Phase-0), runtime **wont_wire** (AGPL source-disclosure on hosted dashboards; Atto already rejects AGPL in product — KekuleHtml precedent) |
| **Zenodo** | `10.5281/zenodo.20048428` |

## Narrative

AmalthAI is an open-source computer-vision platform that lowers the CV/ML pipeline barrier for cultural-heritage (CH) domain experts who are not ML practitioners. The interface covers dataset management, training, and inference for classification, segmentation, and object detection, with Kubeflow and Katib driving scalable training and hyperparameter search. **Grad-CAM** localizes the image region behind a prediction, and a **vision-language model (VLM)** adds a text description of it for expert review — a human-in-the-loop validation loop. Because archaeological data is often state-owned or rights-encumbered and cannot leave institutional custody, AmalthAI is **self-hostable**, keeping sensitive data on-premises. It is validated on a custom dataset of clay textile imprints, where CH experts trained and validated segmentation and classification models for hypothesis testing.

**SEO remit:** cs.CV cultural-heritage false positive — not local SEO. Federation: **Atto PRIMARY** (inspectable CV UI + expert-in-loop pipeline + Grad-CAM localization steal for artifact/document photos; Transkribus remains sole HTR). **CCC thin** (inspectable self-hosted CV UI pattern). Code: AGPL-3.0 → REFERENCE clone only, **not** runtime-wired (AGPL; Atto already rejects AGPL in product — KekuleHtml precedent). No model-weight/dataset downloads.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "AmalthAI… enables non-ML CH experts to independently produce and validate archaeologically meaningful findings. The interface covers dataset management, training, and inference for classification, segmentation, and object detection, with Kubeflow and Katib handling scalable training and hyperparameter search. Grad-CAM localizes the image region behind a prediction, and a vision-language model (VLM) adds a text description of it for expert review." [Source: arXiv 2608.13343 Abstract]

> "Since archaeological data is often state-owned or rights-encumbered and cannot leave institutional custody, AmalthAI's self-hostable deployment ensures sensitive data is kept within premises." [Source: arXiv 2608.13343 Abstract]
