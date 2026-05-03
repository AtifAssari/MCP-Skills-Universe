---
title: cloud
url: https://skills.sh/browser-use/browser-use/cloud
---

# cloud

skills/browser-use/browser-use/cloud
cloud
Installation
$ npx skills add https://github.com/browser-use/browser-use --skill cloud
SKILL.md
Browser Use Cloud Reference

Reference docs for the Cloud REST API, SDKs, and integration patterns. Read the relevant file based on what the user needs.

API & Platform
Topic	Read
Setup, first task, pricing, FAQ	references/quickstart.md
v2 REST API: all 30 endpoints, cURL examples, schemas	references/api-v2.md
v3 BU Agent API: sessions, messages, files, workspaces	references/api-v3.md
Sessions, profiles, auth strategies, 1Password	references/sessions.md
CDP direct access, Playwright/Puppeteer/Selenium	references/browser-api.md
Proxies, webhooks, workspaces, skills, MCP, live view	references/features.md
Parallel, streaming, geo-scraping, tutorials	references/patterns.md
Integration Guides
Topic	Read
Building a chat interface with live browser view	references/guides/chat-ui.md
Using browser-use as a subagent (task in → result out)	references/guides/subagent.md
Adding browser-use tools to an existing agent	references/guides/tools-integration.md
Critical Notes
Cloud API base URL: https://api.browser-use.com/api/v2/ (v2) or https://api.browser-use.com/api/v3 (v3)
Auth header: X-Browser-Use-API-Key: <key>
Get API key: https://cloud.browser-use.com/new-api-key
Set env var: BROWSER_USE_API_KEY=<key>
Cloud SDK: uv pip install browser-use-sdk (Python) or npm install browser-use-sdk (TypeScript)
Python v2: from browser_use_sdk import AsyncBrowserUse
Python v3: from browser_use_sdk.v3 import AsyncBrowserUse
TypeScript v2: import { BrowserUse } from "browser-use-sdk"
TypeScript v3: import { BrowserUse } from "browser-use-sdk/v3"
CDP WebSocket: wss://connect.browser-use.com?apiKey=KEY&proxyCountryCode=us
Weekly Installs
965
Repository
browser-use/browser-use
GitHub Stars
91.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn