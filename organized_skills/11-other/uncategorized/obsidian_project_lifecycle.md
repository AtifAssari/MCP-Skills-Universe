---
rating: ⭐⭐
title: obsidian-project-lifecycle
url: https://skills.sh/galaxy-dawn/claude-scholar/obsidian-project-lifecycle
---

# obsidian-project-lifecycle

skills/galaxy-dawn/claude-scholar/obsidian-project-lifecycle
obsidian-project-lifecycle
Installation
$ npx skills add https://github.com/galaxy-dawn/claude-scholar --skill obsidian-project-lifecycle
SKILL.md
Obsidian Project Lifecycle

Use the shared helper script for deterministic lifecycle operations.

Role in the workflow

This is a supporting skill under obsidian-project-memory.

Use it for project-level state changes and, when needed, note-level removal or rename flows.

Project-level commands
python3 ../obsidian-project-memory/scripts/project_kb.py lifecycle --cwd "$PWD" --mode detach
python3 ../obsidian-project-memory/scripts/project_kb.py lifecycle --cwd "$PWD" --mode archive
python3 ../obsidian-project-memory/scripts/project_kb.py lifecycle --cwd "$PWD" --mode purge

Note-level command
python3 ../obsidian-project-memory/scripts/project_kb.py note-lifecycle --cwd "$PWD" --mode archive --note "Results/Old-Result.md"
python3 ../obsidian-project-memory/scripts/project_kb.py note-lifecycle --cwd "$PWD" --mode purge --note "Results/Old-Result.md"
python3 ../obsidian-project-memory/scripts/project_kb.py note-lifecycle --cwd "$PWD" --mode rename --note "Experiments/Old-Name.md" --dest "Experiments/New-Name.md"

Policy
Detach: stop syncing, keep vault content.
Archive: default for “remove this project's knowledge”; move the project to Archive/ and disable syncing.
Purge: only when the user explicitly requests permanent deletion.
Rename / move: treat as update plus link repair, not delete plus create.

Always summarize what was removed, what was preserved, and whether auto-sync remains enabled.

Weekly Installs
45
Repository
galaxy-dawn/cla…-scholar
GitHub Stars
3.5K
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass