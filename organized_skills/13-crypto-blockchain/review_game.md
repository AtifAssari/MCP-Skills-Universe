---
rating: ⭐⭐
title: review-game
url: https://skills.sh/opusgamelabs/game-creator/review-game
---

# review-game

skills/opusgamelabs/game-creator/review-game
review-game
Installation
$ npx skills add https://github.com/opusgamelabs/game-creator --skill review-game
SKILL.md
Performance Notes
Take your time to do this thoroughly
Quality is more important than speed
Do not skip validation steps
Review Game

Analyze an existing game codebase and provide a structured review. This is the final step in the pipeline — it checks everything is wired up correctly and gives you a quality score.

Instructions

Analyze the game at $ARGUMENTS (or the current directory if no path given).

Step 1: Identify the game
Detect the engine (Three.js, Phaser, or other)
Read package.json for dependencies and scripts
Read the main entry point and index.html
Identify the game concept/genre
Step 2: Architecture Review

Check for these required patterns and report compliance:

 EventBus: Is there a centralized event system? Are modules decoupled?
 GameState: Is there a centralized state singleton?
 Constants: Are config values centralized or scattered as magic numbers?
 Orchestrator: Is there a main Game class that initializes everything?
 Directory Structure: Is code organized into core/systems/gameplay/ui/level layers?
 Event Constants: Are events defined as named constants or raw strings?
Step 3: Performance Review

Check for common issues:

 Delta time capping: Is getDelta() capped to prevent death spirals?
 Object pooling: Are temp objects reused in hot loops?
 Resource disposal: Are Three.js geometries/materials/textures disposed?
 Event cleanup: Are event listeners cleaned up on scene transitions?
 Asset loading: Are assets preloaded with progress feedback?
Step 4: Code Quality
 No circular dependencies: Modules flow one direction
 Single responsibility: Each module has one clear job
 Error handling: Event handlers wrapped in try/catch
 Consistent naming: Events use domain:action, files use PascalCase
Step 5: Monetization Readiness
 Points system: Is there a scoring/points mechanism?
 Session tracking: Can game sessions be identified?
 Anti-cheat potential: Is score validation server-side or at least structured for it?
 Play.fun integration: Any existing SDK integration?
Output Format

Provide a structured report with:

Game Overview - What the game is, tech stack, game loop
Architecture Score (out of 6 checks)
Performance Score (out of 5 checks)
Code Quality Score (out of 4 checks)
Monetization Readiness (out of 4 checks)
Top Recommendations - Prioritized list of improvements with plain-English explanations
What's Working Well - Positive findings
Example Usage
/review-game examples/flappy-bird


Result: Architecture 6/6, Performance 4/5, Code Quality 4/4, Monetization 2/4 → Top recommendations: add Play.fun SDK, add object pooling for pipes, add delta time capping. Positive findings: clean EventBus usage, proper GameState reset, well-organized directory structure.

Next Step

Tell the user:

Your game has been through the full pipeline! Here's what you have:

Scaffolded architecture (/make-game)
Visual polish (/design-game)
Music and sound effects (/add-audio)
Automated tests (/qa-game)
Architecture review (/review-game)

What's next?

Add new gameplay features with /game-creator:add-feature [description]
Deploy to the web — run npm run build && ~/.agents/skills/here-now/scripts/publish.sh dist/ for instant hosting, or use GitHub Pages, Vercel, Netlify, itch.io
Keep iterating! Run /design-game, /add-audio, or /review-game again anytime after making changes.
Weekly Installs
321
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