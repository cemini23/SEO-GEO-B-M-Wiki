---
title: Easy Review — Companion App for Wiki-Driven Review Replies
type: entity
tags: [tool, automation, companion-app, review-management, nextjs, pocketbase, gemini-flash, octokit]
keywords: [easy review, review automation, review reply, review categorization, gemini flash, pocketbase, next.js, octokit, brief writeback, paste-flow]
related:
  - concepts/reviews-reputation-management.md
  - concepts/review-response-templates.md
  - concepts/first-90-days-playbook.md
  - concepts/session-1-facilitator-notes.md
  - entities/platforms/google-business-profile.md
  - concepts/high-ticket-smb-lead-generation.md
maturity: draft
created: 2026-05-08
updated: 2026-07-31
wire_status: policy_wired
wire_target: .cursor/rules/cemini-phase1-seo-geo-wires.mdc
---

## Relations

- @concepts/reviews-reputation-management.md
- @concepts/review-response-templates.md
- @concepts/first-90-days-playbook.md
- @concepts/session-1-facilitator-notes.md
- @entities/platforms/google-business-profile.md
- @concepts/high-ticket-smb-lead-generation.md

## Raw Concept

Companion app to this wiki, developed in a parallel Claude Code session. The wiki is the knowledge base (read-and-feed-to-Claude); Easy Review is the operator-facing surface that consumes the wiki's review-response framework and applies it to real reviews. Both repos are intentionally public and meant to be discovered together — wiki at [cemini23/SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki), app at [cemini23/Easy-Review](https://github.com/cemini23/Easy-Review).

The two surfaces are deliberately separate — the wiki has a long shelf life and broad scope; Easy Review is a focused operator UI with a narrower ship-cycle and a build/deploy lifecycle the wiki doesn't need.

## Narrative

### What it is (v0, paste-flow)

Easy Review v0 is a Next.js 15 (App Router) + TypeScript + Tailwind v4 + PocketBase + Gemini 2.0 Flash + Octokit app. It implements one feature end-to-end: **paste a review, get a categorized AI draft, approve, ship the brief back to the wiki**.

The flow:

1. Operator pastes a Google / Yelp / Facebook review (author, rating, date, text) into the form
2. App categorizes against the wiki's 5-category framework (`5star_specific` / `5star_generic` / `4star` / `3star_mixed` / `1_2star_complaint` / `1star_fake`) — see @concepts/review-response-templates.md
3. Gemini 2.0 Flash drafts a single reply using the wiki's response templates baked at build time. The 1★-likely-fake category is **never** AI-drafted; UI shows a fraud-handling card with "Don't reply / Flag to GBP / Override" choices instead.
4. Operator edits, regenerates, or approves the draft
5. On Approve, the app commits a brief markdown file back to the wiki repo via Octokit (`briefs/YYYY-MM-DD_<draft-id>.md`) — the wiki accumulates a corpus of real production replies that operators (and Claude) can learn from over time

### What it is NOT (yet)

v0 deliberately defers:

- **Live GBP / Yelp / Facebook API integration** — v1. Until then, paste in, copy out. This lets any operator validate the loop with zero OAuth scoping and no write-access risk.
- **Auto-posting of replies** — never. The Post click is always the operator's action, by design (not just by limitation). See "Boundary discipline" below.
- **Customer re-engagement / SMS / win-back flows** — out of scope for v0. The earlier prototype that bundled review-reply drafting + customer re-engagement (the "VIP Re-Engager" Tinder-style swipe deck) was retired in the v0 transform; v0 is single-purpose: review reply drafting that feeds the wiki.
- **Multi-tenant auth** — current build supports a single operator per deployment (PocketBase auth, but only one operator row).

### Tech stack

- **Framework**: Next.js 15 (App Router); Server Actions over API routes
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4
- **Backend**: PocketBase (open-source Firebase alternative; PocketHost free tier)
- **AI drafting**: Gemini 2.0 Flash (`gemini-2.0-flash-exp`) via `@google/generative-ai`
- **Wiki integration**: Octokit (commits approved briefs back to the wiki repo with a fine-scoped GitHub PAT, `contents:write` on the wiki repo only)
- **Build-time wiki sync**: `scripts/sync-wiki.ts` reads `wiki/concepts/review-response-templates.md` from the cloned wiki and bakes templates into `src/data/templates.json` so the runtime never depends on a live wiki fetch
- **Tests**: vitest + jsdom

### Where it fits in the wiki's recommendations

- @concepts/reviews-reputation-management.md — Easy Review is the recommended way to operationalize the *response* side of the playbook. Acquisition (asking for reviews) still happens through the booking platform or in-shop signage / QR codes.
- @concepts/review-response-templates.md — Easy Review's category-aware draft is a runtime instantiation of the templates documented in the concept page. The wiki page is the *frame*; Easy Review applies that frame at scale and writes successful drafts back as briefs that future operators can study.
- @concepts/first-90-days-playbook.md — Week 3 (review acquisition + response) is where Easy Review enters the operator's stack, after the GBP foundation (Week 1) + NAP cleanup (Week 2) work.
- @concepts/session-1-facilitator-notes.md — once GBP is captured + claimed in session 1, Easy Review is the natural follow-up tool to introduce in session 2.
- @entities/platforms/google-business-profile.md — once the GBP API integration lands in v1, Easy Review reads from + writes to GBP directly. Until then, the operator copies the review into the form and copies the approved reply back into the GBP dashboard.

### Vertical-agnostic by design

Easy Review accepts a `vertical` field per operator (`barbershop` / `dental` / `salon` / `gym` / `retail` / `restaurant` / `auto_shop` / `other`) and threads it through the Gemini prompt so drafts use the right register. The wiki's response templates are vertical-agnostic; Easy Review respects that.

### Boundary discipline

Easy Review explicitly does NOT:

- Auto-post replies (every send is operator-approved; the only path to a write is the operator's Post click)
- Pre-draft replies for the 1★-likely-fake category (operator decides manually per wiki guidance — emotional engagement with likely-fake reviews is a known trap)
- Gate reviews ("are you happy with us? if yes, leave a Google review; if no, tell us privately" — Google policy violation)
- Generate or solicit fake reviews
- Log customer names from reviews to console or error toasts (PII discipline)

These mirror the boundaries the wiki enforces in @concepts/reviews-reputation-management.md. The tool inherits them by design.

### Current state (2026-05-07)

- v0 implementation merged to `main` on [cemini23/Easy-Review](https://github.com/cemini23/Easy-Review) — repo is intentionally public
- All 23 v0 tasks complete (paste form → categorization → Gemini draft → operator review → brief writeback)
- Live GBP / Yelp / Facebook API integration: v1 (deferred)
- Multi-tenant: deferred
- No production deployment yet — operator can self-host (Vercel/PocketHost) or run locally
- The pre-v0 "VIP Re-Engager" feature (customer CSV upload + slipping-regulars detection + SMS re-engagement) was retired during the v0 transform; the v1 work backed up to `archive/v1-feb-2026` on the same repo for reference

### Why a separate app and not part of the wiki

The wiki is content (markdown). Easy Review is software (app). The concerns are different:

- The wiki accumulates over time; pages don't go stale fast. No build step. Read with any markdown viewer or load into Claude as context.
- Easy Review needs a backend, auth model, API integrations, and a deployable surface. Different lifecycle, different release cadence.

Bundling them would force the wiki into a build/deploy cycle it doesn't need. Keeping them separate also lets the brief-writeback feedback loop work cleanly: app commits to wiki via Octokit; wiki accumulates a real-world corpus over time.

### Phase-0 audit verdict

N/A — Easy Review is built in-house alongside the wiki, not a third-party tool being adopted. The wiki's Phase-0 pattern applies to external tools (Yoast, Local Falcon, Semrush, etc.). Internal companion apps are tracked here for reference but don't need GO/NO-GO scoring.

## Snippets

(none — Easy Review is internal, not yet citable from external research)
