---
title: "Shinde et al. 2026 - Priority scheduling in programmable data plane switches (arXiv 2610.04587) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, networking, packet-scheduling, k285]
keywords: [2610.04587, PIFO, programmable data plane, priority queue, P4, SP-PIFO, AIFO, RIFO, priority inversion]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-10-07-daily.md
maturity: draft
read_status: skimmed
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — networking hardware; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K285 digest fetch
- @sweeps/2026-10-07-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Parallel Architectures For Priority Scheduling In Programmable Data Plane Switches |
| **Authors** | Nikhil Shinde, Krishna M. Sivalingam (IIT Madras); Gauravdeep Shami (Ciena Corporation) |
| **arXiv** | 2610.04587 |
| **Filename** | `arxiv-2610.04587-parallel-architectures-for-priority-scheduling-i.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2610.04587-parallel-architectures-for-priority-scheduling-i.pdf` |
| **Retrieved** | 2026-10-07 |
| **Code** | None linked. The paper references `barefootnetworks/Open-Tofino` and `ndal-eth/netbench` as tooling, not as its own release. |

## Narrative

Programmable Data Plane (PDP) switches process packets flexibly but schedule them poorly. **PIFO** (Push-In First-Out) gives an ideal priority-queue abstraction — packets ordered by user-defined rank — but needs line-rate sorting, which is impractical at 100 Gbps and beyond. Approximate schedulers (**SP-PIFO**, **AIFO**, **RIFO**) cut the complexity but introduce **priority inversions**, so a packet can be served out of order.

The paper proposes parallel architectures for priority scheduling on PDP hardware. It is a switch-ASIC and packet-scheduling result.

**SEO remit:** no GBP/GEO/local-search playbook — overflow inventory only. No transferable steal. The wiki has no analogue for line-rate packet ordering, and the "priority inversion" concept does not map onto search or citation ranking. Routed nowhere.

**Why it was fetched:** the daily digest's `local-seo-paper` arXiv query matched it. See @concepts/corpus-overflow-out-of-scope.md for the query-hygiene note — the config has since been corrected.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. No paper code; the referenced repos belong to other projects. No clone.

## Snippets

> "Existing accurate schedulers involve complex packet movement between the scheduling queues. Approximate schedulers such as SP-PIFO, AIFO, and RIFO reduce complexity but introduce priority inversions." [Source: arXiv 2610.04587 Abstract]
