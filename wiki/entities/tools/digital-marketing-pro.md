---
title: Digital Marketing Pro — Claude Plugin Ecosystem
type: entity
tags: [tool, marketing-analytics, claude-plugin, mcp, geo-aeo, qa-verification]
keywords: [digital marketing pro, claude plugin, mcp server, marketing analytics, qa verification, geo, aeo]
related:
  - "@osint-wiki/entities/tools/digital-marketing-pro.md"
  - concepts/generative-engine-optimization.md
  - entities/tools/marketingskills.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/entities/tools/digital-marketing-pro.md"
---

## Relations

- @osint-wiki/entities/tools/digital-marketing-pro.md — cross-wiki source (OSINT-wiki entity stub)
- @concepts/generative-engine-optimization.md — QA/claim-verification layer directly applicable to GEO/AEO content pipelines
- @entities/tools/marketingskills.md — sibling marketing skill bundle for Claude Code

## Raw Concept

Cross-wiki brief routed from `@osint-wiki/sources/evaluating-code-for-trading-stacks.md`. The OSINT wiki encountered `github.com/indranilbanerjee/digital-marketing-pro` during a trading-stack tool evaluation and rejected it for that domain — but it is directly on-topic for the SEO/GEO wiki.

## Narrative

A massive Claude-plugin ecosystem built to convert Claude into a full-stack digital marketing intelligence system.

- **115 distinct commands** spanning the full marketing analytics + intelligence workflow
- **67 separate MCP servers** — likely the largest single MCP catalog in the marketing domain at time of ingest
- **5-layer memory architecture**: session context → RAG/vector DB (Pinecone, Qdrant) → temporal knowledge graphs (Graphiti) → universal memory → file-based knowledge bases
- **v3.0 QA/evaluation layer**: hallucination detection, claim verification, output validation, A+→F grading
- **Safety enforcement**: `disable-model-invocation: true` flags demand explicit human-in-the-loop approval before write actions to external platforms
- **External integrations**: Salesforce, HubSpot, plus marketing-platform APIs

### SEO/GEO relevance

- **GEO/AEO content validation** — the QA + claim-verification layer is exactly the kind of validation discipline GEO/AEO content needs before publishing
- **67 MCP server templates** — highest-density reference catalog for marketing-domain MCP tools
- **Human-in-the-loop write gates** — the `disable-model-invocation: true` pattern is directly applicable to GBP / social-media posting workflows
- **Salesforce/HubSpot connectors** — direct relevance for CRM-integrated workflows

### Recommended next actions

1. Phase-0 audit: verify MIT license [NEEDS VERIFICATION 2026-05-21], check repo maturity
2. Inventory the 67 MCP servers — marketing-domain specific vs generic
3. Extract QA/claim-verification scripts as building blocks for GEO/AEO content-pipeline veto gate
4. Reference but do NOT deploy the full 5-layer memory stack (Pinecone + Graphiti = heavy infra)

[NEEDS VERIFICATION 2026-05-21] license, repo URL, stars, commit cadence.
