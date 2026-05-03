---
title: push
url: https://skills.sh/boshu2/agentops/push
---

# push

skills/boshu2/agentops/push
push
Installation
$ npx skills add https://github.com/boshu2/agentops --skill push
SKILL.md
Push Skill

Atomic test-commit-push workflow. Catches failures before they reach the remote.

Steps
Step 1: Detect Project Type

Determine which test suites apply:

Go: Check for go.mod (or cli/go.mod). If found, Go tests apply.
Python: Check for requirements.txt, pyproject.toml, or setup.py. If found, Python tests apply.
Shell: Check for modified .sh files. If found, shellcheck applies (if installed).
Step 2: Run Tests

Run ALL applicable test suites. Do NOT skip any.

Go projects:

cd cli && go vet ./...
cd cli && go test ./... -count=1 -short


Python projects:

python -m pytest --tb=short -q


Shell scripts (if shellcheck available):

shellcheck <modified .sh files>


If ANY test fails: STOP. Fix the failures before continuing. Do not commit broken code.

Step 3: Stage Changes
git add <specific files>


Stage only the files relevant to the current work. Do NOT use git add -A unless the user explicitly requests it. Review untracked files and skip anything that looks like secrets, temp files, or build artifacts.

Step 4: Write Commit Message

Write a conventional commit message based on the diff:

Use conventional commit format: type(scope): description
Types: feat, fix, refactor, docs, test, chore, style, perf
Keep subject line under 72 characters
Focus on WHY, not WHAT
Step 5: Commit
git commit -m "<message>"

Step 6: Sync with Remote
git pull --rebase origin $(git branch --show-current)


If rebase conflicts occur: resolve them, re-run tests, then continue.

Step 7: Push
git push origin $(git branch --show-current)

Step 8: Report

Output a summary:

Files changed count
Tests passed (with suite names)
Commit hash
Branch pushed to
Guardrails
NEVER push to main or master without explicit user confirmation
NEVER stage files matching: .env*, *credentials*, *secret*, *.key, *.pem
If tests were not run (no test suite found), WARN the user before committing
If git pull --rebase fails, do NOT force push — ask the user
Examples
Pushing Changes

User says: /push

What happens:

Runs Go and Python tests
Commits with conventional message
Pushes to current branch

Result: Verified, committed, and pushed changes in one atomic workflow.

Troubleshooting
Problem	Cause	Fix
Tests fail	Code has errors	Fix failing tests before retrying
Push rejected	Remote has new commits	Pull and rebase, then retry
No changes to commit	Working tree is clean	Make changes first
Weekly Installs
95
Repository
boshu2/agentops
GitHub Stars
323
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass