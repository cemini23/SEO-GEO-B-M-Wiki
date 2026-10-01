---
title: Conversational capture — trajectory-level GEO for local operators
type: concept
tags: [concept, geo-aeo, measurement, multi-turn, playbook, k284]
keywords: [conversational capture, trajectory gain, feedback term, compounding ratio, capture coefficient, misranking, multi-turn GEO]
related:
  - sources/arxiv-yu-2026-conversational-capture-geo-2609.40069-2026-10-01.md
  - concepts/geo-visibility-measurement.md
  - concepts/generative-engine-optimization.md
  - concepts/geo-visibility-vector-protocol.md
  - concepts/process-verified-agentic-search-geo.md
  - concepts/citation-verification-aeo.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/agent-ready-website-local-bm.md
  - sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md
  - sources/aggarwal-2024-geo-paper.md
  - sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-10-01-daily.md
maturity: validated
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- @sources/arxiv-yu-2026-conversational-capture-geo-2609.40069-2026-10-01.md — source paper (Yu et al., HAI '26, arXiv 2609.40069)
- @concepts/geo-visibility-measurement.md — the measurement loop this page changes
- @concepts/generative-engine-optimization.md — GEO/AEO hub
- @concepts/geo-visibility-vector-protocol.md — Martinez visibility vector; this page supplies the time axis
- @concepts/process-verified-agentic-search-geo.md — the search→read hop, chained across turns
- @concepts/citation-verification-aeo.md — capture is decoupled from current relevance
- @concepts/evidence-ecosystem-geo.md — evidence coordination across a trajectory
- @concepts/agent-ready-website-local-bm.md — K283 AX: readability at the drill-down
- @sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md — K283 AX source
- @sources/aggarwal-2024-geo-paper.md — the single-turn baseline this framework supersedes
- @sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md — 45-study survey; this supplies the mechanism behind its time warnings
- @concepts/federated-daily-research-digest.md — K284 ingest
- @sweeps/2026-10-01-daily.md — overnight inbox drop

## Raw Concept

A customer no longer asks one search query and picks a link. They talk to an assistant: "best barber near me" → "do they do walk-ins" → "what do they charge for a fade" → "are they good with kids". Each answer shapes the next question. If the shop is cited in the first answer, **that citation tends to persist** — and it can persist even after the conversation moves past what the shop is actually best at.

**Conversational capture** is that persistence, named and formalized by Yu et al. (HAI '26, arXiv 2609.40069). This page is the operator translation.

## Narrative

### What the paper found

Full detail in @sources/arxiv-yu-2026-conversational-capture-geo-2609.40069-2026-10-01.md. The load-bearing points:

- **A cited source tends to keep being cited.** The paper defines a **capture coefficient** κ = P(cited next turn | cited this turn) − P(cited next turn | not cited). κ > 0 is the signature. GEO raises κ.
- **Two channels cause it.** **M1 (machine-side):** the engine conditions on the dialogue history, so an earlier source resurfaces *even with the query held fixed* — measurable with no user model at all. **M2 (human-side):** the answer steers the user's *next question* toward the captured source.
- **Early turns decide the outcome.** In a Pólya-urn model the citation share converges to a *random* limit set by the initial composition. The process is **non-ergodic** — the long-run outcome depends on early turns rather than on a deterministic notion of relevance. The paper's conclusion: "GEO has its greatest leverage in the early turns."
- **Single-turn measurement undercounts, and can pick the wrong method.** In the worked model the feedback term (1.48) **exceeds** the direct term (1.20); the compounding ratio ρ = 2.23, rising toward a ceiling of 1/(2L₁) ≈ 4.17 as the conversation lengthens. Ranking GEO methods by single-turn gain disagreed with the trajectory ranking (Kendall's τ = 0.4), and across random method sets the single-turn winner was wrong in 48% of draws — **91%** when salience and capture trade off against each other.

### What this means for a local business

**1. The first answer matters more than any later one.** The non-ergodicity result is the strongest argument yet for the readability work in @concepts/agent-ready-website-local-bm.md. It is not enough to be readable somewhere in a conversation. The shop must be readable **in the opening turn**, because the opening turn sets the trajectory.

**2. A citation is more durable than a ranking.** Classical SEO rank is re-decided every query. A cited source under capture keeps its position across the conversation. This explains why practitioners see a shop "stick" in AI answers well past the point where its relevance would predict it — and it cuts the other way: **a competitor captured early is hard to dislodge mid-conversation.** There is no mid-conversation fix. The work is to be the first credible answer.

**3. Corrective follow-ups are the operator's only lever inside a live conversation — and they are not the operator's to pull.** The paper is explicit that the sign of the feedback term is an empirical assumption. Confirmatory reinforcement (self-consistency, primacy, sycophancy) predicts L_feedback ≥ 0. But **corrective** follow-ups — "is that independently confirmed?", "what about [competitor]?" — make the human channel negative and reverse the advantage. A shop with a genuinely strong, checkable third-party footprint survives that challenge. A shop that was captured on a thin first answer does not. This is the operational case for @concepts/evidence-ecosystem-geo.md: the corrective challenge is where real evidence beats early noise.

**4. Trust miscalibration is the risk the paper names.** Repeated exposure raises perceived reliability through familiarity while reducing exposure to alternatives that would support recalibration. Anti-fabrication rules already in this wiki (@concepts/citation-verification-aeo.md, the CLAUDE.md hands-on rules) cover the operator's side of this.

### What to measure now

The current measurement loop in @concepts/geo-visibility-measurement.md samples repeated queries. That catches non-determinism. It does **not** catch capture, because each probe starts a fresh conversation.

**Add a trajectory probe.** The full procedure is in `briefs/2026-10-01_k284-conversational-capture-probe-hands-on.md`. The shape:

1. Write a **3–5 turn buyer conversation** for the shop's real category, in the order a customer would ask it: opening category query → a service detail → a price question → a comparison or trust question.
2. Run the conversation **start to finish** on each engine, keeping the thread. Do not reset between turns.
3. Record, per turn: is the shop cited? is it still cited **after the topic moves past its strength**? does a corrective follow-up ("are you sure — what about X?") dislodge it?
4. Repeat ≥3 times on different days and engines, per the sampling rules in @concepts/geo-visibility-measurement.md.

**What to record, in the paper's terms** (plain-language version):

| Paper construct | Operator version |
|---|---|
| Carryover | Is the shop cited in turn *n+1* after being cited in turn *n*? |
| Decay | How many turns after the topic moves on does the citation survive? |
| Corrective response | Does a challenge turn remove the citation? |
| Opening-turn capture | Was the shop cited in turn 1 at all? This is the term that decides the rest |

**Cheap starting signal:** run the same opening query twice — once as a fresh conversation, once as turn 3 of a conversation that already mentioned the shop. If the shop is cited in the second but not the first, the case is about capture, not relevance, and the fix is the opening turn.

### What NOT to do

- **Do not try to engineer capture.** The paper treats multi-turn GEO as a manipulation surface and proposes platform defenses against it (per-turn re-grounding, enforced source diversity, provenance transparency). Deliberately seeding a conversation to lock in a citation is the adversarial path described in @sources/arxiv-hu-2025-adversarial-attacks-llm-search-2501.00745-2026-06-10.md and is against the hands-on rules in CLAUDE.md. The legitimate version of capture is **being the best, most checkable answer first**.
- **Do not read the model numbers as measurements.** Every figure is derived from the model, not from a deployed engine. The paper says so repeatedly. Treat the direction as `[CONFIRMED]` at the theory level and the magnitudes as `[NEEDS VERIFICATION 2026-10-01]`.
- **Do not generalize to near-me queries yet.** The paper contains no local, geographic, or near-me query. Local-service generalization is `[NEEDS VERIFICATION 2026-10-01]`.

## Snippets

> "In multi-turn generative retrieval, once a source is cited in earlier turns, its probability of being cited in later turns is significantly elevated; this persistence may be independent of the source's relevance to the user's current (narrowed or drifted) information need." [Source: @sources/arxiv-yu-2026-conversational-capture-geo-2609.40069-2026-10-01.md — §2.3]

> "The feedback term is larger than the direct term: more than half of GEO's modeled conversational payoff is not represented by single-turn evaluation." [Source: @sources/arxiv-yu-2026-conversational-capture-geo-2609.40069-2026-10-01.md — §7.2]

> "Capture can therefore amplify trust miscalibration." [Source: @sources/arxiv-yu-2026-conversational-capture-geo-2609.40069-2026-10-01.md — §8]

Hands-on: `briefs/2026-10-01_k284-conversational-capture-probe-hands-on.md`.
