#!/usr/bin/env python3
"""GuruWatcher Outlier / X Article hero — 1792x716 (5:2)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "briefs" / "guruwatcher-outlier-x-article-hero-1792x716.png"

W, H = 1792, 716
PAD = 56


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def rounded_rect(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    radius: int,
    fill: tuple[int, int, int],
    outline: tuple[int, int, int] | None = None,
    width: int = 2,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_envelope(draw: ImageDraw.ImageDraw, cx: int, cy: int, size: int = 56) -> None:
    """Simple envelope icon centered at (cx, cy)."""
    ink = (31, 41, 55)
    w, h = size, int(size * 0.72)
    x0, y0 = cx - w // 2, cy - h // 2
    x1, y1 = x0 + w, y0 + h
    draw.rounded_rectangle((x0, y0, x1, y1), radius=6, outline=ink, width=3)
    # flap
    draw.line([(x0 + 2, y0 + 4), (cx, y0 + h // 2 + 2)], fill=ink, width=3)
    draw.line([(x1 - 2, y0 + 4), (cx, y0 + h // 2 + 2)], fill=ink, width=3)


def draw_discord_mark(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float = 1.0) -> None:
    """Minimal Discord-ish gamepad mark (white on dark card)."""
    s = scale
    white = (248, 250, 252)
    # body oval-ish rounded rect
    draw.rounded_rectangle(
        (x, y, x + int(44 * s), y + int(32 * s)),
        radius=int(12 * s),
        fill=white,
    )
    # cut eye holes (dark)
    dark = (31, 41, 55)
    r = int(5 * s)
    draw.ellipse((x + int(10 * s), y + int(10 * s), x + int(10 * s) + 2 * r, y + int(10 * s) + 2 * r), fill=dark)
    draw.ellipse((x + int(26 * s), y + int(10 * s), x + int(26 * s) + 2 * r, y + int(10 * s) + 2 * r), fill=dark)


def main() -> None:
    bg = (248, 247, 244)
    white = (255, 255, 255)
    ink = (17, 24, 39)
    muted = (107, 114, 128)
    card_outline = (229, 231, 235)
    chip_bg = (220, 252, 231)
    chip_ink = (22, 101, 52)
    discord_card = (31, 41, 55)

    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)

    title_f = load_font(44, bold=True)
    panel_f = load_font(30, bold=True)
    sub_f = load_font(22)
    chip_f = load_font(20, bold=True)
    footer_f = load_font(20)

    title = "Newsletter level → Discord (alert-only)"
    tw = draw.textlength(title, font=title_f)
    draw.text(((W - tw) / 2, 48), title, font=title_f, fill=ink)

    # Three panels across the wide 5:2 canvas
    panel_y0 = 150
    panel_h = 360
    gap = 48
    arrow_w = 56
    usable = W - 2 * PAD - 2 * arrow_w
    panel_w = usable // 3

    left = (PAD, panel_y0, PAD + panel_w, panel_y0 + panel_h)
    mid = (
        PAD + panel_w + arrow_w,
        panel_y0,
        PAD + 2 * panel_w + arrow_w,
        panel_y0 + panel_h,
    )
    right = (
        PAD + 2 * panel_w + 2 * arrow_w,
        panel_y0,
        PAD + 3 * panel_w + 2 * arrow_w,
        panel_y0 + panel_h,
    )

    # Left: Macro Charts issue
    rounded_rect(draw, left, 24, white, card_outline, 2)
    lx0, ly0, lx1, ly1 = left
    lcx = (lx0 + lx1) // 2
    draw_envelope(draw, lcx, ly0 + 110, size=72)
    label = "Macro Charts issue"
    lw = draw.textlength(label, font=panel_f)
    draw.text((lcx - lw / 2, ly0 + 175), label, font=panel_f, fill=ink)

    chip = "VIX >20"
    cw = draw.textlength(chip, font=chip_f) + 36
    ch = 40
    cx0 = int(lcx - cw / 2)
    cy0 = ly0 + 240
    rounded_rect(draw, (cx0, cy0, cx0 + int(cw), cy0 + ch), 20, chip_bg, None, 0)
    draw.text((cx0 + 18, cy0 + 8), chip, font=chip_f, fill=chip_ink)

    # Arrow 1
    a1x0 = lx1 + 10
    a1x1 = mid[0] - 10
    ay = (panel_y0 + panel_y0 + panel_h) // 2
    draw.line([(a1x0, ay), (a1x1 - 8, ay)], fill=ink, width=4)
    draw.polygon([(a1x1, ay), (a1x1 - 16, ay - 10), (a1x1 - 16, ay + 10)], fill=ink)

    # Mid: claim ledger
    rounded_rect(draw, mid, 24, white, card_outline, 2)
    mx0, my0, mx1, my1 = mid
    mcx = (mx0 + mx1) // 2
    m1 = "claim ledger"
    m1w = draw.textlength(m1, font=panel_f)
    draw.text((mcx - m1w / 2, my0 + 130), m1, font=panel_f, fill=ink)
    m2 = "newest article wins"
    m2w = draw.textlength(m2, font=sub_f)
    draw.text((mcx - m2w / 2, my0 + 180), m2, font=sub_f, fill=muted)

    # Arrow 2
    a2x0 = mx1 + 10
    a2x1 = right[0] - 10
    draw.line([(a2x0, ay), (a2x1 - 8, ay)], fill=ink, width=4)
    draw.polygon([(a2x1, ay), (a2x1 - 16, ay - 10), (a2x1 - 16, ay + 10)], fill=ink)

    # Right: Discord alert card
    # Outer light panel so "no orders" sits on the cream canvas like the reference
    rx0, ry0, rx1, ry1 = right
    # Discord card centered in right column
    card_w, card_h = panel_w - 48, 120
    c0 = rx0 + (panel_w - card_w) // 2
    c1 = ry0 + 110
    rounded_rect(draw, (c0, c1, c0 + card_w, c1 + card_h), 18, discord_card, None, 0)
    draw_discord_mark(draw, c0 + 22, c1 + 44, scale=1.0)
    alert = "VIX gt 20 sustained"
    draw.text((c0 + 80, c1 + 42), alert, font=load_font(26, bold=True), fill=(248, 250, 252))

    no_orders = "no orders"
    nw = draw.textlength(no_orders, font=sub_f)
    draw.text(((rx0 + rx1) / 2 - nw / 2, c1 + card_h + 28), no_orders, font=sub_f, fill=ink)

    # Footer
    footer = "fluid mind · verbatim guards · 15m poll"
    fw = draw.textlength(footer, font=footer_f)
    draw.text(((W - fw) / 2, H - PAD - 8), footer, font=footer_f, fill=muted)

    img.save(OUT_PATH, "PNG", optimize=True)
    print(f"Wrote {OUT_PATH} ({W}x{H})")


if __name__ == "__main__":
    main()
