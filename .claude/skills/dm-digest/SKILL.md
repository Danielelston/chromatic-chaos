---
name: dm-digest
description: Build a merge-ready digest of all proposed companion notes to send to the DM. Excludes secret notes.
---
Delegate to `dm-liaison`. Find every `*(companion).md` with `status: proposed` and not `secret: true`. Write `Inbox/DM Digest — YYYY-MM-DD.md` (`owner: player`) grouped by original note: original link, `based-on` date, flag if the original changed since, then additions / corrections / questions. Give the user the path; they send or commit it.
