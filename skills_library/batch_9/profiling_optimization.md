---
title: profiling-optimization
url: https://skills.sh/aj-geddes/useful-ai-prompts/profiling-optimization
---

# profiling-optimization

skills/aj-geddes/useful-ai-prompts/profiling-optimization
profiling-optimization
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill profiling-optimization
SKILL.md
Profiling & Optimization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Profile code execution to identify performance bottlenecks and optimize critical paths using data-driven approaches.

When to Use
Performance optimization
Identifying CPU bottlenecks
Optimizing hot paths
Investigating slow requests
Reducing latency
Improving throughput
Quick Start

Minimal working example:

import { performance, PerformanceObserver } from "perf_hooks";

class Profiler {
  private marks = new Map<string, number>();

  mark(name: string): void {
    this.marks.set(name, performance.now());
  }

  measure(name: string, startMark: string): number {
    const start = this.marks.get(startMark);
    if (!start) throw new Error(`Mark ${startMark} not found`);

    const duration = performance.now() - start;
    console.log(`${name}: ${duration.toFixed(2)}ms`);

    return duration;
  }

  async profile<T>(name: string, fn: () => Promise<T>): Promise<T> {
    const start = performance.now();

    try {
      return await fn();
    } finally {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js Profiling	Node.js Profiling
Chrome DevTools CPU Profile	Chrome DevTools CPU Profile
Python cProfile	Python cProfile
Benchmarking	Benchmarking
Database Query Profiling	Database Query Profiling
Flame Graph Generation	Flame Graph Generation
Best Practices
✅ DO
Profile before optimizing
Focus on hot paths
Measure impact of changes
Use production-like data
Consider memory vs speed tradeoffs
Document optimization rationale
❌ DON'T
Optimize without profiling
Ignore readability for minor gains
Skip benchmarking
Optimize cold paths
Make changes without measurement
Weekly Installs
276
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass