---
title: commit-changes
url: https://skills.sh/tenzir/skills/commit-changes
---

# commit-changes

skills/tenzir/skills/commit-changes
commit-changes
Installation
$ npx skills add https://github.com/tenzir/skills --skill commit-changes
SKILL.md
Commit Changes

Commit changes as clean, reviewable snapshots.

Workflow
Read git status and the relevant diffs before deciding how many commits to make.
Split orthogonal work into separate logical units. If a file mixes unrelated edits, stage only the hunks for the current commit.
Run the relevant checks before committing. For Python projects, delegate to the follow-python-conventions skill. If you skip a check, say so.
For each commit:
Stage only the relevant hunks.
Read the staged diff before writing the message.
Write the commit message from what is actually staged, including the AI assistance trailer.
Create the commit with a real multiline message, using separate -m arguments for subject, body, and final trailer block.
Do not put literal \n escapes in a single -m string.
Amend immediately if the final message reads awkwardly.
Weekly Installs
40
Repository
tenzir/skills
GitHub Stars
1
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass