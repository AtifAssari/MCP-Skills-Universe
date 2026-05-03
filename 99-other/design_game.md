---
title: design-game
url: https://skills.sh/opusgamelabs/game-creator/design-game
---

# design-game

skills/opusgamelabs/game-creator/design-game
design-game
Installation
$ npx skills add https://github.com/opusgamelabs/game-creator --skill design-game
SKILL.md
Performance Notes
Take your time to do this thoroughly
Quality is more important than speed
Do not skip validation steps
Design Game

Run a UI/UX design pass on an existing game to improve visuals, atmosphere, and game feel. No design experience needed — this command analyzes your game and applies proven visual patterns.

Instructions

Analyze the game at $ARGUMENTS (or the current directory if no path given).

First, load the game-designer skill to get the full design vocabulary and patterns.

Step 1: Audit
Read package.json to identify the engine
Read src/core/Constants.js for the current color palette and config
Read all scene files to understand current visuals
Read entity files to see how game objects are drawn
Read src/core/EventBus.js for existing events
Step 2: Design Report

Score each area 1-5 and present as a table:

Area	Score	Notes
Background & Atmosphere		
Color Palette		
Animations & Tweens		
Particle Effects		
Screen Transitions		
Typography		
Game Feel / Juice		
Game Over		
Expression Usage		If personality characters exist, score how reactively expressions change to game events. Score 1 if expressions never change.

Then list the top improvements ranked by visual impact, with a plain-English description of what each one does (e.g., "Add a sky gradient so the background looks like a real sky instead of a flat color").

Step 3: Implement

Ask the user which improvements they want, or implement all if they say so. Follow the game-designer skill patterns:

All new values in Constants.js
Use EventBus for triggering effects
Don't alter gameplay (physics, scoring, controls, spawn timing)
Prefer procedural graphics
New files in proper directories
Step 4: Verify
Run npm run build to confirm no errors
Summarize all changes made in plain English
Example Usage
Full design pass
/design-game examples/asteroid-dodge


Result: Audits visuals → scores Background 2/5, Particles 1/5, Typography 3/5 → adds sky gradient background, star parallax, explosion particles on asteroid destroy, screen shake on hit, smooth scene transitions. All values in Constants.js.

Troubleshooting
Visual changes cause performance drops

Cause: Too many particle emitters or gradient fills per frame. Fix: Limit active particles (pool and reuse). Use cached gradient textures instead of recreating per-frame.

Design changes break layout on different screen sizes

Cause: Hardcoded pixel positions instead of using PX scale factor. Fix: All positions and sizes should use Constants.js PX-relative values.

Next Step

Tell the user:

Your game looks much better now! Next, run /game-creator:add-audio to add chiptune background music and retro sound effects — all procedurally generated, no audio files needed.

Pipeline progress: /make-game → /design-game → /add-audio → /qa-game → /review-game

Weekly Installs
368
Repository
opusgamelabs/ga…-creator
GitHub Stars
128
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass