# Chromatic Chaos

Campaign notes for a **D&D 5.5e** game set in **Akroma**, a world where nine nations each carry a color. This repo is an [Obsidian](https://obsidian.md) vault with [Claude Code](https://claude.com/claude-code) skills and agents for querying it, capturing notes, and passing changes between players and the DM.

Start with [`Chromatic Chaos — Index.md`](<Chromatic Chaos — Index.md>).

## Layout

| Folder | Contents |
|---|---|
| `World/` | Nations, places, maps |
| `Lore/` | Gods and Mordants, history, customs |
| `Characters/` | PCs and NPCs |
| `Player Notes/` | Player theories, goals, to-dos |
| `Sessions/` | Session recaps |
| `Inbox/` | Quick captures, sorted later |
| `Dropzone/` | Drop raw files here (handouts, PDFs, maps), then run `/ingest` |
| `Sources/`, `Assets/` | Archived originals after ingest |
| `_templates/` | Note templates |

## Getting started

1. Clone the repo and open the folder in Obsidian (optional) and/or Claude Code.
2. Create your role file (gitignored):
   ```bash
   echo player > .claude/role   # or: echo dm > .claude/role
   ```
3. Run `claude` in the repo root. `CLAUDE.md`, the skills, agents, and hook load automatically.

## Ownership rules

Every note has `owner:` in its frontmatter.

- **`owner: dm`** is DM canon. Players never edit these directly; a hook blocks it.
- **`owner: player`** notes belong to their author and can be edited freely.
- To change a DM note, players create a **companion note** (`<Note> (companion).md`, with `companion-of`, `status: proposed`). The DM later folds it in with `/merge`.
- `secret: true` marks private player notes, which are never included in digests.

## Skills

| Skill | Who | What it does |
|---|---|---|
| `/recall <question>` | all | Answer from the notes, with citations |
| `/who <name>` | all | Character card for an NPC or PC |
| `/threads` | all | Open quests and unanswered questions |
| `/note <text>` | all | Quick capture into `Inbox/` |
| `/recap <notes>` | all | Turn raw notes into a session recap |
| `/character-concept [name]` | all | Brainstorm and/or interview to build a PC/NPC concept note |
| `/propose <note> <change>` | players | Propose a change via a companion note |
| `/dm-digest` | players | Collect proposed companions into a DM digest |
| `/triage` | all | File `Inbox/` items |
| `/ingest` | all | Process `Dropzone/` files into notes |
| `/merge` | DM only | Review and merge proposed companions into canon |

## Agents

`lore-keeper` (read-only research), `scribe` (the only writer), `ingester` (Dropzone extraction), `continuity-checker` (audit), `dm-liaison` (digest and merge workflow).

## Workflow

```
player: /note, /propose  ->  companion notes (status: proposed)
player: /dm-digest       ->  digest for the DM
DM:     /merge           ->  canon updated, companion marked merged
anyone: drop files in Dropzone/  ->  /ingest  ->  notes + archived originals
```

Commit and push as usual; companions and their `status` changes keep a reviewable history.

## Notes

- The hook blocks Edit/Write on DM notes but does not stop shell commands. This is a collaboration guard, not a security boundary.
- Content is game material provided by the DM and is shared here with their knowledge.
