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
  - sweeps/2026-06-04-daily.md
  - sources/bespoke-2025-search-augmented-personalization-benchmark.md
  - sources/ptah-2026-verifiable-multimodal-deep-research.md
  - sources/memento-2026-web-learning-signal-low-data.md
  - sources/score-2026-self-evolving-deep-research.md
  - sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md
  - sources/arxiv-webknograph-internal-linking-2606.06106-2026-06-05.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - sweeps/2026-06-05-daily.md
  - sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md
  - concepts/citation-verification-aeo.md
  - sweeps/2026-06-06-daily.md
  - sweeps/2026-06-07-daily.md
  - sources/arxiv-caption-injection-2511.04080-2026-06-08.md
  - sweeps/2026-06-08-daily.md
  - sweeps/2026-06-09-daily.md
  - sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md
  - sources/arxiv-hu-2025-adversarial-attacks-llm-search-2501.00745-2026-06-10.md
  - concepts/geo-visibility-measurement.md
  - sweeps/2026-06-10-daily.md
  - sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md
  - sources/arxiv-yuan-2026-flowbank-agentic-workflows-2606.11290-2026-06-16.md
  - sources/arxiv-zhu-2026-deeprubric-evidence-tree-2606.17029-2026-06-16.md
  - concepts/llm-reputation-signals-geo.md
  - sweeps/2026-06-16-daily.md
  - entities/tools/flowbank.md
  - entities/tools/deeprubric-code.md
  - sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md
  - entities/tools/wikikv.md
  - sweeps/2026-06-17-daily.md
  - sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md
  - concepts/llm-brand-bias-geo-competition.md
  - sweeps/2026-06-18-daily.md
  - sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md
  - entities/tools/ranqo.md
  - sweeps/2026-06-19-daily.md
  - sweeps/2026-06-20-daily.md
  - sweeps/2026-06-21-daily.md
  - sweeps/2026-06-22-daily.md
  - concepts/citation-verification-aeo.md
  - concepts/agent-first-web-atml-framework.md
  - concepts/near-me-search.md
maturity: draft
created: 2026-06-01
updated: 2026-06-22
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
- @sources/memento-2026-web-learning-signal-low-data.md — procedural memory analog for recurring digest queries
- @sources/score-2026-self-evolving-deep-research.md — digest outputs lack ground truth (same structural problem as deep-research reports)
- @sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md — skim vs deep-pass routing for morning ingest
- @concepts/adaptive-rag-internal-linking-geo.md — query-complexity routing tree
- @sweeps/2026-06-04-daily.md — 2026-06-04 ingest (MEMENTO + SCORE)
- @sweeps/2026-06-05-daily.md — 2026-06-05 ingest (adaptive RAG + WebKnoGraph)
- @sweeps/2026-06-06-daily.md — 2026-06-06 ingest (Med-V1 evidence attribution)
- @sweeps/2026-06-07-daily.md — empty inbox (dupes only)
- @sources/arxiv-caption-injection-2511.04080-2026-06-08.md — 2026-06-08 ingest (Caption Injection multimodal G-SEO)
- @sweeps/2026-06-08-daily.md — overnight fetch + Caption Injection ingest
- @sweeps/2026-06-09-daily.md — empty inbox (dupes only)
- @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md — 2026-06-10 ingest (AI visibility uncertainty)
- @sources/arxiv-hu-2025-adversarial-attacks-llm-search-2501.00745-2026-06-10.md — 2026-06-10 ingest (LLM search manipulation game theory)
- @concepts/geo-visibility-measurement.md — measurement playbook from Sielinski paper
- @sweeps/2026-06-10-daily.md — overnight fetch + dual arXiv ingest
- @sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md — 2026-06-16 ingest (hotel reputation audit)
- @sources/arxiv-yuan-2026-flowbank-agentic-workflows-2606.11290-2026-06-16.md — 2026-06-16 ingest (FlowBank REFERENCE)
- @sources/arxiv-zhu-2026-deeprubric-evidence-tree-2606.17029-2026-06-16.md — 2026-06-16 ingest (DeepRubric REFERENCE)
- @concepts/llm-reputation-signals-geo.md — K120 operator playbook
- @sweeps/2026-06-16-daily.md — overnight fetch + K120 full ingest
- @sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md — K121 hierarchical wiki storage REFERENCE
- @entities/tools/wikikv.md
- @sweeps/2026-06-17-daily.md — overnight fetch + K121 ingest
- @sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md — K122 incumbent brand bias / GEO competition audit
- @concepts/llm-brand-bias-geo-competition.md — operator playbook
- @sweeps/2026-06-18-daily.md — overnight fetch + K122 ingest
- @sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md — K123 Ranqo production GEO baseline
- @entities/tools/ranqo.md
- @osint-wiki/sources/arxiv-scholarquest-agentic-academic-search-2606.20235-2026-06-19.md — K123 cross-wiki: agentic literature search benchmark
- @sweeps/2026-06-19-daily.md — overnight fetch + K123 ingest
- @osint-wiki/sources/arxiv-metaresearcher-deep-research-2606.19893-2026-06-20.md — K124 cross-wiki: adversarial deep-research RL framework
- @osint-wiki/entities/tools/metaresearcher.md — Phase-0 REFERENCE entity
- @sweeps/2026-06-20-daily.md — overnight fetch + K124 ingest (ScholarQuest re-archive)
- @concepts/citation-verification-aeo.md — adversarial misinformation audit steal
- @concepts/agent-first-web-atml-framework.md — CCC K119 cross-route stub
- @game-dev-wiki/sources/arxiv-na-2026-binary-tracking-spatial-qa-2606.16902-2026-06-21.md — K125 cross-wiki: BinTrack spatial QA (route-query pattern analog)
- @sweeps/2026-06-21-daily.md — overnight fetch + K125 ingest (2 duplicate re-archives)
- @sweeps/2026-06-22-daily.md — overnight fetch + K126 duplicate-only batch

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

### Ingest depth routing [TENTATIVE]

@sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md — overnight digest fetch is **single-pass retrieval** (correct). Morning Cursor sessions should default to **skim ingest** (abstract + intro → source stub) and run **deep pass** only when operator requests or paper maps to active ROADMAP workstream. Multi-hop cross-paper synthesis degrades ranking precision when over-decomposed; prefer `@relation` following over blind sub-query splitting. Full routing tree: @concepts/adaptive-rag-internal-linking-geo.md Part A.

## Snippets

> "Each sibling wiki gets a copy of the script bundle… plus a wiki-local daily_research_config.yaml with domain active_topics." [Source: @osint-wiki/concepts/federated-daily-research-digest.md (retrieved 2026-06-01)]
