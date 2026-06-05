---
title: Agent-orchestrated adaptive RAG — comparative study (arXiv 2606.05658)
type: source
tags: [source, arxiv, rag, geo-aeo, agents, digest]
keywords: [2606.05658, adaptive-rag, query-decomposition, reflection, musique, devops]
related:
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/generative-engine-optimization.md
  - concepts/federated-daily-research-digest.md
  - sources/memento-2026-web-learning-signal-low-data.md
  - sources/score-2026-self-evolving-deep-research.md
  - sources/ptah-2026-verifiable-multimodal-deep-research.md
  - concepts/obsidian-integration.md
  - sweeps/2026-06-05-daily.md
maturity: draft
read_status: read
created: 2026-06-05
updated: 2026-06-05
---

## Relations

- @concepts/adaptive-rag-internal-linking-geo.md — adaptive orchestration playbook for wiki/digest workflows
- @concepts/generative-engine-optimization.md — citation accuracy vs latency tradeoffs for operator research loops
- @concepts/federated-daily-research-digest.md — digest ingest should route simple vs complex queries differently
- @sources/memento-2026-web-learning-signal-low-data.md — procedural memory across sessions (complementary)
- @sources/score-2026-self-evolving-deep-research.md — evaluation must co-evolve with generators
- @sources/ptah-2026-verifiable-multimodal-deep-research.md — citation fidelity at synthesis time
- @concepts/obsidian-integration.md — structured corpus + metadata filtering analog
- @sweeps/2026-06-05-daily.md — 2026-06-05 digest ingest

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agent-Orchestrated Adaptive RAG: A Comparative Study on Structured and Multi-Hop Retrieval |
| **Authors** | Anuj Maharjan, Devinder Kaur, Richard G. Molyet |
| **arXiv** | 2606.05658 |
| **Filename** | `arxiv-2606.05658-agent-orchestrated-adaptive-rag-a-comparative-st.pdf` |
| **Location** | `raw-sources/` (gitignored); PDF synced to librarian per 2026-06-05 ingest |
| **Retrieved** | 2026-06-05 |
| **Read status** | read (architecture + results + limitations) |

## Narrative

Empirical comparison of **agent-orchestrated adaptive RAG** vs naive single-pass RAG across two contrasting corpora: a **structured DevOps knowledge base** (80 docs, ~10K words, six doc types with YAML metadata) and **MuSiQue** (compositional multi-hop QA benchmark). Core claim: agentic enhancements (query decomposition, bounded reflection) are **not universally beneficial** — gains are domain-dependent and carry large latency costs.

### Architecture

Four specialized agents + central **Orchestrator** (rule-based routing):

| Component | Role |
|-----------|------|
| **Query Classifier** | Categorizes requests; enables metadata filtering (doc type: runbook, incident, etc.) before similarity ranking |
| **Query Decomposer** | Splits multi-hop queries into ordered sub-queries; retrieves per sub-query; aggregates |
| **Answer Evaluator** | Scores relevance, citation accuracy, grounding, hallucination risk |
| **Orchestrator** | Routes: simple → direct retrieval; complex → decomposition; eval failure → reflection (max **2 retries**) |

**Stack (local, privacy-first):** Llama-3.1-8B-Instruct (4-bit GGUF via llama.cpp), BGE-base-en-v1.5 embeddings, FAISS vector store. Ingestion: IBM **Docling** → structured Markdown → YAML frontmatter → **600-token chunks / 100-token overlap**.

### Routing behavior

| Dataset | Standard RAG | Complex RAG | Decomposed RAG |
|---------|-------------|-------------|----------------|
| DevOps (structured) | **69.2%** | ~25% | **~5%** |
| MuSiQue (multi-hop) | low | **~49%** | **~16%** |

Reflection is post-hoc correction — strategy distribution identical with/without reflection enabled.

### Results — query decomposition

| Metric | DevOps (base → decomp) | MuSiQue (base → decomp) |
|--------|------------------------|-------------------------|
| Overall Score | 0.814 → **0.855** | 0.786 → 0.809 |
| MRR | 0.556 → **0.722** | 0.469 → **0.102** |
| Success@5 | 0.833 → **1.000** | 1.000 → **0.063** |
| Citation Accuracy | 0.750 → **0.917** | 0.906 → 1.000 |
| Topic Coverage | 0.625 → 0.558 | 0.609 → **0.859** |
| Latency (s) | 21 → **48** | 22 → **75** |

**Pattern:** Decomposition helps **structured, domain-specific** retrieval where sub-questions map cleanly. On **genuine multi-hop** data it broadens coverage but **fragments ranking signal** — MRR and Success@5 collapse.

### Results — reflection (bounded retry loop)

| Metric | DevOps (base → full agentic) | MuSiQue (base → full) |
|--------|------------------------------|----------------------|
| Overall Score | 0.870 → **0.781** ↓ | 0.721 → 0.666 ↓ |
| Citation Accuracy | 1.000 → 1.000 | 0.882 → 0.941 |
| Latency (s) | 11 → **22** | 17 → **104** |

Reflection: **marginal citation gains, often quality regression, 2–6× latency**. MuSiQue sixfold slowdown likely unacceptable for real-time ops.

### Operator / wiki relevance `[TENTATIVE]`

Maps directly to how **this wiki's ingest + query workflows** should behave:

1. **Route by query complexity** — "What's our GBP review response template?" → single-pass wiki read. "Synthesize GEO citation factors across 6 papers and our barbershop playbook" → multi-step decomposition (read index → follow relations → cross-wiki).
2. **Metadata filtering** — wiki frontmatter (`type`, `tags`, `maturity`) is the analog of DevOps doc-type filtering; `@concepts/` vs `@sources/` vs `@entities/` narrows retrieval before similarity search.
3. **Don't default to reflection loops** — bounded self-critique (re-read sources, verify citations) helps citation accuracy but burns session time; reserve for high-stakes outputs (schema deploy, GBP NAP change), not every digest skim.
4. **Chunking matters** — 600/100 overlap parallels wiki page structure (frontmatter + sections); poorly segmented corpus breaks multi-hop synthesis — aligns with @sources/ptah-2026-verifiable-multimodal-deep-research.md.
5. **Pairs with MEMENTO + SCORE** — MEMENTO = procedural memory across sessions; SCORE = co-evolving evaluator; this paper = **when to invoke expensive agentic paths at all**.

### Limitations (paper)

- Small DevOps corpus (80 docs); LLM-assisted generation + manual validation
- Small evaluation query sets — wide confidence intervals
- Single generator (Llama-3.1-8B) + single embedder (BGE)
- Rule-based orchestrator, not learned routing policy
- Latency environment-specific (local quantized inference)

## Snippets

> "These contrasting results show that agentic enhancements are not universally beneficial and must be applied selectively according to query and domain characteristics. Our findings argue for adaptive, cost-aware orchestration rather than uniformly aggressive reasoning pipelines." [Source: arXiv 2606.05658 Abstract (retrieved 2026-06-05)]

> "If the query is simple → direct retrieval. If the query is complex → decomposition pipeline. If evaluation fails → trigger reflection (at most two retries)." [Source: arXiv 2606.05658 §III-B (retrieved 2026-06-05)]

> "Decomposition helps in structured domains where chained reasoning maps cleanly onto well-defined relationships, but it is not universally beneficial and degrades ranking precision on harder multi-hop data." [Source: arXiv 2606.05658 §V-E (retrieved 2026-06-05)]

> "Reflection offers limited, inconsistent gains relative to its cost. And because a large share of queries are handled well by standard RAG, adaptive orchestration—applying expensive strategies only when warranted—is essential rather than optional." [Source: arXiv 2606.05658 §V-E (retrieved 2026-06-05)]
