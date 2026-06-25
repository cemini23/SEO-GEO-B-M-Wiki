---
title: K129 hands-on — negative review aspect-theme audit
type: brief
target: hands-on
created: 2026-06-25
updated: 2026-06-25
sources:
  - sources/arxiv-han-2026-aspect-sentiment-peer-review-evolution-2606.24188-2026-06-25.md
  - concepts/reviews-reputation-management.md
  - concepts/review-response-templates.md
---

## Target

**hands-on** — operator tags **which themes** drive negative Google/Yelp reviews (not just star count).

## Summary

Han 2026 (arXiv 2606.24188) studies **academic** peer-review rounds — domain mismatch. Steal: fine-grained **aspect + sentiment** beats coarse star monitoring for spotting fixable service failures.

## Body

### Step 1 — Sample last 30 reviews ≤3★ (per location)

Export from GBP + Yelp. Include **review text** only (stars alone insufficient).

### Step 2 — Aspect tag each review (pick one primary)

| Tag | Examples |
|-----|----------|
| **wait_time** | long wait, walk-in chaos, appointment delays |
| **skill_quality** | bad fade, uneven line, rushed cut |
| **price_value** | overpriced, hidden fees, tip pressure |
| **staff_attitude** | rude, dismissive, rushed |
| **cleanliness** | dirty chairs, messy floor |
| **booking_tech** | can't book online, wrong hours online |
| **other** | parking, kids policy, etc. |

### Step 3 — Count theme frequency

| Theme | Count | % of negatives |
|-------|-------|----------------|
| | | |

Top 2 themes = **operational fixes** before marketing spend.

### Step 4 — Match response template

Use @concepts/review-response-templates.md category rules — response should acknowledge the **specific aspect** named (not generic "sorry for your experience").

### Step 5 — Re-audit monthly

Track whether top theme count drops after operational change. Unlike Han's multi-round academic loop, GBP negatives are **public and persistent** — unresolved themes compound in AI sentiment summaries `[NEEDS VERIFICATION 2026-06-25]`.

## Sources

- @sources/arxiv-han-2026-aspect-sentiment-peer-review-evolution-2606.24188-2026-06-25.md
- @concepts/reviews-reputation-management.md
- @concepts/review-response-templates.md
