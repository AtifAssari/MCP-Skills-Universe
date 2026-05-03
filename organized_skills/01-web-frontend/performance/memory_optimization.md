---
rating: ⭐⭐
title: memory-optimization
url: https://skills.sh/aj-geddes/useful-ai-prompts/memory-optimization
---

# memory-optimization

skills/aj-geddes/useful-ai-prompts/memory-optimization
memory-optimization
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill memory-optimization
SKILL.md
Memory Optimization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Memory optimization improves application performance, stability, and reduces infrastructure costs. Efficient memory usage is critical for scalability.

When to Use
High memory usage
Memory leaks suspected
Slow performance
Out of memory crashes
Scaling challenges
Quick Start

Minimal working example:

// Browser memory profiling

// Check memory usage
performance.memory: {
  jsHeapSizeLimit: 2190000000,    // Max available
  totalJSHeapSize: 1300000000,    // Total allocated
  usedJSHeapSize: 950000000       // Currently used
}

// React DevTools Profiler
- Open React DevTools → Profiler
- Record interaction
- See component renders and time
- Identify unnecessary renders

// Chrome DevTools
1. Open DevTools → Memory
2. Take heap snapshot
3. Compare before/after
4. Look for retained objects
5. Check retained sizes

// Node.js profiling
node --inspect app.js
// Open chrome://inspect
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Memory Profiling	Memory Profiling
Memory Leak Detection	Memory Leak Detection
Optimization Techniques	Optimization Techniques
Monitoring & Targets	Monitoring & Targets
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
347
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass