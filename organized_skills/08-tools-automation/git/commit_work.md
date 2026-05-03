---
rating: ⭐⭐
title: commit-work
url: https://skills.sh/softaworks/agent-toolkit/commit-work
---

# commit-work

skills/softaworks/agent-toolkit/commit-work
commit-work
Installation
$ npx skills add https://github.com/softaworks/agent-toolkit --skill commit-work
Summary

Create logical, well-described git commits with staged review and Conventional Commits formatting.

Guides you through inspecting changes, deciding commit boundaries, and staging only intended modifications using patch mode when needed
Enforces Conventional Commits format (type, scope, subject, body, footer) with clear separation of what changed and why
Includes a pre-commit checklist covering secrets detection, accidental debug code, and unrelated formatting to catch issues before shipping
Splits mixed changes across files or within single files by feature, backend/frontend, logic/tests, and dependency updates to keep commits logically scoped
SKILL.md
Commit work
Goal

Make commits that are easy to review and safe to ship:

only intended changes are included
commits are logically scoped (split when needed)
commit messages describe what changed and why
Inputs to ask for (if missing)
Single commit or multiple commits? (If unsure: default to multiple small commits when there are unrelated changes.)
Commit style: Conventional Commits are required.
Any rules: max subject length, required scopes.
Workflow (checklist)
Inspect the working tree before staging
git status
git diff (unstaged)
If many changes: git diff --stat
Decide commit boundaries (split if needed)
Split by: feature vs refactor, backend vs frontend, formatting vs logic, tests vs prod code, dependency bumps vs behavior changes.
If changes are mixed in one file, plan to use patch staging.
Stage only what belongs in the next commit
Prefer patch staging for mixed changes: git add -p
To unstage a hunk/file: git restore --staged -p or git restore --staged <path>
Review what will actually be committed
git diff --cached
Sanity checks:
no secrets or tokens
no accidental debug logging
no unrelated formatting churn
Describe the staged change in 1-2 sentences (before writing the message)
"What changed?" + "Why?"
If you cannot describe it cleanly, the commit is probably too big or mixed; go back to step 2.
Write the commit message
Use Conventional Commits (required):
type(scope): short summary
blank line
body (what/why, not implementation diary)
footer (BREAKING CHANGE) if needed
Prefer an editor for multi-line messages: git commit -v
Use references/commit-message-template.md if helpful.
Run the smallest relevant verification
Run the repo's fastest meaningful check (unit tests, lint, or build) before moving on.
Repeat for the next commit until the working tree is clean
Deliverable

Provide:

the final commit message(s)
a short summary per commit (what/why)
the commands used to stage/review (at minimum: git diff --cached, plus any tests run)
Weekly Installs
3.6K
Repository
softaworks/agent-toolkit
GitHub Stars
1.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass