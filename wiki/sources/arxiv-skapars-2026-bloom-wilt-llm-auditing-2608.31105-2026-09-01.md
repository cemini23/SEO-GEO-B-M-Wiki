---
title: "Skapars & Manino 2026 - BLOOM-WILT logit tilting for LLM auditing (arXiv 2608.31105) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, llm-auditing, red-team, k167]
keywords: [2608.31105, BLOOM-WILT, WILT, logit tilting, behaviour elicitation, automated auditing]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - concepts/generative-engine-optimization.md
  - sweeps/2026-09-01-daily.md
  - sources/dong-2025-safesearch-red-teaming.md
maturity: draft
read_status: skimmed
created: 2026-09-01
updated: 2026-09-01
cross-wiki-routed: cybersecurity-wiki
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — automated LLM safety auditing; not local-pack SEO
- @concepts/federated-daily-research-digest.md — K167 digest fetch
- @concepts/generative-engine-optimization.md — deployment-scale behaviour gaps vs lab eval (adjacent only)
- @sweeps/2026-09-01-daily.md — overnight inbox drop
- @sources/dong-2025-safesearch-red-teaming.md — prior search-agent red-team routing pattern
- Cyber brief (repo root, not wiki/): `../Cybersecurity wiki/briefs/2026-09-01_2026-09-01_k167-bloom-wilt-llm-auditing-from-seo.md` (**primary**)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | BLOOM-WILT: Logit Tilting for Behaviour Elicitation in Automated LLM Auditing |
| **Authors** | Adrians Skapars, Edoardo Manino |
| **arXiv** | 2608.31105 (cs.AI, cs.CL) |
| **Filename** | `arxiv-2608.31105-bloom-wilt-logit-tilting-for-behaviour-elicitati.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.31105-bloom-wilt-logit-tilting-for-behaviour-elicitati.pdf` |
| **Retrieved** | 2026-09-01 |
| **Code** | No public repo URL in abstract → Watch / 0 MB |

## Narrative

Deployed LLMs see orders of magnitude more interactions than any pre-deployment eval. Automated auditors scale cheaply but stay sample-inefficient without optimisation pressure. **BLOOM-WILT** is a full auditing pipeline that elicits natural multi-turn rare behaviours using only next-token access (no training cost). **WILT** revises conversational strategy across rounds from scored interactions; on the output side it adaptively reweights decoding via logit tilting conditioned on an elicitation prompt so behaviour-relevant tokens rank ahead of equally probable unprompted outputs.

Evaluated on 4 target models × 8 behaviours: beats baseline auditor in 30/32 settings; overturns prior model safety rankings. Example: self-harm encouragement presence on Qwen3.5-4B rises from 51% → 100% at matched compute without pushing output probability below baseline.

**SEO remit:** agent safety / red-team false positive — no GBP ranking playbook. Federation: **Cyber primary** (automated behaviour elicitation for deployed LLM audits). **CCC thin steal:** logit-tilting elicitation vocabulary for harness eval gaps (pairs K260 adversarial curriculum — sample-inefficient happy-path eval misses deployment behaviours).

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "We introduce BLOOM-WILT, a full auditing pipeline that elicits natural multi-turn instances of rare behaviours, without training cost or access beyond the target's next-token distribution." [Source: arXiv 2608.31105 Abstract]

> "WILT adaptively reweights the target's decoding using the model's own distribution conditioned on an elicitation prompt, so that behaviour-relevant generations are sampled ahead of others it finds equally probable when unprompted." [Source: arXiv 2608.31105 Abstract]
