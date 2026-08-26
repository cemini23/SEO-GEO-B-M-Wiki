---
title: "Hazra et al. 2026 - CRASE bounded scholarly DeepSearch (arXiv 2608.24809) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, deep-research, agentic-search, crase, k164]
keywords: [2608.24809, CRASE, Crase, scholarly DeepSearch, citation graph, bounded exploration, LitSearch]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - concepts/process-verified-agentic-search-geo.md
  - sweeps/2026-08-26-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-26
updated: 2026-08-26
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — scholarly agentic search; not local SEO/GEO ranking
- @concepts/federated-daily-research-digest.md — K164 digest fetch
- @concepts/process-verified-agentic-search-geo.md — **thin GEO steal** (bounded graph exploration vs open-ended deep research)
- @sweeps/2026-08-26-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-26_k164-crase-bounded-deepsearch-from-seo.md` (CCC **primary** — bounded inspectable agent loop; empty repo → Watch / 0 MB)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Structurally-bounded Agentic Graph Exploration for Evidence-Grounded Scholarly DeepSearch |
| **Authors** | Rima Hazra, Sayan Layek, Somnath Banerjee, Soumen Chakrabarti, Animesh Mukherjee (NUS / TCG CREST / IIT Kharagpur / SIT / IIT Bombay) |
| **arXiv** | 2608.24809 (cs.IR / cs.AI) |
| **Filename** | `arxiv-2608.24809-structurally-bounded-agentic-graph-exploration-f.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.24809-structurally-bounded-agentic-graph-exploration-f.pdf` |
| **Retrieved** | 2026-08-26 |
| **Code** | `github.com/RadiantCrystal/CRASE` — **empty repo (409, no commits)** → Watch / 0 MB. Do not clone. |

## Narrative

Deep research agents decompose questions, call tools, judge sufficiency, and search again — but exploration is **open-ended**, errors persist in context, and stopping is opaque. **CRASE** (Crase) is a bounded alternative for scholarly search: **one** search-engine query for seed papers → expand along the **1.5-hop citation neighborhood** → prune edges whose claims lack entailment support → rank remaining papers with a recency-aware random walk. The candidate set, the reason each paper is kept, and the stopping condition are **explicit and fixed before inference**. On LitSearch and additional benchmarks over a 500K-paper arXiv corpus, CRASE outperforms deep-research agents built on proprietary models by up to **3× recall@50 at roughly a third of the cost**.

**SEO remit:** cs.IR scholarly-search false positive — no local-pack playbook. Federation: **thin GEO steal** on process-verified agentic search (fixed evidence graph beats open-ended “search until budget”; pairs K139 entity-hit verification). **CCC primary** — bounded inspectable agent loop (pairs K277 labels≠endpoints, K256 trajectory audit). Empty GitHub → Watch / 0 MB.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "Can scholarly discovery be performed through a structurally bounded and evidence-inspectable process without sacrificing retrieval effectiveness?" [Source: arXiv 2608.24809 Abstract]

> "Crase queries a search engine once for seed papers, expands them along their 1.5-hop citation neighborhood, prunes citation edges whose claims lack entailment support, and ranks the remaining papers with a recency-aware random walk." [Source: arXiv 2608.24809 Abstract]
