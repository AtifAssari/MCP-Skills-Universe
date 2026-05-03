---
rating: ⭐⭐
title: game-engine
url: https://skills.sh/github/awesome-copilot/game-engine
---

# game-engine

skills/github/awesome-copilot/game-engine
game-engine
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill game-engine
Summary

Web-based game engine and game development using HTML5 Canvas, WebGL, and JavaScript.

Covers 2D and 3D game creation with frameworks like Phaser, Three.js, Babylon.js, and A-Frame
Includes game loop implementation, physics, collision detection, sprite management, tilemaps, and rendering techniques
Supports multiple input methods: keyboard, mouse, touch, and gamepad controls
Provides starter templates for breakout games, platformers, maze games, and 3D experiences
Addresses audio integration, WebRTC multiplayer, performance optimization, and game publishing workflows
SKILL.md
Game Engine Skill

Build web-based games and game engines using HTML5 Canvas, WebGL, and JavaScript. This skill includes starter templates, reference documentation, and step-by-step workflows for 2D and 3D game development with frameworks such as Phaser, Three.js, Babylon.js, and A-Frame.

When to Use This Skill
Building a game engine or game from scratch using web technologies
Implementing game loops, physics, collision detection, or rendering
Working with HTML5 Canvas, WebGL, or SVG for game graphics
Adding game controls (keyboard, mouse, touch, gamepad)
Creating 2D platformers, breakout-style games, maze games, or 3D experiences
Working with tilemaps, sprites, or animations
Adding audio to web games
Implementing multiplayer features with WebRTC or WebSockets
Optimizing game performance
Publishing and distributing web games
Prerequisites
Basic knowledge of HTML, CSS, and JavaScript
A modern web browser with Canvas/WebGL support
A text editor or IDE
Optional: Node.js for build tooling and local development servers
Core Concepts

The following concepts form the foundation of every web-based game engine.

Game Loop

Every game engine revolves around the game loop -- a continuous cycle of:

Process Input - Read keyboard, mouse, touch, or gamepad input
Update State - Update game object positions, physics, AI, and logic
Render - Draw the current game state to the screen

Use requestAnimationFrame for smooth, browser-optimized rendering.

Rendering
Canvas 2D - Best for 2D games, sprite-based rendering, and tilemaps
WebGL - Hardware-accelerated 3D and advanced 2D rendering
SVG - Vector-based graphics, good for UI elements
CSS - Useful for DOM-based game elements and transitions
Physics and Collision Detection
2D Collision Detection - AABB, circle, and SAT-based collision
3D Collision Detection - Bounding box, bounding sphere, and raycasting
Velocity and Acceleration - Basic Newtonian physics for movement
Gravity - Constant downward acceleration for platformers
Controls
Keyboard - Arrow keys, WASD, and custom key bindings
Mouse - Click, move, and pointer lock for FPS-style controls
Touch - Mobile touch events and virtual joysticks
Gamepad - Gamepad API for controller support
Audio
Web Audio API - Programmatic sound generation and spatial audio
HTML5 Audio - Simple audio playback for music and sound effects
Step-by-Step Workflows
Creating a Basic 2D Game
Set up an HTML file with a <canvas> element
Get the 2D rendering context
Implement the game loop using requestAnimationFrame
Create game objects with position, velocity, and size properties
Handle keyboard/mouse input for player control
Implement collision detection between game objects
Add scoring, lives, and win/lose conditions
Add sound effects and music
Building a 3D Game
Choose a framework (Three.js, Babylon.js, A-Frame, or PlayCanvas)
Set up the scene, camera, and renderer
Load or create 3D models and textures
Implement lighting and shaders
Add physics and collision detection
Implement player controls and camera movement
Add audio and visual effects
Publishing a Game
Optimize assets (compress images, minify code)
Test across browsers and devices
Choose distribution platform (web, app stores, game portals)
Implement monetization if needed
Promote through game communities and social media
Game Templates

Starter templates are available in the assets/ folder. Each template provides a complete, working example that can be used as a starting point for a new project.

Template	Description
paddle-game-template.md	2D Breakout-style game with pure JavaScript
2d-maze-game.md	Maze game with device orientation controls
2d-platform-game.md	Platformer game using Phaser framework
gameBase-template-repo.md	Game base template repository structure
simple-2d-engine.md	Simple 2D platformer engine with collisions
Reference Documentation

Detailed reference material is available in the references/ folder. Consult these files for in-depth coverage of specific topics.

Reference	Topics Covered
basics.md	Game development introduction and anatomy
web-apis.md	Canvas, WebGL, Web Audio, Gamepad, and other web APIs
techniques.md	Collision detection, tilemaps, async scripts, audio
3d-web-games.md	3D theory, frameworks, shaders, WebXR
game-control-mechanisms.md	Touch, keyboard, mouse, and gamepad controls
game-publishing.md	Distribution, promotion, and monetization
algorithms.md	Raycasting, collision, physics, vector math
terminology.md	Game development glossary
game-engine-core-principles.md	Core design principles for game engines
Troubleshooting
Issue	Solution
Canvas is blank	Check that you are calling drawing methods after getting the context and inside the game loop
Game runs at different speeds	Use delta time in update calculations instead of fixed values
Collision detection is inconsistent	Use continuous collision detection or reduce time steps for fast-moving objects
Audio does not play	Browsers require user interaction before playing audio; trigger playback from a click handler
Performance is poor	Profile with browser dev tools, reduce draw calls, use object pooling, and optimize asset sizes
Touch controls are unresponsive	Prevent default touch behavior and handle touch events separately from mouse events
WebGL context lost	Handle the webglcontextlost event and restore state on webglcontextrestored
Weekly Installs
9.6K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass