---
title: commit
url: https://skills.sh/odysseus0/symphony/commit
---

# commit

skills/odysseus0/symphony/commit
commit
Installation
$ npx skills add https://github.com/odysseus0/symphony --skill commit
SKILL.md
Commit
Goals
Produce a commit that reflects the actual code changes and the session context.
Follow common git conventions (type prefix, short subject, wrapped body).
Include both summary and rationale in the body.
Inputs
Codex session history for intent and rationale.
git status, git diff, and git diff --staged for actual changes.
Repo-specific commit conventions if documented.
Steps
Read session history to identify scope, intent, and rationale.
Inspect the working tree and staged changes (git status, git diff, git diff --staged).
Stage intended changes, including new files (git add -A) after confirming scope.
Sanity-check newly added files; if anything looks random or likely ignored (build artifacts, logs, temp files), flag it to the user before committing.
If staging is incomplete or includes unrelated files, fix the index or ask for confirmation.
Choose a conventional type and optional scope that match the change (e.g., feat(scope): ..., fix(scope): ..., refactor(scope): ...).
Write a subject line in imperative mood, <= 72 characters, no trailing period.
Write a body that includes:
Summary of key changes (what changed).
Rationale and trade-offs (why it changed).
Tests or validation run (or explicit note if not run).
Append a Co-authored-by trailer for Codex using Codex <codex@openai.com> unless the user explicitly requests a different identity.
Wrap body lines at 72 characters.
Create the commit message with a here-doc or temp file and use git commit -F <file> so newlines are literal (avoid -m with \n).
Commit only when the message matches the staged changes: if the staged diff includes unrelated files or the message describes work that isn't staged, fix the index or revise the message before committing.
Output
A single commit created with git commit whose message reflects the session.
Template

Type and scope are examples only; adjust to fit the repo and changes.

<type>(<scope>): <short summary>

Summary:
- <what changed>
- <what changed>

Rationale:
- <why>
- <why>

Tests:
- <command or "not run (reason)">

Co-authored-by: Codex <codex@openai.com>

Weekly Installs
177
Repository
odysseus0/symphony
GitHub Stars
62
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass