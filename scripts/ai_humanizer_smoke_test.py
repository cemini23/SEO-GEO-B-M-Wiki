#!/usr/bin/env python3
"""Smoke-test AI Text Humanizer against local-business marketing samples.

Run from repo root:
  ~/.cemini/venvs/ai-text-humanizer/bin/python scripts/ai_humanizer_smoke_test.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_DIR = ROOT / "tools" / "ai-text-humanizer"
DEFAULT_VENV = Path.home() / ".cemini" / "venvs" / "ai-text-humanizer" / "bin" / "python"

if DEFAULT_VENV.is_file() and Path(sys.executable).resolve() != DEFAULT_VENV.resolve():
    os.execv(str(DEFAULT_VENV), [str(DEFAULT_VENV), *sys.argv])

sys.path.insert(0, str(APP_DIR))

from transformer.app import AcademicTextHumanizer, download_nltk_resources  # noqa: E402

SAMPLES = {
    "gbp_post": (
        "Summer fade season is here! We're now open late on Thursdays until 8pm "
        "at our Eastside location. Walk-ins welcome — or book online if you'd "
        "rather skip the wait. First-time clients get 10% off any cut this month."
    ),
    "service_page": (
        "Our signature skin fade takes about 45 minutes and includes a hot towel "
        "finish. We've been serving Austin since 2018 and our barbers specialize "
        "in fades, tapers, and beard shaping. Book your appointment today — we "
        "can't wait to see you."
    ),
    "instagram": (
        "Fresh fade Friday 🔥 Walk-ins open till 6. Tag a friend who needs a "
        "lineup. #AustinBarber #FadeGame"
    ),
}


def main() -> None:
    if not APP_DIR.is_dir():
        print(f"Missing {APP_DIR}. Run: bash scripts/run_ai_humanizer.sh (once) or clone manually.")
        sys.exit(1)

    download_nltk_resources()
    humanizer = AcademicTextHumanizer(seed=42)

    for name, text in SAMPLES.items():
        out = humanizer.humanize_text(text, use_passive=False, use_synonyms=False)
        print(f"\n{'=' * 60}\n{name}\n{'=' * 60}")
        print("ORIGINAL:\n", text, sep="")
        print("\nDEFAULT TRANSFORM:\n", out, sep="")


if __name__ == "__main__":
    main()
