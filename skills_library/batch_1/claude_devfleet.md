---
title: claude-devfleet
url: https://skills.sh/affaan-m/everything-claude-code/claude-devfleet
---

# claude-devfleet

skills/affaan-m/everything-claude-code/claude-devfleet
claude-devfleet
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill claude-devfleet
SKILL.md
Claude DevFleet Multi-Agent Orchestration
When to Use

Use this skill when you need to dispatch multiple Claude Code agents to work on coding tasks in parallel. Each agent runs in an isolated git worktree with full tooling.

Requires a running Claude DevFleet instance connected via MCP:

claude mcp add devfleet --transport http http://localhost:18801/mcp

How It Works
User → "Build a REST API with auth and tests"
  ↓
plan_project(prompt) → project_id + mission DAG
  ↓
Show plan to user → get approval
  ↓
dispatch_mission(M1) → Agent 1 spawns in worktree
  ↓
M1 completes → auto-merge → auto-dispatch M2 (depends_on M1)
  ↓
M2 completes → auto-merge
  ↓
get_report(M2) → files_changed, what_done, errors, next_steps
  ↓
Report back to user

Tools
Tool	Purpose
plan_project(prompt)	AI breaks a description into a project with chained missions
create_project(name, path?, description?)	Create a project manually, returns project_id
create_mission(project_id, title, prompt, depends_on?, auto_dispatch?)	Add a mission. depends_on is a list of mission ID strings (e.g., ["abc-123"]). Set auto_dispatch=true to auto-start when deps are met.
dispatch_mission(mission_id, model?, max_turns?)	Start an agent on a mission
cancel_mission(mission_id)	Stop a running agent
wait_for_mission(mission_id, timeout_seconds?)	Block until a mission completes (see note below)
get_mission_status(mission_id)	Check mission progress without blocking
get_report(mission_id)	Read structured report (files changed, tested, errors, next steps)
get_dashboard()	System overview: running agents, stats, recent activity
list_projects()	Browse all projects
list_missions(project_id, status?)	List missions in a project

Note on wait_for_mission: This blocks the conversation for up to timeout_seconds (default 600). For long-running missions, prefer polling with get_mission_status every 30–60 seconds instead, so the user sees progress updates.

Workflow: Plan → Dispatch → Monitor → Report
Plan: Call plan_project(prompt="...") → returns project_id + list of missions with depends_on chains and auto_dispatch=true.
Show plan: Present mission titles, types, and dependency chain to the user.
Dispatch: Call dispatch_mission(mission_id=<first_mission_id>) on the root mission (empty depends_on). Remaining missions auto-dispatch as their dependencies complete (because plan_project sets auto_dispatch=true on them).
Monitor: Call get_mission_status(mission_id=...) or get_dashboard() to check progress.
Report: Call get_report(mission_id=...) when missions complete. Share highlights with the user.
Concurrency

DevFleet runs up to 3 concurrent agents by default (configurable via DEVFLEET_MAX_AGENTS). When all slots are full, missions with auto_dispatch=true queue in the mission watcher and dispatch automatically as slots free up. Check get_dashboard() for current slot usage.

Examples
Full auto: plan and launch
plan_project(prompt="...") → shows plan with missions and dependencies.
Dispatch the first mission (the one with empty depends_on).
Remaining missions auto-dispatch as dependencies resolve (they have auto_dispatch=true).
Report back with project ID and mission count so the user knows what was launched.
Poll with get_mission_status or get_dashboard() periodically until all missions reach a terminal state (completed, failed, or cancelled).
get_report(mission_id=...) for each terminal mission — summarize successes and call out failures with errors and next steps.
Manual: step-by-step control
create_project(name="My Project") → returns project_id.
create_mission(project_id=project_id, title="...", prompt="...", auto_dispatch=true) for the first (root) mission → capture root_mission_id. create_mission(project_id=project_id, title="...", prompt="...", auto_dispatch=true, depends_on=["<root_mission_id>"]) for each subsequent task.
dispatch_mission(mission_id=...) on the first mission to start the chain.
get_report(mission_id=...) when done.
Sequential with review
create_project(name="...") → get project_id.
create_mission(project_id=project_id, title="Implement feature", prompt="...") → get impl_mission_id.
dispatch_mission(mission_id=impl_mission_id), then poll with get_mission_status until complete.
get_report(mission_id=impl_mission_id) to review results.
create_mission(project_id=project_id, title="Review", prompt="...", depends_on=[impl_mission_id], auto_dispatch=true) — auto-starts since the dependency is already met.
Guidelines
Always confirm the plan with the user before dispatching, unless they said to go ahead.
Include mission titles and IDs when reporting status.
If a mission fails, read its report before retrying.
Check get_dashboard() for agent slot availability before bulk dispatching.
Mission dependencies form a DAG — do not create circular dependencies.
Each agent runs in an isolated git worktree and auto-merges on completion. If a merge conflict occurs, the changes remain on the agent's worktree branch for manual resolution.
When manually creating missions, always set auto_dispatch=true if you want them to trigger automatically when dependencies complete. Without this flag, missions stay in draft status.
Weekly Installs
2.3K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass