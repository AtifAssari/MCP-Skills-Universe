---
title: smart-commit
url: https://skills.sh/jackjin1997/clawforge/smart-commit
---

# smart-commit

skills/jackjin1997/clawforge/smart-commit
smart-commit
Installation
$ npx skills add https://github.com/jackjin1997/clawforge --skill smart-commit
SKILL.md
Smart Commit

AI-powered git commit message generation using LLM. Creates meaningful commit messages from code changes.

Capabilities
Amend Last Commit - Summarize staged/unstaged changes and amend the last commit message
Squash Commits - Summarize last N commits and create a consolidated commit
Interactive Commit - Confirm files with user, then summarize and create new commit
Quick Start
For New Commit
# Show changed files and ask user confirmation
git status

# After confirmation, summarize changes with LLM
# Create commit with generated message

For Amending
# Get diff of changes to amend
git diff --cached  # staged
git diff HEAD~1    # compared to last commit

# LLM summarizes, then
git commit --amend -m "new message"

For Squashing
# Get last N commit messages and diffs
git log -n N --format="%H %s"

# LLM summarizes, then
git reset --soft HEAD~N
git commit -m "consolidated message"

Workflow Decision Tree
User wants git commit help?
├─ "amend" or "修改"? → Amend workflow
├─ "squash" or "合并" + number? → Squash workflow
└─ New commit? → Interactive workflow

Amend Workflow
Get changes: git diff --cached (staged) or git diff HEAD~1 (all changes since last commit)
Send to LLM with prompt from references/prompts.md section "Amend Commit"
User reviews suggested message
git commit --amend -m "message"
Squash Workflow
Get last N commits: git log -n N --format="%H|%s|%an|%ad"
Get combined diff: git diff HEAD~N..HEAD
Send to LLM with prompt from references/prompts.md section "Squash Commits"
User reviews suggested message
git reset --soft HEAD~N && git commit -m "message"
Interactive Commit Workflow
Show git status to user
Ask user to confirm which files to include
Get diff for confirmed files
Send to LLM with prompt from references/prompts.md section "New Commit"
User reviews suggested message
git add <files> && git commit -m "message"
LLM Prompts

See references/prompts.md for:

New commit message generation
Amend commit message generation
Squash commit message generation

Each prompt includes:

Git diff input format
Output format requirements
Style guidelines (conventional commits, etc.)
Weekly Installs
29
Repository
jackjin1997/clawforge
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass