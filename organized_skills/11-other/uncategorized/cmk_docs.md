---
rating: ⭐⭐
title: cmk:docs
url: https://skills.sh/commandosslabs/ai-devkit/cmk:docs
---

# cmk:docs

skills/commandosslabs/ai-devkit/cmk:docs
cmk:docs
Installation
$ npx skills add https://github.com/commandosslabs/ai-devkit --skill cmk:docs
SKILL.md
Docs
Intents
Set up the docs structure for this project

Check if our docs structure matches the latest devkit

We added a new service — update the docs scaffold

Are we missing any docs directories?

References

Read references/scaffold-manifest.md for the complete file manifest and exact content for each file.

Modes

Init (default) — First-time scaffolding. Create missing directories, navigation files, and templates. Never overwrite existing files. Report divergences.

Update — Re-sync after devkit changes. Create newly added files, compare AGENTS.md/README.md against manifest and report divergences, add new templates without overwriting customized ones. Confirm with user before modifying existing files.

Verify — Dry-run. Report gaps and divergences without creating or modifying anything.

Workflow
Determine mode from user intent.
Scan target repository for existing /docs structure.
Compare against references/scaffold-manifest.md.
Execute based on mode (init → create missing; update → create missing + offer fixes; verify → report only).
Create directories before contents, in order: docs/, templates/, adrs/, specs/, rules/, rules/common/, knowledge/, guides/, reference/.
For each directory, create AGENTS.md first, then README.md.
Report: created, skipped, diverged, updated.
Output
Every directory has both AGENTS.md and README.md
Root AGENTS.md → docs/AGENTS.md → docs/README.md chain is intact
Templates directory contains all baseline templates
Init mode never modifies existing files
Update mode confirms before modifying
Verify mode makes no file changes
Weekly Installs
12
Repository
commandosslabs/ai-devkit
GitHub Stars
3
First Seen
Mar 9, 2026