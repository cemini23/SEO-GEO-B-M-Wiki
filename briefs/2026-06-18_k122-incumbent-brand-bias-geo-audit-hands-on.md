---
title: K122 hands-on — incumbent brand bias GEO audit (local service)
type: brief
target: hands-on
created: 2026-06-18
updated: 2026-06-18
sources:
  - wiki/sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md
  - wiki/concepts/llm-brand-bias-geo-competition.md
  - wiki/concepts/llm-reputation-signals-geo.md
---

## Target

**hands-on** — operator runs assistant recommendation audits in Claude / ChatGPT / Gemini when shop + competitor data are filled.

## Summary

Replicate Chu 2026 **Conditional Monopoly** and **minimal-quality-threshold** tests for a local barbershop (or dental/salon) query. Goal: learn whether assistants default to the famous local brand when cards tie, and whether a small rating/review/price edge flips the pick.

**Do not** use fabricated clinical or award claims from the paper's GEO templates — audit with **real** GBP/website facts only.

## Body

### Prerequisites

- Operator shop NAP + GBP rating/review count + service prices documented
- 2–4 real local competitors with same fields (manual scrape from GBP/maps)
- 3 engines: ChatGPT, Claude (web), Gemini

### Test A — Identical-spec tie (IAI)

**Prompt template** (adapt city + category):

```
I'm looking for a [fade haircut / men's grooming] shop in [CITY, ST].

Here are 4 options — same rating, review count, and price range:

A. [Competitor 1 name] — 4.6★, 120 reviews, fades from $35
B. [Operator shop] — 4.6★, 120 reviews, fades from $35
C. [Competitor 2 name] — 4.6★, 120 reviews, fades from $35
D. [Market leader / chain name] — 4.6★, 120 reviews, fades from $35

Recommend ONE shop and one sentence why.
RECOMMEND: [letter]
```

Run **3 personas** × **3 days** × **3 engines** (27 cells minimum). Log which letter wins.

**Interpret:** If market leader wins >80% when specs match → Conditional Monopoly present `[TENTATIVE]`. If picks spread evenly → tie-breaker weak on your queries.

### Test B — Minimal edge (+0.1★ or +15 reviews)

Same prompt; give **operator shop** 4.7★ (others 4.6★) OR operator 150 reviews (others 120). Hold everything else identical.

**Interpret:** Chu L1 threshold ≈ +0.075★. If operator flip rate jumps from <10% to >50% → quality edge breaks brand default.

### Test C — Verifiable differentiation (not fabricated authority)

Replace matched specs with **unique true facts** per shop (specialty service, years open, licensed barber name, neighborhood). Re-run Test A.

**Interpret:** If differentiation removes market-leader lock-in → invest in factual GBP/website depth, not boilerplate GEO copy.

### Log sheet

| Date | Engine | Test | Winner | Notes |
|------|--------|------|--------|-------|
| | | A/B/C | | |

File results back to @concepts/llm-brand-bias-geo-competition.md via wiki update when n≥9.

## Sources

- @sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md
- @concepts/llm-brand-bias-geo-competition.md
- @concepts/llm-reputation-signals-geo.md — pair with Baig reputation AMCE checklist
- @concepts/geo-visibility-measurement.md — sample-size / repeat-run discipline
