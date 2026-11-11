---
name: propose
description: Propose a change or addition to a DM-owned note by creating/updating its companion note. Never edits the original.
argument-hint: <note name> <change or info to add>
---
Parse `$ARGUMENTS` into a target note and a proposed change.

1. Locate the target (Glob/Grep). If ambiguous, ask. If it's `owner: player`, just say it can be edited directly and offer to do so.
2. Companion path: same folder, `<Note> (companion).md`. Create from `_templates/companion.md` if missing (set `companion-of`, `based-on` = original's last-modified date, `author` = git user.name if available). If it exists, append to it; reset `status: proposed`.
3. Put the content under `## Additions`, `## Corrections` or `## Questions for DM`. Keep entries short, dated, and attributable. Never copy the original wholesale.
4. Report the companion path and a one-line summary.
