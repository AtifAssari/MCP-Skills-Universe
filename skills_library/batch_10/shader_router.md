---
title: shader-router
url: https://skills.sh/bbeierle12/skill-mcp-claude/shader-router
---

# shader-router

skills/bbeierle12/skill-mcp-claude/shader-router
shader-router
Installation
$ npx skills add https://github.com/bbeierle12/skill-mcp-claude --skill shader-router
SKILL.md
Shader Router

Routes to 4 specialized GLSL shader skills based on task requirements.

Routing Protocol
Classify — Identify what visual result is needed
Match — Find skill(s) with highest signal match
Combine — Most shaders need 2-3 skills together
Load — Read matched SKILL.md files before implementation
Quick Route
Tier 1: Core (Always Consider)
Task Type	Skill	Primary Signal Words
Writing shaders	shader-fundamentals	GLSL, vertex, fragment, uniform, varying, coordinate
Organic patterns	shader-noise	noise, procedural, terrain, clouds, turbulence, organic
Tier 2: Specialized (Add When Needed)
Task Type	Skill	Primary Signal Words
Shapes/geometry	shader-sdf	shape, circle, box, boolean, union, morph, raymarch
Visual polish	shader-effects	glow, bloom, chromatic, distortion, vignette, glitch
Signal Matching Rules
Priority Order

When multiple signals present, resolve by priority:

Explicit technique — "use simplex noise" → shader-noise
Visual goal — "organic look" → shader-noise
Shape need — "rounded rectangle" → shader-sdf
Polish need — "add glow" → shader-effects
Default — Start with shader-fundamentals
Confidence Scoring
High (3+ signals) — Route immediately
Medium (1-2 signals) — Route with shader-fundamentals as base
Low (0 signals) — Ask: "What visual effect are you trying to achieve?"
Common Combinations
Procedural Texture (2 skills)
shader-fundamentals → Vertex/fragment setup, uniforms
shader-noise        → Noise functions, FBM


Wiring: Fundamentals provides shader structure, noise generates patterns.

Stylized Shape (3 skills)
shader-fundamentals → Shader setup, UV handling
shader-sdf          → Shape definition, boolean ops
shader-effects      → Glow, outline, anti-aliasing


Wiring: SDF defines shape, effects add visual polish.

Terrain/Landscape (2 skills)
shader-fundamentals → Vertex displacement, lighting
shader-noise        → Height generation, detail layers


Wiring: Noise generates heightmap, fundamentals handles displacement and shading.

Holographic/Cyberpunk (3 skills)
shader-fundamentals → Fresnel, scanlines base
shader-noise        → Animated distortion
shader-effects      → Chromatic aberration, glitch, glow


Wiring: Layer multiple effects for complex visual style.

UI/Logo Animation (3 skills)
shader-fundamentals → Animation timing, UV manipulation
shader-sdf          → Shape primitives, morphing
shader-effects      → Glow, dissolve, outline


Wiring: SDF creates shapes, effects add transitions.

Raymarched 3D (3 skills)
shader-fundamentals → Ray setup, lighting math
shader-sdf          → 3D primitives, scene composition
shader-noise        → Surface detail, displacement


Wiring: SDF defines geometry, noise adds organic detail.

Decision Table
Visual Goal	Organic?	Shapes?	Effects?	Route To
Clouds	Yes	No	Maybe	fundamentals + noise
Logo	No	Yes	Yes	fundamentals + sdf + effects
Terrain	Yes	No	No	fundamentals + noise
Fire/smoke	Yes	No	Yes	fundamentals + noise + effects
UI element	No	Yes	Yes	fundamentals + sdf + effects
Abstract art	Yes	Maybe	Yes	all skills
3D raymarch	Maybe	Yes	Maybe	fundamentals + sdf + (noise)
Skill Dependencies
shader-fundamentals (foundation)
├── shader-noise (extends fundamentals)
├── shader-sdf (extends fundamentals)
└── shader-effects (extends fundamentals)

Always start with shader-fundamentals
shader-noise and shader-sdf are often independent
shader-effects typically applied last
Visual Goal → Technique Mapping
Want This	Use This
Natural/organic look	Noise (FBM, turbulence)
Geometric shapes	SDF primitives
Smooth morphing	SDF smooth operations
Infinite patterns	SDF repetition
Terrain height	Noise + vertex displacement
Water/caustics	Noise + Worley
Glow/bloom	Effects (glow functions)
Retro/CRT look	Effects (scanlines, grain)
Transitions	SDF dissolve or Effects dissolve
Outlines	SDF or Effects (both have methods)
Fallback Behavior
Unknown technique → Start with shader-fundamentals
No clear signals → Ask: "Describe the visual you're trying to create"
Performance concerns → Check shader-noise optimization tips
Quick Decision Flowchart
User Request
     │
     ▼
┌─────────────────────┐
│ Writing shaders?    │──Yes──▶ shader-fundamentals (always)
└─────────────────────┘
     │
     ▼
┌─────────────────────┐
│ Organic/natural?    │──Yes──▶ + shader-noise
└─────────────────────┘
     │
     ▼
┌─────────────────────┐
│ Geometric shapes?   │──Yes──▶ + shader-sdf
└─────────────────────┘
     │
     ▼
┌─────────────────────┐
│ Visual polish?      │──Yes──▶ + shader-effects
└─────────────────────┘

Reference

See individual skill files for detailed patterns:

/mnt/skills/user/shader-fundamentals/SKILL.md
/mnt/skills/user/shader-noise/SKILL.md
/mnt/skills/user/shader-sdf/SKILL.md
/mnt/skills/user/shader-effects/SKILL.md
Weekly Installs
51
Repository
bbeierle12/skil…p-claude
GitHub Stars
8
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass