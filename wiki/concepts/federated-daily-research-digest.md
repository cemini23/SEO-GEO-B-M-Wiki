---
title: Federated daily research digest — SEO wiki learning loop
type: concept
tags: [meta, automation, federation, geo-search, geo-aeo]
keywords: [federated-digest, daily-research, exa, inbox-watcher, gbp, local-seo]
related:
  - meta/daily-research-digest-cadence.md
  - concepts/generative-engine-optimization.md
  - concepts/google-business-profile.md
  - concepts/obsidian-integration.md
  - sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md
  - sweeps/2026-06-01-daily.md
  - sweeps/2026-06-02-daily.md
  - sweeps/2026-06-03-daily.md
  - sources/bespoke-2025-search-augmented-personalization-benchmark.md
  - sources/ptah-2026-verifiable-multimodal-deep-research.md
maturity: draft
created: 2026-06-01
updated: 2026-06-04
cross-wiki-source: "@osint-wiki/concepts/federated-daily-research-digest.md"
---

## Relations

- @meta/daily-research-digest-cadence.md — operator cadence + LaunchAgent label for this repo
- @concepts/generative-engine-optimization.md — GEO/AEO queries in digest config
- @concepts/google-business-profile.md — GBP policy + feature drift queries
- @concepts/obsidian-integration.md — sweep markdown lands in vault alongside wiki pages
- @sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md
- @sources/bespoke-2025-search-augmented-personalization-benchmark.md
- @sources/ptah-2026-verifiable-multimodal-deep-research.md — same K93 brief batch as digest rollout

## Raw Concept

Routed from `briefs/2026-06-01_k93-seo-digest-goaccess-from-osint.md`. Replicates the OSINT morning digest pattern for this wiki: automated Exa discovery + optional arXiv fetch into `research to be indexed/`, sweep report at `wiki/sweeps/YYYY-MM-DD-daily.md`. **Tier 3 auto-ingest remains NO-GO** — Cursor sessions still run the ingest workflow from inbox drops.

## Narrative

### Repo-local stack (2026-06-01)

| Piece | Path |
|-------|------|
| Config | `scripts/daily_research_config.yaml` |
| Runner | `scripts/daily_research_digest_run.py` |
| Fetch helper | `scripts/daily_research_fetch.py` |
| Report | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| Inbox | `research to be indexed/` |

Canonical federation docs: @osint-wiki/concepts/federated-daily-research-digest.md.

### Install (operator hands-on)

```bash
bash "/Users/claudiobarone/Desktop/OSINT WORKSPACE/scripts/federation/daily_digest/install_federated_daily_digest.sh" \
  "/Users/claudiobarone/Desktop/projects/SEO:GEO B&M Business" seo
```

Creates `~/bin/cemini-daily-research-digest-seo` + LaunchAgent `com.cemini.daily-research-digest.seo` (08:15 local). Requires `.env` Exa key per `.env.example`.

### Active topic lanes

Configured in `scripts/daily_research_config.yaml`: GBP policy/features, GEO/AEO citation surfaces, local-pack practitioner news, review acquisition/response, and B&M web stack (schema, CWV, GA4/GSC). Bump `active_topics` when @ROADMAP.md workstreams shift.

### Human gates

1. Digest writes **sweeps + inbox only** — never entity/concept pages
2. Morning Cursor session: triage inbox → discuss takeaways → ingest per @CLAUDE.md
3. After meaningful commits: optional `rsync` + `kb ingest` on cemini-librarian (existing federation sync)

## Snippets

> "Each sibling wiki gets a copy of the script bundle… plus a wiki-local daily_research_config.yaml with domain active_topics." [Source: @osint-wiki/concepts/federated-daily-research-digest.md (retrieved 2026-06-01)]
