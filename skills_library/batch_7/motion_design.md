---
title: motion-design
url: https://skills.sh/lottiefiles/motion-design-skill/motion-design
---

# motion-design

skills/lottiefiles/motion-design-skill/motion-design
motion-design
Installation
$ npx skills add https://github.com/lottiefiles/motion-design-skill --skill motion-design
SKILL.md
Motion Design Skill
When to Apply

Use this skill when:

Creating UI animations (buttons, cards, modals, page transitions)
Designing micro-interactions and feedback animations
Building loading, success, or error states
Animating illustrations or decorative elements
Planning scroll-triggered or progress-based animations
Establishing brand motion identity
Choreographing multi-element sequences

Decision tree:

Does it serve a functional purpose (feedback, guidance)? → Timing rules for responsiveness
Does it express brand personality? → Motion Personality archetypes
Does it tell a story or guide attention? → Disney principles + choreography
Is this a complex multi-element scene? → 1/3 Rule + stagger patterns
Quick Reference: 8-Step Checklist

Before creating any animation:

Emotional target? — joy, calm, urgency, elegance
Motion Personality? — Playful, Premium, Corporate, Energetic
Primary property? — position, scale, rotation, opacity
Duration? — see duration table below
Easing family? — entrance=decelerate, exit=accelerate
Hero element? — apply staging principles
Secondary + ambient layers? — add richness
1/3 rules? — motion distance, simultaneous elements
Three Pillars (CRITICAL)

Every animation must satisfy three pillars before any technical decisions:

Pillar	Question	Drives
Emotional Intent	What should the viewer FEEL?	Easing, timing, amplitude
Visual Narrative	What's the micro-story?	Setup → Action → Resolution
Motion Craft	How do we make it believable?	Physics, secondary motion, paths

Three motion layers (flat animation = missing layers):

Primary: Main action the viewer follows
Secondary: Supporting richness (shadows, icons shifting)
Ambient: Background life (gradients, subtle pulses)

Deep dive: director/core-philosophy.md

Motion Personality

Select ONE archetype per project. Apply consistently.

Archetype	Duration	Easing	Overshoot	Keywords
Playful	150-300ms	ease-out-back	10-20%	fun, whimsical, bouncy, cute
Premium	350-600ms	cubic-bezier(0.4,0,0.2,1)	0%	elegant, minimal, luxury, sophisticated
Corporate	200-400ms	cubic-bezier(0.2,0,0,1)	0-3%	clean, professional, business, dashboard
Energetic	100-250ms	ease-out-expo	15-30%	dynamic, energetic, bold, exciting

Default: Corporate for UI, Playful for illustrations.

Brand Motion Identity — define three constants:

Signature easing: One curve for 80% of animations
Duration palette: 3 durations (quick / standard / slow)
Entrance pattern: One consistent entry style

Deep dive: director/motion-personality.md

Property Selection
Effect Goal	Primary Property	Secondary Properties
Entrance/Exit	position	opacity, scale
Emphasis/Attention	scale	rotation (subtle), opacity pulse
State Change	opacity, color	scale (press feedback)
Direction/Flow	position	rotation (follow path)
Depth/3D Feel	scale + shadow	position (parallax)
Loading/Progress	rotation (spinner)	scale, opacity pulse
Success	scale (pop)	color, rotation (checkmark draw)
Error/Alert	position (shake)	color, rotation (wobble)

Simplicity threshold: Use the minimum properties needed. One = direct. Two = polished. Three+ = potentially overwhelming.

Deep dive: reference/property-selection.md

Duration Table
Element Type	Duration	Rationale
Tooltip / micro-feedback	80-120ms	Must feel instant
Button press / toggle	120-180ms	Responsive feedback
Icon transition	150-250ms	Clear state change
Card enter / exit	200-350ms	Spatial awareness
Modal / dialog	300-400ms	Focus shift
Page transition	400-600ms	Context switch
Dramatic reveal	600-1200ms	Theatrical build

Distance scales duration: 100px = base. 200px = 1.3x. 400px = 1.6x.

Enter > Exit: Entrances 30-50% longer than exits. Users care about what appears.

Interactive feedback:

Hover: <100ms
Press: <150ms
Release/settle: 200-300ms
Error shake: 300-400ms (2-3 oscillations)

Deep dive: reference/timing-easing-tables.md

Easing Selection

Directional rules:

Entrance → decelerate (fast start, gentle landing): ease-out family
Exit → accelerate (gentle start, fast departure): ease-in family
On-screen → smooth both ends: ease-in-out family
Looping ambient → seamless: sine-based ease-in-out

Industry standards:

Standard	Cubic Bezier	Use For
Material Design 3	(0.2, 0, 0, 1)	Default on-screen
MD3 Emphasized	(0.05, 0.7, 0.1, 1)	Entrances, attention
MD3 Accelerate	(0.3, 0, 1, 1)	Exits, dismissals
Apple HIG	(0.25, 0.1, 0.25, 1)	Standard iOS
Snappy UI	(0.2, 0, 0, 1)	Fast, decisive
Gentle float	(0.4, 0, 0.2, 1)	Ambient, background
Bounce settle	(0.175, 0.885, 0.32, 1.275)	Overshoot, playful

Material-based easing:

Material	Duration Scale	Overshoot
Rigid (metal, stone)	1.2x	0%
Elastic (rubber, gel)	0.8x	15-25%
Fluid (water, paint)	1.5x	5%
Paper (cards, sheets)	1.0x	3-5%
Gas (smoke, fog)	2.0x	0%
Glass (brittle)	0.9x	0%

Deep dive: reference/timing-easing-tables.md

Common Patterns
Button Press (Playful)
Anticipation: Scale to 0.97 (50ms, ease-out)
Squash: Scale to [1.04, 0.96] (100ms, ease-in)
Follow through: Overshoots to 1.02, settles to 1.0 (spring, 200ms)
Secondary: Shadow shrinks during press, icon shifts down 2px
Total: ~150ms press + 200ms settle
Card Entrance (Premium)
Start: 20px below target, opacity 0
Path: Slight curve (10px X offset at midpoint)
Easing: ease-out-cubic deceleration
Follow through: Shadow arrives 50ms after card
Secondary: Content fades in 100ms after card lands
Staging: Other cards dim to 80%
Success State (Playful)
Primary: Scale pop with ease-out-back
Secondary: Checkmark draws in
Ambient: Subtle particle burst
Color: Green fill
Total: 300-400ms
Error Shake (Corporate)
Primary: Position oscillates 2-3 times, ±10-15px horizontal
Easing: ease-in-out for sharp stops
Color: Red tint
Total: 300-400ms
No overshoot: Errors feel firm

More patterns: patterns/entrance-exit.md | patterns/state-feedback.md

Choreography Essentials

Coordinated entry:

Lead with the hero — primary element enters first or most prominently
Spatial consistency — all elements enter from same direction
Counter-motion — hero moves right → ambient moves left at 20-30% speed

1/3 Rule (distance): No motion travels more than 1/3 of screen without a keyframe change.

1/3 Rule (elements): With 3+ elements, no more than 1/3 in active motion simultaneously.

Stagger budgets:

Pattern	Delay	Total Budget	Use Case
Micro cascade	20-40ms	<200ms	List items, grid cells
Standard	50-100ms	<400ms	Cards, panels, nav
Dramatic	100-200ms	<600ms	Hero sections
Wave	30-60ms	<500ms	Data visualizations

Critical: Total stagger must stay under 500ms.

Deep dive: director/choreography.md

Emotion-to-Motion Map
Emotion	Character	Path	Easing	Duration
Joy	Bouncy, arcs	Curved, upward	ease-out-back	200-400ms
Calm	Smooth, flowing	Gentle curves	sine ease-in-out	500-1000ms
Urgency	Sharp, fast	Straight lines	ease-out	100-200ms
Sadness	Slow, downward	Drooping curves	cubic ease-in-out	600-1200ms
Surprise	Sudden, expanding	Radial outward	ease-out-expo	150-300ms
Elegance	Slow, controlled	Long arcs	(0.4,0,0.2,1)	400-700ms
Playfulness	Bouncy, irregular	Arcs, squiggly	ease-out-back	200-350ms

Path as language: Angular = tense. Curved = friendly. Spiral = whimsical. Diagonal = purposeful. Vertical = growth/weight. Horizontal = progress.

Deep dive: director/emotion-mapping.md

Weight Classification
Weight	Examples	Duration	Overshoot	Easing
Heavy	Modals, overlays	300-500ms	0%	Gentle, high damping
Medium	Cards, panels	200-350ms	3-5%	Moderate
Light	Tooltips, badges, icons	80-200ms	5-15%	Responsive
Quality Rules
CRITICAL — never break
Never linear for spatial movement — always use easing curves (linear only for spinners, progress bars)
Never opacity-only for important state changes — combine with position or scale
Never exceed 1/3 screen without intermediate keyframe
Always three motion layers — primary + secondary + ambient
HIGH — strongly follow
Match duration to element type (see tables)
Use directional easing (ease-out entrance, ease-in exit)
Apply Disney principles (especially anticipation, follow-through)
Maintain consistent personality across scene

Full checklist: reference/quality-checklist.md

Troubleshooting Quick Reference
Problem	Likely Cause	Fix
Looks robotic	Linear easing or no arcs	Add easing curves + arc paths
Feels too slow	Duration too long for element type	Check duration table, use ease-out
Feels cheap/flat	Missing secondary + ambient	Add shadow motion + background life
Too distracting	Too many elements moving	Apply 1/3 rule, reduce amplitude
No personality	Generic easing everywhere	Apply personality archetype consistently

Deep dive: reference/troubleshooting.md

File Reference

Philosophy (director/):

core-philosophy.md — Three Pillars deep dive
decision-framework.md — Full decision pipeline
disney-principles.md — 12 principles, UI-adapted
motion-personality.md — 4 archetypes + brand identity
emotion-mapping.md — Emotion → motion + color psychology
choreography.md — Multi-element coordination
narrative-structure.md — Micro-story framework
context-adaptation.md — Platform, a11y, performance

Reference (reference/):

timing-easing-tables.md — Duration + easing lookups
property-selection.md — Property communication guide
troubleshooting.md — Animation smells + fixes
quality-checklist.md — Evaluation criteria

Patterns (patterns/):

entrance-exit.md — Entrance/exit recipes
state-feedback.md — Success, error, loading, hover
ambient-continuous.md — Looping, breathing, parallax
multi-element.md — Stagger + choreography recipes
Weekly Installs
935
Repository
lottiefiles/mot…gn-skill
GitHub Stars
94
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass