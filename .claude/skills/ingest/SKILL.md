---
name: ingest
description: Process files in Dropzone/ (DM handouts, PDFs, maps, images, pasted docs): extract them into properly-owned campaign notes, archive the originals, and clear the dropzone.
argument-hint: [file name, or blank for everything]
---
Delegate the heavy reading to the `ingester` agent. Work in two phases.

**Phase 1 — plan (no writes yet).**
1. List `Dropzone/` (or the file in `$ARGUMENTS`). Ask once, if unknown: *who provided this batch — the DM or a player/me?* Provenance decides ownership:
   - From the DM → new notes get `owner: dm`, `provided-by: dm`.
   - From a player/me → `owner: player`.
2. For each file, propose: extracted notes (title, folder, type), split plan (one note per god/nation/town/NPC when the source is a list of entities, plus a hub note for the source), where the original goes (`Sources/` for documents, `Assets/` for images/media), and any existing notes it overlaps.
3. Show it as a table and wait for confirmation.

**Phase 2 — apply.**
- Create notes from `_templates/`, every one with frontmatter `owner`, `type`, `ingested-from: "Sources/<file>"`, `ingested-on: YYYY-MM-DD`, `provided-by`. Faithful extraction: keep the source's wording and facts; don't embellish or merge in outside lore; keep system notes (e.g. "PF2E Domains") as written.
- Link entities with `[[wikilinks]]`. Images: create a note in `World/` embedding `![[file.png]]` with a description of what is visible (towns, regions, labels) — only what is actually shown.
- **Never overwrite or edit an existing `owner: dm` note.** If the drop is a newer version of one, save the new source, tell the user, and create a companion (`/propose` procedure) or leave it for the DM role's `/merge`.
- Move the original out of `Dropzone/` (`mv`, never delete) into `Sources/` or `Assets/`. Large binaries (>10 MB): mention Git LFS / downscaling to the user; don't alter the original.
- Add new notes to the Index if it lists them. Report: notes created (paths), originals moved, anything skipped or needing a decision.
