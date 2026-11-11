---
name: note
description: Quick-capture a note, fact, or message into the campaign Inbox. Use when the user says "note:", "remember", "jot down", or passes something to store.
argument-hint: <text to capture>
---
Capture `$ARGUMENTS` via the `scribe` agent (or directly if trivial).

1. Create `Inbox/YYYY-MM-DD — <short title>.md` from `_templates/player.md` (`type: player`, `owner: player`).
2. Body = the user's text, lightly cleaned but not rewritten. Add `[[wikilinks]]` to existing notes it clearly mentions (search first; don't link to nonexistent notes).
3. If it concerns a DM-owned note, add a line `Relates to: [[Note]]` and suggest `/propose`.
4. Confirm with the file path in one line.
