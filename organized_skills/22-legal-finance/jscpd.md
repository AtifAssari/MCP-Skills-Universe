---
rating: ⭐⭐
title: jscpd
url: https://skills.sh/knoopx/pi/jscpd
---

# jscpd

skills/knoopx/pi/jscpd
jscpd
Installation
$ npx skills add https://github.com/knoopx/pi --skill jscpd
SKILL.md
jscpd

Copy-paste detector for JavaScript, TypeScript, and many other languages.

Quick Start
# With ignore patterns
bunx jscpd --ignore "**/node_modules/**,**/dist/**" <path>


Common Options
Option	Description
--min-tokens N	Minimum tokens for duplicate detection
--min-lines N	Minimum lines for duplicate detection
--threshold N	Fail if duplication % exceeds threshold
--ignore "glob"	Ignore patterns (comma-separated)
--reporters type	Output format: console, json, html
--output path	Output directory for reports
--silent	Suppress console output
Workflow
Run jscpd to find duplicates
Review the reported duplicates
Refactor to eliminate duplication
Re-run to verify cleanup
Related Skills
maintenance: Refactoring and technical debt management
design: DRY principle violations
ast-grep: Structural refactoring of duplicated patterns
Weekly Installs
45
Repository
knoopx/pi
GitHub Stars
45
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass