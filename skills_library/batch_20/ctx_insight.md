---
title: ctx-insight
url: https://skills.sh/mksglu/context-mode/ctx-insight
---

# ctx-insight

skills/mksglu/context-mode/ctx-insight
ctx-insight
Installation
$ npx skills add https://github.com/mksglu/context-mode --skill ctx-insight
SKILL.md
Context Mode Insight

Open the personal analytics dashboard in the browser.

Instructions
Call the ctx_insight MCP tool (no parameters needed, or pass port: 4747 to customize). Optional data-dir overrides: sessionDir/insightSessionDir for INSIGHT_SESSION_DIR, and contentDir/insightContentDir for INSIGHT_CONTENT_DIR.
The tool will:
Copy source files to cache (first run only)
Install dependencies (first run only, ~30s)
Build the dashboard (~1s)
Start a local server
Open the browser
Display the tool's output to the user — it contains progress steps and the dashboard URL.
Tell the user:
"Dashboard is running at http://localhost:4747"
"Refresh the page to see updated metrics"
"Dashboard stops automatically when Claude exits. To stop sooner: kill the PID shown above."
Weekly Installs
88
Repository
mksglu/context-mode
GitHub Stars
11.9K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass