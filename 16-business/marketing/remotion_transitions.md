---
title: remotion-transitions
url: https://skills.sh/ashad001/remotion-transitions/remotion-transitions
---

# remotion-transitions

skills/ashad001/remotion-transitions/remotion-transitions
remotion-transitions
Installation
$ npx skills add https://github.com/ashad001/remotion-transitions --skill remotion-transitions
SKILL.md
Remotion Custom Transitions

This skill teaches you how to build production-grade, high-energy custom transitions in Remotion using the TransitionPresentation API — the same pattern used in Fyltr's Instagram Reel campaign.

Quick Reference
Custom Transition Pattern — The TransitionPresentation API, the exact component shape, and how timing works
Transition Catalog — 6 battle-tested transitions with full source: Striped Slam, Zoom Punch, Diagonal Reveal, Emerald Burst, Vertical Shutter, Glitch Slam
Animation Math — Easing functions, stagger formulas, spring configs, and the clamp extrapolation pattern used throughout
Core Concept

Remotion's @remotion/transitions package exposes a TransitionPresentation type. You implement a component that receives:

presentationProgress — 0 at transition start → 1 at transition end
presentationDirection — "exiting" (old scene) or "entering" (new scene)
children — the scene being wrapped

The same component wraps both scenes simultaneously. You animate different things depending on direction.

Golden Rules
Never use CSS transitions/animations — all motion via interpolate() / spring() driven by presentationProgress
Never use useCurrentFrame() inside a transition component — use presentationProgress only
Always return { component, props: {} } — the props object must exist even if empty
Create instances outside components at module level to keep them stable across re-renders
Pair with linearTiming (for dramatic frame-perfect transitions) or springTiming (for springy physics)
When to Load References
Building a new custom transition → load custom-transition-pattern.md first
Copying/adapting an existing effect → load transition-catalog.md
Debugging timing or easing math → load animation-math.md
Weekly Installs
123
Repository
ashad001/remoti…nsitions
GitHub Stars
58
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass