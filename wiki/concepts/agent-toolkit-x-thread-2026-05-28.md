---
title: Agent toolkit X thread — May 2026
type: concept
tags: [social, x-twitter, open-source, agent-tooling]
keywords: [vet, phase0, wikilint, cemini23, agent skills, CI]
related:
  - concepts/x-account-voice-and-format.md
  - concepts/x-article-3-notes.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/x-account-voice-and-format.md — X voice + Article paste protocol
- @concepts/x-article-3-notes.md — Article #3 ties toolkit to contribution rate

## Raw Concept

Source material for an X post/thread promoting the cemini23 open-source agent toolkit (vet, phase0, wikilint, demo, ara-schema). Synthesized from OSINT workspace OSS agent toolkit roadmap (`docs/oss-agent-toolkit-roadmap.md`).

## Narrative

### Hook options

- "Your agent skills ship with TODOs and broken frontmatter. We open-sourced the veto gate we use on 100+ internal briefs."
- "LLM wikis die from orphan pages and one-way links. We fixed it with stdlib CI you can fork in 2 minutes."

### Stack (one tweet each)

| Tool | One-liner | URL |
|------|-----------|-----|
| **vet** | Static audit for SKILL.md, briefs, runbooks — veto gates, stdlib-only | https://github.com/cemini23/vet |
| **phase0** | Phase-0 audit before adopting MCP/skill repos; `verify-eval` catches license lies | https://github.com/cemini23/phase0 |
| **wikilint** | Orphans, bidirectional gaps, dangling `@paths`, stale verification tags | https://github.com/cemini23/wikilint |
| **agent-toolkit-demo** | Copy-paste GitHub Actions — green badges, bad artifacts fail on purpose | https://github.com/cemini23/agent-toolkit-demo |
| **ara-schema** | Wiki page contract — structure only, content stays private | https://github.com/cemini23/ara-schema |

### Proof points

- Battle-tested on internal brief/skill workflows before OSS
- Stdlib Python, composite GitHub Actions, no API keys
- Deliberately closed: trading stack, prod MCP, raw research corpuses

### CTAs

- Fork the demo repo before your next skill PR
- Star vet for PyPI polish
- Reply with your worst skill anti-pattern

### Hashtags

`#ClaudeCode` `#Cursor` `#MCP` `#AgentSkills` `#DevTools` `#OpenSource`
