---
title: 1k-performance
url: https://skills.sh/onekeyhq/app-monorepo/1k-performance
---

# 1k-performance

skills/onekeyhq/app-monorepo/1k-performance
1k-performance
Installation
$ npx skills add https://github.com/onekeyhq/app-monorepo --skill 1k-performance
SKILL.md
OneKey Performance Optimization

Performance optimization patterns and best practices for React/React Native applications in the OneKey monorepo.

Quick Reference
Category	Key Optimization	When to Use
Concurrent Requests	Limit to 3-5, use executeBatched	Multiple API calls, network-heavy operations
Bridge Optimization	Minimize crossings, batch data	React Native bridge overhead, iOS/Android
List Rendering	FlashList, windowSize={5}, content-visibility	Lists with 100+ items
Memoization	memo, useMemo, useCallback	Expensive computations, prevent re-renders
Heavy Operations	InteractionManager, setTimeout	UI blocking operations
Critical Performance Rules
❌ FORBIDDEN: Too Many Concurrent Requests
// ❌ BAD - Can freeze UI with 15+ requests
const requests = items.map(item => fetchData(item));
await Promise.all(requests);

✅ CORRECT: Batched Execution with Concurrency Limit
async function executeBatched<T>(
  tasks: Array<() => Promise<T>>,
  concurrency = 3,
): Promise<Array<PromiseSettledResult<T>>> {
  const results: Array<PromiseSettledResult<T>> = [];
  for (let i = 0; i < tasks.length; i += concurrency) {
    const batch = tasks.slice(i, i + concurrency);
    const batchResults = await Promise.allSettled(
      batch.map((task) => task()),
    );
    results.push(...batchResults);
  }
  return results;
}

const tasks = items.map(item => () => fetchData(item));
await executeBatched(tasks, 3); // Max 3 concurrent

🚨 Built-in Optimizations

Already Optimized - NO ACTION NEEDED:

Component	Optimization	Details
ListView	windowSize={5}	Auto-limits visible items
Tabs	contentVisibility: 'hidden'	Hides inactive tabs
Dialog	contentVisibility: 'hidden'	Hides when closed
Detailed Guide

For comprehensive performance optimization strategies, see performance.md.

Topics covered:

Concurrent request control
React Native bridge optimization
Heavy operations offloading
List rendering (windowSize, FlashList, content-visibility)
Memoization & callbacks
State updates optimization
Image optimization
Async operations & race conditions
Real-world iOS AppHang case study
Related Skills
/1k-coding-patterns - General coding patterns and conventions
/1k-sentry-analysis - Sentry error analysis (includes performance issues)
/react-native-best-practices - React Native specific optimizations
Weekly Installs
56
Repository
onekeyhq/app-monorepo
GitHub Stars
2.4K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass