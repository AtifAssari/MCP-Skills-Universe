---
rating: ⭐⭐
title: figma-plugin
url: https://skills.sh/srstomp/pokayokay/figma-plugin
---

# figma-plugin

skills/srstomp/pokayokay/figma-plugin
figma-plugin
Installation
$ npx skills add https://github.com/srstomp/pokayokay --skill figma-plugin
SKILL.md
Figma Plugin Development

Build plugins that extend Figma's functionality using the Plugin API.

Architecture

Figma plugins run in two threads communicating via postMessage:

Main thread (sandbox): Plugin API access, node manipulation, figma.* calls
UI thread (iframe): HTML/CSS/JS interface, no Figma API access, npm packages allowed
Key Principles
Main thread handles all Figma document operations
UI thread handles user interface and external APIs
Communication between threads via figma.ui.postMessage() and onmessage
Plugins must be performant — avoid blocking the main thread
Quick Start Checklist
Set up project with manifest.json (name, id, main, ui)
Create main thread code (code.ts) with plugin logic
Create UI (ui.html) with interface elements
Wire up postMessage communication between threads
Test in Figma development mode
Publish via Figma Community
References
Reference	Description
project-structure-and-build.md	Manifest, TypeScript setup, build configuration
development-testing-and-publishing.md	Dev workflow, testing, publishing, troubleshooting
api-globals-and-nodes.md	Global objects, node types, components
api-rendering-and-advanced.md	Paints, effects, auto layout, styles, variables, events
ui-architecture-and-messaging.md	iframe UI, postMessage, typed messages, plain HTML
ui-react-and-theming.md	React setup, hooks, Figma theme colors
ui-patterns-and-resources.md	Loading states, tabs, color pickers, file downloads
selection-traversal-and-batching.md	Selection handling, node traversal, batch operations
colors-and-text.md	Color conversion, manipulation, text operations
layout-storage-and-utilities.md	Positioning, alignment, storage, error handling, utilities
Weekly Installs
79
Repository
srstomp/pokayokay
GitHub Stars
6
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn