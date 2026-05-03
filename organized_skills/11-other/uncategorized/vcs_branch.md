---
rating: ⭐⭐
title: vcs-branch
url: https://skills.sh/diegocanepa/agent-skills/vcs-branch
---

# vcs-branch

skills/diegocanepa/agent-skills/vcs-branch
vcs-branch
Installation
$ npx skills add https://github.com/diegocanepa/agent-skills --skill vcs-branch
SKILL.md
VCS Branching
Format

<type>/<issue-number>-<short-description>

Types
feat/ - New feature
fix/ - Bug fix
refactor/ - Code refactoring
docs/ - Documentation
test/ - Tests
chore/ - Maintenance
Workflow
Identify: Find the related issue number and platform (GitHub/GitLab).
Drafting:
Use lowercase and kebab-case.
3-6 words for description.
MITM Confirmation: ALWAYS present the drafted branch name to the USER for approval before creation.
Execution:
git checkout main
git pull origin main
git checkout -b <branch-name>

Guidelines
English Only: Branch descriptions must be in English.
Sync: Always pull the latest changes from the base branch before creating a new one.
Weekly Installs
8
Repository
diegocanepa/agent-skills
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass