#!/usr/bin/env python3
"""Build X Article cover: bed-math panel + CXW options position screenshot (1792x716, 5:2)."""

from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
POSITION_SHOT = Path(
    os.environ.get(
        "CXW_COVER_POSITION_IMAGE",
        Path.home()
        / ".cursor/projects/Users-claudiobarone-Projects-SEO-GEO-B-M-Business/assets/image-4650d2e4-1f54-440e-a12f-f04e39b4b0bf.png",
    )
)
OUT_PATH = ROOT / "briefs" / "cxw-geo-x-article-cover-1792x716.png"

W, H = 1792, 716
LEFT_W = int(W * 0.58)
RIGHT_W = W - LEFT_W
PAD = 48


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                pass
    return ImageFont.load_default()


def build_left_panel() -> Image.Image:
    left = Image.new("RGB", (LEFT_W, H), (15, 17, 23))
    draw = ImageDraw.Draw(left)

    title_f = load_font(42, bold=True)
    head_f = load_font(28, bold=True)
    body_f = load_font(24)
    small_f = load_font(20)

    accent = (34, 197, 94)
    muted = (156, 163, 175)
    white = (248, 250, 252)
    red = (248, 113, 113)
    gold = (250, 204, 21)

    y = PAD
    draw.text((PAD, y), "$CXW / $GEO", font=title_f, fill=white)
    y += 52
    draw.text((PAD, y), "Plan B: Buy the beds", font=head_f, fill=accent)
    y += 56

    for label, value, color in [
        ("Federal bed target", "100,000", white),
        ("Warehouse conversions operating", "0 / 11", red),
        ("Plan A spend (stalled)", "$1.1B", muted),
        ("Idle beds (CXW + GEO)", "20,000+", accent),
        ("Benchmark PT (Jun 26)", "$28 → $36", gold),
        ("2-sale scenario", "80% · ~$680M after-tax", gold),
        ("Next public test", "Aug 5–10 earnings", white),
    ]:
        draw.text((PAD, y), label, font=small_f, fill=muted)
        draw.text((PAD, y + 26), value, font=body_f, fill=color)
        y += 62

    draw.line([(PAD, H - PAD - 40), (LEFT_W - PAD, H - PAD - 40)], fill=(55, 65, 81), width=2)
    draw.text((PAD, H - PAD - 32), "Sources: Axios · Benchmark · Secure America Act", font=small_f, fill=muted)
    return left


def build_right_panel() -> Image.Image:
    if not POSITION_SHOT.exists():
        raise FileNotFoundError(f"Position screenshot not found: {POSITION_SHOT}")

    pos = Image.open(POSITION_SHOT).convert("RGB")
    rp = 24
    max_w, max_h = RIGHT_W - 2 * rp, H - 2 * rp
    scale = min(max_w / pos.width, max_h / pos.height)
    nw, nh = int(pos.width * scale), int(pos.height * scale)
    pos = pos.resize((nw, nh), Image.Resampling.LANCZOS)

    right = Image.new("RGB", (RIGHT_W, H), (9, 9, 11))
    ox, oy = (RIGHT_W - nw) // 2, (H - nh) // 2
    right.paste(pos, (ox, oy))

    fd = ImageDraw.Draw(right)
    fd.text(((RIGHT_W - 380) // 2, 12), "Author position · Jul 17 CXW calls", font=load_font(20), fill=(156, 163, 175))
    fd.rounded_rectangle([ox - 8, oy - 8, ox + nw + 8, oy + nh + 8], radius=24, outline=(55, 65, 81), width=3)
    return right


def main() -> None:
    out = Image.new("RGB", (W, H), (0, 0, 0))
    out.paste(build_left_panel(), (0, 0))
    out.paste(build_right_panel(), (LEFT_W, 0))
    ImageDraw.Draw(out).line([(LEFT_W, 0), (LEFT_W, H)], fill=(55, 65, 81), width=4)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    out.save(OUT_PATH, "PNG", optimize=True)
    print(f"Saved {OUT_PATH} ({W}x{H})")


if __name__ == "__main__":
    main()
