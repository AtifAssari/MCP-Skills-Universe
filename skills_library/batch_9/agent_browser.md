---
title: agent-browser
url: https://skills.sh/vercel-labs/agent-browser/agent-browser
---

# agent-browser

skills/vercel-labs/agent-browser/agent-browser
agent-browser
Installation
$ npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser
Summary

Fast, persistent browser automation with session continuity across sequential agent commands.

Supports three browser modes: headless Chromium, real Chrome with profile support, and cloud-hosted remote browsers with proxy configuration
Includes 15+ command categories covering navigation, page inspection, interactions, data extraction, cookie management, and JavaScript execution
Offers cloud session management, local server tunneling via Cloudflare, and parallel subagent execution through remote sessions
Built-in Python integration for setting variables, accessing the browser object, and running scripts within the automation context
SKILL.md
agent-browser

Fast browser automation CLI for AI agents. Chrome/Chromium via CDP with accessibility-tree snapshots and compact @eN element refs.

Install: npm i -g agent-browser && agent-browser install

Start here

This file is a discovery stub, not the usage guide. Before running any agent-browser command, load the actual workflow content from the CLI:

agent-browser skills get core             # start here — workflows, common patterns, troubleshooting
agent-browser skills get core --full      # include full command reference and templates


The CLI serves skill content that always matches the installed version, so instructions never go stale. The content in this stub cannot change between releases, which is why it just points at skills get core.

Specialized skills

Load a specialized skill when the task falls outside browser web pages:

agent-browser skills get electron          # Electron desktop apps (VS Code, Slack, Discord, Figma, ...)
agent-browser skills get slack             # Slack workspace automation
agent-browser skills get dogfood           # Exploratory testing / QA / bug hunts
agent-browser skills get vercel-sandbox    # agent-browser inside Vercel Sandbox microVMs
agent-browser skills get agentcore         # AWS Bedrock AgentCore cloud browsers


Run agent-browser skills list to see everything available on the installed version.

Why agent-browser
Fast native Rust CLI, not a Node.js wrapper
Works with any AI agent (Cursor, Claude Code, Codex, Continue, Windsurf, etc.)
Chrome/Chromium via CDP with no Playwright or Puppeteer dependency
Accessibility-tree snapshots with element refs for reliable interaction
Sessions, authentication vault, state persistence, video recording
Specialized skills for Electron apps, Slack, exploratory testing, cloud providers
Weekly Installs
229.5K
Repository
vercel-labs/age…-browser
GitHub Stars
31.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn