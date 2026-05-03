---
title: wt
url: https://skills.sh/llama-farm/llamafarm/wt
---

# wt

skills/llama-farm/llamafarm/wt
wt
Installation
$ npx skills add https://github.com/llama-farm/llamafarm --skill wt
SKILL.md
wt - Worktree Manager Skill

Manages isolated LlamaFarm development environments using git worktrees. Each worktree has its own services, ports, and data directories - enabling parallel agent sessions without conflicts.

Full Documentation

For complete documentation, architecture details, and advanced usage: @scripts/wt/README.md

Quick Reference
Task	Command
Create worktree and start services	wt create feat/my-feature
Create and cd into worktree	wt create --go feat/my-feature
List all worktrees with status	wt list
Check service health	wt status or wt health
Start/stop services	wt start / wt stop
View service logs	wt logs [server|rag|runtime|designer|all]
Delete worktree	wt delete <name>
Switch to worktree	wt switch <name>
Open Designer in browser	wt open
Diagnose issues	wt doctor
Clean orphaned data	wt gc
When to Use wt

Use wt when:

Starting isolated work on a feature/task that needs running services
Running parallel coding sessions (multiple agents or terminals)
Testing changes without affecting the main development environment
Avoiding port conflicts between concurrent LlamaFarm instances
Common Workflows
Starting a New Task
# Create isolated environment with services running
wt create --go feat/my-task

# Work in the worktree...
# Services are already running on auto-assigned ports

# Check status anytime
wt status

# View logs if needed
wt logs server

Checking What's Running
# List all worktrees with their port assignments
wt list

# Example output:
# NAME              STATUS    SERVER   DESIGNER  RUNTIME
# feat-my-task      running   8150     5150      11150
# fix-bug           stopped   8234     5234      11234

Cleaning Up
# Stop services and remove a worktree
wt delete feat-my-task

# Remove data for worktrees that no longer exist
wt gc

# Remove worktrees for branches merged to main
wt prune

Troubleshooting
# Diagnose common issues (ports, stale PIDs, missing tools)
wt doctor

# Restart stuck services
wt stop && wt start

# Force delete if normal delete fails
wt delete my-worktree --force

Service URLs

Each worktree gets unique ports. Check URLs with:

wt url
# Outputs:
#   Server:   http://localhost:8150
#   Designer: http://localhost:5150
#   Runtime:  http://localhost:11150


If the Caddy proxy is running, use port-free URLs:

http://server.feat-my-task.localhost
http://designer.feat-my-task.localhost

Key Environment Details
Worktrees location: ~/worktrees/llamafarm/
Data directories: ~/.llamafarm/worktrees/<name>/
Port allocation: Deterministic hash of worktree name (14345+offset, 5000+offset, 11000+offset)
Logs: ~/.llamafarm/worktrees/<name>/logs/
Notes for the Agent
Always use wt create --go when setting up a new task environment - it handles everything (branch, deps, build, services)
Check wt list first before creating a new worktree to see what already exists
Use wt status to verify services are healthy before running tests or making API calls
Run wt doctor when encountering unexplained service issues
Clean up with wt delete when a task is complete to free resources
Weekly Installs
30
Repository
llama-farm/llamafarm
GitHub Stars
822
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass