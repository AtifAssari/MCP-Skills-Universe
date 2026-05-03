---
title: git-worktrees
url: https://skills.sh/jamesrochabrun/skills/git-worktrees
---

# git-worktrees

skills/jamesrochabrun/skills/git-worktrees
git-worktrees
Installation
$ npx skills add https://github.com/jamesrochabrun/skills --skill git-worktrees
SKILL.md
Git Worktrees for Claude Code
Overview

Run multiple Claude Code sessions in parallel on different branches using Git worktrees. This skill provides simple scripts and workflows to set up, manage, and clean up worktrees, enabling true parallel development without conflicts.

Why Worktrees?

Parallel Development: Run multiple Claude Code instances simultaneously
Zero Conflicts: Each worktree has independent file state
Fast Context Switching: No need to stash/commit when switching tasks
Isolated Experiments: Try different approaches without affecting main work
Long-Running Tasks: Let Claude work in background while you continue in main
Quick Start
1. Create a New Worktree (Super Easy!)

Just run the interactive script:

scripts/create_worktree.sh


This will:

✅ Prompt for feature name
✅ Create a new branch
✅ Set up the worktree
✅ Open in VS Code / editor
✅ Give you the Claude Code setup command

That's it! The script handles all complexity.

2. View All Worktrees
scripts/list_worktrees.sh


Shows a clean, formatted list of all your worktrees with their branches and status.

3. Clean Up Old Worktrees
scripts/cleanup_worktrees.sh


Interactive removal of merged or abandoned worktrees.

Core Workflow
Pattern 1: Parallel Feature Development

Scenario: You want Claude to build feature A while you work on feature B.

Steps:

Create worktree for feature A:

scripts/create_worktree.sh
# Enter: feature-a
# Script creates: ../repo-feature-a/


Open Claude Code in the new worktree:

The script outputs the path
Open Claude Code and navigate to that directory
Run /init to orient Claude

Give Claude the task:

"Build the user authentication feature with OAuth support"


Continue your work in main:

Your original directory is unchanged
No conflicts, no waiting
Claude works in parallel

When both are done, merge:

# Review Claude's work
cd ../repo-feature-a
git log

# If good, merge back
git checkout main
git merge feature-a

# Clean up
scripts/cleanup_worktrees.sh

Pattern 2: Long-Running Refactor

Scenario: You want Claude to refactor a large module while you continue development.

Steps:

Create refactor worktree:

scripts/create_worktree.sh
# Enter: refactor-auth-module


Start Claude in refactor worktree:

"Refactor the authentication module to use dependency injection"


Continue your daily work in main:

No interruption
No merge conflicts
Check progress periodically

Review and integrate when ready:

cd ../repo-refactor-auth-module
git log --oneline
# Review changes

# Merge when satisfied
git checkout main
git merge refactor-auth-module

Pattern 3: Multiple AI Agents (Advanced)

Scenario: You want 3 Claude instances working on different features simultaneously.

Steps:

Create 3 worktrees:

scripts/create_worktree.sh  # feature-api-endpoints
scripts/create_worktree.sh  # feature-ui-dashboard
scripts/create_worktree.sh  # feature-email-notifications


Open 3 Claude Code sessions:

Session 1: ../repo-feature-api-endpoints/
Session 2: ../repo-feature-ui-dashboard/
Session 3: ../repo-feature-email-notifications/

Assign tasks to each Claude:

Claude 1: "Build REST API endpoints for user management"
Claude 2: "Create admin dashboard UI"
Claude 3: "Implement email notification system"

Monitor progress:

scripts/list_worktrees.sh


Merge features as they complete:

# Feature by feature
git checkout main
git merge feature-api-endpoints
git merge feature-ui-dashboard
git merge feature-email-notifications

# Clean up
scripts/cleanup_worktrees.sh

Pattern 4: Hotfix While Development Continues

Scenario: Production bug needs immediate fix while Claude is working on a feature.

Steps:

Claude is already working in a feature worktree

Let it continue, don't interrupt

Create hotfix worktree from main:

scripts/create_worktree.sh
# Enter: hotfix-login-bug
# Choose base branch: main


Fix the bug yourself or with another Claude session:

cd ../repo-hotfix-login-bug
# Make fixes
git add .
git commit -m "Fix login redirect bug"


Merge hotfix to main:

git checkout main
git merge hotfix-login-bug
git push origin main


Sync feature worktree with latest main:

cd ../repo-feature-xyz
scripts/sync_worktree.sh
# Merges latest main into feature branch

Essential Scripts
scripts/create_worktree.sh

Interactive worktree creation with all the right defaults.

What it does:

Prompts for feature name
Validates git repo
Creates branch from main (or specified base)
Sets up worktree in parallel directory
Outputs setup instructions

Usage:

scripts/create_worktree.sh

# Prompts:
# Feature name: my-feature
# Base branch (default: main):
#
# Creates: ../repo-my-feature/
# Branch: my-feature


Advanced usage:

# Create from specific branch
scripts/create_worktree.sh --base develop

# Specify location
scripts/create_worktree.sh --dir ~/worktrees/my-feature

scripts/list_worktrees.sh

Shows all active worktrees with status.

Output:

╔════════════════════════════════════════════════╗
║            Active Git Worktrees                ║
╚════════════════════════════════════════════════╝

📁 Main Worktree
   Path: /home/user/project
   Branch: main
   Status: clean

📁 Feature Worktrees
   Path: /home/user/project-feature-api
   Branch: feature-api
   Status: 2 uncommitted changes

   Path: /home/user/project-refactor
   Branch: refactor-auth
   Status: clean

scripts/cleanup_worktrees.sh

Interactive cleanup of old worktrees.

Features:

Lists all worktrees with merge status
Identifies merged branches (safe to remove)
Prompts for confirmation
Safely removes worktree and branch

Usage:

scripts/cleanup_worktrees.sh

# Output:
# Found 3 worktrees
#
# 1. feature-api (merged to main) - Safe to remove
# 2. feature-dashboard (not merged) - Keep
# 3. old-experiment (not merged, 30 days old) - Consider removing
#
# Which worktrees to remove? (1,3): 1

scripts/sync_worktree.sh

Keep worktree up-to-date with main branch.

What it does:

Fetches latest from remote
Merges main into current worktree branch
Handles conflicts with guidance

Usage:

# From within a worktree
cd ../repo-feature-api
scripts/sync_worktree.sh

# Or specify worktree
scripts/sync_worktree.sh ../repo-feature-api

Claude Code Integration
Important: Run /init in Each Worktree

When you open a new Claude Code session in a worktree, always run /init first:

/init


This ensures Claude:

Understands the codebase structure
Has proper context
Can navigate files correctly
Recommended Claude Code Workflow
Create worktree (using script)
Open Claude Code in worktree directory
Run /init to orient Claude
Give task to Claude
Monitor via git log or file watching
Review when complete
Merge if satisfied
Cleanup worktree
Best Practices
Naming Conventions

Good names:

feature-user-auth ✅
refactor-api-layer ✅
hotfix-login-bug ✅
experiment-new-db ✅

Bad names:

test ❌ (too vague)
wt1 ❌ (meaningless)
fixes ❌ (unclear)

Recommended format:

<type>-<short-description>

Types:
- feature-*
- refactor-*
- hotfix-*
- experiment-*
- review-*

Directory Structure

Recommended layout:

~/projects/
  └── myapp/              # Main worktree (main branch)
      ├── myapp-feature-api/      # Feature worktree
      ├── myapp-refactor-auth/    # Refactor worktree
      └── myapp-hotfix-bug/       # Hotfix worktree


The scripts default to creating worktrees as siblings to your main directory with a naming pattern: <repo>-<branch-name>.

When to Use Worktrees

✅ Use worktrees when:

Running multiple Claude Code sessions in parallel
Working on independent features simultaneously
Doing long-running refactors
Experimenting with major changes
Quick hotfixes during feature development
Code reviews without interrupting work

❌ Don't use worktrees for:

Simple branch switching (just use git checkout)
Minor tweaks (stash instead)
Single-task workflows
Very short-lived branches (< 1 hour)
Keeping Worktrees in Sync

Problem: Feature branches can get out of date with main.

Solution: Regularly sync worktrees:

# Option 1: Use the sync script
cd ../repo-feature-api
scripts/sync_worktree.sh

# Option 2: Manual sync
cd ../repo-feature-api
git fetch origin
git merge origin/main


Recommended frequency:

Daily for long-running features
After major merges to main
Before creating PRs
Managing Many Worktrees

Quick status of all worktrees:

scripts/list_worktrees.sh


Regular cleanup (weekly):

scripts/cleanup_worktrees.sh


Find stale worktrees:

# Worktrees with old commits
git worktree list | while read path branch commit; do
  cd "$path"
  last_commit=$(git log -1 --format=%cr)
  echo "$branch: Last commit $last_commit"
done

Troubleshooting
Issue: "fatal: invalid reference"

Cause: Branch name has invalid characters

Solution: Use alphanumeric + hyphens only:

# Bad
feature/my_feature  ❌

# Good
feature-my-feature  ✅

Issue: "cannot remove worktree, path is not a working tree"

Cause: Worktree directory was manually deleted

Solution: Prune worktree references:

git worktree prune

Issue: Claude seems "lost" in worktree

Cause: Didn't run /init after opening worktree

Solution: Always run /init when starting Claude in a new worktree:

/init

Issue: Merge conflicts when syncing worktree

Cause: Changes in worktree conflict with main

Solution 1: Resolve conflicts manually:

cd ../repo-feature-api
git fetch origin
git merge origin/main
# Fix conflicts in editor
git add .
git commit -m "Merge main and resolve conflicts"


Solution 2: If you want to discard worktree changes and restart:

cd ../repo-feature-api
git fetch origin
git reset --hard origin/main
# Start feature over

Issue: "Cannot lock ref" error

Cause: Branch exists in multiple worktrees

Solution: You can't have the same branch checked out in multiple worktrees. Create a new branch:

scripts/create_worktree.sh
# Use a different branch name

Issue: Worktree takes up too much disk space

Cause: Git worktrees share the .git directory, but files are duplicated

Solution 1: Clean up old worktrees:

scripts/cleanup_worktrees.sh


Solution 2: For large repos, use sparse-checkout:

git -C ../repo-feature-api sparse-checkout set src/ tests/

Advanced Usage
Custom Slash Command

Create a /worktree command for Claude Code. See references/slash_command_template.md for the complete setup.

Usage after setup:

/worktree feature-new-api


Claude will:

Create the worktree
Provide setup instructions
Offer to continue the conversation in the new worktree
Sharing Worktrees in Team

Worktrees are local only, but you can share the workflow:

Share branch, not worktree:

cd ../repo-feature-api
git push origin feature-api

# Teammate creates their own worktree
git worktree add ../repo-feature-api feature-api


Document your worktree structure in team docs

Use consistent naming across team

Worktree Performance Optimization

For large repos:

Use sparse-checkout (only checkout files you need):

git -C ../repo-feature-api sparse-checkout init
git -C ../repo-feature-api sparse-checkout set src/ tests/


Use worktree prune regularly:

git worktree prune


Limit concurrent worktrees to 3-5 for best performance

Common Workflows Summary
Quick Reference
Task	Command
Create new worktree	scripts/create_worktree.sh
List all worktrees	scripts/list_worktrees.sh
Clean up worktrees	scripts/cleanup_worktrees.sh
Sync with main	scripts/sync_worktree.sh
Manual create	git worktree add ../path branch-name
Manual list	git worktree list
Manual remove	git worktree remove ../path
Prune references	git worktree prune
Real-World Examples
Example 1: Parallel API & UI Development

Setup:

# Create API worktree
scripts/create_worktree.sh
# Name: feature-api

# Create UI worktree
scripts/create_worktree.sh
# Name: feature-ui


Execution:

Claude 1 in ../repo-feature-api: "Build REST API for user management"
Claude 2 in ../repo-feature-ui: "Create React UI for user management"
You in main: Continue other work

Merge:

git checkout main
git merge feature-api
git merge feature-ui
scripts/cleanup_worktrees.sh

Example 2: Code Review Without Context Switching

Scenario: Need to review PR while Claude works on feature

Setup:

# Claude is working in feature worktree
# You need to review PR #123

scripts/create_worktree.sh
# Name: review-pr-123
# Base: pr-branch-name


Execution:

Review code in ../repo-review-pr-123
Claude continues work in ../repo-feature-xyz
No context switching needed

Cleanup:

# After review
scripts/cleanup_worktrees.sh
# Select review-pr-123

Example 3: Experimentation Without Risk

Scenario: Want to try a radical refactor without breaking current work

Setup:

scripts/create_worktree.sh
# Name: experiment-new-architecture


Execution:

Experiment freely in ../repo-experiment-new-architecture
Main worktree remains stable
If experiment fails, just delete worktree

Decision:

# If experiment succeeded
git checkout main
git merge experiment-new-architecture

# If experiment failed
scripts/cleanup_worktrees.sh
# Delete experiment worktree (no harm done)

Tips for Maximum Productivity
1. Name Worktrees Descriptively
You'll thank yourself later when you have 5 worktrees open
2. Always Run /init
First thing when opening Claude in a new worktree
3. Merge Frequently
Don't let worktrees diverge for weeks
Sync with main regularly
4. Clean Up Weekly
Run scripts/cleanup_worktrees.sh every Friday
Keep your workspace tidy
5. Use Scripts
Don't memorize git worktree commands
Scripts handle edge cases and validation
6. Monitor Progress
Use scripts/list_worktrees.sh to see what's active
Check git logs in worktrees periodically
7. Limit Concurrent Sessions
3-5 worktrees max for best performance
More than that gets hard to manage
Resources
Scripts
create_worktree.sh - Interactive worktree creation
list_worktrees.sh - Show all active worktrees
cleanup_worktrees.sh - Remove old worktrees
sync_worktree.sh - Keep worktrees synchronized
References
worktree_commands.md - Complete Git worktree command reference
best_practices.md - Detailed best practices and patterns
slash_command_template.md - Create custom /worktree command
Summary

Git worktrees enable true parallel development with Claude Code:

✅ Run multiple Claude sessions without conflicts ✅ Switch contexts instantly without stashing ✅ Experiment safely without breaking main ✅ Simple scripts handle all complexity ✅ Clean workflows for common scenarios

Get started:

scripts/create_worktree.sh


That's it! The scripts make worktrees simple and practical.

Weekly Installs
75
Repository
jamesrochabrun/skills
GitHub Stars
128
First Seen
6 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass