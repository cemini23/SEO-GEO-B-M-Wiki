# Posts.docx style pass — X long-form research ritual

**Trigger:** OSINT ingest step **4c** in `CLAUDE.md` — runs when `Posts.docx` or `trading-posts-compilation-*` is ingested in OSINT workspace. Canonical ingest stays OSINT; updates land here (seo-wiki).

## Inputs

- OSINT source page: `@osint-wiki/sources/trading-posts-compilation-*.md` (read from sibling repo)
- Raw post text (from docx or operator paste)
- `@seo-wiki/concepts/x-account-voice-and-format.md` (update exemplar table + snippets)

## Steps

1. **Identify long-forms** — Articles or 10+ tweet threads marketed as guides. Skip single-tweet reply fodder unless hook is exceptional.

2. **Per long-form, capture:**

   | Field | Values |
   |-------|--------|
   | Author | @handle |
   | Hook type | pain / contrarian / number-led / story |
   | Framework | e.g. 3 zones, 5 workflows |
   | Paragraph discipline | good / broken (line-per-sentence) |
   | AI tells present? | em dashes, "game-changer", emoji, stacked questions |
   | CTA | follow / fork / reply prompt / none |
   | Steal for our Articles? | yes/no + which element |

3. **Update** `@seo-wiki/concepts/x-account-voice-and-format.md`:
   - Style exemplars table (new row or amend author row)
   - `## Snippets` if one quotable rhythm line worth keeping
   - `## Dead Ends` if we tried a pattern and it failed on our account

4. **Article queue** — if a post overlaps our lane (wiki, agents, Polymarket), add beat to `@seo-wiki/concepts/x-article-3-notes.md` or create `x-article-N-notes.md`. Do **not** draft full Article unless operator asks.

5. **Formatting flag** — if stored text has hard line breaks every sentence, note: "needs paragraph merge before X Article paste."

6. **Log** — append one line to `@seo-wiki/wiki/log.md`: `style-pass | Posts.docx K## | N long-forms | authors: …`

## Output to operator (when asked or at session end)

Short summary:

- Top 1–2 posts worth replying to today (with suggested reply angle)
- One style takeaway for next Article
- Any formatting warning for our own publishing

## Cyril checklist (quick)

- [ ] Opens with recognizable failure?
- [ ] Named framework with counts?
- [ ] Deliverable artifact (tree, prompt, checklist)?
- [ ] Single metric?
- [ ] Avoids hyperbole stack?
- [ ] Paragraphs multi-sentence?
