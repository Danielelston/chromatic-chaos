---
type: index
campaign: Chromatic Chaos
system: D&D 5.5e (2024)
---
# Chromatic Chaos — Index

Player-side notes for the campaign. Entry point for querying and capturing info.

## Folders
- `World/` — places, factions, geography, maps
- `Lore/` — history, myths, rules of the setting
- `Characters/` — PCs and NPCs
- `Player Notes/` — my own theories, goals, to-dos
- `Sessions/` — session recaps
- `Dropzone/` — drop raw files here (DM handouts, PDFs, maps); run `/ingest`
- `Sources/` / `Assets/` — archived originals after ingest
- `Inbox/` — quick captures, unsorted, to be filed later

## Ownership convention
- **DM-owned** notes (`owner: dm` in frontmatter) are **never edited directly**.
- Changes/additions go in a **companion note** named `<Note> (companion).md`, with `companion-of: "[[<Note>]]"` in frontmatter, living next to the original.
- Companions are collected for the DM to merge; once merged, set `status: merged`.
- Notes I author use `owner: player`, and can be edited freely.

## Quick capture
Drop anything into `Inbox/` as `YYYY-MM-DD — <short title>.md`. Triage into the folders above later.

## Frontmatter template
```yaml
---
type: world | lore | character | player | session
owner: dm | player
companion-of: "[[Original Note]]"   # companions only
status: draft | proposed | merged   # companions only
---
```

## Start here (ingested 2026-11-11)
- [[Campaign Pitch]]
- [[Nations & Culture]] — nations, places, culture
- [[Gods & Mordants]] — pantheon
- [[Akroma Map]]
