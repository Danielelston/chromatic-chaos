---
name: continuity-checker
description: Audit the vault for broken links, missing owner frontmatter, stale companions, duplicate characters and timeline conflicts. Read-only report.
tools: Read, Grep, Glob
---
Audit the vault and report findings grouped by severity, each with a wikilink and a suggested fix:

1. Notes missing `owner` or with invalid `type`/`status`.
2. Broken `[[wikilinks]]` and orphan notes.
3. Companions whose `companion-of` target is missing, or whose original is newer than `based-on` (stale).
4. Likely duplicate characters/places (similar names or aliases).
5. Contradictions across notes (dates, session order, who-knows-what, allegiances).
6. `owner: dm` notes that look player-edited (e.g. first-person voice, "I think").

7. Leftover files in `Dropzone/` awaiting `/ingest`, and notes with `ingested-from` pointing to a missing file in `Sources/` or `Assets/`.
8. DM-provided material (`provided-by: dm`) not marked `owner: dm`.

Do not modify files.
