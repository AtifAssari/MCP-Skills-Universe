---
rating: ⭐⭐
title: 1k-sentry-analysis
url: https://skills.sh/onekeyhq/app-monorepo/1k-sentry-analysis
---

# 1k-sentry-analysis

skills/onekeyhq/app-monorepo/1k-sentry-analysis
1k-sentry-analysis
Installation
$ npx skills add https://github.com/onekeyhq/app-monorepo --skill 1k-sentry-analysis
SKILL.md
Sentry Error Analysis & Fixes

Complete workflow for analyzing and fixing production errors from Sentry crash reports.

Workflow Overview
1. Obtain Sentry JSON log
   ↓
2. Analyze error
   ↓
3. Identify root cause
   ↓
4. Generate bug analysis log
   ↓
🚨 WAIT FOR USER CONFIRMATION 🚨
   ↓
5. Implement fix (only after approval)
   ↓
6. Test & verify
   ↓
7. Create PR

Critical Requirements

MUST follow these rules:

✅ Always create a bug analysis log in node_modules/.cache/bugs/ before implementing fixes
🚨 MUST wait for user confirmation before starting any code changes
✅ Bug analysis must be complete with all sections filled
✅ Use evidence-based methodology (环环相扣，逐步递进)
Quick Reference
Common Error Types
Type	Description	Common Causes
AppHang	iOS app frozen >5s	Too many concurrent requests, main thread blocking
ANR	Android Not Responding	Heavy operations on main thread, deadlocks
Crash	App terminated	Null pointer, memory issues, unhandled exceptions
Exception	Handled error	Network failures, validation errors, state issues
Analysis Methodology

Use 6 types of proof to establish causation:

Stack Trace Evidence - Error location in code
Breadcrumbs Evidence - User actions leading to error
Code Logic Evidence - Why the code causes the issue
Timing Evidence - When and how often it occurs
Device/Platform Evidence - Affected platforms/devices
Fix Verification - Testing confirms fix works
Common Fix Patterns
// Pattern 1: Concurrent request control
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

// Pattern 2: Main thread offloading (React Native)
import { InteractionManager } from 'react-native';

InteractionManager.runAfterInteractions(() => {
  // Heavy operation here
});

// Pattern 3: Error boundary
<ErrorBoundary fallback={<ErrorFallback />}>
  <Component />
</ErrorBoundary>

Detailed Guide

For comprehensive Sentry error analysis workflow, see fix-sentry-errors.md.

Topics covered:

Obtaining Sentry JSON logs
Python-based quick analysis
Bug analysis log template
6 types of proof methodology
Root cause identification
Common fix patterns (AppHang, ANR, Crashes)
Real-world case studies
Testing and verification
PR creation workflow
Key Files
Purpose	Location
Bug analysis logs	node_modules/.cache/bugs/
Sentry config	packages/shared/src/modules/sentry/
Error boundaries	packages/kit/src/components/ErrorBoundary/
When to Use This Skill
Analyzing iOS AppHang errors (5+ second freezes)
Fixing Android ANR (Application Not Responding)
Investigating crash reports with stack traces
Understanding user actions before crashes (breadcrumbs)
Creating evidence-based bug analysis reports
Implementing fixes for production errors
Related Skills
/1k-performance - Performance optimization patterns
/1k-error-handling - Error handling best practices
/1k-sentry - Sentry configuration and filtering
/1k-code-quality - Lint fixes and code quality
Weekly Installs
53
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