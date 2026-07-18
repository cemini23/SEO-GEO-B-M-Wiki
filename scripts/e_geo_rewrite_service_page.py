#!/usr/bin/env python3
"""Build an E-GEO-style rewrite prompt for local B&M service/location pages.

Uses adopted prompts from raw-sources/tools/E-GEO/src/optimized_prompts.json
(CONDITIONAL-GO — research use; no LICENSE on upstream).

Does not call an LLM itself — prints a ready-to-paste prompt so Claude/Cursor
(or the operator) can run the rewrite with factual shop copy only.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_PATH = ROOT / "raw-sources/tools/E-GEO/src/optimized_prompts.json"
BEST_PROMPTS_PATH = (
    ROOT / "raw-sources/datasets/E-GEO/results/META_OPT_RESULTS/best_prompts.json"
)

# Styles that transfer cleanest to local service pages (scannable + intent + facts).
DEFAULT_STYLES = ("competitive", "FAQ", "authoritative", "format")

LOCAL_ADAPTER = """
DOMAIN ADAPTER (local brick-and-mortar / service business — NOT e-commerce SKUs):
- Treat the input as a service or location page, not a product listing.
- Keep NAP, hours, prices, and services factually identical to the source text.
- Prefer neighborhood / "near me" / walk-in language customers actually use.
- Do NOT invent awards, competitor comparisons, or fake reviews.
- Do NOT add "rank us first" or engine-gaming instructions into the page copy.
- End with one clear CTA: Book / Call / Directions (whichever the source supports).
"""


def load_prompts() -> dict[str, str]:
    path = PROMPTS_PATH if PROMPTS_PATH.is_file() else BEST_PROMPTS_PATH
    if not path.is_file():
        sys.stderr.write(
            f"Missing prompts at {PROMPTS_PATH} (and fallback {BEST_PROMPTS_PATH}).\n"
            "Run: bash scripts/adopt_k142_phase0.sh\n"
        )
        sys.exit(1)
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        sys.stderr.write(f"Unexpected JSON shape in {path}\n")
        sys.exit(1)
    return {str(k): str(v) for k, v in data.items()}


def build_prompt(style: str, description: str, prompts: dict[str, str]) -> str:
    if style not in prompts:
        available = ", ".join(sorted(prompts))
        raise SystemExit(f"Unknown style {style!r}. Available: {available}")
    template = prompts[style]
    if "{description}" not in template:
        raise SystemExit(f"Style {style!r} has no {{description}} placeholder")
    filled = template.replace("{description}", description.strip())
    return filled + "\n" + LOCAL_ADAPTER.strip() + "\n"


def main() -> None:
    prompts = load_prompts()
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--style",
        default="competitive",
        help=f"Prompt style key (default competitive). Try: {', '.join(DEFAULT_STYLES)}",
    )
    p.add_argument(
        "--list",
        action="store_true",
        help="List available style keys and exit",
    )
    p.add_argument(
        "--file",
        type=Path,
        help="Path to current service-page copy (UTF-8). If omitted, read stdin.",
    )
    p.add_argument(
        "--out",
        type=Path,
        help="Write built prompt to this path (default: stdout)",
    )
    args = p.parse_args()

    if args.list:
        for k in sorted(prompts):
            mark = " *" if k in DEFAULT_STYLES else ""
            print(f"{k}{mark}")
        print("\n* = recommended for local B&M service pages")
        return

    if args.file:
        description = args.file.read_text(encoding="utf-8")
    else:
        if sys.stdin.isatty():
            sys.stderr.write("Paste service-page copy, then Ctrl-D (EOF):\n")
        description = sys.stdin.read()
    if not description.strip():
        raise SystemExit("Empty description — pass --file or pipe text on stdin")

    out = build_prompt(args.style, description, prompts)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(out, encoding="utf-8")
        print(f"Wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
