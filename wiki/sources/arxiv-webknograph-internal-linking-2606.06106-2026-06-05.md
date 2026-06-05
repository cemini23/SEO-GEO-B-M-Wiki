---
title: WebKnoGraph — GNN-powered internal linking (arXiv 2606.06106)
type: source
tags: [source, arxiv, internal-linking, gnn, seo, geo-search]
keywords: [2606.06106, webknograph, graphsage, pagerank, semantic-coherence, kalicube]
related:
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/on-page-seo-local.md
  - concepts/generative-engine-optimization.md
  - concepts/content-strategy-local.md
  - entities/tools/semrush.md
  - entities/tools/ahrefs.md
  - entities/tools/yoast-seo.md
  - sweeps/2026-06-05-daily.md
maturity: draft
read_status: read
created: 2026-06-05
updated: 2026-06-05
---

## Relations

- @concepts/adaptive-rag-internal-linking-geo.md — internal-link graph evaluation playbook
- @concepts/on-page-seo-local.md — hub-and-spoke internal linking patterns for local sites
- @concepts/generative-engine-optimization.md — semantic coherence + authority redistribution as AEO inputs
- @concepts/content-strategy-local.md — service/location hub structure the framework assumes
- @entities/tools/semrush.md — commercial internal-link audit baseline
- @entities/tools/ahrefs.md — commercial internal-link audit baseline
- @entities/tools/yoast-seo.md — WP internal-linking suggestions (heuristic, not graph-evaluated)
- @sweeps/2026-06-05-daily.md — 2026-06-05 digest ingest

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | WebKnoGraph: GNN-Powered Internal Linking |
| **Authors** | Emilija Gjorgjevska (TUM), Georgina Mirceva, Miroslav Mirchev (Ss. Cyril and Methodius University, Skopje) |
| **Affiliations** | WordLift + Kalicube collaboration (E.Gj.); Complexity Science Hub Vienna (M.M.) |
| **arXiv** | 2606.06106 |
| **Filename** | `arxiv-2606.06106-webknograph-gnn-powered-internal-linking-arxiv.pdf` |
| **Location** | `raw-sources/` (gitignored); PDF synced to librarian per 2026-06-05 ingest |
| **Code** | https://github.com/martech-engine/WebKnoGraph |
| **Retrieved** | 2026-06-05 |
| **Read status** | read (full paper + methodology + results) |

## Narrative

**WebKnoGraph** is an open-source framework for **pre-deployment evaluation** of internal-link interventions on production website crawls. It does not claim live ranking or traffic effects — it models authority redistribution and semantic coherence *before* links go live, when post-hoc attribution is noisy (content updates, external links, crawl behavior, algorithm changes).

### Problem framing

Internal linking is a recurring SEO task, but production workflows often rely on manual judgment, fixed templates, or generic tool recommendations with limited ability to compare candidate interventions. PageRank theory exists, but teams rarely translate it into reproducible evaluation. Live A/B tests are confounded by many simultaneous signals.

### Pipeline (four stages)

| Stage | What it does |
|-------|----------------|
| **1. Crawl → site graph** | Directed graph \(G_S = (V_S, E_S)\); pages = nodes, internal links = edges |
| **2. Embeddings + GraphSAGE** | Page text embedded with **nomic-embed-text-v1** (768-d, L2-normalized); **GraphSAGE** (2-layer mean aggregation) combines content + neighborhood structure to score donor→target candidate links |
| **3. Strategy + selection** | Five strategies define candidate link spaces; ~**240 links** per intervention set (realistic editorial budget) |
| **4. Host embedding + metrics** | Site embedded into external host graph (FineWeb empirical or Barabási–Albert synthetic); PageRank computed on composite graph; outcomes reported only for site pages |

### Five linking strategies

| Strategy | Target |
|----------|--------|
| **High** | Boost high-PageRank pages at directory depth 5 |
| **Low** | Boost low-PageRank pages at depth 5 |
| **Mixed** | Both high- and low-PageRank at depth 5 |
| **Folder** | Pages at depths 4–5 (mid-level connectivity) |
| **Random** | Unguided baseline |

Two selection regimes: **automatic** (GraphSAGE-ranked + load-balancing so links don't cluster on few pages) and **expert-assisted** (WordLift SEO professionals filter for template compatibility, section alignment, UX, deployability).

### Evaluation metrics

| Metric | Meaning | Operator read |
|--------|---------|---------------|
| **Authority Yield (AY)** | Average relative PageRank gain ÷ intervention budget \(k\) | Efficiency of authority redistribution per link added |
| **Authority Volatility (AV)** | Std dev of gains ÷ \(k\) | Predictability across host embeddings; lower = more stable |
| **Authority Down/Up Ratio (R_D/U)** | Pages losing authority vs gaining (τ = 0.025% threshold) | \<1 = gains dominate; \>1 = losses dominate |
| **Semantic-Coherence Change (ΔSC)** | Avg cosine similarity of connected page embeddings | Negative = added links connect less-topically-related pages |

### Key empirical findings (Kalicube.com, 1,841 pages)

Evaluated on Q2 2025 production crawl in FineWeb-based and BA host environments. `[CONFIRMED]` within paper's single-domain, pre-deployment scope; `[TENTATIVE]` for generalization to small local-business sites.

1. **No single metric wins.** Expert-assisted **Low** strategy achieved highest Authority Yield but worst Down/Up ratio — strong average gain with unfavorable loss–gain distribution across pages.
2. **Automatic vs expert tradeoff.** Automatic selection generally produces **higher average AY**; expert-assisted selection **preserves semantic coherence** better (smaller negative ΔSC).
3. **Folder strategy (automatic)** had most favorable Down/Up balance among automatic strategies; **High** did not beat Random under automatic selection — strategy intent is sensitive to final link choices.
4. **All interventions slightly reduced semantic coherence** — expected when expanding link structure beyond original architecture; expert review mitigates magnitude.
5. **Host environment** affects magnitude, not qualitative tradeoff patterns between strategies.

### Operator relevance for local B&M sites

**Direct applicability [TENTATIVE]:**

- Validates the @concepts/on-page-seo-local.md hub-and-spoke model as something worth **evaluating**, not just templating — especially for multi-location operators deciding which service pages should receive links from location pages.
- **Low-PageRank boost** (orphan service pages, new neighborhood landing pages) can yield high AY but may steal authority from other pages — check R_D/U before deploying bulk link additions.
- **Semantic coherence** aligns with GEO "narrative coherence" (@concepts/generative-engine-optimization.md): links between topically unrelated pages (e.g. random blog → location page with forced exact-match anchor) may redistribute authority but hurt topical signal.
- Framework requires a **full crawl** (~1,800+ pages on Kalicube; a 2-location barbershop is 15–40 pages) — for small sites, manual audit against the paper's four metrics is the practical analog; WebKnoGraph tooling is overkill until page count grows.

**Not applicable without adaptation:**

- No click/impression/crawl-frequency data — GSC integration is future work (WordLift Internal Links product roadmap).
- Single production domain evaluated — e-commerce, news, and 10-page local sites untested.
- Does not model external links, GBP, or citations.

### Limitations (paper)

- No live A/B ranking tests
- Excludes behavioral signals (clicks, conversions, crawl logs)
- Single domain (Kalicube.com — entity/SEO education site, not local B&M)
- FineWeb host graph is a controlled proxy, not the real Web

## Snippets

> "Internal link optimization is a recurring task in search engine optimization, yet many production workflows rely on manual judgment, fixed page templates, or generic tool recommendations." [Source: arXiv 2606.06106 Abstract (retrieved 2026-06-05)]

> "Rather than claiming direct ranking or traffic effects, we provide reproducible pre-deployment evidence on the structural and semantic tradeoffs of candidate internal-link interventions." [Source: arXiv 2606.06106 §1 (retrieved 2026-06-05)]

> "These findings support a practical workflow in which candidate intervention sets are generated at scale, evaluated jointly across authority gain, volatility, loss–gain balance, and semantic coherence, and then reviewed for editorial deployability before implementation." [Source: arXiv 2606.06106 Abstract (retrieved 2026-06-05)]

> "Automatic interventions generally produce higher average AY than expert-assisted interventions… expert assistance better preserves semantic coherence and can produce competitive or superior AY in specific strategy-level settings." [Source: arXiv 2606.06106 §5.3 (retrieved 2026-06-05)]

> "The WebKnoGraph framework, experiment scripts, and configuration files are available at https://github.com/martech-engine/WebKnoGraph." [Source: arXiv 2606.06106 Data Availability (retrieved 2026-06-05)]
