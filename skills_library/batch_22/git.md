---
title: git
url: https://skills.sh/tao3k/omni-dev-fusion/git
---

# git

skills/tao3k/omni-dev-fusion/git
git
Installation
$ npx skills add https://github.com/tao3k/omni-dev-fusion --skill git
SKILL.md
Git Skill (Smart Commit Workflow)

Code is Mechanism, Prompt is Policy

Smart Commit Workflow (Primary Query Anchor)

smart commit is the canonical query phrase for this skill. Use git.smart_commit to run the full smart commit workflow (stage -> scan -> approve -> commit).

Architecture

This skill keeps its runnable command functions in scripts/*.py. Commands are exposed through the retained tool runtime as git.command_name.

Available Commands
Command	Description
git.status	Show working tree status
git.stage_all	Stage all changes (with security scan)
git.commit	Commit staged changes
git.smart_commit	Smart Commit workflow (stage → scan → approve → commit)
git.push	Push to remote
git.log	Show commit logs
Smart Commit Workflow

Use git.smart_commit for secure, human-in-the-loop commits:

# Step 1: Start workflow
git.smart_commit(action="start")
# Returns workflow_id and diff preview

# Step 2: After LLM analysis and user approval
git.smart_commit(action="approve", workflow_id="xxx", message="feat: description")


Flow: stage_and_scan → route_prepare → format_review → re_stage → interrupt → commit

Linked Notes
Related: Smart Commit Workflow Reference
Related: Skill Routing Value Standard
Staged Files Feature
Stage and Scan Workflow

The stage_and_scan function provides automatic staging with security validation:

Stage All Files → Security Scan → Lefthook Pre-commit → Finalize

Key Features

Automatic Staging

stage_and_scan(project_root=".")
# Returns: {staged_files, diff, security_issues, lefthook_error}


Security Scanning

Detects sensitive files (.env*, *.pem, *.key, *.secret, etc.)
Automatically un-stages detected files
Returns list of security issues

Lefthook Integration

Runs pre-commit hooks after staging
Re-stages files modified by lefthook formatters
Returns lefthook output for review
Staged Files Commands
Command	Description
git.stage_all()	Stage all changes with security scan
git.status()	Show staged files and working tree status
git.diff()	Show staged diff
Security Patterns Detected
.env*, *.env*, *.pem, *.key, *.secret, *.credentials*
id_rsa*, id_ed25519*, *.priv
secrets.yml, secrets.yaml, credentials.yml

Usage Guidelines
Read Operations (Safe - Use Claude-native bash)
git status
git diff --cached
git diff
git log --oneline

Write Operations (Use Tool Runtime Calls)
Operation	Tool
Stage all	git.stage_all() (scans for secrets)
Commit	git.commit(message="...")
Push	git.push()
Smart Commit	git.smart_commit(action="start")
Key Principle

Read = Claude-native bash. Write = tool runtime calls.

Weekly Installs
15
Repository
tao3k/omni-dev-fusion
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass