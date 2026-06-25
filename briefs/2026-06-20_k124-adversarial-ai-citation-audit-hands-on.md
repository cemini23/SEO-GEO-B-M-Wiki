---
title: K124 hands-on — adversarial misinformation in AI local answers
type: brief
target: hands-on
created: 2026-06-20
updated: 2026-06-20
sources:
  - concepts/citation-verification-aeo.md
  - concepts/geo-visibility-measurement.md
  - osint-wiki/sources/arxiv-metaresearcher-deep-research-2606.19893-2026-06-20.md
---

## Target

**hands-on** — operator audits whether AI engines cite plausible-but-wrong local business facts.

## Summary

MetaResearcher cites **Synthetic Web**: one high-plausibility misinformation article can collapse answer accuracy. Pair GEO **mention tracking** with **claim–source verification** on local queries.

## Body

### Step 1 — Baseline queries (10)

Use unbranded local prompts from @briefs/2026-06-19_k123-ranqo-geo-visibility-baseline-hands-on.md.

### Step 2 — Fact extraction

For each engine response that mentions a shop (yours or competitor), extract:

- Star rating claimed
- Price range claimed
- Hours / walk-in policy claimed
- "Best for …" attribute claimed

### Step 3 — Ground-truth check

Compare against live GBP / website / Yelp. Mark each claim:

- [ ] **Verified** — matches primary source
- [ ] **Unverifiable** — no source cited
- [ ] **Wrong** — contradicts primary source

### Step 4 — Misinformation sensitivity

Note if a **single** low-authority page (new blog, spam directory) appears to drive a wrong fact. This mirrors adversarial injection failure mode.

### Step 5 — Mitigation (operator-owned surfaces only)

- Ensure GBP + website + top directories agree on NAP, hours, services, price band
- Do not fabricate listicle placements — earn real ones per @concepts/citation-building.md

Re-audit in 30 days alongside Ranqo-style mention baseline.

## Sources

- @concepts/citation-verification-aeo.md
- @concepts/geo-visibility-measurement.md
- @osint-wiki/sources/arxiv-metaresearcher-deep-research-2606.19893-2026-06-20.md
