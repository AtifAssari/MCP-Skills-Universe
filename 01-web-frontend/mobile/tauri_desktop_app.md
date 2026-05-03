---
title: tauri-desktop-app
url: https://skills.sh/kahojyun/fricon/tauri-desktop-app
---

# tauri-desktop-app

skills/kahojyun/fricon/tauri-desktop-app
tauri-desktop-app
Installation
$ npx skills add https://github.com/kahojyun/fricon --skill tauri-desktop-app
SKILL.md
Tauri Desktop App

Use this skill only for work under crates/fricon-ui that crosses the Rust/Tauri boundary.

Read First
Command and event definitions: crates/fricon-ui/src/commands/
App setup, tray, window lifecycle: crates/fricon-ui/src/runtime.rs
Tauri config: crates/fricon-ui/tauri.conf.json
Capabilities and permissions: crates/fricon-ui/capabilities/default.json
Frontend bridge and wire-to-domain normalization: crates/fricon-ui/frontend/src/lib/backend.ts
Generated bindings: crates/fricon-ui/frontend/src/lib/bindings.ts
Repo Rules
This repo uses Tauri v2 with tauri-specta; Rust is the type source of truth for exported commands, payloads, and events.
Do not edit crates/fricon-ui/frontend/src/lib/bindings.ts manually.
Regenerate bindings with pnpm --filter fricon-ui run gen:bindings after Rust command or event signature changes.
Keep native-call wrappers and wire-to-domain normalization in crates/fricon-ui/frontend/src/lib/backend.ts.
When a feature needs Tauri capabilities or plugin permissions, update crates/fricon-ui/capabilities/default.json.
Keep CI fmt lightweight. Do not move binding generation or Rust-compiling checks into fmt.
Workflow
Decide whether the change is frontend-only or needs a Rust command/event.
If IPC changes, update the Rust types first in crates/fricon-ui/src/commands/.
If runtime behavior changes, inspect crates/fricon-ui/src/runtime.rs before adding new Tauri setup code.
Keep the frontend integration behind crates/fricon-ui/frontend/src/lib/backend.ts.
Regenerate bindings.ts if command or event signatures changed.
If the feature needs extra Tauri permissions, update crates/fricon-ui/capabilities/default.json and tauri.conf.json only as required by the concrete feature.
Example Triggers
"Add a new Rust command and call it from the frontend"
"Expose a typed Tauri event to React"
"Change tray or window close behavior"
"Add a plugin permission to the default capability"
"Update tauri.conf.json for a concrete desktop feature"
Weekly Installs
19
Repository
kahojyun/fricon
GitHub Stars
2
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass