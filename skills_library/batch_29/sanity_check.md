---
title: sanity-check
url: https://skills.sh/chmouel/lazyworktree/sanity-check
---

# sanity-check

skills/chmouel/lazyworktree/sanity-check
sanity-check
Installation
$ npx skills add https://github.com/chmouel/lazyworktree --skill sanity-check
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Sanity Check

Run comprehensive quality checks and report results.

Current Git Status

!git status --short

Lint Results

!make lint 2>&1 | head -30

Test Results

!go test ./... -short 2>&1 | tail -20

Coverage

!go test ./... -cover 2>&1 | grep coverage

Analyse these results and report:

Any blocking issues that must be fixed
Files that need attention
Coverage gaps in tested packages
Summary of overall project health
Weekly Installs
43
Repository
chmouel/lazyworktree
GitHub Stars
215
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass