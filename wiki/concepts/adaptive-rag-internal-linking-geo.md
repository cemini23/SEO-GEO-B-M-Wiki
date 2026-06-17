---
title: Adaptive RAG orchestration + GNN internal linking for GEO
type: concept
tags: [concept, geo-aeo, geo-search, seo, rag, internal-linking, k100]
keywords: [2606.05658, 2606.06106, internal-linking, adaptive-rag, graphsage, pagerank]
related:
  - sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md
  - sources/arxiv-webknograph-internal-linking-2606.06106-2026-06-05.md
  - concepts/generative-engine-optimization.md
  - concepts/on-page-seo-local.md
  - concepts/federated-daily-research-digest.md
  - concepts/content-strategy-local.md
  - sources/memento-2026-web-learning-signal-low-data.md
  - sources/score-2026-self-evolving-deep-research.md
  - sources/ptah-2026-verifiable-multimodal-deep-research.md
  - entities/tools/semrush.md
  - entities/tools/ahrefs.md
  - entities/tools/yoast-seo.md
  - concepts/obsidian-integration.md
  - sweeps/2026-06-05-daily.md
  - sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md
  - concepts/citation-verification-aeo.md
  - concepts/citation-verification-aeo.md
  - sweeps/2026-06-06-daily.md
  - sources/arxiv-yuan-2026-flowbank-agentic-workflows-2606.11290-2026-06-16.md
  - entities/tools/flowbank.md
  - sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md
  - entities/tools/wikikv.md
  - sweeps/2026-06-17-daily.md
maturity: draft
created: 2026-06-05
updated: 2026-06-17
---

## Relations

- @sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md — adaptive RAG routing evidence
- @sources/arxiv-webknograph-internal-linking-2606.06106-2026-06-05.md — pre-deployment internal-link evaluation
- @concepts/generative-engine-optimization.md — semantic coherence + citation surfaces
- @concepts/on-page-seo-local.md — hub-and-spoke linking patterns for local sites
- @concepts/federated-daily-research-digest.md — digest query routing implications
- @concepts/content-strategy-local.md — service/location hub architecture
- @sources/memento-2026-web-learning-signal-low-data.md — procedural memory across research sessions
- @sources/score-2026-self-evolving-deep-research.md — co-evolving evaluation pressure
- @sources/ptah-2026-verifiable-multimodal-deep-research.md — citation fidelity at synthesis
- @entities/tools/semrush.md — commercial internal-link audits
- @entities/tools/ahrefs.md — commercial internal-link audits
- @entities/tools/yoast-seo.md — WP internal-link suggestions
- @concepts/obsidian-integration.md — structured corpus + metadata for agentic retrieval
- @sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md — high-stakes publish verification routing
- @concepts/citation-verification-aeo.md — reflection-before-publish analog
- @sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md — hierarchical NAV(q,B) vs flat chunk RAG
- @entities/tools/wikikv.md — path-indexed wiki storage REFERENCE

## Raw Concept

K100 digest batch (2026-06-05): two arXiv papers with **different operator surfaces** — (1) **when** to use expensive multi-step retrieval vs single-pass lookup, and (2) **how** to evaluate internal-link changes before deployment. Synthesized here as paired playbooks for client-site SEO and wiki/digest workflows.

## Narrative

These papers address orthogonal layers of the same stack:

| Layer | Paper | Question it answers |
|-------|-------|---------------------|
| **Research / ingest orchestration** | Adaptive RAG (2606.05658) | When should the system decompose queries, reflect, and retry — vs stop at one retrieval pass? |
| **Site architecture / on-page** | WebKnoGraph (2606.06106) | Given a crawl, which internal links redistribute authority without destroying topical coherence? |

Both argue against **uniformly aggressive** automation: adaptive routing and expert review beat always-on agentic pipelines or always-on automatic link insertion.

---

### Part A — Adaptive RAG orchestration `[TENTATIVE]` for wiki + operator research

From @sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md.

**Core finding [CONFIRMED in paper's testbed]:** Query decomposition improves structured-domain retrieval (+0.04 overall score, MRR +0.17 on DevOps) but **hurts ranking precision on multi-hop benchmarks** (MuSiQue MRR 0.469 → 0.102). Reflection adds 2–6× latency with inconsistent quality gains.

#### Routing decision tree (wiki / Claude sessions)

```
Query arrives
├─ Single fact lookup (NAP, hours, one concept definition)
│   └─ DIRECT: read index.md → one page → answer
├─ Structured synthesis (one domain, known page types)
│   └─ DECOMPOSE: sub-questions per concept/source cluster → aggregate
├─ Open multi-hop (cross-wiki, competitor + GEO + GBP)
│   └─ CAUTION: decomposition may broaden coverage but lose precision
│       → prefer explicit relation-following over blind sub-query splitting
└─ High-stakes output (schema deploy, GBP edit, review response to legal threat)
    └─ REFLECTION (max 2 passes): verify citations against source Snippets
```

#### Wiki-specific mappings

| Paper mechanism | Wiki analog |
|-----------------|-------------|
| Metadata filtering (doc type) | Frontmatter `type:` + `tags:` — route to `@sources/` vs `@concepts/` vs `@entities/` |
| 600/100 token chunking | Page sections (`## Narrative`, `## Snippets`) — don't retrieve half a concept |
| Orchestrator routing | Session-start: index.md first; don't deep-research for FAQ-level questions |
| Bounded reflection (2 retries) | Re-read `## Snippets` + raw source before operator hands-on actions |

#### Digest workflow implication

@concepts/federated-daily-research-digest.md overnight fetch is **single-pass retrieval** (correct). Morning Cursor ingest should:

- **Skim pass** (default): abstract + intro → source stub (what K100 stub ingest did)
- **Deep pass** (on demand): full paper → concept upgrade + operator playbook (this page)
- **Avoid** running reflection loops on every PDF — latency cost with no ranking benefit on multi-hop academic synthesis

Pairs with @sources/memento-2026-web-learning-signal-low-data.md (procedural memory: which queries duped, which lanes work) and @sources/score-2026-self-evolving-deep-research.md (re-run citation tests on schedule, not once).

---

### Part B — Internal link graph evaluation `[TENTATIVE]` for client sites

From @sources/arxiv-webknograph-internal-linking-2606.06106-2026-06-05.md.

**Core finding [CONFIRMED in paper's Kalicube testbed]:** Internal linking is a **multi-objective graph intervention** — authority gain, stability, loss–gain balance, and semantic coherence trade off. No single metric or strategy dominates. Expert review after automatic candidate generation preserves semantic coherence; automatic selection wins on average authority yield.

#### Four-metric pre-deploy checklist (manual analog for small sites)

Before adding a batch of internal links to a client site, score the proposal:

| Check | Question | Red flag |
|-------|----------|----------|
| **Authority yield** | Will orphan/high-value pages (service pages, new location page) gain discoverability? | Links only among already-strong pages (homepage ↔ about) |
| **Down/Up balance** | Are we boosting one page at the expense of many others? | 20 new links all targeting one service page from unrelated blog posts |
| **Semantic coherence** | Do linked pages share topical overlap? | Blog post about "history of barbering" → exact-match anchor to "fade haircut [city]" |
| **Volatility / stability** | Would this hold under different site contexts? | Links that only make sense during a temporary promo |

#### Strategy selection for local B&M sites

| Site situation | Strategy analog | Notes |
|--------------|-----------------|-------|
| New service page not ranking | **Low** boost | High AY potential but watch Down/Up ratio — don't drain location pages |
| Established location page needs reinforcement | **High** or **Folder** | Expert review matters — automatic High did not beat Random in paper |
| Multi-location hub | **Folder** (depth 4–5) | Connect location ↔ service ↔ FAQ at same hierarchy level |
| Replatform / new theme | **Random** baseline first | Measure before "SEO module" auto-links everything |

#### Integration with existing on-page guidance

Extends @concepts/on-page-seo-local.md **Internal linking — the site graph** section:

- Existing rules (descriptive anchors, hub-and-spoke) remain `[CONFIRMED]` practitioner baseline
- WebKnoGraph adds: **evaluate candidate link sets jointly** before deploy, not link-by-link in isolation
- GEO angle (@concepts/generative-engine-optimization.md): semantic-coherence loss from off-topic internal links may weaken extractable Q&A spans engines cite — authority redistribution alone is insufficient

#### Tooling path

| Scale | Approach |
|-------|----------|
| **≤50 pages** (typical 2-shop barbershop) | Manual audit against four-metric checklist; GSC Links report + Screaming Frog crawl. **Hands-on template:** `briefs/2026-06-05_two-shop-internal-link-audit.md` (worked example: `briefs/2026-06-05_two-shop-internal-link-audit-eastside-example.md`) |
| **50–500 pages** | @entities/tools/semrush.md or @entities/tools/ahrefs.md internal-link suggestions + manual coherence review |
| **500+ pages / agency** | WebKnoGraph open-source framework (https://github.com/martech-engine/WebKnoGraph); WordLift Internal Links integration planned |

`[NEEDS VERIFICATION 2026-06-05]` — WebKnoGraph Phase-0 on local 15-page WP sites not run; framework validated on Kalicube.com (1,841 pages) only.

---

### Combined operator workflow

For a **client site audit + content refresh** session:

1. **Crawl** site → export link graph (Screaming Frog, Sitebulb, or GSC)
2. **Identify orphans** (Low-strategy candidates) and **hubs** (location + top services)
3. **Generate candidate links** (tool suggestions or WebKnoGraph if scale warrants)
4. **Score batch** against four metrics — reject sets with high AY but bad Down/Up or large coherence penalty
5. **Expert pass** — template/UX/deployability (matches paper's expert-assisted regime)
6. **Deploy** → monitor GSC impressions/clicks 4–8 weeks (paper does not substitute live measurement)

For a **wiki research session**:

1. **Classify query** (fact vs structured synthesis vs multi-hop)
2. **Single-pass** unless synthesis requires decomposition
3. **Deep-pass** flagged papers on demand (not every digest PDF)
4. **Citation verify** only before hands-on platform actions

## Snippets

> "Internal linking should be treated as a multi-objective graph intervention problem." [Source: @sources/arxiv-webknograph-internal-linking-2606.06106-2026-06-05.md — §7]

> "Adaptive orchestration—applying expensive strategies only when warranted—is essential rather than optional." [Source: @sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md — §V-E]

## Dead Ends

- **Always-on query decomposition for digest ingest** — MuSiQue results predict precision loss on cross-paper synthesis; relation-following beats blind sub-query splitting for this wiki's graph structure.
- **Reflection loops on every operator Q&A** — 6× latency on multi-hop tasks for marginal citation gains; reserve for high-stakes outputs only.
- **WebKnoGraph on 10-page local sites without crawl tooling** — framework overhead exceeds benefit; use manual four-metric checklist instead.
