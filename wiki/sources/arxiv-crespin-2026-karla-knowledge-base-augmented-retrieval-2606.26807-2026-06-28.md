---
title: "Crespin 2026 — KARLA knowledge-base augmented retrieval (arXiv 2606.26807)"
type: source
tags: [source, arxiv, geo-aeo, rag, factual-grounding, k132]
keywords: [2606.26807, KARLA, knowledge base, inline retrieval, factual externalization, provenance]
related:
  - concepts/canonical-business-facts-geo.md
  - concepts/citation-verification-aeo.md
  - concepts/generative-engine-optimization.md
  - concepts/schema-markup-local.md
  - concepts/google-business-profile.md
  - concepts/website-essentials-local-business.md
  - sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md
  - sources/davidson-2026-factual-gv-gap.md
  - sources/searchengineland-2026-google-llm-patent-entity-characterization-480625.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-28-daily.md
maturity: validated
read_status: read
created: 2026-06-28
updated: 2026-06-28
---

## Relations

- @concepts/canonical-business-facts-geo.md — operator playbook (GBP/schema as updatable fact KB)
- @concepts/citation-verification-aeo.md — KB-sourced spans vs parametric hallucination
- @concepts/generative-engine-optimization.md — factual grounding beyond vanilla RAG
- @concepts/schema-markup-local.md — structured relation layer on owned site
- @concepts/google-business-profile.md — maps/listing fact store
- @concepts/website-essentials-local-business.md — canonical hours/services/prices on owned pages
- @sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md — RAG routing complement (retrieval orchestration)
- @sources/davidson-2026-factual-gv-gap.md — engines blend conflicting parametric + retrieved facts
- @sources/searchengineland-2026-google-llm-patent-entity-characterization-480625.md — entity models consume listing/maps data
- @concepts/federated-daily-research-digest.md — K132 ingest
- @sweeps/2026-06-28-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | KARLA: Knowledge-base Augmented Retrieval for Language Models |
| **Authors** | François Crespin, Fabian M. Suchanek, Nils Holzenberger (Télécom Paris / IP Paris) |
| **arXiv** | 2606.26807 |
| **Filename** | `arxiv-2606.26807-2606-26807v1-karla-knowledge-base-augmented-retr.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2606.26807-2606-26807v1-karla-knowledge-base-augmented-retr.pdf` |
| **Retrieved** | 2026-06-28 |
| **Read status** | read (abstract, §3–4, counterfactual KB-update experiments) |
| **Code** | promised public in supplementary material `[NEEDS VERIFICATION 2026-06-28]` |

## Narrative

KARLA trains LLMs to emit **relation-specific trigger tokens** during generation that query a structured **knowledge base (KB)** and inject canonical values inline — separating linguistic competence from factual storage.

**Three claims (paper):**

1. Facts update via **KB edits** without retraining (counterfactual YAGO: **96.1%** accuracy immediately vs hundreds of LoRA steps for parametric fine-tuning).
2. KB-sourced spans carry **provenance** — each fact traceable to a KB triple (RAG passages lack this guarantee).
3. Smaller models (Qwen 0.6B + KARLA) beat larger parametric models on factual QA when facts live in KB.

**vs classic RAG:** 1-hop graph RAG can still **ignore** retrieved neighborhood and revert to parametric memory (accuracy drops to **77.8%** on popular entities in counterfactual setting). KARLA forces KB values into generation path once query tokens fire.

**Operator analog (local B&M):** treat GBP + schema-marked website + consistent directory NAP as the shop's **canonical fact KB**. When hours/prices/services change, update listings first — engines may still hallucinate stale parametric facts until retrieval wins (@sources/davidson-2026-factual-gv-gap.md). Not a deployed Google product; academic method `[TENTATIVE]` for barbershop AI answers.

## Snippets

> "Factual knowledge can be updated in the KB at virtually no cost, without retraining the model." [Source: arxiv-2606.26807 §3.1]

> "Every KB-sourced span is verifiable against a specific fact in the KB, a guarantee that neither vanilla generation nor RAG can deliver." [Source: arxiv-2606.26807 §3.1]

> "KARLA… updates factual behavior immediately by replacing the KB, reaching 96.1% accuracy without any additional gradient steps." [Source: arxiv-2606.26807 §4.4]
