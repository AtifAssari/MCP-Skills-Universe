---
title: react-useeffect
url: https://skills.sh/softaworks/agent-toolkit/react-useeffect
---

# react-useeffect

skills/softaworks/agent-toolkit/react-useeffect
react-useeffect
Installation
$ npx skills add https://github.com/softaworks/agent-toolkit --skill react-useeffect
Summary

React useEffect best practices guide covering when to use Effects and superior alternatives.

Teaches the escape-hatch nature of Effects: use only for synchronizing with external systems, not for derived state, expensive calculations, or user event responses
Provides a decision tree and quick-reference table mapping common situations (data fetching, state derivation, prop changes) to the correct React pattern
Covers when NOT to use Effects: transforming data for render, handling user events, deriving state, and chaining state updates
Recommends alternatives including direct calculation during render, useMemo for expensive computations, key prop for state reset, and useSyncExternalStore for subscriptions
SKILL.md
You Might Not Need an Effect

Effects are an escape hatch from React. They let you synchronize with external systems. If there is no external system involved, you shouldn't need an Effect.

Quick Reference
Situation	DON'T	DO
Derived state from props/state	useState + useEffect	Calculate during render
Expensive calculations	useEffect to cache	useMemo
Reset state on prop change	useEffect with setState	key prop
User event responses	useEffect watching state	Event handler directly
Notify parent of changes	useEffect calling onChange	Call in event handler
Fetch data	useEffect without cleanup	useEffect with cleanup OR framework
When You DO Need Effects
Synchronizing with external systems (non-React widgets, browser APIs)
Subscriptions to external stores (use useSyncExternalStore when possible)
Analytics/logging that runs because component displayed
Data fetching with proper cleanup (or use framework's built-in mechanism)
When You DON'T Need Effects
Transforming data for rendering - Calculate at top level, re-runs automatically
Handling user events - Use event handlers, you know exactly what happened
Deriving state - Just compute it: const fullName = firstName + ' ' + lastName
Chaining state updates - Calculate all next state in the event handler
Decision Tree
Need to respond to something?
├── User interaction (click, submit, drag)?
│   └── Use EVENT HANDLER
├── Component appeared on screen?
│   └── Use EFFECT (external sync, analytics)
├── Props/state changed and need derived value?
│   └── CALCULATE DURING RENDER
│       └── Expensive? Use useMemo
└── Need to reset state when prop changes?
    └── Use KEY PROP on component

Detailed Guidance
Anti-Patterns - Common mistakes with fixes
Better Alternatives - useMemo, key prop, lifting state, useSyncExternalStore
Weekly Installs
3.5K
Repository
softaworks/agent-toolkit
GitHub Stars
1.7K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass