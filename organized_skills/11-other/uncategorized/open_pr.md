---
rating: ⭐⭐⭐
title: open-pr
url: https://skills.sh/willbooster/agent-skills/open-pr
---

# open-pr

skills/willbooster/agent-skills/open-pr
open-pr
Installation
$ npx skills add https://github.com/willbooster/agent-skills --skill open-pr
SKILL.md
Open PR workflow

Commit your changes and push them to the current branch. Write a PR body that helps reviewers quickly understand the scope, motivation, and validation. Include the linked issue when applicable, a concise summary of the changes, the reasoning behind them, and how they were tested. Run the following command to open a pull request. Finally, report the PR URL.

bunx @willbooster/agent-skills@latest open-pr "feat: concise PR title" <<'EOF'
Close #<issue>

## Summary

- What changed
- Key scope or affected area
- Any notable tradeoff or limitation

## Why

- Problem being solved
- Reason this approach was chosen

## Testing

- Exact commands run
- Manual verification steps if relevant

## Notes (if needed)

- Breaking changes, rollout concerns, screenshots, or follow-up work
EOF


Note that the prefix of the PR title must follow the Conventional Commits specification:

feat: A new feature for the user or API.
fix: A bug fix for the user or API.
build: Changes that affect the build system or external dependencies (e.g., npm, webpack, typescript).
chore: Routine tasks, maintenance, or tooling changes that don't modify source or test files.
ci: Changes to CI/CD configuration files and scripts.
docs: Documentation-only changes.
perf: A code change that improves performance.
refactor: A code change that neither fixes a bug nor adds a feature, but improves code structure or readability.
style: Changes that do not affect the meaning of the code (e.g., formatting).
test: Adding missing tests or correcting existing tests.
Weekly Installs
49
Repository
willbooster/agent-skills
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn