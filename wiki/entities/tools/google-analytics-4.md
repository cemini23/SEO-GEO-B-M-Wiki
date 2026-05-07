---
title: Google Analytics 4 (Tool)
type: entity
tags: [tool, google, analytics, ga4]
keywords: [google analytics, GA4, conversion tracking, attribution, events]
related:
  - concepts/website-essentials-local-business.md
maturity: draft
created: 2026-05-07
updated: 2026-05-07
---

## Relations

- @concepts/website-essentials-local-business.md

## Raw Concept

Stub entity page for Google Analytics 4 — Google's free website-analytics platform, replacing Universal Analytics in 2023. Tracks visitors, traffic sources, and operator-defined conversion events.

## Narrative

GA4 is event-based (every interaction is an event), unlike Universal Analytics's session-based model. For a barbershop website, the load-bearing setup is: (a) book / call / direction-click / message events configured as conversions, (b) traffic-source attribution (so the operator can see what share of bookings came from organic vs IG vs paid), (c) per-page conversion-rate to spot under-performing location pages.

Privacy / consent requirements: GA4 with default settings collects data that may require a cookie banner for compliance with state privacy laws (Florida's pending consumer-data law `[NEEDS VERIFICATION 2026-05-07]`). Server-side / consent-mode setup is more complex than legacy Analytics.

GA4 is for the **website**. GBP traffic is a separate analytics surface; phone calls from GBP need call-tracking integration (CallRail, Marchex, or platform-native) to attribute correctly.

## Snippets

(none yet)
