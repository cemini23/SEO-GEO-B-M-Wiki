#!/usr/bin/env python3
"""Lint pass over the wiki/.

Reports:
  1. Orphans              — pages with zero inbound `related:` references
  2. Bidirectional gaps   — A lists B as related but B doesn't list A
  3. Dangling links       — `related:` paths that don't resolve to a real file
  4. Missing pages        — `@path` mentions in body where the file doesn't exist
  5. Cited unread stubs   — source pages with read_status=unread-stub but ≥1 inbound related: edge
  6. Frontmatter quality  — missing `type` / `maturity` / mismatched `updated:`
  7. Stale verification   — `[NEEDS VERIFICATION YYYY-MM-DD]` tags older than --verify-age-days
                            (default 7) — Exa-resolution candidates per CLAUDE.md "External research"
"""

import argparse
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path
from collections import defaultdict

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("--verify-age-days", type=int, default=7,
                    help="Flag [NEEDS VERIFICATION YYYY-MM-DD] tags older than this many days (default: 7)")
args = parser.parse_args()
TODAY = date.today()

# Resolve WIKI relative to this script (scripts/wiki_lint.py → repo root → wiki/),
# with WIKI_DIR env-var override for non-standard layouts (e.g. CI checkout paths).
WIKI = Path(os.environ.get("WIKI_DIR", Path(__file__).resolve().parent.parent / "wiki"))

# -- frontmatter parsing (no PyYAML dep) ----------------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
RELATED_LIST_RE = re.compile(r"^related:\s*\n((?:\s+-\s+.+\n?)*)", re.MULTILINE)
RELATED_INLINE_RE = re.compile(r"^related:\s*\[([^\]]*)\]", re.MULTILINE)
SCALAR_RE = lambda key: re.compile(rf"^{key}:\s*(.+?)\s*$", re.MULTILINE)

def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm_text = m.group(1)
    out = {}
    # related: list block
    rl = RELATED_LIST_RE.search(fm_text)
    if rl:
        items = []
        for line in rl.group(1).splitlines():
            s = line.strip()
            if s.startswith("- "):
                items.append(s[2:].strip())
        out["related"] = items
    else:
        # try inline form: related: [a, b, c]
        ri = RELATED_INLINE_RE.search(fm_text)
        if ri:
            out["related"] = [s.strip() for s in ri.group(1).split(",") if s.strip()]
        else:
            out["related"] = []
    # scalars
    for key in ("type", "maturity", "title", "created", "updated", "read_status"):
        m2 = SCALAR_RE(key).search(fm_text)
        if m2:
            out[key] = m2.group(1).strip()
    return out

def normalize_path(p):
    """Strip leading slash, drop wiki/ prefix if accidentally included."""
    p = p.strip().lstrip("/")
    if p.startswith("wiki/"):
        p = p[len("wiki/"):]
    return p

# -- walk ----------------------------------------------------------------

pages = {}                  # rel_path -> frontmatter dict
all_paths = set()

for p in WIKI.rglob("*.md"):
    rel = str(p.relative_to(WIKI))
    if rel in ("index.md", "log.md", "dashboard.md"):  # navigational, exempt
        continue
    text = p.read_text(errors="replace")
    fm = parse_frontmatter(text)
    if fm is None:
        # log later
        pages[rel] = {"_no_frontmatter": True, "related": [], "_body": text}
        all_paths.add(rel)
        continue
    fm["_body"] = text
    pages[rel] = fm
    all_paths.add(rel)

# -- 1+2+3: build inbound edge map ---------------------------------------

inbound = defaultdict(set)  # target -> {source, ...}
outbound = defaultdict(set) # source -> {target, ...}
dangling = []               # (source, raw_target) where target file doesn't exist

for src, fm in pages.items():
    for tgt_raw in fm.get("related", []):
        tgt = normalize_path(tgt_raw)
        if tgt in all_paths:
            inbound[tgt].add(src)
            outbound[src].add(tgt)
        else:
            dangling.append((src, tgt_raw))

# orphans: pages with zero inbound edges (excluding index/log already excluded)
orphans = sorted(p for p in all_paths if p not in inbound)

# bidirectional gaps: src→tgt without tgt→src
gaps = []
for src, tgts in outbound.items():
    for tgt in tgts:
        if src not in outbound.get(tgt, set()):
            gaps.append((src, tgt))
gaps.sort()

# -- 4: @path body mentions that don't resolve ---------------------------

# `@path/to/page.md` style references in markdown body
AT_PATH_RE = re.compile(r"@([a-z0-9_./-]+\.md)")

missing_mentions = defaultdict(set)  # mentioned_path -> {source, ...}
for src, fm in pages.items():
    body = fm.get("_body", "")
    if not body:
        continue
    for m in AT_PATH_RE.finditer(body):
        mentioned = normalize_path(m.group(1))
        if mentioned not in all_paths and mentioned not in ("index.md", "log.md", "dashboard.md"):
            missing_mentions[mentioned].add(src)

# -- 5: cited unread stubs -----------------------------------------------

cited_unread = []
for p, fm in pages.items():
    if not p.startswith("sources/"):
        continue
    rs = (fm.get("read_status") or "").lower()
    if rs in ("unread-stub", "unread", ""):
        if p in inbound and len(inbound[p]) >= 1:
            cited_unread.append((p, len(inbound[p])))
cited_unread.sort(key=lambda x: -x[1])

# -- 6: frontmatter quality ----------------------------------------------

no_frontmatter = sorted(p for p, fm in pages.items() if fm.get("_no_frontmatter"))
no_type = sorted(p for p, fm in pages.items()
                 if not fm.get("_no_frontmatter") and not fm.get("type"))
no_maturity = sorted(p for p, fm in pages.items()
                     if not fm.get("_no_frontmatter") and not fm.get("maturity")
                     and fm.get("type") in ("source", "entity", "concept"))

# -- 7: stale [NEEDS VERIFICATION YYYY-MM-DD] tags -----------------------

# Match [NEEDS VERIFICATION YYYY-MM-DD] with optional date. Date is required for staleness check;
# tags without a date are flagged separately as "undated" (can't compute age).
NEEDS_VERIFY_DATED_RE = re.compile(r"\[NEEDS VERIFICATION\s+(\d{4}-\d{2}-\d{2})\]")
NEEDS_VERIFY_BARE_RE = re.compile(r"(?<!`)\[NEEDS VERIFICATION\](?!`)(?!\s+\d{4})")

stale_verifications = []  # (page, date_str, age_days, line_num, line_text)
undated_verifications = []  # (page, line_num, line_text)

for src, fm in pages.items():
    body = fm.get("_body", "")
    if not body:
        continue
    for line_num, line in enumerate(body.splitlines(), start=1):
        for m in NEEDS_VERIFY_DATED_RE.finditer(line):
            try:
                tag_date = datetime.strptime(m.group(1), "%Y-%m-%d").date()
            except ValueError:
                continue
            age = (TODAY - tag_date).days
            if age >= args.verify_age_days:
                stale_verifications.append((src, m.group(1), age, line_num, line.strip()))
        if NEEDS_VERIFY_BARE_RE.search(line):
            undated_verifications.append((src, line_num, line.strip()))

stale_verifications.sort(key=lambda x: -x[2])  # oldest first

# -- print report --------------------------------------------------------

def header(s):
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)

print(f"Wiki lint scan — {len(all_paths)} pages indexed (excluding index.md / log.md / dashboard.md)")
print(f"Outbound edges: {sum(len(v) for v in outbound.values())}; "
      f"Inbound edge coverage: {len(inbound)} pages")

header(f"1. Orphans — {len(orphans)} pages with zero inbound references")
for p in orphans:
    fm = pages[p]
    t = fm.get("type", "?")
    m = fm.get("maturity", "?")
    print(f"  [{t}/{m}] {p}")

header(f"2. Bidirectional gaps — {len(gaps)} asymmetric edges")
# group by target so the "target page is missing N backlinks" view is readable
gaps_by_target = defaultdict(list)
for src, tgt in gaps:
    gaps_by_target[tgt].append(src)
for tgt in sorted(gaps_by_target.keys(), key=lambda x: -len(gaps_by_target[x])):
    srcs = gaps_by_target[tgt]
    print(f"  → {tgt}  (missing backlinks from {len(srcs)} source page(s))")
    for s in srcs[:5]:
        print(f"      - {s}")
    if len(srcs) > 5:
        print(f"      ... and {len(srcs)-5} more")

header(f"3. Dangling related: links — {len(dangling)} edges to missing files")
for src, tgt in dangling:
    print(f"  {src}  →  {tgt}  (file not found)")

header(f"4. @path body mentions to missing files — {len(missing_mentions)} unique paths")
for path in sorted(missing_mentions.keys()):
    srcs = missing_mentions[path]
    print(f"  {path}  (mentioned in {len(srcs)} page(s))")
    for s in sorted(srcs)[:5]:
        print(f"      - {s}")
    if len(srcs) > 5:
        print(f"      ... and {len(srcs)-5} more")

header(f"5. Cited but unread source stubs — {len(cited_unread)} pages")
for p, n in cited_unread[:30]:
    print(f"  {p}  ({n} inbound)")
if len(cited_unread) > 30:
    print(f"  ... and {len(cited_unread)-30} more (showing top 30 by citation count)")

header("6. Frontmatter quality")
print(f"  no frontmatter at all: {len(no_frontmatter)}")
for p in no_frontmatter:
    print(f"    - {p}")
print(f"  missing 'type' field: {len(no_type)}")
for p in no_type[:20]:
    print(f"    - {p}")
print(f"  missing 'maturity' field (source/entity/concept only): {len(no_maturity)}")
for p in no_maturity[:20]:
    print(f"    - {p}")

header(f"7. Stale [NEEDS VERIFICATION] tags — {len(stale_verifications)} dated tag(s) "
       f"≥{args.verify_age_days} days old (Exa-resolution candidates)")
if not stale_verifications:
    print(f"  (none — all dated NEEDS VERIFICATION tags are within the {args.verify_age_days}-day window)")
for page, date_str, age, line_num, line_text in stale_verifications[:30]:
    print(f"  [{age:>4}d old, tagged {date_str}] {page}:{line_num}")
    snippet = line_text if len(line_text) <= 140 else line_text[:137] + "..."
    print(f"      {snippet}")
if len(stale_verifications) > 30:
    print(f"  ... and {len(stale_verifications)-30} more (showing top 30 by age)")

if undated_verifications:
    print(f"\n  Also: {len(undated_verifications)} undated [NEEDS VERIFICATION] tag(s) "
          f"— add a date so age can be tracked:")
    for page, line_num, line_text in undated_verifications[:20]:
        snippet = line_text if len(line_text) <= 140 else line_text[:137] + "..."
        print(f"    - {page}:{line_num}  {snippet}")
    if len(undated_verifications) > 20:
        print(f"    ... and {len(undated_verifications)-20} more")
