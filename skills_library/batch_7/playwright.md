---
title: playwright
url: https://skills.sh/openai/skills/playwright
---

# playwright

skills/openai/skills/playwright
playwright
Installation
$ npx skills add https://github.com/openai/skills --skill playwright
Summary

Terminal-driven browser automation with element snapshots and interactive UI workflows.

Operates via playwright-cli wrapper script (requires npx); supports headless and headed modes for visual debugging
Core workflow: open page, snapshot for stable element references, interact using refs, re-snapshot after navigation or DOM changes
Includes form filling, clicking, typing, multi-tab management, screenshot/PDF capture, and trace recording for flow debugging
Element refs (e.g., e3, e15) remain valid only until the next significant DOM change; re-snapshot when refs go stale
SKILL.md
Playwright CLI Skill

Drive a real browser from the terminal using playwright-cli. Prefer the bundled wrapper script so the CLI works even when it is not globally installed. Treat this skill as CLI-first automation. Do not pivot to @playwright/test unless the user explicitly asks for test files.

Prerequisite check (required)

Before proposing commands, check whether npx is available (the wrapper depends on it):

command -v npx >/dev/null 2>&1


If it is not available, pause and ask the user to install Node.js/npm (which provides npx). Provide these steps verbatim:

# Verify Node/npm are installed
node --version
npm --version

# If missing, install Node.js/npm, then:
npm install -g @playwright/cli@latest
playwright-cli --help


Once npx is present, proceed with the wrapper script. A global install of playwright-cli is optional.

Skill path (set once)
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export PWCLI="$CODEX_HOME/skills/playwright/scripts/playwright_cli.sh"


User-scoped skills install under $CODEX_HOME/skills (default: ~/.codex/skills).

Quick start

Use the wrapper script:

"$PWCLI" open https://playwright.dev --headed
"$PWCLI" snapshot
"$PWCLI" click e15
"$PWCLI" type "Playwright"
"$PWCLI" press Enter
"$PWCLI" screenshot


If the user prefers a global install, this is also valid:

npm install -g @playwright/cli@latest
playwright-cli --help

Core workflow
Open the page.
Snapshot to get stable element refs.
Interact using refs from the latest snapshot.
Re-snapshot after navigation or significant DOM changes.
Capture artifacts (screenshot, pdf, traces) when useful.

Minimal loop:

"$PWCLI" open https://example.com
"$PWCLI" snapshot
"$PWCLI" click e3
"$PWCLI" snapshot

When to snapshot again

Snapshot again after:

navigation
clicking elements that change the UI substantially
opening/closing modals or menus
tab switches

Refs can go stale. When a command fails due to a missing ref, snapshot again.

Recommended patterns
Form fill and submit
"$PWCLI" open https://example.com/form
"$PWCLI" snapshot
"$PWCLI" fill e1 "user@example.com"
"$PWCLI" fill e2 "password123"
"$PWCLI" click e3
"$PWCLI" snapshot

Debug a UI flow with traces
"$PWCLI" open https://example.com --headed
"$PWCLI" tracing-start
# ...interactions...
"$PWCLI" tracing-stop

Multi-tab work
"$PWCLI" tab-new https://example.com
"$PWCLI" tab-list
"$PWCLI" tab-select 0
"$PWCLI" snapshot

Wrapper script

The wrapper script uses npx --package @playwright/cli playwright-cli so the CLI can run without a global install:

"$PWCLI" --help


Prefer the wrapper unless the repository already standardizes on a global install.

References

Open only what you need:

CLI command reference: references/cli.md
Practical workflows and troubleshooting: references/workflows.md
Guardrails
Always snapshot before referencing element ids like e12.
Re-snapshot when refs seem stale.
Prefer explicit commands over eval and run-code unless needed.
When you do not have a fresh snapshot, use placeholder refs like eX and say why; do not bypass refs with run-code.
Use --headed when a visual check will help.
When capturing artifacts in this repo, use output/playwright/ and avoid introducing new top-level artifact folders.
Default to CLI commands and workflows, not Playwright test specs.
Weekly Installs
2.1K
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail