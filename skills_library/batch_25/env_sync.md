---
title: env-sync
url: https://skills.sh/qiaoshouqing/skills/env-sync
---

# env-sync

skills/qiaoshouqing/skills/env-sync
env-sync
Installation
$ npx skills add https://github.com/qiaoshouqing/skills --skill env-sync
SKILL.md
Env Sync - Git Worktree Environment File Synchronization

This skill syncs .env files from a git root repository to git worktrees.

When to Use
User asks to sync env or copy env
User mentions missing environment variables or .env file
Working in a git worktree that lacks a .env file
User asks to set up environment for a worktree
Security Rules
NEVER display .env file contents - they contain secrets
ALWAYS ask before overwriting - if .env already exists, confirm with user first
Validate paths - ensure the root path exists and is a valid git repository
No arbitrary paths - only sync from the actual git root repository
Instructions for Agent
Step 1: Check if in a Git Worktree
# Check if .git is a file (worktree) or directory (regular repo)
[ -f .git ] && echo "worktree" || echo "not-worktree"


If not a worktree, inform user this skill is for git worktrees only.

Step 2: Find and Validate Root Repository
# Read gitdir and extract root path
GITDIR=$(cat .git | grep "^gitdir:" | sed 's/gitdir: //')
ROOT_REPO=$(echo "$GITDIR" | sed 's/\.git\/worktrees\/.*//')

# Validate: must be a real git repository
if [ -d "${ROOT_REPO}/.git" ]; then
  echo "Valid root: $ROOT_REPO"
else
  echo "Invalid root path - not a git repository"
  exit 1
fi

Step 3: Check for Existing .env
# IMPORTANT: Always check before copying
if [ -f ./.env ]; then
  echo "WARNING: .env already exists in this worktree"
  # ASK USER before proceeding
fi


If .env exists: STOP and ask user "Do you want to overwrite the existing .env file?"

Step 4: Copy .env (only after user confirmation if needed)
if [ -f "${ROOT_REPO}/.env" ]; then
  cp "${ROOT_REPO}/.env" ./.env
  echo "Synced .env from $ROOT_REPO"
else
  echo "No .env found in root repository: $ROOT_REPO"
fi

Complete Safe Script
# Safe env sync with validation
if [ ! -f .git ]; then
  echo "Not a git worktree"
  exit 1
fi

GITDIR=$(cat .git | grep "^gitdir:" | sed 's/gitdir: //')
ROOT=$(echo "$GITDIR" | sed 's/\.git\/worktrees\/.*//')

# Validate root is a git repo
if [ ! -d "${ROOT}/.git" ]; then
  echo "Invalid: $ROOT is not a git repository"
  exit 1
fi

# Check if .env exists at root
if [ ! -f "${ROOT}/.env" ]; then
  echo "No .env in root: $ROOT"
  exit 1
fi

# Check if local .env exists - MUST ASK USER
if [ -f ./.env ]; then
  echo "WARNING: .env already exists here. Ask user before overwriting."
  exit 0
fi

# Safe to copy
cp "${ROOT}/.env" ./.env
echo "Synced .env from $ROOT"

Response Guidelines
Always inform user what was done
If .env already exists: MUST ask user before overwriting
If root .env doesn't exist: tell user the path checked
Never display .env file contents
Report only: file exists/copied, line count, file size
Error Handling
Situation	Action
Not a worktree	Inform user, no action
Invalid root path	Warn user, no action
No root .env	Tell user path, suggest checking
.env exists	Ask user before overwrite
Permission denied	Suggest checking permissions
Weekly Installs
10
Repository
qiaoshouqing/skills
GitHub Stars
1
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass