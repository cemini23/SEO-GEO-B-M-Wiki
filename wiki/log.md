---
title: Operations Log
type: log
updated: 2026-08-06
last_easy_review_ingest: 2026-05-08
---

# Operations Log

## [2026-08-06] ingest | K153 arXiv API false-positive batch (3 OOD; RepairFormer → Atto)

- **Inbox** — 3 PDFs; **0** SEO Adopt; RepairFormer MIT → Atto local adopt
- **Overflow** — @sources/arxiv-paul-2026-repairformer-structured-input-repair-2608.05060-2026-08-06.md; @sources/arxiv-breczewski-2026-glauber-axion-graviton-2608.05082-2026-08-06.md; @sources/arxiv-aliaga-2026-dasyr-llm-kinetic-symbolic-regression-2608.05120-2026-08-06.md
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @wiki/index.md, @sweeps/2026-08-06-daily.md
- **Phase-0** — `scripts/adopt_k153_phase0.sh` (SEO OOD; Atto `.local/adopts/RepairFormer` ~5MB MIT)
- **Phase-1** — no new SEO wires; Atto holds runtime clone (HITL only)
- **Cross-wiki** — Atto RepairFormer brief + adopt; CCC RepairFormer + DASyR
- **GuruWatcher / TipDrop / poker / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API lanes still noisy (K141–K153)

## [2026-08-05] ingest | K152 arXiv API false-positive batch (3 OOD)

- **Inbox** — 3 PDFs; **0** in-scope for local SEO/GEO
- **Overflow** — @sources/arxiv-rahman-2026-quantum-game-of-telephone-2608.03963-2026-08-05.md (quant-ph); @sources/arxiv-ghosh-2026-doubly-charged-higgs-exclusion-2608.03988-2026-08-05.md (hep-ph); @sources/arxiv-hariri-2026-test-time-scaling-reasoning-llms-2608.04001-2026-08-05.md (TTS/Scorio)
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @wiki/index.md, @sweeps/2026-08-05-daily.md
- **Phase-0** — `scripts/adopt_k152_phase0.sh` (all OUT-OF-SCOPE; Scorio HF Watch / over cap; 0 MB local adopt)
- **Phase-1** — no new SEO wires
- **Cross-wiki** — CCC TTS eval taxonomy; poker inference-regime delta
- **Atto / GuruWatcher / TipDrop / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API lanes still noisy (K141–K152)

## [2026-08-04] ingest | K151 arXiv API false-positive batch (3 OOD; 1 thin GEO steal)

- **Inbox** — 3 PDFs; **0** SEO Adopt; thin measurement steal from Pinterest VLM relevance
- **Overflow** — @sources/arxiv-wang-2026-vlm-relevance-web-scale-search-2608.02446-2026-08-04.md; @sources/arxiv-lin-2026-atumai-datacenter-control-plane-2608.02569-2026-08-04.md; @sources/arxiv-kumar-2026-smooth-reparameterizations-simplicial-2608.02576-2026-08-04.md
- **Updated** — @concepts/geo-visibility-measurement.md (engagement vs semantic relevance guardrail); @concepts/corpus-overflow-out-of-scope.md; @concepts/federated-daily-research-digest.md; @wiki/index.md; @sweeps/2026-08-04-daily.md
- **Phase-0** — `scripts/adopt_k151_phase0.sh` (all OUT-OF-SCOPE Adopt; smooth_reparam ~17KB wrong-domain; 0 MB local adopt)
- **Phase-1** — no new wires (no ADOPT/GO tools)
- **Cross-wiki** — CCC: VLM relevance guardrail + AtumAI agentic policy search
- **Atto / GuruWatcher / TipDrop / poker / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API lanes still noisy (K141–K151)

## [2026-08-03] ingest | K150 arXiv API false-positive batch (3 OOD)

- **Inbox** — 3 PDFs; **0** in-scope for local SEO/GEO (schema keyword collision on ExtractBench)
- **Overflow** — @sources/arxiv-tang-2026-multi-policy-peft-task-sequencing-2607.29601-2026-08-03.md (PEFT); @sources/arxiv-ferhatosmanoglu-2026-qasp-vector-search-policy-2607.29606-2026-08-03.md (QASP ANN); @sources/arxiv-zhang-2026-extractbench-schema-guided-extraction-2607.29677-2026-08-03.md (ExtractBench IE)
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @entities/tools/denseon-lateon.md (QASP infra note), @wiki/index.md, @sweeps/2026-08-03-daily.md
- **Phase-0** — `scripts/adopt_k150_phase0.sh` (all OUT-OF-SCOPE; ExtractBench GitHub 404 Watch; Quake related-not-this-paper Watch; 0 MB local adopt)
- **Phase-1** — no new SEO wires (no ADOPT/GO); DenseOn remains `policy_wired`
- **Cross-wiki** — Atto ExtractBench; CCC PEFT + QASP + ExtractBench; OSINT QASP thin
- **SEO hands-on / TipDrop / poker / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API lanes still noisy (K141–K150)

## [2026-07-31] phase1 | SEO/GEO adopt-wire backlog clear

- **Policy rule** — `.cursor/rules/cemini-phase1-seo-geo-wires.mdc` (alwaysApply): dual GEO Claude skills, Easy Review/GBP hands-on, DenseOn/LateOn probe
- **CLAUDE.md** — new Phase-1 section pointing at policy rule + `adopted-geo-tools` runtime skill
- **Entity stamps** — all 47 `wiki/entities/tools/*` now have `wire_status` ≠ unwired (6 policy / 3 runtime / 28 wont_wire / 10 deferred)
- **Runtime** — E-GEO / geo-optimizer / wondelai via `.cursor/skills/adopted-geo-tools/SKILL.md`; **MCP** `geo-optimizer` → `/Users/claudiobarone/.local/bin/geo-mcp` in `.cursor/mcp.json` (`uv tool install --with 'mcp>=1.0,<2' 'geo-optimizer-skill[mcp]'`)
- **Deferred next actions** — seomachine (DataForSEO), claude-ads (security issues), saas-boilerplate + Adopt-eligible pending Phase-0 (taste/social/notfair/goaccess/open-seo/digital-marketing-pro/pm-claude-skills)
- **Skipped** — Image-gen / 3D local wires; no Harbor/ORCA/AskChem MCP

## [2026-07-31] ingest | K149 arXiv API false-positive batch (4 OOD)

- **Inbox** — 4 PDFs; **0** in-scope for local SEO/GEO
- **Overflow** — @sources/arxiv-bushnell-2026-indelfreealigner-2607.27291-2026-07-31.md (genomics); @sources/arxiv-gong-2026-orca-bench-oncall-agents-2607.28545-2026-07-31.md (ORCA-bench); @sources/arxiv-jensen-2026-bootes-iii-styx-2607.28594-2026-07-31.md (Boo3/Styx); @sources/arxiv-heckman-2026-seiberg-dualities-ml-2607.28628-2026-07-31.md (Seiberg ML)
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @wiki/index.md, @sweeps/2026-07-31-daily.md
- **Phase-0** — `scripts/adopt_k149_phase0.sh` (all OUT-OF-SCOPE; ORCA Harbor ~50GB Watch; no SEO local adopt)
- **Cross-wiki** — CCC ORCA + Seiberg thin; Cyber ORCA oncall RCA
- **SEO hands-on / Atto / TipDrop / poker / prod** — SKIP
- **Hygiene** — geo-aeo + local-seo arXiv API lanes still noisy (K141–K149)

## [2026-07-30] ingest | K148 DenseOn/LateOn + 2 OOD

- **Inbox** — 3 PDFs; **1** in-scope (DenseOn/LateOn), **2** overflow
- **In-scope** — @sources/arxiv-sourty-2026-denseon-lateon-open-retrieval-2607.27178-2026-07-30.md → @entities/tools/denseon-lateon.md; GEO hub + adaptive-RAG / evidence / visibility backlinks
- **Overflow** — @sources/arxiv-shikhman-2026-latent-risk-neutral-densities-2607.27188-2026-07-30.md (RND options → OSINT+Gambling); @sources/arxiv-agarwal-2026-quadratic-axion-couplings-2607.27190-2026-07-30.md (axion → overflow only)
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @concepts/generative-engine-optimization.md, @wiki/index.md, @sweeps/2026-07-30-daily.md
- **Phase-0** — `scripts/adopt_k148_phase0.sh`: DenseOn/LateOn weights **Watch** (~600MB over cap); adopted `pylate`+`fast-plaid` (~7MB) under `raw-sources/tools/`
- **Briefs** — SEO hands-on passage probe; Atto multilingual retrieval; OSINT RND; Gambling RND; CCC RAG advisory (no prod scp)
- **TipDrop / poker / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API still noisy (2/3 FP this pass; DenseOn was a true hit)

## [2026-07-29] ingest | K147 arXiv API false-positive batch (3 OOD)

- **Inbox** — 3 PDFs; **0** in-scope for local SEO/GEO
- **Overflow** — @sources/arxiv-atlas-2026-large-r-jet-calibration-run2-2607.25893-2026-07-29.md (ATLAS jets); @sources/arxiv-yap-2026-eigenframe-topology-efg-2607.26008-2026-07-29.md (EFG topology); @sources/arxiv-dey-2026-quickgwecc-eccentric-pta-2607.26051-2026-07-29.md (QuickGWecc)
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @wiki/index.md, @sweeps/2026-07-29-daily.md
- **Phase-0** — `scripts/adopt_k147_phase0.sh` (all OUT-OF-SCOPE; no SEO local adopt)
- **Cross-wiki** — OSINT thin Bayes brief (QuickGWecc projection/shape); ATLAS + EFG overflow-only
- **SEO hands-on / Atto / David / tipdrop / poker / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API lane still noisy (K141–K147)

## [2026-07-28] voice pass | GuruWatcher Outlier + X Article ship-ready paste

- **Brief:** `briefs/2026-07-27_guruwatcher-outlier-x-article.md` upgraded outline → paste packages (Cyril voice, no em dashes, IP boundary intact)
- **Outlier title:** Discord Only Fires When the Newsletter Level Is Real (~1.5k)
- **X Article title:** The Newsletter Bot That Refuses to Hallucinate Levels (~0.9k+ after expand)
- **Notes:** @concepts/guruwatcher-outlier-x-article-notes.md → SHIP-READY
- **Voice table:** @concepts/x-account-voice-and-format.md row flipped Brief ready → SHIP-READY
- **Still optional before publish:** Discord fire screenshot; confirm Outlier issue # (likely 8)
- **Ship order:** Outlier first, X Article D+2

## [2026-07-27] brief | GuruWatcher Outlier + X Article pack

- **Brief:** `briefs/2026-07-27_guruwatcher-outlier-x-article.md` — dual spine for Outlier Weekly + X Article (alert-only newsletter → Discord)
- **Queue notes:** @concepts/guruwatcher-outlier-x-article-notes.md
- **Guardrails:** private repo (no fork CTA); alert-only; verbatim levels; Macro Charts named without dumping paid text
- **Blocked on ship:** one clean Discord fire screenshot (dedicated webhook installed on prod 2026-07-27)
- **Updated:** @wiki/index.md, @concepts/x-account-voice-and-format.md (published arc row)

## [2026-07-26] ingest | K146 arXiv API false-positive backlog (3 OOD from 2026-07-24)

- **Inbox** — 3 PDFs sitting since 2026-07-24 (also noted on 2026-07-25/26); **0** in-scope for local SEO/GEO
- **Overflow** — @sources/arxiv-breitenmoser-2026-beap-neutron-source-id-2607.21543-2026-07-26.md (BEAP neutron); @sources/arxiv-cai-2026-sequential-eqa-memory-bottlenecks-2607.21571-2026-07-26.md (sequential EQA memory); @sources/arxiv-qi-2026-bias-aware-compositional-robot-data-2607.21582-2026-07-26.md (factor-bias robot data)
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @wiki/index.md, @sweeps/2026-07-24-daily.md, @sweeps/2026-07-25-daily.md, @sweeps/2026-07-26-daily.md
- **Phase-0** — `scripts/adopt_k146_phase0.sh` (all OUT-OF-SCOPE; EQA GitHub URL truncated; no SEO local adopt)
- **Cross-wiki** — cyber (BEAP); OSINT + CCC + poker (EQA memory); TipDrop/David + Image Gen (factor bias)
- **SEO hands-on / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API lane still noisy (K141–K146)

## [2026-07-23] ingest | K145 arXiv API false-positive batch (3 OOD)

- **Inbox** — 3 PDFs; **0** in-scope for local SEO/GEO
- **Overflow** — @sources/arxiv-aragon-2026-gabidulin-constant-time-rqc-2607.20305-2026-07-23.md (Gabidulin/RQC); @sources/arxiv-tootoonian-2026-smell-in-stereo-2607.20307-2026-07-23.md (olfaction); @sources/arxiv-closset-2026-tqft-argyres-douglas-2607.20308-2026-07-23.md (hep-th TQFT)
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @wiki/index.md, @sweeps/2026-07-23-daily.md
- **Phase-0** — `scripts/adopt_k145_phase0.sh` (all OUT-OF-SCOPE; no public Gabidulin repo; no SEO local adopt)
- **Cross-wiki** — cybersecurity (Gabidulin constant-time RQC); smell + TQFT overflow-only
- **SEO hands-on / David / tipdrop / poker / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API lane still 3/3 false positives (K141–K145)

## [2026-07-22] ingest | K144 arXiv API false-positive batch (3 OOD)

- **Inbox** — 3 PDFs; **0** in-scope for local SEO/GEO
- **Overflow** — @sources/arxiv-smirnov-2026-erank-latent-image-richness-2607.19315-2026-07-22.md (ERank vision); @sources/arxiv-albert-2026-dark-matter-13mev-mkid-2607.19319-2026-07-22.md (hep-ex); @sources/arxiv-dokme-2026-malora-mara-state-space-adapters-2607.19326-2026-07-22.md (MaLoRA/MaRA)
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @wiki/index.md, @sweeps/2026-07-22-daily.md
- **Phase-0** — `scripts/adopt_k144_phase0.sh` (all OUT-OF-SCOPE; no code; no SEO local adopt)
- **Cross-wiki** — Image Gen + TipDrop/David (ERank); OSINT + CCC + poker (MaLoRA/MaRA); dark matter overflow-only
- **SEO hands-on / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API lane 3/3 false positives again (K141/K143/K144)

## [2026-07-20] ingest | K143 arXiv API false-positive batch (3 OOD)

- **Inbox** — 3 PDFs; **0** in-scope for local SEO/GEO
- **Overflow** — @sources/arxiv-mcclendon-2026-model-merging-joint-rl-2607.16062-2026-07-20.md (AppWorld merge vs joint RL); @sources/arxiv-egan-2026-complex-generalised-weighing-matrices-2607.16069-2026-07-20.md (CGW/QECC); @sources/arxiv-gnedin-2026-memoryless-best-choice-2607.16145-2026-07-20.md (memoryless best-choice)
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @wiki/index.md, @sweeps/2026-07-20-daily.md
- **Phase-0** — `scripts/adopt_k143_phase0.sh` (all OUT-OF-SCOPE; no SEO local adopt — maml-agent/appworld-rl OOD + GPU/vLLM)
- **Cross-wiki** — OSINT + CCC (model merging); cybersecurity (CGW→QECC); poker arena + Gambling (memoryless threshold)
- **SEO hands-on / David / tipdrop / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API lane 3/3 false positives again (same as K141)

## [2026-07-18] cursor | federate adopted-geo-tools skill

- **Canon** — `.cursor/skills/adopted-geo-tools/SKILL.md` (absolute `SEO_ROOT` so it works from any workspace)
- **Sync** — CCC `scripts/sync_federation_cursor_skills.sh` now includes `DOMAIN_SKILL_DIRS` → user-global + 20 workspaces (tipdrop, OSINT, gambling, CeminiSuite, …)
- **Operator** — re-run sync after editing this skill; no per-repo hand copies

## [2026-07-18] adopt | raise budget to 750MB + wire tools into use

- **Budget** — raised adopt cap **500 → 750 MB** for full E-GEO HF `data/` (~624 MB); total adopts ~696 MB
- **Wired** — `scripts/e_geo_rewrite_service_page.py` (used: competitive-style sample rewrite); `scripts/run_geo_audit.sh` (used: smoke audit of Google AI docs → `briefs/2026-07-18_geo-optimizer-audit.txt`); wondelai CRO Big-5 → @concepts/website-essentials-local-business.md; Cursor skill `.cursor/skills/adopted-geo-tools/SKILL.md`
- **Operator blockers** — fill @entities/companies/shop-1.md website URL for a real GEO audit; optional `npx skills add wondelai/skills/cro-methodology --global`
- **Updated** — entity pages e-geo / geo-optimizer / wondelai; @concepts/e-geo-universal-rewrite-playbook.md; `scripts/adopt_k142_phase0.sh`

## [2026-07-18] adopt | local CONDITIONAL-GO clones + E-GEO slim HF

- **E-GEO** — slim HF → `raw-sources/datasets/E-GEO` (~91 MB); skipped `queries_products` + `train_val_full` (≈558 MB)
- **geo-optimizer-skill** (K134) — `raw-sources/tools/geo-optimizer-skill` (~62 MB, MIT)
- **wondelai/skills** (K113) — `raw-sources/tools/wondelai-skills` (~8.7 MB, MIT)
- **Total adopt disk** — ~163 MB (under 500 MB)
- **Skipped (pending Phase-0)** — taste-skill, social-media-skills, notfair-toprank, goaccess, open-seo
- **Skipped (over budget / REFERENCE)** — full E-GEO HF corpus; agent-ready (no code)
- **Updated** — @entities/tools/e-geo.md, @entities/tools/geo-optimizer-skill.md, @entities/tools/wondelai-skills.md, @sources/arxiv-bagga-2026-e-geo-ecommerce-testbed-2511.20867-2026-07-18.md, `scripts/adopt_k142_phase0.sh`

## [2026-07-18] ingest | K142 E-GEO testbed + agent-ready websites (Brave rescue)

- **Inbox** — overnight empty (3 K141 dupes skipped); Brave rescue fetched 2 in-scope PDFs
- **Sources** — @sources/arxiv-bagga-2026-e-geo-ecommerce-testbed-2511.20867-2026-07-18.md; @sources/arxiv-elnaffar-2026-agent-ready-websites-2607.12056-2026-07-18.md
- **New** — @concepts/e-geo-universal-rewrite-playbook.md; @concepts/agent-ready-website-local-bm.md; @entities/tools/e-geo.md
- **Updated** — @concepts/generative-engine-optimization.md, @concepts/website-essentials-local-business.md, @concepts/geo-visibility-vector-protocol.md, @concepts/agent-first-web-atml-framework.md, @concepts/federated-daily-research-digest.md, @concepts/competitive-geo-citation-factors.md, @concepts/content-strategy-local.md, @concepts/schema-markup-local.md, @concepts/google-business-profile.md, @concepts/canonical-business-facts-geo.md, @sources/aggarwal-2024-geo-paper.md, @sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md, @wiki/index.md, @sweeps/2026-07-18-daily.md
- **Phase-0** — `scripts/adopt_k142_phase0.sh` (E-GEO CONDITIONAL-GO no LICENSE; agent-ready REFERENCE)
- **Local adopt** — `raw-sources/tools/E-GEO` (~1.4 MB shallow); HF dataset Watch (not pulled)
- **Briefs (2 hands-on)** — rewrite audit + agent-ready audit (gitignored `briefs/`)
- **Cross-wiki** — CCC thin steal `Cemini claude code CCC/briefs/2026-07-18_k142-agent-ready-websites-from-seo.md`
- **Poker / David / tipdrop / prod** — SKIP (no arena / ComfyUI / XSP hook)

## [2026-07-17] ingest | K141 arXiv API false-positive batch (3 OOD)

- **Inbox** — 3 PDFs; **0** in-scope for local SEO/GEO
- **Overflow** — @sources/arxiv-ronchini-2026-swift-bat-glimpse-2607.15130-2026-07-17.md (Swift BAT astrophysics); @sources/arxiv-sankar-2026-quantum-spin-zprime-ttbar-2607.15153-2026-07-17.md (HEP Z′); @sources/arxiv-dutta-2026-stigmergic-graph-memory-mapd-2607.15182-2026-07-17.md (SGM warehouse MAPD)
- **Updated** — @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k141_phase0.sh` (all OUT-OF-SCOPE; no local adopt)
- **Cross-wiki** — game-dev + OSINT briefs for SGM; poker arena delta (stigmergic spot-class ranking)
- **SEO hands-on / David / tipdrop / prod** — SKIP
- **Hygiene** — geo-aeo arXiv API lane 3/3 false positives again; consider query tighten

## [2026-07-16] ingest | K140 Martinez GEO critical survey + 2 OOD archives (3 arXiv)

- **Inbox** — 3 PDFs; GEO survey ingested; biosecurity + optomechanics overflow
- **Source (core)** — @sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md
- **New** — @concepts/geo-visibility-vector-protocol.md
- **Overflow** — @sources/arxiv-guntoro-2026-evo2-biosecurity-metagenomic-2607.14070-2026-07-16.md; @sources/arxiv-hyatt-2026-sail-membranes-optomechanical-2607.14089-2026-07-16.md
- **Updated** — @concepts/generative-engine-optimization.md, @concepts/geo-visibility-measurement.md, @concepts/competitive-geo-citation-factors.md, @concepts/ai-citation-sourcing-geo.md, @concepts/citation-verification-aeo.md, @sources/aggarwal-2024-geo-paper.md, @concepts/federated-daily-research-digest.md, @concepts/corpus-overflow-out-of-scope.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k140_phase0.sh` (survey REFERENCE; ancillary CSVs Adopt ~15KB; OOD no-adopt)
- **Local adopt** — `raw-sources/ancillary/arxiv-2607.14035/{literature_matrix,search_protocol}.csv`
- **Brief (1 hands-on)** — visibility vector probe protocol (`briefs/2026-07-16_k140-geo-visibility-vector-probe-protocol-hands-on.md`)
- **Cross-wiki** — cybersecurity brief for Evo2 biosecurity (`Cybersecurity wiki/briefs/2026-07-16_k140-evo2-biosecurity-metagenomic-probes-from-seo.md`)
- **Poker / David / prod** — SKIP (no arena / ComfyUI / XSP hook)

## [2026-07-15] ingest | K139 DeepSearch-World process-verified agentic search (1 arXiv)

- **Inbox** — 1 PDF (arXiv 2607.07820 DeepSearch-World) archived to `cemini-egress-fi:/opt/cemini-bulk/research/seo/`
- **Source** — @sources/arxiv-geng-2026-deepsearch-world-self-distillation-2607.07820-2026-07-15.md
- **New** — @concepts/process-verified-agentic-search-geo.md
- **Updated** — @concepts/evidence-ecosystem-geo.md, @concepts/generative-engine-optimization.md, @concepts/adaptive-rag-internal-linking-geo.md, @concepts/geo-visibility-measurement.md, @concepts/federated-daily-research-digest.md, @sources/arxiv-ye-2026-ecogeo-trajectory-aware-evidence-ecosystems-2605.12887-2026-07-04.md, @sources/score-2026-self-evolving-deep-research.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k139_phase0.sh` (REFERENCE/Watch; code+420K not released; no local adopt)
- **Brief (1 hands-on)** — entity-hit agent path audit (`briefs/2026-07-15_k139-entity-hit-agent-path-audit-hands-on.md`)
- **Poker delta** — OSINT `agents/devfun-poker-arena/briefs/2026-07-15_k139-deepsearch-scaffold-staged-reflection-delta.md` (on top of shipped K161 filter); mirrored to Gambling arena briefs
- **David / tipdrop** — SKIP (no ComfyUI/image path)
- **Prod scp** — SKIP (default wiki-only)
- **Federated note** — OSINT+Gambling already ingested 2026-07-13; SEO adds GEO operator angle

Append-only chronological log of wiki operations: scaffolding, ingests, lints, distributions. Most recent at top.

## [2026-07-14] style-pass | OW7 wikilint / contribution rate

- **Brief:** `briefs/2026-07-14_outlier-weekly-issue7-wikilint-contribution-rate.md` — voice pass vs `@concepts/x-account-voice-and-format.md`
- **Pass:** Cyril checklist (failure open, 4 modes, CLI+checklist, contribution rate, limitation)
- **Cuts:** "steal these names"; Not X / Not Y stack; bold lead-ins; Article #1/#2 insider aside; newsletter-admin closer; em dashes in paste + X replies

## [2026-07-08] style-pass | CXW/GEO/TH turnkey postmortem Article (new after Jul 6)

- **New Article notes:** `@concepts/x-article-cxw-geo-th-postmortem-notes.md` — companion to published Jul 6 vindication; hook = right on sale / wrong on pop
- **Paste brief (OSINT):** `Desktop/OSINT WORKSPACE/briefs/2026-07-08_cxw-geo-th-turnkey-postmortem-x-article.md`
- **Voice table:** operator Jul 6 LIVE + Jul 8 Ready rows on `@concepts/x-account-voice-and-format.md`
- **Steal:** flat-close failure open; 6 right / 5 wrong; fade stack; TH cousin not clone; Aug 5/6 CTA
- **Avoid:** re-vindicating the 8-K; Dilley turnkey as base case; em dashes; line-per-sentence paste

## [2026-07-06] brief | CXW turnkey 8-K vindication — X Article + GEO chase

- **Brief:** `briefs/2026-07-06_cxw-turnkey-8k-vindication-x-article.md` — paste-ready X Article; opener tweet + reply stack; GEO sympathy/chase frame
- **Event:** CoreCivic 8-K (Jul 2 close / Jul 6 announce) — Cal City $732.6M + Otay $739.2M = **$1.5B gross**, **~$1.1B net**; retains ICE management contracts; additional ICE sale talks
- **Updated:** `briefs/2026-07-03_cxw-geo-outlier-front-to-back-thesis.md` (vindication addendum), `briefs/2026-06-26_cxw-geo-detention-turnkey-wsb-handoff.md`, `wiki/index.md`
- **Primary:** https://ir.corecivic.com/news-releases/news-release-details/corecivic-sells-two-detention-facilities

## [2026-07-04] ingest | K138 daily digest — EcoGEO trajectory-aware evidence ecosystems (1 arXiv)

- **Inbox** — 1 PDF (arXiv 2605.12887 EcoGEO) archived to `cemini-egress-fi:/opt/cemini-bulk/research/seo/`
- **Source** — @sources/arxiv-ye-2026-ecogeo-trajectory-aware-evidence-ecosystems-2605.12887-2026-07-04.md
- **New** — @concepts/evidence-ecosystem-geo.md
- **Updated** — @concepts/generative-engine-optimization.md, @concepts/adaptive-rag-internal-linking-geo.md, @concepts/ai-citation-sourcing-geo.md, @concepts/geo-visibility-measurement.md, @concepts/content-strategy-local.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k138_phase0.sh` (EcoGEO REFERENCE; no public-web synthetic evidence adoption)
- **Brief (1 hands-on)** — evidence ecosystem GEO audit (`briefs/2026-07-04_k138-evidence-ecosystem-geo-audit-hands-on.md`)
- **Operator note** — coordinate real evidence paths (GBP/site/reviews/citations); do not fabricate support pages or planted forum/social proof

## [2026-07-03] ingest | K137 daily digest — GBP missing reviews + additive restrictions (0 arXiv)

- **Inbox** — empty (no PDFs)
- **Source** — @sources/seroundtable-2026-gbp-review-loss-restrictions-2026-07-03.md
- **Updated** — @concepts/reviews-reputation-management.md, @concepts/google-business-profile.md, @entities/platforms/google-business-profile.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k137_phase0.sh` (SERoundtable REFERENCE; first-party GBP Help already K136; vendor rows skipped)
- **Brief (1 hands-on)** — GBP review loss + restriction response (`briefs/2026-07-03_k137-gbp-review-loss-restriction-response-hands-on.md`)
- **Operator note** — distinguish platform bug / suspicious-review pause from policy restriction; preserve weekly review-count screenshots

## [2026-07-03] brief | CXW/GEO Outlier front-to-back article handoff

- **Brief (1 master):** `briefs/2026-07-03_cxw-geo-outlier-front-to-back-thesis.md` — article spine from warehouse failure → turnkey pivot → funding → site sequencing → Cal City/Bonta → Florence/J&A trap → recorder monitor negatives → BOP closure counterpoint.
- **Updated:** `briefs/2026-06-26_cxw-geo-detention-turnkey-wsb-handoff.md` now points to the master Outlier brief; `wiki/index.md` adds the brief row.
- **Frame:** real thesis / dirty timing; base case contract continuity, upside tail turnkey 8-K; avoid overclaims on BOP privatization, Nantucket jet routing, Florence CAFCC, and options flow.

## [2026-07-02] ingest | K136 daily digest — Google Search Central first-party GEO + GBP reviews (0 arXiv)

- **Inbox** — empty (10 non-arXiv hits; wiki dupes skipped)
- **Sources** — Search Central AI optimization guide; GBP Help tips to get more reviews (3474122)
- **New** — @sources/google-search-central-2026-ai-optimization-guide.md, @sources/google-business-profile-help-2026-tips-get-more-reviews-3474122.md
- **Updated** — @concepts/generative-engine-optimization.md, @concepts/reviews-reputation-management.md, @concepts/review-response-templates.md, @concepts/schema-markup-local.md, @concepts/google-business-profile.md, @sources/techwyse-2026-google-good-seo-is-good-geo-kraham-2026-06.md, @entities/tools/geo-optimizer-skill.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k136_phase0.sh` (both CORE first-party; vendor rows skipped)
- **Brief (1 hands-on)** — Google first-party GEO + review checklist (`briefs/2026-07-02_k136-google-first-party-geo-review-checklist-hands-on.md`)
- **Wiki-cited brief audit** — K120–K135 hands-on suite confirmed git-tracked

## [2026-07-01] ingest | K135 daily digest — review compliance + HubSpot AEO primer (0 arXiv)

- **Inbox** — empty (Žatuchin + KARLA dupes; non-arXiv skipped)
- **Sources** — Salon Today 2026-06-24 review gating / FTC enforcement; HubSpot 2026-06-29 AI search optimization primer
- **New** — @sources/salon-today-2026-review-gating-ftc-compliance-dodson-2026-06-24.md, @sources/hubspot-2026-ai-search-optimization-aeo-primer-2026-06-29.md
- **Updated** — @concepts/reviews-reputation-management.md, @concepts/generative-engine-optimization.md, @concepts/geo-visibility-measurement.md, @entities/platforms/google-business-profile.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k135_phase0.sh` (Salon Today REFERENCE; HubSpot REFERENCE; news dupes skipped)
- **Brief (1 hands-on)** — review compliance vendor audit (`briefs/2026-07-01_k135-review-compliance-vendor-audit-hands-on.md`)
- **Wiki-cited brief audit** — K120–K134 hands-on suite confirmed git-tracked (21 briefs)

## [2026-06-30] ingest | K134 daily digest — zero-click AEO + geo-optimizer-skill Phase-0 (0 arXiv)

- **Inbox** — empty (KARLA dupe skipped)
- **Sources** — HousingWire 2026-06-29 zero-click AEO / GBP AI feed
- **New** — @sources/housingwire-2026-answer-engine-optimization-zero-click-gbp-2026-06-29.md, @entities/tools/geo-optimizer-skill.md
- **Updated** — @concepts/generative-engine-optimization.md, @concepts/google-business-profile.md, @concepts/geo-visibility-measurement.md, @entities/tools/geo-seo-claude.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k134_phase0.sh` (HousingWire REFERENCE; Auriti CONDITIONAL-GO — ignore llms.txt for Google)
- **Brief (1 hands-on)** — AI citation vs click audit (`briefs/2026-06-30_k134-ai-citation-vs-click-audit-hands-on.md`)

## [2026-06-29] ingest | K133 daily digest — wiki-cited brief backfill (0 arXiv)

- **Inbox** — empty (4 arXiv dupes; non-arXiv skipped)
- **Brief backfill (git-track)** — K124 adversarial citation audit; K100 two-shop internal-link audit + eastside example
- **Updated** — @concepts/citation-verification-aeo.md (K124 hands-on link)
- **Phase-0** — `scripts/adopt_k133_phase0.sh` (no new sources; news dupes skipped)

## [2026-06-28] ingest | K132 daily digest — KARLA canonical-fact KB layer (1 arXiv)

- **Sources** — arXiv 2606.26807 (Crespin KARLA knowledge-base augmented retrieval)
- **New** — @sources/arxiv-crespin-2026-karla-knowledge-base-augmented-retrieval-2606.26807-2026-06-28.md, @concepts/canonical-business-facts-geo.md
- **Updated** — @concepts/generative-engine-optimization.md, @concepts/citation-verification-aeo.md, @concepts/schema-markup-local.md, @concepts/google-business-profile.md, @concepts/reviews-reputation-management.md (incentivized-review news cite), @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k132_phase0.sh` (KARLA REFERENCE; news dupes skipped)
- **Brief (1 hands-on)** — canonical fact sync audit (`briefs/2026-06-28_k132-canonical-fact-sync-audit-hands-on.md`)
- **PDF** → `raw-sources/` + egress-fi archive; inbox cleared
- **Operator note** — KB edits beat parametric memory in paper; 1-hop RAG can ignore retrieved facts `[NEEDS VERIFICATION 2026-06-28]` on local hours/price queries

## [2026-06-27] ingest | K131 daily digest — Google entity-model news lane (0 arXiv)

- **Inbox** — empty (0 PDFs; paper hits non-arXiv or wiki dupes)
- **Sources** — Search Engine Land 480625 (Google LLM patent entity characterization); TechWyse/Kraham “Good SEO is good GEO” (Think with Google June 2026 summary)
- **New** — @sources/searchengineland-2026-google-llm-patent-entity-characterization-480625.md, @sources/techwyse-2026-google-good-seo-is-good-geo-kraham-2026-06.md
- **Updated** — @concepts/generative-engine-optimization.md, @concepts/schema-markup-local.md, @concepts/google-business-profile.md, @entities/tools/google-search-console.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k131_phase0.sh` (both REFERENCE journalism; R2/R4–R6 syndicated rows SKIP)
- **Brief (1 hands-on)** — entity evidence audit (`briefs/2026-06-27_k131-entity-evidence-audit-hands-on.md`)
- **News skipped** — vendor playbook (R2), KBEW dental syndication (R4–R6)
- **Operator note** — patent ≠ product; llms.txt not needed for Google Search per June 2026 messaging `[NEEDS VERIFICATION 2026-06-27]`

## [2026-06-26] ingest | K130 daily digest — Žatuchin citation sourcing (earned-media GEO layer) (1 arXiv)

- **Sources** — arXiv 2606.25787 (Žatuchin LLM brand reputation sourcing across languages)
- **New** — @sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md, @concepts/ai-citation-sourcing-geo.md
- **Updated** — @concepts/citation-building.md, @concepts/competitive-geo-citation-factors.md, @concepts/geo-visibility-measurement.md, @concepts/generative-engine-optimization.md, @concepts/multilingual-geo-audit.md, @entities/tools/rankfor-ai.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k130_phase0.sh` (Žatuchin REFERENCE; Zenodo + open.rankfor.ai data; no SaaS audit)
- **Brief (1 hands-on)** — earned-media citation audit (`briefs/2026-06-26_k130-earned-media-citation-audit-hands-on.md`)
- **PDF** → `raw-sources/` + egress-fi archive; inbox cleared
- **Operator note** — 85.7% third-party citation share; Wikipedia #1 in 11/12 languages `[NEEDS VERIFICATION 2026-06-26]` on local barbershop queries

## [2026-06-25] ingest | K129 daily digest — ABSA peer-review aspect steal + duplicate re-archives (3 arXiv)

- **Sources** — arXiv 2606.24188 (Han ABSA peer-review evolution); 2606.20853 ReSequel re-fetch (K128 duplicate); 2606.19893 MetaResearcher re-fetch (K124 duplicate)
- **New** — @sources/arxiv-han-2026-aspect-sentiment-peer-review-evolution-2606.24188-2026-06-25.md
- **Updated** — @concepts/reviews-reputation-management.md, @concepts/review-response-templates.md, @concepts/corpus-overflow-out-of-scope.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k129_phase0.sh` (Han REFERENCE LICENSE null; ReSequel + MetaResearcher DUPLICATE-ARCHIVE)
- **Briefs (1 hands-on)** — negative review aspect-theme audit
- **Brief backfill** — git-track K120–K127 hands-on suite cited in wiki (`briefs/2026-06-16_k120-*` … `2026-06-23_k127-*`)
- **PDFs** → `raw-sources/` + egress-fi archive; inbox cleared

## [2026-06-24] ingest | K128 daily digest — Language Blind Spot multilingual GEO + review polarity bias + archives (5 arXiv)

- **Sources** — arXiv 2606.23165 (Žatuchin Language Blind Spot); 2606.22745 (Rajiv sentiment polarity); 2606.20853 ReSequel → @osint-wiki brief; 2606.19893 MetaResearcher re-fetch (K124 duplicate); 2606.19635 Token Factory archive
- **New** — @sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md, @concepts/multilingual-geo-audit.md, @sources/arxiv-rajiv-2026-sentiment-polarity-bias-reviews-2606.22745-2026-06-24.md, @entities/tools/rankfor-ai.md, @sources/arxiv-chen-2026-token-factory-recommendation-2606.19635-2026-06-24.md
- **Updated** — @concepts/geo-visibility-measurement.md, @concepts/generative-engine-optimization.md, @concepts/llm-reputation-signals-geo.md, @concepts/reviews-reputation-management.md, @concepts/review-response-templates.md, @concepts/federated-daily-research-digest.md, @entities/tools/ranqo.md, @concepts/corpus-overflow-out-of-scope.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k128_phase0.sh` (Žatuchin/Rajiv REFERENCE; ReSequel CONDITIONAL-GO @osint-wiki; MetaResearcher DUPLICATE-ARCHIVE; Token Factory REFERENCE-ARCHIVE)
- **Briefs (2 hands-on)** — multilingual GEO query audit; review sentiment polarity check
- **Cross-wiki (OSINT)** — `briefs/2026-06-24_k128-resequel-llm-query-rewrite-handoff.md`
- **PDFs** → `raw-sources/` + egress-fi archive; inbox cleared
- **Operator note** — English-only GEO audits understate local-champion recommendation share (+0.80 home-language shift vs +0.15 for globals) `[NEEDS VERIFICATION 2026-06-24]` on barbershop queries

## [2026-06-23] ingest | K127 daily digest — PEBM verified-mention framework + MetaResearcher re-archive (2 arXiv)

- **Sources** — arXiv 2606.21595 (Varga PEBM); 2606.19893 MetaResearcher re-fetch (K124 duplicate archive)
- **New** — @sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md, @concepts/per-entity-bias-mapping-geo.md
- **Updated** — @concepts/geo-visibility-measurement.md, @concepts/citation-verification-aeo.md, @concepts/generative-engine-optimization.md, @concepts/llm-brand-bias-geo-competition.md, @entities/tools/ranqo.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k127_phase0.sh` (PEBM REFERENCE Zenodo; MetaResearcher DUPLICATE-ARCHIVE)
- **Brief (1 hands-on)** — PEBM verified-mention audit (raw vs verified mention rate)
- **PDFs** → `raw-sources/` + egress-fi archive; inbox cleared
- **Operator note** — high-salience brands: 52.7% fabricated citations vs 37.9% Tier 3 in Varga B2B panel `[NEEDS VERIFICATION 2026-06-23]` on local barbershop queries

## [2026-06-22] ingest | K126 daily digest — duplicate re-archive batch (2 arXiv) + GBP news lane

- **Sources** — arXiv 2606.16902 (BinTrack re-fetch — K125 game-dev); 2606.19893 (MetaResearcher re-fetch — K124 OSINT)
- **Updated (SEO)** — @concepts/federated-daily-research-digest.md, @concepts/google-business-profile.md (Collected Info + GA4/Gemini feature drift), @wiki/log.md
- **Phase-0** — `scripts/adopt_k126_phase0.sh` (both DUPLICATE-ARCHIVE; no new briefs)
- **PDFs** → `raw-sources/` + egress-fi archive; inbox cleared
- **News lane** — GBP Collected Info section, GBP+GA4+Gemini integration flagged `[NEEDS VERIFICATION 2026-06-22]`

## [2026-06-21] ingest | K125 daily digest — BinTrack spatial QA cross-wiki + duplicate re-archives (3 arXiv)

- **Sources** — arXiv 2606.16902 (BinTrack → game-dev); 2606.19893 + 2606.20235 re-fetch (K124/K123 duplicate archive)
- **Updated (SEO)** — @concepts/federated-daily-research-digest.md, @concepts/near-me-search.md, @wiki/log.md
- **Phase-0** — `scripts/adopt_k125_phase0.sh` (BinTrack CONDITIONAL-GO no LICENSE; MetaResearcher + ScholarQuest DUPLICATE-ARCHIVE)
- **Brief (1 hands-on)** — route-context local query audit (beyond static near-me)
- **Cross-wiki (game-dev)** — @game-dev-wiki/sources/arxiv-na-2026-binary-tracking-spatial-qa-2606.16902-2026-06-21.md, @game-dev-wiki/entities/tools/binarytracking.md, brief `briefs/research/bintrack-spatial-qa-steal-2026-06-21.md`
- **PDFs** → `raw-sources/` + egress-fi archive; inbox cleared
- **Operator note** — route-aware AI queries ("on the way home") may diverge from radius near-me rankings `[NEEDS VERIFICATION 2026-06-21]`

## [2026-06-20] brief | WC Ticket Monitor — SEO advertising handoff

- **Brief** — `briefs/2026-06-20_wc-ticket-monitor-seo-advertising-handoff.md` (ready-for-draft)
- **Product** — https://github.com/cemini23/wc-ticket-monitor — hourly knockout ticket price alerts (FIFA official + TicketWave); distinct from World Cup Bot (PM)
- **Lane** — WC fans + OSS builders; X Article/thread, optional Outlier Weekly, GitHub topics
- **Wiki stubs queued** — `entities/tools/wc-ticket-monitor.md`, `concepts/wc-ticket-monitor-search-discovery.md`

## [2026-06-20] ingest | K124 daily digest — MetaResearcher adversarial deep research + ScholarQuest re-archive (2 arXiv)

- **Sources** — arXiv 2606.19893 (MetaResearcher → OSINT); 2606.20235 (ScholarQuest re-fetch — K123 duplicate archive)
- **Updated (SEO)** — @concepts/federated-daily-research-digest.md, @concepts/citation-verification-aeo.md, @concepts/agent-first-web-atml-framework.md, @entities/tools/geo-seo-claude.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k124_phase0.sh` (MetaResearcher REFERENCE; ScholarQuest DUPLICATE-ARCHIVE, LICENSE still null)
- **Briefs (1 hands-on)** — adversarial AI citation audit for local queries
- **Cross-wiki (OSINT)** — @osint-wiki/sources/arxiv-metaresearcher-deep-research-2606.19893-2026-06-20.md, @osint-wiki/entities/tools/metaresearcher.md, brief `briefs/2026-06-20_k124-metaresearcher-deep-research-handoff.md`
- **ScholarQuest** — OSINT pages unchanged (K123); GitHub LICENSE re-check 2026-06-20: still null
- **PDFs** → `raw-sources/` + egress-fi archive; inbox cleared
- **Operator note** — one plausible misinformation source can collapse AI answer accuracy `[NEEDS VERIFICATION 2026-06-20]` on local near-me queries

## [2026-06-19] ingest | K123 daily digest — Ranqo GEO at scale + ScholarQuest cross-wiki (2 arXiv)

- **Sources** — arXiv 2606.20065 (Kumar/Ranqo production GEO); 2606.20235 (ScholarQuest agentic academic search → OSINT)
- **New (SEO)** — @sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md, @entities/tools/ranqo.md
- **Updated (SEO)** — @concepts/geo-visibility-measurement.md, @concepts/generative-engine-optimization.md, @concepts/competitive-geo-citation-factors.md, @concepts/content-strategy-local.md, @concepts/citation-building.md, @concepts/federated-daily-research-digest.md, @entities/tools/local-falcon.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k123_phase0.sh` (Ranqo REFERENCE; ScholarQuest CONDITIONAL-GO — no GitHub LICENSE)
- **Brief (1 hands-on)** — Ranqo-style tier + per-engine mention baseline
- **Cross-wiki (OSINT)** — @osint-wiki/sources/arxiv-scholarquest-agentic-academic-search-2606.20235-2026-06-19.md, @osint-wiki/entities/tools/scholarquest.md, brief `briefs/2026-06-19_k123-scholarquest-digest-eval-handoff.md`
- **PDFs** → `raw-sources/` + egress-fi archive; inbox cleared
- **Operator note** — listicles 21% citations; own domain 2.9%; track mention not sentiment `[NEEDS VERIFICATION 2026-06-19]` on local queries

## [2026-06-18] ingest | K122 daily digest — incumbent brand bias / GEO competition (1 arXiv)

- **Source** — arXiv 2606.17443 (Chu & Hou): Conditional Monopoly (IAI=10.0 at identical specs); +0.075★ breaks lock-in; authority BSV +0.17★; multi-brand GEO PD (+0.802→+0.007 at k=9)
- **New** — @sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md, @concepts/llm-brand-bias-geo-competition.md
- **Updated** — @concepts/generative-engine-optimization.md, @concepts/competitive-geo-citation-factors.md, @concepts/llm-reputation-signals-geo.md, @concepts/geo-visibility-measurement.md, @concepts/content-strategy-local.md, @concepts/federated-daily-research-digest.md, @sources/arxiv-hu-2025-adversarial-attacks-llm-search-2501.00745-2026-06-10.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k122_phase0.sh` (REFERENCE — academic audit; no code)
- **Brief (1 hands-on)** — Conditional Monopoly / tie-breaker audit for local service queries
- **PDF** → `raw-sources/` + egress-fi archive; inbox cleared
- **Operator note** — break spec ties with real rating/price/volume; do not fabricate clinical authority claims `[NEEDS VERIFICATION 2026-06-18]` on barbershop queries

## [2026-06-17] ingest | K121 daily digest — WikiKV hierarchical wiki storage (1 arXiv)

- **Source** — arXiv 2606.14275 (WikiKV): path-indexed KV for LLM-curated hierarchical wikis; O(1) GET/LS; NAV(q,B) search-accelerated routing; WeChat production; AUTHTRACE 63.2% E2E correctness
- **New** — @sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md, @entities/tools/wikikv.md
- **Updated** — @concepts/obsidian-integration.md, @concepts/adaptive-rag-internal-linking-geo.md, @concepts/federated-daily-research-digest.md, @concepts/generative-engine-optimization.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k121_phase0.sh` (REFERENCE — no public code)
- **Brief (1 prod)** — hierarchical wiki storage federation steal → **scp prod**
- **Cross-wiki** — @osint-wiki/sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md, @osint-wiki/entities/tools/wikikv.md, @osint-wiki/concepts/wiki-tooling-evaluation.md update
- **PDF** → `raw-sources/` + egress-fi archive; inbox cleared

## [2026-06-16] ingest | K120 daily digest — 3 arXiv full ingest

- **Sources** — arXiv 2606.16344 (Baig hotel LLM reputation conjoint); 2606.11290 (FlowBank); 2606.17029 (DeepRubric)
- **New** — @sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md, @sources/arxiv-yuan-2026-flowbank-agentic-workflows-2606.11290-2026-06-16.md, @sources/arxiv-zhu-2026-deeprubric-evidence-tree-2606.17029-2026-06-16.md, @concepts/llm-reputation-signals-geo.md, @entities/tools/flowbank.md, @entities/tools/deeprubric-code.md
- **Updated** — @concepts/generative-engine-optimization.md, @concepts/competitive-geo-citation-factors.md, @concepts/reviews-reputation-management.md, @concepts/geo-visibility-measurement.md, @concepts/federated-daily-research-digest.md, @wiki/index.md
- **Phase-0** — `scripts/adopt_k120_phase0.sh` (DeepRubric Apache-2.0 REFERENCE; FlowBank project-page REFERENCE; hotel audit no code)
- **Briefs (3)** — hands-on reputation-signal audit; FlowBank conductor prod handoff; DeepRubric CCC wiki-ingest handoff → **prod scp (1):** FlowBank conductor brief
- **Cross-wiki** — CCC stubs: agent-workflow-portfolio-optimization, evidence-tree-rubric-supervision, tool entities
- **PDFs** → `raw-sources/` + egress-fi archive; inbox cleared
- **Operator note** — management response null at LLM selection; prioritize rating + price + volume `[NEEDS VERIFICATION 2026-06-16]` on barbershop queries

## [2026-06-16] cross-wiki handoff | dev.fun Tournament S1 Article brief

- **Brief** — `briefs/2026-06-16_devfun-tournament-s1-article-handoff.md` (full data pack: hero stats, top-5 field, loss attribution, Article beats)
- **Stub** — @concepts/devfun-tournament-s1-article-notes.md (queue + hook)
- **Source** — @osint-wiki/agents/devfun-poker-arena/briefs/2026-06-12_why-cemini-last-s1.md + S1 export on `cemini-prod`
- **Lane** — X Article: prediction markets + agent OSS; Playground #1 → Tournament bust narrative

## [2026-06-10] ingest | AI visibility uncertainty + LLM search manipulation game theory (2 arXiv)

- **Sources** — 2603.08924 Sielinski (IQRush): citation visibility as stochastic estimators; bootstrap CI; platform sample-size targets; critique of GEO-BENCH without uncertainty. 2501.00745 Hu (ASU): ranking manipulation as Infinitely Repeated Prisoners' Dilemma; non-monotonic attack success; futile defense regions.
- **New** — @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md, @sources/arxiv-hu-2025-adversarial-attacks-llm-search-2501.00745-2026-06-10.md, @concepts/geo-visibility-measurement.md
- **Updated** — @concepts/generative-engine-optimization.md (uncertainty bands + adversarial dynamics subsections; step 7 repeated sampling), @sources/aggarwal-2024-geo-paper.md (CI gap in GEO-BENCH), @concepts/competitive-geo-citation-factors.md, @entities/tools/local-falcon.md (SAIV noise floor), @concepts/federated-daily-research-digest.md, @wiki/index.md
- **PDFs** → `raw-sources/`; inbox cleared
- **Operator note** — local near-me queries untested `[NEEDS VERIFICATION 2026-06-10]`; SearchGPT may need >200 queries for stable share CI; do not attribute Aggarwal-scale lifts without pre/post bootstrap CIs

## [2026-06-09] style-pass | Posts.docx K108 | OSINT ingest

- **Batch** — @osint-wiki/sources/trading-posts-compilation-8-2026-06-09.md (6 posts)
- **Updated** — @concepts/x-account-voice-and-format.md (exemplars: @GodEyeDotFun, @raulvk, @Av1dlive, @0x_rody, @ArrakisFinance)
- **Formatting** — @Av1dlive THE HIVE docx has line-per-sentence breaks — merge before Article paste

## [2026-06-09] style-pass | Posts.docx K107 | OSINT ingest

- **Batch** — @osint-wiki/sources/trading-posts-compilation-7-2026-06-09.md (17 posts)
- **Updated** — @concepts/x-account-voice-and-format.md (exemplars: @PawelHuryn dynamic workflows, @cyrilXBT skills course, @Zephyr_hg Gmail MCP)
- **Steal** — workflow-as-code orchestrator pattern; Skills Purpose/Trigger template
- **Avoid** — @igor_mikerin referral-first PM posts; @maqxbt unverified Polystrat stats without primary source

## [2026-06-08] style-pass | Posts.docx K106 | OSINT ingest

- **Batch** — @osint-wiki/sources/trading-posts-compilation-6-2026-06-08.md (6 posts)
- **Updated** — @concepts/x-account-voice-and-format.md (exemplars: @whydeso, @RuujSs, @Zephyr_hg n8n, @AlphaCartell DexScreener MCP)
- **Article beats** — none new (n8n machine = SEO workflow lane only)

## [2026-06-08] ingest | Caption Injection multimodal G-SEO (1 arXiv)

- **Source** — 2511.04080 Caption Injection: first multimodal G-SEO; O-A-S caption → refine → inject into page text; MRAMG benchmark; +1.12% G-EVAL vs +0.71% fluency in multimodal sim; uniqueness dimension lift largest
- **New** — @sources/arxiv-caption-injection-2511.04080-2026-06-08.md
- **Updated** — @concepts/generative-engine-optimization.md (multimodal subsection + playbook step 8b), @concepts/competitive-geo-citation-factors.md (uniqueness/visual differentiation), @concepts/content-strategy-local.md (gallery caption pattern), @concepts/on-page-seo-local.md (caption injection under Image SEO), @concepts/google-business-profile.md (GBP ↔ website visual mirror), @concepts/federated-daily-research-digest.md, @sources/aggarwal-2024-geo-paper.md (MRAMG replication caveat), @wiki/index.md
- **PDF** → `raw-sources/`; inbox cleared
- **Operator note** — absolute lifts modest; local pages untested `[NEEDS VERIFICATION 2026-06-08]`; do not replace Aggarwal fluency/statistics/quotation stack

## [2026-06-07] style-pass | Posts.docx K103 | 5 long-forms | authors: @eng_khairallah1, @smaaaliy, @zeuuss_01, @BimbaCrypto, @RitOnchain

## [2026-06-06] smoke-test | AI Text Humanizer — NO-GO for marketing workflow

- **Installed** — `tools/ai-text-humanizer/` + `~/.cemini/venvs/ai-text-humanizer`; `scripts/run_ai_humanizer.sh`, `scripts/ai_humanizer_smoke_test.py`
- **Verdict** — academicizes copy (contractions expanded, random `Therefore/Furthermore`); worse for GBP/IG/service pages
- **Workflow** — explicitly excluded from @concepts/content-strategy-local.md; use marketingskills + Claude fluency edit instead
- **Entity** — @entities/tools/ai-text-humanizer-app.md upgraded CONDITIONAL-GO → **NO-GO**

## [2026-06-06] check | briefs/ — K102 ingest + two-shop audit links

- **Easy Review:** 0 new briefs since 2026-05-08 (`manual_17` only; below ≥3 pattern threshold)
- **K102:** `briefs/2026-06-06_k102-seo-ai-humanizer-from-osint.md` → @entities/tools/ai-text-humanizer-app.md + @sources/multi-wiki-tool-eval-k102-2026-06-06.md
- **Hands-on (staged):** linked `briefs/2026-06-05_two-shop-internal-link-audit.md` + eastside example from @concepts/adaptive-rag-internal-linking-geo.md Part B
- **No action:** 40+ historical briefs already wiki-ingested per prior log entries; Issue 3 / X Article / Reddit briefs remain hands-on deliverables

## [2026-06-06] ingest | K101 federation morning — Med-V1 evidence attribution (1 arXiv)

- **Source** — 2603.05308 Med-V1: 3B SLM for biomedical evidence attribution; GPT-4o/GPT-5 citation hallucination rates 43–56% on standard formats
- **Concept** — `citation-verification-aeo` (new): claim–source verification loop for operators
- **Updated** — @concepts/generative-engine-optimization.md, @concepts/competitive-geo-citation-factors.md, @concepts/adaptive-rag-internal-linking-geo.md, @concepts/federated-daily-research-digest.md, @sources/davidson-2026-factual-gv-gap.md, @sources/ptah-2026-verifiable-multimodal-deep-research.md
- **PDF** → `raw-sources/`; inbox cleared

## [2026-06-05] deep-pass | K100 arXiv — adaptive RAG + WebKnoGraph

- **Deep-read** @sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md — routing tree, DevOps vs MuSiQue tradeoffs, digest ingest implications
- **Deep-read** @sources/arxiv-webknograph-internal-linking-2606.06106-2026-06-05.md — four-metric pre-deploy checklist, five strategies, Kalicube findings
- **Upgraded** @concepts/adaptive-rag-internal-linking-geo.md — full synthesis (Part A orchestration + Part B link graph)
- **Updated** @concepts/generative-engine-optimization.md, @concepts/on-page-seo-local.md, @concepts/federated-daily-research-digest.md — bidirectional backlinks + operator subsections
- **Updated** @wiki/index.md
- **Brief staged:** `briefs/2026-06-05_two-shop-internal-link-audit.md` — hands-on 2-shop audit template

## [2026-06-05] ingest | K100 federation morning — adaptive RAG + WebKnoGraph (2 arXiv)

- **Sources** — 2606.05658 agent-orchestrated adaptive RAG; 2606.06106 WebKnoGraph internal linking
- **Concept** — `adaptive-rag-internal-linking-geo`
- **PDFs** → librarian; inbox cleared

## [2026-06-04] ingest | digest inbox — 2 arXiv (MEMENTO + SCORE)

**Digest sweep:** `wiki/sweeps/2026-06-04-daily.md` — 2 NEW PDFs from overnight Exa fetch.

- **New:** @sources/memento-2026-web-learning-signal-low-data.md — web as learning signal; AET + dual memory; sales/legal low-data eval `[TENTATIVE]`
- **New:** @sources/score-2026-self-evolving-deep-research.md — SCORE co-evolution framework; static LLM-judge saturation problem
- **Updated:** @concepts/generative-engine-optimization.md — deep-research synthesis cluster extended
- **Updated:** @concepts/federated-daily-research-digest.md, @concepts/high-ticket-smb-lead-generation.md
- **Updated:** @sources/ptah-2026-verifiable-multimodal-deep-research.md, @sources/davidson-2026-factual-gv-gap.md — verifier-harness backlinks
- **Moved:** 2 PDFs → `raw-sources/`
- **Lint:** 0 orphans, 0 bidirectional gaps, 0 dangling links

## [2026-06-04] lint | wiki health pass

- **Lint:** 0 orphans, 0 bidirectional gaps, 0 dangling `related:` (3 cross-wiki dangling unchanged — OSINT/cybersec paths)
- **Fixed:** sweep frontmatter (`sweeps/2026-06-03-daily.md`), 4 bidirectional gaps from prior K90/K97 passes

## [2026-06-04] style-pass | Posts.docx K98 | 3 long-forms | authors: horizon_trade_x, YahavFuchs, mphrediction (+ Voxyz funnel note)

- **New:** `sources/trading-posts-compilation-18-2026-06-04.md` — K98 cross-route stub
- **Updated:** @concepts/x-account-voice-and-format.md — YahavFuchs + mphrediction exemplar rows; K98 provenance
- **Updated:** @concepts/generative-engine-optimization.md — LLM referral traffic subsection `[TENTATIVE]`
- **Updated:** @concepts/x-article-3-notes.md — optional K98 Article beats
- **OSINT brief folded:** `2026-06-04_k98-seo-geo-llm-traffic-from-osint.md`

## [2026-06-04] ingest | briefs/ — Reddit filter + X Article #4 (local)

- **Reddit sitewide filter:** `briefs/2026-06-03_reddit-filter-safe-posts.md` → @entities/platforms/reddit.md (recovery playbook)
- **X Article #4:** `briefs/2026-06-04_world-cup-bot-x-article-runbook.md` already on @concepts/world-cup-bot-x-article-runbook-notes.md
- **Hands-on only (no wiki page):** `2026-06-03_fifa-quote-reddit-distribution.md`, `2026-06-04_world-cup-bot-x-article-hero-prompts.md`
- **Easy Review:** 0 new briefs since 2026-05-08 (below ≥3 threshold)

## [2026-06-03] style-pass | Posts.docx K97 | 6 long-forms | authors: horizon_trade_x, 0x_rody, RohOnChain, Gustafssonkotte, Zephyr_hg (+ CCC batch routed OSINT)

## [2026-06-03] ingest | briefs/ — K88 + K90 cross-wiki completion (wiki-ingested)

Finalized pending OSINT briefs with missing cross-route stubs and K90 concept pages.

- **K88 brief** — `2026-05-31_k88-seo-geo-claude-skills-from-osint.md` → `status: wiki-ingested`
- **New:** `sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` — cross-wiki stub (SEO slice)
- **Updated:** `entities/tools/seo-geo-claude-skills.md` — local K88 source backlink

- **K90 brief** — `2026-05-31_k90-seo-from-osint.md` → `status: wiki-ingested`
- **New:** `sources/trading-posts-compilation-16-2026-05-31.md` — Posts cross-route stub
- **New:** `concepts/high-ticket-sales-psychology.md` — @vizionaryfocuss Post 3
- **New:** `concepts/cold-email-outbound-agency.md` — @MichLieben Post 9
- **Updated:** `concepts/high-ticket-smb-lead-generation.md`, `concepts/x-account-voice-and-format.md`, `sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md`

## [2026-06-02] ingest | digest inbox — 2 arXiv (BESPOKE + Ptah); triage misroute

**Digest status:** AM LaunchAgent ran but wrote to wrong `projects/SEO` (template config) — 3 OOD PDFs archived to `raw-sources/digest-misroute-2026-06-02/`. Reinstalled wrapper → correct repo; manual run fetched 2 on-topic PDFs (deduped prior GEO papers).

- **New:** @sources/bespoke-2025-search-augmented-personalization-benchmark.md — personalized search-augmented LLMs [TENTATIVE for local]
- **New:** @sources/ptah-2026-verifiable-multimodal-deep-research.md — verifiable deep research / citation fidelity
- **Updated:** @concepts/generative-engine-optimization.md, @meta/daily-research-digest-cadence.md
- **New sweep:** `wiki/sweeps/2026-06-02-daily.md`
- **Skipped (OOD):** Eliot literature explorer, AI originality study, cross-domain ML generalization (misroute batch)
- **Lint:** 0 orphans, 0 bidirectional gaps, 0 dangling links

## [2026-06-02] query | YouTube @Cemini23 launch analytics → lessons filed

- **Source** — `sources/youtube-cemini23-launch-analytics-2026-06-02.md` (Studio export May 5 – Jun 1; live May 30)
- **Updated** — `entities/platforms/youtube.md` → **validated** + launch playbook (Short vs long, 16:9, titles, TTS sync)
- **Updated** — `sources/youtube-shorts-creator-growth-2026.md` — operator [CONFIRMED] backlink
- **Meta** — `LESSONS.md` entry; raw CSV in `briefs/youtube-cemini23/analytics-2026-06-02/` (gitignored)

style-pass | Posts.docx K93 | 31 posts (OSINT ingest) | garrytan harness thread + mixed PM/agent; low direct SEO voice density — skim only unless operator flags a post

style-pass | Posts.docx K92 | 12 posts | authors: @get_truenorth, @rohit4verse, @humzaakhalid, @peterom, @Voxyz_ai (+ sparse exports)

---

## [2026-06-01] ingest | digest inbox — 3 arXiv GEO/AEO papers

First federated-daily-digest inbox full ingest (`wiki/sweeps/2026-06-01-daily.md`).

- **New sources (3):** @sources/vishwakarma-2026-competitive-geo-sigir.md (deep-read), @sources/davidson-2026-factual-gv-gap.md (read), @sources/dong-2025-safesearch-red-teaming.md (skimmed, record-only)
- **New concept:** @concepts/competitive-geo-citation-factors.md — operator gatekeeper/differentiator digest from SIGIR '26
- **Updated:** @concepts/generative-engine-optimization.md — competitive citation + GV-gap sections
- **Updated:** @concepts/content-strategy-local.md, @concepts/website-essentials-local-business.md — explicit pricing / recency for competitive GEO
- **Updated:** @sources/aggarwal-2024-geo-paper.md — backlink to SIGIR follow-up
- **Cross-wiki:** @cybersecurity-wiki/sources/dong-2025-safesearch-red-teaming.md stub (SafeSearch primary domain)
- **Moved:** 3 PDFs → `raw-sources/`
- **Lint:** 0 orphans, 0 bidirectional gaps, 0 dangling links

## [2026-06-01] ingest | briefs/ — K93 federated digest + goaccess (1 new)

- **New:** `sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md` — K93 v5 cross-route stub (SEO slice: goaccess MIT re-verified)
- **New:** `concepts/federated-daily-research-digest.md` — per-wiki Exa + inbox loop (GBP/GEO/AEO query lanes)
- **New:** `meta/daily-research-digest-cadence.md` — operator cadence + LaunchAgent label `com.cemini.daily-research-digest.seo`
- **New (structural):** `scripts/daily_research_config.yaml`, `scripts/daily_research_digest_run.py`, `scripts/daily_research_fetch.py`, `wiki/sweeps/`
- **Updated:** `entities/tools/goaccess.md` — K93 Adopt reaffirmed + snippet
- **Updated:** `concepts/generative-engine-optimization.md`, `concepts/google-business-profile.md`, `concepts/obsidian-integration.md` — digest backlinks
- **Updated:** `sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` — K93 cross-link
- **Brief processed:** `briefs/2026-06-01_k93-seo-digest-goaccess-from-osint.md` (`processed: 2026-06-01`; LaunchAgent install still operator hands-on)
- **Skipped:** Easy Review (still 1 brief; below ≥3 threshold); Posts K93 style pass (low SEO voice density)
- **Lint:** 0 orphans, 0 bidirectional gaps, 0 dangling links

## [2026-06-01] check | easy-review-briefs + briefs inventory (no new Easy Review)

Cadence check: `git pull` clean; tracked `briefs/*.md` on `origin/main` unchanged (still 6 files; Easy Review = `2026-05-08_manual_17.md` only). Local gitignored briefs: 6 lack `processed:` markers but were already folded into wiki pages on prior passes (Issue 3, agent-toolkit, GSC checklist, reddit hands-on).

- **Easy Review:** 0 new briefs since `2026-05-08` dry-run cutoff; still below ≥3 threshold for pattern extraction
- **Updated:** @concepts/review-response-templates.md — Production patterns "current state" reflects validated loop + corpus size (was stale "awaiting first ingest")
- **Lint:** 0 orphans, 0 bidirectional gaps, 0 dangling links (5 cited-unread stubs unchanged)

## [2026-06-04] brief | World Cup Bot X Article #4 runbook + docs/RUNBOOK.md

- **New (local):** `briefs/2026-06-04_world-cup-bot-x-article-runbook.md` — full paste-ready X Article body + distribution tweets
- **New:** `concepts/world-cup-bot-x-article-runbook-notes.md`
- **External:** world-cup-bot `docs/RUNBOOK.md` + Pages/README links (94b1a40)

## [2026-06-03] launch | Outlier Weekly Issue 3 + X thread — live

- **Substack:** https://outlierweekly.substack.com/p/i-open-sourced-the-world-cup-lp-bot (free)
- **Updated:** `concepts/outlier-weekly-issue3-world-cup-bot-notes.md`, `concepts/world-cup-bot-search-discovery.md`
- **Briefs (local):** drafts, reddit profile, indexing checklist, YouTube teaser pack
- **External:** world-cup-bot README + Pages → Issue 3 permalink

## [2026-06-03] correction | world-cup-bot test count

- **209** tests collected on `main` (`pytest --collect-only`); marketing copy → **200+** (was 178/170+)

## [2026-06-03] launch-prep | Outlier Weekly Issue 3 — final pass vs live repo

- **Briefs (local):** `2026-06-03_outlier-weekly-issue3-drafts.md` — launch-day table; conviction v5; 200+ tests (209 collected); `--liquidity-gate`; Module 6 paper arb boundary
- **Updated:** `concepts/outlier-weekly-issue3-world-cup-bot-notes.md` — K84 guardrails + test count
- **Verified:** CI green; Pages + Gambling-wiki links live; hero PNGs on disk; X posts ≤280 chars

## [2026-05-31] update | Issue 3 marketing — Gambling-wiki cross-promo

- **Updated:** `concepts/outlier-weekly-issue3-world-cup-bot-notes.md` — gambling wiki anchor table + asset status
- **Updated:** `concepts/world-cup-bot-search-discovery.md` — launch backlink signals include Gambling-wiki
- **Briefs (local):** `2026-06-03_outlier-weekly-issue3-drafts.md`, `2026-05-30_outlier-weekly-issue3-world-cup-bot-launch.md`, `2026-05-31_reddit-profile-first-post.md`, `2026-05-30_world-cup-bot-search-indexing-checklist.md`, `youtube-cemini23/WORLD-CUP-BOT-TEASER-PACK.md`, `youtube-cemini23/world-cup-bot-teaser-brief.md`
- **External:** world-cup-bot `docs/index.html` + README Related → https://github.com/cemini23/Gambling-wiki

## [2026-05-31] ingest | briefs/ — K90 tools + Posts style pass

- **New:** `sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` — cross-wiki stub (SEO slice: claude-ads, goaccess)
- **New:** `entities/tools/goaccess.md` — MIT log analyzer; Adopt-eligible (K90)
- **Updated:** `entities/tools/claude-ads.md` — K90 Adopt tier noted; K71 security defer upheld (#30/#34/#40 open)
- **Updated:** `concepts/x-account-voice-and-format.md` — K90 exemplars (@Voxyz_ai, @vizionaryfocuss)
- **Updated:** `entities/tools/google-analytics-4.md` — goaccess backlink
- **Brief processed:** `2026-05-31_k90-seo-from-osint.md` (`processed: true`)
- **Skipped:** Easy Review (still 1 brief; below ≥3 threshold); `2026-05-31_reddit-profile-first-post.md` (hands-on only)

## [2026-05-31] style-pass | Posts.docx K90 | @Voxyz_ai + @vizionaryfocuss exemplars

- OSINT source: `@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md`
- Updated `@concepts/x-account-voice-and-format.md` exemplar table
- Brief: `briefs/2026-05-31_k90-seo-from-osint.md` — folded into ingest entry above

## [2026-05-31] ingest | briefs/ — K88 tool + YouTube channel + Issue 3 assets (3 briefs)

- **New:** `entities/tools/seo-geo-claude-skills.md` — Steal-from (Apache-2.0 confirmed K88; audit parallel-reject unchanged)
- **New:** `entities/platforms/youtube.md` — @Cemini23 operator channel (Shorts + long-form + NotebookLM)
- **Updated:** `outlier-weekly-issue3-world-cup-bot-notes.md` (hero-prompts brief, GSC boundary, YouTube trailer row)
- **Updated:** `claude-seo-agrici.md`, `geo-seo-claude.md`, `x-account-voice-and-format.md`, `agent-toolkit-x-thread-2026-05-28.md` (backlinks)
- **Synced:** `briefs/2026-05-30_world-cup-bot-search-indexing-checklist.md` → Pages-only GSC steps
- **Briefs processed:** `2026-05-31_k88-seo-geo-claude-skills-from-osint.md` (`processed: true`); `2026-06-03_outlier-weekly-issue3-hero-prompts.md` + `youtube-cemini23/` launch assets folded into concept/platform pages (hands-on copy stays in `briefs/`)
- **Skipped:** Easy Review (still 1 brief; below ≥3 threshold)
- **Lint:** 0 orphans / 0 bidirectional gaps / 0 dangling

---

## [2026-05-30] seo | World Cup Bot — Google/Bing discovery (GitHub Pages)

- **Repo:** [cemini23/world-cup-bot PR #1](https://github.com/cemini23/world-cup-bot/pull/1) merged — `docs/index.html`, sitemap, robots.txt
- **Live:** https://cemini23.github.io/world-cup-bot/ (Pages enabled; GSC/Bing verify target)
- **Repo metadata:** topics (`world-cup-bot`, `polymarket`, `kalshi`, …), homepage → Pages URL
- **Wiki:** `concepts/world-cup-bot-search-discovery.md`, `briefs/2026-05-30_world-cup-bot-search-indexing-checklist.md`
- **Drafts:** Issue 3 + X Reply 1 link landing page
- **Operator TODO:** verify Pages URL in Google Search Console + Bing Webmaster Tools (hands-on checklist in brief)

---

- **Draft:** `briefs/2026-06-03_outlier-weekly-issue3-drafts.md` → status **ship-ready** (Substack ~1,970 words, X 6+2 thread)
- **Hero:** `briefs/ow-issue3-world-cup-bot-substack-hero.png`, `briefs/ow-issue3-world-cup-bot-x-card.png` verified
- **No-static-mids:** runtime Gamma+CLOB mids vs vendored CC0 kickoffs split explicit in Module 5, architecture flow, Proof (matches README + DATA_ATTRIBUTION)
- **Updated:** `concepts/outlier-weekly-issue3-world-cup-bot-notes.md` (asset table, ship-ready)
- **Ship:** 2026-06-03 Substack free + X thread

---

## [2026-05-30] style-pass | Posts.docx K84 | 5 long-forms | authors: @0xPhilanthrop, @polybacktest, @Gustafssonkotte, @ziwenxu_, @cyrilXBT

OSINT source: `@osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md`. Updated `@concepts/x-account-voice-and-format.md` exemplar table + snippets + Dead Ends. **Article beat:** polybacktest 1.5% gross-EV spread gate → optional OW3 footnote, not standalone Article. **CCC route:** @ziwenxu_ Codex /side /fork /goal → ccc brief staged. **Formatting:** Cyril K84 vault-stack post needs paragraph merge before X paste.

---

## [2026-05-30] brief | Outlier Weekly Issue 3 — World Cup Bot launch pack

- **Brief:** `briefs/2026-05-30_outlier-weekly-issue3-world-cup-bot-launch.md` — Substack outline, X thread beats, IP boundary, distribution calendar (ship **2026-06-03**)
- **Concept:** `concepts/outlier-weekly-issue3-world-cup-bot-notes.md` — marketing queue stub
- **Updated:** `x-account-voice-and-format.md` (OW3 arc row + backlink), `index.md`
- **Librarian copy:** `cemini-librarian:/opt/cemini-wiki/briefs/2026-05-30_outlier-weekly-issue3-world-cup-bot-launch.md`
- **Cross-wiki source:** OSINT `entities/tools/world-cup-bot.md`

---

## [2026-05-28] query + file | X voice, Article #3 notes, Posts.docx style ritual

- **New:** `concepts/x-account-voice-and-format.md` — Cyril (@cyrilXBT K78) style deconstruction, operator voice rules, X Article paragraph-merge protocol (Article #2 spacing fix), living exemplar table
- **New:** `concepts/x-article-3-notes.md` — git wiki CI + contribution rate; Cyril structure map; title options; image prompt
- **New:** `prompts/posts-docx-style-pass.md` — agent ritual after each Posts.docx ingest
- **Updated:** `agent-toolkit-x-thread-2026-05-28.md`, `obsidian-integration.md` (backlinks)
- **Operator ask:** ongoing attention to daily docx X posts for style/format; Article #2 already live
- **Cross-wiki:** OSINT `CLAUDE.md` ingest step **4c** added — `Posts.docx` style pass handoff to this wiki

---

- 1 brief: `briefs/2026-05-28_k73-seo-obsidian-workflows-from-osint.md`
- New source stub: `sources/trading-posts-compilation-38-2026-05-28.md` (provenance; canonical on OSINT)
- Updated: `obsidian-integration.md`, `claude-platforms.md`, `generative-engine-optimization.md` (workflow references only; no new ranking mechanism validated)
- Easy Review: unchanged

---

## [2026-05-27] ingest | briefs/ — K72 Obsidian + Claude workflows (1 new)

- 1 brief: `briefs/2026-05-27_k72-seo-obsidian-workflows-from-osint.md`
- New source stub: `sources/trading-posts-compilation-25-2026-05-27.md` (provenance; canonical on OSINT)
- Updated: `obsidian-integration.md` (Claude Code + vault memory/moat), `generative-engine-optimization.md` (vault as coherence source of truth), `claude-platforms.md` (wiki-as-context)
- Easy Review: unchanged

---

## [2026-05-27] ingest | briefs/ — K71 SEO tooling (1 new)

- 1 brief: `briefs/2026-05-27_k71-seo-tooling-from-osint.md`
- New pages: `entities/tools/notfair-toprank.md` (Adopt-eligible), `entities/tools/claude-ads.md` (Defer — SSRF/path-traversal issues open)
- Backlinks: claude-seo-agrici, geo-seo-claude, claude-platforms, meta-ads-local, index
- Easy Review: unchanged (still 1 brief; barbershop/5star_specific below ≥3 pattern threshold)

---

## [2026-05-27] ingest | briefs/ — K69 cross-wiki routes (2 new)

- 2 briefs from OSINT K69 ingest (routed via `cross_wiki_route` pattern, not SEO inbox):
  - `briefs/2026-05-27_k69-local-business-website-gap-kimi-from-osint.md`
  - `briefs/2026-05-27_k69-obsidian-offline-geo-coherence-from-osint.md`
- New source stub: `sources/trading-posts-compilation-20-2026-05-27.md` (provenance only; canonical on OSINT)
- Updated: `website-essentials-local-business.md` (Maps-gap outreach), `obsidian-integration.md` (offline plugin stack), `generative-engine-optimization.md` (coherence frame), `google-business-profile.md` (GBP without website)
- Easy Review: unchanged

---

## [2026-05-26] ingest | briefs/ — K68 SEO tooling (1 new)

- 1 brief: `briefs/2026-05-26_k68-seo-tooling-from-osint.md`
- New pages: `entities/tools/taste-skill.md` (Adopt-eligible), `entities/tools/social-media-skills.md` (Adopt-eligible), `entities/tools/money-printer-turbo.md` (Defer)
- Backlinks: garden-skills, awesome-design-md, marketingskills, social-media-for-barbershops, creator-external-promotion, ugc-monetization-loop, website-essentials, creator-content-strategy, index
- Easy Review: unchanged

---

## [2026-05-24] ingest | briefs/ — K63 weather-icons (1 new)

- 1 brief: `briefs/2026-05-24_k63-weather-icons-ui-from-osint.md`
- New page: `entities/tools/weather-icons.md` — erikflowers/weather-icons; steal-from posture (no LICENSE on GitHub)
- Backlinks: website-essentials-local-business, itshover, index
- Easy Review: unchanged (1 brief total; pattern ingest not triggered)

---

## [2026-05-22] ingest | briefs/ — 2 new cross-wiki briefs processed

Inventory after May 21 triage: 21 briefs on disk; 2 lacked `processed:` markers (`2026-05-21_k55-2-ridark-eth-seo-relevant-repos.md`, `2026-05-22_k57-bowtied-bull-leadgen-from-osint.md`). Easy Review brief count unchanged (still 1 ingested; below ≥3 pattern threshold).

**Promoted (4 wiki pages):**
- `sources/bowtied-bull-solopreneur-leadgen-macro-2026-05-22.md` — K57 source stub (skimmed via brief)
- `concepts/high-ticket-smb-lead-generation.md` — offer stack + SEO/GEO hooks + barbershop light-touch note
- `entities/tools/saas-boilerplate.md` — ixartz/SaaS-Boilerplate stub, CONDITIONAL-GO pending Phase-0
- `concepts/free-smb-ops-stack.md` — akaunting + Faveo + Laracom bundle; PBN/crawler items deferred

**Backlinks:** reviews-reputation-management, generative-engine-optimization, meta-ads-local, claude-ecommerce-workflows (4 pages touched + index + log).

**Briefs marked** `processed: 2026-05-22` (2). No Easy Review ingest.

---

## [2026-05-17] maintenance | freshness sweep round 2 — bulk refactor

**Continuation of round 1.** Round 1 left 61 stale `[NEEDS VERIFICATION 2026-05-07/08]` tags after verifying 4 high-stakes tactical claims. Most remaining tags fell into three buckets that don't benefit from a date-based "needs verification" signal:

1. **Page-header preambles** (~6 pages) — boilerplate "this page is upgraded with current best-practice synthesis" notes that aren't claims at all. Refactored to drop the meta-tag wrapper; kept the descriptive text.
2. **Operator-conditional claims** (~12 tags) — things that depend on operator's specific market, shops, or counsel (e.g., "two-shop branding approach", "minor-consent rules by state", "consent-mode requirement for US-only operators"). Reframed as operator-conditional with explicit "confirm with own counsel" or "depends on market" language.
3. **Proprietary-algorithm claims** (~12 tags) — engine internals that vendors don't publish (Yelp filter weights, Facebook recommendation algorithm, Apple Intelligence citation behavior, Bing/Copilot citation patterns, OnlyFans recommended-creators surface). Converted to `[TENTATIVE]` with practical-implication framing.

Pages touched (12, all bumped `updated: 2026-05-17`):
- `concepts/local-seo-foundations.md` — NAP claim `[CONFIRMED]` (kaidm + linkdatabase) + preamble refactor
- `concepts/google-business-profile.md` — post cadence 1-2/week `[CONFIRMED]` (reviewly.ai + yadavbikash) + preamble refactor
- `concepts/creator-marketing-foundations.md` — timeline benchmarks → `[TENTATIVE]` + preamble refactor
- `concepts/review-response-templates.md` — GBP AI-summary weighting → `[TENTATIVE]` + operational marker
- `entities/platforms/bing-places.md` — Copilot citation → `[TENTATIVE]`
- `entities/platforms/apple-business-connect.md` — Apple Intelligence citation → `[TENTATIVE]`
- `entities/platforms/facebook.md` — recommendation algorithm → `[TENTATIVE]`
- `entities/platforms/yelp.md` — filter weights → `[TENTATIVE]`
- `entities/platforms/onlyfans.md` — 3 tags (recommended creators, enforcement, ID verification times) → `[TENTATIVE]`
- `entities/platforms/instagram.md` — minor-jurisdiction → operator-counsel direction
- `entities/companies/friend-1.md` — operational marker
- `entities/tools/google-analytics-4.md` — jurisdiction-dependent refactor

Lint re-run: all 8 checks clean. Stale-tag count: **62 → 29**. Remaining 29 are higher-value claims that would benefit from real verification (vendor pricing for Yext/Semrush/Ahrefs/BrightLocal/Local Falcon, visit-frequency 2-6wk, schema spec drift, near-me 70-90% share, Helpful Content wording, GBP barbershop category list, OnlyFans Radvinsky ownership). Defer to round 3 if/when operator engages.

---

## [2026-05-17] maintenance | lint script bug fix + freshness sweep (round 1 of N)

**Two-part session.**

**Part 1 — lint script bug fix.** Section 8 of `wiki_lint.py` reported 13 dangling `@osint-wiki/...` and `@ccc-wiki/...` cross-wiki links. Root cause: not wiki content — script bugs. Two fixes:
- `parse_frontmatter` was returning `related:` list items with the surrounding YAML `"..."` quotes attached, so `"@osint-wiki/foo.md"` became the lookup key. Patched to strip paired surrounding `"` or `'`.
- `CROSS_WIKI_RE = r"@([a-z0-9_-]+)/([^\s\`)]+)"` did not exclude `"`, so body `@path` matches could capture a trailing quote from inline-code or YAML contexts. Added `"` to the exclusion char class.

Re-run: 0 dangling cross-wiki links across all 56 references. Wiki-content side untouched.

**Part 2 — freshness sweep round 1.** 65 dated `[NEEDS VERIFICATION YYYY-MM-DD]` tags (48 from 2026-05-07, 17 from 2026-05-08) all ≥7 days old. Verified the 4 highest-stakes tactical claims via Brave (3 searches):

- **`concepts/reviews-reputation-management.md`** — review-gating-forbidden tag `[CONFIRMED]`. Found April 2026 GBP policy update explicitly enumerating review gating, incentivized reviews, on-premises kiosk pressure, staff quotas, and content direction as Maps UGC Policy violations under Rating Manipulation. Sourced to support.google.com + launchcodex coverage.
- **`concepts/social-media-for-barbershops.md`** (hashtag count) — old "5-10 hashtags per post" advice **`[RETRACTED]`**. Instagram **capped posts/Reels at 5 hashtags platform-wide in December 2025** (Later guide). New canonical claim: **3-5 hashtags**, treated as classification signals, not discovery/reach drivers. **Material change for the operator** — if he was following pre-2026 hashtag-stuffing advice, that's now a platform-enforced cap.
- **`concepts/social-media-for-barbershops.md`** (Reels reach gap) — `[CONFIRMED]`. Reels still dominate organic reach in 2026; engagement-rate gap narrower (~0.52% vs ~0.37%) but reach-gap large because algorithm pushes Reels to non-followers via Explore/Reels-tab/feed recommendations.
- **`concepts/generative-engine-optimization.md`** (AI-content E-E-A-T) — `[CONFIRMED]`. Google does not penalize AI content per se; penalizes low-quality/scaled-abuse content regardless of origin. Ahrefs study of ~600K pages found 86.5% of top-ranking content uses some AI assistance, near-zero correlation (0.011) with penalties. Practical implication: AI-drafted copy is fine *if* it demonstrates E-E-A-T (real photos, real reviews, real local context).

Remaining: 61 dated tags untouched. Most are either operator-conditional (can't be verified from external research — depend on operator's market/shops/data) or by-nature-uncertain (engine re-indexing frequency, GBP API partnerships, etc.). Next round of sweep could batch-refactor these to `[TENTATIVE]` or remove the date entirely rather than continue claiming "needs verification".

Pages touched: 3 concept pages + log.md + scripts/wiki_lint.py. Lint re-run: all 8 checks clean (now 61 stale tags remaining, down from 62).

---

## [2026-05-10] maintenance | wiki health pass + DOCX ingest

Routine health check triggered by "is everything working?" Found and fixed multiple issues across the wiki + ingested one pending source.

**Quick cleanup:**
- Deleted 2 empty Obsidian canvas files (`wiki/Untitled.canvas`, `wiki/Untitled 1.canvas`)
- Resolved duplicate page conflict: merged `concepts/ai-assitance-guardrails.md` (typo, 69 lines, better frontmatter) into the canonical `concepts/ai-assistance-guardrails.md` (correct spelling, 147 lines, richer body). Fixed 7 wiki files that referenced the typo'd path. Tag `ai-assitance` corrected to `ai-assistance`.
- Added 2 missing bidirectional backlinks: `concepts/claude-platforms.md` ↔ `entities/tools/claude-code-tool-stack.md`, `concepts/ai-assistance-guardrails.md` ↔ `entities/tools/claude-code-tool-stack.md`

**Frontmatter schema compliance:**
- Added `type:` field to 51 pages that were missing it (26 concept pages → `type: concept`, 5 source pages → `type: source`, 20 entity pages → `type: entity`). Lint now reports 0 missing `type` fields.
- Added missing `maturity: draft` to `sources/ai-detection-platforms-2026.md` and `sources/onlyfans-tos-violations-case-studies.md`. Also de-duplicated their related: lists (artifact from the typo'd-path replacement).
- Removed duplicate `concepts/ai-assistance-guardrails.md` entry in `creator-marketing-foundations.md`.

**Lint script patches (`scripts/wiki_lint.py`):**
- Section 4 (@path body mentions) now recognizes `briefs/*.md` paths that exist at repo root (briefs live outside `wiki/` by convention but are referenced from inside). Fixes 4 false-positive "missing page" warnings for briefs that exist.
- Section 4 now strips inline-code backticks and fenced code blocks before matching `@path` mentions. Illustrative `@example-page.md` references inside documentation no longer flagged.

**Ingest — AI Creator GTM Strategy Blueprint.docx:**
- Source file (3 MB DOCX, 120 paragraphs, 60+ citations) was in `research to be indexed/` from a prior session. Confirmed it is the authoritative source for the previously-content-rich `sources/fanvue-gtm-blueprint-2026.md` stub (which had 12 inbound citations but no `read_status` set, flagging it as cited-unread).
- Updated `sources/fanvue-gtm-blueprint-2026.md`: set `read_status: deep-read`, refreshed Raw Concept provenance to reference both the DOCX file and the earlier `blha6pkkl.txt` cache, added 7 verbatim quotes to a new `## Snippets` section (covering generalist-vs-niche economics, AI slop / aesthetic fatigue, geographic anchoring, PPV whale economics, chatbot reset failure mode, AI ad creative CTR/AOV tradeoff, organic reach decline).
- Cleared duplicate `fanvue-gtm-blueprint-2026` entry in `wiki/index.md` (Sources section).
- Moved DOCX from `research to be indexed/` to `raw-sources/`. Inbox now empty.

**Cited-unread stub sweep (second pass):**
- Audited the 9 remaining cited-unread stubs. Each had 89–145 lines of body content with 4–7 verbatim quote snippets already in place — these were all already-read sources from previous research passes that simply lacked an explicit `read_status` frontmatter field. Added `read_status: read` to all 9: `instagram-reels-creator-marketing-2026`, `creator-email-marketing-2026`, `paid-advertising-creators-2026`, `tiktok-marketing-2026`, `ai-detection-enforcement-2026`, `youtube-shorts-creator-growth-2026`, `onlyfans-funnel-optimization-2026`, `onlyfans-tos-violations-case-studies`, `ai-detection-platforms-2026`.

**Final lint state:** 87 pages indexed, 1 orphan (intentional off-topic `slcg-paper-off-topic.md`), 0 bidirectional gaps, 0 dangling related: links, 0 dangling @path mentions, 0 cited-unread stubs, 0 missing type/maturity fields, 0 stale NEEDS VERIFICATION tags, all 7 cross-wiki references resolve. Lint is fully clean across all 8 checks for the first time.

---

## [2026-05-09] brief | Creator Launch Decision Hub — 24-hour sprint resource

Compiled all critical decision-support resources from both the SEO:GEO wiki and the Image Gen wiki into a single launch-day reference document. Covers: platform choice (OnlyFans vs Fanvue vs Passes vs Patreon with compliance comparison), pricing strategy (subscription tiers + PPV ladder), content mix (wall + external platforms), AI assistance guardrails (what Claude can/can't safely do), conversion/retention benchmarks, 90-day revenue projections, realistic cost breakdown, and a day-by-day action checklist. Cross-wiki bridge document linking @wiki-alias/image-gen-wiki sources where needed.

- Created `briefs/2026-05-09_creator-launch-decision-hub.md` — 7-section decision hub (platform, pricing, content, AI guardrails, retention, revenue, action plan)
- Updated `wiki/index.md` — added brief to index

## [2026-05-09] brief | Creator Marketing 24-Hour Sprint

Time-boxed punch list for creator marketing operations. Covers OF account audit, content calendar, link-in-bio & email capture setup, platform optimization (X, IG, TikTok, Reddit), DM retention templates, PPV strategy, viral content prep, analytics review, and competitor spot-check. Linked from @concepts/creator-marketing-foundations.md.

- Created `briefs/2026-05-09_creator-24hr-sprint.md` — 24-hour sprint punch list (24 blocks × 1 hour)
- Updated `wiki/concepts/creator-marketing-foundations.md` — added backlink to sprint brief in frontmatter + Relations section

## [2026-05-08] ingest | Fanvue GTM Blueprint — synthetic creator monetization strategy

Created comprehensive source page and synthesized 4-pillar GTM strategy for launching a synthetic AI creator on Fanvue.

- Created `wiki/sources/fanvue-gtm-blueprint-2026.md` — source page (171 paragraphs, 2026 market data)
- Created `wiki/concepts/synthetic-creator-gtm.md` — four-pillar GTM hub: niche selection, aesthetic positioning, GEO traffic, conversion/retention
- Created `wiki/concepts/creator-aesthetic-positioning.md` — "Imperfect by Design" visual trust doctrine
- Created `briefs/2026-05-08_fanvue-synthetic-creator-gtm.md` — actionable 90-day launch playbook
- Enriched `wiki/entities/platforms/fanvue.md` with GTM strategy section + backlink to source
- Enriched `wiki/concepts/generative-engine-optimization.md` with AI persona GEO references + backlink
- Enriched `wiki/concepts/creator-marketing-foundations.md` with backlink to new source
- Updated `wiki/index.md` with 2 new sources + 2 new concept entries

## [2026-05-08] ingest | Twitter/X + Reddit creator promotion research

Created source pages from 2026 web research (OpenTweet, Tweet Archivist, Shopify, Monetag, SocialBee, Sprout Social, Outfy, Sotrender, Pseudoface, Unfiltered Management, Substy, Reddit r/onlyfansadvice, KarmaGuy, Conbersa, IPFoxy, Indie Hackers, Link Assistant, AuditSocials, TechCrunch).

- Created `wiki/sources/twitter-x-creator-guide-2026.md` (algorithm signals with Grok-powered transformer model, NSFW three-tier policy, monetization thresholds, traffic conversion benchmarks, engagement velocity research)
- Created `wiki/sources/reddit-creator-promotion-2026.md` (10:1 rule verification, account warm-up schedule, karma building strategies, subreddit promotion tactics, ban avoidance)
- Enriched `wiki/entities/platforms/twitter-x.md` with 2026 verified data: algorithm weights (reply=150x like), three-stage tweet lifecycle, SimClusters (145,000 topic clusters), external link penalty data, NSFW three-tier classification, monetization programs with thresholds
- Enriched `wiki/entities/platforms/reddit.md` with 2026 verified data: account warm-up schedule (14-day plan), karma building strategies (Rising strategy, CQS), Contributor Quality Score, 67% creator adoption rate, 90/10 community participation ratio

All `[NEEDS VERIFICATION 2026-05-08]` tags replaced with `[CONFIRMED]` and sourced to specific web references.

---

## [2026-05-08] ingest | OnlyFans platform docs + creator economy research

Created comprehensive documentation on OnlyFans platform mechanics using 2026 web research (Brave Search). Populated from onlyfans.com/terms, B9 Agency, ofstats.net, gitnux.org, influencers.feedspot.com, thewebaddicted.com, sirency.com, list25.com.

- Created `sources/onlyfans-official-docs.md` (official docs summary) — frontmatter type:source, read_status:read. Covers: verification process, 80/20 split, payout methods (Visa/Mastercard/Discover/Maestro + 3D Secure), PPV pricing ($5-200), subscription caps ($49.99), 2026 policy updates (AI disclosure, deepfake ban, enhanced verification, DSA/Online Safety Bill compliance), analytics metrics, platform scale (4.63M creators, 377.5M users, $7.22B revenue 2024).
- Created `sources/creator-economy-2026-report.md` (2026 benchmarks) — 9 high-quality sources cited. Key findings: power-law distribution (top 1% earn $49K/year, top 0.1% earn 15x more), PPV dominance (59% of top earner revenue), 50% burnout rate, 42% earn $500-2K/month, high-ticket subscriptions ($15-25) outperform low-ticket by 40%, X (Twitter) dominates referrals.
- Enriched `entities/platforms/onlyfans.md` with 2026 verified data: updated monetization models table with revenue shares, subscription tier benchmarks ($7.21 avg, $9.99-19.99 sweet spot), PPV ladder strategy, DM response time impact (30% higher retention for <1hr), content policy enforcement (2026 AI/deepfake bans), payout net calculations (75-78% after fees), traffic source hierarchy. Added CONFIRMED tags and NEEDS VERIFICATION 2026-05-08 tags per CLAUDE.md schema. Updated related: frontmatter and Relations body with new source pages.
- Updated `wiki/index.md` Sources section: added "Creator platforms research" subsection with ai-detection-platforms-2026, onlyfans-tos-violations-case-studies (pre-existing), and the two new source pages.

Pages touched: 2 created + 1 enriched + 2 index/log updated = 5 pages.

---

## [2026-05-08] enrich | tier-2 stubs (yelp + GSC + GA4 + local-falcon) → workflow-grade pages

Promoted four Tier-2 entity stubs from ~33-37 lines of skeletal content to ~110-180 lines each of workflow-grade reference material. Sourced from Yelp Trust & Safety + Yelp Content Guidelines + Sterling Sky 2025 enforcement walkthrough + GSC verification guides (Bluehost, Incremys, WordPress.com, Stan Ventures) + GA4 / GTM tutorials (Nimbata, Conversios, Digitnetix) + Local Falcon first-party pricing + comparative-tool reviews.

- @entities/platforms/yelp.md — added: Recommendation Software (the official term for the filter) and its 2024 LLM-enhanced detection; full Don't-Ask-For-Reviews policy quote with operator-side examples; 2025 enforcement shift from hidden search penalty to public Consumer Alerts; Apple Maps + Siri data-partnership context (why Yelp matters even to operators who don't compete on it); cross-platform interaction with Easy Review (no public response API → manual workflow only).
- @entities/tools/google-search-console.md — added: Domain vs URL-prefix property comparison + DNS-TXT recommendation for stability; the four reports operators actually use (Performance Queries, Indexing Pages, URL Inspection, Enhancements); GSC ↔ GA4 integration; common operator mistakes including verification-element drop-during-redesign.
- @entities/tools/google-analytics-4.md — added: 2024 conversion → "key event" rename; the four key events a B&M website should track (`click_to_call`, `get_directions`, `book_appointment`, `contact_form_submit`); GTM-as-only-sane-stack rationale; GBP-traffic-invisible-by-default attribution gotcha + UTM workaround; Consent Mode v2 (mandatory for EEA traffic since March 2024).
- @entities/tools/local-falcon.md — added: full credit-pricing table (3×3=9 → 21×21 grids); credit-expiry "breakage" trap on monthly plans + workarounds; Falcon AI + AI Visibility Tracking (2025) + GSC Query Groups integration; Phase-0 audit table per CLAUDE.md schema; comparison to free alternative @entities/tools/claude-seo-agrici.md.

- 4 pages updated; maturity stays `draft` (further upgrade to `validated` requires real-world operator testing in production)
- 0 new related: edges added (existing cross-link graph already covered the natural neighbors)
- 1 backlink added (yelp ↔ schema-markup-local — both already pointed at each other indirectly via reviews-reputation-management; making it bidirectional)
- Lint: 0 orphans (excluding the 1 expected slcg-paper-off-topic), 0 bidirectional gaps, 0 dangling links, 0 cited-unread stubs, 0 stale [NEEDS VERIFICATION] tags

---

## [2026-05-08] ingest | easy-review-briefs (1 new since cold-start; dry-run)

First easy-review-briefs ingest pass — establishes the cutoff baseline for future cadence (≥10 briefs OR monthly per `prompts/ingest-easy-review-briefs.md`). Triggered as a procedure-validation dry-run, not by threshold; below the ≥3-brief minimum for pattern extraction so `concepts/review-response-templates.md` is unchanged this pass.

- 1 brief read: `briefs/2026-05-08_manual_17.md` (5★ specific praise, barbershop, posted via paste-flow + Groq fallback after Gemini quota exhaustion)
- 0 new pattern observations added to @concepts/review-response-templates.md (single-brief group below ≥3 threshold)
- Anti-pattern alerts: 0 — reply respects all hard rules (3 sentences, no URLs/prices/promos, first-name-only, business name only in sign-off)
- Vertical coverage: barbershop=1
- Categories present: 5star_specific=1

**Procedure issues surfaced + fixed in Easy Review:**
- `prompts/ingest-easy-review-briefs.md` line 26 expected `operator_vertical` in brief frontmatter; serializer only encoded it inside `tags[]`. Fixed in Easy-Review commit `e9d0fb6`: explicit `operator_vertical:` field added to brief YAML frontmatter going forward. The 1 existing brief on disk pre-dates the fix; future cutoff-based ingests will skip it, so no backfill needed.
- Author whitespace produced double-space artifacts in the brief title line (`title: GBP reply —  Mike R.`). Same Easy-Review commit trims author before templating.
- Both fixes are TDD-covered (`tests/lib/wiki-brief.test.ts`, 5/5 green; full suite 36/36).

**Loop validated:** paste → Groq draft → operator approve → Octokit → wiki repo → manual `git pull` → ingest dry-run end-to-end. Next ingest happens when the brief count reaches ≥3 in any single category × vertical group OR monthly, whichever first.

---

## [2026-05-08] add | easy-review companion app entity page + README mention

Easy Review is being built in a parallel Claude Code session — a Next.js 15 + TypeScript + Tailwind + Supabase + Gemini Flash micro-app for review-reply drafting (3 tone options per review, Tinder-style approve/edit UI) + customer re-engagement (slipping-regulars CSV → personalized SMS drafts). Human-in-the-loop on every send; no auto-posting, no review gating, no bulk SMS blasts.

The wiki and Easy Review are deliberately separate: wiki = thinking tool (markdown, no build, broad scope); Easy Review = software (backend, auth, deploy cycle, narrow scope). Documenting Easy Review here so wiki recommendations can reference the tool by name where relevant (review-acquisition / review-response / first-90-days Week 3 / GBP integration).

- New page: `wiki/entities/tools/easy-review.md`, maturity: draft, ~600 words. Covers tech stack, two features, where it fits in the wiki's recommendations, boundary discipline, current state (mock data, no prod deploy, GBP API integration pending OAuth), why-separate-from-wiki, Phase-0 N/A (in-house companion, not third-party adoption).
- README.md gained a "Companion app: Easy Review" section between the "What the wiki does NOT do for you" guardrail section and "Contributing / forking", framing Easy Review as the operator-approved automation surface that respects the same policy boundaries the wiki enforces.
- 5 pages received bidirectional backlinks: `concepts/reviews-reputation-management.md` + `concepts/review-response-templates.md` + `concepts/first-90-days-playbook.md` + `concepts/session-1-facilitator-notes.md` + `entities/platforms/google-business-profile.md`.
- index.md Tools subsection now lists easy-review alphabetically between claude-seo-agrici and geo-seo-claude.
- Updated dates bumped to 2026-05-08 on all 5 backlinked pages.

---

## [2026-05-08] add | session-1-facilitator-notes (pre-meeting script for the operator-facilitator)

Single-purpose page distinct from the playbook: scripts the **facilitator's** behavior during the first in-person intake meeting (90 min). Pre-meeting prep, session opener, ordered .env-walkthrough sequence, live `/seo maps` diagnostic, baseline-screenshot capture, wrap with Week-1 prioritization, and post-meeting between-session work. Includes a "common landmines" section (managed-by-another-user GBP, missing website credentials, personal-vs-business IG account, etc.) and a "what NOT to do during the meeting" guardrail list.

- New page: `wiki/concepts/session-1-facilitator-notes.md`, maturity: validated, ~1700 words
- 6 referenced pages received bidirectional backlinks (playbook + shop-1/shop-2 + market template + GBP entity + claude-seo-agrici)
- index.md "Operator-onboarding playbook" subsection now lists both playbook + facilitator notes
- Lint state: 43 pages (was 42), 285 outbound edges (was 272), 0 breaking issues

---

## [2026-05-08] enrich | first-90-days playbook + index polish + thin-page expansion + shop-2 parity

Pre-handoff polish pass. Wiki was structurally clean (0 lint failures) but lacked sequencing for a new operator and had some thin pages.

**New page**:
- `wiki/concepts/first-90-days-playbook.md` — 1773-word week-by-week / month-by-month sequencing playbook bridging every hub. Day-zero pre-flight + Week 1 GBP foundation + Week 2 NAP/citations + Week 3 reviews + Week 4 website + Month 2 content/on-page + Month 3 measurement + recurring cadence + omissions + when-not-to-apply. maturity: validated.

**Expanded (3 thin concept pages)**:
- `wiki/concepts/competitor-analysis-local.md` — 368 → 806 words. Added "How to identify the competitor set" (3 converging methods), structured per-competitor capture template, six-gap framework with cross-references, quarterly refresh workflow.
- `wiki/concepts/local-pack-rankings.md` — 344 → 804 words. Added cluster→hub mapping table, multi-shop per-listing dynamics, common pack-rank mistakes section.
- `wiki/concepts/content-strategy-local.md` — 302 → 791 words. Added editorial calendar table, AI-content workflow (the only acceptable pattern), cross-platform repurposing pattern.

**Structural parity**:
- `wiki/entities/companies/shop-2.md` — 220 → 547 words. Replaced "(Same fields as shop-1)" stubs with full mirrored placeholder structure including service-area-overlap risk callout for multi-shop operators.

**Bidirectional backlink closure**:
- 22 hub/entity pages received `concepts/first-90-days-playbook.md` in their `related:` frontmatter + `## Relations` body. Atomically applied via Python helper.

**Index polish**:
- `wiki/index.md` — Added "Start here" section pointing to README, .env.example, playbook, foundations. Renamed "Tier-2 deep-dives (stubs to populate)" → "Tier-2 deep-dives" (no longer stubs). Added "Operator-onboarding playbook" subsection ahead of Tier-1 hubs.

**Lint state**: 42 pages (was 41), 272 outbound edges (was 226), 0 breaking issues. Strict CI passes.

---

## [2026-05-07] ingest | Aggarwal 2024 GEO paper + Phase-0 audit of 21 GitHub SEO/GEO repos

First content-bearing ingest. Three documents arrived in `research to be indexed/`:

1. `GEO- Generative Engine Optimization.pdf` — Aggarwal et al. KDD '24 empirical study (12 pages)
2. `GitHub Repo Audit for Local SEO.docx` — Phase-0 audit of 21 SEO/GEO/local-business GitHub repos
3. `S-LCG- Structured Linear Congruential Generator-Based Deterministic Algorithm for Search and Optimization.pdf` — pure-math optimization paper (off-topic)

**Source pages created (3)**:
- `wiki/sources/aggarwal-2024-geo-paper.md` — maturity: validated. Full extract: 9 GEO methods ranked by Position-Adjusted Word Count (Quotation Addition +41%, Statistics Addition +33%, Fluency Optimization +28%, Cite Sources +27%, Keyword Stuffing -8%); small-business democratization finding (Cite Sources +115% lift for rank-5 sites, -30% for rank-1); Business-domain guidance (Fluency Optimization primary); Fluency+Statistics best 2-method combo. 4 cited Snippets.
- `wiki/sources/github-repo-audit-2026-05-07.md` — maturity: validated. 21 repos, 4 GO + 1 CONDITIONAL-GO + 16 NO-GO. Hard policy NO-GO: `goenning/google-indexing-script` (abuses Indexing API, terms violation). Critical platform finding: 4/5 GO+cGO tools are **Claude Code Agent Skills**, not Claude Desktop MCPs.
- `wiki/sources/slcg-paper-off-topic.md` — maturity: draft. Stub recording the off-topic paper for ingest-completeness; recommends relocation.

**Tool entity pages created (5)**:
- `wiki/entities/tools/yoast-seo.md` — WordPress plugin (GPL-3.0, 77K stars). Install: WordPress admin → Plugins. validated.
- `wiki/entities/tools/marketingskills.md` — Claude Code skill (MIT, 19K stars). Install: `/plugin install marketing-skills`. PAS, AIDA, product-marketing-context pattern. validated.
- `wiki/entities/tools/claude-seo-agrici.md` — Claude Code skill (CC-BY, 3.5K stars). Install: `/plugin marketplace add AgriciDaniel/claude-seo`. Slash commands `/seo local`, `/seo maps`, `/seo nap`, `/seo grid`, `/seo competitors`. Built-in doorway-page warn-at-30 + hard-stop-at-50. validated.
- `wiki/entities/tools/geo-seo-claude.md` — Claude Code skill (MIT, 6.7K stars). Citability scoring, AI-crawler analysis, schema validation. Operationalizes Aggarwal paper measurement side. validated.
- `wiki/entities/tools/seomachine.md` — Claude Code skill (MIT, 6.8K stars). Long-form content + AI-watermark scrubbing + DataForSEO API. CONDITIONAL-GO (operator must self-config DataForSEO key). draft.

**New concept page (1)**:
- `wiki/concepts/claude-platforms.md` — meta/setup reference. Claude Desktop (MCP, `claude_desktop_config.json`) vs Claude Code (Agent Skills, `/plugin marketplace add`). Distribution-mapping table for the local-SEO domain. Recommends installing Claude Code when ready to adopt the 4 GO'd skills. validated.

**Concept page enriched**:
- `wiki/concepts/generative-engine-optimization.md` — moved `maturity: draft → validated`. New section "What the Aggarwal 2024 paper measured" with full 9-method results table + small-business democratization finding + Business-domain Fluency-Optimization guidance + Fluency+Statistics best-combo finding. Keyword Stuffing -8% upgraded `[CONFIRMED]`. Playbook extended with steps 8-9: apply Aggarwal top-3 methods + run citability audits via geo-seo-claude. 4 cited Snippets added.

**Bidirectional backlinks added** (CLAUDE.md discipline) on 11 existing concept pages: `on-page-seo-local`, `schema-markup-local` (×2), `website-essentials-local-business`, `content-strategy-local` (×2), `review-response-templates`, `local-seo-foundations` (×2), `google-business-profile`, `near-me-search`, `local-pack-rankings`, `citation-building`, `competitor-analysis-local`. Each adds the relevant tool entity / source page to both `related:` frontmatter and `## Relations` body.

**Index updates**: `wiki/index.md` now has Sources section (3 entries split into "Research papers" / "Audits + evaluations" / "Off-topic / record-only"), 5 new tool entries, and a new "Meta / setup" subsection under Concepts for `claude-platforms.md`.

**Raw sources moved**: 3 PDFs/docx moved from `research to be indexed/` to local `raw-sources/` directory (gitignored — no librarian server in this workspace; raw sources stay local on the operator's laptop).

**Pages touched**: 9 created + 12 edited (1 enriched concept + 11 backlink updates) + 2 index/log = 23 pages.

**Operator-facing implication**: friend currently uses Claude Desktop. To adopt the 4 GO'd skills (claude-seo-agrici, geo-seo-claude, marketingskills + the cGO seomachine) he needs **Claude Code installed alongside** Claude Desktop. The `claude_desktop_config.json.example` already-shipped in the workspace remains correct as-is for Claude Desktop — none of the audit's findings are MCPs. Yoast is a WordPress plugin (separate install path). See `concepts/claude-platforms.md` for the canonical reference.

**Next**: lint pass + commit. Adoption decisions (Claude Code install, Yoast install on the website, which skills to enable first) are operator-side and gated on the operator + website status.

---

## [2026-05-07] scaffold | initial wiki seeded for local brick-and-mortar barbershop operator

HEAVY-mode wiki scaffolding for a brick-and-mortar local-services SEO/GEO knowledge hub (seed domain: a two-shop barbershop business). Modeled on OSINT-workspace + 3D-printing-wiki precedents. Designed to generalize across local-service categories (restaurants, dental, auto, salons, gyms, retail) — the barbershop examples are illustrative, not scope-limiting.

**Top-level files**:
- `CLAUDE.md` — schema (folder layout, page format, ingest/query/lint operations, MCP tools, distribution rules, hard policy boundaries, Phase-0 audit pattern, session-start ritual)
- `LESSONS.md` — empty starter
- `ROADMAP.md` — W1 active workstream + open decisions about operator's shop data
- `hot.md` — session-state cache
- `.gitignore` — gitignores `research-to-be-indexed/`, `briefs/`, `.claude/`, `hot.md`, `.env`, `claude_desktop_config.json`
- `.env.example` — Brave + Exa API key placeholders
- `claude_desktop_config.json.example` — MCP config (filesystem, brave-search, playwright, context7) with user-replaceable placeholders
- `.claude/settings.local.json` — Claude Code permissions
- `prompts/github-repo-eval.md` — Phase-0 audit prompt for SEO-tool / local-business-tool repos with hard NO-GO triggers (review gating, GBP automation, fake reviews, blackhat tactics) + operator-fit (non-coder runnability) check

**Wiki Tier-1 hubs (8 concept pages)**:
- `concepts/local-seo-foundations.md` — main hub
- `concepts/google-business-profile.md` — GBP playbook
- `concepts/reviews-reputation-management.md` — review acquisition/response with hard policy boundaries
- `concepts/website-essentials-local-business.md` — must-have pages + mobile UX + Core Web Vitals + schema
- `concepts/social-media-for-barbershops.md` — platform priority + content categories
- `concepts/generative-engine-optimization.md` — GEO/AEO operator playbook
- `concepts/barbershop-marketing-fundamentals.md` — industry hub: visit frequency, LTV, two-shop dynamics
- `concepts/near-me-search.md` — implicit-location query behavior + grid-based rank tracking

**Wiki Tier-2 stubs (7 concept pages)**:
- `concepts/schema-markup-local.md`
- `concepts/citation-building.md`
- `concepts/on-page-seo-local.md`
- `concepts/content-strategy-local.md`
- `concepts/competitor-analysis-local.md`
- `concepts/local-pack-rankings.md`
- `concepts/review-response-templates.md` (with 5-star / 4-star / 3-or-lower / 1-star-likely-fake skeleton templates)

**Entity stubs**:
- `entities/companies/shop-1.md` + `shop-2.md` — operator-fillable placeholders; shop-2 has "Relationship to Shop 1" section
- `entities/markets/local-market-template.md` — fillable template for the operator's market: city/county context, adjacent municipalities, cultural notes, citation directories
- `entities/platforms/{google-business-profile,instagram,yelp,tiktok,facebook,apple-business-connect,bing-places}.md` — 7 platform entities
- `entities/tools/{google-search-console,google-analytics-4,local-falcon,semrush,ahrefs,brightlocal}.md` — 6 tool entities

**Bidirectional-link discipline**: Tier-1 hubs (local-seo-foundations, website-essentials, near-me-search) retroactively edited to backlink to all Tier-2 tool entities and competitor-analysis-local concept page that forward-link them.

**Index + log written**: `wiki/index.md` + `wiki/log.md` (this entry).

**Sources directory**: `wiki/sources/` created (empty + `.gitkeep`); will be populated via `research to be indexed/` drop-zone ingests.

Total scaffold: 30 wiki pages across 4 page types (concept + entity-platform + entity-company + entity-market + entity-tool). All pages `maturity: draft`. All `[NEEDS VERIFICATION 2026-05-07]` tags pending source ingest.

**Next**: operator drops research documents into `research to be indexed/`. Ingest pipeline reads → discusses key takeaways → creates source pages → updates entity/concept pages → moves raw to permanent location → updates index + log.

---

## [2026-05-08] lint | close all bidirectional backlink gaps across wiki (114 gaps → 0)

Automated gap scan found 114 missing reciprocal backlinks across 38 wiki pages after the creator-marketing expansion. Python script added missing `related:` frontmatter entries + `## Relations` body links to each target page.

**Result:** 0 missing backlinks, 5 dangling links (2 gitignored briefs, 3 cross-wiki references to image-gen-wiki — all legitimate).

Pages touched: 38.

Gap breakdown by file:
- `concepts/ai-assistance-guardrails.md` +1 · `concepts/ai-assitance-guardrails.md` +1 · `concepts/citation-building.md` +4 · `concepts/competitor-analysis-local.md` +2 · `concepts/creator-audience-growth.md` +8 · `concepts/creator-content-strategy.md` +13 · `concepts/creator-external-promotion.md` +9 · `concepts/creator-marketing-foundations.md` +11 · `concepts/creator-retention.md` +3 · `concepts/customer-retention-barbershop.md` +1 · `concepts/generative-engine-optimization.md` +3 · `concepts/google-ads-local.md` +2 · `concepts/google-business-profile.md` +4 · `concepts/local-pack-rankings.md` +1 · `concepts/meta-ads-local.md` +3 · `concepts/near-me-search.md` +1 · `concepts/on-page-seo-local.md` +3 · `concepts/review-response-templates.md` +2 · `concepts/reviews-reputation-management.md` +5 · `concepts/schema-markup-local.md` +2 · `concepts/social-media-for-barbershops.md` +2 · `concepts/website-essentials-local-business.md` +1 · `entities/companies/shop-1.md` +2 · `entities/companies/shop-2.md` +3 · `entities/platforms/apple-business-connect.md` +1 · `entities/platforms/bing-places.md` +2 · `entities/platforms/fanvue.md` +3 · `entities/platforms/google-business-profile.md` +2 · `entities/platforms/instagram.md` +2 · `entities/platforms/onlyfans.md` +8 · `entities/platforms/tiktok.md` +1 · `entities/platforms/twitter-x.md` +1 · `entities/platforms/yelp.md` +1 · `entities/tools/claude-seo-agrici.md` +1 · `entities/tools/google-analytics-4.md` +2 · `entities/tools/google-search-console.md` +1 · `entities/tools/local-falcon.md` +1 · `entities/tools/marketingskills.md` +1

Note: 4 concept pages (first-90-days-playbook, barbershop-marketing-fundamentals, session-1-facilitator-notes, local-seo-foundations) and log.md already had full reciprocal coverage — no gaps found. Bulk of gaps concentrated in creator-marketing pages from the May 8 expansion that forward-linked to many entities but missed the reciprocal.

---

## [2026-05-08] add | marketing expansion — google ads, meta ads, retention, promotions

User requested expanding the marketing aspect of the wiki with 4 new concept pages. Researched current 2024-2026 best practices for each topic, then created full workflow-grade pages.

- **[google-ads-local](concepts/google-ads-local.md)** — maturity: draft, ~900 words. Campaign types (Search/LSA/Display), radius targeting (3-10 miles, 5-mile sweet spot), dayparting, device bid adjustments, budget tiers ($5-50/day), landing page requirements (never homepage → dedicated service pages), Quality Score factors, key metrics (CPA $15 target, CTR 5-10%), common mistakes, GBP integration (70% more visits with complete profile). 6 sources cited.

- **[meta-ads-local](concepts/meta-ads-local.md)** — maturity: draft, ~850 words. Campaign objectives (Traffic/Conversions/Brand Awareness/Lead Gen), geo/demographic/interest targeting, creative best practices (before/after photos, 15-30s Reels, copy formula [Hook]+[Offer]+[CTA]), Instagram vs Facebook placement strategy, retargeting (Pixel-based, engagement, profile visitors), local page vs central brand (local pages 12% better retention), ROAS 4:1 target. 7 sources cited.

- **[customer-retention-barbershop](concepts/customer-retention-barbershop.md)** — maturity: draft, ~950 words. Retention fundamentals (quality + relationship + scheduling), loyalty programs (25% more repeat business, points/tiered/punch/subscription models, digital vs paper comparison $19-50/mo vs $30-100/yr), referral programs (double-sided rewards, 25-40% acquisition lift), win-back campaigns (4-6 weeks soft, 6-8 weeks incentive, 8+ weeks aggressive), VIP perks (priority booking, skip-the-wait, birthday rewards), measurement metrics (retention rate 60-70% avg, LTV $500+/yr). 8 sources cited.

- **[promotional-campaigns-barbershop](concepts/promotional-campaigns-barbershop.md)** — maturity: draft, ~1000 words. Seasonal calendar (Back-to-School Aug-Sep, Wedding Season Apr-Jun/Sep-Oct, Holiday Nov-Dec, Summer Prep May-Jun), weekly recurring promotions (Manic Monday, Early Bird, Ladies Day, Friday Fresh), tactical types (flash sales, birthday campaigns 10x conversion vs standard, upsell/cross-sell at checkout), cross-promotions (coffee shop, gym, men's clothing, wedding venues), amplification channels (GSC cost $0, Meta $5-20/day, SMS $0.01-0.02/msg), promotion metrics (redemption rate 5-15% target). 8 sources cited.

**Index updated**: wiki/index.md "Tier-2 deep-dives" section now includes all 4 new pages in alphabetical order.

**Bidirectional backlinks**: each new page links to 3-4 related pages in `related:` frontmatter + `## Relations` body; those pages updated with reciprocal links.

**Pages touched**: 4 created + 12 edited (backlink updates) + index.md + log.md = 18 pages.

**Sources ingested**: 0 new source pages (all 4 pages synthesized from web research via Brave Search; no new raw-source drops). Tagged as `[Source: https://... (retrieved 2026-05-08)]`.

**Next**: operator tests loyalty program + referral workflow in real shop; promote pages to `validated` after real-world LTV/retention measurement.

## [2026-05-15] cross-wiki route | open-seo — SEO automation skill set

Cross-wiki stub routed from `@osint-wiki/entities/tools/open-seo.md`.
- Created wiki/entities/tools/open-seo.md (stub)

## [2026-05-17] cross-wiki route | html-anything + itshover + oransim (OSINT 56-repo tool eval)

Three tools cross-routed from the OSINT workspace 56-repo multi-wiki tool eval (`@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`). All three Adopt-tier, SEO-primary-fit; full entity pages (not stubs).

**Created (3 entity pages):**
- `entities/tools/html-anything.md` — agentic local HTML editor (nexu-io, Apache-2.0, HTML/TS, ~283★). LLM-driven web-design generation + sandboxed templates + one-click deploy to WeChat/X. Lets Claude Code / Codex act as autonomous design engines enforcing DESIGN.md guidelines.
- `entities/tools/itshover.md` — motion-first React icon component suite (itshover.com, MIT, React/TS, Vercel-backed). Copy/paste/customize SVG motion in source; zero dependency bloat; Next.js/shadcn-compatible.
- `entities/tools/oransim.md` — local-first causal simulator for marketing-campaign ROI (OranAi-Ltd, Apache-2.0, Python/SCM). SCM over a creative-to-user graph, LLM "user souls" reacting via embeddings, Hawkes processes + do-calculus. Test campaign assets before capital deployment.

**Linked existing pages (bidirectional backlinks added, `updated:` bumped):**
- `entities/tools/claude-code-tool-stack.md` — html-anything + itshover added (web-generation surface / Next.js-shadcn icon assets)
- `entities/tools/awesome-design-md.md` — html-anything + itshover added (DESIGN.md enforcement editor / motion-icon assets)
- `concepts/website-essentials-local-business.md` — html-anything + itshover added (client-site delivery)
- `concepts/competitor-analysis-local.md` — oransim added (pre-spend promotion-ROI forecasting)
- `concepts/creator-content-strategy.md` — oransim added (simulation-testing content plans)

**Index updated**: 3 new rows in Tools section (alphabetical, `cross-wiki` tag).

**Pages touched**: 3 created + 5 edited (backlinks) + index.md + log.md = 10.

Cross-route notes recorded on pages: html-anything → image-gen-wiki + ccc-wiki; oransim → osint-wiki (causal/temporal-cascade modeling).

---

## [2026-05-21] ingest | briefs/ triage — 19 briefs processed (all historical)

Full inventory and triage of every unprocessed brief in `briefs/`. 19 briefs, 19 `processed: 2026-05-21` markers added. No briefs deleted — provenance trail preserved.

**Already ingested (9 briefs, marker only):** tool-adoption-handoff, ai-content-workflow, fanvue-synthetic-creator-gtm, manual_17 (GBP reply), onlyfans-account-setup, onlyfans-launch-strategy, creator-24hr-sprint, creator-launch-decision-hub, obsidian-integration. All had their substantive content already folded into existing wiki pages.

**Promoted to concept pages (2):**
- `concepts/ugc-monetization-loop.md` — 3-platform UGC creator monetization (TikTok+IG+Pinterest) from @timbidefi's X post; Claude pattern extraction + Higgsfield faceless video generation + retainer-based pricing
- `concepts/claude-ecommerce-workflows.md` — 5 reusable Claude prompt templates for Shopify/e-commerce from @gippp69 (competitor autopsy, negative-review mining, 5-email post-purchase sequence, UGC ad scripts, Sunday diagnostic)

**Promoted to entity stubs (5):**
- `entities/tools/digital-marketing-pro.md` — 115-command Claude plugin ecosystem, 67 MCP servers, QA/claim-verification layer
- `entities/tools/n8n-workflows.md` — 4,343-script automation library (MIT)
- `entities/tools/pm-claude-skills.md` — 106 SKILL.md files, marketing-analysis + Figma-template-generation
- `entities/tools/garden-skills.md` — 4,900★ MIT web-design-engineer templates
- `entities/tools/reactive-resume.md` — 37k★ MIT; Steal-from CSS template architecture + JSON→PDF/DOCX pipeline

**Reference-only index entries (4):** evilcharts, svgrepo, mobilepalette, markdown-preview-pluk — cataloged under new "Tools — reference-only" subsection.

**Index gaps fixed (2):** `creator-content-flywheel.md` and `viral-content-mechanics.md` existed on disk but were missing from index — added to Creator marketing section.

**Pages touched**: 7 created + index.md + log.md = 9. 19 briefs marked processed.
style-pass | Posts.docx K88 | 42 posts (5 PM/HL deep-read) | authors: ScottyBeamIO, myttle_web3, DankoWeb3, cyrilXBT, Damir_Akaza
style-pass | Posts.docx K112 | 8 long-forms | authors: Gustafssonkotte, horizon_trade_x, AlterEgo_eth, Arvin Shivram, Lutchyn13, 0xSurferX, zodchiii, akshay_pacha

## [2026-06-26] brief | CXW/GEO detention turnkey — WSB handoff

- **Brief:** `briefs/2026-06-26_cxw-geo-detention-turnkey-wsb-handoff.md` — cross-wiki from `@osint-wiki/concepts/geo-ice-turnkey-acquisition-thesis.md` + Jun 2026 catalyst chain (Secure America Act, Appropriations hearing timing, Benchmark PT $36)
- **Target:** r/wallstreetbets DD draft ready-for-post
- **Primary source:** Investing.com Benchmark note (Jun 26, 2026)ar

## [2026-07-05] cross-wiki route | SparkToro Blog — New Research from Similarweb: How AI Brand Mentions Influence Direct Visits & Traditional Search Queries

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-sparktoro-2026-06-29-new-research-from-similarweb-how-ai-brand-mentio.md`.
- Created wiki/sources/newsletter-rss-sparktoro-2026-06-29-new-research-from-similarweb-how-ai-brand-mentio.md (stub)

## [2026-08-03] brief | K220 eve marketing extract from OSINT

- Brief: `briefs/2026-08-03_k220-eve-marketing-extract.md` (OSINT K220 revenue eval)
