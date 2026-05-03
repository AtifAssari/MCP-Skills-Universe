---
title: cli-anything-notebooklm
url: https://skills.sh/hkuds/cli-anything/cli-anything-notebooklm
---

# cli-anything-notebooklm

skills/hkuds/cli-anything/cli-anything-notebooklm
cli-anything-notebooklm
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-notebooklm
SKILL.md
cli-anything-notebooklm

Experimental NotebookLM harness for CLI-Anything.

Installation

This package is intended to be installed from the harness directory:

cd notebooklm/agent-harness
python3 -m pip install -e .


Install the upstream NotebookLM CLI if needed:

python3 -m pip install --user 'notebooklm-py[browser]'
python3 -m playwright install chromium

Requirements
notebooklm command installed locally
Valid local NotebookLM login session
Usage
Basic Commands
# Show help
cli-anything-notebooklm --help

# Start with a notebook context
cli-anything-notebooklm --notebook nb_123 source list

# Prefer JSON for agent use
cli-anything-notebooklm --json notebook list

Command Groups
Group	Purpose
auth	login and auth validation
notebook	notebook list, create, summary
source	source listing and URL add
chat	ask questions and inspect history
artifact	list and generate artifacts
download	fetch generated outputs
share	inspect sharing state
Agent Workflow
Check auth with cli-anything-notebooklm auth status
Discover notebook IDs with cli-anything-notebooklm --json notebook list
Use explicit --notebook for follow-up commands
Prefer --json only where the upstream notebooklm command supports it
Agent Guidance
Prefer explicit notebook IDs with --notebook.
Use --json for machine-readable output only on commands that support it upstream.
Treat this harness as experimental and unofficial.
Do not expose auth files or cookies in logs.
NotebookLM is a Google product; this harness is unofficial and not affiliated with Google.
References
CLI-Anything: https://github.com/HKUDS/CLI-Anything
CLI-Anything HARNESS.md: https://github.com/HKUDS/CLI-Anything/blob/main/cli-anything-plugin/HARNESS.md
notebooklm-py: https://github.com/teng-lin/notebooklm-py
Google NotebookLM help: https://support.google.com/notebooklm/answer/16206563
Weekly Installs
113
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn