---
title: phaser-2d-arcade
url: https://skills.sh/farworld-labs/remix-skills/phaser-2d-arcade
---

# phaser-2d-arcade

skills/farworld-labs/remix-skills/phaser-2d-arcade
phaser-2d-arcade
Installation
$ npx skills add https://github.com/farworld-labs/remix-skills --skill phaser-2d-arcade
SKILL.md
Phaser 2D Arcade

Use this skill when a user asks for a Phaser browser game, especially for fast single-file 2D gameplay loops.

Workflow
Start from assets/starter-single-file.html.
Implement core loop first: boot -> preload -> create -> update.
Add win/lose condition and scoring before polish.
Add touch controls and responsive layout early (mobile-first).
If targeting Remix, apply SDK hooks from references/sdk-integration.md.
Validate required hooks (gameOver, onPlayAgain, onToggleMute) before handoff.
Guardrails
Prefer Phaser Arcade Physics for simplicity/performance.
Keep initial scope small: 1 scene, 1 mechanic, 1 fail condition.
Avoid expensive per-frame allocations and unnecessary visual effects.
Keep gameplay restart-safe and deterministic.
For Remix uploads, produce single-file HTML with inline JS/CSS unless user asks otherwise.
For Remix uploads, include <script src="https://cdn.jsdelivr.net/npm/@remix-gg/sdk@latest/dist/index.min.js"></script> in HTML <head>.
References
references/phaser-arcade-patterns.md for scene architecture, controls, and perf defaults.
references/sdk-integration.md for Remix SDK hooks and integration shape.
Weekly Installs
33
Repository
farworld-labs/r…x-skills
GitHub Stars
9
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass