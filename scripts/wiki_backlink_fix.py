#!/usr/bin/env python3
"""Add missing reciprocal `related:` backlinks to the wiki.

The wiki's convention is that `related:` is bidirectional: if A lists B, B must
list A. wiki_lint.py check 2 reports the violations. This script repairs them.

It computes the gaps itself rather than parsing lint output, because the linter
truncates its per-target listing at five sources.

Only targets that already declare a `related:` list are patched. Pages with no
`related:` key are one-way indexes (generated sweeps, logs) and are skipped —
wiki_lint.py exempts them for the same reason.

Usage:
  python3 scripts/wiki_backlink_fix.py [--dry-run] [--limit N]

  --dry-run   report what would change; write nothing
  --limit N   patch at most N targets, highest-count first (default: all)
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
TODAY = "2026-10-01"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)
RELATED_LIST_RE = re.compile(r"^related:\s*\n((?:[ \t]+-[ \t]+.*\n?)+)", re.M)
RELATED_INLINE_RE = re.compile(r"^related:\s*\[(.*?)\]\s*$", re.M)


def parse_related(text):
    """Return (related_list, has_related_key, is_list_form)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return [], False, False
    fm = m.group(1)

    if re.search(r"^related:", fm, re.M) is None:
        return [], False, False

    rl = RELATED_LIST_RE.search(fm)
    if rl:
        items = []
        for line in rl.group(1).splitlines():
            s = line.strip()
            if s.startswith("- "):
                v = s[2:].strip()
                if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "'"):
                    v = v[1:-1]
                items.append(v)
        return items, True, True

    ri = RELATED_INLINE_RE.search(fm)
    if ri:
        return [s.strip() for s in ri.group(1).split(",") if s.strip()], True, False

    return [], True, False


def normalize(p):
    p = p.strip().lstrip("/")
    if p.startswith("wiki/"):
        p = p[len("wiki/"):]
    return p


def load_wiki():
    pages = {}   # rel -> dict
    for path in WIKI.rglob("*.md"):
        rel = str(path.relative_to(WIKI))
        if rel in ("index.md", "log.md", "dashboard.md"):
            continue
        text = path.read_text(errors="replace")
        related, has_key, is_list = parse_related(text)
        pages[rel] = {
            "path": path,
            "related": related,
            "has_key": has_key,
            "is_list": is_list,
        }
    return pages


def related_block_span(lines):
    """Return (start, end) of the frontmatter `related:` list, or None."""
    if not lines or lines[0].strip() != "---":
        return None
    fm_end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm_end = i
            break
    if fm_end is None:
        return None

    start = None
    for i in range(1, fm_end):
        if re.match(r"^related:\s*$", lines[i]):
            start = i
            break
    if start is None:
        return None  # inline form or absent

    end = start + 1
    while end < fm_end and re.match(r"^\s+- ", lines[end]):
        end += 1
    return start, end


def patch_target(rel, sources, dry_run):
    path = WIKI / rel
    lines = path.read_text(errors="replace").splitlines(keepends=True)
    span = related_block_span(lines)
    if span is None:
        return 0

    start, end = span
    existing = set()
    for line in lines[start + 1:end]:
        m = re.match(r"^\s+- (.+?)\s*$", line)
        if m:
            existing.add(m.group(1).strip().strip('"').strip("'"))

    added = sorted(s for s in sources if s not in existing)
    if not added:
        return 0

    if not lines[end - 1].endswith("\n"):
        lines[end - 1] += "\n"
    new_lines = [f"  - {s}\n" for s in added]
    out = lines[:end] + new_lines + lines[end:]

    if not dry_run:
        text = "".join(out)
        text = re.sub(r"^updated: .*$", f"updated: {TODAY}", text, count=1, flags=re.M)
        path.write_text(text)
    return len(added)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="patch at most N targets")
    args = ap.parse_args()

    pages = load_wiki()
    all_paths = set(pages)

    outbound = defaultdict(set)
    for rel, meta in pages.items():
        for raw in meta["related"]:
            tgt = normalize(raw)
            if tgt.startswith("briefs/"):
                continue
            if tgt in all_paths:
                outbound[rel].add(tgt)

    gaps = defaultdict(list)
    for src, tgts in outbound.items():
        for tgt in tgts:
            if not pages[tgt]["has_key"]:
                continue          # one-way index — exempt
            if src not in outbound.get(tgt, set()):
                gaps[tgt].append(src)

    if not gaps:
        print("No bidirectional gaps. Nothing to do.")
        return 0

    targets = sorted(gaps, key=lambda t: -len(gaps[t]))
    if args.limit:
        targets = targets[:args.limit]

    total, touched = 0, []
    for tgt in targets:
        n = patch_target(tgt, gaps[tgt], args.dry_run)
        if n:
            total += n
            touched.append((tgt, n))

    verb = "would add" if args.dry_run else "added"
    print(f"{verb} {total} backlink(s) across {len(touched)} page(s)")
    for t, n in touched[:30]:
        print(f"  +{n:3d}  {t}")
    if len(touched) > 30:
        print(f"  ... and {len(touched) - 30} more page(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
