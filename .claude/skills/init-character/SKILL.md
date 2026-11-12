---
name: init-character
description: Scaffold a new PC or NPC note from the template.
argument-hint: <name> [pc|npc] [details]
---
Create `Characters/<Name>.md` from `_templates/character-concept.md`. Fill in any provided details; leave the rest blank. Set `owner: player` (or `dm` only if the DM role is active and requested). Refuse to overwrite an existing note; check for near-duplicate names first and ask.
