---
rating: ⭐⭐⭐
title: openai-playwright
url: https://skills.sh/trailofbits/skills-curated/openai-playwright
---

# openai-playwright

skills/trailofbits/skills-curated/openai-playwright
openai-playwright
Installation
$ npx skills add https://github.com/trailofbits/skills-curated --skill openai-playwright
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

Scripts and references are located under {baseDir}/.

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
When to Use
When NOT to Use
Weekly Installs
31
Repository
trailofbits/ski…-curated
GitHub Stars
381
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail