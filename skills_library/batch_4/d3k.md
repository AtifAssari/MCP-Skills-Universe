---
title: d3k
url: https://skills.sh/vercel-labs/dev3000/d3k
---

# d3k

skills/vercel-labs/dev3000/d3k
d3k
Installation
$ npx skills add https://github.com/vercel-labs/dev3000 --skill d3k
SKILL.md
d3k Standalone Bootstrap

Use this skill when working in a standalone AI app and you need reliable local web debugging with browser + server context.

Why d3k-first
d3k captures server logs, browser console, network events, and screenshots in one timeline.
d3k exposes a stable CDP endpoint so the agent can control the same browser session being monitored.
Running npm run dev or bun run dev directly omits this unified telemetry and usually leads to weaker diagnoses.
Bootstrap Workflow
Confirm whether d3k is installed:
command -v d3k >/dev/null && d3k --version

If d3k is missing, install dev3000 globally (prefer Bun):
bun install -g dev3000


Fallback if Bun is unavailable:

npm install -g dev3000

Start d3k as the runtime (preferred default in agent shells):
d3k --no-agent --no-tui -t

Keep d3k running while editing code. Do not start a second dev server with npm/bun dev.
Codex Fresh Browser/Profile Startup

Use this workflow when the user asks Codex to start d3k with a fresh browser/profile.

Close any stale agent-browser daemon before launching with --profile. Otherwise agent-browser will reuse the existing daemon and print --profile ignored.

d3k agent-browser close --all


Start the app through d3k in servers-only mode and keep that command running. In Codex, this is more reliable than asking d3k to launch the browser itself when a fresh profile is required.

d3k --no-agent --no-skills --servers-only --command "npm run dev -- -H 127.0.0.1 -p 3000" --port 3000 --startup-timeout 90 --no-tui


Adjust the package-manager command and port for the project. Prefer --command over --script when passing framework flags. For npm scripts, put flags after --; otherwise tools like Next.js can interpret the port as a project directory.

Verify the server before opening more browser windows:

curl -I http://127.0.0.1:3000


Open the fresh profile as a separate browser step:

d3k agent-browser --profile /tmp/d3k-fresh-profile --headed open http://127.0.0.1:3000


Sanity-check the opened page:

d3k agent-browser get title
d3k agent-browser snapshot -i
d3k errors


Practical rules:

Prefer 127.0.0.1 for this workflow. If localhost hangs or flips between IPv4/IPv6 behavior, do not keep retrying browser launches.
If curl -I hangs, the server is wedged even if the port appears occupied; restart the d3k server process before opening a browser.
In servers-only mode there is no d3k-monitored CDP browser. Use regular d3k agent-browser commands, not d3k cdp-port.
In sandboxed agent environments, rerun local-network checks and agent-browser opens outside the sandbox when sandbox networking blocks access to 127.0.0.1.
Debugging Commands

Use these first before ad-hoc log scraping:

d3k errors --context
d3k logs -n 200
d3k logs --type browser
d3k logs --type server

CDP Browser Control

Use the already-monitored browser session instead of launching a separate automation browser.

CDP_PORT="$(d3k cdp-port)"
d3k agent-browser --cdp "$CDP_PORT" open http://localhost:3000
d3k agent-browser --cdp "$CDP_PORT" snapshot -i
d3k agent-browser --cdp "$CDP_PORT" click @e2
d3k agent-browser --cdp "$CDP_PORT" screenshot /tmp/d3k-current.png

Browser Tool Choice

Use the browser tool that matches the task instead of treating them as interchangeable:

agent-browser
Default choice.
Best for generic web apps and for driving the exact headed browser session that d3k is already monitoring via CDP.
Use it when you need snapshot, ref-based click, fill, or to reproduce what the user sees in the monitored tab.
next-browser
Next.js-specific tool.
Best for React/Next introspection: tree, errors, logs, routes, project, PPR inspection, and related Next dev-server signals.
It is not a drop-in replacement for agent-browser: no accessibility snapshot, no ref-based click, and no fill.
It launches its own daemon/browser flow and does not use d3k cdp-port.

Practical rule:

Need to drive the same browser d3k is monitoring: use agent-browser.
Need Next.js component tree or Next-specific diagnostics: use next-browser.

Examples:

# Same monitored browser session
CDP_PORT="$(d3k cdp-port)"
d3k agent-browser --cdp "$CDP_PORT" snapshot -i
d3k agent-browser --cdp "$CDP_PORT" click @e2

# Next.js-specific inspection
d3k next-browser open http://localhost:3000
d3k next-browser tree
d3k next-browser errors
d3k next-browser logs

Artifacts to Read
~/.d3k/{project}/d3k.log
~/.d3k/{project}/logs/
~/.d3k/{project}/screenshots/
~/.d3k/{project}/session.json
Operating Rules
Prefer headed mode for interactive debugging.
Use --headless only for CI or when explicitly requested.
Use --servers-only only when browser monitoring is intentionally disabled.
Weekly Installs
422
Repository
vercel-labs/dev3000
GitHub Stars
1.2K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn