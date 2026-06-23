---
title: Per-Entity Bias Mapping (PEBM) — verified AI visibility audits
type: concept
tags: [geo-aeo, measurement, entity-audit, playbook, k127]
keywords: [PEBM, verified mention, Brand Hallucination Paradox, canonical presence, ghost cartography]
related:
  - sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md
  - concepts/geo-visibility-measurement.md
  - concepts/citation-verification-aeo.md
  - concepts/generative-engine-optimization.md
  - concepts/llm-brand-bias-geo-competition.md
  - concepts/competitive-geo-citation-factors.md
  - sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md
  - entities/tools/ranqo.md
  - concepts/schema-markup-local.md
  - concepts/citation-building.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-23-daily.md
maturity: validated
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- @sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md — primary source (arXiv 2606.21595)
- @concepts/geo-visibility-measurement.md — citation share CIs + repeated sampling
- @concepts/citation-verification-aeo.md — claim–source verification methodology
- @concepts/generative-engine-optimization.md — GEO hub
- @concepts/llm-brand-bias-geo-competition.md — brand default under spec ties (Chu) vs fabrication under familiarity (Varga)
- @concepts/competitive-geo-citation-factors.md — winning citation slots vs visibility quality
- @sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md — mention-rate tiers need verified-mention overlay
- @entities/tools/ranqo.md — vendor mention telemetry; pair with manual verification
- @concepts/schema-markup-local.md — canonical presence via JSON-LD
- @concepts/citation-building.md — third-party co-citation density
- @concepts/federated-daily-research-digest.md — K127 ingest
- @sweeps/2026-06-23-daily.md — overnight fetch

## Raw Concept

Operator playbook from @sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md — calibrate AI visibility **per entity**, not platform averages.

## Narrative

### Raw mention ≠ good visibility

| Brand | Mention rate | Verification | Strategic read |
|-------|--------------|--------------|----------------|
| A | 40% | Mostly accurate | Strong verified visibility |
| B | 40% | Many false claims | **High reputational exposure** |

Pair Ranqo-style **mention tracking** (@sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md) with **verified mention rate** from this framework.

### Brand Hallucination Paradox (local analog) `[TENTATIVE]`

Famous chains / long-established shops may get **more AI mentions** but also **more fabricated citations** (52.7% vs 37.9% in Varga B2B panel). Tier-3 local shops: low mention rate **and** different failure mode (invisibility, not misattribution).

**Operator rule:** if Tier 1–2 analog, audit **citation fidelity** aggressively; if Tier 3, prioritize **canonical presence** + co-citation before copy tweaks.

### Canonical presence checklist

- [ ] Stable entity ID where applicable (Wikidata QID for notable businesses; consistent `@id` in JSON-LD)
- [ ] schema.org `LocalBusiness` / `BarberShop` on owned site (@concepts/schema-markup-local.md)
- [ ] Consistent legal name + NAP across GBP, website, top directories
- [ ] Third-party references (listicles, chamber, local press) — field density per Varga

### Parametric–retrieval lag

After rebrand, hours change, or new location: re-audit **both** retrieval-heavy engines (Perplexity) and parametric-dominant surfaces — stale parametric image may persist 12–24 months `[NEEDS VERIFICATION 2026-06-23]` on local queries.

### Minimal operator audit (5 dimensions)

1. **Mention probability** — unbranded category queries (Ranqo brief)
2. **Verified mention rate** — open cited URLs; claim matches GBP/website
3. **False attribution rate** — services/prices/hours AI claims that are wrong
4. **Citation fidelity** — cited page supports the specific claim
5. **Parametric–retrieval lag** — compare engines after a deliberate NAP/hours update

Full ten-dimension protocol: @sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md Table 2.

## Snippets

> "A brand mention in an AI answer is not automatically a positive signal." [Source: arxiv-2606.21595 §1]

> "Figurality emerges from structured patterns of third-party confirmation, citation density, co-citation, entity identifiers, and knowledge graph anchoring." [Source: arxiv-2606.21595 §3.10]
