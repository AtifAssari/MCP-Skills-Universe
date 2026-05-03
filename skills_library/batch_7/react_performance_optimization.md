---
title: react-performance-optimization
url: https://skills.sh/nickcrew/claude-ctx-plugin/react-performance-optimization
---

# react-performance-optimization

skills/nickcrew/claude-ctx-plugin/react-performance-optimization
react-performance-optimization
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill react-performance-optimization
Summary

Memoization, code splitting, and virtualization patterns for optimizing React application performance.

Covers four core optimization techniques: memoization (React.memo, useMemo, useCallback), code splitting with lazy/Suspense, virtualization for large lists, and state management strategies to minimize render cascades
Includes React 18+ concurrent features (useTransition, useDeferredValue) for improved responsiveness and perceived performance
Provides profiling workflow using React DevTools Profiler to identify bottlenecks before and after optimization, with emphasis on measuring impact rather than premature optimization
Documents common anti-patterns (over-memoization, inline objects breaking memoization, index-based keys) and includes performance checklist covering profiling, optimization targets, and verification steps
SKILL.md
React Performance Optimization

Expert guidance for optimizing React application performance through memoization, code splitting, virtualization, and efficient rendering strategies.

When to Use This Skill
Optimizing slow-rendering React components
Reducing bundle size for faster initial load times
Improving responsiveness for large lists or data tables
Preventing unnecessary re-renders in complex component trees
Optimizing state management to reduce render cascades
Improving perceived performance with code splitting
Debugging performance issues with React DevTools Profiler
Core Concepts
React Rendering Optimization

React re-renders components when props or state change. Unnecessary re-renders waste CPU cycles and degrade user experience. Key optimization techniques:

Memoization: Cache component renders and computed values
Code splitting: Load code on demand for faster initial loads
Virtualization: Render only visible list items
State optimization: Structure state to minimize render cascades
When to Optimize
Profile first: Use React DevTools Profiler to identify actual bottlenecks
Measure impact: Verify optimization improves performance
Avoid premature optimization: Don't optimize fast components
Quick Reference

Load detailed patterns and examples as needed:

Topic	Reference File
React.memo, useMemo, useCallback patterns	skills/react-performance-optimization/references/memoization.md
Code splitting with lazy/Suspense, bundle optimization	skills/react-performance-optimization/references/code-splitting.md
Virtualization for large lists (react-window)	skills/react-performance-optimization/references/virtualization.md
State management strategies, context splitting	skills/react-performance-optimization/references/state-management.md
useTransition, useDeferredValue (React 18+)	skills/react-performance-optimization/references/concurrent-features.md
React DevTools Profiler, performance monitoring	skills/react-performance-optimization/references/profiling-debugging.md
Common pitfalls and anti-patterns	skills/react-performance-optimization/references/common-pitfalls.md
Optimization Workflow
1. Identify Bottlenecks
# Open React DevTools Profiler
# Record interaction → Analyze flame graph → Find slow components


Look for:

Components with yellow/red bars (slow renders)
Unnecessary renders (same props/state)
Expensive computations on every render
2. Apply Targeted Optimizations

For unnecessary re-renders:

Wrap component with React.memo
Use useCallback for stable function references
Check for inline objects/arrays in props

For expensive computations:

Use useMemo to cache results
Move calculations outside render when possible

For large lists:

Implement virtualization with react-window
Ensure proper unique keys (not index)

For slow initial load:

Add code splitting with React.lazy
Analyze bundle size with webpack-bundle-analyzer
Use dynamic imports for heavy dependencies
3. Verify Improvements
# Record new Profiler session
# Compare before/after metrics
# Ensure optimization actually helped

Common Patterns
Memoize Expensive Components
import { memo } from 'react';

const ExpensiveList = memo(({ items, onItemClick }) => {
  return items.map(item => (
    <Item key={item.id} data={item} onClick={onItemClick} />
  ));
});

Cache Computed Values
import { useMemo } from 'react';

function DataTable({ items, filters }) {
  const filteredItems = useMemo(() => {
    return items.filter(item => filters.includes(item.category));
  }, [items, filters]);

  return <Table data={filteredItems} />;
}

Stable Function References
import { useCallback } from 'react';

function Parent() {
  const handleClick = useCallback((id) => {
    console.log('Clicked:', id);
  }, []);

  return <MemoizedChild onClick={handleClick} />;
}

Code Split Routes
import { lazy, Suspense } from 'react';

const Dashboard = lazy(() => import('./Dashboard'));
const Reports = lazy(() => import('./Reports'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/reports" element={<Reports />} />
      </Routes>
    </Suspense>
  );
}

Virtualize Large Lists
import { FixedSizeList } from 'react-window';

function VirtualList({ items }) {
  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={80}
      width="100%"
    >
      {({ index, style }) => (
        <div style={style}>{items[index].name}</div>
      )}
    </FixedSizeList>
  );
}

Common Mistakes
Over-memoization: Don't memoize simple, fast components (adds overhead)
Inline objects/arrays: New references break memoization (config={{ theme: 'dark' }})
Missing dependencies: Stale closures in useCallback/useMemo
Index as key: Breaks reconciliation when list order changes
Single large context: Causes widespread re-renders on any update
No profiling: Optimizing without measuring wastes time
Performance Checklist

Before optimizing:

 Profile with React DevTools to identify bottlenecks
 Measure baseline performance metrics

Optimization targets:

 Memoize expensive components with stable props
 Cache computed values with useMemo (if actually expensive)
 Use useCallback for functions passed to memoized children
 Implement code splitting for routes and heavy components
 Virtualize lists with >100 items
 Provide stable keys for list items (unique IDs, not index)
 Split state by update frequency
 Use concurrent features (useTransition, useDeferredValue) for responsiveness

After optimizing:

 Profile again to verify improvements
 Check bundle size reduction (if applicable)
 Ensure no regressions in functionality
Resources
React Docs - Performance: https://react.dev/learn/render-and-commit
React DevTools: Browser extension for profiling
react-window: https://github.com/bvaughn/react-window
Bundle analyzers: webpack-bundle-analyzer, rollup-plugin-visualizer
Lighthouse: Chrome DevTools performance audit
Weekly Installs
1.1K
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass