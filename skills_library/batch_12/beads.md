---
title: beads
url: https://skills.sh/johnlindquist/claude/beads
---

# beads

skills/johnlindquist/claude/beads
beads
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill beads
SKILL.md
Beads Issue Tracker

Git-backed issue tracking with dependency awareness. Perfect for agent task management.

Prerequisites

Install beads:

# Install via cargo or download binary
cargo install beads
# Or download from releases


Initialize in a project:

bd init

CLI Reference
View Ready Work
# Get issues with no blockers
bd ready --json

# Filter by assignee
bd ready --assignee username --json

# Filter by label
bd ready --label "urgent" --json

# Limit results
bd ready --limit 5 --json

Create Issues
# Basic task
bd create "Task title" --json

# With details
bd create "Task title" -d "Description" -t task -p 2 --json

# As subtask of epic
bd create "Subtask" --parent epic-123 --force --json

# With dependencies
bd create "Task" --deps "other-issue-id" --json

# Quick mode (less output)
bd create "Task" -q --json

Issue Types
bug - Bug reports
feature - New features
task - General tasks
epic - Parent containers
chore - Maintenance work
Priority Levels
0 - Critical
1 - High
2 - Normal (default)
3 - Low
4 - Backlog
Update Issues
# Change status
bd update issue-id -s in_progress --json

# Add notes
bd update issue-id --notes "Progress update" --json

# Change priority
bd update issue-id -p 1 --json

# Add labels
bd update issue-id --add-label "urgent" --json

Close Issues
# Close with reason
bd close issue-id -r "Completed successfully" --json

List Issues
# All open issues
bd list --status open --json

# Filter by type
bd list --type bug --json

# Filter by assignee
bd list --assignee "username" --json

# Filter by label
bd list --label "backend" --json

# Filter by priority
bd list --priority 1 --json

Show Issue Details
bd show issue-id --json

Dependencies
# Add dependency (issue-a depends on issue-b)
bd dep add issue-a issue-b

# Dependency types: blocks, related, parent-child, discovered-from
bd dep add issue-a issue-b -t blocks

Sync with Git
# Sync issues to git remote
bd sync

Hygiene Commands
# Find duplicate issues
bd duplicates --dry-run

# Auto-merge duplicates
bd duplicates --auto-merge

# Find stale issues (no activity)
bd stale --days 14 --json

# Cleanup old closed issues
bd cleanup --dry-run
bd cleanup -f

Install Git Hooks
# Auto-sync on commit
bd hooks install

System Info
# Check version
bd --version

# Project info
bd info --json

Workflow Patterns
Session Start
# See what's ready to work on
bd ready --json

Working on a Task
# Start working
bd update task-id -s in_progress --json

# Add progress notes
bd update task-id --notes "Halfway done" --json

# Complete
bd close task-id -r "Implemented and tested" --json

Epic Planning
# Create epic
bd create "User Authentication" -t epic --json

# Add subtasks
bd create "Design auth flow" --parent auth-epic --force --json
bd create "Implement login" --parent auth-epic --force --json
bd create "Add tests" --parent auth-epic --force --json

# Add dependencies between subtasks
bd dep add implement-id design-id -t blocks
bd dep add tests-id implement-id -t blocks

End of Session
# Sync to git
bd sync

Worktree Mode

When using git worktrees, disable the daemon:

export BEADS_NO_DAEMON=1
# Or per-command
bd --no-daemon ready --json

Best Practices
Always use --json for parseable output
Use bd ready at session start to see unblocked work
Add dependencies to express task relationships
Use epics for grouping related tasks
Run bd sync before ending sessions
Install hooks for automatic sync: bd hooks install
Weekly Installs
63
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass