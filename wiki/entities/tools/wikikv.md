---
title: WikiKV — hierarchical path-indexed wiki storage (REFERENCE)
type: entity
tags: [tool, wiki, rag, reference, k121]
keywords: [WikiKV, path-indexed, hierarchical knowledge base, Tencent, schema evolution]
related:
  - sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md
  - concepts/obsidian-integration.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-17-daily.md
  - osint-wiki/entities/tools/wikikv.md
  - osint-wiki/concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-06-17
updated: 2026-07-31
phase_0_verdict: REFERENCE
license_verified: n/a
repo: n/a
cross-wiki-source: "@osint-wiki/entities/tools/wikikv.md"
wire_status: wont_wire
wire_target: REFERENCE — no public install; pattern steal only
---

## Relations

- @sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md — arXiv 2606.14275
- @concepts/obsidian-integration.md — laptop git wiki reading layer
- @concepts/adaptive-rag-internal-linking-geo.md — navigation vs flat retrieval
- @concepts/federated-daily-research-digest.md — federation ingest read path
- @sweeps/2026-06-17-daily.md — K121 ingest
- @osint-wiki/entities/tools/wikikv.md — canonical tooling context
- @osint-wiki/concepts/wiki-tooling-evaluation.md — adoption evaluation row

## Raw Concept

Phase-0 on arXiv 2606.14275 (2026-06-17). **REFERENCE** — Tencent production hierarchical wiki KV; no public code release. Primary evaluation: @osint-wiki/concepts/wiki-tooling-evaluation.md.

## Narrative

### Phase-0 audit (2026-06-17)

| Check | Result |
|-------|--------|
| **License / code** | No public GitHub repo; WeChat production deployment only |
| **Maturity** | Production + AUTHTRACE benchmark (63.2% E2E correctness) |
| **Failure mode** | Rebuilding flat RAG when hierarchical navigation + schema evolution is the bottleneck |
| **Verdict** | **REFERENCE** — steal storage/navigation **patterns** for federation wikis post-librarian-decommission; no install on operator laptop |

### SEO-wiki steal (process only)

- Treat git `wiki/` as canonical tree; Obsidian vault is read/navigation layer (@concepts/obsidian-integration.md).
- **Path-as-key mental model** — `concepts/`, `entities/`, `sources/` prefixes mirror Index/Dimension routing.
- **Error Book analog** — `wiki/log.md` + ingest corrections persist across digest batches.

Prod handoff: `briefs/2026-06-17_k121-wikikv-hierarchical-wiki-storage-cemini-prod.md`.

## Snippets

> "Every online query observes a consistent, partial-read-free view of the wiki." [Source: @sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md §IV paraphrase]
