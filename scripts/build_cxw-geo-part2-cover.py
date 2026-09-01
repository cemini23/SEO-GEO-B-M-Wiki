#!/usr/bin/env python3
"""Part 2 X Article cover: OGE/flow panel + computed Jul 17 CXW options book (1792x716)."""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import date

from PIL import Image, ImageDraw, ImageFont

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "briefs" / "cxw-geo-part2-cover-1792x716.png"

W, H = 1792, 716
LEFT_W = int(W * 0.58)
RIGHT_W = W - LEFT_W
PAD = 44

# Operator book (Jul 17/2026 CXW calls) — matches Robinhood screenshots
LEGS = (
    ("CXW $35 Call", "7/17", 37, 35.0),
    ("CXW $33 Call", "7/17", 100, 33.0),
    ("CXW $30 Call", "7/17", 1227, 30.0),
)

# Jul 1, 2026 EOD — yfinance last marks (run script to refresh)
DEFAULT_MARKS = {
    35.0: 0.55,
    33.0: 0.90,
    30.0: 2.42,
}
STOCK_EOD = 31.01
AS_OF = date(2026, 7, 1)
PRIOR_VALUE = 283_501.0  # prior Robinhood screenshot for day P&L
COST_BASIS = PRIOR_VALUE / (1 + 2.1613)  # implied from +216% at prior mark


@dataclass
class Portfolio:
    stock: float
    as_of: date
    marks: dict[float, float]
    value: float
    day_pnl: float
    day_pct: float
    total_pnl: float
    total_pct: float


def fetch_portfolio() -> Portfolio:
    try:
        import yfinance as yf

        t = yf.Ticker("CXW")
        hist = t.history(period="5d")
        stock = float(hist["Close"].iloc[-1])
        as_of = hist.index[-1].date()
        chain = t.option_chain("2026-07-17").calls
        marks = {}
        for *_, strike in LEGS:
            row = chain[chain["strike"] == strike].iloc[0]
            marks[strike] = float(row["lastPrice"])
    except Exception:
        stock = STOCK_EOD
        as_of = AS_OF
        marks = DEFAULT_MARKS

    value = sum(qty * marks[strike] * 100 for _, _, qty, strike in LEGS)
    day_pnl = value - PRIOR_VALUE
    day_pct = day_pnl / PRIOR_VALUE * 100
    total_pnl = value - COST_BASIS
    total_pct = total_pnl / COST_BASIS * 100
    return Portfolio(stock, as_of, marks, value, day_pnl, day_pct, total_pnl, total_pct)


def load_font(size: int, bold: bool = False):
    for path in (
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ):
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                pass
    return ImageFont.load_default()


def fmt_money(n: float, signed: bool = False) -> str:
    if signed:
        sign = "+" if n >= 0 else "-"
        return f"{sign}${abs(n):,.2f}"
    return f"${n:,.2f}"


def build_left() -> Image.Image:
    left = Image.new("RGB", (LEFT_W, H), (15, 17, 23))
    d = ImageDraw.Draw(left)
    title, head, body, small = load_font(40, True), load_font(26, True), load_font(22), load_font(18)
    accent, muted, white, gold, red = (34, 197, 94), (156, 163, 175), (248, 250, 252), (250, 204, 21), (248, 113, 113)

    y = PAD
    d.text((PAD, y), "$CXW / $GEO — Part 2", font=title, fill=white)
    y += 48
    d.text((PAD, y), "OGE disclosure · Jul 1 flow", font=head, fill=accent)
    y += 52

    rows = [
        ("OGE filing released", "Jun 30, 2026", white),
        ("GEO holding band", "$50k – $100k", gold),
        ("CXW holding band", "$15k – $50k", gold),
        ("First buy both names", "Jan 30, 2025", white),
        ("Jul 1 GEO call premium", "~$4.1M", accent),
        ("Jul 1 CXW call premium", "~$1.8M", accent),
        ("Still no sale 8-K", "Through Jul 1", red),
    ]
    for label, val, color in rows:
        d.text((PAD, y), label, font=small, fill=muted)
        d.text((PAD, y + 22), val, font=body, fill=color)
        y += 54

    d.line([(PAD, H - PAD - 36), (LEFT_W - PAD, H - PAD - 36)], fill=(55, 65, 81), width=2)
    d.text((PAD, H - PAD - 28), "NBC led GEO · CXW in same PDF · Sources in Article", font=small, fill=muted)
    return left


def build_right(p: Portfolio) -> Image.Image:
    right = Image.new("RGB", (RIGHT_W, H), (9, 9, 11))
    d = ImageDraw.Draw(right)

    title_f, head_f, row_f, small_f, price_f = load_font(34, True), load_font(22), load_font(20), load_font(17), load_font(22, True)
    white, muted, green, card_bg, border = (17, 17, 17), (115, 115, 115), (0, 200, 5), (255, 255, 255), (230, 230, 230)

    mx, my, mw, mh = 28, 36, RIGHT_W - 56, H - 72
    d.rounded_rectangle([mx, my, mx + mw, my + mh], radius=20, fill=card_bg, outline=border, width=2)

    x = mx + 28
    y = my + 24
    d.text((x, y), "Options", font=title_f, fill=(0, 0, 0))
    y += 46
    d.text((x, y), f"Jul 17 CXW book · EOD {p.as_of.isoformat()}", font=small_f, fill=muted)
    y += 28
    d.text((x, y), "Value", font=row_f, fill=(0, 0, 0))
    d.text((x + 120, y), fmt_money(p.value), font=head_f, fill=(0, 0, 0))
    y += 34
    d.text((x, y), "Today's return", font=row_f, fill=(0, 0, 0))
    d.text((x + 120, y), f"{fmt_money(p.day_pnl, True)} ({p.day_pct:+.2f}%)", font=row_f, fill=green)
    y += 30
    d.text((x, y), "Total return", font=row_f, fill=(0, 0, 0))
    d.text((x + 120, y), f"{fmt_money(p.total_pnl, True)} ({p.total_pct:+.1f}%)", font=row_f, fill=green)
    y += 36
    d.line([(x, y), (mx + mw - 28, y)], fill=border, width=1)
    y += 18

    for name, exp, qty, strike in LEGS:
        mark = p.marks[strike]
        d.text((x, y), name, font=row_f, fill=(0, 0, 0))
        y += 22
        d.text((x, y), f"{exp} · {qty:,} contracts", font=small_f, fill=muted)
        d.text((mx + mw - 28 - 70, y - 22), f"${mark:.2f}", font=price_f, fill=(0, 0, 0))
        y += 30

    d.text((x, my + mh - 28), f"CXW ${p.stock:.2f} · marks = contract last", font=small_f, fill=muted)
    return right


def main() -> None:
    p = fetch_portfolio()
    out = Image.new("RGB", (W, H), (0, 0, 0))
    out.paste(build_left(), (0, 0))
    out.paste(build_right(p), (LEFT_W, 0))
    ImageDraw.Draw(out).line([(LEFT_W, 0), (LEFT_W, H)], fill=(55, 65, 81), width=4)
    os.makedirs(OUT_PATH.parent, exist_ok=True)
    out.save(OUT_PATH, "PNG", optimize=True)
    print(f"Saved {OUT_PATH}")
    print(f"Portfolio EOD {p.as_of}: {fmt_money(p.value)} | day {p.day_pct:+.2f}% | total {p.total_pct:+.1f}%")
    for _, exp, qty, strike in LEGS:
        print(f"  {strike}C x{qty}: ${p.marks[strike]:.2f}")


if __name__ == "__main__":
    main()
