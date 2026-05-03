---
title: react19-concurrent-patterns
url: https://skills.sh/github/awesome-copilot/react19-concurrent-patterns
---

# react19-concurrent-patterns

skills/github/awesome-copilot/react19-concurrent-patterns
react19-concurrent-patterns
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill react19-concurrent-patterns
SKILL.md
React 19 Concurrent Patterns

React 19 introduced new APIs that complement the migration work. This skill covers two concerns:

Preserve existing React 18 concurrent patterns that must not be broken during migration
Adopt new React 19 APIs worth introducing after migration stabilizes
Part 1 Preserve: React 18 Concurrent Patterns That Must Survive the Migration

These patterns exist in React 18 codebases and must not be accidentally removed or broken:

createRoot Already Migrated by the R18 Orchestra

If the R18 orchestra already ran, ReactDOM.render → createRoot is done. Verify it's correct:

// CORRECT React 19 root (same as React 18):
import { createRoot } from 'react-dom/client';
const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

useTransition No Migration Needed

useTransition from React 18 works identically in React 19. Do not touch these patterns during migration:

// React 18 useTransition  unchanged in React 19:
const [isPending, startTransition] = useTransition();

function handleClick() {
  startTransition(() => {
    setFilteredResults(computeExpensiveFilter(input));
  });
}

useDeferredValue No Migration Needed
// React 18 useDeferredValue  unchanged in React 19:
const deferredQuery = useDeferredValue(query);

Suspense for Code Splitting No Migration Needed
// React 18 Suspense with lazy  unchanged in React 19:
const LazyComponent = React.lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <LazyComponent />
    </Suspense>
  );
}

Part 2 React 19 New APIs

These are worth adopting in a post-migration cleanup sprint. Do not introduce these DURING the migration stabilize first.

For full patterns on each new API, read:

references/react19-use.md the use() hook for promises and context
references/react19-actions.md Actions, useActionState, useFormStatus, useOptimistic
references/react19-suspense.md Suspense for data fetching (the new pattern)
Migration Safety Rules

During the React 19 migration itself, these concurrent-mode patterns must be left completely untouched:

# Verify nothing touched these during migration:
grep -rn "useTransition\|useDeferredValue\|Suspense\|startTransition" \
  src/ --include="*.js" --include="*.jsx" | grep -v "\.test\."


If the migrator touched any of these files, review the changes the migration should only have modified React API surface (forwardRef, defaultProps, etc.), never concurrent mode logic.

Weekly Installs
548
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass