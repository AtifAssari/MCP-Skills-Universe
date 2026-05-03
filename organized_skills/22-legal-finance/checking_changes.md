---
rating: ⭐⭐
title: checking-changes
url: https://skills.sh/streamlit/streamlit/checking-changes
---

# checking-changes

skills/streamlit/streamlit/checking-changes
checking-changes
Installation
$ npx skills add https://github.com/streamlit/streamlit --skill checking-changes
SKILL.md
Checking Changes

Run at the end of a work session or after completing a set of changes — not after every small edit.

make check


This runs formatting, linting, type checking, and unit tests on all uncommitted files (staged, unstaged, and untracked).

Workflow
Run make check
If issues are found:
Fix the reported errors
Re-run make check
Repeat until all checks pass
Only consider work complete when make check succeeds
Notes
E2E tests are not included by default; use E2E_CHECK=true make check to also run changed e2e tests
E2E snapshot mismatches can be ignored (they require manual updates)
Weekly Installs
89
Repository
streamlit/streamlit
GitHub Stars
44.4K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass