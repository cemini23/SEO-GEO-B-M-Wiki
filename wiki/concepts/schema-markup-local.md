---
title: Schema Markup for Local Business
type: concept
tags: [seo, schema, structured-data, json-ld, geo-search, geo-aeo]
keywords: [schema, JSON-LD, LocalBusiness, BarberShop, Service, FAQPage, Review, structured data]
related:
  - concepts/local-seo-foundations.md
  - concepts/website-essentials-local-business.md
  - concepts/google-business-profile.md
  - concepts/generative-engine-optimization.md
  - entities/tools/yoast-seo.md
  - entities/tools/geo-seo-claude.md
maturity: draft
created: 2026-05-07
updated: 2026-05-07
---

## Relations

- @concepts/local-seo-foundations.md
- @concepts/website-essentials-local-business.md
- @concepts/google-business-profile.md
- @concepts/generative-engine-optimization.md
- @entities/tools/yoast-seo.md
- @entities/tools/geo-seo-claude.md

## Raw Concept

Stub concept page for **schema markup** — JSON-LD structured data on the website that tells search engines and AI engines what the business is, where it is, what it offers, and what people say about it. Critical for both classical local SEO and 2026 GEO/AEO citation behavior. Populate via ingest of schema.org docs, Google Rich Results Test guidance, and `BarberShop` / `LocalBusiness` spec.

## Narrative

Schema.org is the shared vocabulary for structured data on the web. Search engines (Google, Bing) and AI engines (ChatGPT, Claude, Perplexity, Gemini) all parse it to varying degrees. For a barbershop, the load-bearing schema types are:

- `LocalBusiness` (parent class) → `BarberShop` (specific subtype). Includes `name`, `address` (`PostalAddress`), `telephone`, `geo` (`GeoCoordinates`), `openingHours`, `image`, `url`, `priceRange`.
- `Service` — for each service offered (haircut, beard trim, hot towel shave, kids' cut), with `name`, `description`, `offers.price`.
- `FAQPage` — on FAQ content; each question/answer becomes a Q&A pair Google may surface as a rich result.
- `Review` / `aggregateRating` — only if displaying *real* on-page reviews; faking these is a structured-data spam violation.
- `BreadcrumbList` — site-wide navigation.

Schema lives in JSON-LD `<script type="application/ld+json">` blocks in the page `<head>`. Google's Rich Results Test (`search.google.com/test/rich-results`) and the Schema.org validator (`validator.schema.org`) are the two test surfaces.

For a multi-location operator: each per-location page should have its own `LocalBusiness` block with that location's NAP and geo. The homepage may either omit the schema (and rely on per-location pages to carry it) or use a multi-location pattern (organization + locations array). `[NEEDS VERIFICATION 2026-05-07]`: 2026-current best-practice pattern for multi-location.

WordPress / Wix / Squarespace plugins (Yoast, Rank Math, Schema Pro, etc.) auto-generate schema from page content; the operator should review the output in Rich Results Test rather than trust the plugin blindly — common failure modes include using deprecated properties, missing `@id` for entity de-duplication, schema that doesn't match the visible page content (Google penalizes mismatch).

## Snippets

(none yet — populate via ingest of schema.org BarberShop spec + Google Rich Results help docs)
