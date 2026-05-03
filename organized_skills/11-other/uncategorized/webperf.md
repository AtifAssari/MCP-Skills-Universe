---
rating: ⭐⭐
title: webperf
url: https://skills.sh/nucliweb/webperf-snippets/webperf
---

# webperf

skills/nucliweb/webperf-snippets/webperf
webperf
Installation
$ npx skills add https://github.com/nucliweb/webperf-snippets --skill webperf
SKILL.md
WebPerf Snippets Toolkit

A collection of 49 JavaScript snippets for measuring and debugging web performance in Chrome DevTools. Each snippet runs in the browser console and outputs structured, color-coded results.

Quick Reference
Skill	Snippets	Trigger phrases
webperf-core-web-vitals	7	"debug LCP", "slow LCP", "CLS", "layout shifts", "INP", "interaction latency", "responsiveness"
webperf-loading	29	"TTFB", "slow server", "FCP", "render blocking", "font loading", "script loading", "resource hints", "service worker"
webperf-interaction	8	"jank", "scroll performance", "long tasks", "animation frames", "INP debug"
webperf-media	3	"image audit", "lazy loading", "image optimization", "video audit"
webperf-resources	1	"network quality", "bandwidth", "connection type", "save-data"
Workflow
Identify the relevant skill based on the user's question (see Quick Reference above)
Load the skill's skill.md to see available snippets and thresholds
Execute with Chrome DevTools MCP:
mcp__chrome-devtools__navigate_page → navigate to target URL
mcp__chrome-devtools__evaluate_script → run the snippet
mcp__chrome-devtools__get_console_message → read results
Interpret results using the thresholds defined in the skill
Provide actionable recommendations based on findings
Weekly Installs
110
Repository
nucliweb/webper…snippets
GitHub Stars
1.4K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn