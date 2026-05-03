---
title: pr-workflow
url: https://skills.sh/fcakyon/claude-codex-settings/pr-workflow
---

# pr-workflow

skills/fcakyon/claude-codex-settings/pr-workflow
pr-workflow
Installation
$ npx skills add https://github.com/fcakyon/claude-codex-settings --skill pr-workflow
SKILL.md
Pull Request Workflow

Complete workflow for creating pull requests following project standards.

Process

Verify staged changes exist with git diff --cached --name-only

Branch setup

If on main/master, create feature branch first: feature/brief-description or fix/brief-description
Use github-dev:commit-creator subagent to handle staged changes if needed

Documentation check

Update README.md or docs based on changes compared to target branch
For config/API changes, use mcp__tavily__tavily_search to verify info and include sources

Analyze all commits

Use git diff <base-branch>...HEAD to review complete changeset
PR message must describe all commits, not just latest
Focus on what changed from reviewer perspective

Create PR

Use /pr-creator agent or gh pr create with parameters:
-t (title): Start with capital letter, use verb, NO "fix:" or "feat:" prefix
-b (body): Brief summary + bullet points with inline markdown links
-a @me (self-assign)
-r <reviewer>: Only add if the user explicitly asks OR recent PRs by this author have reviewers. Check with: gh pr list --repo <owner>/<repo> --author @me --limit 5 --json reviewRequests If recent PRs have no reviewers, skip -r entirely.

PR Body Guidelines

Single section, no headers if possible. Very concise
Few bullet points + 1 CLI/usage snippet or simple before/after snippet
No test plans, no changed file lists, no line-number links
Examples
CLI snippet:
Add compare command for side-by-side model comparison

- Run multiple models on same images with `--models` and `--phrases` flags
- Horizontal panel concatenation with model name headers

`ultrannotate compare --source ./images --models sam3.pt,yoloe-26x-seg.pt --phrases "person,car"`

Before/after:
Inline single-use variables in compare_models

- xyxy2xywhn handles empty arrays, guard unnecessary
- Use function reference for draw dispatch

Before: `boxes = result.get(...); ops.xyxy2xywhn(boxes, ...)`
After: `ops.xyxy2xywhn(result.get(...), ...)`

Weekly Installs
47
Repository
fcakyon/claude-…settings
GitHub Stars
657
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass