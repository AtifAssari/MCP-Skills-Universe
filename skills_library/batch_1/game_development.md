---
title: game-development
url: https://skills.sh/sickn33/antigravity-awesome-skills/game-development
---

# game-development

skills/sickn33/antigravity-awesome-skills/game-development
game-development
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill game-development
Summary

Routing orchestrator for game development projects with platform and dimension-specific sub-skills.

Routes to specialized sub-skills based on target platform (web, mobile, PC, VR/AR) and game dimension (2D or 3D)
Covers core principles applicable across all platforms: game loop architecture, fixed timestep physics, input abstraction, and performance budgeting for 60 FPS
Includes pattern selection matrix (State Machine, ECS, Behavior Trees, Object Pooling) with decision rules for when to apply each
Provides AI selection by complexity level, collision strategy recommendations, and universal anti-patterns to avoid
SKILL.md
Game Development

Orchestrator skill that provides core principles and routes to specialized sub-skills.

When to Use This Skill

You are working on a game development project. This skill teaches the PRINCIPLES of game development and directs you to the right sub-skill based on context.

Sub-Skill Routing
Platform Selection
If the game targets...	Use Sub-Skill
Web browsers (HTML5, WebGL)	game-development/web-games
Mobile (iOS, Android)	game-development/mobile-games
PC (Steam, Desktop)	game-development/pc-games
VR/AR headsets	game-development/vr-ar
Dimension Selection
If the game is...	Use Sub-Skill
2D (sprites, tilemaps)	game-development/2d-games
3D (meshes, shaders)	game-development/3d-games
Specialty Areas
If you need...	Use Sub-Skill
GDD, balancing, player psychology	game-development/game-design
Multiplayer, networking	game-development/multiplayer
Visual style, asset pipeline, animation	game-development/game-art
Sound design, music, adaptive audio	game-development/game-audio
Core Principles (All Platforms)
1. The Game Loop

Every game, regardless of platform, follows this pattern:

INPUT  → Read player actions
UPDATE → Process game logic (fixed timestep)
RENDER → Draw the frame (interpolated)


Fixed Timestep Rule:

Physics/logic: Fixed rate (e.g., 50Hz)
Rendering: As fast as possible
Interpolate between states for smooth visuals
2. Pattern Selection Matrix
Pattern	Use When	Example
State Machine	3-5 discrete states	Player: Idle→Walk→Jump
Object Pooling	Frequent spawn/destroy	Bullets, particles
Observer/Events	Cross-system communication	Health→UI updates
ECS	Thousands of similar entities	RTS units, particles
Command	Undo, replay, networking	Input recording
Behavior Tree	Complex AI decisions	Enemy AI

Decision Rule: Start with State Machine. Add ECS only when performance demands.

3. Input Abstraction

Abstract input into ACTIONS, not raw keys:

"jump"  → Space, Gamepad A, Touch tap
"move"  → WASD, Left stick, Virtual joystick


Why: Enables multi-platform, rebindable controls.

4. Performance Budget (60 FPS = 16.67ms)
System	Budget
Input	1ms
Physics	3ms
AI	2ms
Game Logic	4ms
Rendering	5ms
Buffer	1.67ms

Optimization Priority:

Algorithm (O(n²) → O(n log n))
Batching (reduce draw calls)
Pooling (avoid GC spikes)
LOD (detail by distance)
Culling (skip invisible)
5. AI Selection by Complexity
AI Type	Complexity	Use When
FSM	Simple	3-5 states, predictable behavior
Behavior Tree	Medium	Modular, designer-friendly
GOAP	High	Emergent, planning-based
Utility AI	High	Scoring-based decisions
6. Collision Strategy
Type	Best For
AABB	Rectangles, fast checks
Circle	Round objects, cheap
Spatial Hash	Many similar-sized objects
Quadtree	Large worlds, varying sizes
Anti-Patterns (Universal)
Don't	Do
Update everything every frame	Use events, dirty flags
Create objects in hot loops	Object pooling
Cache nothing	Cache references
Optimize without profiling	Profile first
Mix input with logic	Abstract input layer
Routing Examples
Example 1: "I want to make a browser-based 2D platformer"

→ Start with game-development/web-games for framework selection → Then game-development/2d-games for sprite/tilemap patterns → Reference game-development/game-design for level design

Example 2: "Mobile puzzle game for iOS and Android"

→ Start with game-development/mobile-games for touch input and stores → Use game-development/game-design for puzzle balancing

Example 3: "Multiplayer VR shooter"

→ game-development/vr-ar for comfort and immersion → game-development/3d-games for rendering → game-development/multiplayer for networking

Remember: Great games come from iteration, not perfection. Prototype fast, then polish.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
2.1K
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass