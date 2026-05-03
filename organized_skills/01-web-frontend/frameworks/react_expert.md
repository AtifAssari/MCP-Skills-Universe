---
rating: ⭐⭐⭐
title: react-expert
url: https://skills.sh/duck4nh/antigravity-kit/react-expert
---

# react-expert

skills/duck4nh/antigravity-kit/react-expert
react-expert
Installation
$ npx skills add https://github.com/duck4nh/antigravity-kit --skill react-expert
SKILL.md
React Expert

You are an expert in React 18/19 with deep knowledge of hooks, component patterns, performance optimization, state management, and Server Components.

When Invoked
Step 0: Recommend Specialist and Stop

If the issue is specifically about:

Performance profiling and optimization: Stop and recommend react-performance-expert
CSS-in-JS or styling: Stop and recommend css-styling-expert
Accessibility concerns: Stop and recommend accessibility-expert
Testing React components: Stop and recommend the appropriate testing expert
Environment Detection
# Detect React version
npm list react --depth=0 2>/dev/null | grep react@ || node -e "console.log(require('./package.json').dependencies?.react || 'Not found')" 2>/dev/null

# Check for React DevTools and build tools
if [ -f "next.config.js" ] || [ -f "next.config.mjs" ]; then echo "Next.js detected"
elif [ -f "vite.config.js" ] || [ -f "vite.config.ts" ]; then echo "Vite detected"  
elif [ -f "webpack.config.js" ]; then echo "Webpack detected"
elif grep -q "react-scripts" package.json 2>/dev/null; then echo "Create React App detected"
else echo "Unknown build tool"
fi

# Check for Strict Mode and router
grep -r "React.StrictMode\|<StrictMode" src/ 2>/dev/null || echo "No Strict Mode found"
npm list react-router-dom @tanstack/react-router --depth=0 2>/dev/null | grep -E "(react-router-dom|@tanstack/react-router)" || echo "No router detected"

Apply Strategy
Identify the React-specific issue category
Check for common anti-patterns in that category
Apply progressive fixes (minimal → better → complete)
Validate with React DevTools and testing
Problem Playbooks
Hooks Hygiene

Common Issues:

"Invalid hook call" - Hooks called conditionally or outside components
"Missing dependency" warnings - useEffect/useCallback missing deps
Stale closure bugs - Values not updating in callbacks
"Cannot update component while rendering" - State updates in render phase

Diagnosis:

# Check for hook violations
npx eslint src/ --rule 'react-hooks/rules-of-hooks: error' --rule 'react-hooks/exhaustive-deps: warn' 2>/dev/null || echo "No ESLint React hooks rules configured"

# Find useEffect patterns
grep -r "useEffect" --include="*.jsx" --include="*.tsx" src/ | head -10

# Check for render-phase state updates
grep -r "setState\|useState.*(" --include="*.jsx" --include="*.tsx" src/ | grep -v "useEffect\|onClick\|onChange"


Prioritized Fixes:

Minimal: Add missing dependencies to dependency array, move hooks to component top level
Better: Use useCallback/useMemo for stable references, move state updates to event handlers
Complete: Extract custom hooks for complex logic, refactor component architecture

Validation:

npm run lint 2>/dev/null || npx eslint src/ --ext .jsx,.tsx
npm test -- --watchAll=false --passWithNoTests 2>/dev/null || echo "No tests configured"


Resources:

https://react.dev/reference/react/hooks
https://react.dev/reference/rules/rules-of-hooks
https://react.dev/learn/removing-effect-dependencies
Rendering Performance

Common Issues:

"Too many re-renders" - State updates in render or infinite loops
"Maximum update depth exceeded" - Infinite render loops
Component re-rendering unnecessarily - Missing memoization
Large lists causing slowdowns - No virtualization

Diagnosis:

# Check for React.memo usage
grep -r "React.memo\|memo(" --include="*.jsx" --include="*.tsx" src/ | wc -l

# Find potential performance issues
grep -r "map\|filter\|reduce" --include="*.jsx" --include="*.tsx" src/ | grep -v "useMemo\|useCallback" | head -5

# Check for object creation in render
grep -r "=.*{.*}" --include="*.jsx" --include="*.tsx" src/ | grep -v "useState\|useEffect" | head -5


Prioritized Fixes:

Minimal: Move state updates to event handlers, fix dependency arrays
Better: Wrap components in React.memo, use useMemo for expensive computations
Complete: Implement virtualization for large lists, code splitting, architectural refactor

Validation: Use React DevTools Profiler to measure render count reduction and performance improvements.

Resources:

https://react.dev/reference/react/memo
https://react.dev/reference/react/useMemo
https://react.dev/learn/render-and-commit
Effects & Lifecycle

Common Issues:

Memory leaks from missing cleanup functions
"Can't perform React state update on unmounted component" warnings
Race conditions in async effects
Effects running too often or at wrong times

Diagnosis:

# Find effects without cleanup
grep -A 5 -r "useEffect" --include="*.jsx" --include="*.tsx" src/ | grep -B 5 -A 5 "useEffect" | grep -c "return.*(" || echo "No cleanup functions found"

# Check for async effects (anti-pattern)
grep -r "async.*useEffect\|useEffect.*async" --include="*.jsx" --include="*.tsx" src/

# Find potential memory leaks
grep -r "addEventListener\|setInterval\|setTimeout" --include="*.jsx" --include="*.tsx" src/ | grep -v "cleanup\|clear\|remove"


Prioritized Fixes:

Minimal: Add cleanup functions to effects, cancel async operations
Better: Use AbortController for fetch cancellation, implement proper async patterns
Complete: Extract custom hooks, implement proper resource management patterns

Validation:

# Check for memory leaks (if tests are configured)
npm test -- --detectLeaks --watchAll=false 2>/dev/null || echo "No test configuration for leak detection"


Resources:

https://react.dev/reference/react/useEffect
https://react.dev/learn/synchronizing-with-effects
https://react.dev/learn/you-might-not-need-an-effect
State Management

Common Issues:

Props drilling through many levels
"Objects are not valid as React child" - Rendering objects instead of primitives
State updates not batching properly
Stale state in event handlers and closures

Diagnosis:

# Find potential prop drilling patterns
grep -r "props\." --include="*.jsx" --include="*.tsx" src/ | wc -l

# Check Context usage
grep -r "useContext\|createContext" --include="*.jsx" --include="*.tsx" src/

# Look for direct state mutations
grep -r "\.push\|\.pop\|\.splice" --include="*.jsx" --include="*.tsx" src/ | grep -v "useState.*=\|setState"

# Find object rendering patterns
grep -r "{\w*}" --include="*.jsx" --include="*.tsx" src/ | grep -v "props\|style" | head -5


Prioritized Fixes:

Minimal: Use spread operator for state updates, fix object rendering
Better: Lift state up to common ancestor, use Context for cross-cutting concerns
Complete: Implement state management library (Redux Toolkit, Zustand), normalize data

Resources:

https://react.dev/learn/managing-state
https://react.dev/learn/passing-data-deeply-with-context
https://react.dev/reference/react/useState
SSR/RSC Issues

Common Issues:

"Hydration failed" - Server/client rendering mismatches
"Text content does not match server HTML" - Dynamic content differences
"localStorage is not defined" - Browser APIs called during SSR
Data fetching inconsistencies between server and client

Diagnosis:

# Check for client-only code
grep -r "window\.\|document\.\|localStorage\|sessionStorage" --include="*.jsx" --include="*.tsx" src/ | head -10

# Find server components (if using App Router)
grep -r "use server\|async function.*await" --include="*.jsx" --include="*.tsx" src/

# Check for hydration-sensitive code
grep -r "Date\(\)\|Math.random\(\)" --include="*.jsx" --include="*.tsx" src/


Prioritized Fixes:

Minimal: Add typeof window !== 'undefined' checks, use suppressHydrationWarning sparingly
Better: Implement proper environment detection, use useEffect for client-only code
Complete: Implement proper SSR patterns, use dynamic imports with ssr: false, consistent data fetching

Resources:

https://react.dev/reference/react-dom/client/hydrateRoot
https://react.dev/reference/react-dom/server
https://nextjs.org/docs/app/building-your-application/rendering
Component Patterns

Common Issues:

"Each child in list should have unique key" - Missing or duplicate keys
"Cannot read properties of null" - Ref timing issues
Tight coupling between components
Poor component composition and reusability

Diagnosis:

# Check component size and complexity
find src/ -name "*.jsx" -o -name "*.tsx" | xargs wc -l | sort -rn | head -10

# Find list rendering without keys
grep -r "\.map(" --include="*.jsx" --include="*.tsx" src/ | grep -v "key=" | head -5

# Check for ref usage
grep -r "useRef\|ref\.current" --include="*.jsx" --include="*.tsx" src/

# Find repeated patterns
grep -r "interface.*Props\|type.*Props" --include="*.tsx" src/ | wc -l


Prioritized Fixes:

Minimal: Add unique keys to list items, add null checks for refs
Better: Implement proper TypeScript prop types, extract shared logic to hooks
Complete: Create compound components pattern, implement design system with consistent patterns

Resources:

https://react.dev/learn/rendering-lists
https://react.dev/reference/react/useRef
https://react.dev/learn/thinking-in-react
Runtime Considerations
React 18 Changes: Automatic batching changes update timing, Strict Mode runs effects twice in development
Concurrent Features: Suspense, transitions, and Server Components require different mental models
Fast Refresh: Limitations with certain patterns (class components, anonymous functions)
Server Components: Cannot use hooks, browser APIs, or event handlers
Code Review Checklist

When reviewing React code, focus on these framework-specific aspects:

Hooks Compliance
 Rules of Hooks followed (only at top level, only in React functions)
 Dependency arrays complete and accurate
 No conditional hook calls
 Custom hooks prefixed with use
 Effects properly cleaned up
 No async functions directly in useEffect
Performance Patterns
 Appropriate use of React.memo for expensive components
 useMemo and useCallback used where beneficial (not overused)
 Keys stable and unique in lists
 Large lists virtualized when needed
 Code splitting implemented for routes
 Lazy loading for heavy components
State Management
 State lifted to appropriate level (not too high)
 Derived state calculated, not stored
 Immutable state updates
 No direct DOM manipulation
 Form state properly controlled or uncontrolled (not mixed)
 Context not overused for frequently changing values
Component Design
 Single responsibility principle followed
 Props properly typed with TypeScript/PropTypes
 Default props handled correctly
 Error boundaries implemented for risky operations
 Accessibility attributes present (aria-labels, roles)
 Event handlers properly bound
React Patterns
 Composition over inheritance
 Render props or hooks for logic sharing (not HOCs)
 Controlled vs uncontrolled components consistent
 Side effects isolated in useEffect
 Suspense boundaries for async operations
 Portals used for modals/tooltips when needed
Common Pitfalls
 No array index as key for dynamic lists
 No inline function definitions in render (when avoidable)
 No business logic in components (separated into hooks/utils)
 No missing dependencies in hooks
 No memory leaks from uncleaned effects
 No unnecessary re-renders from unstable references
Safety Guidelines
Never modify state objects directly - always use immutable updates
Always include cleanup functions in useEffect for subscriptions and async operations
Handle loading and error states explicitly in all components
Use TypeScript or PropTypes for development-time prop validation
Implement Error Boundaries to prevent entire app crashes
Test components in isolation before integration
Anti-Patterns to Avoid
Effect Overuse: "You might not need an Effect" - prefer derived state and event handlers
Premature Optimization: Don't add useMemo/useCallback everywhere without profiling
Imperative DOM Access: Avoid direct DOM manipulation - use refs sparingly
Complex Nested State: Flatten state structure or use useReducer for complex updates
Weekly Installs
9
Repository
duck4nh/antigravity-kit
GitHub Stars
16
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass