---
rating: ⭐⭐⭐
title: update-pr
url: https://skills.sh/willbooster/agent-skills/update-pr
---

# update-pr

skills/willbooster/agent-skills/update-pr
update-pr
Installation
$ npx skills add https://github.com/willbooster/agent-skills --skill update-pr
SKILL.md
Update PR workflow

Write the full replacement pull request title and the complete replacement PR body so they reflect the current scope, motivation, and validation. Run update-pr with the title as the first argument and the body on stdin. Finally, report the pull request URL.

bunx @willbooster/agent-skills@latest update-pr "feat: concise PR title" <<'EOF'
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
37
Repository
willbooster/agent-skills
GitHub Stars
1
First Seen
10 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn