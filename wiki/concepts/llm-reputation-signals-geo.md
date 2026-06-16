---
title: LLM reputation signals — selection-stage GEO
type: concept
tags: [geo-aeo, reviews, algorithm-audit, playbook]
keywords: [reputation signals, guest rating, review volume, management response, list position, conjoint audit, local business]
related:
  - sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/generative-engine-optimization.md
  - concepts/reviews-reputation-management.md
  - concepts/geo-visibility-measurement.md
  - concepts/google-business-profile.md
  - concepts/website-essentials-local-business.md
  - sources/vishwakarma-2026-competitive-geo-sigir.md
  - sweeps/2026-06-16-daily.md
  - concepts/federated-daily-research-digest.md
maturity: validated
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- @sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md — causal AMCE foundation (hotels; pre-registered conjoint)
- @concepts/competitive-geo-citation-factors.md — content gatekeepers (price on page, specs); this page = **reputation** gatekeepers at selection
- @concepts/generative-engine-optimization.md — parent GEO hub
- @concepts/reviews-reputation-management.md — acquisition + response policy; LLM weighting differs from human SEO lore
- @concepts/geo-visibility-measurement.md — repeated sampling before declaring signal wins
- @concepts/google-business-profile.md — GBP as reputation signal surface
- @concepts/website-essentials-local-business.md — price transparency on owned site
- @sources/vishwakarma-2026-competitive-geo-sigir.md — head-to-head **content** competition; complementary bottleneck
- @sweeps/2026-06-16-daily.md — K120 ingest

## Raw Concept

Operator playbook for **reputation signals** that move LLM **selection** among a fixed candidate set (assistant already retrieved N options). Synthesized from @sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md (Baig et al., arXiv 2606.16344). Study domain: hotels; local-service generalization marked `[TENTATIVE]` / `[NEEDS VERIFICATION 2026-06-16]`.

## Narrative

### Two stages (don't conflate)

| Stage | Question | Primary levers |
|-------|----------|----------------|
| **Retrieval** | Does the business appear in the candidate set at all? | SEO, citations, GBP, links (@concepts/citation-building.md) |
| **Selection** | Which candidate gets recommended? | Reputation signals + price + position (@sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md) |

Vishwakarma 2026 (@sources/vishwakarma-2026-competitive-geo-sigir.md) focuses on **content quality** when two pages compete. Baig 2026 isolates **managed reputation attributes** when five comparable cards compete — closer to "best barber in [city]" pick-one flows.

### Causal signal weights (pooled 12-model panel) `[CONFIRMED in hotel conjoint]`

Ranked by absolute AMCE on recommendation probability:

1. **Star rating / valence** — +31.6 pp (4.7★ vs 3.9★). Highest ROI: protect rating quality, resolve legitimate negatives, avoid review-gating that skews sample.
2. **Price level** — −30.0 pp ($249 vs $129). Publish **explicit service prices** on website + GBP; "call for pricing" hurts selection when assistants compare cards.
3. **Review volume** — +8.3 pp (2,100 vs 45 reviews). Steady ethical acquisition (@concepts/reviews-reputation-management.md); volume matters after rating floor.
4. **Eco / sustainability badge** — +11.6 pp in hotels; **highly model-heterogeneous** (+0.2 to +29.9 pp per model). Do not build barbershop strategy around green badges unless verified on target engines `[NEEDS VERIFICATION 2026-06-16]`.
5. **Review recency** — +1.6 pp (recent review vs stale). Modest; still worth organic review flow.
6. **Chain vs independent** — −1.8 pp (chain penalty in hotel study). May not transfer to barbershop franchises `[TENTATIVE]`.
7. **Management response visible on card** — **+0.1 pp (null)**. Industry GEO advice often promotes response rate; **no causal selection lift** in this audit. Continue responding for humans + GBP engagement; do not expect LLM citation wins from response volume alone.

**List position** (slot in presented list): −2.1 to −3.7 pp vs first slot — **content-free** bias worth ~$12/night in hotel WTP translation. Classical SEO that improves retrieval rank still buys selection advantage.

### Barbershop translation checklist `[TENTATIVE]`

| Hotel signal | Barbershop analog | Action |
|--------------|-------------------|--------|
| Guest rating | Google/Yelp star rating | Monitor ≥4.5★; fix service failures driving 1–2★ themes |
| Price card | Service menu prices | List fade/skin fade/beard trim prices on site + GBP services |
| Review volume | Google review count | In-person ask + QR; no gating |
| Management response | Owner replies on GBP | Keep for trust; **deprioritize as GEO tactic** |
| Eco-cert | Sustainability claims | Only if genuine + verified for your market |
| List position | Map pack / AI list order | Local pack SEO + completeness |

### Measurement discipline

- Run **≥3-day repeated** assistant tests (@concepts/geo-visibility-measurement.md) — Baig used 60k+ calls; operator smoke tests are noisier.
- Optional: **conjoint-style audit** — present 3–5 anonymized competitor cards with randomized attribute levels; log which shop assistant recommends (manual replication of paper method at small n).

Hands-on template: `briefs/2026-06-16_k120-geo-reputation-signal-audit-hands-on.md`.

## Snippets

> "Management response … has no detectable effect (+0.1 pp, statistically equivalent to zero)." [Source: @sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md]

> "List position—a content-free artifact—shifts recommendations causally." [Source: @sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md]
