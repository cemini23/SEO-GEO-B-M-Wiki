---
title: Two-shop barbershop — internal link audit (hands-on)
type: brief
tags: [brief, hands-on, internal-linking, local-seo, barbershop]
keywords: [internal-links, two-location, hub-and-spoke, webknograph, gsc]
related:
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/on-page-seo-local.md
  - sources/arxiv-webknograph-internal-linking-2606.06106-2026-06-05.md
maturity: draft
created: 2026-06-05
updated: 2026-06-06
processed: 2026-06-06
status: linked-from-wiki; hands-on-deliverable
---

## Target

**hands-on** — print or duplicate this brief; fill during a site crawl session. Paste completed link batches into CMS or hand to developer. Re-check in GSC after 4–8 weeks.

## Summary

Manual internal-link audit for a **2-location barbershop** (~15–40 pages). Uses the WebKnoGraph four-metric frame adapted for small sites: score **candidate link batches** before deploy, not one link at a time. Baseline hub-and-spoke rules from `@concepts/on-page-seo-local.md`; scoring frame from `@concepts/adaptive-rag-internal-linking-geo.md` Part B.

**Time budget:** 90–120 min first pass; 30 min for quarterly re-audit.

**Worked example (fictional):** `briefs/2026-06-05_two-shop-internal-link-audit-eastside-example.md` — Eastside Barbers Co., Austin TX, 12-link batch pre-scored and ready to walk through. Replace with operator data after Session 1.

**Tools (pick what you have):**

| Tool | Free? | Use for |
|------|-------|---------|
| Google Search Console → Links | Yes | Inbound/outbound internal links per URL |
| Screaming Frog (≤500 URLs free) | Yes | Full crawl, orphan pages, inlink counts |
| Sitebulb / Ahrefs / Semrush | Paid | Same + competitor teardown |
| Spreadsheet | Yes | Link batch scoring table below |

## Body

---

### 0. Site facts (fill once)

| Field | East shop | West shop |
|-------|-----------|-----------|
| **Brand** | | |
| **City, ST** | | |
| **Location page URL** | | |
| **GBP listing URL** | | |
| **Booking deep link** | | |
| **Primary services to rank** (top 3) | 1. 2. 3. | 1. 2. 3. |

**Site map target** (check when done):

```
[ ] Homepage
[ ] /locations/[city]-east/     (or equivalent)
[ ] /locations/[city]-west/
[ ] /services/                  (Pattern B) OR /services/fade/ etc. (Pattern A)
[ ] /about/
[ ] /faq/
[ ] /book/ or /contact/
[ ] Blog/posts (if any)
```

---

### 1. Crawl + inventory (20 min)

**Run crawl** (Screaming Frog or GSC export). List every indexable URL:

| # | URL | Page type | Inlinks (count) | Outlinks (count) | Orphan? (≤1 inlink) |
|---|-----|-----------|-----------------|------------------|---------------------|
| 1 | | Homepage | | | |
| 2 | | Location East | | | |
| 3 | | Location West | | | |
| 4 | | Services | | | |
| 5 | | FAQ | | | |
| 6 | | About | | | |
| 7 | | Book/Contact | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |

**Orphans / weak pages** (candidates for **Low** boost — new links *to* these pages):

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

**Hubs** (strong pages that should *donate* links — homepage + location pages):

1. _______________________________________________
2. _______________________________________________

---

### 2. Current graph vs target (15 min)

Compare live site to target graph (`@concepts/on-page-seo-local.md`):

| Required link | Exists? | In-content (not footer-only)? | Anchor text OK? | Fix needed |
|---------------|---------|-------------------------------|-----------------|------------|
| Homepage → Location East | Y / N | Y / N | | |
| Homepage → Location West | Y / N | Y / N | | |
| Homepage → top 3 services | Y / N | Y / N | | |
| Location East ↔ Location West | Y / N | Y / N | | |
| Location East → each priority service | Y / N | Y / N | | |
| Location West → each priority service | Y / N | Y / N | | |
| Service pages → both locations | Y / N | Y / N | | |
| FAQ → relevant service + location | Y / N | Y / N | | |
| Blog posts → service + location | Y / N / N/A | Y / N | | |

**Anchor text spot-check** — flag manipulative or generic anchors:

| From URL | To URL | Current anchor | Verdict (OK / fix / remove) |
|----------|--------|----------------|----------------------------|
| | | | |
| | | | |

Rules: descriptive anchors; mix branded + generic; no all exact-match `[city] fade barber` on every link.

---

### 3. Candidate link batch (draft 8–15 links max)

Draft **one batch** to deploy together. Small sites: treat ~8–15 new/edited in-content links as one intervention set (WebKnoGraph uses ~240 on 1,841 pages — scale down).

| ID | Donor page (FROM) | Target page (TO) | Proposed anchor | Strategy | In-content placement |
|----|-------------------|------------------|-----------------|----------|----------------------|
| L1 | | | | Low / Folder / High | e.g. "Services" H2 |
| L2 | | | | | |
| L3 | | | | | |
| L4 | | | | | |
| L5 | | | | | |
| L6 | | | | | |
| L7 | | | | | |
| L8 | | | | | |

**Strategy key:**

| Strategy | When to use on 2-shop site |
|----------|----------------------------|
| **Low** | Target page is orphan or weak (new service page, thin FAQ section) |
| **Folder** | Connect location ↔ service ↔ FAQ at same hierarchy level |
| **High** | Reinforce already-strong location or homepage (use sparingly) |

---

### 4. Four-metric pre-deploy score (batch level)

Score the **whole batch** before publishing. Use 1–5 (1 = bad, 5 = good). Any metric ≤2 → revise batch before deploy.

| Metric | Question | Score (1–5) | Notes / revision |
|--------|----------|-------------|------------------|
| **Authority yield** | Will orphan/weak targets (Low candidates) gain meaningful inlinks from this batch? | | |
| **Down/up balance** | Are we adding many links *to one* page while ignoring others, or draining hubs? | | |
| **Semantic coherence** | Are donor and target topically related (same service, location, or FAQ topic)? | | |
| **Stability** | Will these links still make sense in 6 months (not promo-only)? | | |

**Batch verdict:**

- [ ] **Deploy** — all metrics ≥3
- [ ] **Revise** — any metric ≤2; edit table in §3 and re-score
- [ ] **Reject** — coherence ≤2 (off-topic links); redesign batch

**Common 2-shop failures to reject:**

- Blog history post → exact-match "fade haircut [city]" on unrelated topic
- 5+ new links all targeting one service page from random pages
- Footer-only links when in-content links are missing (footer helps crawl less)

---

### 5. Expert / UX pass (10 min)

Before CMS paste — WebKnoGraph expert-assisted regime analog:

| Check | Pass? |
|-------|-------|
| Links read naturally in paragraph copy (not link dumps) | Y / N |
| Mobile: link tappable, doesn't break layout | Y / N |
| User path makes sense (location → book, service → location) | Y / N |
| No duplicate links on same page to same target (one primary anchor enough) | Y / N |
| Booking CTAs still one-tap on mobile | Y / N |

---

### 6. Deploy checklist

| Step | Done | Date |
|------|------|------|
| Publish link batch in CMS | [ ] | |
| Verify live HTML (View Source or SF re-crawl) | [ ] | |
| Request indexing in GSC for changed URLs (optional) | [ ] | |
| Screenshot "before" link counts for donor/target URLs | [ ] | |

**Changed URLs log:**

1. _______________________________________________
2. _______________________________________________

---

### 7. Follow-up (4–8 weeks)

GSC → **Links** → Internal links. Compare to §1 baseline.

| Target URL | Inlinks at audit | Inlinks at follow-up | Impressions Δ (GSC) | Clicks Δ | Notes |
|------------|------------------|----------------------|---------------------|----------|-------|
| | | | | | |
| | | | | | |

**Decision:**

- [ ] Batch worked — queue next batch (remaining orphans)
- [ ] Mixed — keep links, adjust anchors on low-CTR pages
- [ ] No signal — check indexing/CWV first before adding more links
- [ ] Roll back specific links that fail coherence review

---

### Quick reference — priority link wins for 2-shop barbershops

Usually highest ROI (do these first if graph is broken):

1. Homepage → both location pages (**in-content**, not nav-only)
2. Each location page → its booking deep link + top 3 services
3. Location East ↔ West cross-link with distance/neighborhood context
4. Service/fade page → both locations ("visit our East/West shop")
5. FAQ answers → specific service + location pages (GEO extractable Q&A)

---

## Sources

- `@concepts/on-page-seo-local.md` — hub-and-spoke graph, anchor rules, Pattern A/B services
- `@concepts/adaptive-rag-internal-linking-geo.md` — Part B four-metric checklist, strategy selection
- `@sources/arxiv-webknograph-internal-linking-2606.06106-2026-06-05.md` — WebKnoGraph pre-deploy evaluation frame `[TENTATIVE]` at small-site scale
- `@concepts/generative-engine-optimization.md` — semantic coherence as AEO signal
