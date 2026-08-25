---
title: "Lu et al. 2026 - Beyond Fault Localization: Trajectory-Level LLM Agents for Microservice RCA (arXiv 2608.21310) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, rca, llm-agents, trajectory-eval, diagguard, k163]
keywords: [2608.21310, DIAGGUARD, trajectory-level RCA, root cause analysis, microservices, Acc@1, fault propagation]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-25-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — LLM agent RCA; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K163 digest fetch
- @sweeps/2026-08-25-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-25_k163-diagguard-trajectory-rca-and-chimera-from-seo.md` (CCC **primary** — trajectory-eval + DIAGGUARD ground-then-verify policy candidate; no clone); `../Cybersecurity wiki/briefs/2026-08-25_k163-malware-fscil-and-diagguard-from-seo.md` (Cyber **thin**)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Beyond Fault Localization: A Trajectory-Level Study of LLM Agents for Microservice Root Cause Analysis |
| **Authors** | Qisheng Lu, Aoyang Fang, Junjielong Xu, Jin'ao Shang, Songhan Zhang, Yifan Yang, Xiaochuan Yan, Pinjia He (CUHK-Shenzhen; Xi'an Jiaotong University) |
| **arXiv** | 2608.21310 (cs.SE / AIOps) |
| **Filename** | `arxiv-2608.21310-beyond-fault-localization-a-trajectory-level-stu.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.21310-beyond-fault-localization-a-trajectory-level-stu.pdf` |
| **Retrieved** | 2026-08-25 |
| **Code** | DIAGGUARD prototype described; **no public DIAGGUARD repo located** — `FudanSELab/train-ticket` is the *benchmark*, not the method → Watch / 0 MB. Do not invent a repo URL. |

## Narrative

Existing automated root-cause-analysis (RCA) evaluations for microservices score **endpoint correctness** — whether the method names the responsible service — which says nothing about the evidentiary basis or the **fault-propagation route** linking source to symptoms, both needed before an on-call SRE trusts the diagnosis. The paper treats RCA as an observable diagnostic process: a **trajectory-level framework** evaluates agent executions against manually curated service-level fault-propagation paths, applied to a public microservice RCA benchmark over **3,500 diagnostic trajectories**. Findings: a disconnect between **answer correctness and diagnostic quality** — an agent can localize the fault source yet fail to reconstruct propagation across affected services (harder and more discriminative). Successful investigations stay on the fault-impact surface, act on retrieved evidence, and broaden their query repertoire as the search deepens; failures depart the relevant route, miss decisive observations, or stagnate in shallow repetitive queries. Erroneous diagnoses reduce to three evidence-handling failures: **decisive evidence omitted, retrieved evidence misinterpreted, unsupported inference substituted for missing evidence**. This taxonomy is operationalized as **DIAGGUARD**, a two-stage defense-in-depth: **grounding** (systematically survey available observations before localization) + **verification** (audit the diagnosis against them). In an independent validation setting (different model, benchmark, service topology) the prototype raises **Acc@1 from 43.5% to 52.5%**.

**SEO remit:** cs.SE false positive — no local-SEO playbook. Federation: **CCC primary** — final-answer Acc@1 hides failed propagation reconstruction (pairs K256/K277 label≠endpoints); DIAGGUARD = ground-then-verify. **Cyber thin**. No public DIAGGUARD repo → Watch / 0 MB.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "Our results reveal a disconnect between answer correctness and diagnostic quality. An agent may correctly localize the fault source yet fail to reconstruct its propagation across the affected services; recovering this path is harder and more discriminative than identifying the affected services alone." [Source: arXiv 2608.21310 Abstract]

> "In an independent validation setting with a different model, benchmark, and service topology, the prototype raises Acc@1 from 43.5% to 52.5%." [Source: arXiv 2608.21310 Abstract]
