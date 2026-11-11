---
name: recall
description: Answer a question about the Chromatic Chaos campaign (world, lore, characters, sessions) using only the notes, with wikilink citations. Use for "what do we know about X", "who is Y", "where did Z happen".
argument-hint: <question>
---
Answer `$ARGUMENTS` from the notes. Delegate the search to the `lore-keeper` agent.

- Cite every claim with a `[[wikilink]]`. Mention if a source is a companion (unmerged player proposal) vs DM canon.
- Flag conflicts between notes.
- If the notes don't contain the answer, say "Not in the notes" and suggest what to ask the DM. Never invent canon.
- Exclude nothing the user owns, but do not reveal `secret: true` notes if the output is meant to be shared.
