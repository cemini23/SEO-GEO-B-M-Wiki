---
type: concept
related:
  - concepts/local-seo-foundations.md
  - concepts/website-essentials-local-business.md
  - concepts/google-business-profile.md
  - concepts/generative-engine-optimization.md
  - concepts/on-page-seo-local.md
  - entities/tools/yoast-seo.md
  - entities/tools/geo-seo-claude.md
  - entities/tools/google-search-console.md
  - entities/platforms/yelp.md
  - sources/aggarwal-2024-geo-paper.md
  - concepts/first-90-days-playbook.md
  - concepts/content-strategy-local.md
  - concepts/local-pack-rankings.md
  - concepts/per-entity-bias-mapping-geo.md
  - sources/searchengineland-2026-google-llm-patent-entity-characterization-480625.md
  - sources/arxiv-crespin-2026-karla-knowledge-base-augmented-retrieval-2606.26807-2026-06-28.md
  - concepts/canonical-business-facts-geo.md

maturity: validated
created: 2026-05-07
updated: 2026-06-28

---

## Relations

- @concepts/local-seo-foundations.md
- @concepts/website-essentials-local-business.md
- @concepts/google-business-profile.md
- @concepts/generative-engine-optimization.md
- @concepts/on-page-seo-local.md
- @entities/tools/yoast-seo.md
- @entities/tools/geo-seo-claude.md
- @entities/tools/google-search-console.md
- @entities/platforms/yelp.md
- @sources/aggarwal-2024-geo-paper.md
- @concepts/first-90-days-playbook.md
- @concepts/content-strategy-local.md
- @concepts/local-pack-rankings.md
- @sources/searchengineland-2026-google-llm-patent-entity-characterization-480625.md — unstructured + structured entity evidence
- @sources/arxiv-crespin-2026-karla-knowledge-base-augmented-retrieval-2606.26807-2026-06-28.md — typed relation layer (KARLA analog)
- @concepts/canonical-business-facts-geo.md — GBP + schema sync playbook

## Raw Concept

Concept hub for **schema markup** — JSON-LD structured data on the website that tells search engines and AI engines what the business is, where it is, what it offers, and what people say about it. Critical for both classical local SEO (rich results in SERPs, Knowledge Panel data, local pack qualification) and 2026 GEO/AEO citation behavior (AI engines preferentially cite pages with valid `Service` / `FAQPage` / `LocalBusiness` markup that disambiguates the entity).

Schema supports **entity confidence**, but @sources/searchengineland-2026-google-llm-patent-entity-characterization-480625.md describes LLM pipelines that also interpret **unstructured** page copy — JSON-LD is hygiene, not a substitute for clear services/team/experience evidence. Google June 2026 guidance (@sources/techwyse-2026-google-good-seo-is-good-geo-kraham-2026-06.md): structured data + helpful content over speculative AI-only files (e.g. llms.txt).

For the barbershop operator, schema markup is **a one-time setup task that pays off forever**.

## Narrative

### What schema actually does

Schema.org is the shared vocabulary for structured data on the web — a way to label HTML so machines can extract entities and relationships unambiguously. Search engines (Google, Bing), AI engines (ChatGPT, Claude, Perplexity, Gemini), and other parsers (DuckDuckGo, Brave, Apple Maps via Yelp) all consume it to varying degrees. The output for the operator:

- **Rich results in Google search** — star ratings, business hours, FAQ accordions, breadcrumbs in the SERP
- **Knowledge Panel data** — when Google surfaces a business card on the right side of search, schema feeds attributes
- **Local pack qualification** — schema isn't a primary ranking factor but is a confidence signal for entity disambiguation
- **AI engine citations** — see @sources/aggarwal-2024-geo-paper.md; structured pages are preferentially cited because they're easier to extract correctly

### The load-bearing schema types for a barbershop

| Schema type | Where it lives | Why it matters |
|-------------|---------------|----------------|
| `BarberShop` (extends `LocalBusiness`) | Homepage + each per-location page | Defines the entity itself: name, address, hours, phone, geo |
| `Service` | Each service-detail page (or as `hasOfferCatalog` on the LocalBusiness) | Defines what's offered + price; AI-engine-friendly for "haircut prices [city]" type queries |
| `FAQPage` | Any page with FAQ content | Surfaces in SERP as expandable accordion; preferentially cited by AI engines per Aggarwal 2024 |
| `BreadcrumbList` | Every page (auto-generated) | Site navigation in SERP; helps Google understand site structure |
| `WebSite` + `SearchAction` | Homepage only | Enables sitelinks search box in SERP |
| `Person` | Per-barber bio pages (if any) | E-E-A-T signal; AI engines name the barber when answering "who's the best fade specialist in [city]" |
| `Review` / `aggregateRating` | ONLY if displaying real on-page reviews | Surfaces star count in SERP — but **never fake these**; structured-data spam violation gets manual penalty |

### The full BarberShop JSON-LD template

Drop this in the `<head>` of each per-location page (homepage if single location). Replace ALL-CAPS placeholders with real values. This template is `[NEEDS VERIFICATION 2026-05-07]` against the current schema.org `BarberShop` spec but reflects the 2024-2025 stable shape.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BarberShop",
  "@id": "https://YOURSHOP.COM/locations/CITY-SLUG/#barbershop",
  "name": "SHOP NAME",
  "image": [
    "https://YOURSHOP.COM/images/storefront-1x1.jpg",
    "https://YOURSHOP.COM/images/storefront-4x3.jpg",
    "https://YOURSHOP.COM/images/storefront-16x9.jpg"
  ],
  "url": "https://YOURSHOP.COM/locations/CITY-SLUG/",
  "telephone": "+1-555-XXX-XXXX",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "STREET ADDRESS",
    "addressLocality": "CITY",
    "addressRegion": "ST",
    "postalCode": "ZIP",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 0.0000,
    "longitude": 0.0000
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Tuesday","Wednesday","Thursday","Friday"],
      "opens": "10:00",
      "closes": "19:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "09:00",
      "closes": "18:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Sunday",
      "opens": "10:00",
      "closes": "16:00"
    }
  ],
  "sameAs": [
    "https://www.google.com/maps/place/?q=place_id:GBP_PLACE_ID",
    "https://www.instagram.com/YOURHANDLE",
    "https://www.facebook.com/YOURPAGE",
    "https://www.yelp.com/biz/YOUR-LISTING-SLUG"
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Barbershop Services",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Men's Haircut",
          "description": "Classic men's haircut including consultation, shampoo, cut, and styling.",
          "serviceType": "Haircut"
        },
        "price": "35.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Fade",
          "description": "Skin fade or scissor fade with detailed line-up.",
          "serviceType": "Haircut"
        },
        "price": "40.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Beard Trim",
          "description": "Beard shaping, lining, and conditioning.",
          "serviceType": "Beard Trim"
        },
        "price": "20.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Hot Towel Shave",
          "description": "Traditional straight-razor shave with hot towels and aftershave.",
          "serviceType": "Shave"
        },
        "price": "45.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Kids' Cut (12 and under)",
          "description": "Patient, kid-friendly haircut.",
          "serviceType": "Haircut"
        },
        "price": "25.00",
        "priceCurrency": "USD"
      }
    ]
  }
}
</script>
```

**Critical fields explained**:

- `@id` — stable canonical URI for the entity. Use `https://yourshop.com/locations/CITY-SLUG/#barbershop` form (page URL + fragment). Required so Google can de-duplicate the same entity across pages.
- `image` — supply 1:1, 4:3, and 16:9 ratio versions of the storefront photo. Google Rich Results expects the array.
- `priceRange` — use `$` / `$$` / `$$$` (dollar signs, not numeric). For a typical barbershop in a mid-priced market, `$$` is appropriate (~$30-50 cuts); adjust to `$` or `$$$` based on the operator's actual price points.
- `geo.latitude` / `geo.longitude` — replace with shop-exact coordinates from Google Maps "right-click → What's here?" (down to 4 decimal places is enough — that's ~10m precision).
- `openingHoursSpecification` — use 24-hour format strings. Closed days are simply omitted.
- `sameAs` — array of canonical URLs to the same entity on other platforms. Critical for entity disambiguation. The GBP `sameAs` URL uses the Google Place ID format; obtain Place ID from [Google's Place ID finder tool](https://developers.google.com/maps/documentation/places/web-service/place-id).
- `hasOfferCatalog` — service menu. Each `Offer` wraps a `Service` with explicit `price` + `priceCurrency`. AI engines extract these for "barbershop prices in [city]" queries.

### FAQPage schema (paste on the FAQ page)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need an appointment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We accept walk-ins and appointments. Walk-ins are first-come-first-served; Saturdays usually have wait times of 30–60 minutes. Appointments can be booked at YOURSHOP.COM/book or by calling 555-XXX-XXXX."
      }
    },
    {
      "@type": "Question",
      "name": "How much does a haircut cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Standard men's haircuts start at $35. Fades are $40. Beard trims are $20. Kids' cuts (12 and under) are $25. Full pricing is on our services page."
      }
    },
    {
      "@type": "Question",
      "name": "Do you do skin fades?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — skin fades and scissor fades are core specialties. Several of our barbers focus on fade and line-up work for clients with curly, coily, and textured hair."
      }
    },
    {
      "@type": "Question",
      "name": "What ages do you cut?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All ages. Kids 12 and under are $25 and we have barbers experienced with first-haircuts and squirmy clients."
      }
    },
    {
      "@type": "Question",
      "name": "Do you accept tips on card?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — tips can be added on card at checkout, or in cash to your barber directly."
      }
    }
  ]
}
</script>
```

**Why FAQ schema matters specifically for AI engines**: per @sources/aggarwal-2024-geo-paper.md, content with the "Cite Sources" + "Statistics Addition" patterns gets +27% / +33% citation lift in generative engines. FAQ format embeds both: short authoritative answers + concrete data. AI engines preferentially cite FAQ-formatted content because it matches their answer-shape.

### Multi-location pattern (Shop 1 + Shop 2)

If both shops share one website domain (e.g., `yourshop.com/locations/[city]-east/` + `yourshop.com/locations/[city]-west/`):

- Each location page gets its own `BarberShop` block with that location's `@id`, address, geo, hours
- Homepage adds an `Organization` schema referring to both locations:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://yourshop.com/#organization",
  "name": "BRAND NAME",
  "url": "https://yourshop.com/",
  "logo": "https://yourshop.com/images/logo.png",
  "sameAs": [
    "https://www.instagram.com/YOURHANDLE",
    "https://www.facebook.com/YOURPAGE"
  ],
  "subOrganization": [
    { "@id": "https://yourshop.com/locations/CITY-EAST/#barbershop" },
    { "@id": "https://yourshop.com/locations/CITY-WEST/#barbershop" }
  ]
}
</script>
```

If each shop has a separate website (or separate brand identity): treat each as standalone, no `Organization` parent.

### Validation workflow

After dropping schema in:

1. **Google Rich Results Test** — `https://search.google.com/test/rich-results` → enter URL → see what Google parses + which rich results are eligible. Fix every error and warning before going live.
2. **Schema.org Validator** — `https://validator.schema.org/` → strict spec validation. Less forgiving than Google but catches issues Google ignores.
3. **Visual cross-check** — every fact in the schema must match the visible page content. `priceRange: $$` + visible $35 cuts: fine. `priceRange: $` + visible $200 cuts: Google penalty. `aggregateRating: 4.9` with no visible reviews on the page: spam violation.

After live: re-test 24-48 hours later in **Search Console → Enhancements** for "FAQ", "Local Business" enhancement reports. These show what Google is actually picking up site-wide.

### What to NEVER put in schema

- `aggregateRating` / `Review` schemas without matching visible reviews on the page → spam violation, manual penalty
- Hours / phone / address that don't match GBP and the visible page → kills entity confidence
- Services you don't offer ("organic massage" etc. when you're a pure barbershop) → spam
- Prices you don't honor → consumer-protection issue + spam
- Schema for content that's hidden from users (display:none, behind a tab the user can't open) → Google parses what users see; mismatch = penalty

### Plugin vs hand-written

WordPress + **Yoast SEO** (see @entities/tools/yoast-seo.md) auto-generates `LocalBusiness` schema from the Local SEO addon (paid) or basic `Organization` schema (free). The free version does NOT generate `BarberShop` (the more specific subtype) — operator must either pay for Yoast Local SEO or hand-write the schema in a custom HTML block.

Other platforms:
- **Wix** — has built-in structured data for business listings; `BarberShop` subtype availability `[NEEDS VERIFICATION 2026-05-07]`
- **Squarespace** — limited built-in schema; usually requires custom code injection
- **Webflow** — full control via the visual editor's `<head>` injection
- **Shopify** — barbershop-as-Shopify is unusual but possible; product-schema patterns dominate

For all platforms: **the geo-seo-claude Claude Code skill** (see @entities/tools/geo-seo-claude.md) audits live page schema and reports gaps. Run it after install + before each major page update.

## Snippets

### From schema.org spec

> "BarberShop: A barbershop. (Type: LocalBusiness > HealthAndBeautyBusiness > BarberShop)"  
> [Source: https://schema.org/BarberShop (retrieved 2026-05-07)]

> "FAQPage: A FAQPage is a WebPage presenting one or more 'Frequently asked questions' (see also QAPage)."  
> [Source: https://schema.org/FAQPage (retrieved 2026-05-07)]

### From Aggarwal 2024 (re schema-relevance for GEO)

> "FAQ-format content received +27% to +41% citation visibility uplift in generative engines depending on the optimization strategy applied."  
> [Source: aggarwal-2024-geo-paper.md p.7] — see @sources/aggarwal-2024-geo-paper.md

`[NEEDS VERIFICATION 2026-05-07]` — the BarberShop and FAQPage spec details above need re-validation against schema.org as of the operator's actual launch date; spec details occasionally shift in minor revisions.
