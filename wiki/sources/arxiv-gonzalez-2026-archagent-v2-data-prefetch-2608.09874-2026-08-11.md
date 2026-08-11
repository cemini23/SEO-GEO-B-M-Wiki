---
title: "Gonzalez et al. 2026 - ArchAgent v2 data-prefetching championship (arXiv 2608.09874) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, agentic-ai, microarchitecture, cs-ar, k156]
keywords: [2608.09874, ArchAgent, data prefetching, evolutionary search, hardware design]
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

- @concepts/corpus-overflow-out-of-scope.md — microarchitecture agent search; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K156 digest fetch
- @sweeps/2026-08-11-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-11_k156-archagent-v2-and-evolutionary-replay-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ArchAgent v2: A Case Study with the Data Prefetching Championship |
| **Authors** | Abraham Gonzalez, Raghav Gupta, Akanksha Jain, Hanna Alam, Alexander Novikov, Po-Sen Huang, Matej Balog, Marvin Eisenberger, Sergey Shirobokov, Ngân Vũ, Hank Levy, Borivoje Nikolić, Sagar Karandikar, Martin Dixon, Parthasarathy Ranganathan (Google + UC Berkeley + Google DeepMind) |
| **arXiv** | 2608.09874 |
| **Filename** | `arxiv-2608.09874-archagent-v2-a-case-study-with-the-data-prefetch.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.09874-archagent-v2-a-case-study-with-the-data-prefetch.pdf` |
| **Retrieved** | 2026-08-11 |
| **Code** | **Watch** — no clear licensed ArchAgent repo URL on arXiv page (only tooling references); do not clone |

## Narrative

Scales agentic automated microarchitecture search to multi-level data prefetching. ArchAgent originally discovered single-level cache replacement policies in competition settings but did not scale to multi-level prefetching. Two additions: a **cascaded evolutionary search** that subdivides the design space by sequentially evolving and freezing prefetchers at individual cache levels, and a **hardware-realizability feedback loop** embedding real-time size-estimates to keep designs within strict hardware budgets.

**SEO remit:** cs.AR / systems-agent false positive — not local SEO. Federation: **CCC** (agent search-loop / staged-evolution harness design) with optional Atto thin if the search pattern clearly serves agent loops (skipped — no genealogy-loop fit). No forced GEO steal.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. Code **Watch**. Local SEO disk: **0 MB**. **GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "We introduce two new additions to ArchAgent: a cascaded evolutionary search that subdivides the design space by sequentially evolving and freezing prefetchers at individual cache levels, and a hardware-realizability feedback loop that embeds real-time size-estimates." [Source: arXiv 2608.09874 Abstract]
