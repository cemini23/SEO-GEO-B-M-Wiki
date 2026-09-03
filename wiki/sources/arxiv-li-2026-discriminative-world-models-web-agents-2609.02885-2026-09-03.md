---
title: "Li et al. 2026 - Discriminative world models for web agents (arXiv 2609.02885) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, web-agents, world-models, k169]
keywords: [2609.02885, world model, web agent, predicted-state matching, WebArena, PRM, test-time scaling]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-03-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-03
updated: 2026-09-03
cross-wiki-routed: ccc-wiki
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — web-agent world models; not local-pack SEO
- @concepts/federated-daily-research-digest.md — K169 digest fetch
- @sweeps/2026-09-03-daily.md — overnight inbox drop
- CCC brief (repo root, not wiki/): `../Cemini claude code CCC/briefs/2026-09-03_k169-dwm-web-agents-ccc-from-seo.md` (**primary**)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Discriminative World Models for Web Agents |
| **Authors** | Kelvin Li, Dhruv Pendharkar, Anish Pahilajani, Chuyi Shang, Leon Oks, Leonid Karlinsky, Rogerio Feris, Trevor Darrell, Roei Herzig |
| **arXiv** | 2609.02885 (cs.AI, cs.LG) |
| **Filename** | `arxiv-2609.02885-discriminative-world-models-for-web-agents.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.02885-discriminative-world-models-for-web-agents.pdf` |
| **Retrieved** | 2026-09-03 |
| **Code** | Project page https://dhruvpendharkar.github.io/dwm/ — no SPDX clone this pass → Watch / 0 MB |

## Narrative

Web agents increasingly use **world models** at test time: sample candidate actions, predict resulting web states (HTML/AXTree), rank with a ranker or PRM. Standard training uses **supervised next-state prediction**, but rankers need predicted states that are **discriminative across candidates** — objectives misalign.

**Predicted-state matching:** predicted representation must distinguish the true resulting state from states reached by alternative actions. Trained on a **branching WebArena Go-Browse** dataset where every decision point has multiple alternative actions and outcomes.

Results: beats supervised next-state models on held-out predicted-state matching benchmark; improves PRM-style action ranking on **WebPRMBench** vs action-only PRMs and PRMs + supervised world models; **WebArena-Lite** test-time action selection improves end-to-end success.

**SEO remit:** geo-aeo digest false positive. Federation: **CCC primary** (ranker-aligned world models for browser harness eval; pairs K283 Twin validate-before-act + K321 structured state over screenshot-click). **Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "We introduce predicted-state matching, a training objective where the predicted representation must distinguish the true resulting state from those reached by alternative actions." [Source: arXiv 2609.02885 Abstract]

> "Experiments on our held-out predicted-state matching benchmark show that our approach outperforms world models trained with supervised next-state prediction." [Source: arXiv 2609.02885 Abstract]
