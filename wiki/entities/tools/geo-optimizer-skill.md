---
title: geo-optimizer-skill — open-source AEO/GEO audit CLI (Auriti-Labs)
type: entity
tags: [tool, geo-aeo, foss, cli, mcp, k134]
keywords: [Auriti-Labs, geo-optimizer-skill, AEO, GEO audit, llms.txt, MCP, PyPI]
related:
  - concepts/generative-engine-optimization.md
  - entities/tools/geo-seo-claude.md
  - entities/tools/seo-geo-claude-skills.md
  - entities/tools/google-search-console.md
  - concepts/geo-visibility-measurement.md
  - concepts/schema-markup-local.md
  - sources/aggarwal-2024-geo-paper.md
  - sources/techwyse-2026-google-good-seo-is-good-geo-kraham-2026-06.md
  - sources/google-search-central-2026-ai-optimization-guide.md
  - sources/housingwire-2026-answer-engine-optimization-zero-click-gbp-2026-06-29.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-30-daily.md
maturity: draft
created: 2026-06-30
updated: 2026-07-02
---

## Relations

- @concepts/generative-engine-optimization.md — GEO/AEO tool stack
- @entities/tools/geo-seo-claude.md — adopted Claude Code GEO skill (GO 2026-05-07); complementary audit CLI
- @entities/tools/seo-geo-claude-skills.md — Steal-from pattern reference
- @entities/tools/google-search-console.md — first-party AI performance when available
- @concepts/geo-visibility-measurement.md — third-party citation scores need CI discipline
- @concepts/schema-markup-local.md — JSON-LD checks in audit
- @sources/aggarwal-2024-geo-paper.md — cited in tool docs (KDD 2024 methods)
- @sources/techwyse-2026-google-good-seo-is-good-geo-kraham-2026-06.md — **ignore llms.txt push** for Google Search
- @sources/google-search-central-2026-ai-optimization-guide.md — first-party llms.txt mythbust `[CONFIRMED]`
- @sources/housingwire-2026-answer-engine-optimization-zero-click-gbp-2026-06-29.md — zero-click / citation KPI framing
- @concepts/federated-daily-research-digest.md — K134 sweep fetch
- @sweeps/2026-06-30-daily.md — overnight Exa hit

## Raw Concept

Phase-0 from K134 ingest — [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) (MIT, ~508★, last push 2026-06-27). PyPI package `geo-optimizer-skill`; CLI + Python API + MCP server; hosted SaaS at geoready.dev (separate product audit).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | github.com/Auriti-Labs/geo-optimizer-skill |
| **License** | MIT |
| **Category** | GEO/AEO audit CLI — robots.txt, schema, citability scoring, optional live citation probes |
| **Phase-0 verdict** | **CONDITIONAL-GO** — local CLI audit only; do not treat `geo citations` as ground truth without bootstrap CIs (@concepts/geo-visibility-measurement.md) |
| **Steal** | 8-category AI-readiness audit; schema/citability modules; MCP hook for Cursor |
| **Reject module** | **`llms.txt` generation/checks for Google Search** — @sources/google-search-central-2026-ai-optimization-guide.md: not used by Google Search generative features `[CONFIRMED]` |
| **Compare** | @entities/tools/geo-seo-claude.md (Claude skill, installed); @entities/tools/ranqo.md (SaaS mention tracking REFERENCE) |
| **Operator install** | `uvx --from geo-optimizer-skill geo audit --url https://yoursite.com` — laptop-only; no GBP write access |

Do not bulk-automate GBP posts or review flows through this tool — audit/read-only surfaces only.

## Snippets

> "One command scores your site 0–100 on AI-search readiness… and checks whether AI engines actually cite you." [Source: github.com/Auriti-Labs/geo-optimizer-skill README (retrieved 2026-06-30)]

> "1720 tests" / MIT license / MCP compatible. [Source: github.com/Auriti-Labs/geo-optimizer-skill (retrieved 2026-06-30)]
