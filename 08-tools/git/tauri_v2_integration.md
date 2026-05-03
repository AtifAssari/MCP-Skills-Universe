---
rating: ⭐⭐
title: tauri-v2-integration
url: https://skills.sh/xiaolai/vmark/tauri-v2-integration
---

# tauri-v2-integration

skills/xiaolai/vmark/tauri-v2-integration
tauri-v2-integration
Installation
$ npx skills add https://github.com/xiaolai/vmark --skill tauri-v2-integration
SKILL.md
Tauri v2 Integration (VMark)
Overview

Ensure Tauri v2 bridge patterns and IPC flows are consistent across frontend and Rust.

Workflow
Identify the bridge direction:
Rust -> Webview: window.emit()/app.emit() + listen() on frontend.
Webview -> Rust: invoke().
Update frontend hooks/plugins that manage IPC (src/hooks/, src/plugins/).
Update Rust commands or menu entries in src-tauri/.
Keep behavior consistent across WYSIWYG and Source modes.
If E2E behavior needs validation, use Tauri MCP tools.
References
references/paths.md for key files and patterns.
Manual E2E: see tauri-mcp-testing skill for patterns.
Related Skills
tauri-app-dev — General Tauri 2.0 patterns (commands, state, plugins, security)
tauri-mcp-testing — E2E testing via Tauri MCP tools
rust-tauri-backend — VMark Rust backend implementation
Weekly Installs
56
Repository
xiaolai/vmark
GitHub Stars
301
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass