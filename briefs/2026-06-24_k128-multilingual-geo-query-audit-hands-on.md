---
title: K128 hands-on — multilingual GEO query audit
type: brief
target: hands-on
created: 2026-06-24
updated: 2026-06-24
sources:
  - concepts/multilingual-geo-audit.md
  - sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md
  - concepts/geo-visibility-measurement.md
  - entities/tools/ranqo.md
---

## Target

**hands-on** — operator tests whether English-only AI queries understate shop visibility in customer languages.

## Summary

Žatuchin 2026: English → home-language queries raise **recommendation share +0.80** for local champions vs **+0.15** for global brands. Run a minimal **language × engine** matrix before trusting English-only Ranqo baselines.

## Body

### Step 1 — Languages (pick 1–2 beyond English)

From shop market: review language mix, customer requests, census. Examples: Spanish, French, Portuguese.

### Step 2 — Engines (fix set for whole audit)

Pick **2–3** engines customers use — e.g. ChatGPT, Gemini, Perplexity. **Do not change engines** when comparing languages (model stability η²=0.32 vs language η²=0.01).

### Step 3 — Prompts (5 per language)

Unbranded buyer-intent, localized:

| English | Example alternate |
|---------|-------------------|
| best barbershop in [city] | mejor barbería en [city] |
| fade haircut near [neighborhood] | [localized equivalent] |
| walk-in barber [city] | … |
| kids haircut [city] | … |
| beard trim [city] | … |

### Step 4 — Score each response

| Field | Record |
|-------|--------|
| **Named** | Shop name appears? |
| **Recommended** | Top pick or explicit shortlist? |
| **Sentiment** | Rough: positive / neutral / critical |
| **Claims** | Hours, price, rating if stated |

### Step 5 — Compare English vs home-language

- **Recommendation rate** = recommended / 5 prompts per language
- **Delta** = home-language rate − English rate
- Local independent shop: expect **large positive delta** `[TENTATIVE]` per Žatuchin local-champion tier

### Step 6 — Verification overlay

For any mention, open cited URLs — claim vs GBP/website (@concepts/per-entity-bias-mapping-geo.md verified mention rate).

### Step 7 — Actions (owned surfaces only)

- Bilingual GBP services + website copy where market warrants
- Consistent NAP across directories in each language where listings exist
- Re-audit quarterly or after major GBP/website language updates

## Sources

- @concepts/multilingual-geo-audit.md
- @sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md
- @concepts/geo-visibility-measurement.md
