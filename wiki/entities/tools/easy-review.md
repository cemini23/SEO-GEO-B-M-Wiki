---
title: Easy Review — Companion App for Review Replies + Customer Re-engagement
type: entity
tags: [tool, automation, companion-app, review-management, customer-retention, nextjs, supabase, gemini-flash]
keywords: [easy review, review automation, review reply, slipping regulars, win-back, sms, gemini flash, supabase, next.js]
related:
  - concepts/reviews-reputation-management.md
  - concepts/review-response-templates.md
  - concepts/first-90-days-playbook.md
  - concepts/session-1-facilitator-notes.md
  - entities/platforms/google-business-profile.md
maturity: draft
created: 2026-05-08
updated: 2026-05-08
---

## Relations

- @concepts/reviews-reputation-management.md
- @concepts/review-response-templates.md
- @concepts/first-90-days-playbook.md
- @concepts/session-1-facilitator-notes.md
- @entities/platforms/google-business-profile.md

## Raw Concept

Companion micro-app to this wiki, developed in a parallel Claude Code session. The wiki is a knowledge base (read-and-feed-to-Claude); Easy Review is the operator-facing execution surface for the two highest-volume tasks that the wiki points at: responding to reviews + winning back lapsed regulars.

The two surfaces are deliberately separate — the wiki has a long shelf life and broad scope; Easy Review is a focused operator UI with a narrower ship-cycle. This page documents Easy Review's scope so the wiki's recommendations can reference the tool by name where relevant.

## Narrative

### What it is

Easy Review is a Next.js 15 (App Router) + TypeScript + Tailwind v4 + Supabase + Gemini Flash micro-SaaS. Two features:

**1. Review Command Center**

- Pulls 1–5 star reviews from Google Business Profile (mock JSON in current state; live GBP API integration pending OAuth)
- For each review, Gemini Flash drafts 3 reply options labeled by tone — *Empathetic*, *Professional*, *Brief*
- UI presents each review as a card; operator swipes / clicks Approve, Edit, or Skip. Mobile-first (iPad + iPhone primary surfaces)
- Operator stays in the loop on every send. No auto-posting. No review gating (which would violate Google policy — see @concepts/reviews-reputation-management.md)

**2. VIP Re-Engager**

- Operator uploads a guest CSV (export from Square / Booksy / Vagaro / Squire / Schedulicity / any CRM with last-visit-date + favorite-service columns)
- App flags "slipping regulars" — guests whose last visit is >45 days ago and whose visit cadence suggests they're at risk of churn
- Gemini Flash drafts a personalized SMS invite per guest, anchored on their visit history (favorite service, average price tier, last appointment)
- Operator reviews + approves each draft before sending. No bulk auto-send, no SMS to guests who haven't opted in.

### Tech stack

- **Framework**: Next.js 15 (App Router); Server Actions over API routes
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4
- **Auth + DB**: Supabase (Postgres + auth)
- **AI drafting**: Gemini Flash (Google's fast/cheap model — appropriate for templated short-form drafting; cost predictable at operator scale)
- **CSV parsing**: papaparse
- **UI motion**: framer-motion (Tinder-style swipe deck)

### Where it fits in the wiki's recommendations

- @concepts/reviews-reputation-management.md — Easy Review is the recommended way to operationalize the *response* side of the playbook. Acquisition (asking for reviews) still happens through the booking platform (Booksy / Square / Vagaro auto-trigger SMS post-appointment) or in-shop signage / QR codes.
- @concepts/review-response-templates.md — Easy Review's three-option draft (Empathetic / Professional / Brief) is a runtime instantiation of the templates documented in the wiki concept page. The wiki page is the *frame* for what good replies look like; Easy Review applies that frame at scale.
- @concepts/first-90-days-playbook.md — Week 3 (review acquisition + response) is where Easy Review enters the operator's stack, after the GBP foundation (Week 1) + NAP cleanup (Week 2) work.
- @concepts/session-1-facilitator-notes.md — once the operator's GBP is captured + claimed in session 1, Easy Review is the natural follow-up tool to introduce in session 2 (alongside review-acquisition workflow setup).
- @entities/platforms/google-business-profile.md — once the GBP API integration lands, Easy Review reads from + writes to GBP directly, replacing the mock JSON layer. Until then, the operator copies + pastes replies from Easy Review into the GBP dashboard.

### Boundary discipline

Easy Review explicitly does NOT:

- Auto-post replies (every send is operator-approved)
- Gate reviews (no "are you happy with us? if yes, leave a Google review; if no, tell us privately" funnel — that's a Google policy violation)
- Generate or solicit fake reviews
- Send SMS to guests who haven't opted in to marketing communication
- Bulk-blast templated messages (every SMS draft is reviewed individually)

These are the same boundaries the wiki enforces in @concepts/reviews-reputation-management.md. The tool inherits them by design.

### Current state (2026-05-08)

- Active development in a parallel Claude Code session
- Mock data wired (`src/data/mock-reviews.json`, `src/data/mock-guests.csv`)
- App shell live (operator-branded header on the home page)
- Live GBP API integration: pending (OAuth scoping + Google review-management API access)
- Live SMS send (via Twilio or similar): pending
- Supabase auth + multi-tenant: pending
- No production deployment yet

### Why a separate app and not part of the wiki

The wiki is content (markdown). Easy Review is software (app). The concerns are different:

- The wiki accumulates over time; pages don't go stale fast. No build step. Read with any markdown viewer or load into Claude as context.
- Easy Review needs a backend, auth model, API integrations, and a deployable surface. Different lifecycle, different release cadence.

Bundling them would force the wiki into a build/deploy cycle it doesn't need.

### Phase-0 audit verdict

N/A — Easy Review is built in-house alongside the wiki, not a third-party tool being adopted. The wiki's Phase-0 pattern applies to external tools (Yoast, Local Falcon, Semrush, etc.). Internal companion apps are tracked here for reference but don't need GO/NO-GO scoring.

## Snippets

(none — Easy Review is internal, not yet citable from external research)
