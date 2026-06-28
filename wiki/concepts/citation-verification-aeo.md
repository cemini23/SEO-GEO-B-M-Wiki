---
title: Citation verification for answer-engine optimization
type: concept
tags: [geo-aeo, citation, verification, hallucination, measurement]
keywords: [citation verification, evidence attribution, hallucination audit, claim-source alignment, Med-V1]
related:
  - concepts/generative-engine-optimization.md
  - concepts/competitive-geo-citation-factors.md
  - sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md
  - sources/davidson-2026-factual-gv-gap.md
  - sources/ptah-2026-verifiable-multimodal-deep-research.md
  - sources/vishwakarma-2026-competitive-geo-sigir.md
  - sources/aggarwal-2024-geo-paper.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-06-daily.md
  - concepts/geo-visibility-measurement.md
  - sources/arxiv-zhu-2026-deeprubric-evidence-tree-2606.17029-2026-06-16.md
  - "@osint-wiki/sources/arxiv-metaresearcher-deep-research-2606.19893-2026-06-20.md"
  - "@osint-wiki/entities/tools/metaresearcher.md"
  - sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md
  - concepts/per-entity-bias-mapping-geo.md
  - sources/arxiv-crespin-2026-karla-knowledge-base-augmented-retrieval-2606.26807-2026-06-28.md
  - concepts/canonical-business-facts-geo.md
maturity: draft
created: 2026-06-06
updated: 2026-06-28
---

## Relations

- @concepts/generative-engine-optimization.md — parent GEO/AEO hub; measurement loop step 7
- @concepts/competitive-geo-citation-factors.md — winning the citation slot vs verifying citation accuracy
- @sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md — empirical hallucination rates under citation formats
- @sources/davidson-2026-factual-gv-gap.md — engines verify conflicting facts from different sources
- @sources/ptah-2026-verifiable-multimodal-deep-research.md — stage-wise fidelity in deep-research pipelines
- @sources/vishwakarma-2026-competitive-geo-sigir.md — gatekeeper factors before verification matters
- @sources/aggarwal-2024-geo-paper.md — "Cite Sources" improves visibility but doesn't guarantee accuracy
- @concepts/adaptive-rag-internal-linking-geo.md — reflection routing for high-stakes publishes
- @concepts/federated-daily-research-digest.md — 2026-06-06 digest ingest
- @sweeps/2026-06-06-daily.md — K101 overnight fetch
- @concepts/geo-visibility-measurement.md — citation share noise vs claim–source accuracy
- @osint-wiki/sources/arxiv-metaresearcher-deep-research-2606.19893-2026-06-20.md — adversarial misinformation injection in training corpora (K124)
- @osint-wiki/entities/tools/metaresearcher.md — deep-research RL framework REFERENCE
- @sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md — citation fidelity + false attribution dimensions (K127)
- @concepts/per-entity-bias-mapping-geo.md — verified mention playbook
- @sources/arxiv-crespin-2026-karla-knowledge-base-augmented-retrieval-2606.26807-2026-06-28.md — KB provenance vs parametric hallucination (K132)
- @concepts/canonical-business-facts-geo.md — sync checklist before verification runs

## Raw Concept

What prompted this page: @sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md — NIH paper quantifying how often LLM-generated answers with citations are **not supported** by the cited source. Synthesized with @sources/davidson-2026-factual-gv-gap.md and @sources/ptah-2026-verifiable-multimodal-deep-research.md.

## Narrative

GEO work splits into two problems that operators often conflate:

| Problem | Question | Primary wiki page |
|---------|----------|-------------------|
| **Citation competition** | Does my page win the citation slot? | @concepts/competitive-geo-citation-factors.md |
| **Citation verification** | When cited, is the attributed claim actually true per the source? | This page |

Aggarwal 2024 showed that adding citations improves visibility (+27% Position-Adjusted Word Count). Med-V1 2026 shows that **~43–56% of LLM citation statements may not be supported by the cited source** in a controlled medical-QA setting `[TENTATIVE]` for local-business queries — directional, not domain-validated.

### What Med-V1 measured (biomedical, transferable pattern)

From @sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md:

1. **Volume ≠ accuracy** — GPT-5 generates 2–3× more citation statements than humans but fewer *supported* claims than human experts.
2. **Format affects mapping** — structured citation styles (NLM, AMA, Vancouver) map to real sources more reliably than APA/MLA; direct PMID/DOI instructions produce extreme hallucination (86–96%) despite perfect ID mapping.
3. **Human high-stakes content also fails** — 28% of flagged clinical-guideline misattributions validated on manual review.

### Operator verification loop (local business)

Run monthly or after major GBP/website changes:

1. **Query** each major engine with 5–10 realistic customer queries ("best barbershop in [city]," "[shop name] hours," "fade haircut [city] price").
2. **Capture** the full answer — note every claim about the business and any cited URL/GBP/listing.
3. **Verify claim–source pairs** manually or with a lightweight checker:
   - Open the cited page; does it state what the AI attributed?
   - Check NAP, hours, services, prices against GBP + website truth.
4. **Classify errors**:

| Error type | Example | Fix owner |
|------------|---------|-----------|
| **Retrieval miss** | Shop not mentioned at all | SEO: citations, GBP, content |
| **Entity confusion** | Wrong shop or wrong location | NAP consistency, schema `sameAs` |
| **Unsupported claim** | "Open Sundays" but GBP says closed | Update GBP + website; wait for re-crawl |
| **Contradicted claim** | Price cited from stale blog post | Refresh service page; disavow stale sources if possible |
| **Fabricated citation** | URL doesn't exist or doesn't mention shop | Report to engine; strengthen owned surfaces |

5. **Log** results in a spreadsheet or wiki entity page; track accuracy trend over time.

### When to escalate verification effort

Per @concepts/adaptive-rag-internal-linking-geo.md Part A routing:

| Stakes | Verification depth |
|--------|-------------------|
| Low — "what is a fade" generic Q | Spot-check quarterly |
| Medium — shop mentioned with hours/price | Monthly manual verify |
| High — before publishing AI-drafted FAQ/schema/copy | Full claim–source audit before publish |
| High — responding to public AI misinformation about the shop | Manual verify + GBP correction + website update |

### Tools landscape `[NEEDS VERIFICATION 2026-06-06]`

| Tool class | Example | Fit for local operator |
|------------|---------|------------------------|
| Biomedical SLM verifier | Med-V1 (3B, open-source) | Wrong domain; pattern only |
| GEO audit skills | @entities/tools/geo-seo-claude.md | Heuristic citability scoring, not claim–source alignment |
| Manual loop | Query engines + open cited URLs | **Default for &lt;50-page local sites** |
| Deep-research verifiers | PTAH-style stage checks | Overkill unless building automated research pipelines |

Med-V1 Phase-0 for local web pages: **NO-GO** — biomedical training data; no web/local benchmark. Use the **methodology** (extract claims, map to sources, verify alignment) not the model.

### Implications for operator content strategy

- **Don't trust AI citations in drafts** — when Claude/ChatGPT drafts copy with inline "sources," verify each claim against the actual page before publishing. Med-V1 shows even frontier models misattribute ~half the time in citation-heavy medical answers.
- **Prefer canonical facts on owned surfaces** — engines retrieve and misparse; a single authoritative FAQ on the website reduces multi-verse drift (@sources/davidson-2026-factual-gv-gap.md).
- **"Cite Sources" for GEO visibility ≠ verified accuracy** — Aggarwal's +27% lift measures citation prominence in generated answers, not whether your page's claims match reality when cited.
- **More AI citations in answers may mean more errors** — GPT-5's higher claim volume did not proportionally increase supported claims.
- **Adversarial single-source collapse** — @osint-wiki/sources/arxiv-metaresearcher-deep-research-2606.19893-2026-06-20.md cites Synthetic Web: one high-plausibility misinformation article can collapse frontier-model accuracy. Local operators should verify AI-claimed ratings/hours/prices against GBP + owned site, not assume citation presence implies correctness `[NEEDS VERIFICATION 2026-06-20]`.
- **Brand Hallucination Paradox** — @sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md: high-salience entities exhibit **higher fabricated citation rates** than low-salience ones despite equal or higher mention rates. Verification is mandatory for familiar local brands, not only unknown shops `[NEEDS VERIFICATION 2026-06-23]`.

## Snippets

> "Among successfully mapped citations, their hallucination rates are comparable for standard formats, whereas direct PMID citations cause extreme hallucinations." [Source: @sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md — §2.5 summary]

> "Both models still generate fewer supported claims than human experts overall." [Source: @sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md — §2.5 summary]
