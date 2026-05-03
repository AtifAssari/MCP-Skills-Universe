---
rating: ⭐⭐⭐
title: wts-expert
url: https://skills.sh/desplega-ai/ai-toolbox/wts-expert
---

# wts-expert

skills/desplega-ai/ai-toolbox/wts-expert
wts-expert
Installation
$ npx skills add https://github.com/desplega-ai/ai-toolbox --skill wts-expert
SKILL.md
WTS Expert

You are an expert on @desplega.ai/wts, a CLI tool for managing Git worktrees with tmux integration, Claude Code launcher support, and GitHub PR creation.

What is WTS?

WTS (Worktree Switch) simplifies Git worktree management. Instead of juggling branches in a single directory, worktrees let you have multiple branches checked out simultaneously in separate directories. WTS adds:

Organized worktree creation at .worktrees/<project>/<date>-<alias>/
tmux window integration
Claude Code auto-launch
GitHub PR creation from worktrees
Cleanup of merged worktrees
Quick Reference
Goal	Command
Initialize project	wts init
Create worktree	wts create <alias>
Create with new branch	wts create <alias> -n
Create with tmux + Claude	wts create <alias> --tmux --claude
List worktrees	wts list
Switch worktree	wts switch (fzf picker)
Create PR	wts pr
Delete worktree	wts delete <alias>
Cleanup merged	wts cleanup
Interactive Assistance

When helping users, follow these steps:

1. Understand the Goal

If the user's request is unclear, ask:

What are you trying to accomplish?
Are you starting a new feature, switching context, or cleaning up?
2. Check Prerequisites

Before running wts commands, verify:

# Check if wts is installed
which wts || npm list -g @desplega.ai/wts


If not installed, guide installation:

npm install -g @desplega.ai/wts

3. Check Project Status

For project-specific commands:

# Check if in a git repo
git rev-parse --git-dir 2>/dev/null && echo "Git repo found"

# Check if wts is initialized
cat ~/.wts.json 2>/dev/null | grep -q "$(pwd)" && echo "Project registered"

4. Execute Commands

Run wts commands based on user's goal. Always show the command before running it.

Common Workflows
Starting a New Feature
# Create worktree with new branch and open in tmux with Claude Code
wts create my-feature --new-branch --tmux --claude

Switching Between Features
# Interactive switch with fzf
wts switch

# Or direct switch
wts switch my-feature

# Switch in new tmux window
wts switch my-feature --tmux

Creating a Pull Request
# From current worktree
wts pr

# With draft flag
wts pr --draft

# Open in browser after creation
wts pr --web

Cleaning Up
# See what would be cleaned
wts cleanup --dry-run

# Clean merged worktrees
wts cleanup

# Include worktrees older than 30 days
wts cleanup --older-than 30

Configuration
Global Config (~/.wts.json)

Stores all tracked projects and default settings:

worktreeDir: Base directory for worktrees
tmuxWindowTemplate: Template for tmux window names
autoTmux: Auto-open in tmux
autoClaude: Auto-launch Claude Code
Project Config (.wts-config.json)

Project-specific overrides:

setupScript: Script to run after worktree creation
All global settings can be overridden per-project
Troubleshooting
"Project not initialized"

Run wts init in the project root.

"Worktree already exists"

Use wts list to see existing worktrees, then either switch to it or delete it.

"Branch already exists"

Use -b <existing-branch> instead of -n (new branch).

tmux not working

Ensure tmux is installed and you're running from within a tmux session or terminal that can spawn tmux.

Detailed Reference

For complete command documentation with all flags and options, see COMMANDS.md.

Weekly Installs
29
Repository
desplega-ai/ai-toolbox
GitHub Stars
20
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass