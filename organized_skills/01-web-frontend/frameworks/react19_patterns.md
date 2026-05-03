---
rating: ⭐⭐
title: react19-patterns
url: https://skills.sh/qingqishi/shiqingqi.com/react19-patterns
---

# react19-patterns

skills/qingqishi/shiqingqi.com/react19-patterns
react19-patterns
Installation
$ npx skills add https://github.com/qingqishi/shiqingqi.com --skill react19-patterns
SKILL.md
React 19 Patterns
Overview

This project uses React 19 with the React Compiler enabled. This changes how you should write React code, especially around Context and optimization.

React 19 Context Pattern
Use Shorthand Syntax

React 19 introduces shorthand syntax for Context providers.

✅ Correct (React 19):

<MyContext value={someValue}>
  <ChildComponents />
</MyContext>


❌ Incorrect (Old pattern):

<MyContext.Provider value={someValue}>
  <ChildComponents />
</MyContext.Provider>

Use use() Hook Instead of useContext()

React 19 introduces the use() hook for consuming context.

✅ Correct (React 19):

import { use } from "react";
import { MyContext } from "./MyContext";

function MyComponent() {
  const value = use(MyContext);
  return <div>{value}</div>;
}


❌ Incorrect (Old pattern):

import { useContext } from "react";
import { MyContext } from "./MyContext";

function MyComponent() {
  const value = useContext(MyContext);
  return <div>{value}</div>;
}

React Compiler Enabled
No Manual Memoization Needed

The React Compiler automatically optimizes components and handles memoization. Do not use manual memoization patterns.

✅ Correct (React Compiler handles it):

function MyComponent({ items }) {
  // React Compiler automatically memoizes this computation
  const filteredItems = items.filter((item) => item.active);

  // React Compiler automatically stabilizes this function reference
  const handleClick = (id) => {
    console.log(id);
  };

  return (
    <div>
      {filteredItems.map((item) => (
        <button key={item.id} onClick={() => handleClick(item.id)}>
          {item.name}
        </button>
      ))}
    </div>
  );
}


❌ Incorrect (Manual memoization not needed):

import { useMemo, useCallback, memo } from "react";

function MyComponent({ items }) {
  // ❌ Don't use useMemo - React Compiler handles this
  const filteredItems = useMemo(
    () => items.filter((item) => item.active),
    [items],
  );

  // ❌ Don't use useCallback - React Compiler handles this
  const handleClick = useCallback((id) => {
    console.log(id);
  }, []);

  return <div>...</div>;
}

// ❌ Don't use memo() - React Compiler handles this
export default memo(MyComponent);

React 19 ViewTransition + Suspense Pattern
The Hydration Issue

When using <ViewTransition> to wrap content that includes Suspense boundaries, you may encounter hydration errors if some children are in Suspense while others are not.

Error Message:

A tree hydrated but some attributes of the server rendered HTML didn't match the client properties.
This won't be patched up. This can happen if a SSR-ed Client Component used...
Specifically: style={{view-transition-name:"_T_0_"}}


Root Cause:

ViewTransition uses a "just-in-time" mechanism to apply view-transition-name styles only when transitions trigger
During SSR hydration, content reveals from non-Suspense children trigger ViewTransition activation
This causes the client to apply styles during hydration that weren't in the server HTML
React detects the mismatch and logs a hydration warning
The Solution: Consistent Suspense Boundaries

✅ Correct (All content in Suspense):

<ViewTransition>
  <Suspense fallback={<HeaderSkeleton />}>
    <Header />
  </Suspense>
  <Suspense fallback={null}>{children}</Suspense>
</ViewTransition>


❌ Incorrect (Mixed Suspense/non-Suspense):

<ViewTransition>
  <Suspense fallback={<HeaderSkeleton />}>
    <Header />
  </Suspense>
  {children} {/* NOT in Suspense - causes hydration error! */}
</ViewTransition>


Alternative (Suspense outside ViewTransition):

<Suspense fallback={<LoadingSkeleton />}>
  <ViewTransition>
    <Header />
    {children}
  </ViewTransition>
</Suspense>


Note: This alternative forces all content into the same loading state, which may not be desirable if Header and children should load independently.

Why This Fixes It

By wrapping all children in Suspense boundaries:

Content reveals are coordinated through React's Suspense mechanism
ViewTransition doesn't activate prematurely during hydration
Server and client rendering remain consistent
No hydration mismatch occurs
Key Rules
Context Shorthand: Always use <Context value={...}> instead of <Context.Provider value={...}>
use() Hook: Always use use(Context) instead of useContext(Context)
No useMemo: React Compiler automatically memoizes expensive computations
No useCallback: React Compiler automatically stabilizes function references
No memo(): React Compiler automatically optimizes component re-renders
Trust the Compiler: Let React Compiler handle optimization instead of manual patterns
ViewTransition + Suspense: When using ViewTransition with Suspense, ensure all children are within Suspense boundaries to prevent hydration errors
When Manual Optimization Might Be Needed

In rare cases, you might still need manual optimization:

External library integration that expects stable references
Performance profiling shows a specific issue that React Compiler doesn't catch

Always profile first before adding manual optimizations. The React Compiler is very effective.

Weekly Installs
41
Repository
qingqishi/shiqingqi.com
GitHub Stars
4
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass