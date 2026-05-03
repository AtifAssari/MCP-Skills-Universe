---
rating: ⭐⭐⭐
title: openwork-core
url: https://skills.sh/different-ai/openwork/openwork-core
---

# openwork-core

skills/different-ai/openwork/openwork-core
openwork-core
Installation
$ npx skills add https://github.com/different-ai/openwork --skill openwork-core
SKILL.md
Quick Usage (Already Configured)
Orientation
Read AGENTS.md, VISION.md, PRINCIPLES.md, PRODUCT.md, and ARCHITECTURE.md before changing behavior.
Ensure vendor/opencode exists for self-reference.
Use the tauri-solidjs skill for stack-specific guidance.
Update the OpenCode mirror
git -C vendor/opencode pull --ff-only

Development workflow
pnpm tauri dev          # Desktop development
pnpm tauri ios dev      # iOS development
pnpm tauri android dev  # Android development

# Or run directly in the desktop package:
pnpm -C packages/desktop tauri dev

OpenCode Integration
Spawn OpenCode CLI
opencode -p "your prompt" -f json -q

Read OpenCode database
~/.opencode/opencode.db  # SQLite database

Key tables
sessions — Task runs
messages — Chat messages and tool calls
history — File change tracking
Common Gotchas
OpenWork must stay within OpenCode's tool surface; avoid inventing new capabilities.
Always expose plans, permissions, and progress for non-technical users.
Use Tauri commands for all system access (file, shell, database).
Keep UI at 60fps; avoid blocking the main thread.
Mobile builds require platform-specific setup (Xcode, Android Studio).
UI Principles
Slick and fluid: animations, transitions, micro-interactions.
Mobile-first: touch targets, gestures, adaptive layouts.
Transparency: show plans, steps, and tool calls.
Progressive disclosure: hide advanced controls until needed.
First-Time Setup (If Not Configured)
Clone the OpenCode mirror
git clone https://github.com/anomalyco/opencode vendor/opencode

Initialize Tauri project
pnpm create tauri-app . --template solid-ts

Add mobile targets
pnpm tauri ios init
pnpm tauri android init

Common Gotchas
OpenWork must stay within OpenCode’s tool surface; avoid inventing new capabilities.
Always expose plans, permissions, and progress for non-technical users.
First-Time Setup (If Not Configured)
Clone the OpenCode mirror
git clone https://github.com/anomalyco/opencode vendor/opencode

Weekly Installs
403
Repository
different-ai/openwork
GitHub Stars
14.6K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn