---
title: react-best-practices
url: https://skills.sh/0xbigboss/claude-code/react-best-practices
---

# react-best-practices

skills/0xbigboss/claude-code/react-best-practices
react-best-practices
Installation
$ npx skills add https://github.com/0xbigboss/claude-code --skill react-best-practices
Summary

React patterns for hooks, effects, refs, and component design with escape hatch guidance.

Effects synchronize with external systems only (WebSocket, third-party libraries, browser APIs); most component logic should avoid Effects entirely
Common anti-patterns: derived state, expensive calculations, prop-change resets, and event handling all belong outside Effects—use render calculations, useMemo, key props, and event handlers instead
Effect dependencies must never be suppressed; use updater functions, move objects/functions inside Effects, and useEffectEvent for non-reactive logic to keep dependency lists correct
Always clean up subscriptions and event listeners; use ignore flags for data fetching to prevent stale updates
Refs store mutable values that don't affect rendering; never read or write ref.current during render, only in event handlers and Effects
SKILL.md
React Best Practices
Pair with TypeScript

When working with React, always load both this skill and typescript-best-practices together. TypeScript patterns (type-first development, discriminated unions, Zod validation) apply to React code.

Core Principle: Effects Are Escape Hatches

Effects let you "step outside" React to synchronize with external systems. Most component logic should NOT use Effects. Before writing an Effect, ask: "Is there a way to do this without an Effect?"

Decision Tree
Need to respond to user interaction? Use event handler
Need computed value from props/state? Calculate during render
Need cached expensive calculation? Use useMemo
Need to reset state on prop change? Use key prop
Need to synchronize with external system? Use Effect with cleanup
Need non-reactive code in Effect? Use useEffectEvent
Need mutable value that doesn't trigger render? Use ref
When to Use Effects

Synchronizing with external systems: browser APIs (WebSocket, IntersectionObserver), third-party non-React libraries, window/document event listeners, non-React DOM elements (video, maps).

When NOT to Use Effects
Derived state — calculate during render
Expensive calculations — use useMemo
Resetting state on prop change — use key prop
Responding to user events — use event handlers
Notifying parent of state changes — update both in the same event handler
Chains of effects — calculate derived state and update in one event handler
Refs
Use for values that don't affect rendering (timer IDs, DOM node references)
Never read or write ref.current during render; only in event handlers and effects
Use ref callbacks (not useRef in loops) for dynamic lists
Use useImperativeHandle to limit what parent can access
Custom Hooks
Share logic, not state — each call gets an independent state instance
Name useXxx only if it actually calls other hooks; otherwise use a regular function
Avoid lifecycle hooks (useMount, useEffectOnce) — use useEffect directly so the linter catches missing deps
Keep focused on a single concrete use case
Component Patterns
Controlled: parent owns state; uncontrolled: component owns state
Prefer composition with children over prop drilling
Treat boolean props that switch large component trees (isEditing, isThread, hideAttachments) as a composition smell; prefer separate composed components for distinct use cases
For complex reusable UI, prefer compound components with provider-scoped state/actions over monolithic components with many optional props
Use Context for scoped component families as well as truly global state, when it defines a local interface consumed by descendants
Render JSX directly for UI variation; avoid config-array mini-frameworks unless the config is real domain data
Lift the provider boundary when sibling or external controls need access to the same state/actions
Use flushSync when you need to read the DOM synchronously after a state update

See react-patterns.md for code examples and detailed patterns.

Weekly Installs
2.5K
Repository
0xbigboss/claude-code
GitHub Stars
43
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass