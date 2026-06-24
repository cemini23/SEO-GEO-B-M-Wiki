---
title: K128 hands-on — multilingual review sentiment polarity check
type: brief
target: hands-on
created: 2026-06-24
updated: 2026-06-24
sources:
  - sources/arxiv-rajiv-2026-sentiment-polarity-bias-reviews-2606.22745-2026-06-24.md
  - concepts/reviews-reputation-management.md
  - concepts/review-response-templates.md
---

## Target

**hands-on** — operator sanity-checks automated sentiment on non-English reviews before trusting dashboard flags.

## Summary

Rajiv 2026: LLMs show **negative bias in French** review classification; mDeBERTa shows **positive bias in Japanese** (misses indirect criticism). Polarity bias is **architecture + language specific**.

## Body

### Step 1 — Sample 20 reviews per language

Pull from GBP/Yelp where shop receives non-English reviews. Tag manually:

- [ ] Clearly positive
- [ ] Clearly negative
- [ ] Mixed / indirect criticism

### Step 2 — Compare tool labels

If using BrightLocal, Birdeye, or native platform sentiment:

- List reviews where **your human tag ≠ tool tag**
- Note language of mismatches

### Step 3 — French / Japanese patterns (if applicable)

| Language | Watch for |
|----------|-----------|
| French | Tool over-flags negative; verify before escalation |
| Japanese | Tool may miss polite/indirect negatives |

Other languages: still run Step 2 — bias may exist `[NEEDS VERIFICATION 2026-06-24]`.

### Step 4 — Response workflow

- **Never auto-reply** from sentiment flags alone (@concepts/review-response-templates.md)
- Prioritize human read for mismatched-language reviews
- Log patterns for monthly review (@concepts/reviews-reputation-management.md)

### Step 5 — GEO overlap

If AI summaries shop reputation in a language, cross-check against raw review sample — automated polarity skew may feed AI narratives (@sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md).

## Sources

- @sources/arxiv-rajiv-2026-sentiment-polarity-bias-reviews-2606.22745-2026-06-24.md
- @concepts/reviews-reputation-management.md
- @concepts/review-response-templates.md
