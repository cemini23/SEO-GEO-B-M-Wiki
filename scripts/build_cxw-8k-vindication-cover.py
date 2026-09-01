#!/usr/bin/env python3
"""8-K vindication X Article cover — deal stats only, no position screenshot (1792x716)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "briefs" / "cxw-8k-vindication-cover-1792x716.png"

W, H = 1792, 716
PAD = 56


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def fetch_cxw_close() -> str | None:
    try:
        import yfinance as yf

        hist = yf.Ticker("CXW").history(period="5d")
        if hist.empty:
            return None
        return f"${hist['Close'].iloc[-1]:.2f}"
    except Exception:
        return None


def draw_card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    price: str,
    beds: str,
    *,
    accent: tuple[int, int, int],
) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=20, fill=(22, 27, 38), outline=(55, 65, 81), width=2)
    draw.text((x0 + 28, y0 + 24), title, font=load_font(26, bold=True), fill=(248, 250, 252))
    draw.text((x0 + 28, y0 + 72), price, font=load_font(44, bold=True), fill=accent)
    draw.text((x0 + 28, y1 - 52), beds, font=load_font(22), fill=(156, 163, 175))


def main() -> None:
    img = Image.new("RGB", (W, H), (11, 14, 20))
    draw = ImageDraw.Draw(img)

    white = (248, 250, 252)
    muted = (156, 163, 175)
    green = (34, 197, 94)
    gold = (250, 204, 21)
    blue = (96, 165, 250)

    title_f = load_font(52, bold=True)
    sub_f = load_font(30)
    label_f = load_font(24)
    stat_f = load_font(38, bold=True)
    small_f = load_font(20)

    draw.text((PAD, PAD), "CXW 8-K VINDICATION", font=title_f, fill=white)
    draw.text((PAD, PAD + 64), "ICE bought two California detention facilities", font=sub_f, fill=muted)

    y = PAD + 130
    draw.rounded_rectangle((PAD, y, W - PAD, y + 88), radius=16, fill=(17, 24, 39), outline=(37, 99, 235), width=2)
    draw.text((PAD + 28, y + 18), "Gross sale price", font=label_f, fill=muted)
    draw.text((PAD + 28, y + 46), "$1.5B", font=stat_f, fill=gold)
    draw.text((W - PAD - 420, y + 28), "Closed Jul 2  ·  Announced Jul 6", font=label_f, fill=white)

    card_y = y + 120
    card_h = 220
    gap = 32
    card_w = (W - 2 * PAD - gap) // 2
    draw_card(
        draw,
        (PAD, card_y, PAD + card_w, card_y + card_h),
        "California City",
        "$732.6M",
        "2,560 beds",
        accent=green,
    )
    draw_card(
        draw,
        (PAD + card_w + gap, card_y, W - PAD, card_y + card_h),
        "Otay Mesa",
        "$739.2M",
        "1,994 beds",
        accent=blue,
    )

    footer_y = card_y + card_h + 36
    metrics = [
        ("Net proceeds", "~$1.1B"),
        ("Taxes + expenses", "~$0.4B"),
        ("Blended $/bed", "~$329k"),
        ("Chase leg", "$GEO"),
    ]
    col_w = (W - 2 * PAD) // len(metrics)
    for i, (label, value) in enumerate(metrics):
        x = PAD + i * col_w
        draw.text((x, footer_y), label, font=small_f, fill=muted)
        draw.text((x, footer_y + 28), value, font=load_font(28, bold=True), fill=white)

    cxw = fetch_cxw_close()
    bottom = H - PAD - 28
    if cxw:
        draw.text((PAD, bottom), f"CXW last close {cxw}  ·  Long CXW calls", font=small_f, fill=muted)
    else:
        draw.text((PAD, bottom), "Long CXW calls  ·  Research, not financial advice", font=small_f, fill=muted)

    draw.text((W - PAD - 260, bottom), "Form 8-K filed Jul 6, 2026", font=small_f, fill=muted)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH, "PNG", optimize=True)
    print(f"Saved {OUT_PATH} ({W}x{H})")


if __name__ == "__main__":
    main()
