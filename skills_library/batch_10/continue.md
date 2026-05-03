---
title: continue
url: https://skills.sh/bfly123/claude_code_bridge/continue
---

# continue

skills/bfly123/claude_code_bridge/continue
continue
Installation
$ npx skills add https://github.com/bfly123/claude_code_bridge --skill continue
SKILL.md
Continue (Attach Latest History)
Overview

Find the newest Markdown in ./.ccb/history/ (or legacy ./.ccb_config/history/) and reply with an @file reference so Claude loads it.

Workflow
Locate the newest .md under the current project's history folder.
If none exists, report that no history file was found.
Reply with a single line @<path> and nothing else.
Execution (MANDATORY)
latest="$(ls -t "$PWD"/.ccb/history/*.md 2>/dev/null | head -n 1)"
if [[ -z "$latest" ]]; then
  latest="$(ls -t "$PWD"/.ccb_config/history/*.md 2>/dev/null | head -n 1)"
fi
if [[ -z "$latest" ]]; then
  echo "No history file found in ./.ccb/history."
  exit 0
fi
printf '@%s\n' "$latest"

Output Rules
When a history file exists: output only @<path> on a single line.
When none exists: output the error message and stop.
Examples
/continue -> @/home/bfly/workspace/hippocampus/.ccb/history/claude-20260208-225221-9f236442.md
Weekly Installs
9
Repository
bfly123/claude_…e_bridge
GitHub Stars
2.2K
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass