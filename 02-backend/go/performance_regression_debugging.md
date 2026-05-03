---
rating: ⭐⭐
title: performance-regression-debugging
url: https://skills.sh/aj-geddes/useful-ai-prompts/performance-regression-debugging
---

# performance-regression-debugging

skills/aj-geddes/useful-ai-prompts/performance-regression-debugging
performance-regression-debugging
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill performance-regression-debugging
SKILL.md
Performance Regression Debugging
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Performance regressions occur when code changes degrade application performance. Detection and quick resolution are critical.

When to Use
After deployment performance degrades
Metrics show negative trend
User complaints about slowness
A/B testing shows variance
Regular performance monitoring
Quick Start

Minimal working example:

// Before: 500ms response time
// After: 1000ms response time (2x slower = regression)

// Capture baseline metrics
const baseline = {
  responseTime: 500, // ms
  timeToInteractive: 2000, // ms
  largestContentfulPaint: 1500, // ms
  memoryUsage: 50, // MB
  bundleSize: 150, // KB gzipped
};

// Monitor after change
const current = {
  responseTime: 1000,
  timeToInteractive: 4000,
  largestContentfulPaint: 3000,
  memoryUsage: 150,
  bundleSize: 200,
};

// Calculate regression
const regressions = {};
for (let metric in baseline) {
  const change = (current[metric] - baseline[metric]) / baseline[metric];
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Detection & Measurement	Detection & Measurement
Root Cause Identification	Root Cause Identification
Fixing & Verification	Fixing & Verification
Prevention Measures	Prevention Measures
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