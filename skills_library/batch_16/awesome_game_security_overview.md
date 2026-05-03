---
title: awesome-game-security-overview
url: https://skills.sh/gmh5225/awesome-game-security/awesome-game-security-overview
---

# awesome-game-security-overview

skills/gmh5225/awesome-game-security/awesome-game-security-overview
awesome-game-security-overview
Installation
$ npx skills add https://github.com/gmh5225/awesome-game-security --skill awesome-game-security-overview
SKILL.md
Awesome Game Security - Project Overview
Purpose

This is a curated collection of resources related to game security, covering both offensive (game hacking, cheating) and defensive (anti-cheat) aspects. The project serves as a comprehensive reference for security researchers, game developers, and enthusiasts, especially where Windows internals, driver trust, reverse engineering, DMA, and modern anti-cheat defenses intersect.

README Coverage
Top-level engines and rendering: Game Engine, Renderer, DirectX, OpenGL, Vulkan
Offensive research: Cheat
Defensive research: Anti Cheat
Platform hardening: Windows Security Features
Platform-specific ecosystems: Android Emulator, IOS Emulator, Windows Emulator, Linux Emulator
Supporting infrastructure: Mathematics, 3D Graphics, AI, Image Codec, Wavefront Obj, Task Scheduler, Game Network, PhysX SDK, Game Develop, Game Assets, Game Hot Patch, Game Testing, Game Tools, Game Manager, Game CI
Platform subsystems: WSL, WSA
Console emulation: Game Boy, Nintendo Switch, Xbox, PlayStation
Tips and tricks: Some Tricks
Project Structure
awesome-game-security/
├── README.md           # Main resource list
├── LICENSE             # MIT License
├── awesome-image.webp  # Project banner
└── scripts/
    ├── generate-toc.py  # Generate table of contents
    └── remove-forks.py  # Clean up forked repos

README.md Format Convention
Category Structure

Each category follows this format:

## Category Name
> Subcategory (optional)
- https://github.com/user/repo [Brief description]
- https://github.com/user/repo [Another description]

Link Format
Always use full GitHub URLs for repositories
Non-GitHub links are also supported (blog posts, articles, documentation sites)
Add brief descriptions in square brackets [description]
Use consistent spacing and formatting
Group related resources under subcategories with >
Example Entry
## Game Engine
> Guide
- https://github.com/example/guide [Comprehensive game dev guide]

> Source
- https://github.com/example/engine [Open source game engine]

Skill Routing Guide

When an AI agent receives a query, use this table to select the best skill:

Query topic	Primary skill	Related skills
EAC, BattlEye, Vanguard, detection, heartbeat, screenshot	anti-cheat	windows-kernel
pcileech, FPGA, DMA, IOMMU, Thunderbolt	dma-attack	anti-cheat
Unreal SDK, Unity IL2CPP, engine structs, Godot, Lumix	game-engine	game-hacking
Memory hacking, injection, overlays, driver comm, HWID spoof	game-hacking	graphics-api
D3D/Vulkan/OpenGL hooks, Present hook, shader interception	graphics-api	game-hacking
Android root, Frida, iOS jailbreak, KernelSU, APatch	mobile-security	game-hacking
IDA, Ghidra, DBI, deobfuscation, binary diffing, MCP RE tools, trap-and-emulate CFT, WHP tracing	reverse-engineering	anti-cheat, windows-kernel
Drivers, callbacks, PatchGuard, HVCI, ETW, pool forensics, WHP API	windows-kernel	anti-cheat, reverse-engineering
Adding resources, README format, link validation	overview	(any)
Main Categories

All 27 top-level ## sections in README.md:

Game Engine: Engines, source code, plugins (Unreal/Unity/Godot/Lumix), detectors
Mathematics: Linear algebra, physics libraries
Renderer: Software renderers, ray tracing
3D Graphics: 3D modeling and graphics resources
AI: Machine learning for games
Image Codec: Image processing libraries
Wavefront Obj: OBJ file parsers
Task Scheduler: Job/task scheduling systems
Game Network: Networking, KCP, JWT, geolocation
PhysX SDK: NVIDIA PhysX resources
Game Develop: Development guides, source code, MCP servers, AI agents
Game Assets / Hot Patch / Testing / Tools / Manager / CI: Supporting infrastructure
DirectX: Guides, hooks, tools, emulation, overlays
OpenGL: Guides, source, hooks
Vulkan: API, guides, hooks
Cheat: Offensive research (debugging, injection, hooking, DMA, overlays, driver comm, EFI, anti-forensics, game-specific)
Anti Cheat: Defensive research (protection, detection, callbacks, forensics, signature scanning)
Some Tricks: Ring0/Ring3/Linux/Android tricks and techniques
Windows Security Features: DSE, PatchGuard, VBS, HVCI, Secure Boot
WSL / WSA: Windows Subsystem for Linux/Android
Windows / Linux / Android / IOS Emulator: Platform emulators
Game Boy / Nintendo Switch / Xbox / PlayStation: Console emulators and research
Contributing Guidelines
Check for duplicates before adding new resources
Verify links are working and point to original repos
Add descriptions that clearly explain the resource's purpose
Place in correct category based on primary functionality
Follow existing format for consistency
Quality Criteria
Resource should be actively maintained or historically significant
Should provide unique value not covered by existing entries
Prefer original repos over forks unless fork adds significant value
Include language/platform tags when helpful (e.g., [Rust], [Unity])
Scripts Usage
Generate Table of Contents
python scripts/generate-toc.py

Remove Fork References
python scripts/remove-forks.py

Data Source

Important: This skill provides conceptual guidance and overview information. For detailed information use the following sources:

1. Project Overview & Resource Index

Fetch the main README for the full curated list of repositories, tools, and descriptions:

https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/README.md


The main README contains thousands of curated links organized by category. When users ask for specific tools, projects, or implementations, retrieve and reference the appropriate sections from this source.

2. Repository Code Details (Archive)

For detailed repository information (file structure, source code, implementation details), the project maintains a local archive. If a repository has been archived, always prefer fetching from the archive over cloning or browsing GitHub directly.

Archive URL format:

https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/{owner}/{repo}.txt


Examples:

https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/ufrisk/pcileech.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/000-aki-000/GameDebugMenu.txt


How to use:

Identify the GitHub repository the user is asking about (owner and repo name from the URL).
Construct the archive URL: replace {owner} with the GitHub username/org and {repo} with the repository name (no .git suffix).
Fetch the archive file — it contains a full code snapshot with file trees and source code generated by code2prompt.
If the fetch returns a 404, the repository has not been archived yet; fall back to the README or direct GitHub browsing.
3. Repository Descriptions

For a concise English summary of what a repository does, the project maintains auto-generated description files.

Description URL format:

https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/{owner}/{repo}/description_en.txt


Examples:

https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/00christian00/UnityDecompiled/description_en.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/ufrisk/pcileech/description_en.txt


How to use:

Identify the GitHub repository the user is asking about (owner and repo name from the URL).
Construct the description URL: replace {owner} with the GitHub username/org and {repo} with the repository name.
Fetch the description file — it contains a short, human-readable summary of the repository's purpose and contents.
If the fetch returns a 404, the description has not been generated yet; fall back to the README entry or the archive.

Priority order when answering questions about a specific repository:

Description (quick summary) — fetch first for concise context
Archive (full code snapshot) — fetch when deeper implementation details are needed
README entry — fallback when neither description nor archive is available
Weekly Installs
63
Repository
gmh5225/awesome…security
GitHub Stars
2.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn