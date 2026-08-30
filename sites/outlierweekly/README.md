# Outlier Weekly — owned hub (Cloudflare Worker + static assets)

This directory is a deployable Cloudflare Workers project. It serves the owned
HTML hub for Outlier Weekly on `outlierweekly.com`. The letters themselves stay
canonical on Substack (`outlierweekly.substack.com`).

The Worker name is **locked** to `outlierweekly-redirect`. The zone routes
`outlierweekly.com/*` and `www.outlierweekly.com/*` already point at it. Do not
rename it, or the routes break.

## What the worker does

- `www.outlierweekly.com` → 301 → `outlierweekly.com` (same path/query).
- `/p/*`, `/subscribe`, `/feed`, `/archive` → 301 → `outlierweekly.substack.com`
  (same path/query). Letters stay on Substack.
- `/prediction-market-lp-bot` and `/agent-harness` (with or without slash) →
  301 → `https://outlierweekly.com/` (retired 2026-08-30).
- `/cxw-geo` (with or without slash) → 301 →
  `https://outlierweekly.com/spcx-anthropic/` (the Short letter is SPCX /
  Anthropic, not the detention thread).
- Everything else → served from `public/` (Workers static assets). Unknown
  paths 404 via `public/404.html`.

The apex is a 200 hub. It does **not** blanket-301 to Substack — that was the
2026-08-08 SEO defect this project replaces.

## Layout

```
wrangler.toml            worker name lock + assets config
src/index.js             worker-first router (<80 lines, no KV, no secrets)
public/                  owned 200 surfaces (hubs, crawl files, IndexNow key)
scripts/deploy.sh        wrangler deploy + IndexNow ping (warn on ping failure)
scripts/indexnow-ping.sh POST owned sitemap URLs to api.indexnow.org
```

## Deploy (parent runs this, after review)

```bash
cd sites/outlierweekly
bash scripts/deploy.sh
```

`scripts/deploy.sh` runs `npx wrangler@4 deploy` (same worker name keeps
existing routes) and then `bash scripts/indexnow-ping.sh` in a child
shell. If the IndexNow ping fails, the script prints a warning and
continues — a ping failure must never fail a successful deploy.

Prereqs: Node/`npx` with Wrangler 4, logged in with access to the
`outlierweekly.com` zone. No secrets, no `.env`, no KV bindings in this
project. `workers_dev` is off so deploy does not publish a second copy
on `*.workers.dev`.

## What NOT to do

- **Do not attach `outlierweekly.com` as a Substack custom domain.** That
  path costs the $50/year CNAME fee and is deferred this quarter. The owned
  hub works without it.
- **Do not blanket-301 the apex or the crawl files to Substack.** That is the
  defect this project replaces.
- **Do not IndexNow-ping `*.substack.com` URLs.** The IndexNow key lives on
  `outlierweekly.com` only; the sitemap lists owned URLs only.
- **Do not reprint letter bodies.** Duplicate content + copyright. Hub pages
  synthesize and link.
- **Do not invent subscriber counts, open rates, or GSC numbers.**
- **Do not add fake schema** (no `aggregateRating`, no fake LocalBusiness,
  no invented HowTo). JSON-LD lives on the home page only (`Organization` +
  `WebSite`).
- **Do not change the worker name** away from `outlierweekly-redirect`.

## Verification metas

Every HTML page carries the public DNS verification metas:

- `google-site-verification=K40mjJ6Ih6QvEsyuPF-PcEN2CWAHxXBLck7MZ97-0O4`
- `msvalidate.01=1205BD6E2D6995953FDD6BB83FEC4FAD`

No GTM is present and none should be added.
