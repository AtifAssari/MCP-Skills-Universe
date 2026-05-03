---
title: commit
url: https://skills.sh/sebkay/skills/commit
---

# commit

skills/sebkay/skills/commit
commit
Installation
$ npx skills add https://github.com/sebkay/skills --skill commit
SKILL.md
Commit Changes

Create one focused commit for the work that is ready now.

Workflow
Inspect the working tree with git status --short.
Identify the files and hunks that belong to the requested unit of work.
Leave unrelated, pre-existing, or uncertain changes unstaged. If the scope is ambiguous, ask before committing.
Stage only the relevant files or hunks.
Review the staged diff with git diff --cached --stat and git diff --cached.
Write a concise imperative subject line that describes the change.
Create a single commit with no body unless the user explicitly asks for one.
Guardrails
Prefer the user's requested commit message when they provide one.
Do not create empty commits.
Do not use --no-verify, amend an existing commit, or bundle unrelated changes unless the user explicitly asks.
If hooks or commit validation fail, surface the failure instead of bypassing it.
Weekly Installs
15
Repository
sebkay/skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass