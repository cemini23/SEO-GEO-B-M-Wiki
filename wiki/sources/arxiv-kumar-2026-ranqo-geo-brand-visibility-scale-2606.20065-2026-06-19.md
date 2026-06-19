---
title: "Kumar 2026 — GEO at scale: brand visibility across AI search engines (arXiv 2606.20065)"
type: source
tags: [source, arxiv, geo-aeo, measurement, vendor, digest]
keywords: [2606.20065, Ranqo, brand visibility, share of voice, listicle, YouTube, brand-stature ladder, AI search]
related:
  - concepts/geo-visibility-measurement.md
  - concepts/generative-engine-optimization.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/content-strategy-local.md
  - concepts/citation-building.md
  - entities/tools/ranqo.md
  - sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md
  - sources/aggarwal-2024-geo-paper.md
  - sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-19-daily.md
maturity: validated
read_status: read
created: 2026-06-19
updated: 2026-06-19
---

## Relations

- @concepts/geo-visibility-measurement.md — production baseline + tier ladder + sentiment noise multiplier
- @concepts/generative-engine-optimization.md — parent GEO hub; SME-focused measurement frame
- @concepts/competitive-geo-citation-factors.md — listicle + third-party corporate citation surfaces
- @concepts/content-strategy-local.md — YouTube + listicle earning for local brands
- @concepts/citation-building.md — third-party peer-brand pages dominate citations
- @entities/tools/ranqo.md — vendor platform (REFERENCE)
- @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md — CI discipline complements Ranqo point estimates
- @sources/aggarwal-2024-geo-paper.md — content-quality lifts; Kumar cites as baseline
- @sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md — brand-stature / incumbent dynamics at selection
- @concepts/federated-daily-research-digest.md — 2026-06-19 digest fetch
- @sweeps/2026-06-19-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines |
| **Author** | Pratyush Kumar (Ranqo / Ranqo AI) |
| **arXiv** | 2606.20065v1 |
| **Filename** | `arxiv-2606.20065-1-introduction-arxiv.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-19 |
| **Read status** | read (methodology, §6 findings, v1.1 protocols) |

## Narrative

Vendor-backed **production measurement** paper from Ranqo: controlled queries to five AI engines (ChatGPT, Perplexity, Gemini, Claude, Grok) tracking mention rate, position, sentiment, share of voice, and citation source classes. **100K+ prompt responses**, **100+ brands**, March–May 2026. Complements academic audits (Baig, Chu, Sielinski) with multi-tenant SaaS telemetry. **Not a randomized intervention study** — baselines + designed v1.1 protocols (P1–P7) for causal follow-up.

### Brand-stature visibility ladder (day-1, unbranded prompts) `[CONFIRMED in Ranqo panel]`

| Tier | Example profile | Day-1 mention rate |
|------|-----------------|-------------------|
| **Tier 1** | Global household names (Stripe, Nike) | **~73%** |
| **Tier 2** | Established mid-market / regional | **~44%** |
| **Tier 3** | Niche / small brands | **~11%** |

~30 pp step per tier. Local barbershop likely Tier 3 analog `[TENTATIVE]` — expect low unbranded category visibility until brand-mass signals accumulate.

### Citation source composition (149,912 citations) `[CONFIRMED in Ranqo panel]`

| Source class | Share |
|--------------|-------|
| Corporate / **third-party** brand pages | **75.2%** |
| Brand-owned (own domain) | **2.9%** |
| YouTube / video | **4.2%** |
| Tech & business media | **3.8%** |
| Reddit / forums | **3.3%** |
| Wikipedia | **2.6%** |

**Headline:** AI engines build "alternatives" answers from **peer-brand and vendor pages**, not the tracked brand's site. Own + third-party corporate ≈ **78%**. Among non-corporate, **YouTube leads** (ahead of Reddit assumption).

### Content format — listicle dominance `[CONFIRMED in Ranqo panel]`

- **59%** of cited pages are content (vs homepage/product landing).
- **Listicles** ("best X") = **35.7%** of content citations (**21%** of all citations) — highest-leverage single format; one ranked list can surface a brand across many prompts.
- Generic articles 31%; how-to guides 9.7%.

### Measurement reliability `[CONFIRMED in Ranqo panel]`

- **Mention** near-binary: 77.5% of (brand, prompt, engine) cells always or never mentioned; flipping rate **6.8%**.
- **Sentiment** flipping rate **45.5%** — **6.7× noisier** than mention; need ≥10 prompts/platform/brand before sentiment scores stabilize.
- **0.0%** cells consistently negative — negativity transient when it appears.

### Per-engine divergence `[CONFIRMED in Ranqo panel]`

Same brand, same prompts, 5 weeks: Perplexity mention rate 37%→62%; ChatGPT 45%→20%; Claude flat ~24%. **Treat each engine as separate market** — Perplexity win ≠ Gemini win.

### Prompt category mention rates (unbranded)

Discovery ~23%; problem/solution & use case ~11%; comparison ~75% (often names brands); brand research ~97%.

### v1.1 protocols (designed, not yet reported)

P1 cross-platform source overlap; P2 position-decay; **P3 RCT closed-loop lift** (centerpiece); P4 schema vs citation (expect near-zero independent schema effect); P5 entity-first sequencing; P6 web-search on/off; P7 white-hat C-SEO replication (Puerto et al.).

### Operator relevance (local B&M) `[TENTATIVE]`

- **Tier diagnosis before spend** — Tier 3 local shops: invest in Wikipedia/press/YouTube mass before per-engine micro-optimization.
- **Earn listicle inclusion** — "best barber in [city]" roundups on media/blogs/review sites > own-site schema alone.
- **YouTube + editorial** — largest non-corporate citation surfaces in panel.
- **Facts up front** — entity + provenance early on page; schema as hygiene not primary lever (P4 hypothesis).
- **14–30 day re-audit loop** — visibility changes observable in weeks per vendor methodology.
- Pair mention-rate tracking with @concepts/geo-visibility-measurement.md bootstrap CIs — Ranqo gives point estimates; Sielinski warns on false precision.

## Snippets

> "The very first visibility runs form a clear three-tier brand-stature ladder: global household names … 73%; established mid-market … 44%; niche and small brands … 11%." [Source: arxiv-2606.20065 §Abstract]

> "Only 2.9% of citations point at the brand's own domain, while 75.2% point at other companies in the same space." [Source: arxiv-2606.20065 §6.5]

> "The listicle … is 35.7% of content citations … the highest-leverage page a brand can target." [Source: arxiv-2606.20065 §6.5]

> "Sentiment is 6.7× noisier than mention at the same observational level." [Source: arxiv-2606.20065 §6.6]
