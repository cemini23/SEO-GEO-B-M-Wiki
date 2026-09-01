### Verdict
WARN — The Substack content can be found by Google in principle, but the Cloudflare 301-worker on the brand domain, missing RSS-as-sitemap submission, absent Bing/IndexNow/Brave integration, and lack of owned hub URLs mean discovery is materially throttled. Not FAIL because the existing stack can be repaired without moving off Substack.

### Findings

| Severity | Finding | Evidence (file:line or quote) | Fix |
|----------|---------|----------------------------------|-----|
| critical | `outlierweekly.com` is a Cloudflare worker that 301s everything to `outlierweekly.substack.com`, so the brand domain never serves 200 content. | EVIDENCE.md: “Cloudflare 301 worker”; “0 page views; 90%+ are 301s” | Scoped routing: serve `/`, `/about`, `/start-here`, hub pages and `/llms.txt` as 200 from the worker; redirect only legacy `/p/*` paths to Substack. Or move to Substack custom domain. |
| critical | Substack `/sitemap.xml` is 404, and no RSS feed has been submitted as a sitemap. | EVIDENCE.md: “Substack `/sitemap.xml` 404 is a platform limit” | Submit `https://outlierweekly.substack.com/feed` to Google Search Console and Bing Webmaster Tools. Google accepts RSS/Atom feeds as sitemaps. |
| warning | Brave “submit-url” was done 2026-08-08, but `site:outlierweekly.com` is empty. | EVIDENCE.md: “Assuming Brave submit-url equals indexed” | Make the brand domain return real 200 pages; then resubmit `/` and the 3–5 hub URLs to Brave. Use backlinks from product sites to help Brave discover them. |
| warning | Bing and IndexNow are not configured; IndexNow cannot work on the Substack host because the key file cannot be placed at its root. | EVIDENCE.md: no Bing/IndexNow evidence in pack | Add the site to Bing Webmaster Tools, import from GSC, submit the feed; after moving content to an owned host/custom domain, create an IndexNow key and serve `/{key}.txt` from the Cloudflare worker. |
| warning | All content is chronological Substack posts; there are no owned pillar/hub URLs for topic queries or LLM citation. | EVIDENCE.md: “all content at outlierweekly.substack.com” | Add 3–5 owned URLs: `/start-here`, a topical hub, `/glossary`, `/best-of`, `/about`. Link to these from every post. |
| warning | Brand collision risk with “Outlier AI” is not handled in the current surface. | Prompt context: “brand collision with Outlier AI” | Always use the full “Outlier Weekly” name in `<title>`, `h1`, About copy, and JSON-LD; add an explicit “independent/not affiliated” line if true. |
| info | Email list is ~18 subscribers, so owned audience is not yet meaningful for traffic. | `freeSubscriberCountOrderOfMagnitude: "18"` | Treat email as a retention layer, not acquisition. Use search/GEO and backlinks for new traffic. |
| info | No evidence of legitimate schema on owned pages; Substack controls most page-level output. | EVIDENCE.md: no schema inventory | On owned pages, add valid `Organization`, `WebSite`, `Person`, and `NewsArticle` JSON-LD only when the facts are present on the page. |

### Answers

1. **Traffic: next 30 vs 90 days**

- **Next 30 days — make existing content discoverable.** Highest leverage is not more content; it is fixing the redirect/sitemap problem:
  - Change the worker so `outlierweekly.com` serves at least `/about` and `/start-here` as 200 pages.
  - Add `https://outlierweekly.substack.com/feed` as the sitemap in Google Search Console and Bing Webmaster Tools.
  - Request indexing for the 5–10 best posts via GSC URL Inspection.
  - Add internal links to those posts from every newer post.
- **Next 90 days — build topical authority.** Add 10–20 high-intent guide/hub pages, get backlinks from product sites you cover, and use GSC query data to find posts ranking on page 1–2 for update/interlinking. Build one “state of” data page per quarter; data pages are disproportionately cited by LLM/AI-overview features.

2. **More pages: yes/no/conditional**

**Conditional yes — but only 3–5 owned URLs, not a blog mill.** The condition is that `outlierweekly.com` must stop blanket-301ing before these pages can do anything.

Recommended owned URLs:

- `https://outlierweekly.com/start-here` — “What is Outlier Weekly?” with scope, mission, top posts, and subscription CTA. This is the natural LLM citation for “what is” and also solves brand disambiguation.
- `https://outlierweekly.com/topics/ai-labor-market` — one topical hub for your main vertical, collecting every post on that theme. This is an internal-link hub and a landing page for topic queries.
- `https://outlierweekly.com/glossary` — 20–50 one-line definitions of niche terms used in the newsletter. Useful to human readers and easy for LLMs to quote.
- `https://outlierweekly.com/best-of` — a library of canonical posts sorted by theme, not date. Helps crawlers understand content inventory and increases dwell time.
- `https://outlierweekly.com/llms.txt` — a machine-readable index of the top 10–15 URLs with one-line descriptions. Cheap GEO addition; not a replacement for human pages.

If you cannot change the worker, do not add these yet. Instead, first fix the host.

3. **LLM/AEO citability**

- Put a direct answer in the first 40–60 words of every post. LLM extractors tend to lift that paragraph.
- Add stable entity facts: “Outlier Weekly is an independent newsletter by [author] covering [vertical]. It launched [month/year].”
- Add legitimate JSON-LD schema on owned pages: `Organization`, `WebSite`, `Person`, `NewsArticle` with `datePublished`/`dateModified`. Do not add `FAQPage` unless the visible page actually has Q&A.
- Build the hubs above and link every post to the relevant hub with descriptive anchor text.
- Get product-site backlinks: when you cover a product, send the company a one-line summary + link and ask them to link back. A single relevant backlink from a product site does more for both search ranking and LLM corpus authority than directory links.
- Add explicit “Sources” sections linking claims to primary reports. LLM-audited content favors verifiable citations.
- Keep URLs stable, avoid `?utm_*` on canonical URLs, and show “Last updated” dates.

4. **Linked and indexed status**

- **Google:** not proven from the pack. Operator must run `site:outlierweekly.substack.com` and inspect GSC coverage. Without a submitted sitemap, deeper posts are likely undiscovered or slow to be crawled.
- **Bing:** no evidence of Bing Webmaster Tools setup. Missing verification and sitemap.
- **Brave:** submission on 2026-08-08 did not produce an index; `site:outlierweekly.com` is empty today because the brand domain returns 301s.
- **IndexNow:** absent. Missing a root key file on an operator-controlled host.
- **What’s missing:** a 200-status brand domain, RSS-as-sitemap submission, Bing Webmaster Tools verification, IndexNow key, and internal hub pages.

5. **Other variables**

- **Canonical host:** pick one. Right now effective canonical is `outlierweekly.substack.com`, while `outlierweekly.com` redirects. That splits signals and makes citations less stable. Prefer moving to a Substack custom domain: content at `outlierweekly.com/p/...`, old subdomain redirects handled by Substack/worker.
- **Brand collision:** always use “Outlier Weekly” in full; “Outlier” alone collides with Outlier AI.
- **Crawl:** don’t let the worker serve a blanket 301 to `/archive`, `/feed`, or future hub pages.
- **E-E-A-T:** add an author bio and an “About the editor” page with credentials and publication history.
- **Email list:** ~18 subscribers is not a traffic source yet; use it as a notification list only.
- **Internal links:** Substack’s default “more from” is weak; add manual “Read next” links in each post to the best previous piece.
- **X/Reddit:** use these as discovery channels, but do not treat them as ranking or LLM-citation evidence.

6. **Index / sitemap status and exact operator clicks**

- **GSC:**
  1. Go to `https://search.google.com/search-console`.
  2. Add property → Domain → `outlierweekly.com`; verify via DNS TXT in Cloudflare.
  3. Add a separate URL-prefix property: `https://outlierweekly.substack.com/`.
  4. Sitemaps → submit `https://outlierweekly.substack.com/feed`.
  5. URL Inspection → enter `/about`, `/start-here`, and top posts → click “Request indexing”.
- **Bing:**
  1. Go to `https://www.bing.com/webmasters`.
  2. Add site → import from GSC or enter `outlierweekly.substack.com`.
  3. Verify DNS.
  4. Sitemaps → submit the same `/feed`.
  5. URL Submission → paste the top post URLs.
- **IndexNow:**
  1. In Bing Webmaster Tools, create an IndexNow key.
  2. Serve `https://outlierweekly.com/{key}.txt` from the Cloudflare worker. This cannot be done on the Substack host.
  3. Ping `https://www.bing.com/indexnow?url={encoded-url}&key={key}` for each new post.
- **Brave:**
  1. First, make `outlierweekly.com` return 200 for `/`, `/about`, and `/start-here`.
  2. Resubmit those URLs via the Brave website submission form.
  3. Use `site:outlierweekly.com` after 2–4 weeks to verify; if empty, earn backlinks from product sites and resubmit.

### Root cause

Traffic is low because the brand domain is a dead 301 layer rather than a citable host, Substack has no XML sitemap and the RSS feed was never submitted, Bing/IndexNow/Brave are either unconfigured or queued without 200 content, and all content is isolated on chronological Substack posts with no topical hubs. A ~18-subscriber email list adds almost no owned traffic. The architecture does not block Substack indexing, but it blocks the brand URL, sitemap-driven crawl, Bing/IndexNow, and LLM citation of an owned canonical host.

### Confidence

medium — the pack is missing GSC coverage data, Bing/IndexNow status, current worker route code, and Substack open rates. I would change to high if the operator pastes GSC Coverage/Sitemaps, Bing Webmaster Tools index counts, `site:` results, and the actual worker route configuration.

### Unique angle

The Cloudflare 301 worker is not just a redirect problem — it makes `outlierweekly.com` a “dead host” to LLM/agent crawlers, which increasingly reward URLs that serve stable 200 content with dates, descriptions, and internal hubs. The cheapest GEO win is not another blog post; it is making the brand domain a 200-status entity hub and treating `/feed` as the real sitemap until Substack offers one.