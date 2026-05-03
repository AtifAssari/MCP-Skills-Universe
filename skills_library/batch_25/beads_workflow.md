---
title: beads-workflow
url: https://skills.sh/nguyenhuuca/assessment/beads-workflow
---

# beads-workflow

skills/nguyenhuuca/assessment/beads-workflow
beads-workflow
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill beads-workflow
SKILL.md
Beads Workflow
Overview

Beads is an AI-native issue tracker designed for agent workflows. Issues live in your repo, sync via git, and require no web UI.

MCP Tools

GitHub (remote collaboration):

Link Beads issues to GitHub PRs
Create GitHub issues for team visibility
Track PR status for blocked work
Auto-close Beads issues when PRs merge
Core Commands
Issue Management
# Create a new issue
bd create "Title" -t feature -p 2

# List open issues
bd list --status open

# View issue details
bd show <issue-id>

# Update issue
bd update <id> --status in_progress
bd update <id> --assignee claude

# Close issue
bd close <id> --reason "Completed: description"

Finding Work
# Get unblocked issues (no dependencies blocking)
bd ready --sort hybrid

# Filter by priority
bd list --priority 1 --status open

# Filter by labels
bd list --label backend

Dependencies
# Add dependency (X blocks Y)
bd dep add <blocking-id> <blocked-id> --type blocks

# View dependency tree
bd dep tree <id>

# Remove dependency
bd dep rm <blocking-id> <blocked-id>

Syncing
# Sync with git remote
bd sync

# Force flush to JSONL
bd flush

GitHub Integration Patterns
Linking Issues to PRs
Create Beads issue: bd create "Feature X"
Implement and create PR via GitHub MCP
Reference Beads ID in PR description
When PR merges, close Beads issue: bd close <id>
Syncing Status
# Check if related PR is merged (use GitHub MCP)
# Then update Beads status accordingly
bd update <id> --status done

Team Visibility

For issues that need team visibility:

Create in Beads for local tracking
Use GitHub MCP to create corresponding GitHub issue
Link both in descriptions
Keep Beads as source of truth for agents
Workflow Patterns
Starting a Session
Check ready work: bd ready --sort hybrid
Check GitHub: Use GitHub MCP to verify no blocking PRs
Claim an issue: bd update <id> --status in_progress
Review dependencies: bd dep tree <id>
Begin implementation
During Implementation
Track sub-tasks: bd create "Sub-task" --parent <id>
Add blockers: bd dep add <new-blocker> <id> --type blocks
Update progress: bd comment <id> "Progress update"
Create PR: Use GitHub MCP when ready
Completing Work
Verify completion: All acceptance criteria met
PR status: Use GitHub MCP to check CI/review status
Close issue: bd close <id> --reason "Implemented X, PR #123"
Sync: bd sync
Check next: bd ready
Multi-Agent Coordination
# See who's working on what
bd list --status in_progress --json | jq '.[] | {id, title, assignee}'

# Avoid conflicts - check before claiming
bd show <id>  # Check assignee field

# Hand off work
bd update <id> --assignee other-agent
bd comment <id> "Handoff: context and next steps"

Issue Types
Type	When to Use
feature	New functionality
bug	Defect fixes
task	General work items
spike	Research/investigation
chore	Maintenance, cleanup
Priority Levels
Priority	Meaning
0	Critical - Drop everything
1	High - Next up
2	Medium - Normal flow
3	Low - When time permits
4	Backlog - Future consideration
Status Flow
open -> in_progress -> done
         |-> blocked -> in_progress

Best Practices
One issue per logical unit: Don't combine unrelated work
Clear titles: Should explain what, not how
Use dependencies: Makes ready work visible
Sync frequently: Keep other agents informed
Close promptly: Don't leave stale in_progress issues
Link to GitHub: Create GitHub issues for team-visible work
Integration with Swarm

When working in a swarm:

Check active work: bd list --status in_progress
Claim before editing: Update status before touching code
Document blockers: Create issues for discovered blockers
Handoff cleanly: Update assignee and add context
Sync before ending: bd sync to share state
Create PRs: Use GitHub MCP for review visibility
Troubleshooting
# Check daemon health
bd daemons health

# View daemon logs
bd daemons logs

# Force reimport from JSONL
bd import --force

# Check for conflicts
bd sync --dry-run

Weekly Installs
10
Repository
nguyenhuuca/assessment
GitHub Stars
24
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn