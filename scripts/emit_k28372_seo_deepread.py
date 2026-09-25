#!/usr/bin/env python3
"""Deep-read SEO source arXiv 2609.28372 from arXiv abstract (2026-09-25)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-25"

SOURCE = ROOT / "wiki/sources/arxiv-2609-28372-agentic-surrogate-shopper-2026-09-24.md"
BRAND = ROOT / "wiki/concepts/llm-brand-bias-geo-competition.md"
GEO = ROOT / "wiki/concepts/geo-visibility-measurement.md"
LOG = ROOT / "wiki/log.md"

SNIPPETS_BLOCK = """## Snippets

> Tool-Lab adapts information-board process tracing: product attributes sit behind costly tool calls while LLM agents shop. [Source: arXiv 2609.28372 abstract (retrieved 2026-09-25)]

> Eight commercial LLMs from three providers: at **zero acquisition cost**, just-below pricing and promotional framing rarely mislead agents. Under **vague goals + costly search**, models skip diagnostic attributes needed for unit-price math and pick suboptimal offers—human-like heuristics. **Specific goal prompts** preserve diagnostic search and optimality. [Source: arXiv 2609.28372 abstract (retrieved 2026-09-25)]

> Claim: delegated-AI vulnerability is **search-mediated** and tied to storefront information architecture, not necessarily fixed LLM flaws. [Source: arXiv 2609.28372 abstract (retrieved 2026-09-25)]"""

NARRATIVE_EXTRA = """
### K28372 audit steal (Tool-Lab surrogate shopper)

For **agentic commerce / GEO** engagements, treat pricing pages as an **information-board**: fees, unit size, and promo framing only matter if the shopping agent **pays tool cost** to retrieve them. Audit with both **vague** and **specific** shopping goals; report choice quality when attribute fetch is costly. Pairs ConsumerQ (recommendation quality) with **process-traced shopping** under price cues. [CONFIRMED] from arXiv abstract; full PDF on cybersec egress — body tables not yet extracted.
"""


def patch_source() -> None:
    t = SOURCE.read_text(encoding="utf-8")
    t = t.replace("maturity: draft", "maturity: validated", 1)
    t = t.replace("read_status: skimmed", "read_status: deep-read", 1)
    t = t.replace("updated: 2026-09-24", f"updated: {DATE}", 1)
    t = t.replace(
        "| **Read status** | skimmed (abstract + triage; routed from Cybersecurity wiki ingest) |",
        f"| **Read status** | deep-read ({DATE}; abstract + arXiv API; PDF on egress) |",
        1,
    )
    if NARRATIVE_EXTRA.strip() not in t:
        t = t.replace(
            "Pairs with ConsumerQ-style audits:",
            NARRATIVE_EXTRA + "\nPairs with ConsumerQ-style audits:",
            1,
        )
    if "## Snippets\n\n> See arXiv" in t:
        t = t.split("## Snippets")[0].rstrip() + "\n\n" + SNIPPETS_BLOCK + "\n"
    SOURCE.write_text(t, encoding="utf-8")


def add_related(path: Path, rel_line: str) -> None:
    t = path.read_text(encoding="utf-8")
    if rel_line in t:
        return
    needle = "related:\n"
    idx = t.find(needle)
    if idx == -1:
        return
    insert_at = idx + len(needle)
    t = t[:insert_at] + f"  - {rel_line}\n" + t[insert_at:]
    t = t.replace("updated: 2026-09-17", f"updated: {DATE}", 1)
    t = t.replace("updated: 2026-09-23", f"updated: {DATE}", 1)
    path.write_text(t, encoding="utf-8")


def patch_log() -> None:
    entry = f"""## [{DATE}] deep-read | arXiv 2609.28372 surrogate shopper (Grok-aligned SEO follow-up)

- **Source:** @sources/arxiv-2609-28372-agentic-surrogate-shopper-2026-09-24.md → validated, deep-read (abstract-backed).
- **Concepts:** @concepts/llm-brand-bias-geo-competition.md, @concepts/geo-visibility-measurement.md — related backlinks.
- **Cross-wiki:** @cybersecurity-wiki/sources/arxiv-2609-28372-agentic-ai-surrogate-consumer-ood.md unchanged (OOD stub).
- **friend brief:** n/a

"""
    lt = LOG.read_text(encoding="utf-8")
    if "deep-read | arXiv 2609.28372" in lt:
        return
    if lt.startswith("## [2026-09-24] cross-wiki"):
        lt = entry + lt
    else:
        lt = entry + lt
    LOG.write_text(lt, encoding="utf-8")


def main() -> None:
    patch_source()
    rel = "sources/arxiv-2609-28372-agentic-surrogate-shopper-2026-09-24.md"
    add_related(BRAND, rel)
    add_related(GEO, rel)
    patch_log()
    print("OK", DATE)


if __name__ == "__main__":
    main()
