---
name: merge
description: DM only. Review proposed companion notes and merge accepted changes into the DM-owned originals.
argument-hint: [note name or "all"]
disable-model-invocation: true
---
**First check `.claude/role` is `dm`.** If not, stop and explain that only the DM can merge.

Delegate gathering to `dm-liaison`, then walk the DM through each companion with `status: proposed` (or the one named in `$ARGUMENTS`):

1. Show: original, companion path, author, `based-on` date, and whether the original changed since.
2. For each item (addition / correction / question) ask: **accept**, **edit**, **reject**, or **skip** (use AskUserQuestion, batched sensibly).
3. Apply accepted items to the original, integrated naturally into its structure and voice — not appended as a quote dump. Keep `owner: dm`. Do not mention the player in canon text unless asked.
4. Answer "Questions for DM" by adding the DM's reply to the companion under `## DM response`.
5. Update the companion frontmatter: `status: merged` (all handled), `rejected`, or leave `proposed` with remaining items. Add `merged-on: YYYY-MM-DD`.
6. Summarize what changed. Do not commit unless asked.
