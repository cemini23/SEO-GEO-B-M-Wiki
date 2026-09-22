# Outlier Weekly — operator leftovers (2026-08-30)

Hands-on items for the human operator. None of these are agent actions; the
agent does not touch Substack settings, GSC, Bing, Brave, or Cloudflare
dashboard toggles.

## GSC digest follow-up — first pull (2026-09-03)

Filed from the 2026-09-02 GSC digest (read-only Performance export, account
`cjbarone23@gmail.com`). Property `sc-domain:outlierweekly.com`. The digest bot
made no sitemap, robots, verification, or indexing-request changes. Facts below
are exact from the digest; no extra GSC numbers are inferred.

- Windows: last 7 days **2026-08-25 – 2026-08-31**; last 28 days
  **2026-08-04 – 2026-08-31**. Prior digest: none (first pull).
- 7 days: **0 clicks / 0 impressions**, CTR 0%, avg position 0. Queries: none.
  Pages: none.
- 28 days: **0 clicks / 0 impressions**, CTR 0%, avg position 0. Queries: none.
  Pages: none.
- Chart on this property only showed 2026-08-08 – 2026-08-31 because earlier
  days had no data.
- Raw OW CSVs are header-only.
- URL-prefix `https://outlierweekly.substack.com/` is listed in the account but
  **Not verified**; not used this run. Verify it only if you want that property
  too.
- Empty is expected, not a ranking failure: hub + sitemap were submitted
  2026-08-30; the digest window ends 2026-08-31; first digest; no prior movers.

Operator leftover (digest action 3 — Coverage check):

- [x] GSC **Pages / Page indexing** for `sc-domain:outlierweekly.com` (agent pull
      via logged-in browser, 2026-09-17). Report last updated **2026-09-13**.

### Indexed (6) — matches sitemap exactly

| URL | Last crawled |
|-----|--------------|
| `https://outlierweekly.com/` | Sep 8, 2026 |
| `https://outlierweekly.com/about/` | Aug 30, 2026 |
| `https://outlierweekly.com/methodology/` | Sep 8, 2026 |
| `https://outlierweekly.com/atto/` | Aug 30, 2026 |
| `https://outlierweekly.com/guruwatcher/` | Aug 30, 2026 |
| `https://outlierweekly.com/spcx-anthropic/` | Sep 5, 2026 |

`site:outlierweekly.com` on Google (2026-09-17) returns the same six URLs.

### Not indexed (6) — all expected redirects / retired hubs

| URL | Reason | Redirect target (probed) |
|-----|--------|--------------------------|
| `http://outlierweekly.com/` | Page with redirect | → `https://outlierweekly.com/` |
| `http://www.outlierweekly.com/` | Page with redirect | (canonical HTTPS apex) |
| `https://www.outlierweekly.com/` | Page with redirect | → `https://outlierweekly.com/` |
| `https://outlierweekly.com/agent-harness/` | Page with redirect | → `https://outlierweekly.com/` |
| `https://outlierweekly.com/prediction-market-lp-bot/` | Page with redirect | (retired hub) |
| `https://outlierweekly.com/cxw-geo/` | Page with redirect | → `https://outlierweekly.com/spcx-anthropic/` |

GSC labels these **Page with redirect** (validation failed 2026-09-05). This is
normal — Google indexes the destination URLs above, not the redirect sources.

### Performance delta vs first digest (2026-09-03)

28-day window ending ~2026-09-14 (GSC Performance, 2026-09-17):

- **17 impressions / 0 clicks** (was 0/0 on first digest)
- Avg position **5.3**
- Top query: `spcx anthropic` (1 impression)
- Indexing chart shows 6 indexed pages from ~Aug 30 onward

No action required on coverage unless a new hub page ships — then add to
`sitemap.xml` and request indexing via URL Inspection.

## Substack (UI)

- [x] Rename the publication to **Outlier Weekly** (operator, 2026-08-30).
      Confirmed on the About OG title (`About - Outlier Weekly`) and the
      sign-in chrome (`Sign in to Outlier Weekly`). Home `og:title` / RSS
      channel still say `outlierweekly` — Substack cache or the subdomain
      slug. Subdomain stays `outlierweekly.substack.com`.
- [ ] Optional: add a link to `https://outlierweekly.com/` from the Substack
      About page (homepage does not mention the custom domain today).

## Google Search Console

- [x] Confirm `sc-domain:outlierweekly.com` (already verified via TXT).
- [x] Submit the owned sitemap: `https://outlierweekly.com/sitemap.xml` (GSC dialog: “Sitemap submitted successfully”, 2026-08-30).
- [ ] Optional: submit the Substack feed
      (`https://outlierweekly.substack.com/feed`) once the Substack
      URL-prefix property is verified.

## Bing Webmaster Tools

- [x] Property `outlierweekly.com/` is already verified (checked 2026-08-30 in Bing WMT; 0 clicks / 0 impressions).
- [x] Submit `https://outlierweekly.com/sitemap.xml` (Bing: Success / Processing, 2026-08-30).

## Brave Search

- [x] Re-ran submit-url after 200s (2026-08-30): home + about confirmed
      Success.
- [x] After Atto/GuruWatcher swap (2026-08-30): atto, guruwatcher,
      methodology, and (then) cxw-geo each returned Success on
      search.brave.com/submit-url. Form is a re-fetch, not a new-URL
      intake. Brave has no sitemap API.
- [x] After SPCX/Anthropic swap (2026-08-30):
      `https://outlierweekly.com/spcx-anthropic/` returned Success on
      search.brave.com/submit-url (`/cxw-geo/` 301s there).

## Backlinks (other repos, parent)

- [ ] Add "Outlier Weekly" links from product surfaces: `youratto.com`,
      `guruwatcher.com`, and the `cemini23/world-cup-bot` README + GitHub
      Pages site.

## Cloudflare

- [x] Bot Fight Mode is **off** (probed 2026-08-30). The ~502 status-403
      responses in the audit window were not BFM. Recheck after the hub
      is live if crawlers still get 403 (security_level is medium).
- [x] **Always Use HTTPS** on (patched 2026-08-30). Worker also 301s `http` → `https`.
- [x] **Minimum TLS** raised to 1.2.
- [ ] Confirm `Strict-Transport-Security` on HTML (set in the Worker, not
      `_headers` — `run_worker_first` skips the `_headers` file). No `preload`.

## Later (not this quarter)

- [ ] $50/year Substack custom-domain CNAME: wait months. The owned hub is the
      working solution without it.
