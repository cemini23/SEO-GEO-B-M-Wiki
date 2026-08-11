---
title: "Sultan et al. 2026 - Signal-integrity framework for PPCB-1347/MuPix11 (arXiv 2608.09462) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, signal-integrity, eess, k156]
keywords: [2608.09462, MuPix11, PPCB-1347, signal integrity, high-speed interconnects, eye diagram]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-11-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-11
updated: 2026-08-11
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — physics-instrumentation SI; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K156 digest fetch
- @sweeps/2026-08-11-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Automated Signal Integrity Analysis Framework for High-Speed Interconnects in the PPCB-1347/MuPix11 Probe Card |
| **Authors** | D M S Sultan, R. Plackett, A.E. McDougall, A.J.A. Knight, A.S. Rotelli, J. Vossebeld, D. Bortoletto |
| **arXiv** | 2608.09462 |
| **Filename** | `arxiv-2608.09462-automated-signal-integrity-analysis-framework-fo.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.09462-automated-signal-integrity-analysis-framework-fo.pdf` |
| **Retrieved** | 2026-08-11 |
| **Code** | None (MATLAB framework; no public repo) |

## Narrative

A reusable MATLAB signal-integrity (SI) framework converting compatible four-port S-parameter data (VNA-measured or EM-simulated) into traceable link-level evidence. Demonstrated on the four 1.25 Gbps differential routes (DP1–DP4) of the PPCB-1347/MuPix11 probe card: power-normalized mixed-mode transform, route-length-aware loss decomposition, causally loaded channel model, PRBS-31 propagation into eye-diagram / conditional-BER / 8b10b analyses.

**SEO remit:** physics.ins-det / EE instrumentation false positive from arXiv API bleed — overflow only.

**Phase-0:** OUT-OF-SCOPE. **Atto / CCC / Cyber / GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "A reusable MATLAB signal-integrity (SI) framework is presented that converts compatible four-port S-parameter data, measured by VNA or obtained from electromagnetic simulation, into traceable link-level evidence rather than a single loss metric." [Source: arXiv 2608.09462 Abstract]
