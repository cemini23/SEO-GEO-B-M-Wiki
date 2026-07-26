---
title: "Cai et al. 2026 - Sequential EQA memory bottlenecks (arXiv 2607.21571) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, embodied-ai, memory, k146]
keywords: [2607.21571, EQA, sequential memory, spatially grounded, 3D metric memory]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-26-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-26
updated: 2026-07-26
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — embodied robotics EQA; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K146 digest fetch
- @sweeps/2026-07-26-daily.md — backlog ingest
- Cross-wiki briefs: `../OSINT WORKSPACE/briefs/2026-07-26_k146-sequential-eqa-memory-architecture-from-seo.md`; `../Cemini claude code CCC/briefs/2026-07-26_k146-spatially-grounded-persistent-memory-from-seo.md`; poker `../OSINT WORKSPACE/agents/devfun-poker-arena/briefs/2026-07-26_k146-structured-persistent-memory-delta.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering |
| **Authors** | Zikui Cai et al. (Maryland / UT Austin / UIUC / …) |
| **arXiv** | 2607.21571 |
| **Filename** | `arxiv-2607.21571-beyond-episodic-evaluation-memory-architectural.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.21571-beyond-episodic-evaluation-memory-architectural.pdf` |
| **Retrieved** | 2026-07-24 (ingested 2026-07-26) |
| **Code** | PDF claims `Code:https://github.com/` (URL truncated / incomplete at ingest) |

## Narrative

EQA is usually evaluated episodically (reset between questions). Sequential multi-query-in-same-scene evaluation exposes memory bottlenecks: occupancy-only memory lacks visual-semantic evidence; short-horizon episodic training mismatches long continuous histories. **Structured, spatially grounded memory** (persistent visual observations on metric 3D geometry) raises accuracy and lowers navigation cost; validated on a real mobile robot.

**SEO remit:** robotics — overflow. Steal: persistent structured memory beats “keep the chat log” / map-only memory for multi-query agent loops.

**Phase-0:** OUT-OF-SCOPE for SEO. Incomplete GitHub URL → no Adopt.

## Snippets

> "architectures that map persistent visual observations onto metric 3D geometry preserve visual-semantic evidence in a coherent scene representation." [Source: arXiv 2607.21571 Abstract]
