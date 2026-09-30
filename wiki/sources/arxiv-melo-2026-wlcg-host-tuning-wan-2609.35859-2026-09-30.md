---
title: "Melo et al. 2026 - WLCG host tuning for WAN data transfers (arXiv 2609.35859) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, networking, hpc, host-tuning, k283]
keywords: [2609.35859, WLCG, FTS, TCP tuning, ring buffer, offload, iperf3, bottleneck]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-30-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-30
updated: 2026-09-30
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — HEP network/host tuning; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K283 digest fetch
- @sweeps/2026-09-30-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | WLCG Mini-Capability Challenge: Host Tuning to Improve WAN Data Transfers |
| **Authors** | Andrew Malone Melo et al. (Vanderbilt, Michigan, UCSD, BNL, UMass Amherst, ESnet, UNL, Michigan State, Fermilab) |
| **arXiv** | 2609.35859v1 [physics.ins-det] |
| **Submitted** | 25 September 2026 |
| **Filename** | `arxiv-2609.35859-wlcg-mini-capability-challenge-host-tuning-to-im.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.35859-wlcg-mini-capability-challenge-host-tuning-to-im.pdf` |
| **Retrieved** | 2026-09-30 |
| **Code** | None linked (method uses ESnet Fasterdata guidance + the OSG-hosted `fasterdata-tuning.sh` framework) |

## Narrative

A WLCG mini-capability challenge applying TCP, queue, offload, and ring-buffer host tuning across ATLAS/CMS sites (FNAL, UCSD, UNL, BNL, AGLT2, MWT2, Vanderbilt) on EL8/9 hosts with ≥25 Gbps NICs, plus a trans-Atlantic NET2 test.

Headline: **tuning benefit depends entirely on the local bottleneck.** At UNL (DTN and storage both capable) FTS throughput rose **60 → 90 Gbps**. At UCSD (storage-bound) iperf3 improved **20 → 90 Gbps** while FTS was unchanged. At Vanderbilt (25 G NIC-bound) the same profile **actively reduced** throughput. The challenge also found and fixed a dCache proxying misconfiguration at AGLT2 — a diagnostic outcome with no performance component.

**SEO remit:** no GBP/GEO/local-search playbook — overflow inventory only. Distant analog worth remembering: an intervention's sign depends on the binding constraint, so the same "best practice" can help one site and hurt another. This is the same shape as the Martinez 2026 finding that GEO heuristics transfer poorly across contexts (@concepts/geo-visibility-vector-protocol.md). Noted; no routed brief.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. No paper code; `esnet/iperf` and `axboe/fio` appear only as measurement tools. Not domain-relevant.

## Snippets

> "Results show that tuning benefit depends critically on the local bottleneck." [Source: arXiv 2609.35859 Abstract]
