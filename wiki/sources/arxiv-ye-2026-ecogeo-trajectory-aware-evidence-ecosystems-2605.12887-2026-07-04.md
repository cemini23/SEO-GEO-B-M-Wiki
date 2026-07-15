---
title: "Ye 2026 - EcoGEO trajectory-aware evidence ecosystems (arXiv 2605.12887)"
type: source
tags: [source, arxiv, geo-aeo, agentic-search, internal-linking, k138]
keywords: [2605.12887, EcoGEO, TRACE, evidence ecosystem, web-enabled LLM agents, internal links, trajectory]
related:
  - concepts/evidence-ecosystem-geo.md
  - concepts/generative-engine-optimization.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/geo-visibility-measurement.md
  - concepts/content-strategy-local.md
  - concepts/citation-building.md
  - sources/google-search-central-2026-ai-optimization-guide.md
  - sources/arxiv-webknograph-internal-linking-2606.06106-2026-06-05.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-04-daily.md
  - sources/arxiv-geng-2026-deepsearch-world-self-distillation-2607.07820-2026-07-15.md
  - concepts/process-verified-agentic-search-geo.md
maturity: validated
read_status: read
created: 2026-07-04
updated: 2026-07-15
---

## Relations

- @concepts/evidence-ecosystem-geo.md - operator playbook distilled from EcoGEO
- @concepts/generative-engine-optimization.md - GEO/AEO hub
- @concepts/adaptive-rag-internal-linking-geo.md - internal-link and agent trajectory analog
- @concepts/ai-citation-sourcing-geo.md - source layer before answer layer
- @concepts/geo-visibility-measurement.md - trajectory metrics beyond mention/citation
- @concepts/content-strategy-local.md - hub and support-page architecture
- @concepts/citation-building.md - ethical earned evidence outside owned site
- @sources/google-search-central-2026-ai-optimization-guide.md - Google query fan-out + no AI hacks baseline
- @sources/arxiv-webknograph-internal-linking-2606.06106-2026-06-05.md - graph/internal-link predeploy evaluation
- @concepts/federated-daily-research-digest.md - K138 ingest routing
- @sweeps/2026-07-04-daily.md - overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Search Agents |
| **Authors** | Hengwei Ye, Jiasheng Mao, Zhenhan Guan, Zheng Tian (ShanghaiTech University) |
| **arXiv** | 2605.12887v2 |
| **Filename** | `arxiv-2605.12887-ecogeo-trajectory-aware-evidence-ecosystems-for.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2605.12887-ecogeo-trajectory-aware-evidence-ecosystems-for.pdf` |
| **Retrieved** | 2026-07-04 |
| **Read status** | read (abstract, intro, method, results, limitations, ethics) |

## Narrative

EcoGEO argues that GEO for web-enabled agents is not only a **single-page rewrite** problem. Agents issue searches, crawl results, follow links, reformulate queries, and synthesize evidence over a browsing **trajectory**. Visibility can therefore depend on whether the brand's pages form a coherent evidence environment.

### TRACE method

TRACE (Trajectory-Aware Coordinated Evidence Ecosystem) builds a synthetic product evidence graph:

- **Navigation entry page** - agent-facing guide/review/comparison surface that introduces the target as a candidate and links to supporting evidence.
- **Role-specialized support pages** - official, review, expert, news, forum, and social-style pages.
- **Attribute consistency** - stable product name, category, features, use cases, and limitations across source styles.
- **Cross-page references** - links among support pages so an agent can traverse the evidence ecosystem after first crawl.

### Results

On OPR-Bench (3,124 query-product pairs; controlled synthetic product setup), TRACE beat single-page and page-level GEO baselines:

| Dataset | Best baseline target recommendation | TRACE | Lift |
|---------|-------------------------------------|-------|------|
| SafeSearch | 35.9% | 67.2% | +31.3 pp |
| E-Commerce | 56.2% | 71.9% | +15.7 pp |
| E-GEO | 59.0% | 73.9% | +14.9 pp |

Trajectory metrics rose too: initial target-result crawls, target-specific second searches, and internal-link crawls. In ablations with forced initial exposure, coordinated pages beat uncoordinated pages, and TRACE's navigation entry beat a review-style entry; internal-link crawl rose to **29.7%** (SafeSearch) and **25.6%** (E-Commerce).

### Operator translation `[TENTATIVE]`

For a local business, the safe analog is **not** fabricating multi-source evidence. It is making real evidence easier for agents to traverse:

- Website service/location hub links to per-service proof, team bios, pricing/hours, gallery, and FAQs.
- GBP, Yelp, Apple Maps, Bing Places, chamber/listicles, and local press use consistent NAP/category/service language.
- Review themes and service pages use the same real vocabulary customers use.
- Internal links point from broad "barbershop in [city]" pages to concrete evidence pages (fade, beard trim, kids cuts, walk-ins, parking).

### Safety boundary

The authors explicitly used fictional products in a controlled, non-public environment and state they do **not** advocate applying TRACE to public web platforms. Treat the paper as a measurement and architecture lens, not a green light for synthetic review/forum/social pages.

**Phase-0:** REFERENCE - academic paper; no tool adoption. Ethical boundary: do not publish fabricated support pages. Hands-on: `briefs/2026-07-04_k138-evidence-ecosystem-geo-audit-hands-on.md`.

## Snippets

> "EcoGEO complements page-level GEO by situating individual pages within the larger evidence ecosystem in which web-enabled agents search, browse, and synthesize information."

> "The support pages Vs are designed to sustain the target product's presence after the agent encounters the entry page."

> "This controlled setup is intentional for both methodological and ethical reasons."

> "We do not advocate applying these techniques to real systems or public web platforms."

[Source: arxiv-2605.12887v2 (retrieved 2026-07-04)]
