---
name: recap
description: Turn raw session notes into a session recap note and propose new NPCs, places and open threads.
argument-hint: <raw notes or path to a file> [session number]
---
1. Read the raw notes in `$ARGUMENTS` (text or file path).
2. Write `Sessions/Session <n> — YYYY-MM-DD.md` from `_templates/session.md` (`owner: player`). Faithful to the source; no embellishment.
3. List entities mentioned that have no note yet. Offer to create stubs (`/character-concept`, `World/`, `Lore/`) — ask before creating.
4. For facts that touch DM-owned notes, offer `/propose` entries.
5. Link everything with wikilinks.
