---
title: logseq-plugin-dev
url: https://skills.sh/0xrichardh/agent-skills/logseq-plugin-dev
---

# logseq-plugin-dev

skills/0xrichardh/agent-skills/logseq-plugin-dev
logseq-plugin-dev
Installation
$ npx skills add https://github.com/0xrichardh/agent-skills --skill logseq-plugin-dev
SKILL.md
Logseq Plugin Development

This skill helps you build high-quality plugins for Logseq using the @logseq/libs SDK.

Core Concepts

Logseq plugins run in a sandboxed iframe and communicate with the main Logseq application via an RPC bridge.

Manifest: Every plugin needs a package.json with a logseq field.
SDK: Use @logseq/libs to interact with Logseq.
Lifecycle: Use logseq.ready(main) to initialize your plugin.
Getting Started
Scaffold:
Basic TS: assets/template/
React + Vite: assets/template-react/
Install Dependencies: npm install @logseq/libs.
Build: Use Vite or a similar bundler to package your JS/TS code.
Load: In Logseq, go to Settings -> Plugins -> Developer Mode, then Load unpacked plugin and select your plugin directory.
Common Workflows
1. Registering Commands

Use logseq.Editor.registerSlashCommand or logseq.App.registerCommandPalette.

2. Interacting with Content
Read: logseq.Editor.getCurrentPageBlocksTree()
Write: logseq.Editor.insertBlock(parentBlockId, content)
Query: logseq.DB.datascriptQuery(query)
3. UI and Theming
UI: Use logseq.provideUI to inject HTML or logseq.showMainUI to show a full-screen app.
Theming: Use Logseq CSS variables (e.g., --ls-primary-background-color) for consistency.
Resources
API Reference: See references/api.md for a detailed list of available methods and examples.
Boilerplates:
assets/template/ (Vanilla TS)
assets/template-react/ (React + Vite)
Examples: See references/examples.md for common patterns like mind maps and slash commands.
Weekly Installs
14
Repository
0xrichardh/agent-skills
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass