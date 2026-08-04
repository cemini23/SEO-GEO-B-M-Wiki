---
title: "Lin et al. 2026 - AtumAI agentic datacenter control-plane policies (arXiv 2608.02569) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, agents, systems, datacenter, k151]
keywords: [2608.02569, AtumAI, datacenter, control plane, agentic AI, Azure, evolutionary search]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-04-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — datacenter control-plane agents; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K151 digest fetch
- @sweeps/2026-08-04-daily.md — overnight inbox drop
- Cross-wiki brief: `../Cemini claude code CCC/briefs/2026-08-04_k151-atumai-agentic-policy-search-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies |
| **Authors** | Qiushi Lin, Chaojie Zhang, Íñigo Goiri, Aditya Akella, Ricardo Bianchini, Jovan Stojkovic (UT Austin / Microsoft Azure) |
| **arXiv** | 2608.02569 |
| **Filename** | `arxiv-2608.02569-atumai-a-principled-framework-for-agentic-genera.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.02569-atumai-a-principled-framework-for-agentic-genera.pdf` |
| **Retrieved** | 2026-08-04 |
| **Code** | None linked (Azure Public Dataset cited only) |

## Narrative

**AtumAI** compiles a natural-language datacenter control task into a machine-checkable IR (objectives, constraints, decision vars, eval methodology), then searches with diffusion + evolutionary tuning + surrogate filtering. Evaluated on workload placement (+17% success / +8% scheduler throughput), resource scaling (+24% cost efficiency), and power management (−21% power / +17% throughput) vs expert baselines.

**SEO remit:** systems/cloud false positive — overflow. Steal shape for CCC: formalize informal agent goals into searchable specs before LLM proposal loops; expand search beyond the LLM alone.

**Phase-0:** OUT-OF-SCOPE for SEO. No local adopt. **Atto / GuruWatcher / TipDrop / poker / prod:** SKIP (not a prod harness pin).

## Snippets

> "From a goal stated in plain language, AtumAI autonomously proposes, tests, and refines candidate policies until one satisfies the request." [Source: arXiv 2608.02569 Abstract]
