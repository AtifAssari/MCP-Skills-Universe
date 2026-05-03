---
rating: ⭐⭐⭐
title: project-session-manager
url: https://skills.sh/yeachan-heo/oh-my-claudecode/project-session-manager
---

# project-session-manager

skills/yeachan-heo/oh-my-claudecode/project-session-manager
project-session-manager
Installation
$ npx skills add https://github.com/yeachan-heo/oh-my-claudecode --skill project-session-manager
SKILL.md
Project Session Manager (PSM) Skill

psm is the compatibility alias for this canonical skill entrypoint.

Quick Start (worktree-first): Start with omc teleport when you want an isolated issue/PR/feature worktree before adding any tmux/session orchestration:

omc teleport #123          # Create worktree for issue/PR
omc teleport my-feature    # Create worktree for feature
omc teleport list          # List worktrees


See Teleport Command below for details.

Automate isolated development environments using git worktrees and tmux sessions with Claude Code. Enables parallel work across multiple tasks, projects, and repositories.

Canonical slash command: /oh-my-claudecode:project-session-manager (alias: /oh-my-claudecode:psm).

Commands
Command	Description	Example
review <ref>	PR review session	/psm review omc#123
fix <ref>	Issue fix session	/psm fix omc#42
feature <proj> <name>	Feature development	/psm feature omc add-webhooks
list [project]	List active sessions	/psm list
attach <session>	Attach to session	/psm attach omc:pr-123
kill <session>	Kill session	/psm kill omc:pr-123
cleanup	Clean merged/closed	/psm cleanup
status	Current session info	/psm status
Project References

Supported formats:

Alias: omc#123 (requires ~/.psm/projects.json)
Full: owner/repo#123
URL: https://github.com/owner/repo/pull/123
Current: #123 (uses current directory's repo)
Configuration
Project Aliases (~/.psm/projects.json)
{
  "aliases": {
    "omc": {
      "repo": "Yeachan-Heo/oh-my-claudecode",
      "local": "~/Workspace/oh-my-claudecode",
      "default_base": "main"
    }
  },
  "defaults": {
    "worktree_root": "~/.psm/worktrees",
    "cleanup_after_days": 14
  }
}

Providers

PSM supports multiple issue tracking providers:

Provider	CLI Required	Reference Formats	Commands
GitHub (default)	gh	owner/repo#123, alias#123, GitHub URLs	review, fix, feature
Jira	jira	PROJ-123 (if PROJ configured), alias#123	fix, feature
Jira Configuration

To use Jira, add an alias with jira_project and provider: "jira":

{
  "aliases": {
    "mywork": {
      "jira_project": "MYPROJ",
      "repo": "mycompany/my-project",
      "local": "~/Workspace/my-project",
      "default_base": "develop",
      "provider": "jira"
    }
  }
}


Important: The repo field is still required for cloning the git repository. Jira tracks issues, but you work in a git repo.

For non-GitHub repos, use clone_url instead:

{
  "aliases": {
    "private": {
      "jira_project": "PRIV",
      "clone_url": "git@gitlab.internal:team/repo.git",
      "local": "~/Workspace/repo",
      "provider": "jira"
    }
  }
}

Jira Reference Detection

PSM only recognizes PROJ-123 format as Jira when PROJ is explicitly configured as a jira_project in your aliases. This prevents false positives from branch names like FIX-123.

Jira Examples
# Fix a Jira issue (MYPROJ must be configured)
psm fix MYPROJ-123

# Fix using alias (recommended)
psm fix mywork#123

# Feature development (works same as GitHub)
psm feature mywork add-webhooks

# Note: 'psm review' is not supported for Jira (no PR concept)
# Use 'psm fix' for Jira issues

Jira CLI Setup

Install the Jira CLI:

# macOS
brew install ankitpokhrel/jira-cli/jira-cli

# Linux
# See: https://github.com/ankitpokhrel/jira-cli#installation

# Configure (interactive)
jira init


The Jira CLI handles authentication separately from PSM.

Directory Structure
~/.psm/
├── projects.json       # Project aliases
├── sessions.json       # Active session registry
└── worktrees/          # Worktree storage
    └── <project>/
        └── <type>-<id>/

Session Naming
Type	Tmux Session	Worktree Dir
PR Review	psm:omc:pr-123	~/.psm/worktrees/omc/pr-123
Issue Fix	psm:omc:issue-42	~/.psm/worktrees/omc/issue-42
Feature	psm:omc:feat-auth	~/.psm/worktrees/omc/feat-auth
Implementation Protocol

When the user invokes a PSM command, follow this protocol:

Parse Arguments

Parse {{ARGUMENTS}} to determine:

Subcommand: review, fix, feature, list, attach, kill, cleanup, status
Reference: project#number, URL, or session ID
Options: --branch, --base, --no-claude, --no-tmux, etc.
Subcommand: review <ref>

Purpose: Create PR review session

Steps:

Resolve reference:

# Read project aliases
cat ~/.psm/projects.json 2>/dev/null || echo '{"aliases":{}}'

# Parse ref format: alias#num, owner/repo#num, or URL
# Extract: project_alias, repo (owner/repo), pr_number, local_path


Fetch PR info:

gh pr view <pr_number> --repo <repo> --json number,title,author,headRefName,baseRefName,body,files,url


Ensure local repo exists:

# If local path doesn't exist, clone
if [[ ! -d "$local_path" ]]; then
  git clone "https://github.com/$repo.git" "$local_path"
fi


Create worktree:

worktree_path="$HOME/.psm/worktrees/$project_alias/pr-$pr_number"

# Fetch PR branch
cd "$local_path"
git fetch origin "pull/$pr_number/head:pr-$pr_number-review"

# Create worktree
git worktree add "$worktree_path" "pr-$pr_number-review"


Create session metadata:

cat > "$worktree_path/.psm-session.json" << EOF
{
  "id": "$project_alias:pr-$pr_number",
  "type": "review",
  "project": "$project_alias",
  "ref": "pr-$pr_number",
  "branch": "<head_branch>",
  "base": "<base_branch>",
  "created_at": "$(date -Iseconds)",
  "tmux_session": "psm:$project_alias:pr-$pr_number",
  "worktree_path": "$worktree_path",
  "source_repo": "$local_path",
  "github": {
    "pr_number": $pr_number,
    "pr_title": "<title>",
    "pr_author": "<author>",
    "pr_url": "<url>"
  },
  "state": "active"
}
EOF


Update sessions registry:

# Add to ~/.psm/sessions.json


Create tmux session:

tmux new-session -d -s "psm:$project_alias:pr-$pr_number" -c "$worktree_path"


Launch Claude Code (unless --no-claude):

# --dangerously-skip-permissions prevents the "Do you trust this directory?" prompt
# and repeated tool-approval prompts from stalling the session (issue #2508).
tmux send-keys -t "psm:$project_alias:pr-$pr_number" "claude --dangerously-skip-permissions" Enter

# After claude boots (PSM_CLAUDE_STARTUP_DELAY, default 5s), deliver the task.
# Use -l (literal) so special characters are not misinterpreted by tmux.
sleep "${PSM_CLAUDE_STARTUP_DELAY:-5}"
tmux send-keys -t "psm:$project_alias:pr-$pr_number" -l \
  "Review PR #$pr_number: \"$pr_title\" by @$pr_author ($head_branch → $base_branch). URL: $pr_url." Enter


Output session info:

Session ready!

  ID: omc:pr-123
  Worktree: ~/.psm/worktrees/omc/pr-123
  Tmux: psm:omc:pr-123

To attach: tmux attach -t psm:omc:pr-123

Subcommand: fix <ref>

Purpose: Create issue fix session

Steps:

Resolve reference (same as review)

Fetch issue info:

gh issue view <issue_number> --repo <repo> --json number,title,body,labels,url


Create feature branch:

cd "$local_path"
git fetch origin main
branch_name="fix/$issue_number-$(echo "$title" | tr ' ' '-' | tr '[:upper:]' '[:lower:]' | head -c 30)"
git checkout -b "$branch_name" origin/main


Create worktree:

worktree_path="$HOME/.psm/worktrees/$project_alias/issue-$issue_number"
git worktree add "$worktree_path" "$branch_name"


Create session metadata (similar to review, type="fix")

Update registry, create tmux, launch claude: Same as review, but pass issue context as the initial task prompt:

tmux send-keys -t "psm:$project_alias:issue-$issue_number" "claude --dangerously-skip-permissions" Enter
# After claude boots, deliver the task (see PSM_CLAUDE_STARTUP_DELAY):
tmux send-keys -t "psm:$project_alias:issue-$issue_number" -l \
  "Fix issue #$issue_number: \"$issue_title\". URL: $issue_url. Branch: $branch_name." Enter

Subcommand: feature <project> <name>

Purpose: Start feature development

Steps:

Resolve project (from alias or path)

Create feature branch:

cd "$local_path"
git fetch origin main
branch_name="feature/$feature_name"
git checkout -b "$branch_name" origin/main


Create worktree:

worktree_path="$HOME/.psm/worktrees/$project_alias/feat-$feature_name"
git worktree add "$worktree_path" "$branch_name"


Create session, tmux, launch claude with feature context as initial prompt:

tmux send-keys -t "psm:$project_alias:feat-$feature_name" "claude --dangerously-skip-permissions" Enter
tmux send-keys -t "psm:$project_alias:feat-$feature_name" -l \
  "Implement feature \"$feature_name\" for project $project. Branch: $branch_name." Enter

Subcommand: list [project]

Purpose: List active sessions

Steps:

Read sessions registry:

cat ~/.psm/sessions.json 2>/dev/null || echo '{"sessions":{}}'


Check tmux sessions:

tmux list-sessions -F "#{session_name}" 2>/dev/null | grep "^psm:"


Check worktrees:

ls -la ~/.psm/worktrees/*/ 2>/dev/null


Format output:

Active PSM Sessions:

ID                 | Type    | Status   | Worktree
-------------------|---------|----------|---------------------------
omc:pr-123        | review  | active   | ~/.psm/worktrees/omc/pr-123
omc:issue-42      | fix     | detached | ~/.psm/worktrees/omc/issue-42

Subcommand: attach <session>

Purpose: Attach to existing session

Steps:

Parse session ID: project:type-number

Verify session exists:

tmux has-session -t "psm:$session_id" 2>/dev/null


Attach:

tmux attach -t "psm:$session_id"

Subcommand: kill <session>

Purpose: Kill session and cleanup

Steps:

Kill tmux session:

tmux kill-session -t "psm:$session_id" 2>/dev/null


Remove worktree:

worktree_path=$(jq -r ".sessions[\"$session_id\"].worktree" ~/.psm/sessions.json)
source_repo=$(jq -r ".sessions[\"$session_id\"].source_repo" ~/.psm/sessions.json)

cd "$source_repo"
git worktree remove "$worktree_path" --force


Update registry:

# Remove from sessions.json

Subcommand: cleanup

Purpose: Clean up merged PRs and closed issues

Steps:

Read all sessions

For each PR session, check if merged:

gh pr view <pr_number> --repo <repo> --json merged,state


For each issue session, check if closed:

gh issue view <issue_number> --repo <repo> --json closed,state


Clean up merged/closed sessions:

Kill tmux session
Remove worktree
Update registry

Report:

Cleanup complete:
  Removed: omc:pr-123 (merged)
  Removed: omc:issue-42 (closed)
  Kept: omc:feat-auth (active)

Subcommand: status

Purpose: Show current session info

Steps:

Detect current session from tmux or cwd:

tmux display-message -p "#{session_name}" 2>/dev/null
# or check if cwd is inside a worktree


Read session metadata:

cat .psm-session.json 2>/dev/null


Show status:

Current Session: omc:pr-123
Type: review
PR: #123 - Add webhook support
Branch: feature/webhooks
Created: 2 hours ago

Error Handling
Error	Resolution
Worktree exists	Offer: attach, recreate, or abort
PR not found	Verify URL/number, check permissions
No tmux	Warn and skip session creation
No gh CLI	Error with install instructions
Teleport Command

The omc teleport command provides a lightweight alternative to full PSM sessions. It creates git worktrees without tmux session management — ideal for quick, isolated development.

Usage
# Create worktree for an issue or PR
omc teleport #123
omc teleport owner/repo#123
omc teleport https://github.com/owner/repo/issues/42

# Create worktree for a feature
omc teleport my-feature

# List existing worktrees
omc teleport list

# Remove a worktree
omc teleport remove issue/my-repo-123
omc teleport remove --force feat/my-repo-my-feature

Options
Flag	Description	Default
--worktree	Create worktree (default, kept for compatibility)	true
--path <path>	Custom worktree root directory	~/Workspace/omc-worktrees/
--base <branch>	Base branch to create from	main
--json	Output as JSON	false
Worktree Layout
~/Workspace/omc-worktrees/
├── issue/
│   └── my-repo-123/        # Issue worktrees
├── pr/
│   └── my-repo-456/        # PR review worktrees
└── feat/
    └── my-repo-my-feature/ # Feature worktrees

PSM vs Teleport
Feature	PSM	Teleport
Git worktree	Yes	Yes
Tmux session	Yes	No
Claude Code launch	Yes	No
Session registry	Yes	No
Auto-cleanup	Yes	No
Project aliases	Yes	No (uses current repo)

Use PSM for full managed sessions. Use teleport for quick worktree creation.

Requirements

Required:

git - Version control (with worktree support v2.5+)
jq - JSON parsing
tmux - Session management (optional, but recommended)

Optional (per provider):

gh - GitHub CLI (for GitHub workflows)
jira - Jira CLI (for Jira workflows)
Initialization

On first run, create default config:

mkdir -p ~/.psm/worktrees ~/.psm/logs

# Create default projects.json if not exists
if [[ ! -f ~/.psm/projects.json ]]; then
  cat > ~/.psm/projects.json << 'EOF'
{
  "aliases": {
    "omc": {
      "repo": "Yeachan-Heo/oh-my-claudecode",
      "local": "~/Workspace/oh-my-claudecode",
      "default_base": "main"
    }
  },
  "defaults": {
    "worktree_root": "~/.psm/worktrees",
    "cleanup_after_days": 14,
    "auto_cleanup_merged": true
  }
}
EOF
fi

# Create sessions.json if not exists
if [[ ! -f ~/.psm/sessions.json ]]; then
  echo '{"version":1,"sessions":{},"stats":{"total_created":0,"total_cleaned":0}}' > ~/.psm/sessions.json
fi

Weekly Installs
304
Repository
yeachan-heo/oh-…audecode
GitHub Stars
32.3K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn