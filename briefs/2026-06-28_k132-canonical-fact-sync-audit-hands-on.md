---
title: K132 hands-on — canonical fact sync audit (GBP ↔ site ↔ schema)
type: brief
target: hands-on
created: 2026-06-28
updated: 2026-06-28
sources:
  - concepts/canonical-business-facts-geo.md
  - sources/arxiv-crespin-2026-karla-knowledge-base-augmented-retrieval-2606.26807-2026-06-28.md
  - concepts/google-business-profile.md
  - concepts/schema-markup-local.md
  - concepts/citation-verification-aeo.md
---

## Target

**hands-on** — verify the shop's **canonical fact KB** is consistent before GEO copy work.

## Summary

KARLA 2026: facts should live in an updatable KB, not model memory. Operator KB = GBP + website + schema + directory NAP. Contradictions let AI revert to wrong parametric facts.

## Body

### Step 1 — Fact checklist (one row per fact)

| Fact | GBP value | Website value | JSON-LD value | Top directory (Yelp) |
|------|-----------|---------------|---------------|----------------------|
| Business name | | | | |
| Address | | | | |
| Phone | | | | |
| Hours (Mon–Sun) | | | | |
| Primary category | | | | |
| Top 5 services + prices | | | | |
| Booking URL | | | | |

### Step 2 — Mark mismatches

Any cell ≠ canonical → **P0 fix** (same session: GBP → site → directories).

### Step 3 — AI spot-check (3 prompts)

Ask ChatGPT / Gemini / Perplexity:

- "What are the hours for [shop name] in [city]?"
- "What services does [shop name] offer?"
- "How much is a fade at [shop name]?"

Record answer vs checklist. Wrong fact → trace which surface AI likely read (@briefs/2026-06-26_k130-earned-media-citation-audit-hands-on.md).

### Step 4 — Counterfactual test (optional)

After fixing a fact (e.g. summer hours), re-run prompts **24h / 7d / 30d**. Stale answers = parametric/RAG failure — keep KB surfaces aligned; expect tail latency `[NEEDS VERIFICATION 2026-06-28]`.

### Step 5 — Cadence

- **Trigger-based:** any NAP/hours/price change → full sync same day
- **Quarterly:** full checklist even if no changes

## Sources

- @concepts/canonical-business-facts-geo.md
- @sources/arxiv-crespin-2026-karla-knowledge-base-augmented-retrieval-2606.26807-2026-06-28.md
- @concepts/citation-verification-aeo.md
