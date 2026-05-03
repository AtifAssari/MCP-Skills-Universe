---
title: swiftui
url: https://skills.sh/petekp/claude-code-setup/swiftui
---

# swiftui

skills/petekp/claude-code-setup/swiftui
swiftui
Installation
$ npx skills add https://github.com/petekp/claude-code-setup --skill swiftui
SKILL.md
SwiftUI Excellence Playbook

Tactical guide for designing and building world-class SwiftUI interfaces—the kind that feel at home next to Apple's own apps.

Six Non-Negotiables
Content first — UI is a frame, not the painting
System components unless measured reason not to — buy accessibility, platform behavior, design updates for free
Design for states, not screens — every screen handles: loading, empty, error, offline, partial, permission denied
Accessibility is a constraint — Dynamic Type, VoiceOver, Reduce Motion/Transparency, Increased Contrast
Performance is a feature — "feels instant" interactions, instrument when hitches occur
Coherence over cleverness — best interfaces feel inevitable
Quick Reference: ADA Rubric
Category	Requirement
Delight	Micro-delight at success moments only, never reduces clarity
Innovation	In discovery, state communication, simplifying complexity
Interaction	Predictable, direct, forgiving, platform-appropriate
Inclusivity	Dynamic Type XXL+, VoiceOver, no color-only meaning, reduced motion
Visuals	Consistent rhythm, coherent materials, restrained tint
Design Workflow (Step-by-Step)
Define experience — 10-line spec: goal, primary action, states, edge cases, platforms
Sketch IA — TabView vs NavigationSplitView vs deep navigation
Design hierarchy — one hero, one primary CTA per moment, progressive disclosure
Build tokens first — spacing, radius, typography, motion, colors
Build components — cards, rows, buttons, empty states, filters
Integrate structure — NavigationStack, NavigationSplitView, TabView, Sheets
Add motion — only what improves comprehension and causality
Accessibility + performance pass — Dynamic Type, VoiceOver, Instruments
Liquid Glass Quick Rules (iOS 26+)

Do:

Use glass for navigation/control layer floating above content
Group nearby glass in GlassEffectContainer
Use glassEffect(.interactive) for custom controls
Use glassEffectID for morphing transitions

Don't:

Glass on content layer (tables, documents)
Glass on glass stacking
Tint everything — only primary actions/meaning
Custom backgrounds behind toolbars (let system handle scroll edge effects)
Layout Essentials
Container	Use For
List	Large datasets, selection, swipe actions, edit mode
ScrollView + LazyVStack	Custom surfaces, cards, mixed content
Grid	Forms, settings, dense structured layouts
LazyVGrid	Responsive galleries
NavigationSplitView	iPad/Mac hierarchical apps
NavigationStack	Deep navigation flows
Animation Principles
Motion communicates causality, hierarchy, continuity
State-driven animation, not imperative choreography
Springs for organic UI, ease-in/out for fades
Custom transitions for signature moments only
Always provide Reduce Motion fallback
Performance Rules
Rule	Implementation
Body must be cheap	No sorting, filtering, formatting, I/O in body
Stable identity	ForEach(items, id: \.id) not \.self, no UUID() in body
Dependency hygiene	Keep @State local, pass Binding not whole model
Instrument	Use SwiftUI instrument (Instruments 26) for hitches
Accessibility Checklist
 System text styles, no clipping at XXL+
 Layout adapts (stacks turn vertical, rows multi-line)
 VoiceOver labels/hints on non-obvious controls
 Focus order matches reading order
 44×44pt minimum touch targets
 Reduced Motion removes parallax, uses opacity
 Reduced Transparency increases separation
Component Primitives (Build These)
Screen scaffold
Section header
Card surface
List row
Primary/secondary/icon buttons
Empty state
Loading skeleton
Error banner
Form field row
Chip/tag/pill
Full Reference

For complete implementation patterns, code recipes, design tokens, Liquid Glass details, and the full ADA review checklist:

See: swiftui-playbook.md

Weekly Installs
39
Repository
petekp/claude-code-setup
GitHub Stars
35
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass