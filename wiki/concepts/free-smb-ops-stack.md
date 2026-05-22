---
title: Free Open-Source SMB Operations Stack
type: concept
tags: [smb, tooling, open-source, cost-reduction]
keywords: [akaunting, faveo helpdesk, laracom, free smb stack, quickbooks alternative]
related:
  - entities/tools/saas-boilerplate.md
  - concepts/claude-ecommerce-workflows.md
maturity: draft
created: 2026-05-22
updated: 2026-05-22
cross-wiki-source: "@osint-wiki/sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md"
---

## Relations

- @entities/tools/saas-boilerplate.md
- @concepts/claude-ecommerce-workflows.md

## Raw Concept

Routed from `briefs/2026-05-21_k55-2-ridark-eth-seo-relevant-repos.md` (K55-2). Bundles three FOSS replacements for common paid SMB SaaS — accounting, helpdesk, e-commerce — as a **cost-reduction stack** for operators running adjacent businesses (agency, merch, productized services). Not core to barbershop day-one local SEO; reference when the operator asks "what free tools replace QuickBooks/Zendesk/Shopify?"

## Narrative

| Tool | Repo | Replaces | Notes |
|------|------|----------|-------|
| Akaunting | `akaunting/akaunting` | QuickBooks (accounting) | Self-hosted; ops overhead vs SaaS convenience |
| Faveo Helpdesk | `faveosuite/faveo-helpdesk` | Zendesk (support) | Ticket workflow for multi-location or agency clients |
| Laracom | `jsdecena/laracom` | Shopify (storefront) | Laravel e-commerce; eliminates Shopify monthly + transaction cut |

All three are **[TENTATIVE]** — sourced from an unaudited @ridark_eth list (K52 misrepresentation incident noted on author entity in OSINT). Phase-0 audit each before adoption: license, security update cadence, hosting requirements, PCI/payment compliance for Laracom.

**Deferred from same brief (index-only, not entity pages):**
- `DigitalPlatDev/FreeDomain` — free domains for test landings; **PBN-adjacent** — contested SEO tactic; wiki has no PBN playbook; do not adopt without explicit operator policy
- `certimate-go/certimate` — ACME SSL automation; catalog under Tools — reference-only if needed for multi-client site ops
- Crawlers (`firecrawl`, `crawl4ai`, `jina-ai/reader`, `docling`) — primary home @osint-wiki; defer duplicate entity stubs here

## Snippets

(none — unaudited list; verify repos before quoting README claims)
