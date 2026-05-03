---
title: agent-browser
url: https://skills.sh/supercent-io/skills-template/agent-browser
---

# agent-browser

skills/supercent-io/skills-template/agent-browser
agent-browser
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill agent-browser
Summary

Deterministic browser automation for AI agents with snapshot-based element references and multi-session support.

Interact with web pages using stable element refs (@e1, @e2, etc.) generated from snapshots, enabling reliable automation across DOM changes
Core commands cover navigation, form filling, clicking, waiting, screenshots, PDFs, and visual regression testing via baseline comparison
Supports parallel isolated sessions, network-aware waits (networkidle), and selector-based targeting for dynamic single-page applications
Optional hardening includes domain allowlists, action policies, and content boundaries to reduce injection risk in sensitive workflows
SKILL.md
agent-browser - Browser Automation for AI Agents
When to use this skill
Open websites and automate UI actions
Fill forms, click controls, and verify outcomes
Capture screenshots/PDFs or extract content
Run deterministic web checks with accessibility refs
Execute parallel browser tasks via isolated sessions
Core workflow

Always use the deterministic ref loop:

agent-browser open <url>
agent-browser snapshot -i
interact with refs (@e1, @e2, ...)
agent-browser snapshot -i again after page/DOM changes
agent-browser open https://example.com/form
agent-browser wait --load networkidle
agent-browser snapshot -i
agent-browser fill @e1 "user@example.com"
agent-browser click @e2
agent-browser snapshot -i

Command patterns

Use && chaining when intermediate output is not needed.

# Good chaining: open -> wait -> snapshot
agent-browser open https://example.com && agent-browser wait --load networkidle && agent-browser snapshot -i

# Separate calls when output is needed first
agent-browser snapshot -i
# parse refs
agent-browser click @e2


High-value commands:

Navigation: open, close
Snapshot: snapshot -i, snapshot -i -C, snapshot -s "#selector"
Interaction: click, fill, type, select, check, press
Verification: diff snapshot, diff screenshot --baseline <file>
Capture: screenshot, screenshot --annotate, pdf
Wait: wait --load networkidle, wait <selector|@ref|ms>
Verification patterns

Use explicit evidence after actions.

# Baseline -> action -> verify structure
agent-browser snapshot -i
agent-browser click @e3
agent-browser diff snapshot

# Visual regression
agent-browser screenshot baseline.png
agent-browser click @e5
agent-browser diff screenshot --baseline baseline.png

Safety and reliability
Refs are invalid after navigation or significant DOM updates; re-snapshot before next action.
Prefer wait --load networkidle or selector/ref waits over fixed sleeps.
For multi-step JS, use eval --stdin (or base64) to avoid shell escaping breakage.
For concurrent tasks, isolate with --session <name>.
Use output controls in long pages to reduce context flooding.
Optional hardening in sensitive flows: domain allowlist and action policies.

Optional hardening examples:

# Wrap page content with boundaries to reduce prompt-injection risk
export AGENT_BROWSER_CONTENT_BOUNDARIES=1

# Limit output volume for long pages
export AGENT_BROWSER_MAX_OUTPUT=50000

# Restrict navigation and network to trusted domains
export AGENT_BROWSER_ALLOWED_DOMAINS="example.com,*.example.com"

# Restrict allowed action types
export AGENT_BROWSER_ACTION_POLICY=./policy.json


Example policy.json:

{"default":"deny","allow":["navigate","snapshot","click","fill","scroll","wait","get"],"deny":["eval","download","upload","network","state"]}


CLI-flag equivalent:

agent-browser --content-boundaries --max-output 50000 --allowed-domains "example.com,*.example.com" --action-policy ./policy.json open https://example.com

Troubleshooting
command not found: install and run agent-browser install.
Wrong element clicked: run snapshot -i again and use fresh refs.
Dynamic SPA content missing: wait with --load networkidle or targeted wait selector.
Session collisions: assign unique --session names and close each session.
Large output pressure: narrow snapshots (-i, -c, -d, -s) and extract only needed text.
References

Deep-dive docs in this skill:

commands
snapshot-refs
session-management
authentication

Related resources:

https://github.com/vercel-labs/agent-browser
https://agent-browser.dev

Ready templates:

./templates/form-automation.sh
./templates/capture-workflow.sh
Metadata
Version: 1.1.0
Last updated: 2026-02-26
Scope: deterministic browser automation for agent workflows
Weekly Installs
10.5K
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn