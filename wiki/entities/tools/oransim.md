---
title: "oransim — local-first causal simulator for marketing-campaign ROI"
type: entity
tags: [tool, marketing-analytics, causal-modeling, campaign-roi, structural-causal-model, apache-2, adopt]
keywords: [oransim, oranai, causal simulator, structural causal model, marketing roi, do-calculus, hawkes process, llm user souls, creative-to-user graph]
related:
  - concepts/competitor-analysis-local.md
  - concepts/creator-content-strategy.md
maturity: draft
created: 2026-05-17
updated: 2026-07-31
osint_eval_origin: "OSINT 56-repo multi-wiki tool eval, 2026-05-17 (SEO primary fit)"
wire_status: wont_wire
wire_target: Out of SEO remit / no operator wire
---

## Relations

- `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md` — OSINT cross-route origin (56-repo tool eval)
- @concepts/competitor-analysis-local.md — campaign-ROI forecasting complements competitive-landscape analysis before capital deployment
- @concepts/creator-content-strategy.md — creator-marketing content can be simulation-tested against an LLM-user-souls model before posting

## Raw Concept

Cross-routed from the OSINT workspace 56-repo multi-wiki tool eval, 2026-05-17. Routed to the SEO wiki as the primary-fit destination on the marketing-analytics vertical.

- **Repo**: [OranAi-Ltd/oransim](https://github.com/OranAi-Ltd/oransim)
- **License**: Apache-2.0
- **Language**: Python / Structural Causal Models
- **Tier**: Adopt (SEO primary fit)

## Narrative

oransim is a **local-first causal simulator** that predicts marketing-campaign ROI. Rather than A/B-testing live with real ad spend, it models a campaign as a **structural causal model (SCM)** over a creative-to-user graph and runs the campaign in simulation first.

### How it works

- **Structural causal model** over a creative-to-user graph — the campaign's creative assets and the audience are nodes; causal edges carry the predicted influence.
- **LLM-driven user "souls"** — simulated users react to content via embeddings, giving a behaviorally plausible response to each creative rather than a flat conversion-rate assumption.
- **Hawkes processes** — model the temporal cascade of engagement (one interaction triggering follow-on interactions / self-exciting spread).
- **do-calculus** — answers interventional questions ("what ROI *if* we change this creative / this channel mix?") rather than just correlational ones.

### SEO-wiki relevance

oransim bridges creator-marketing analysis with mathematical forecasting: **test campaign assets before capital deployment**. For the creator-marketing vertical it lets a content plan be stress-tested against simulated audience reaction before posting (see @concepts/creator-content-strategy.md). For local-business marketing it complements competitor analysis — model expected ROI of a promotion against the competitive landscape before spending (see @concepts/competitor-analysis-local.md).

Apache-2.0, local-first — no data leaves the laptop, no per-query SaaS cost.

### Caveats (Phase-0 follow-up)

- A simulator's output is only as good as the SCM and embedding assumptions — treat predicted ROI as a `[TENTATIVE]` directional signal, not a guaranteed number, until validated against a real campaign.
- LLM "user souls" can encode the base model's biases; the simulated audience is a model of the audience, not the audience.
- Maturity signals (stars, commit cadence, maintainer) not captured in the eval — verify before adoption.

### Cross-route notes

- **osint-wiki** — causal modeling / temporal-cascade analysis (Hawkes processes + do-calculus are directly reusable for prediction-market and quant-finance cascade work).

## Snippets

> Apache-2.0, Python / Structural Causal Models — local-first causal simulator predicting marketing-campaign ROI via an SCM over a creative-to-user graph; LLM-driven user "souls" react via embeddings; uses Hawkes processes + do-calculus. [Source: @osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md]
