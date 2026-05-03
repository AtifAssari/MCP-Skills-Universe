---
title: gate
url: https://skills.sh/iankiku/forwward-teams/gate
---

# gate

skills/iankiku/forwward-teams/gate
gate
Installation
$ npx skills add https://github.com/iankiku/forwward-teams --skill gate
SKILL.md
Gate — Self-Healing Verification

Run checks, read errors, fix them, repeat. Prove code WORKS by executing it.

Anti-Shortcut Rules
NEVER declare PASS from reading source. Execute and observe output.
NEVER declare PASS without command output. "It should work" is not evidence.
If a check can't execute, report BLOCKED — never fake PASS.
Step 0: Get Commands

Read .claude/project.json for build commands. If missing, init from the plugin CLI:

${CLAUDE_PLUGIN_ROOT}/scripts/cli init


Or run checks directly via the plugin CLI:

${CLAUDE_PLUGIN_ROOT}/scripts/cli gate        # lint + typecheck + build + test
${CLAUDE_PLUGIN_ROOT}/scripts/cli gatekeep -g  # same, with PASS/FAIL report
${CLAUDE_PLUGIN_ROOT}/scripts/cli gatekeep -l  # lint only
${CLAUDE_PLUGIN_ROOT}/scripts/cli gatekeep -t  # test only

The Loop

Run up to 4 iterations:

Execute: lint → typecheck → build → test
All pass? → GATE PASSED — stop.
Any fail? → Read full error, fix it, run again.
Fix Rules
Error Type	Fix	Don't
Type errors	Fix the type, add the import	Use @ts-ignore
Build errors	Fix imports, exports, modules	Skip the check
Lint errors	Fix the actual issue	Blanket disable
Test failures	Fix the code or the test	Delete the test

NEVER change business logic during gate. Only fix types, imports, lint.

Circuit Breaker

After 4 iterations without full pass:

Report which checks still fail with last error output
Do NOT fake a PASS
Inform user or team lead
CLI Reference
Flag	What
-l	Lint only
-c	Typecheck only
-b	Build only
-t	Tests only
-a	App startup (dev server + health check)
-u	UI tests (Playwright/Cypress)
-g	Full gate: lint + typecheck + build + test
--all	Everything including app + UI
Weekly Installs
20
Repository
iankiku/forwward-teams
GitHub Stars
14
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass