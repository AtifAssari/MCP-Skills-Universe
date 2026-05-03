---
title: cli-anything-seaclip
url: https://skills.sh/hkuds/cli-anything/cli-anything-seaclip
---

# cli-anything-seaclip

skills/hkuds/cli-anything/cli-anything-seaclip
cli-anything-seaclip
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-seaclip
SKILL.md
cli-anything-seaclip

A stateless command-line interface for SeaClip-Lite project management. Communicates via HTTP API and direct SQLite reads. No local state or session.

Installation
pip install -e .


Prerequisites:

Python 3.10+
SeaClip-Lite backend running at localhost:5200
Usage
Basic Commands
# Show help
cli-anything-seaclip --help

# Start interactive REPL mode
cli-anything-seaclip

# Run with JSON output (for agent consumption)
cli-anything-seaclip --json server health
cli-anything-seaclip --json issue list
cli-anything-seaclip --json agent list

REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

cli-anything-seaclip
# Enter commands interactively with tab-completion and history

Command Groups
Issue

Issue management commands.

Command	Description
list	List issues (--status, --priority, --search, --limit)
create	Create a new issue (--title, --description, --priority)
move	Move issue to column (ISSUE_ID --column COL)
status	Update issue status (ISSUE_ID --set STATUS)
delete	Delete an issue (ISSUE_ID)
Agent

Pipeline agent commands.

Command	Description
list	List all pipeline agents
Pipeline

Pipeline control commands.

Command	Description
start	Start pipeline (--issue UUID --mode auto/manual)
status	Get pipeline status (--issue UUID)
resume	Resume paused pipeline (--issue UUID)
stop	Stop running pipeline (--issue UUID)
Scheduler

Schedule configuration commands.

Command	Description
list	List all schedule configs
add	Add schedule (--name, --cron, --repo)
sync	Trigger sync (SCHEDULE_ID)
Activity

Activity feed commands.

Command	Description
list	Recent activity (--limit N)
Server

Server utility commands.

Command	Description
health	Check backend health
Output Formats

All commands support dual output modes:

Human-readable (default): Tables, colors, formatted text
Machine-readable (--json flag): Structured JSON for agent consumption
# Human output
cli-anything-seaclip issue list

# JSON output for agents
cli-anything-seaclip --json issue list

For AI Agents

When using this CLI programmatically:

Always use --json flag for parseable output
Check return codes - 0 for success, non-zero for errors
Parse stderr for error messages on failure
Error responses include {"error": "message"} in JSON mode
Version

1.0.0

Weekly Installs
86
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass