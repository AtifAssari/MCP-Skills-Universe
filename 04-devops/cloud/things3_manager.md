---
title: things3-manager
url: https://skills.sh/eugenepyvovarov/things3-agent-skill/things3-manager
---

# things3-manager

skills/eugenepyvovarov/things3-agent-skill/things3-manager
things3-manager
Installation
$ npx skills add https://github.com/eugenepyvovarov/things3-agent-skill --skill things3-manager
SKILL.md
Things 3 Manager (CLI)
Quick start
Ensure Things 3 is installed and opened at least once.
In Things → Settings → General: enable “Enable Things URLs”.
Run the CLI (auto-bootstraps .skills-data/things3-manager/venv and installs deps on first run):
bash .codex/skills/things3-manager/scripts/things --help
bash .codex/skills/things3-manager/scripts/things inbox
bash .codex/skills/things3-manager/scripts/things search "weekly review"
bash .codex/skills/things3-manager/scripts/things add-todo --title "Book flights" --when today --tag travel --checklist "passport" --checklist "charger"
Operating rules (for Codex)
Prefer read-only commands first (inbox, today, search, projects, areas, tags) to discover UUIDs and current state.
Before any write command (add-todo, add-project, update-todo, update-project), summarize the exact changes and confirm with the user.
If the user provides a project/area/heading by name, resolve it by listing (projects/areas/headings) before writing.
Local data and env
Store all mutable state under <project_root>/.skills-data//.
Keep config and registries in .skills-data// (for example: config.json, .json).
Use .skills-data//.env for SKILL_ROOT, SKILL_DATA_DIR, and any per-skill env keys.
Install local tools into .skills-data//bin and prepend it to PATH when needed.
Install dependencies under .skills-data//venv:
Python: .skills-data//venv/python
Node: .skills-data//venv/node_modules
Go: .skills-data//venv/go (modcache, gocache)
PHP: .skills-data//venv/php (cache, vendor)
Write logs/cache/tmp under .skills-data//logs, .skills-data//cache, .skills-data//tmp.
Keep automation in /scripts and read SKILL_DATA_DIR (default to <project_root>/.skills-data//).
Do not write outside and <project_root>/.skills-data// unless the user requests it.
Commands (CLI)
Lists:
inbox, today, upcoming, anytime, someday, logbook, trash, recent
Browsing:
projects, areas, tags, headings, todos, tagged-items
Search:
search, search-advanced
Writes (via Things URL scheme):
add-todo, add-project, update-todo, update-project
Open in Things:
show, search-items
Attribution
CLI implementation is based on things_server.py, url_scheme.py, and formatters.py from https://github.com/hald/things-mcp.
Weekly Installs
15
Repository
eugenepyvovarov…nt-skill
GitHub Stars
16
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass