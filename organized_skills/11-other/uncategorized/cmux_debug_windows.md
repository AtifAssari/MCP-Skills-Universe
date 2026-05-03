---
rating: ⭐⭐
title: cmux-debug-windows
url: https://skills.sh/manaflow-ai/cmux/cmux-debug-windows
---

# cmux-debug-windows

skills/manaflow-ai/cmux/cmux-debug-windows
cmux-debug-windows
Installation
$ npx skills add https://github.com/manaflow-ai/cmux --skill cmux-debug-windows
SKILL.md
cmux Debug Windows

Keep this workflow focused on existing debug windows and menu entries. Do not add a new utility/debug control window unless the user asks explicitly.

Workflow
Verify debug menu wiring in Sources/cmuxApp.swift under CommandMenu("Debug").
Menu path in app: Debug → Debug Windows → window entry.
The Debug menu only exists in DEBUG builds (./scripts/reload.sh --tag ...).
Release builds (reloadp.sh, reloads.sh) do not show this menu.
Keep these actions available in Menu("Debug Windows"):
Sidebar Debug…
Background Debug…
Menu Bar Extra Debug…
Open All Debug Windows
Reuse existing per-window copy buttons (Copy Config) in each debug window before adding new UI.
For one combined payload, run:
skills/cmux-debug-windows/scripts/debug_windows_snapshot.sh --copy

After code edits, run build + tagged reload:
xcodebuild -project GhosttyTabs.xcodeproj -scheme cmux -configuration Debug -destination 'platform=macOS' build
./scripts/reload.sh --tag <tag>

Key Files
Sources/cmuxApp.swift: Debug menu entries and debug window controllers/views.
Sources/AppDelegate.swift: Menu bar extra debug settings payload and defaults keys.
Script
scripts/debug_windows_snapshot.sh

Purpose:

Reads current debug-related defaults values.
Prints one combined snapshot for sidebar/background/menu bar extra.
Optionally copies it to clipboard.

Examples:

skills/cmux-debug-windows/scripts/debug_windows_snapshot.sh
skills/cmux-debug-windows/scripts/debug_windows_snapshot.sh --copy
skills/cmux-debug-windows/scripts/debug_windows_snapshot.sh --domain <bundle-id> --copy

Weekly Installs
495
Repository
manaflow-ai/cmux
GitHub Stars
16.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass