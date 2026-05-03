---
title: git-worktree
url: https://skills.sh/everyinc/compound-engineering-plugin/git-worktree
---

# git-worktree

skills/everyinc/compound-engineering-plugin/git-worktree
git-worktree
Installation
$ npx skills add https://github.com/everyinc/compound-engineering-plugin --skill git-worktree
SKILL.md
Git Worktree Manager

This skill provides a unified interface for managing Git worktrees across your development workflow. Whether you're reviewing PRs in isolation or working on features in parallel, this skill handles all the complexity.

What This Skill Does
Create worktrees from main branch with clear branch names
List worktrees with current status
Switch between worktrees for parallel work
Clean up completed worktrees automatically
Interactive confirmations at each step
Automatic .gitignore management for worktree directory
Automatic .env file copying from main repo to new worktrees
Automatic dev tool trusting for mise and direnv configs with review-safe guardrails
CRITICAL: Always Use the Manager Script

NEVER call git worktree add directly. Always use the worktree-manager.sh script.

The script handles critical setup that raw git commands don't:

Copies .env, .env.local, .env.test, etc. from main repo
Trusts dev tool configs with branch-aware safety rules:
mise: auto-trust only when unchanged from a trusted baseline branch
direnv: auto-allow only for trusted base branches; review worktrees stay manual
Ensures .worktrees is in .gitignore
Creates consistent directory structure
# ✅ CORRECT - Always use the script
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh create feature-name

# ❌ WRONG - Never do this directly
git worktree add .worktrees/feature-name -b feature-name main

When to Use This Skill

Use this skill in these scenarios:

Code Review (/ce:review): If NOT already on the target branch (PR branch or requested branch), offer worktree for isolated review
Feature Work (/ce:work): Always ask if user wants parallel worktree or live branch work
Parallel Development: When working on multiple features simultaneously
Cleanup: After completing work in a worktree
How to Use
In Claude Code Workflows

The skill is automatically called from /ce:review and /ce:work commands:

# For review: offers worktree if not on PR branch
# For work: always asks - new branch or worktree?

Manual Usage

You can also invoke the skill directly from bash:

# Create a new worktree (copies .env files automatically)
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh create feature-login

# List all worktrees
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh list

# Switch to a worktree
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh switch feature-login

# Copy .env files to an existing worktree (if they weren't copied)
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh copy-env feature-login

# Clean up completed worktrees
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh cleanup

Commands
create <branch-name> [from-branch]

Creates a new worktree with the given branch name.

Options:

branch-name (required): The name for the new branch and worktree
from-branch (optional): Base branch to create from (defaults to main)

Example:

bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh create feature-login


What happens:

Checks if worktree already exists
Updates the base branch from remote
Creates new worktree and branch
Copies all .env files from main repo (.env, .env.local, .env.test, etc.)
Trusts dev tool configs with branch-aware safety rules:
trusted bases (main, develop, dev, trunk, staging, release/*) compare against themselves
other branches compare against the default branch
direnv auto-allow is skipped on non-trusted bases because .envrc can source unchecked files
Shows path for cd-ing to the worktree
list or ls

Lists all available worktrees with their branches and current status.

Example:

bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh list


Output shows:

Worktree name
Branch name
Which is current (marked with ✓)
Main repo status
switch <name> or go <name>

Switches to an existing worktree and cd's into it.

Example:

bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh switch feature-login


Optional:

If name not provided, lists available worktrees and prompts for selection
cleanup or clean

Interactively cleans up inactive worktrees with confirmation.

Example:

bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh cleanup


What happens:

Lists all inactive worktrees
Asks for confirmation
Removes selected worktrees
Cleans up empty directories
Workflow Examples
Code Review with Worktree
# Claude Code recognizes you're not on the PR branch
# Offers: "Use worktree for isolated review? (y/n)"

# You respond: yes
# Script runs (copies .env files automatically):
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh create pr-123-feature-name

# You're now in isolated worktree for review with all env vars
cd .worktrees/pr-123-feature-name

# After review, return to main:
cd ../..
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh cleanup

Parallel Feature Development
# For first feature (copies .env files):
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh create feature-login

# Later, start second feature (also copies .env files):
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh create feature-notifications

# List what you have:
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh list

# Switch between them as needed:
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh switch feature-login

# Return to main and cleanup when done:
cd .
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh cleanup

Key Design Principles
KISS (Keep It Simple, Stupid)
One manager script handles all worktree operations
Simple commands with sensible defaults
Interactive prompts prevent accidental operations
Clear naming using branch names directly
Opinionated Defaults
Worktrees always created from main (unless specified)
Worktrees stored in .worktrees/ directory
Branch name becomes worktree name
.gitignore automatically managed
Safety First
Confirms before creating worktrees
Confirms before cleanup to prevent accidental removal
Won't remove current worktree
Clear error messages for issues
Integration with Workflows
/ce:review

Instead of always creating a worktree:

1. Check current branch
2. If ALREADY on target branch (PR branch or requested branch) → stay there, no worktree needed
3. If DIFFERENT branch than the review target → offer worktree:
   "Use worktree for isolated review? (y/n)"
   - yes → call git-worktree skill
   - no → proceed with PR diff on current branch

/ce:work

Always offer choice:

1. Ask: "How do you want to work?
   1. New branch on current worktree (live work)
   2. Worktree (parallel work)"

2. If choice 1 → create new branch normally
3. If choice 2 → call git-worktree skill to create from main

Troubleshooting
"Worktree already exists"

If you see this, the script will ask if you want to switch to it instead.

"Cannot remove worktree: it is the current worktree"

Switch out of the worktree first (to main repo), then cleanup:

cd $(git rev-parse --show-toplevel)
bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh cleanup

Lost in a worktree?

See where you are:

bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh list

.env files missing in worktree?

If a worktree was created without .env files (e.g., via raw git worktree add), copy them:

bash ${CLAUDE_PLUGIN_ROOT}/skills/git-worktree/scripts/worktree-manager.sh copy-env feature-name


Navigate back to main:

cd $(git rev-parse --show-toplevel)

Technical Details
Directory Structure
.worktrees/
├── feature-login/          # Worktree 1
│   ├── .git
│   ├── app/
│   └── ...
├── feature-notifications/  # Worktree 2
│   ├── .git
│   ├── app/
│   └── ...
└── ...

.gitignore (updated to include .worktrees)

How It Works
Uses git worktree add for isolated environments
Each worktree has its own branch
Changes in one worktree don't affect others
Share git history with main repo
Can push from any worktree
Performance
Worktrees are lightweight (just file system links)
No repository duplication
Shared git objects for efficiency
Much faster than cloning or stashing/switching
Weekly Installs
621
Repository
everyinc/compou…g-plugin
GitHub Stars
16.0K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn