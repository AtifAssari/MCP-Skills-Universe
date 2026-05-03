---
rating: ⭐⭐⭐
title: vibe-kanban
url: https://skills.sh/abpai/skills/vibe-kanban
---

# vibe-kanban

skills/abpai/skills/vibe-kanban
vibe-kanban
Installation
$ npx skills add https://github.com/abpai/skills --skill vibe-kanban
SKILL.md
Vibe Kanban — Task Board Skill

Vibe Kanban (VK) is the shared task board for all agents and the single source of truth for current work.

When to Use

Use this skill when you need to:

Check what you should work on next
Claim, create, update, or complete tasks
Run a heartbeat task check
Scan for @your-agent-id mentions in task descriptions
Generate a daily standup summary
Access
CLI (primary)

The vk binary is a standalone CLI generated from the VK MCP server schema. It lives at vibe-kanban/scripts/vk and requires bun at runtime.

vk <command> [--flag value ...]
vk --help                         # list all commands
vk <command> --help               # help for a specific command

MCP tools (alternative)

If the vibe_kanban MCP server is configured in your Claude Code session, you can call tools directly (e.g. list_projects, list_tasks) without the CLI.

Tool Reference
Task management
vk list-projects
vk list-tasks --project-id <ID>
vk list-tasks --project-id <ID> --status todo
vk list-tasks --project-id <ID> --status inprogress --limit 10
vk create-task --project-id <ID> --title "[agent-id] Task description"
vk create-task --project-id <ID> --title "Title" --description "Details"
vk get-task --task-id <ID>
vk update-task --task-id <ID> --status inprogress
vk update-task --task-id <ID> --status done
vk delete-task --task-id <ID>

Repository management
vk list-repos --project-id <ID>
vk get-repo --repo-id <ID>
vk update-setup-script --repo-id <ID> --script '#!/bin/bash\n...'
vk update-cleanup-script --repo-id <ID> --script '...'
vk update-dev-server-script --repo-id <ID> --script '...'

Workspace sessions
vk start-workspace-session --task-id <ID> --executor CLAUDE_CODE --repos <repo-id1>,<repo-id2>


Supported executors: CLAUDE_CODE, AMP, GEMINI, CODEX, OPENCODE, CURSOR_AGENT, QWEN_CODE, COPILOT, DROID.

Task Statuses
Status	Meaning
todo	Not started
inprogress	Actively being worked on
inreview	Work done, awaiting review
done	Completed
cancelled	No longer needed
Task Assignment Convention

Assign tasks with a title prefix: [agent-id].

Examples:

[main] Configure daily standup cron
[andrej] Document all ~/Projects repos
[fury] Research LLM fine-tuning approaches

When checking assignments, filter by your own prefix first.

Heartbeat Workflow
List todo tasks: vk list-tasks --project-id <ID> --status todo
Filter tasks with your [agent-id] prefix
Pick the highest-priority task (first valid match is acceptable)
Claim it: vk update-task --task-id <ID> --status inprogress
Execute the task work
Mark complete: vk update-task --task-id <ID> --status done
If no matching task exists, reply HEARTBEAT_OK
Scan descriptions for @your-agent-id mentions and respond as needed
Standup Summary Workflow
List all tasks across all statuses
Group by status: done (last 24h), inprogress, inreview, todo
Format as:
📋 Daily Standup — YYYY-MM-DD

✅ Completed:
- [agent] Task description

🔍 In Review:
- [agent] Task description

🔄 In Progress:
- [agent] Task description

📌 To Do:
- [agent] Task description

Tips
Keep titles concise and descriptive
Always include [agent-id] when creating tasks
Update task status promptly so board state stays reliable
Use descriptions for details, links, and handoff context
Pass empty string to --script to clear a script
Use -o json or --output json for machine-readable output (formats: text, markdown, json, raw)
Weekly Installs
18
Repository
abpai/skills
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass