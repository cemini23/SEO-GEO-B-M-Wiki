---
title: "Fayolle et al. 2026 - Benchmarking microarchitectural side-channel attacks (arXiv 2609.03893) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, side-channel, benchmarking, cyber, k170]
keywords: [2609.03893, side-channel, microarchitectural, benchmarking, cs.CR]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-11-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-11
updated: 2026-09-11
cross-wiki-routed: cybersecurity-wiki
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md
- @concepts/federated-daily-research-digest.md
- @sweeps/2026-09-11-daily.md
- Brief (repo root): `../Cybersecurity wiki/briefs/2026-09-11_k170-side-channel-benchmarking-cyber-from-seo.md` (**primary**)


## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Practice Makes (Im)Perfect: A Look Back at Benchmarking Practices for Microarchitectural Side-Channel Attacks |
| **Authors** | Iliana Fayolle et al. |
| **arXiv** | 2609.03893 (cs.CR) |
| **Filename** | `arxiv-2609.03893-practice-makes-im-perfect-a-look-back-at-benchma.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.03893-practice-makes-im-perfect-a-look-back-at-benchma.pdf` |
| **Retrieved** | 2026-09-11 |
| **Code** | None located this pass → Watch / 0 MB |

## Narrative

Microarchitectural side-channel research has grown quickly, but benchmarking practices often still rely on indirect proxies (covert-channel bandwidth, naive AES/RSA key recovery) copied from early papers without questioning whether they measure real attack risk.

This look-back surveys benchmarking habits and argues many standard proxies are **imperfect** — they can over- or under-state practical leakage. **Cyber remit:** federation **Cyber primary** (side-channel eval hygiene; pairs cache-timing / Spectre-class audit patterns). **Phase-0:** OUT-OF-SCOPE for SEO Adopt; no public exploit tooling to clone → 0 MB.

## Snippets

> "Early attack papers typically relied on indirect proxies, such as covert-channel bandwidth or key-recovery on naive AES and RSA implementations, setting de facto standards that many subsequent works continued to replicate." [Source: arXiv 2609.03893 Abstract]
