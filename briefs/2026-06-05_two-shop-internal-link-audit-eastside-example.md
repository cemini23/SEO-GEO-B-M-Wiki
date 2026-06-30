---
title: Two-shop internal link audit — Eastside Barbers Co. (worked example)
type: brief
tags: [brief, hands-on, internal-linking, example, barbershop]
keywords: [eastside-barbers, austin, worked-example, internal-links]
related:
  - briefs/2026-06-05_two-shop-internal-link-audit.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/on-page-seo-local.md
  - entities/companies/shop-1.md
  - entities/companies/shop-2.md
maturity: draft
created: 2026-06-05
updated: 2026-06-06
processed: 2026-06-06
status: hands-on-example; linked-from-wiki
---

## Target

**hands-on** — run this audit on the fictional site below to learn the workflow, then copy `briefs/2026-06-05_two-shop-internal-link-audit.md` and replace every Eastside value with operator data from Session 1 (`@entities/companies/shop-1.md`, `shop-2.md`).

> **Not a live site.** `eastsidebarbers.com` is a worked example. Wiki operator entities are still placeholders — paste real URLs when available.

## Summary

Pre-filled audit for **Eastside Barbers Co.** — 2 locations in Austin, TX, shared WordPress site, Pattern B services page + 3 breakout service pages. Simulates a common pre-audit state: strong nav/footer links, weak in-content links, one orphan service page, no East↔West cross-link in body copy.

**Blank template:** `briefs/2026-06-05_two-shop-internal-link-audit.md`

## Body

---

### 0. Site facts

| Field | East shop | West shop |
|-------|-----------|-----------|
| **Brand** | Eastside Barbers Co. | (same brand) |
| **City, ST** | Austin, TX | Austin, TX |
| **Street** | 1847 E 6th St, Austin, TX 78702 | 4201 Westlake Dr, Austin, TX 78746 |
| **Phone** | (512) 555-0142 | (512) 555-0198 |
| **Location page URL** | https://eastsidebarbers.com/locations/austin-east/ | https://eastsidebarbers.com/locations/austin-west/ |
| **GBP listing URL** | https://maps.google.com/?cid=EXAMPLE_EAST_CID | https://maps.google.com/?cid=EXAMPLE_WEST_CID |
| **Booking deep link** | https://booksy.com/en-us/eastside-barbers-east | https://booksy.com/en-us/eastside-barbers-westlake |
| **Primary services to rank** | 1. Skin fade 2. Beard trim 3. Kids cut | 1. Skin fade 2. Hot towel shave 3. Mens haircut |

**Site map (18 indexable URLs):**

```
[x] https://eastsidebarbers.com/
[x] https://eastsidebarbers.com/locations/austin-east/
[x] https://eastsidebarbers.com/locations/austin-west/
[x] https://eastsidebarbers.com/services/
[x] https://eastsidebarbers.com/services/skin-fade/
[x] https://eastsidebarbers.com/services/beard-trim/
[x] https://eastsidebarbers.com/services/kids-cut/
[x] https://eastsidebarbers.com/services/hot-towel-shave/
[x] https://eastsidebarbers.com/about/
[x] https://eastsidebarbers.com/faq/
[x] https://eastsidebarbers.com/book/
[x] https://eastsidebarbers.com/contact/
[x] https://eastsidebarbers.com/blog/how-often-should-i-get-a-fade/
[x] https://eastsidebarbers.com/blog/beard-trim-vs-beard-shape/
[x] https://eastsidebarbers.com/blog/kids-first-haircut-tips/
[x] https://eastsidebarbers.com/privacy-policy/
[x] https://eastsidebarbers.com/terms/
[ ] /team/joey-rodriguez/  — not built yet (optional future)
```

---

### 1. Crawl inventory (Screaming Frog export — simulated)

| # | URL | Page type | Inlinks | Outlinks | Orphan? |
|---|-----|-----------|---------|----------|---------|
| 1 | `/` | Homepage | 18 | 12 | No |
| 2 | `/locations/austin-east/` | Location East | 8 | 6 | No |
| 3 | `/locations/austin-west/` | Location West | 7 | 5 | No |
| 4 | `/services/` | Services hub | 9 | 8 | No |
| 5 | `/services/skin-fade/` | Service | 4 | 3 | No |
| 6 | `/services/beard-trim/` | Service | 3 | 2 | No |
| 7 | `/services/kids-cut/` | Service | **1** | 2 | **Yes** |
| 8 | `/services/hot-towel-shave/` | Service | 2 | 2 | Borderline |
| 9 | `/about/` | About | 6 | 2 | No |
| 10 | `/faq/` | FAQ | 5 | 4 | No |
| 11 | `/book/` | Book | 7 | 2 | No |
| 12 | `/contact/` | Contact | 6 | 3 | No |
| 13 | `/blog/how-often-should-i-get-a-fade/` | Blog | 2 | 1 | No |
| 14 | `/blog/beard-trim-vs-beard-shape/` | Blog | 1 | 0 | **Yes** |
| 15 | `/blog/kids-first-haircut-tips/` | Blog | 1 | 0 | **Yes** |

**Orphans / weak (Low boost targets):**

1. `/services/kids-cut/` — only footer + sitemap inlinks
2. `/blog/beard-trim-vs-beard-shape/` — no outbound internal links at all
3. `/blog/kids-first-haircut-tips/` — no outbound internal links

**Hubs (donors):**

1. `/` — homepage
2. `/locations/austin-east/` — 4.8★ / 127 reviews
3. `/locations/austin-west/` — 4.7★ / 89 reviews
4. `/services/` — services hub

---

### 2. Current graph vs target

| Required link | Exists? | In-content? | Anchor OK? | Fix needed |
|---------------|---------|-------------|------------|------------|
| Homepage → Location East | Y | Y (hero card) | Y | — |
| Homepage → Location West | Y | Y (hero card) | Y | — |
| Homepage → top 3 services | Y | **N** (footer only) | fix | Add above-fold service cards |
| Location East ↔ Location West | **N** | — | — | **Add cross-link in body** |
| Location East → skin fade | Y | Y | Y | — |
| Location East → kids cut | **N** | — | — | **Add in Services H2** |
| Location East → beard trim | Y | footer | fix | Move to body copy |
| Location West → hot towel shave | Y | Y | Y | — |
| Location West → skin fade | Y | N | fix | Add in body |
| Service skin fade → both locations | Y | Y | Y | — |
| Service kids cut → both locations | **N** | — | — | **Add location CTAs** |
| FAQ → service + location | partial | N | fix | 3 answers lack links |

**Anchor flags:**

| From | To | Current anchor | Verdict |
|------|-----|----------------|---------|
| `/blog/how-often...` | `/services/skin-fade/` | "click here" | **fix** → "how often to refresh your skin fade" |
| `/locations/austin-east/` | `/book/` | "Book now" | OK (branded CTA) |
| Footer sitewide | `/services/kids-cut/` | "Kids Cuts Austin TX Barbershop Kids Haircut" | **fix** — keyword-stuffed; use "Kids' haircuts" |

---

### 3. Candidate link batch (12 links — deploy as one batch)

| ID | FROM | TO | Proposed anchor | Strategy | Placement |
|----|------|-----|-----------------|----------|-----------|
| L1 | `/locations/austin-east/` | `/locations/austin-west/` | "our Westlake shop on Westlake Drive" | Folder | New H2 "Our other Austin location" |
| L2 | `/locations/austin-west/` | `/locations/austin-east/` | "East 6th Street location near downtown" | Folder | Same pattern |
| L3 | `/` | `/services/skin-fade/` | "skin fade specialists" | Folder | Homepage services strip (above fold) |
| L4 | `/` | `/services/beard-trim/` | "beard trims and line-ups" | Folder | Homepage services strip |
| L5 | `/` | `/services/kids-cut/` | "kids' cuts" | **Low** | Homepage services strip |
| L6 | `/locations/austin-east/` | `/services/kids-cut/` | "kids' haircuts on East 6th" | **Low** | Under Services & Pricing H2 |
| L7 | `/services/kids-cut/` | `/locations/austin-east/` | "East 6th barbershop" | **Low** | Bottom CTA block |
| L8 | `/services/kids-cut/` | `/locations/austin-west/` | "Westlake location" | **Low** | Bottom CTA block |
| L9 | `/locations/austin-west/` | `/services/skin-fade/` | "skin fades" | Folder | Services H2 body |
| L10 | `/faq/` | `/services/kids-cut/` | "kids' haircut pricing and what to expect" | **Low** | FAQ: "Do you cut children's hair?" |
| L11 | `/blog/kids-first-haircut-tips/` | `/services/kids-cut/` | "kids' cut services and pricing" | **Low** | Conclusion paragraph |
| L12 | `/blog/kids-first-haircut-tips/` | `/locations/austin-east/` | "visit us on East 6th" | Folder | Conclusion paragraph |

**Deferred (batch 2 — after GSC follow-up):**

- L13 `/blog/beard-trim-vs-beard-shape/` → `/services/beard-trim/` + `/locations/austin-west/` (rewrite post first — currently zero outlinks)
- Fix blog "click here" anchor on fade frequency post

---

### 4. Four-metric pre-deploy score

| Metric | Score | Notes |
|--------|-------|-------|
| **Authority yield** | **5** | Batch targets clear orphan (`kids-cut`) + 3 zero-outlink blog posts get first outbound paths |
| **Down/up balance** | **4** | Homepage donates 3 links but to distinct services; no single page receives >2 new links except kids-cut (3) — acceptable for orphan recovery |
| **Semantic coherence** | **5** | Every link is location↔location, service↔location, FAQ↔service, or blog↔service — no off-topic bridges |
| **Stability** | **5** | Kids cuts and cross-location links are permanent offerings |

**Batch verdict:** ✅ **Deploy** (all metrics ≥3)

---

### 5. Expert / UX pass

| Check | Pass? |
|-------|-------|
| Links read naturally in paragraph copy | Y |
| Mobile: tappable, no layout break | Y (verify in Elementor mobile preview) |
| User path makes sense | Y |
| No duplicate same-page → same-target | Y |
| Booking CTAs still one-tap | Y — Book nav unchanged |

---

### 6. Deploy checklist

| Step | Done | Date |
|------|------|------|
| Publish batch in WordPress (Elementor text widgets) | [ ] | |
| SF re-crawl — confirm 12 new internal links | [ ] | |
| GSC → URL Inspection → Request indexing (location + kids-cut + FAQ) | [ ] | |
| Screenshot GSC Links tab for `/services/kids-cut/` | [ ] | |

**Changed URLs:**

1. https://eastsidebarbers.com/
2. https://eastsidebarbers.com/locations/austin-east/
3. https://eastsidebarbers.com/locations/austin-west/
4. https://eastsidebarbers.com/services/kids-cut/
5. https://eastsidebarbers.com/faq/
6. https://eastsidebarbers.com/blog/kids-first-haircut-tips/

---

### 7. Follow-up (schedule: 2026-08-01)

| Target URL | Inlinks @ audit | Inlinks @ follow-up | Impressions Δ | Clicks Δ | Notes |
|------------|-----------------|---------------------|---------------|----------|-------|
| `/services/kids-cut/` | 1 | | | | Primary KPI |
| `/locations/austin-east/` | 8 | | | | Cross-link to West |
| `/blog/kids-first-haircut-tips/` | 1 | | | | |

---

### Swap-in sheet (paste operator real values)

When Session 1 data lands in `@entities/companies/shop-1.md` / `shop-2.md`, replace:

| Example value | Operator field |
|---------------|----------------|
| `eastsidebarbers.com` | Website URL (root domain) |
| `/locations/austin-east/` | Shop 1 location page path |
| `/locations/austin-west/` | Shop 2 location page path |
| Booksy deep links | Actual booking URLs per shop |
| GBP CIDs | Real Maps URLs from `.env` |
| Service slugs | Match live site (may be Pattern B only — drop breakout rows if `/services/fade/` doesn't exist) |

---

## Sources

- `briefs/2026-06-05_two-shop-internal-link-audit.md` — blank template
- `@concepts/on-page-seo-local.md` — URL patterns, hub-and-spoke graph
- `@concepts/adaptive-rag-internal-linking-geo.md` — four-metric frame
- `@entities/companies/shop-1.md`, `@entities/companies/shop-2.md` — populate to replace this example
