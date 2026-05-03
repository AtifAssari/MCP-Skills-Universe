---
title: tuning-panel
url: https://skills.sh/petekp/agent-skills/tuning-panel
---

# tuning-panel

skills/petekp/agent-skills/tuning-panel
tuning-panel
Installation
$ npx skills add https://github.com/petekp/agent-skills --skill tuning-panel
SKILL.md
Tuning Panel Skill

Create bespoke parameter tuning panels that give users visual control over values they're iterating on. These panels surface all relevant parameters for the current task, enable real-time adjustment, and export tuned values in an LLM-friendly format.

Core Philosophy

Err on the side of exhaustive. When a user is tuning something, surface every parameter that could reasonably affect the outcome. Missing a parameter forces context-switching; having "too many" parameters costs only scroll distance.

Debug-mode only. Tuning panels should never appear in production. Use environment checks, build flags, or URL parameters.

Export changed values only. LLM exports should show only what was tuned, not all 100+ parameters.

Platform Selection
Platform	Library	Reference
React	Leva (recommended)	references/react-leva.md
SwiftUI	Native controls	references/swiftui.md
Vanilla JS	Tweakpane or dat.GUI	references/vanilla-js.md
Implementation Workflow
Step 1: Identify All Tunable Parameters

Analyze the code being tuned and extract every parameter that affects the output. See references/parameter-categories.md for exhaustive lists by domain.

Common categories:

Animation: duration, delay, easing, spring physics (stiffness, damping, mass)
Layout: padding, margin, gap, width, height, position
Visual: colors, opacity, shadows, borders, transforms
Typography: font size, line height, letter spacing, weight

Discovery strategies:

Search for magic numbers (any hardcoded numeric value)
Look for style objects (CSS-in-JS, inline styles, theme values)
Find animation definitions (Framer Motion, CSS transitions, SwiftUI animations)
Identify color values (hex, RGB, HSL anywhere in the file)
Check component props with numeric or color defaults
Examine CSS custom properties (--var-name declarations)
Step 2: Create Debug-Mode Panel

Wrap the tuning panel so it only appears in development:

React: process.env.NODE_ENV === 'development'
SwiftUI: #if DEBUG
Vanilla JS: URL parameter ?debug or environment check

See platform-specific references for code patterns.

Step 3: Implement Controls

Follow these principles:

Group related parameters using folders/sections
Use appropriate control types: sliders for numbers, color pickers for colors, dropdowns for enums
Set sensible min/max/step values based on the parameter domain
Include presets for common configurations
Add reset buttons to return to defaults
Step 4: Add LLM Export

Critical requirements:

Store defaults at initialization for comparison
Use tolerance for floats (e.g., Math.abs(a - b) > 0.001)
Filter to changed values only - don't show unchanged parameters
Format for readability - group by category, use human-readable names

Export format:

## Tuned Parameters for [ComponentName]

### Changed Values
- Duration: 300 → 450
- Spring Damping: 0.80 → 0.65
- Corner Radius: 12 → 16

### Apply These Values
Update the component at `src/components/Card.tsx:42` with the values above.


Why this matters:

A panel might expose 100+ parameters
Exporting all values wastes tokens and obscures what changed
The default → current format makes diffs scannable
Additional Resources
Reference Files
references/react-leva.md - Complete React/Leva implementation guide
references/swiftui.md - SwiftUI native controls and export patterns
references/vanilla-js.md - Tweakpane and dat.GUI for plain JS
references/parameter-categories.md - Exhaustive parameter lists by domain
Example Files
examples/react-leva-animation.tsx - Complete animation tuning panel
examples/export-format.md - Full LLM export template
Weekly Installs
28
Repository
petekp/agent-skills
GitHub Stars
4
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass