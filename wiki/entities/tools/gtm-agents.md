---
title: "gtm-agents — GTM/sales/marketing Claude Code skill suite [seo cross-route stub]"
type: entity
category: tool
tags: [entity, tool, claude-code-skill-pack, gtm-automation, sales-marketing, social-media-automation, k44, skip-phase-0-2026-05-14, misaligned-30-day-revenue-plan]
keywords: [gtm-agents, marketing-workflows, customer-success-skills, creator-marketing, social-media-automation, apache-2-license, single-author-risk, enterprise-scale-mismatch]
related: []
maturity: validated
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @ccc-wiki/entities/tools/gtm-agents.md — CCC-side primary entity (skill-pack distribution model)

## Raw Concept

K44 cross-route from CCC to SEO: gtm-agents' **marketing and social-media automation skills**. Apache-2.0 production-ready Claude Code skill pack for sales, marketing, customer-success workflows. **Stars NOT FOUND in K44 doc-level eval — Phase-0 priority gate**.

## Narrative

For SEO-wiki, the gtm-agents value is the **creator marketing + social media automation subset** — overlaps with the 30-day GEO/AEO + Polymarket newsletter revenue plan's marketing-automation needs.

### Phase-0 audit verdict (2026-05-14): SKIP

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo discovery | **PASS** | `gtmagents/gtm-agents` resolved (top search result) |
| G1 | Star + maturity | **CONDITIONAL** | 206★ (K44 missed the count — minor), Apache-2.0, BUT 6-month-old (created 2025-11-18), **99% single-author** (gtmagents org only, 5 commits), 98 open issues |
| G2 | License | **PASS** | Apache-2.0 verbatim |
| G3 | Skill pack structure | **PASS** | 69 plugins / 244 skills with Claude Code-conformant YAML frontmatter + `/plugin install` pattern |
| G4 | Creator/social subset | **PARTIAL** | 7 social skills + 6 email + 7 content. **Missing newsletter audience-building, AEO/GEO-specific skills** |
| G5 | vs SEO-wiki existing | **SUPPLEMENT-ONLY, NOT REPLACE** | gtm-agents (244 skills, enterprise) vs marketingskills.md (19K★, SMB/boutique). Non-overlapping; **marketingskills.md remains primary** (50x scale gap; different audience tier) |
| G6 | Install pattern | **PASS** | `/plugin marketplace add gtmagents/gtm-agents` |
| G7 | Cost profile | **OPAQUE** | "100-500 tokens/command" claim with no per-skill budgets; data-enrichment-master orchestration likely expensive; caching/batching undocumented |
| G8 | Failure modes | **HIGH-RISK** | Single-author abandonment risk + cold-outreach skills lack GDPR/CCPA/EU-AI-Act guardrails + 6mo-old playbooks with no update cadence + hallucination risk in data-enrichment proxy |
| G9 | 30-day revenue plan fit | **NO FIT** | Missing newsletter audience-building, AEO/GEO positioning, Polymarket-specific workflows. Cold outreach exists but with compliance risk |

**Verdict: SKIP for K44 adoption.** Misaligned with the OSINT workspace's 30-day revenue plan (GEO/AEO audits + Polymarket newsletter).

### Comparison table

| Dimension | marketingskills.md (19K★) | gtm-agents (206★) | Verdict |
|-----------|---------------------------|-------------------|---------|
| Scale | ~5 skills (boutique/SMB) | 244 skills (enterprise GTM) | 50x scale gap; different tier |
| Context-driven | YES (product-marketing-context file) | NO (standalone skills) | marketingskills wins on integration |
| Newsletter/audience | Templates only | Indirect (email segmentation, channel roadmap) | **Both gap** |
| AEO/GEO | NO | NO | **Both missing — critical gap to fill custom** |
| Cold outreach | NO | YES (no compliance guardrails) | Skip gtm-agents version |
| Maintenance | MIT, active, 19K stars | Apache-2.0, single-author, 98 open issues | marketingskills wins decisively |

### Recommended action (instead of adoption)

1. **Keep `marketingskills.md`** as primary SEO/marketing skill reference for SMB/Polymarket use case
2. **Build 2-3 custom skills** to fill the actual 30-day-revenue-plan gaps:
   - Newsletter audience expansion + monetization (Polymarket tie-in)
   - AEO/GEO positioning for prospect acquisition
   - Compliance-safe cold outreach (EU/CA AI Act guardrails)
3. **Reference-only** lookups from gtm-agents (cold-outreach + social-calendar-system) as tactical examples — but do NOT depend on the repo for delivery (single-author + compliance risk)

See @ccc-wiki/entities/tools/gtm-agents.md for the matching CCC-side Phase-0 record.

## Snippets

> "Concurrently, it delivers highly deployable operational logic that fulfills the SEO-wiki's requirements for creator marketing and social media automation."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶313]
