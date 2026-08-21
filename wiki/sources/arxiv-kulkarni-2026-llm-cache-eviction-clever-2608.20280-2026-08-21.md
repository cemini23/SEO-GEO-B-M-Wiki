---
title: "Kulkarni, Harkare & Suresh Yogesh Babu 2026 - Which Eviction Policy Should an LLM Cache Use? CLEVER (arXiv 2608.20280) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, llm-cache, semantic-caching, eviction-policy, k162]
keywords: [2608.20280, CLEVER, semantic cache, LFU, eviction policy, quality-adjusted hit rate, answer-substitutable]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-21-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — LLM serving / cache eviction; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K162 digest fetch
- @sweeps/2026-08-21-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-21_k162-pandora-routing-and-cache-eviction-from-seo.md` (CCC thin — LFU default + quality-adjusted hit rate)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads, Capacities, and Encoders |
| **Authors** | Yash Kulkarni, Shubham Harkare, Arvind Suresh Yogesh Babu (University of Michigan, CSE 584) |
| **arXiv** | 2608.20280 (cs.LG) |
| **Filename** | `arxiv-2608.20280-which-eviction-policy-should-an-llm-cache-use-a.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.20280-which-eviction-policy-should-an-llm-cache-use-a.pdf` |
| **Retrieved** | 2026-08-21 |
| **Code** | CLEVER course-project commits (`39676dd` / `e4f39ee` / `d386ffa`) but **no public GitHub located** (search 2026-08-21) → Watch / 0 MB. Do **not** invent a CLEVER repo URL. |

## Narrative

**CLEVER** is a shared protocol comparing semantic-cache eviction policies — FIFO, LRU, LFU, ARC, GDSF, a single-pass streaming adaptation of SISO, and a semantic-redundancy policy — across three ordered/deduplicated query corpora, three cache capacities, and two encoders (18 settings). **No evaluated policy improves on LFU by more than 0.041 percentage points in any setting.** Replacement still matters: FIFO and streaming SISO trail LFU by up to ~8.67 / 8.55 points at tight capacity. A conditional packing result explains the missing upside: under exact lookup and insert-on-miss, a newly inserted entry cannot have a resident neighbor within the hit radius, so a geometry-aware eviction rule receives little new redundancy signal. A separate audit is the sharpest finding for cache economics: at MiniLM's median nearest-neighbor threshold only **2.1–3.9%** of sampled LMSYS/QQP hits are judged *answer-substitutable*, reducing raw hit rates of **51–60%** to **quality-adjusted rates of 1.1–2.2%**; thresholds also do not transfer between embedding models.

**SEO remit:** cs.LG serving false positive — semantic cache ≠ AEO citation-share; no thin GEO steal this pass. Federation: **CCC thin** — LFU as the strongest simple default; **raw hit rate ≠ answer-substitutable quality** (establish answer validity before tuning eviction sub-points); threshold-transfer caution. No public GitHub → Watch / 0 MB. Pairs TokTier/K238 (cache) and route serving.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "No evaluated policy improves on LFU by more than 0.041 percentage points in any of the eighteen settings." [Source: arXiv 2608.20280 Abstract]

> "At MiniLM's median nearest-neighbor threshold, only 2.1–3.9% of sampled LMSYS and QQP hits are judged answer-substitutable, reducing raw hit rates of 51–60% to quality-adjusted rates of 1.1–2.2%." [Source: arXiv 2608.20280 Abstract]
