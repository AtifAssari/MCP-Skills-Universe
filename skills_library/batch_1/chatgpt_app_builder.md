---
title: chatgpt-app-builder
url: https://skills.sh/alpic-ai/skybridge/chatgpt-app-builder
---

# chatgpt-app-builder

skills/alpic-ai/skybridge/chatgpt-app-builder
chatgpt-app-builder
Installation
$ npx skills add https://github.com/alpic-ai/skybridge --skill chatgpt-app-builder
SKILL.md
Creating Apps For LLMs

ChatGPT apps are conversational experiences that extend ChatGPT through tools and custom UI views. They're built as MCP servers invoked during conversations.

⚠️ The app is consumed by two users at once: the human and the ChatGPT LLM. They collaborate through the view—the human interacts with it, the LLM sees its state. Internalize this before writing code: the view is your shared surface.

SPEC.md keeps track of the app's requirements and design decisions. Keep it up to date as you work on the app.

No SPEC.md? → Read discover.md first. Nothing else until SPEC.md exists.

SPEC.md exists? → Read SPEC.md, then follow architecture.md to design the change. Update SPEC.md, then read the relevant Implementation references below before writing code.

Setup
Copy template → copy-template.md: when starting a new project with ready SPEC.md
Run locally → run-locally.md: when ready to test, need dev server or ChatGPT connection
Architecture

Design or evolve UX flows and API shape → architecture.md

Implementation
Fetch and render data → fetch-and-render-data.md: when implementing server handlers and view data fetching
State and context → state-and-context.md: when persisting view UI state and updating LLM context
Prompt LLM → prompt-llm.md: when view needs to trigger LLM response
UI guidelines → ui-guidelines.md: display modes, layout constraints, theme, device, and locale
External links → open-external-links.md: when redirecting to external URLs or setting "open in app" target
OAuth → oauth.md: when tools need user authentication to access user-specific data
CSP → csp.md: when declaring allowed domains for fetch, assets, redirects, or iframes
Deploy
Ship to production → deploy.md: when ready to deploy via Alpic
Publish to ChatGPT Directory → publish.md: when ready to submit for review

Full API docs: https://docs.skybridge.tech/api-reference.md

Weekly Installs
2.0K
Repository
alpic-ai/skybridge
GitHub Stars
1.1K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass