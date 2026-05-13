---
title: "ai-marketing-skills — Claude Skill bundle for marketing"
type: entity
tags: [tool, claude-skills, marketing, ai-skills, pii-sanitizer, skill-md-schema, mit]
keywords: [ai-marketing-skills, skill.md schema, pii sanitizer hook, marketing automation, mit]
related:
  - "@osint-wiki/entities/tools/ai-marketing-skills.md"
  - "@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md"
  - entities/tools/marketingskills.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
osint_eval_origin: doc1-url-13 (cross-routed; SEO primary)
---

## Relations

- `@osint-wiki/entities/tools/ai-marketing-skills.md` — OSINT cross-route
- `@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md` — origin eval (URL 13)
- `@entities/tools/marketingskills.md` — existing sibling skill bundle

## Raw Concept

- **License**: MIT
- **Tier**: Steal-from / Adopt-candidate (extends marketingskills.md)

## Narrative

Claude Skill bundle for marketing workflows. Two extractable patterns: (1) SKILL.md schema for declarative skill definitions, (2) PII sanitizer pre-hook for any user-input-containing skill. Direct extension target for our existing `marketingskills.md` entry. SKILL.md schema reuse compounds across our entire skill catalog.

### Integration vector

1. Compare ai-marketing-skills' SKILL.md fields against ours; pull useful schema additions
2. Adopt the PII sanitizer pre-hook pattern for any skill that ingests user content (review responses, social media drafts, etc.)
