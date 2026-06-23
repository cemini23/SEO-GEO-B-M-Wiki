---
title: "Varga 2026 — Per-Entity Bias Mapping for AI visibility (arXiv 2606.21595)"
type: source
tags: [source, arxiv, geo-aeo, measurement, entity-audit, k127]
keywords: [2606.21595, PEBM, Brand Hallucination Paradox, verified mention, ghost cartography, canonical presence]
related:
  - concepts/per-entity-bias-mapping-geo.md
  - concepts/geo-visibility-measurement.md
  - concepts/citation-verification-aeo.md
  - concepts/generative-engine-optimization.md
  - concepts/llm-brand-bias-geo-competition.md
  - sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md
  - sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md
  - sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md
  - concepts/competitive-geo-citation-factors.md
  - entities/tools/ranqo.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-23-daily.md
maturity: validated
read_status: read
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- @concepts/per-entity-bias-mapping-geo.md — operator playbook hub
- @concepts/geo-visibility-measurement.md — raw vs verified mention complements citation-share CI discipline
- @concepts/citation-verification-aeo.md — claim–source alignment; PEBM citation fidelity dimension
- @concepts/generative-engine-optimization.md — parent GEO hub
- @concepts/llm-brand-bias-geo-competition.md — Brand Hallucination Paradox vs Conditional Monopoly under ties
- @sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md — production mention-rate baselines need PEBM calibration
- @sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md — brand default under ambiguity
- @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md — bootstrap CI on share; PEBM adds entity error-profile typing
- @concepts/federated-daily-research-digest.md — K127 ingest
- @sweeps/2026-06-23-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Per-Entity Bias Mapping for AI Visibility: Why Brand Mentions Require Entity-Specific Calibration |
| **Author** | Zoltán Varga (Neural Awareness) |
| **arXiv** | 2606.21595 |
| **Zenodo** | 10.5281/zenodo.20308957 (v5: 10.5281/zenodo.20419277) |
| **Filename** | `arxiv-2606.21595-pdf-per-entity-bias-mapping-for-ai-visibility-ar.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2606.21595-pdf-per-entity-bias-mapping-for-ai-visibility-ar.pdf` |
| **Retrieved** | 2026-06-23 |
| **Read status** | read (framework, empirical §8, measurement protocol) |

## Narrative

**PEBM** argues aggregate mention/citation rates hide **entity-specific error profiles**. Study: **n=100** Hungarian B2B entities, **1,400** probe runs, **2,062** sources, non-AI HTTP verification.

### Three failure modes (+ lag asymmetry)

| Mode | Who suffers | Mechanism |
|------|-------------|-----------|
| **Invisibility** | Small / under-structured entities | Weak KG, schema, co-citation density |
| **Brand Hallucination Paradox** | High-salience familiar brands | Schema activation without evidential density → **fabricated citations** |
| **CEE infrastructure gap** | Underrepresented markets | KG absence + NER/linking deficits |
| **Parametric–retrieval lag** | Rebranding / fast-changing entities | RAG updates in days; parametric memory lags 12–24 months |

### Brand Hallucination Paradox (empirical) `[CONFIRMED in Varga panel]`

| Tier | Fabricated citation rate |
|------|-------------------------|
| Tier 1 high-salience | **52.69%** (95% CI 49.76–55.61%) |
| Tier 3 low-salience | **37.87%** (95% CI 34.84–41.00%) |
| Delta | **+14.82 pp** (χ²=45.326, p=1.67×10⁻¹¹) |

Regulatory-framed queries: **56.77%** fabrication vs **37.59%** factual queries (+19.2 pp framing delta).

### Ten PEBM dimensions (steal for audits)

Retrieval inclusion, mention probability, **verified mention rate**, false attribution rate, fabricated capability rate, **citation fidelity**, source authority mix, UI retention, business proxy signal, parametric–retrieval lag.

**Canonical presence** minimum: Wikidata QID (or equivalent KG anchor), consistent naming across authorities, schema.org on owned properties.

**Phase-0:** REFERENCE — Zenodo preprint + open instruments; no production SaaS adoption path. Local barbershop generalization `[NEEDS VERIFICATION 2026-06-23]`.

## Snippets

> "Two brands may have equal mention rates but radically different visibility quality." [Source: arxiv-2606.21595 Table 1]

> "Tier 1 high-salience brands produce 52.69% fabricated citations … versus 37.87% for Tier 3." [Source: arxiv-2606.21595 Abstract]

> "Canonical presence minimally comprises a stable entity identifier in a public knowledge graph … and schema.org structured markup on owned digital properties." [Source: arxiv-2606.21595 §3.6]
