---
title: floor-plan
url: https://skills.sh/markdown-viewer/skills/floor-plan
---

# floor-plan

skills/markdown-viewer/skills/floor-plan
floor-plan
Installation
$ npx skills add https://github.com/markdown-viewer/skills --skill floor-plan
SKILL.md
Floor Plan & Layout Generator

Quick Start: Define room boundaries with walls → Add doors and windows → Place furniture from stencil library → Add dimensions and labels → Wrap in ```drawio fence.

⚠️ IMPORTANT: Always use ```drawio code fence. NEVER use ```xml — it will NOT render as a diagram.

Critical Rules

🔗 This is a drawio-derived skill. All structure, layout, and edge routing rules inherit from drawio SKILL.md. Read the base rules first.

Floor plan-specific additions:

Check stencils/README.md for exact furniture stencil names
Use consistent scale: 1 pixel = 1 cm is a common convention (so a 3m wall = 300px)
Wall thickness: typically 15-20px for exterior, 10px for interior walls
Standard door width: 80-90cm (80-90px), window: varies
Floor Plan Types
Type	Purpose	Stencil Library	Example
Office Layout	Open office, cubicles, meeting rooms	mxgraph.floorplan.* (44 symbols)	office-layout.md
Home Floor Plan	Residential room layouts	mxgraph.floorplan.*	home-floor-plan.md
Evacuation Plan	Emergency exit routes, fire safety	Basic shapes + arrows	evacuation-plan.md
Seating Plan	Event seating, theater layouts	mxgraph.floorplan.*	seating-plan.md
Weekly Installs
213
Repository
markdown-viewer/skills
GitHub Stars
2.4K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass