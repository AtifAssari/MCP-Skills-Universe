---
rating: ⭐⭐⭐
title: sc-worktree
url: https://skills.sh/tony363/superclaude/sc-worktree
---

# sc-worktree

skills/tony363/superclaude/sc-worktree
sc-worktree
Installation
$ npx skills add https://github.com/tony363/superclaude --skill sc-worktree
SKILL.md
Worktree Management Skill

Git worktree isolation for parallel agent development with simple, safe workflows.

Quick Start
# Create isolated worktree for a task
/sc:worktree create feature-auth

# List all active worktrees
/sc:worktree list

# Propose changes for human review
/sc:worktree propose feature-auth

# Clean up stale worktrees
/sc:worktree cleanup

Behavioral Flow
Create - Initialize isolated worktree with unique naming
Validate - Preflight checks (clean repo, no conflicts)
Assign - Spawn subagent with CWD set to worktree
Work - Agent operates in isolation, commits to branch
Propose - Push branch and create PR for human review
Cleanup - Remove merged/stale worktrees
Commands
Command	Purpose	Git Operations
create <task-id>	Create isolated worktree	git worktree add -b wt/<task>
list	Show all active worktrees	git worktree list
status <task-id>	Check worktree state	git status, git log
cleanup [--all]	Remove stale worktrees	git worktree remove, prune
propose <task-id>	Create PR for human review	git push, gh pr create
Flags
Flag	Type	Default	Description
--commits	bool	true	Agent commits directly to branch
--patches	bool	false	Agent produces patch files only
--run-tests	bool	false	Run tests before proposing
--force	bool	false	Override existing worktree/branch
--base	string	main	Base branch for worktree
Evidence Requirements

This skill does NOT require hard evidence. Worktree operations are self-documenting through:

Git worktree list output
Branch history
PR creation confirmation
Naming Convention

Worktrees use deterministic naming to prevent collisions:

Path:   .worktrees/<task-id>/
Branch: wt/<task-id>


Example:

Path:   .worktrees/feature-auth/
Branch: wt/feature-auth

Operations
Create Worktree
/sc:worktree create feature-auth

# Executes:
# 1. mkdir -p .worktrees
# 2. git worktree add -b wt/feature-auth .worktrees/feature-auth
# 3. Returns worktree path for subagent CWD

List Worktrees
/sc:worktree list

# Shows:
# - Active worktrees
# - Associated branches
# - Last commit info

Check Status
/sc:worktree status feature-auth

# Shows:
# - Uncommitted changes
# - Commits ahead of base branch
# - Conflict warnings

Propose Changes
/sc:worktree propose feature-auth

# Executes:
# 1. git push -u origin wt/feature-auth
# 2. gh pr create --title "feat: feature-auth" --body "..."
# 3. Returns PR URL for human review

Cleanup Worktrees
/sc:worktree cleanup          # Remove merged worktrees
/sc:worktree cleanup --all    # Remove ALL worktrees
/sc:worktree cleanup feature-auth  # Remove specific worktree

# Executes:
# 1. git worktree remove .worktrees/<task-id>
# 2. git branch -d wt/<task-id>
# 3. git worktree prune

Subagent Integration

When spawning a subagent to work in a worktree:

# 1. Create worktree
/sc:worktree create feature-auth

# 2. Spawn subagent with CWD
Task(
    prompt="Implement JWT authentication",
    subagent_type="general-purpose",
    # CWD implicitly set to .worktrees/feature-auth/
)

# 3. Agent works in isolation
# - All file operations scoped to worktree
# - Commits go to wt/feature-auth branch

# 4. Propose for review
/sc:worktree propose feature-auth

Preflight Checks

Before creating a worktree, the skill validates:

Repository State

Repo is clean OR --force flag provided
Main branch is up to date

Branch Availability

wt/<task-id> branch doesn't exist OR explicit reuse
No conflicting remote branch

Path Availability

.worktrees/<task-id> doesn't exist OR --force flag
Conflict Detection

Before proposing, the skill checks for conflicts:

# Fetch latest changes
git fetch origin main

# Check if worktree is behind
git merge-base --is-ancestor origin/main HEAD

# Warn but don't block if behind
# Human reviewer handles merge strategy

Examples
Single Agent Workflow
# Create worktree
/sc:worktree create add-logging

# Work in worktree (agent operates here)
# ... agent makes changes, commits ...

# Propose changes
/sc:worktree propose add-logging

# Human reviews PR, merges

# Cleanup
/sc:worktree cleanup add-logging

Parallel Multi-Agent Workflow
# Orchestrator creates multiple worktrees
/sc:worktree create feature-auth
/sc:worktree create feature-logging
/sc:worktree create feature-metrics

# Spawn agents in parallel (each with own worktree)
# Agent A -> .worktrees/feature-auth/
# Agent B -> .worktrees/feature-logging/
# Agent C -> .worktrees/feature-metrics/

# Propose all changes
/sc:worktree propose feature-auth
/sc:worktree propose feature-logging
/sc:worktree propose feature-metrics

# Human reviews 3 PRs, merges sequentially

# Cleanup all
/sc:worktree cleanup --all

Patch Mode (No Direct Commits)
/sc:worktree create refactor-api --patches

# Agent produces .patch files instead of commits
# Orchestrator reviews patches before applying

/sc:worktree propose refactor-api  # Creates PR from patches

MCP Integration
PAL MCP (Validation & Review)
Tool	When to Use	Purpose
mcp__pal__precommit	Before propose	Validate changes in worktree
mcp__pal__codereview	Before propose	Review worktree changes
mcp__pal__consensus	Conflict resolution	Multi-model merge strategy
PAL Usage Patterns
# Validate worktree changes before proposing
mcp__pal__precommit(
    path=".worktrees/feature-auth",
    step="Validating worktree changes",
    findings="Security, test coverage, completeness",
    compare_to="main"
)

# Review worktree branch
mcp__pal__codereview(
    review_type="full",
    step="Reviewing feature-auth worktree",
    relevant_files=[".worktrees/feature-auth/src/auth.py"]
)

Rube MCP (Automation & Notifications)
Tool	When to Use	Purpose
mcp__rube__RUBE_SEARCH_TOOLS	GitHub integration	Find PR tools
mcp__rube__RUBE_MULTI_EXECUTE_TOOL	Propose command	Create PR, notify team
Rube Usage Patterns
# Create PR and notify team
mcp__rube__RUBE_MULTI_EXECUTE_TOOL(tools=[
    {"tool_slug": "GITHUB_CREATE_PULL_REQUEST", "arguments": {
        "repo": "myapp",
        "title": "feat: feature-auth from worktree",
        "body": "## Worktree: feature-auth\nCreated via /sc:worktree",
        "base": "main",
        "head": "wt/feature-auth"
    }},
    {"tool_slug": "SLACK_SEND_MESSAGE", "arguments": {
        "channel": "#pull-requests",
        "text": "New PR from worktree: wt/feature-auth"
    }}
])

Flags (Extended)
Flag	Type	Default	Description
--pal-review	bool	false	Use PAL codereview before propose
--create-pr	bool	true	Create GitHub PR via Rube
--notify	string	-	Notify via Rube (slack, teams)
--draft	bool	false	Create draft PR
Tool Coordination
Bash - Git worktree commands, directory operations
Read - Check worktree status and logs
Task - Spawn subagents with worktree CWD
PAL MCP - Pre-propose validation, code review
Rube MCP - PR creation, team notifications
Safety Guarantees
Isolation - Each worktree has separate working directory
No Auto-Merge - Human review required for all merges
Unique Naming - Deterministic paths prevent collisions
Crash-Safe - cleanup --all removes stale worktrees
Warning-Only Conflicts - Conflicts warn but don't block
Limitations
No automatic quality scoring (use CI/tests)
No lease tracking (periodic cleanup instead)
No sophisticated conflict resolution (human review)
No auto-merge to main (PR-based workflow)
Weekly Installs
27
Repository
tony363/superclaude
GitHub Stars
17
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass