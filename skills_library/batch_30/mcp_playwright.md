---
title: mcp-playwright
url: https://skills.sh/7spade/black-tortoise/mcp-playwright
---

# mcp-playwright

skills/7spade/black-tortoise/mcp-playwright
mcp-playwright
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill mcp-playwright
SKILL.md
MCP Skill: Playwright MCP (UI Verification)
Scope

Use the MCP server configured as microsoft/playwright-mcp in .vscode/mcp.json to run browser automation tasks (navigation, screenshots, DOM checks) during debugging and validation.

Preconditions
Ensure .vscode/mcp.json contains microsoft/playwright-mcp.
Ensure the app is running (typically pnpm run start) if you are testing locally.
Operating Rules
Prefer resilient selectors: data-testid, ARIA roles/labels.
Avoid brittle CSS selectors and deep DOM coupling.
Capture evidence for regressions: screenshots + console errors.
Typical Workflows
Smoke check a route
Navigate to a URL and assert primary heading/landmark is visible.
Regression capture
Take before/after screenshots for a single screen change.
Console hygiene
Collect browser console errors/warnings for a page.
Accessibility spot-check
Verify keyboard focus order for critical controls.
Prompt Templates
"Open and verify . Collect console errors and take a full-page screenshot."
"Run a quick flow: . Use role-based selectors and fail fast with screenshots on error."
Related Repo Guidance
See .github/skills/e2e-playwright for test organization and selector rules.
Weekly Installs
9
Repository
7spade/black-tortoise
First Seen
Feb 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass