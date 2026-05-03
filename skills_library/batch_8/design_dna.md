---
title: design-dna
url: https://skills.sh/zanwei/design-dna/design-dna
---

# design-dna

skills/zanwei/design-dna/design-dna
design-dna
Installation
$ npx skills add https://github.com/zanwei/design-dna --skill design-dna
SKILL.md
Design DNA

A 3-phase workflow for extracting, structuring, and applying design identity across three dimensions:

Design System — measurable tokens (color, typography, spacing, layout, shape, elevation, motion, components)
Design Style — qualitative perception (mood, visual language, composition, imagery, interaction feel, brand voice)
Visual Effects — special rendering (Canvas, WebGL, 3D, particles, shaders, scroll effects, cursor effects, SVG animations, glassmorphism, etc.)
Phases
Phase 1: Structure — Output the Schema

When the user asks for the structural dimensions or schema:

Read references/schema.md
Present the full schema with field descriptions
Explain the three dimensions and their roles:
design_system: What you can measure — exact hex values, pixel sizes, rem scales
design_style: What you can feel — mood, personality, composition strategy
visual_effects: What you can see but can't express in CSS alone — WebGL scenes, particle systems, shader distortions, scroll-driven animations
Ask if the user wants to customize or extend any dimensions
Phase 2: Analyze — Extract DNA from References

When the user provides images, screenshots, or links representing a target design style:

Read references/schema.md for the full field list
For each reference provided:
If image/screenshot: analyze visual properties directly
If URL: fetch and analyze the page's visual design
For every field in the schema, extract or infer a value from the references
When multiple references conflict, note the dominant pattern and mention variants
Output a complete Design DNA JSON — every field populated, no empty strings
After output, ask: "Want to adjust any values before using this for generation?"

Analysis approach per dimension:

Dimension 1: design_system
color: Extract dominant palette via visual sampling. Primary by area dominance, secondary by supporting role, accent by CTA usage. Map neutral scale from lightest background to darkest text.
typography: Identify font families by visual characteristics (geometric, humanist, serif class). Estimate scale ratios from heading/body size relationships.
spacing: Assess density by element proximity. Measure rhythm by section gap consistency.
layout: Identify grid by content alignment patterns. Note max-width, column count, asymmetry.
shape: Measure border-radius by comparing to element height. Note border and divider presence.
elevation: Classify shadow softness, spread, and layering approach.
motion: If observable (video/interactive), note easing curves and duration feel.
Dimension 2: design_style
Synthesize holistic impressions — mood, personality, composition strategy
Compare against genre archetypes (SaaS, editorial, brutalist, etc.)
Note ornamentation level and whitespace philosophy
Dimension 3: visual_effects
From code: Scan for <canvas>, WebGL contexts, Three.js/Pixi.js imports, GSAP/Lottie usage, custom shaders, IntersectionObserver scroll triggers, SVG <animate> elements
From screenshots: Describe visible effects that go beyond standard CSS — glowing particles, 3D object renders, noise textures, gradient animations, parallax depth, cursor trails, text distortions, glassmorphic surfaces. Note these in composite_notes when exact implementation can't be determined.
From video/interaction demos: Note scroll behaviors, hover distortions, transition choreography, loading sequences
Set enabled: false for any effect category not present in the reference
Rate overview.effect_intensity and overview.performance_tier based on what's observed
Phase 3: Generate — Apply DNA to Content

When the user provides DNA JSON + content to design:

Read references/generation-guide.md
Parse the DNA JSON and extract all tokens across three dimensions
Build CSS custom properties from design_system values
Apply design_style qualitative fields to guide subjective design decisions
When the design needs assets or source materials, fetch them from the original source whenever possible. If the user provided a URL, retrieve the real asset from that URL instead of recreating, approximating, or substituting it.
Implement visual_effects using appropriate technologies:
Lightweight effects → CSS animations, SVG, vanilla JS
Medium effects → Canvas 2D, GSAP, Lottie
Heavy effects → Three.js, custom GLSL shaders, Pixi.js
Generate the design output (default: self-contained HTML with inline CSS/JS)
Run quality checks from the generation guide

If the user provides only content without DNA JSON, ask whether to:

Analyze a reference first (go to Phase 2)
Use a described style (extract DNA from description, then generate)
Phase Combinations

Users may invoke any combination:

Phase 1 only: "Show me the design structure/schema"
Phase 2 only: "Analyze this design" (with images/links)
Phase 2 → 3: "Analyze this design and build me a landing page in the same style"
Phase 1 → 2 → 3: Full pipeline
Phase 3 only: User already has DNA JSON

Detect which phase(s) are needed from context and execute accordingly.

Weekly Installs
608
Repository
zanwei/design-dna
GitHub Stars
653
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn