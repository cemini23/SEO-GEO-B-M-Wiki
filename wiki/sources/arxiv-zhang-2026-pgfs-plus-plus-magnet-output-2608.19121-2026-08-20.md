---
title: "Zhang et al. 2026 - PGFS++ Molecular Property Improvement under Synthesis and Diversity Constraints (arXiv 2608.19121) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, molecular-rl, reward-hacking, drug-discovery, k161]
keywords: [2608.19121, PGFS++, magnet output, reward hacking, synthesis-aware RL, diversity]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-20-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-20
updated: 2026-08-20
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — synthesis-aware molecular RL; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K161 digest fetch
- @sweeps/2026-08-20-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-20_k161-gbp-consensus-and-magnet-output-from-seo.md` (CCC thin — magnet-output reward-hack)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | PGFS++: Molecular Property Improvement under Synthesis and Diversity Constraints |
| **Authors** | Boqiao Zhang, Godbless Tamaraebi James, Sai Krishna Gottipati, Andrew Fitzgibbon (Graphcore + University of Cambridge) |
| **arXiv** | 2608.19121 (cs.LG / q-bio) |
| **Filename** | `arxiv-2608.19121-pgfs-molecular-property-improvement-under-synthe.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.19121-pgfs-molecular-property-improvement-under-synthe.pdf` |
| **Retrieved** | 2026-08-20 |
| **Code** | No public PGFS++ repo located (do **not** confuse with Graphcore `ogb-lsc-pcqm4mv2` / GPS++) → Watch / 0 MB |

## Narrative

PGFS (Policy Gradient for Forward Synthesis) constrains molecular improvement to synthesizable routes. **PGFS+** replaces continuous reactant-embedding prediction with trainable embedding lookup + global scoring — property scores rise, but a **magnet-output** failure appears: many distinct inputs collapse to the same high-reward molecule (reward hacking / diversity ≈ 0). **PGFS++** adds an input–output similarity bonus so improvement stays input-specific while preserving diversity.

**SEO remit:** chemistry/RL false positive — not local SEO. Federation: **CCC thin** — *magnet output* as a named reward-hacking mode when a powerful search maps a diverse input set onto one attractor; measure diversity alongside reward. Do not clone Graphcore GPS++ as this paper's code.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "However, it exposes a reward-hacking failure mode: a powerful reactant search can map diverse input molecules to the same high-reward “magnet molecule”, improving the reward while collapsing the output diversity." [Source: arXiv 2608.19121 Abstract]

> "We therefore introduce PGFS++, a synthesis-aware reinforcement learning framework for input-specific molecular improvement." [Source: arXiv 2608.19121 Abstract]
