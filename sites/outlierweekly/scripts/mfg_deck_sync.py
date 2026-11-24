#!/usr/bin/env python3
"""Pull the MFG training deck and print what changed since the last pull.

The deck is the QR-code target on the training packet. It changes during
rollout, so this script keeps a local snapshot and reports line-level changes.
The snapshot holds menu text, so it is gitignored and never committed.

Usage:
    python3 scripts/mfg_deck_sync.py            # fetch, diff, save snapshot
    python3 scripts/mfg_deck_sync.py --check    # fetch and diff, keep old snapshot
"""

from __future__ import annotations

import difflib
import pathlib
import sys
import urllib.request

DECK_ID = "1s735bAqavvM-UfEFM4KW-Z6vKiyNMb1DzI_0U2XNybg"
EXPORT_URL = f"https://docs.google.com/presentation/d/{DECK_ID}/export/txt"

HERE = pathlib.Path(__file__).resolve().parent.parent
SNAPSHOT = HERE / ".mfg-deck-snapshot.txt"


def fetch() -> str:
    request = urllib.request.Request(EXPORT_URL, headers={"User-Agent": "mfg-deck-sync/1"})
    with urllib.request.urlopen(request, timeout=60) as response:
        text = response.read().decode("utf-8", "replace")
    if "Presentation" in text[:200] and "export" in text[:200]:
        raise SystemExit("Deck export returned an error page. Check sharing settings.")
    return text


def main() -> int:
    check_only = "--check" in sys.argv
    fresh = fetch()
    if not fresh.strip():
        print("Empty export; nothing to do.")
        return 1

    if not SNAPSHOT.exists():
        if not check_only:
            SNAPSHOT.write_text(fresh, encoding="utf-8")
        print(f"No previous snapshot. Saved {len(fresh)} characters to {SNAPSHOT.name}.")
        print("Next run will show what changed.")
        return 0

    previous = SNAPSHOT.read_text(encoding="utf-8")
    if previous == fresh:
        print("No changes since the last snapshot.")
        return 0

    old = [line.rstrip() for line in previous.splitlines() if line.strip()]
    new = [line.rstrip() for line in fresh.splitlines() if line.strip()]
    diff = list(difflib.unified_diff(old, new, fromfile="previous", tofile="current", n=2))
    print(f"Deck changed. {len(diff)} diff lines:\n")
    for line in diff:
        if line.startswith(("+++", "---", "@@")):
            print(line)
        elif line.startswith(("+", "-")):
            print(line[:220])

    if not check_only:
        SNAPSHOT.write_text(fresh, encoding="utf-8")
        print(f"\nSnapshot updated: {SNAPSHOT.name}")
    else:
        print("\nSnapshot left unchanged (--check).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
