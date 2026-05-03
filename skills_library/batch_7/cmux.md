---
title: cmux
url: https://skills.sh/manaflow-ai/cmux/cmux
---

# cmux

skills/manaflow-ai/cmux/cmux
cmux
Installation
$ npx skills add https://github.com/manaflow-ai/cmux --skill cmux
Summary

Deterministic control of cmux window, workspace, pane, and surface topology for multi-pane layout automation.

Commands cover window and workspace creation, pane splitting, surface movement and reordering, focus routing, and visual attention cues via flash triggers
Uses short reference handles (window:N, workspace:N, pane:N, surface:N) by default; supports UUID input and output when needed
Designed for automation workflows requiring precise, repeatable placement and navigation across terminal and browser panel layouts
Integrates with cmux-browser and cmux-markdown skills for specialized surface control
SKILL.md
cmux Core Control

Use this skill to control non-browser cmux topology and routing.

Core Concepts
Window: top-level macOS cmux window.
Workspace: tab-like group within a window.
Pane: split container in a workspace.
Surface: a tab within a pane (terminal or browser panel).
Fast Start
# identify current caller context
cmux identify --json

# list topology
cmux list-windows
cmux list-workspaces
cmux list-panes
cmux list-pane-surfaces --pane pane:1

# create/focus/move
cmux new-workspace
cmux new-split right --panel pane:1
cmux move-surface --surface surface:7 --pane pane:2 --focus true
cmux reorder-surface --surface surface:7 --before surface:3

# attention cue
cmux trigger-flash --surface surface:7

Settings and Docs

Use cmux docs settings before changing cmux-owned settings. It prints the docs URL, schema URL, raw GitHub resources, settings file paths, and reload command.

cmux docs settings
cmux settings path


cmux-owned settings live in ~/.config/cmux/settings.json, with ~/Library/Application Support/com.cmuxterm.app/settings.json as the fallback. Before editing, copy any existing settings file to a timestamped .bak next to it so the user can revert. Edit the user file, then reload:

cmux reload-config


Use cmux settings for app behavior, sidebar, notifications, browser behavior, automation, workspace colors, and cmux-owned shortcuts. Terminal rendering settings such as font, cursor style, theme, and scrollback belong in Ghostty config.

Open the UI when useful:

cmux settings
cmux settings json
cmux settings shortcuts

Handle Model
Default output uses short refs: window:N, workspace:N, pane:N, surface:N.
UUIDs are still accepted as inputs.
Request UUID output only when needed: --id-format uuids|both.
Deep-Dive References
Reference	When to Use
references/handles-and-identify.md	Handle syntax, self-identify, caller targeting
references/windows-workspaces.md	Window/workspace lifecycle and reorder/move
references/panes-surfaces.md	Splits, surfaces, move/reorder, focus routing
references/trigger-flash-and-health.md	Flash cue and surface health checks
../cmux-browser/SKILL.md	Browser automation on surface-backed webviews
../cmux-markdown/SKILL.md	Markdown viewer panel with live file watching
Weekly Installs
1.4K
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