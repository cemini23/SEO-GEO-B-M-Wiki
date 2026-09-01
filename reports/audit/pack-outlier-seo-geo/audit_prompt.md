# Super audit — Outlier Weekly SEO + GEO

You are auditor {{MODEL_SLOT}} in a multi-model **readonly** council. Stress-test the evidence pack. Do not edit files. Do not invent metrics.

# Super-audit pack — built 2026-08-30T15:19:09Z

Workspace: `/private/tmp/outlier-audit-artifacts`
Prompt source: `/Users/claudiobarone/Projects/SEO:GEO B&M Business/reports/audit/outlier-seo-geo-2026-08-30/PROMPT.md`

## Read order

- `/Users/claudiobarone/Projects/SEO:GEO B&M Business/reports/audit/pack-outlier-seo-geo/EVIDENCE.md`
- `/Users/claudiobarone/Projects/SEO:GEO B&M Business/reports/audit/pack-outlier-seo-geo/gsc-setup-brief.md`
- `/Users/claudiobarone/Projects/SEO:GEO B&M Business/reports/audit/pack-outlier-seo-geo/world-cup-bot-search-discovery.md`
- `/Users/claudiobarone/Projects/SEO:GEO B&M Business/reports/audit/pack-outlier-seo-geo/e-geo-playbook.md`
- `/Users/claudiobarone/Projects/SEO:GEO B&M Business/reports/audit/pack-outlier-seo-geo/agent-ready-website.md`


## Role

SEO / GEO (generative-engine) strategy reviewer for a 4-month-old newsletter. Pressure-test architecture, indexing, content inventory, and growth levers. Prefer durable owned URLs + citability over “add a blog so we rank.”

## Target

Outlier Weekly — `outlierweekly.com` (Cloudflare 301 worker) + `outlierweekly.substack.com` (all content). Evidence file in this pack. Related wiki: `wiki/concepts/generative-engine-optimization.md`, `wiki/concepts/e-geo-universal-rewrite-playbook.md`, `wiki/concepts/agent-ready-website-local-bm.md`, `wiki/concepts/world-cup-bot-search-discovery.md`, `briefs/2026-08-08_outlier-weekly-search-console-setup.md`.

## Question

How should Outlier Weekly get more **qualified traffic** from (1) web search and (2) LLM / AI-overview citations — and should we add blog/guide pages — given the live indexing, Cloudflare, and Substack facts in the pack?

Answer all of these:

1. Traffic: highest-leverage next 30 days vs next 90 days.
2. More pages: yes/no/conditional. If yes, **which 3–5 owned URLs** (not a generic blog mill) and why. If no, what instead.
3. LLM/AEO citability: concrete GEO moves (facts, schema, hubs, product-site backlinks). No stuffing.
4. Are relevant pages linked + indexed on Google, Bing, Brave, IndexNow? What’s missing.
5. Other variables (canonical host, brand collision with Outlier AI, crawl, E-E-A-T, email list size, internal links, X/Reddit).
6. Index / sitemap status for Brave, IndexNow, Bing, GSC — and the exact operator clicks to close gaps.

## Constraints

- Readonly. No production writes. No LIVE Substack/Discord publish.
- Do not invent open rates, GSC clicks, or subscriber counts. Email stats = NO_EVIDENCE except `freeSubscriberCountOrderOfMagnitude: "18"` as tentative ~18.
- No fake schema, review gating, or LLM-gaming.
- Substack `/sitemap.xml` 404 is a platform limit; workarounds must be explicit (RSS as sitemap, custom domain, or owned host).
- Distinguish **Substack custom domain** (content at `outlierweekly.com/p/...`) from the current **301 worker**.

## Already ruled out

- Publisher API analytics (not enrolled).
- Treating Cloudflare request counts as human page views (0 page views; 90%+ are 301s).
- Assuming Brave submit-url (2026-08-08) equals indexed (site: is empty today).
- Keyword-stuffed README / Pages (wiki already forbids).

## Required output format

Return ONLY this structure:

### Verdict
PASS | WARN | FAIL — one line why (PASS = current stack is enough; WARN = works but major gaps; FAIL = architecture blocks discovery)

### Findings
| Severity | Finding | Evidence (file:line or quote) | Fix |
|----------|---------|----------------------------------|-----|
| critical/warn/info | ... | ... | ... |

### Answers
Numbered replies to the six questions. Be specific (URLs, GSC property type, DNS records).

### Root cause (if debugging)
One paragraph on why traffic is low.

### Confidence
high | medium | low — and what would change your mind (e.g. operator pastes GSC coverage + Substack open rates)

### Unique angle
One thing other models might miss
