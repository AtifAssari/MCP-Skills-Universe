---
title: react-useeffect
url: https://skills.sh/davila7/claude-code-templates/react-useeffect
---

# react-useeffect

skills/davila7/claude-code-templates/react-useeffect
react-useeffect
Originally fromsoftaworks/agent-toolkit
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill react-useeffect
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
382
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass