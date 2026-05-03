---
title: super-worktree
url: https://skills.sh/marioxe301/super-worktree/super-worktree
---

# super-worktree

skills/marioxe301/super-worktree/super-worktree
super-worktree
Installation
$ npx skills add https://github.com/marioxe301/super-worktree --skill super-worktree
SKILL.md
super-worktree

A skill for managing isolated git worktrees for parallel feature development with monorepo-aware env file copying and node_modules symlinking.

Worktree Creation Overview

Git worktrees let you work on multiple branches simultaneously in a single repository. This skill enhances worktrees with:

Sensitive file copying: Automatically copies .env, credentials, and other sensitive files to new worktrees
node_modules symlinking: Saves disk space by symlinking node_modules directories
Configurable patterns: Define custom sync patterns per-project or globally
Dev tool trust: Automatically trusts Mise/direnv baseline when symlinking
Creating a worktree
bash scripts/worktree-manager.sh create <branch> [from-branch] [--config <file>]


Parameters:

<branch> - Name of the new branch/worktree (required)
[from-branch] - Base branch to create from (defaults to origin/HEAD or main)
--config <file> - Path to custom config file (optional)

Example:

# Create feature branch from main
bash scripts/worktree-manager.sh create feature/new-login

# Create from develop branch with custom config
bash scripts/worktree-manager.sh create feature/payments --config .super-worktree.json

# Create from a specific commit
bash scripts/worktree-manager.sh create hotfix/urgent fix/abc123

Deleting a worktree
bash scripts/worktree-manager.sh delete <branch>


Removes the worktree and optionally deletes the branch (use with caution).

Example:

bash scripts/worktree-manager.sh delete feature/new-login

Cleaning up (merge)
bash scripts/worktree-manager.sh merge <branch>


Merges the branch into its upstream and then deletes the worktree. Use when feature is complete.

Example:

bash scripts/worktree-manager.sh merge feature/new-login

Configuration

Create a super-worktree.json in your project root for custom patterns:

{
  "sync": {
    "copyFiles": [
      ".env",
      ".env.*",
      ".envrc",
      ".local.*",
      "*.secret",
      "*.key",
      ".secrets.*",
      "credentials.json",
      "credentials.yml",
      "credentials.env",
      "auth.json",
      "auth.yml",
      "auth.env",
      ".dev.vars",
      ".prod.vars",
      ".staging.vars"
    ],
    "symlinkDirs": [
      "node_modules"
    ],
    "exclude": [
      "node_modules",
      ".git",
      "dist",
      "build",
      ".next",
      "out",
      "coverage",
      ".turbo",
      ".vercel",
      ".worktrees"
    ]
  }
}

Config Priority

Configuration is loaded in this order (later overrides earlier):

Built-in defaults - Always available
Global config - ~/.config/super-worktree/config.json
Project config - .super-worktree.json in repo root
CLI flag - --config <file> argument (highest priority)
JSON Schema

A JSON Schema is provided for config validation:

{
  "$schema": "./schemas/super-worktree.schema.json",
  "sync": {
    "copyFiles": [".env", ".env.local"],
    "symlinkDirs": ["node_modules", ".pnpm-store"],
    "exclude": ["dist", "build"]
  }
}

Default Patterns

The skill includes sensible defaults that cover most projects:

copyFiles (copied to worktree)
.env, .env.* - Environment files
.envrc - direnv config
.local.* - Local overrides
*.secret, *.key, .secrets.* - Secret files
credentials.json, credentials.yml, credentials.env - Credentials
auth.json, auth.yml, auth.env - Auth config
.dev.vars, .prod.vars, .staging.vars - Environment-specific vars
symlinkDirs (symlinked to save space)
node_modules - Node dependencies
exclude (not copied or symlinked)
node_modules, .git, dist, build, .next, out, coverage, .turbo, .vercel, .worktrees
Troubleshooting
"worktree already exists"

The branch already has a worktree. Delete it first:

bash scripts/worktree-manager.sh delete <branch>

"jq not found"

The script uses jq for JSON parsing. Install with:

# macOS
brew install jq

# Ubuntu/Debian
sudo apt install jq

# CentOS/RHEL
sudo yum install jq

"python3 not found"

Fallback JSON parser requires Python 3. Ensure it's installed:

# Verify
python3 --version

# Install (macOS)
brew install python3

# Install (Ubuntu)
sudo apt install python3

"cannot stat: No such file or directory"

The base branch or reference doesn't exist. Verify:

git branch -a
git log --oneline -5

Permission denied

Make the script executable:

chmod +x scripts/worktree-manager.sh

symlink fails with "File exists"

Remove existing node_modules in worktree first:

rm -rf .worktrees/<branch>/node_modules
bash scripts/worktree-manager.sh create <branch>

Installation
OpenCode (recommended via OCX)
# Install via OCX registry (recommended)
ocx add marioxe301/super-worktree --from https://marioxe301.github.io/super-worktree

# Or manual copy
cp -r super-worktree ~/.config/opencode/skills/

Claude Code
# Claude marketplace
/plugin install marioxe301/super-worktree

# Or npx skills
npx skills add marioxe301/super-worktree -a claude-code

Other AI Agents
# npx skills works with Codex, Cursor, Windsurf, Cline, and 40+ agents
npx skills add marioxe301/super-worktree

# Install to specific agents
npx skills add marioxe301/super-worktree -a codex -a cursor

Manual
cp -r super-worktree ~/.config/opencode/skills/

Requirements
Git 2.5+ (worktree support)
Bash 4.0+
jq (optional, for JSON config; Python 3 fallback available)
python3 (optional, for JSON config fallback)
Weekly Installs
9
Repository
marioxe301/supe…worktree
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass