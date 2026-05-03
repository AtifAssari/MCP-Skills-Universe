---
title: react
url: https://skills.sh/hairyf/skills/react
---

# react

skills/hairyf/skills/react
react
Installation
$ npx skills add https://github.com/hairyf/skills --skill react
SKILL.md
React

The skill is based on React, generated at 2026-01-31.

React is a JavaScript library for building user interfaces. It lets you compose complex UIs from small and isolated pieces of code called "components". React uses a declarative paradigm that makes it easier to reason about your application and aims to be both efficient and flexible.

Core References
Topic	Description	Reference
useState	Hook for managing component state with direct updates	core-usestate
useEffect	Hook for synchronizing components with external systems	core-useeffect
useContext	Hook for reading and subscribing to context	core-usecontext
useRef	Hook for referencing values that don't trigger re-renders	core-useref
useReducer	Hook for managing complex state with a reducer function	core-usereducer
Suspense	Component for displaying fallback UI while content is loading	core-suspense
memo	Higher-order component for memoizing component renders	core-memo
createContext	API for creating context objects	core-createcontext
Fragment	Component for grouping elements without wrapper nodes	core-fragment
StrictMode	Component for enabling additional development checks	core-strictmode
Features
Performance Optimization
Topic	Description	Reference
useMemo	Hook for caching expensive calculations	features-usememo
useCallback	Hook for caching function definitions	features-usecallback
lazy	API for code splitting and lazy loading components	features-lazy
useTransition	Hook for non-blocking state updates	features-usetransition
useDeferredValue	Hook for deferring non-critical UI updates	features-usedeferredvalue
useLayoutEffect	Hook that fires synchronously before browser repaint	features-uselayouteffect
startTransition	API for marking non-blocking state updates	features-starttransition
Advanced Hooks
Topic	Description	Reference
useId	Hook for generating unique IDs for accessibility	features-useid
use	API for reading Promise and Context values	features-use
useActionState	Hook for managing form action state	features-useactionstate
useOptimistic	Hook for optimistic UI updates	features-useoptimistic
useInsertionEffect	Hook for CSS-in-JS libraries to inject styles	advanced-useinsertioneffect
useSyncExternalStore	Hook for subscribing to external stores	advanced-usesyncexternalstore
useImperativeHandle	Hook for customizing ref handles	advanced-useimperativehandle
useEffectEvent	Hook for extracting non-reactive logic from Effects	advanced-useeffectevent
useDebugValue	Hook for adding labels to custom hooks in DevTools	advanced-usedebugvalue
React DOM APIs
Topic	Description	Reference
createRoot	API for creating a root to render React components	react-dom-createroot
hydrateRoot	API for hydrating server-rendered HTML	react-dom-hydrateroot
createPortal	API for rendering children into different DOM nodes	react-dom-createportal
flushSync	API for forcing synchronous updates	react-dom-flushsync
React Server Components
Topic	Description	Reference
cache	API for caching function results in Server Components	rsc-cache
Advanced Components
Topic	Description	Reference
Profiler	Component for measuring rendering performance	advanced-profiler
Activity	Component for hiding and restoring UI state	features-activity
Testing
Topic	Description	Reference
act	Test helper for applying pending updates before assertions	testing-act
Best Practices
Topic	Description	Reference
Rules of Hooks	Fundamental rules for using React Hooks correctly	best-practices-rules-of-hooks
Component Purity	Rules for keeping React components and hooks pure	best-practices-purity
Key Recommendations
Use hooks at the top level - Never call hooks conditionally or in loops
Keep components pure - Components should be idempotent and have no side effects during render
Use useEffect for side effects - Synchronize with external systems using Effects
Memoize expensive calculations - Use useMemo for costly computations, useCallback for functions passed to memoized components
Code split with lazy - Use lazy and Suspense for route-based code splitting
Avoid premature optimization - Profile first, optimize only when needed
Use React Compiler - Consider using React Compiler for automatic memoization
Handle dependencies correctly - Always include all reactive values in Effect and memoization dependencies
Weekly Installs
70
Repository
hairyf/skills
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass