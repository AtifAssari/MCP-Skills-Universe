---
title: gh-create-pr
url: https://skills.sh/lwlee2608/agent-skills/gh-create-pr
---

# gh-create-pr

skills/lwlee2608/agent-skills/gh-create-pr
gh-create-pr
Installation
$ npx skills add https://github.com/lwlee2608/agent-skills --skill gh-create-pr
SKILL.md
Create a GitHub Pull Request

Create PRs with short, feature-focused descriptions. No test plan or co-author lines.

Rules
Create the PR using gh pr create with a HEREDOC body:
gh pr create --title "<short title>" --body "$(cat <<'EOF'

Summary

<bullet points describing the main features/changes, proportional to PR size> EOF )"

2. **Title**: Use imperative mood (e.g., "Add user auth", "Fix pagination bug").
3. **Description**: Only a `## Summary` section with bullet points proportional to the PR size.
4. **No test plan**: Do not add a test plan, checklist, or QA section.
5. **No co-author**: Do not add "Co-Authored-By" lines.

Weekly Installs
26
Repository
lwlee2608/agent-skills
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass