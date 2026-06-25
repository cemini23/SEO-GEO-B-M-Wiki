---
title: K127 hands-on — PEBM verified-mention audit (local service)
type: brief
target: hands-on
created: 2026-06-23
updated: 2026-06-23
sources:
  - wiki/concepts/per-entity-bias-mapping-geo.md
  - wiki/sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md
  - wiki/concepts/citation-verification-aeo.md
---

## Target

**hands-on** — operator separates **raw mention rate** from **verified mention rate** for a local barbershop.

## Summary

Varga 2026 PEBM: equal mention rates can mean opposite strategic outcomes. High-salience brands face the **Brand Hallucination Paradox** (more fabricated citations). Audit verified mentions, not celebration at raw mention alone.

## Body

### Step 1 — Tier + failure-mode guess

| Signal | Likely PEBM profile |
|--------|---------------------|
| Unknown local shop | Invisibility — low mention, low fabrication |
| Established city brand | Hallucination paradox risk — check citation fidelity |
| Recent rebrand / new hours | Parametric–retrieval lag — compare engines |

### Step 2 — Query set (15 branded + 15 unbranded)

Reuse pools from @briefs/2026-06-19_k123-ranqo-geo-visibility-baseline-hands-on.md.

### Step 3 — Per-response scorecard

For each mention-bearing answer:

| Field | Record |
|-------|--------|
| Engine | |
| Query type | branded / category / comparison |
| Mentioned? | Y/N |
| Claims extracted | hours, price, services, rating |
| Verified? | Y / N / partial |
| Cited URL opens? | Y/N |
| Citation supports claim? | Y/N |
| Fabricated capability? | Y/N (service you don't offer) |

Compute **verified mention rate** = verified / all mentions (not / all queries).

### Step 4 — Compare to raw mention rate

If raw mention **↑** but verified mention **flat or ↓**, you have reputational exposure — not a win.

### Step 5 — Remediation (pick one)

1. **Invisibility** — canonical presence: schema.org, directory co-citations, listicle earning
2. **Fabrication** — tighten NAP consistency; dispute wrong third-party pages; add FAQ with authoritative facts above fold
3. **Lag** — post GBP + website update; re-audit at t+14 and t+90 days across engines

Re-audit in 30 days.

## Sources

- @concepts/per-entity-bias-mapping-geo.md
- @sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md
- @concepts/citation-verification-aeo.md
- @concepts/geo-visibility-measurement.md
