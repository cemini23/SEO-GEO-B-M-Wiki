---
title: Outlier Weekly — Google / Bing / Brave search discovery setup
type: brief
target: hands-on (Substack Settings + GSC/Bing verify)
created: 2026-08-08
updated: 2026-08-08
status: IN PROGRESS — domain registered + GSC verified; Substack custom-domain DNS + Bing verify remaining
---

## Target

hands-on — Cloudflare domain + Substack custom domain + Google Search Console + Bing Webmaster + Brave submit-url

## Summary

Registered **`outlierweekly.com`** on Cloudflare Registrar (2026-08-08, $10.46/yr, auto-renew). GSC domain property **`sc-domain:outlierweekly.com` verified** via DNS TXT. Hosted Substack GTM path alone could not verify (noscript-only inject). Remaining: wire Substack custom domain CNAME, finish Bing verify, resubmit feeds on the new host.

## Body

### Live surface (probed 2026-08-08)

| Check | Result |
|-------|--------|
| Home | 200 `https://outlierweekly.substack.com/` |
| robots.txt | Allows crawl of posts; blocks `/subscribe`, embeds, etc. |
| sitemap.xml | **404** — Substack: "This publication does not have a sitemap." |
| RSS | 200 `https://outlierweekly.substack.com/feed` (11 posts) |
| google-site-verification meta | **missing** (until paste below) |
| Custom domain | none (`outlierweekly.com` does not resolve for this pub) |
| Bing API sites | youratto, guruwatcher, GH Pages only — **Outlier Substack not added** |
| GSC SA | domain props for youratto + guruwatcher only |

### Google Search Console (DONE in Cursor / pending verify)

1. Property type: **URL prefix** `https://outlierweekly.substack.com/`
2. Status: property created; ownership **not yet verified**
3. Substack Analytics has **no Google Site Verification field** (only GA4 / GTM / pixels / Facebook verify). Use GTM:

| Field | Value |
|-------|--------|
| Google Tag Manager ID | `GTM-5FTL4LBX` |

Created 2026-08-08 in Tag Manager: account **Outlier Weekly**, container **outlierweekly.substack.com** (Web).

HTML-tag token (unused — no Substack field for it): `ClmXJrV5rUQoRRltwz7LQoxpL_4R1DEfEAIswn6AbNg`

4. After pasting GTM ID + Save: GSC → verify via **Google Tag Manager** method (Publish permission on this container).
5. After paste: GSC → Verify → **Sitemaps** submit `feed` (RSS workaround because `/sitemap.xml` 404s). If Substack later enables sitemap, also submit `sitemap.xml`.
6. URL Inspection → Request indexing for home + latest 3–5 posts.

HTML file method (`google7291006905236f9d.html`) **cannot** be used on Substack hosting — ignore it.

### Bing Webmaster Tools (blocked until GSC verify or meta)

Preferred after GSC verifies: Bing → **Import from Google Search Console** → pick `https://outlierweekly.substack.com/`.

Alternative: add site manually + Bing meta (`msvalidate.01`) if Substack exposes a Bing/verification field (many pubs do not).

Then: submit feed/sitemap + URL Submission for home + key posts. Bing API key on this machine already covers youratto/guruwatcher; Outlier must be added first.

### Brave Search (DONE 2026-08-08)

Form: https://search.brave.com/submit-url (same as Atto/GuruWatcher). No Search Console / no sitemap intake.

All key URLs returned **Success** (home, about, archive, feed, and every RSS post). Expect `site:outlierweekly.substack.com` empty for a while — form is a re-fetch queue, not instant indexing.

### Operator checklist

- [ ] Substack Settings → Analytics: paste Google Site Verification token (or GTM)
- [ ] Confirm meta live on homepage HTML
- [ ] GSC → Verify
- [ ] GSC → Sitemaps → submit `feed`
- [ ] GSC → Request indexing (home + recent posts)
- [ ] Bing → Import from GSC (or manual verify)
- [ ] Bing → submit feed + key URLs
- [x] Brave → submit-url for home/about/archive/feed + all RSS posts
- [ ] Optional: ask Substack support / wait for native `/sitemap.xml` once eligible

## Sources

- Live probes of outlierweekly.substack.com (robots, sitemap 404, feed)
- GSC welcome flow (URL-prefix property + HTML tag copy)
- Prior Atto/GuruWatcher Brave submit-url pattern
