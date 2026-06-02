# Lessons

A running log of lessons learned while managing this workspace. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

---

## [2026-06-02] YouTube @Cemini23 — first analytics export (launch week)

**Source:** Studio export `Content 2026-05-05_2026-06-02 Cemini23.zip` → `briefs/youtube-cemini23/analytics-2026-06-02/` (gitignored). Wiki: `@entities/platforms/youtube.md`, `@sources/youtube-cemini23-launch-analytics-2026-06-02.md`.

### What happened

- Channel went live **2026-05-30**; **~91% of first-week views** landed that single day (X launch spike, then tail).
- **Shorts = volume; long = depth.** 91% of views were Shorts, but **77% of watch time** was long-form (9 min wiki explainer + 88s trailer).
- **Don’t judge Shorts by impression CTR.** Shorts showed ~0% CTR and tiny impression counts — feed traffic, not browse thumbnails.
- **Concrete Short titles win.** “3 things wikilint catches…” (696 views) beat generic launch copy; WC trailer (22 views) lost to WC Short (200) on reach.
- **Long-form needs 16:9.** Vertical + &lt;3 min → YouTube treats as Short even via “Upload video.” Re-render long cuts as **1920×1080** (`render_promo.py` `LANDSCAPE`).
- **Audio sync for slide Shorts:** fixed `sec_per_slide` (3s) desynced NotebookLM voiceover; use **per-slide TTS** (`gambling-devfun-june3/render_promo.py`) or `build_short.py` auto-scales duration when `--audio` is set.

### Playbook going forward

1. Every topic: **Short (9:16) + long (16:9)** — Short points to long in description + pinned comment.
2. Short titles: **tool + outcome** (“3 things X catches”), not “launching June N.”
3. Trailer = support/pin, not primary discovery bet.
4. Pin the **long** wiki-style video on the channel during launch weeks.
5. Next Studio export: traffic sources, retention curve on best long, end-screen clicks.

---

(no earlier entries — workspace scaffolded 2026-05-07)
