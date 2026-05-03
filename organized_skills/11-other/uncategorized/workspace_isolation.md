---
rating: ⭐⭐⭐
title: workspace-isolation
url: https://skills.sh/qodex-ai/ai-agent-skills/workspace-isolation
---

# workspace-isolation

skills/qodex-ai/ai-agent-skills/workspace-isolation
workspace-isolation
Installation
$ npx skills add https://github.com/qodex-ai/ai-agent-skills --skill workspace-isolation
SKILL.md
Using Git Worktrees
Overview

Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching.

Core principle: Systematic directory selection + safety verification = reliable isolation.

Announce at start: "I'm using the using-git-worktrees skill to set up an isolated workspace."

Directory Selection Process

Follow this priority order:

1. Check Existing Directories
# Check in priority order
ls -d .worktrees 2>/dev/null     # Preferred (hidden)
ls -d worktrees 2>/dev/null      # Alternative


If found: Use that directory. If both exist, .worktrees wins.

2. Check CLAUDE.md
grep -i "worktree.*director" CLAUDE.md 2>/dev/null


If preference specified: Use it without asking.

3. Ask User

If no directory exists and no CLAUDE.md preference:

No worktree directory found. Where should I create worktrees?

1. .worktrees/ (project-local, hidden)
2. ~/.config/superpowers/worktrees/<project-name>/ (global location)

Which would you prefer?

Safety Verification
For Project-Local Directories (.worktrees or worktrees)

MUST verify .gitignore before creating worktree:

# Check if directory pattern in .gitignore
grep -q "^\.worktrees/$" .gitignore || grep -q "^worktrees/$" .gitignore


If NOT in .gitignore:

Per Jesse's rule "Fix broken things immediately":

Add appropriate line to .gitignore
Commit the change
Proceed with worktree creation

Why critical: Prevents accidentally committing worktree contents to repository.

For Global Directory (~/.config/superpowers/worktrees)

No .gitignore verification needed - outside project entirely.

Creation Steps
1. Detect Project Name
project=$(basename "$(git rev-parse --show-toplevel)")

2. Create Worktree
# Determine full path
case $LOCATION in
  .worktrees|worktrees)
    path="$LOCATION/$BRANCH_NAME"
    ;;
  ~/.config/superpowers/worktrees/*)
    path="~/.config/superpowers/worktrees/$project/$BRANCH_NAME"
    ;;
esac

# Create worktree with new branch
git worktree add "$path" -b "$BRANCH_NAME"
cd "$path"

3. Run Project Setup

Auto-detect and run appropriate setup:

# Node.js
if [ -f package.json ]; then npm install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then poetry install; fi

# Go
if [ -f go.mod ]; then go mod download; fi

4. Verify Clean Baseline

Run tests to ensure worktree starts clean:

# Examples - use project-appropriate command
npm test
cargo test
pytest
go test ./...


If tests fail: Report failures, ask whether to proceed or investigate.

If tests pass: Report ready.

5. Report Location
Worktree ready at <full-path>
Tests passing (<N> tests, 0 failures)
Ready to implement <feature-name>

Quick Reference
Situation	Action
.worktrees/ exists	Use it (verify .gitignore)
worktrees/ exists	Use it (verify .gitignore)
Both exist	Use .worktrees/
Neither exists	Check CLAUDE.md → Ask user
Directory not in .gitignore	Add it immediately + commit
Tests fail during baseline	Report failures + ask
No package.json/Cargo.toml	Skip dependency install
Common Mistakes

Skipping .gitignore verification

Problem: Worktree contents get tracked, pollute git status
Fix: Always grep .gitignore before creating project-local worktree

Assuming directory location

Problem: Creates inconsistency, violates project conventions
Fix: Follow priority: existing > CLAUDE.md > ask

Proceeding with failing tests

Problem: Can't distinguish new bugs from pre-existing issues
Fix: Report failures, get explicit permission to proceed

Hardcoding setup commands

Problem: Breaks on projects using different tools
Fix: Auto-detect from project files (package.json, etc.)
Example Workflow
You: I'm using the using-git-worktrees skill to set up an isolated workspace.

[Check .worktrees/ - exists]
[Verify .gitignore - contains .worktrees/]
[Create worktree: git worktree add .worktrees/auth -b feature/auth]
[Run npm install]
[Run npm test - 47 passing]

Worktree ready at /Users/jesse/myproject/.worktrees/auth
Tests passing (47 tests, 0 failures)
Ready to implement auth feature

Red Flags

Never:

Create worktree without .gitignore verification (project-local)
Skip baseline test verification
Proceed with failing tests without asking
Assume directory location when ambiguous
Skip CLAUDE.md check

Always:

Follow directory priority: existing > CLAUDE.md > ask
Verify .gitignore for project-local
Auto-detect and run project setup
Verify clean test baseline
Integration

Called by:

brainstorming (Phase 4) - REQUIRED when design is approved and implementation follows
Any skill needing isolated workspace

Pairs with:

finishing-a-development-branch - REQUIRED for cleanup after work complete
executing-plans or subagent-driven-development - Work happens in this worktree
Weekly Installs
68
Repository
qodex-ai/ai-agent-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass