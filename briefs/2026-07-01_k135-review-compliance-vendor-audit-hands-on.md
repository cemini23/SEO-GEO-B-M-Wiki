---
title: K135 hands-on — review compliance + vendor audit
type: brief
target: hands-on
created: 2026-07-01
updated: 2026-07-01
sources:
  - sources/salon-today-2026-review-gating-ftc-compliance-dodson-2026-06-24.md
  - concepts/reviews-reputation-management.md
  - entities/tools/easy-review.md
---

## Target

**hands-on** — verify the shop's review **acquisition flow** and any **reputation SaaS** does not gate, incentivize, or kiosk-pressure reviews.

## Summary

Salon Today 2026-06-24: gating tools are **actively enforced** (Google + FTC Consumer Review Rule framing). Three vendor questions expose most violations before Google finds them.

## Body

### Step 1 — Map current flow (per location)

Document every touchpoint that asks for reviews:

| Touchpoint | Channel | Who gets it? | Notes |
|------------|---------|--------------|-------|
| In-person ask | verbal | all / some? | |
| SMS/email tool | Birdeye, Square, etc. | all / filtered? | |
| QR / kiosk | front desk | all / shared tablet? | |
| Easy Review | draft-only | N/A for acquisition | reply tool only |

### Step 2 — Dodson three-question vendor audit

Answer **yes/no** for each active tool:

1. Does the tool send review requests **only** after a positive pre-screen ("How was your visit?" → 4–5★ → Google link)?
2. Is any **discount, reward, or incentive** tied to leaving a review?
3. Does the request go out from a **shared kiosk/tablet** on premises?

**Any yes = fix before next billing cycle.** See @concepts/reviews-reputation-management.md hard boundaries.

### Step 3 — Compliant pattern check

- [ ] **Every** completed service gets the same review invitation (no sentiment filter).
- [ ] Optional NPS/satisfaction survey is **separate** — detractors get human follow-up, not silent suppression.
- [ ] No staff quotas for review count or mandated mention of staff names in review text.
- [ ] Easy Review used for **response drafting only** — never auto-post, never gate sends.

### Step 4 — GBP warning signs

Check each GBP listing weekly:

| Signal | Action |
|--------|--------|
| Reviews disappearing after posting | audit flow for gating |
| "Reviews paused" notice | stop all automated asks; contact Google support |
| Public policy warning banner | emergency — fix process + dispute if erroneous |
| Sudden rating jump without volume change | investigate incentivized burst |

### Step 5 — Document + calendar

Log audit date + pass/fail per location. Re-run **quarterly** or when switching review/SMS vendors.

## Sources

- @sources/salon-today-2026-review-gating-ftc-compliance-dodson-2026-06-24.md
- @concepts/reviews-reputation-management.md
- @entities/tools/easy-review.md
