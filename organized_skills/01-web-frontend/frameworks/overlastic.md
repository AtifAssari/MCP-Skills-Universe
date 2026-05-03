---
rating: ⭐⭐
title: overlastic
url: https://skills.sh/hairyf/skills/overlastic
---

# overlastic

skills/hairyf/skills/overlastic
overlastic
Installation
$ npx skills add https://github.com/hairyf/skills --skill overlastic
Summary

Promise-based modal and dialog library with imperative and declarative modes for React, Vue, and Svelte.

Supports three frameworks (React, Vue 3, Svelte) with framework-specific integration patterns and hooks like useDisclosure
Offers both imperative control via constructors and deferred promises, and declarative usage directly in templates/JSX
Includes provider pattern for context inheritance, custom component integration, and external lifecycle control
Components automatically destroy after configured duration when promises resolve or reject
SKILL.md

Based on Overlastic v0.8.7. A promise-based modal/dialog/popup library supporting React, Vue, and Svelte.

Core References
Topic	Description	Reference
Constructor	Core method for creating overlay constructors	core-constructor
Deferred	Promise variation with external control methods	core-deferred
Global Functions	Utilities for mounting elements and name management	core-defines
useDisclosure	Hook for managing overlay lifecycle and state	core-disclosure
Framework References
Topic	Description	Reference
React Integration	Using Overlastic with React components	framework-react
Vue Integration	Using Overlastic with Vue 3 components	framework-vue
Svelte Integration	Using Overlastic with Svelte components	framework-svelte
Advanced References
Topic	Description	Reference
Provider Pattern	Using OverlaysProvider for context inheritance	advanced-provider
Custom Components	Integrating existing component libraries	advanced-customization
External Control	Controlling overlay lifecycle from outside	advanced-external-control
Declarative Usage	Using overlays in templates/JSX	advanced-declarative
Key Concepts
Constructor: Receives component, props, and options to mount overlays
Deferred: Promise-like object with confirm and cancel methods for external control
Mount Options: Configuration for container, ID, index, and deferred instance
Lifecycle: Components are destroyed after duration ends when deferred resolves/rejects
Imperative Usage: defineOverlay and renderOverlay for callback-based invocation
Declarative Usage: Components can be used in templates/JSX with props
Provider Pattern: OverlaysProvider for context inheritance
Dual Mode Support: Components work in both imperative and declarative modes
Weekly Installs
552
Repository
hairyf/skills
GitHub Stars
15
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass