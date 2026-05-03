---
title: qa-web-test
url: https://skills.sh/delexw/claude-code-misc/qa-web-test
---

# qa-web-test

skills/delexw/claude-code-misc/qa-web-test
qa-web-test
Installation
$ npx skills add https://github.com/delexw/claude-code-misc --skill qa-web-test
SKILL.md
QA Web Testing with PinchTab

Uses Skill("pinchtab") for all browser interaction — navigation, screenshots, viewport emulation, and DOM inspection. Describe what you need and let pinchtab handle the details.

Inputs

Raw arguments: $ARGUMENTS

Infer from the arguments:

TARGET_URL: the URL to test
OUT_DIR: output directory for QA report and screenshots, or ./qa-reports if not provided
Output Location
Creates or updates OUT_DIR/qa-report-{timestamp}.md
Screenshots are saved to OUT_DIR/screenshots/
Run mkdir -p OUT_DIR/screenshots before writing to ensure directories exist.
Workflow

Follow these steps in order. Read each step file for detailed instructions.

Connect and navigate — Navigate to target URL (includes auth check and login if needed)
Determine breakpoints — Choose viewport widths to test
Emulate and capture — Set viewport, screenshot, inspect dimensions
CSS inspection — Inspect computed styles and container queries
Visual design inspection — Check typography, color, spacing, borders, and visibility
Report results — Summarize findings with pass/fail table
Reference Files
Reference	When to Read
references/breakpoints.md	Common breakpoint values, container query vs media query gotchas
references/css-inspection.md	JS snippets for overflow detection, grid/flex inspection, DOM traversal
Weekly Installs
43
Repository
delexw/claude-code-misc
GitHub Stars
1
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn