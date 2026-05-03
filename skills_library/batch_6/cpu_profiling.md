---
title: cpu-profiling
url: https://skills.sh/aj-geddes/useful-ai-prompts/cpu-profiling
---

# cpu-profiling

skills/aj-geddes/useful-ai-prompts/cpu-profiling
cpu-profiling
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill cpu-profiling
SKILL.md
CPU Profiling
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

CPU profiling identifies which functions consume most CPU time, enabling targeted optimization of expensive code paths.

When to Use
High CPU usage
Slow execution
Performance regression
Before optimization
Production monitoring
Quick Start

Minimal working example:

Browser Profiling:

Chrome DevTools:
  Steps:
    1. DevTools → Performance
    2. Click record
    3. Perform action
    4. Stop recording
    5. Analyze flame chart
  Metrics:
    - Function call duration
    - Call frequency
    - Total time vs self time

Firefox Profiler:
  - Built-in performance profiler
  - Flame graphs
  - Timeline view
  - Export and share

React Profiler:
  - DevTools → Profiler
  - Component render times
  - Phase: render vs commit
  - Why component re-rendered
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Profiling Tools	Profiling Tools
Analysis & Interpretation	Analysis & Interpretation
Optimization Process	Optimization Process
Monitoring & Best Practices	Monitoring & Best Practices
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
269
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