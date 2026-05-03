---
rating: ⭐⭐
title: frontend-dev-tools
url: https://skills.sh/iceywu/skills/frontend-dev-tools
---

# frontend-dev-tools

skills/iceywu/skills/frontend-dev-tools
frontend-dev-tools
Installation
$ npx skills add https://github.com/iceywu/skills --skill frontend-dev-tools
SKILL.md
Frontend Development Tools & Workflow

Use this skill to standardize frontend run/open/preview/debug tasks.

1. Trigger (Hard)

Apply this skill when the user intent includes frontend run/open/preview/debug.

Examples of hard triggers:

English: run, open, preview, debug (frontend project/app/page)
Chinese: 运行、打开、预览、调试（前端项目/页面）
2. Required Flow (MCP First)

For hard-trigger requests, execute in this order:

Start or confirm dev server (for example pnpm dev).
Use MCP browser tools first: mcp_microsoft_pla_browser_* or mcp_chrome-devtoo_*.
Verify at least one visible UI signal (title, heading, or key element).
Report result after verification.

Rules:

If MCP browser tools are available, they are mandatory as the primary path.
Do not finish the task with terminal startup logs only.
3. Fallback Policy

Fallback is allowed only when MCP path is unavailable or failed.

You may use terminal checks and open_simple_browser as fallback.
You must explicitly state the blocker (for example: MCP browser runtime unavailable).
You should attempt recovery first when possible (for example install browser/runtime), then fallback.
4. Quick Example: “运行/打开项目”
Start server (pnpm dev or equivalent).
Open local URL via MCP browser tool.
Verify page signal (e.g., title/h1).
Then return completion status.
Weekly Installs
24
Repository
iceywu/skills
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass