# Outlier Weekly — operator leftovers (2026-08-30)

Hands-on items for the human operator. None of these are agent actions; the
agent does not touch Substack settings, GSC, Bing, Brave, or Cloudflare
dashboard toggles.

## Substack (UI)

- [ ] Rename the publication to **Outlier Weekly** (currently the title shows
      `outlierweekly | Cemini23 | Substack`). The owned hub already uses the
      proper brand; the Substack title should match.
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
      Success. Remaining hubs: methodology, prediction-market-lp-bot,
      cxw-geo, agent-harness (same form). Brave has no sitemap API.

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
