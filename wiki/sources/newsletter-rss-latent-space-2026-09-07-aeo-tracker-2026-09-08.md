---
title: "Latent Space — Frontier AEO Tracker (K257 steal)"
type: source
tags: [source, newsletter, geo-aeo, model-bias, measurement, content-negotiation, k257]
keywords: [Frontier AEO Tracker, Latent Space, markdown content negotiation, self-preference, anti-recommendation, 161 categories]
related:
  - concepts/generative-engine-optimization.md
  - concepts/geo-visibility-measurement.md
  - concepts/agent-ready-website-local-bm.md
  - concepts/llm-brand-bias-geo-competition.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-10-01-daily.md
maturity: validated
read_status: read
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- @concepts/generative-engine-optimization.md — AEO hub
- @concepts/geo-visibility-measurement.md — self-preference is a measurement hazard
- @concepts/agent-ready-website-local-bm.md — markdown content-negotiation is a readability lever
- @concepts/llm-brand-bias-geo-competition.md — self-preference bias, measured across seven models
- @concepts/ai-citation-sourcing-geo.md — audit cited third-party sources, not only your own
- @concepts/corpus-overflow-out-of-scope.md — K257 wave sibling
- @concepts/federated-daily-research-digest.md — K257 inbound from OSINT
- @sweeps/2026-10-01-daily.md — K257 wave

## Raw Concept

| Field | Value |
|-------|-------|
| **Source** | Latent Space — Frontier AEO Tracker |
| **Original** | https://www.latent.space/ (Frontier AEO Tracker post, 2026-09-07) |
| **Retrieved via** | mirror summaries, 2026-10-01 (originating OSINT source page never materialised — see note) |
| **Inbound** | OSINT K257 → SEO K257 brief (`briefs/2026-09-08_k257-seo-aeo.md`) |
| **Read status** | read (paraphrased) |

**Provenance note.** The OSINT wave page `@osint-wiki/concepts/k257-ccc-aeo-wave.md` references an OSINT source page that does not exist on disk. This page is filed from the wave summary plus the public tracker coverage, so it records the steal with a weaker provenance chain than a normal ingest. `[NEEDS VERIFICATION 2026-10-01]` on any figure not restated in the tracker's own post.

## Narrative

**What it measures.** Which products **seven frontier AI models** recommend across **161 categories**, with web search enabled. It scores first choices, alternatives, and plain mentions, and is queryable by model, category, entity, or cited source.

**Method.** Seven models — Claude Opus 5, Claude Fable 5.1, GPT-5.6 Sol, GPT-6 Astra, Grok, Muse, SWE-1.7 — over 161 categories with **6 prompt variations each**. Gemini, GLM, and DeepSeek were excluded for technical reasons, so **Google is absent from the set**. Answer extraction used GPT-6 Astra.

**The findings that matter for an operator:**

1. **Self-preference is the clearest signal in the whole tracker.** Opus and Fable pick Claude Code; Sol and Astra pick Codex; Muse picks Muse Code; SWE-1.7 picks Devin. Only Grok picks an unaffiliated tool (Cursor) — it ships no coding agent of its own. **Read this as a measurement warning, not a product finding:** an "AI visibility" number partly reports *which model you asked*. This is the same hazard K283 measured from a different direction (harness variance of sevenfold).
2. **~17% of categories have a single universal winner** — 28 of 161. In those categories expect long displacement. The tracker's own advice is to pick a narrower category.
3. **Search behaviour differs sharply by vendor.** OpenAI's median source count fell from **9 (Sol) to 5 (Astra)**; Anthropic's rose from **11 (Opus) to 15 (Fable)**.
4. **Paraphrase stability varies.** Astra is less likely to change its answer when a question is reworded, which makes its recommendations behave more like a durable ranking and less like a sample.
5. **Markdown content-negotiation is confirmed as a real factor.** Serving a clean markdown version when an agent requests it — instead of JavaScript-heavy HTML. The tracker reports that **failures actively discourage models from reading the content at all**, removing the page from consideration. This corroborates the Ora and Vercel findings already in the wiki.

**AEO score composition** (formula proprietary, not published): first choices weigh most, then alternatives, then mentions. **Negative weights** apply for mild and strong **anti-recommendations** — rare, but real.

**Their practical sequence:**

1. Read actual prompt/answer pairs, not just rankings.
2. Check whether the category has a universal winner before spending.
3. Fix markdown content-negotiation.
4. Audit the **cited third-party sources**, not only your own site.
5. Re-check after every frontier model release — the tracker calls generation-to-generation flips "VERY consequential."

**SEO remit for this wiki:** the **content-negotiation** point is the operator-actionable one, and it slots directly into @concepts/agent-ready-website-local-bm.md beside the K283 readability evidence. The **self-preference** finding is the measurement caveat the wiki already applies to single-engine benchmarks. The **anti-recommendation** weighting is new: copy that a model actively warns against costs more than copy it simply ignores.

**Do not** treat the tracker's category winners as a GBP ranking table, and do not swap the wiki's routing or tooling on the strength of these rankings.

## Limitations (the tracker's own)

- **No Google models** in the set (Gemini excluded), so the picture omits the largest AI surface for local business.
- **Source analysis reflects attempted tool-call scraping** only.
- **Proprietary scoring** prevents independent reproduction.
- Some **deduplication outstanding** at publication.

## Snippets

> "28 of 161 categories (~17%) have a single universal winner across every model." [Source: Frontier AEO Tracker coverage, retrieved 2026-10-01]

> Failure to serve agent-readable markdown "actively discourage[s] models from reading your content." [Source: Frontier AEO Tracker coverage, retrieved 2026-10-01]

> OpenAI's median sources dropped from 9 (Sol) to 5 (Astra); Anthropic's rose from 11 (Opus) to 15 (Fable). [Source: Frontier AEO Tracker coverage, retrieved 2026-10-01]
