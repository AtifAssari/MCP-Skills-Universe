---
title: create-pr
url: https://skills.sh/jmerta/codex-skills/create-pr
---

# create-pr

skills/jmerta/codex-skills/create-pr
create-pr
Installation
$ npx skills add https://github.com/jmerta/codex-skills --skill create-pr
SKILL.md
Create a PR
Goal

Produce a PR that’s easy to review and safe to merge:

small, scoped changes
green checks (lint/tests/build as appropriate)
clear description + validation steps
Workflow (checklist)
Confirm scope
Restate the goal and acceptance criteria.
Identify files likely to change; avoid unrelated cleanup.
Create a branch
Use a descriptive name: fix/<topic>, feat/<topic>, chore/<topic>.
Implement changes
Keep diffs focused; prefer small commits.
Run quality gates
Run the repo’s standard commands (lint/tests/build).
If bun.lock exists, prefer bun lint / bun build.
If bun.lock exists but bun is not available, tell the user and ask whether to install bun or use the repo’s alternative package manager.
Commit
Prefer Conventional Commits: fix: ..., feat: ..., chore: ....
Push + open PR
Always use GitHub CLI (gh) for PR workflows (e.g. gh pr create --fill).
If gh is not authenticated, run gh auth login (or gh auth status to check).
If gh is not installed or cannot be authenticated, tell the user and ask whether to install/authenticate or proceed with manual PR creation steps.
Fill in PR body
Use references/pr-description-template.md.
Notes
Don't force-push unless you're sure it's safe for collaborators.
If the PR changes UX, include screenshots or a short GIF.
Prefer gh for create/view/checks (e.g. gh pr view, gh pr checks).
Deliverable

Provide:

Branch name and PR URL (or the exact steps to open it manually).
PR title/body (using references/pr-description-template.md).
Commits included and verification commands run.
Screenshots/GIFs if UX changed.
Weekly Installs
18
Repository
jmerta/codex-skills
GitHub Stars
126
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass