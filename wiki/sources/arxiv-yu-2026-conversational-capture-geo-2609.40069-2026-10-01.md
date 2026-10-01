---
title: "Yu et al. 2026 - Conversational capture: trajectory-level GEO evaluation (arXiv 2609.40069)"
type: source
tags: [source, arxiv, geo-aeo, measurement, evaluation, multi-turn, theory, k284]
keywords: [2609.40069, conversational capture, trajectory gain, feedback term, Polya urn, compounding ratio, Kendall tau, HAI 2026]
related:
  - concepts/conversational-capture-geo.md
  - concepts/geo-visibility-measurement.md
  - concepts/generative-engine-optimization.md
  - concepts/geo-visibility-vector-protocol.md
  - concepts/process-verified-agentic-search-geo.md
  - concepts/citation-verification-aeo.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md
  - sources/aggarwal-2024-geo-paper.md
  - sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md
  - sweeps/2026-10-01-daily.md
maturity: validated
read_status: deep-read
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- @concepts/conversational-capture-geo.md — operator playbook this paper grounds
- @concepts/geo-visibility-measurement.md — single-turn vs trajectory measurement; the misranking diagnostic
- @concepts/generative-engine-optimization.md — GEO/AEO hub
- @concepts/geo-visibility-vector-protocol.md — Martinez visibility vector; this paper supplies the time axis
- @concepts/process-verified-agentic-search-geo.md — the search→read hop, now chained across turns
- @concepts/citation-verification-aeo.md — capture is decoupled from current relevance
- @concepts/evidence-ecosystem-geo.md — evidence coordination across a trajectory
- @sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md — K283 AX: what the agent can read at the drill-down; this paper: how that compounds over turns
- @sources/aggarwal-2024-geo-paper.md — the single-turn baseline this paper argues is misspecified
- @sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md — Martinez notes one-shot measurement; this is the mechanism
- @concepts/corpus-overflow-out-of-scope.md — K284 sibling stubs
- @concepts/federated-daily-research-digest.md — K284 digest fetch
- @sweeps/2026-10-01-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Conversational Capture: A Trajectory-Level Framework for Evaluating Generative Engine Optimization in Multi-turn Human-Agent Interaction |
| **Authors** | Junwei Yu (U. Tokyo), Jieyu Zhou (UniConvo Inc.), Mufeng Yang (U. Tsukuba), Yepeng Ding (Hiroshima U.), Hiroyuki Sato (National Institute of Informatics) |
| **Venue** | HAI '26 — 14th International Conference on Human-Agent Interaction, Osaka, 16–19 Nov 2026 |
| **arXiv** | 2609.40069v1 [cs.HC], 30 Sep 2026 |
| **DOI** | 10.1145/3841580.3841626 |
| **License** | CC BY 4.0 |
| **Pages** | 9 (+ supplementary S1–S6) |
| **Filename** | `arxiv-2609.40069-conversational-capture-a-trajectory-level-framew.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.40069-conversational-capture-a-trajectory-level-framew.pdf` |
| **Retrieved** | 2026-10-01 |
| **Code / data** | None stated. Theory + model paper; no human study, no repository. |

## Narrative

**The claim.** GEO is evaluated as a **single-turn** property: fix a query, run the engine, score the source's visibility in one answer. The paper argues the single answer is the wrong unit of analysis. Human-agent information seeking is a **closed loop** — the answer changes the user's beliefs, which changes the next question, which changes what the agent retrieves. The authors name the resulting phenomenon **conversational capture**: *once a source is cited in earlier turns, its probability of being cited in later turns is significantly elevated, and this persistence can be decoupled from its relevance to the user's current need.*

**Two channels, kept separate.** This separation is the paper's methodological core.

- **M1 — machine-side capture.** Retrieval and generation condition on the dialogue history, so an earlier-cited source resurfaces **even when the query is held fixed**. M1 is a property of the engine alone: it needs no user model and is measurable by comparing a history-conditioned engine to a stateless one on identical queries.
- **M2 — human-side capture.** A GEO-shaped answer shifts the user's belief state and therefore the **next question** toward the captured source. M2 exists only when a human is in the loop and is the channel specific to human-agent interaction.

Three mechanisms produce capture: the dialogue history is part of the conditioning context; models tend to stay consistent with their own prior answers; and retrieval itself is biased by conversational context.

**The constructs** (all computable from the per-turn visibility values existing pipelines already produce):

| Construct | Definition | Reading |
|---|---|---|
| **Cumulative conversational visibility** (CCV) | Σ γₜ·wₜ(s) over turns; γₜ is an attention/salience weight | Total visibility a source accrues across a conversation. γₜ=1 is raw; decreasing γₜ = primacy; increasing = recency |
| **Trajectory gain** L_T | CCV(GEO) − CCV(¬GEO) along the realized, coupled conversation | The thing a practitioner actually cares about |
| **Direct term** L_direct | The single-turn lift summed with the query path held at its no-GEO counterfactual | Exactly what current evaluation extrapolates |
| **Feedback term** L_feedback | Everything else — visibility gained because GEO changed the queries and the history | **≡ 0 under single-turn evaluation.** The human-in-the-loop term current evaluation omits |
| **Capture coefficient** κ(s) | P(citeₜ₊₁ ∋ s \| citeₜ ∋ s) − P(citeₜ₊₁ ∋ s \| citeₜ ∌ s) | κ > 0 is the operational signature of capture |
| **Compounding ratio** ρ | L_T / (T·L₁) | ρ = 1 means turns are independent and single-turn evaluation is exact; ρ > 1 means linear extrapolation **underestimates** |
| **Misranking diagnostic** τ | Kendall's τ between the single-turn ranking of m GEO methods and their trajectory ranking | Low τ means single-turn evaluation picks the wrong method |

The feedback term splits exactly by a nested counterfactual: **L_feedback = L_M1 + L_M2**, nesting history before queries so that L_M1 is identifiable without behavioural assumptions. L_M2 is then the residual.

**The theory (Pólya urn).** Modelling citations as draws from a reinforced urn with an asymmetric reinforcement split s_g − s_c = Δ_M1 + Δ_M2:

- **Proposition 6.1 (path dependence).** Under symmetric linear reinforcement the citation share is a bounded martingale converging almost surely to a **random** Beta limit set by the initial composition. The process is **non-ergodic**: early turns decide the long-run outcome. GEO raises the turn-1 advantage and shifts the whole limit distribution upward — so **GEO has its greatest leverage in the earliest turns**.
- **Proposition 6.2 (superlinear gain).** Under asymmetric reinforcement the trajectory gain is strictly convex in T — superlinear **while capture develops** — with ρ rising monotonically toward a finite ceiling of **1/(2L₁)**. It is asymptotically linear, not unboundedly superlinear.
- **Corollary 6.3.** L_feedback ≥ 0 under confirmatory reinforcement, with equality only when the engine is memoryless *and* queries do not drift.
- **Corollary 6.4.** L_M1, L_M2 ≥ 0 and sum exactly to L_feedback; each is zero under its own null condition.

**The sign of the feedback term is an empirical assumption, not a tautology.** Confirmatory reinforcement is predicted by history-conditioning, self-consistency, primacy, and sycophancy. But if users respond to a captured answer with **corrective** follow-ups ("is this independently confirmed?"), M2 goes negative and single-turn evaluation *overestimates* GEO instead. Either way the single-turn estimate is biased; the decomposition identifies the direction.

**The worked illustration** (δ = 0.12, β = 0.6, T = 10, γₜ = 1). Closed-loop share climbs from 0.62 at turn 1 to 0.91 at turn 10, while the direct-only counterfactual stays flat at 0.62.

| Quantity | Value |
|---|---|
| Single-turn gain L₁ | 0.120 |
| Naive extrapolation T·L₁ | 1.200 |
| Direct term L_direct | 1.200 |
| **Feedback term L_feedback** | **1.481** |
| — machine-side L_M1 (β_M1=0.35) | 0.851 |
| — human-side L_M2 (β_M2=0.25) | 0.630 |
| Trajectory gain L_T | 2.681 |
| **Compounding ratio ρ** | **2.234** |

**The feedback term is larger than the direct term.** More than half of the modelled conversational payoff is invisible to single-turn evaluation. The machine-side channel alone (0.85) is comparable to the direct term (1.20). ρ climbs toward the ceiling 1/(2δ) ≈ 4.17, so the underestimation grows with conversation length.

**Misranking.** Five stylized GEO methods trading single-turn salience δ against induced capture strength β: the two rankings agree on only 7 of 10 pairs, **Kendall's τ = 0.4**. The single-turn winner ranks third by trajectory; the trajectory winner ranks second on a single turn. Across 5×10⁴ random method sets the rankings disagree in **90%** of draws (mean τ = 0.54, median 0.60), and in **48%** the single-turn winner is not the trajectory winner. When β is drawn negatively correlated with δ — the realistic salience/capture trade-off — disagreement worsens to mean τ = 0.18, with the single-turn winner wrong in **91%** of draws.

**HCI foundations.** The query operator Q is grounded in **information foraging** (the user follows a gradient of information scent; a GEO-shaped answer raises the perceived value of one source's region). The consequence layer is **trust calibration** — repeated exposure can raise perceived reliability through familiarity while reducing exposure to alternatives that would support recalibration, so capture can **amplify trust miscalibration**. The normative layer is **Bayesian persuasion**: multi-turn GEO is a sequential persuasion game, and its multi-turn form is strictly more powerful than its single-turn form.

**Design levers for answer engines** (each targets a term in the framework):

1. **Per-turn re-grounding** — reduce the weight of history during retrieval, addressing M1 and lowering κ.
2. **Enforced source diversity** — cap any single source's share within a turn, bounding L_feedback directly.
3. **Provenance transparency** — explain *why* a source is still cited, distinguishing a previous citation from current relevance, giving the user a corrected information scent.

The paper also argues GEO audits, answer-engine benchmarks, and platform abuse detection should report trajectory-level quantities (L_T, L_feedback, ρ, κ) and the misranking τ, not single-turn visibility alone.

**SEO remit for this wiki:** this is a **methodology** paper, and it changes what a good measurement looks like. It pairs directly with K283 (AX): K283 measures whether the agent can *read* the source at the drill-down; this paper measures whether that read *compounds* over a conversation. See @concepts/conversational-capture-geo.md for the operator translation and @concepts/geo-visibility-measurement.md for the updated measurement loop.

## Caveats (the authors' own)

- **Theory and modelling, not measurement.** No human annotations, no deployed engine. The numbers are properties of the model. The paper is explicit: "This is a property of the model rather than a measurement of a deployed engine."
- **Dependence on user simulation.** The planned empirical study anchors the main trajectory on real human queries and measures M1 **without any user model**; only the M2 counterfactual needs a simulated branch. Sensitivity to the simulator must be reported.
- **The immediate next step** is to estimate wₜ(s), κ, ρ, and τ on conversational open-retrieval corpora with human follow-up sequences — TopiOCQA, QReCC, ORConvQA — by injecting GEO-optimized and control passages into an open-source RAG pipeline turn by turn.
- **Two-source urn** collapses a many-source landscape into one aggregate competitor. The martingale and non-ergodic limit generalize to K sources (Beta → Dirichlet), but competition among several optimized sources is outside the model.
- **LLM-as-judge visibility scoring is imperfect**; an empirical study must report judge agreement and inter-judge reliability.
- **Open-source RAG ≠ a commercial closed engine**; replication across several open models is required.
- No real human trust or perception is measured.
- **Local-service generalization:** `[NEEDS VERIFICATION 2026-10-01]` — no local, geographic, or near-me queries anywhere in the paper.

## Snippets

> "We introduce conversational capture, a phenomenon in which a source cited early becomes substantially more likely to be cited again." [Source: arXiv 2609.40069 Abstract]

> "Using reinforcement-process (Pólya-urn) theory, we prove that the feedback term is identically zero under single-turn evaluation and that GEO's cumulative payoff grows superlinearly with conversation length while capture develops." [Source: arXiv 2609.40069 Abstract]

> "The feedback term is larger than the direct term: more than half of GEO's modeled conversational payoff is not represented by single-turn evaluation." [Source: arXiv 2609.40069 §7.2]

> "A practitioner who optimizes the single-turn metric would therefore select the wrong method within this model." [Source: arXiv 2609.40069 §7.3]

> "GEO has its greatest leverage in the early turns." [Source: arXiv 2609.40069 §6, Proposition 6.1 discussion]

> "Capture can therefore amplify trust miscalibration." [Source: arXiv 2609.40069 §8]

## Phase-0 (tool audit)

**No tool to audit.** Theory + model paper. No repository, no dataset released, no software artifact. 0 SEO Adopt, 0 MB runtime.

## Phase-1 (wire)

**policy_wired** into @concepts/geo-visibility-measurement.md (trajectory measurement + misranking diagnostic) and @concepts/conversational-capture-geo.md (new operator playbook). Hands-on: `briefs/2026-10-01_k284-conversational-capture-probe-hands-on.md`. No runtime wire, no MCP, no `settings.json` change.
