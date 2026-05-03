---
title: building-python-communities
url: https://skills.sh/wdm0006/python-skills/building-python-communities
---

# building-python-communities

skills/wdm0006/python-skills/building-python-communities
building-python-communities
Installation
$ npx skills add https://github.com/wdm0006/python-skills --skill building-python-communities
SKILL.md
Python Library Community Management
Essential Files
CONTRIBUTING.md
# Contributing

## Development Setup

git clone https://github.com/user/package.git
cd package
pip install -e ".[dev]"
pre-commit install
pytest

## Making Changes

1. Create a branch: `git checkout -b feature/name`
2. Make changes, add tests
3. Run: `make test && make lint`
4. Commit and open a PR

## Commit Messages

- `Add:` new feature
- `Fix:` bug fix
- `Update:` enhancement
- `Docs:` documentation

CODE_OF_CONDUCT.md

Use Contributor Covenant - the standard for open source.

Issue Templates

.github/ISSUE_TEMPLATE/bug_report.md:

---
name: Bug Report
labels: 'bug'
---
## Description
## To Reproduce
## Expected vs Actual Behavior
## Environment (OS, Python version, package version)
## Minimal Reproducible Example


.github/ISSUE_TEMPLATE/feature_request.md:

---
name: Feature Request
labels: 'enhancement'
---
## Problem Statement
## Proposed Solution
## Example Usage

PR Template

.github/PULL_REQUEST_TEMPLATE.md:

## Description
## Related Issue (Fixes #)
## Checklist
- [ ] Tests added
- [ ] Documentation updated
- [ ] CHANGELOG entry added

GitHub Actions Automation
# .github/workflows/welcome.yml
on:
  pull_request_target:
    types: [opened]
jobs:
  welcome:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/first-interaction@v1
        with:
          pr-message: "Thanks for your first PR! 🎉"

Labels
good first issue - Newcomer-friendly
help wanted - Extra attention needed
bug, enhancement, documentation

For detailed templates, see:

TEMPLATES.md - Full issue/PR templates
GOVERNANCE.md - Project governance guide
Checklist
Initial Setup:
- [ ] CONTRIBUTING.md
- [ ] CODE_OF_CONDUCT.md
- [ ] Issue templates
- [ ] PR template
- [ ] Labels defined

Ongoing:
- [ ] Respond to issues within 48h
- [ ] Review PRs within 1 week
- [ ] Maintain good first issues
- [ ] Recognize contributors

Learn More

This skill is based on the Maintenance section of the Guide to Developing High-Quality Python Libraries by Will McGinnis. See these posts for deeper coverage:

Building Engaging Community
Inner Source Introduction
Building Internal Library Community
From Silos to Shared Libraries
Cursor for Library Maintenance
Weekly Installs
15
Repository
wdm0006/python-skills
GitHub Stars
24
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass