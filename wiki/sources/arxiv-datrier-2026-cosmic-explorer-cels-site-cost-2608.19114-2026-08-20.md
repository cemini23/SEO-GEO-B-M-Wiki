---
title: "Datrier et al. 2026 - Identifying Cost-Favorable Locations for Cosmic Explorer (arXiv 2608.19114) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, gravitational-waves, gis, site-cost, k161]
keywords: [2608.19114, Cosmic Explorer, CELS, GIS, site evaluation, gravitational-wave]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-20-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-20
updated: 2026-08-20
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — CE gravitational-wave observatory siting; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K161 digest fetch
- @sweeps/2026-08-20-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-20_k161-gbp-consensus-and-magnet-output-from-seo.md` (CCC thin — CELS GIS cost pattern)
- Cross-wiki: `../OSINT WORKSPACE/briefs/2026-08-20_k161-cels-gis-site-cost-from-seo.md` (OSINT thin)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Identifying Cost-Favorable Locations for Cosmic Explorer |
| **Authors** | Laurence Datrier, Geoffrey Lovelace, Tooba Ansar, Lance Blagg, Warren Bristol, Matthew Evans, Chris Lukinbeal, Vuk Mandic, Kiet Pham, Jocelyn Read, Sarmad Rameez, Amber Romero, Oscar Romero, Babatunde Isaac Rotimi, Joshua B. Russell, Andrew Saenz, François Schiettekatte, Robert Schofield, David H. Shoemaker, Bretton Simpson, Bram J.J. Slagmolen, Joshua R. Smith |
| **arXiv** | 2608.19114 (astro-ph.IM / gr-qc) |
| **Filename** | `arxiv-2608.19114-identifying-cost-favorable-locations-for-cosmic.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.19114-identifying-cost-favorable-locations-for-cosmic.pdf` |
| **Retrieved** | 2026-08-20 |
| **Code** | `gitlab.com/cosmic-explorer/cels` — MIT, ~2 MB → `.local/adopts/cels` REFERENCE clone (Phase-0); runtime **wont_wire** (astro OOD) |

## Narrative

Cosmic Explorer (CE) is a proposed next-generation gravitational-wave observatory (20 km + 40 km L-shaped detectors in the conterminous US). This paper presents the **Cosmic Explorer Location Search (CELS)** Python package: given a candidate L-geometry, it estimates site-preparation costs (excavation, land clearing, land acquisition) while accounting for detector tilt, arm length, and opening angle. It complements the National Suitability Analysis (land-and-people GIS). Results use CELS v. 2026.03.12; authors also note ChatGPT Deep Research for cost references and Cursor/Codex for some CELS development.

**SEO remit:** astro-ph / GIS site-cost false positive — not local SEO. Federation: **CCC thin** + **OSINT thin** (reproducible GIS cost / multi-factor site search pattern). Code MIT ~2 MB REFERENCE clone only; not runtime-wired.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. CELS REFERENCE under `.local/adopts/cels`. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "For a specified detector location and L-shaped geometry in the conterminous United States, CELS estimates site-preparation costs associated with excavation, land clearing, and land acquisition, while accounting for the scientific effects of detector tilt, arm length, and arm opening angle." [Source: arXiv 2608.19114 Abstract]

> "CELS is available at https://gitlab.com/cosmic-explorer/cels/." [Source: arXiv 2608.19114 § Data Availability]
