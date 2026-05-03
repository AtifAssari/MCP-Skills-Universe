---
title: react-audit-grep-patterns
url: https://skills.sh/github/awesome-copilot/react-audit-grep-patterns
---

# react-audit-grep-patterns

skills/github/awesome-copilot/react-audit-grep-patterns
react-audit-grep-patterns
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill react-audit-grep-patterns
SKILL.md
React Audit Grep Patterns

Complete scan command library for React 18.3.1 and React 19 migration audits.

Usage

Read the relevant section for your target:

references/react18-scans.md - all scans for React 16/17 → 18.3.1 audit
references/react19-scans.md - all scans for React 18 → 19 audit
references/test-scans.md - test file specific scans (used by both auditors)
references/dep-scans.md - dependency and peer conflict scans
Base Patterns Used Across All Scans
# Standard flags used throughout:
# -r = recursive
# -n = show line numbers
# -l = show filenames only (for counting affected files)
# --include="*.js" --include="*.jsx" = JS/JSX files only
# | grep -v "\.test\.\|\.spec\.\|__tests__" = exclude test files
# | grep -v "node_modules" = safety (usually handled by not scanning node_modules)
# 2>/dev/null = suppress "no files found" errors

# Source files only (exclude tests):
SRC_FLAGS='--include="*.js" --include="*.jsx"'
EXCLUDE_TESTS='grep -v "\.test\.\|\.spec\.\|__tests__"'

# Test files only:
TEST_FLAGS='--include="*.test.js" --include="*.test.jsx" --include="*.spec.js" --include="*.spec.jsx"'

Weekly Installs
522
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass