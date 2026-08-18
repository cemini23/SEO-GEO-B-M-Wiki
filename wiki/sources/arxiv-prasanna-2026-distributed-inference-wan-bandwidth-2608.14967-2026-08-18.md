---
title: "Prasanna C 2026 - When Does Distributed AI Inference Need More Wide-Area Bandwidth? (arXiv 2608.14967) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, distributed-inference, wan, kv-transfer, agentic-compounding, cs-dc, k160]
keywords: [2608.14967, distributed inference, wide-area bandwidth, KV transfer, compute intensity ratio, cs.DC]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-18-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — distributed-systems / WAN inference; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K160 digest fetch
- @sweeps/2026-08-18-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-18_k160-ics-rule-blindness-and-wan-inference-from-seo.md` (CCC thin — KV transfer vs recompute; agentic compounding)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | When Does Distributed AI Inference Need More Wide-Area Bandwidth? A Co-Design Evaluation of Optical, Packet, and Software Levers |
| **Authors** | Prasanna C (Lightstorm) |
| **arXiv** | 2608.14967 (cs.DC) |
| **Filename** | `arxiv-2608.14967-when-does-distributed-ai-inference-need-more-wid.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.14967-when-does-distributed-ai-inference-need-more-wid.pdf` |
| **Retrieved** | 2026-08-18 |
| **Code** | None located (no code URL) → no clone |

## Narrative

Operator's co-design analysis of when cross-site (wide-area) bandwidth is needed for distributed AI inference. It quantifies the compute-intensity-ratio (CIR, bytes-per-FLOP) gap between on-package memory and conventional WAN as four to five orders of magnitude, widening ~12–19%/year, then — answering reviewers who argued "more bandwidth helps" ≠ "provisioned bandwidth beats alternatives" — derives a workload model comparing **moving inference state across sites vs recomputing it**. Crossover is **74–111 Gbps per stream** for a 70B multi-head-attention model, falling to **9–14 Gbps** under grouped-query attention at 1/8 KV heads. Five sensitivity axes: context length, attention architecture, concurrency (queueing), **agentic multi-step compounding**, and loss/jitter-induced effective-bandwidth collapse. Economics: at list GPU prices recomputation is cheaper than transfer; transfer wins when GPU scarcity and KV reuse multiply effective GPU cost by roughly **5–20×**. It positions packet (millisecond lit-capacity allocation) vs optical (minute-timescale fungibility) as complementary rather than adversarial, and specifies a ten-metric measurement plan on a three-site production-fibre testbed.

**SEO remit:** cs.DC distributed-inference/network paper — false positive, not local SEO/GEO. **CCC thin** (KV transfer vs recompute; agentic compounding). No code URL → no clone.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **Atto / GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "a context-independent crossover at 74–111 Gbps per stream for a 70B multi-head-attention model, falling to 9–14 Gbps under grouped-query attention at 1/8 KV heads" [Source: arXiv 2608.14967 Abstract]

> "at list GPU prices recomputation is cheaper than transfer; transfer wins when GPU scarcity and KV reuse multiply the effective GPU cost by roughly 5–20×" [Source: arXiv 2608.14967 Abstract]
