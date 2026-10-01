---
title: "Kang et al. 2026 - PrecogUI proactive GUI agents (arXiv 2609.36923) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, gui-agent, agent-architecture, benchmark, k283]
keywords: [2609.36923, PrecogUI, GUI agent, proactive simulation, experience pool, InterfereBench, AutoTraj]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-30-daily.md
  - "@ccc-wiki/concepts/simulate-before-commit-experience-pool.md"
maturity: draft
read_status: skimmed
created: 2026-09-30
updated: 2026-10-01
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — GUI agent architecture; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K283 digest fetch
- @sweeps/2026-09-30-daily.md — overnight inbox drop
- @ccc-wiki/concepts/simulate-before-commit-experience-pool.md — CCC took the structural steal (K283 landed 2026-10-01)
- Cross-wiki brief: `../Cemini claude code CCC/briefs/2026-09-30_k283-precogui-proactive-simulation-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | PrecogUI: Proactive GUI Agents via Pre-cognitive Simulation and Experience Retrieval |
| **Authors** | Bin Kang, Jiarui Ouyang, Li Jiang, Bin Chen, Zhuotao Tian (UCAS, HKUST, HIT, CUHK, Shenzhen Loop Area Institute) |
| **arXiv** | 2609.36923 |
| **Filename** | `arxiv-2609.36923-precogui-proactive-gui-agents-via-pre-cognitive.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.36923-precogui-proactive-gui-agents-via-pre-cognitive.pdf` |
| **Retrieved** | 2026-09-30 |
| **Code** | None published — "The code will be publicly available" |

## Narrative

A **pre-cognitive** GUI-agent architecture: a Proactive Experience Pool (PEP) caches recurring anomaly and success patterns as state-action-result tuples in dual memory; a Proactive Simulation Executor (PSE) forecasts the next symbolic UI layout for a candidate action and ranks actions by predicted reliability; a Pre-cognitive Execution Controller (PEC) fuses both and adds closed-loop error correction. Ships AutoTraj (data-generation engine) and InterfereBench (long-horizon tasks with strong disturbances).

Headline: SR **79.2%** (Low interference) / **52.7%** (High) on the normal subset; **88.7%** SR on a second split; **89.4%** element-type accuracy / 80.2% mean bbox; 97.5% text · 82.2% icon accuracy on Desktop, 94.6% / 91.7% on Web; **76.4%** SR on AndroidControl-High. A reactive baseline reaches 41.5% SR where PrecogUI does better.

**SEO remit:** no GBP/GEO/local-search playbook — overflow inventory only. Structural steal for the CCC lane: simulate a candidate action forward and rank by predicted reliability *before* committing, with an experience pool of past anomalies. That is the same shape as the pre-flight/verify-before-publish discipline already documented in @concepts/process-verified-agentic-search-geo.md. Routed, not adopted here.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. No public code at ingest. No local SEO clone.

## Snippets

> "We propose PrecogUI, a pre-cognitive architecture that shifts the paradigm from reactive execution to proactive decision-making." [Source: arXiv 2609.36923 Abstract]
