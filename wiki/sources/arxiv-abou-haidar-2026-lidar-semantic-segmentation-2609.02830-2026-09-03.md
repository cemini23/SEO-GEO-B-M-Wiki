---
title: "Abou Haidar et al. 2026 - LiDAR semantic segmentation deployment eval (arXiv 2609.02830) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, lidar, autonomous-driving, robotics, k169]
keywords: [2609.02830, LiDAR, semantic segmentation, domain shift, coarse labels, cs.RO]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-03-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-03
updated: 2026-09-03
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — autonomous-vehicle perception; not local-pack SEO
- @concepts/federated-daily-research-digest.md — K169 digest fetch
- @sweeps/2026-09-03-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Toward Robust LiDAR Semantic Segmentation for Real-World Deployment: Evaluation under Coarse Labels, Adverse Conditions, and Domain Shifts |
| **Authors** | Samir Abou Haidar, Alexandre Chariot, Mehdi Darouich, Cyril Joly, Jean-Emmanuel Deschaud |
| **arXiv** | 2609.02830 (cs.RO) |
| **Filename** | `arxiv-2609.02830-toward-robust-lidar-semantic-segmentation-for-re.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.02830-toward-robust-lidar-semantic-segmentation-for-re.pdf` |
| **Retrieved** | 2026-09-03 |
| **Code** | No public repo URL in abstract → Watch / 0 MB |

## Narrative

LiDAR semantic segmentation is core for AV/mobile robots, but benchmarks focus on clean single-domain fine-grained labels. Real deployment needs safety-critical coarse semantics, degraded sensing, and cross-domain generalization — no unified protocol covered all three.

This paper proposes structured evaluation along: (i) **coarse-label** assessment aligned with safety priorities; (ii) **robustness** under eight LiDAR corruption types (atmospheric, geometric, sensor); (iii) **domain generalization** without adaptation. Includes inference speed on **Jetson AGX Orin**. Findings: fine-grained leaderboard rankings do not always reflect safety-relevant performance; all methods degrade substantially under corruptions with architecture-dependent patterns; domain generalization remains insufficient.

**SEO remit:** geo-aeo digest false positive. **Phase-0:** overflow only. **Federation:** none. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "Our results show that fine-grained benchmark rankings do not always reflect safety-relevant performance, that all methods experience substantial degradation under corruptions with architecture-dependent robustness characteristics." [Source: arXiv 2609.02830 Abstract]

> "The evaluation includes inference speed measured on an embedded Jetson AGX Orin platform, directly reflecting deployment constraints." [Source: arXiv 2609.02830 Abstract]
