---
title: Marketing Skills (Claude Code Agent Skill)
type: entity
tags: [seo-tooling, ai-content-tool, claude-code-skill, copywriting, social-media-copy]
keywords: [marketing skills, claude code plugin, brand voice, PAS framework, product marketing context, localized content]
related:
  - sources/github-repo-audit-2026-05-07.md
  - concepts/content-strategy-local.md
  - concepts/social-media-for-barbershops.md
  - concepts/review-response-templates.md
  - concepts/claude-platforms.md
  - concepts/generative-engine-optimization.md
  - entities/tools/seomachine.md
maturity: validated
created: 2026-05-07
updated: 2026-05-07
---

## Relations

- @sources/github-repo-audit-2026-05-07.md
- @concepts/content-strategy-local.md
- @concepts/social-media-for-barbershops.md
- @concepts/review-response-templates.md
- @concepts/claude-platforms.md
- @concepts/generative-engine-optimization.md
- @entities/tools/seomachine.md

## Raw Concept

Adopted via Phase-0 audit on 2026-05-07 (verdict: GO). See @sources/github-repo-audit-2026-05-07.md.

- **Repo**: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
- **License**: MIT
- **Type**: Claude Code Agent Skill bundle (markdown files loaded into Claude Code CLI)
- **Stars**: ~19K
- **Last commit**: 2026-04-23 (active)
- **Install path**: `/plugin install marketing-skills` inside Claude Code

## Narrative

Marketing Skills is a curated set of marketing-framework prompts/skills designed to make Claude (or other AI agents that support the agentskills.io spec) operate as a competent marketing collaborator rather than a generic copywriter. Its core insight is that AI marketing output goes wrong in predictable ways — generic, off-brand, ignores audience pain points, lacks framework structure — and these failures are fixable by enforcing a **product-marketing-context file** that every other skill consults before drafting anything.

### How it helps the operator

For a Davie barbershop, this means:

1. **One-time setup**: define the `product-marketing-context` file with the shop's positioning (Davie barbershop, Hispanic+Caribbean cultural fluency, fade-specialty, two-shop network, etc.), audience (working professionals + university students at NSU + traditional barbershop regulars), differentiators, and brand voice. This becomes the substrate for every subsequent skill invocation.
2. **Recurring use**: tasks like "draft an Instagram caption for this fade photo," "write a 3-touch email reactivation sequence for lapsed customers," "respond to this Google review using PAS framework" — Claude Code consults the context file first, applies the named framework, and produces output that's on-brand and on-message rather than generic.

### Frameworks included (representative — verify against current repo)

- **PAS** (Problem → Agitate → Solve) for ad copy and longer captions
- **AIDA** (Attention → Interest → Desire → Action) for funnel content
- Email sequence templates (welcome, win-back, post-visit follow-up)
- Social-post templates by platform (IG vs TikTok vs FB tonal differences)
- Review-response frameworks (cross-references our @concepts/review-response-templates.md)

### Install and use

```
# Inside Claude Code, after Claude Code is installed and authenticated:
/plugin install marketing-skills
```

This is **a Claude Code plugin, NOT a Claude Desktop MCP server**. The friend uses Claude Desktop today; for this skill to work he also needs Claude Code installed (separate CLI app). See @concepts/claude-platforms.md.

### Failure modes to watch for

- **Stale product-marketing-context file** — if the shop adds a new service, hires new staff, opens a new location, or changes pricing strategy, the context file must be updated. Otherwise the skill produces outdated copy.
- **Over-reliance** — the skill drafts; the operator still reads, edits, and posts. This is not auto-pilot. Review-response auto-posting is explicitly forbidden by @concepts/reviews-reputation-management.md.
- **Mixing brand voices for two shops** — if Shop 1 and Shop 2 have different brand identities (per @entities/companies/shop-2.md "Relationship to Shop 1" decision), the operator may need two context files or one file with shop-specific subsections.

### Why this beat parallel implementations

Per the audit (@sources/github-repo-audit-2026-05-07.md), [dageno-agents/seo-geo-content-engine](https://github.com/dageno-agents/seo-geo-content-engine) was rejected as a parallel implementation despite organizational pedigree, because (a) unknown license and (b) marketingskills already covers the use case. Workspace policy prefers one well-adopted tool per niche over multiple overlapping ones.

## Snippets

> "Skills are markdown files that provide AI agents with specialized knowledge and frameworks... All other skills check the product-marketing-context file first to understand the specific product, audience, and positioning before performing tasks." [Source: github-repo-audit-2026-05-07 — marketingskills section]
