---
title: Citation Building (NAP Listings)
type: concept
tags: [seo, local-seo, citations, NAP, directories, geo-search]
keywords: [citations, NAP consistency, directory listings, yellow pages, foursquare, yext, data aggregators]
related:
  - concepts/local-seo-foundations.md
  - entities/tools/brightlocal.md
  - entities/tools/claude-seo-agrici.md
maturity: draft
created: 2026-05-07
updated: 2026-05-07
---

## Relations

- @concepts/local-seo-foundations.md
- @entities/tools/brightlocal.md
- @entities/tools/claude-seo-agrici.md

## Raw Concept

Stub concept page for **citation building** — the practice of getting the business listed (with consistent NAP) across the ecosystem of business directories that feed search engines and AI engines. Populate via ingest of Whitespark citation studies, Moz Local guides, and 2024-2026 directory-relevance research.

## Narrative

A "citation" is any mention of the business's NAP (Name, Address, Phone) on the open web. Search engines use citations as signals for entity confidence ("we're sure this is a real business at this location") and for retrieval fan-out ("we'll show this business in the local pack because we found it in 50 places, all consistent").

The 2024-2026 reality: a small number of **high-authority core citations** dominate the value, and the long tail of low-authority directory submissions is mostly noise (and can be net-negative if any of them are spammy). The core citations every barbershop should claim:

1. **GBP** (the primary citation, also the SERP surface)
2. **Apple Business Connect** (powers Apple Maps + Siri)
3. **Bing Places** (powers Bing + Microsoft Copilot)
4. **Yelp** (review surface + Apple Maps data)
5. **Facebook Page** (review surface + Meta data)
6. **Yellow Pages / YP.com** (still a real authority for Google's NAP confidence)
7. **Foursquare** (data flows to many other apps via Foursquare's data partners)
8. **Industry-specific**: barbershop directories, booking-system directories (Booksy, Vagaro, Squire if used), grooming-industry sites
9. **Local Chamber of Commerce** (Davie / Cooper City / Greater Fort Lauderdale chambers)
10. **Major local-newspaper / city-guide directories** (Sun-Sentinel, NewTimes Broward, etc.)

Beyond these, the Phase-0 audit lens applies (see CLAUDE.md): adding the operator's NAP to a spam directory is worse than not adding it, because Google notices.

**NAP consistency** is the load-bearing rule: every citation must list the same name (no "Shop Name" vs "Shop Name Inc" vs "Shop Name Barber Shop"), the same address (suite numbers, abbreviations, etc.), and the same phone format. BrightLocal's citation tracker (@entities/tools/brightlocal.md) is the standard tool for finding existing citations + flagging inconsistencies. For a brand-new operator: start by running this audit against current state before changing anything.

**Data aggregators** — sources like Foursquare, Acxiom, Localeze, Neustar feed many downstream directories. A clean entry in the aggregators propagates through the ecosystem with less per-directory effort. Yext is the commercial product that manages this propagation; whether it's worth the cost vs manual + BrightLocal is operator-specific.

## Snippets

(none yet — populate via ingest of Whitespark citation guides + Moz citation source list + 2024-2026 directory-impact studies)
