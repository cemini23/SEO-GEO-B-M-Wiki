---
title: "Uberti-Bona Marin et al. 2026 - ConsumerQ audit of AI product recommendations (arXiv 2609.18729)"
type: source
tags: [source, arxiv, geo-aeo, audit, commercial-advice, k172]
keywords: [2609.18729, ConsumerQ, AI audit, ChatGPT, Gemini, AI Overviews, product recommendations]
related:
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-17-daily.md
  - concepts/geo-visibility-measurement.md
  - concepts/llm-brand-bias-geo-competition.md
  - concepts/competitive-geo-citation-factors.md
  - sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md
  - sources/arxiv-2609-28372-agentic-surrogate-shopper-2026-09-24.md
maturity: validated
read_status: skimmed
created: 2026-09-17
updated: 2026-09-24
cross-wiki-routed: cybersecurity-wiki
---

## Relations

- @concepts/federated-daily-research-digest.md
- @sweeps/2026-09-17-daily.md
- @concepts/geo-visibility-measurement.md
- @concepts/llm-brand-bias-geo-competition.md
- @concepts/competitive-geo-citation-factors.md
- @sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md
- @sources/arxiv-2609-28372-agentic-surrogate-shopper-2026-09-24.md — agentic **surrogate shopper** + pricing heuristics (cross-wiki from cyber ingest)
- Cyber brief (repo root): `../Cybersecurity wiki/briefs/2026-09-17_k172-consumerq-ai-audit-cyber-from-seo.md` (thin)


## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | "If I Had to Buy Just ONE: Galaxy S26 Ultra": Auditing AI-Generated Product Recommendations |
| **Authors** | Lucas G. Uberti-Bona Marin et al. |
| **arXiv** | 2609.18729 (cs.CY, cs.CL) |
| **Filename** | `arxiv-2609.18729-if-i-had-to-buy-just-one-galaxy-s26-ultra-auditi.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.18729-if-i-had-to-buy-just-one-galaxy-s26-ultra-auditi.pdf` |
| **Retrieved** | 2026-09-17 |
| **Code** | Bajemon: released offline artifacts; ConsumerQ: dataset paper; Martinez: framework calculations — no default clone this pass |

## Narrative

AI audit of commercial-advice chatbots using **ConsumerQ** (2,528 real queries) and 1,536 product responses across ChatGPT (UI + API), Gemini (UI + API), and Google Search AI Overviews.

**Findings:** ChatGPT expresses first-person product preference in **79%** of product-recommending responses vs **7%** Gemini and **2%** AI Overviews; recommendations change across repeated requests. ChatGPT vs Gemini UI share only **5.4%** of domains on average (76.7% comparisons share **no** domain). APIs diverge from their UIs (12.0% / 14.8% mean domain overlap).

**SEO remit:** **IN-SCOPE PRIMARY** for measurement discipline — local GEO audits must sample **repeated queries**, **consumer-facing UI** (not API-only), and treat source-layer overlap as part of the estimand. Thin steal on @concepts/geo-visibility-measurement.md + @concepts/llm-brand-bias-geo-competition.md. Federation: **Cyber thin** (commercial-advice audit methodology).

**Phase-0:** ADOPT pattern (audit protocol; ConsumerQ dataset). **GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "Neither isolated responses nor API observations can be assumed to represent the commercial advice consumers encounter." [Source: arXiv 2609.18729 Abstract]
