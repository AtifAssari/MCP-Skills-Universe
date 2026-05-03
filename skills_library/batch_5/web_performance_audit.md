---
title: web-performance-audit
url: https://skills.sh/aj-geddes/useful-ai-prompts/web-performance-audit
---

# web-performance-audit

skills/aj-geddes/useful-ai-prompts/web-performance-audit
web-performance-audit
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill web-performance-audit
SKILL.md
Web Performance Audit
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Web performance audits measure load times, identify bottlenecks, and guide optimization efforts to create faster, better user experiences.

When to Use
Regular performance monitoring
After major changes
User complaints about slowness
SEO optimization
Mobile optimization
Performance baseline setting
Quick Start

Minimal working example:

Core Web Vitals (Google):

Largest Contentful Paint (LCP):
  Measure: Time to load largest visible element
  Good: <2.5 seconds
  Poor: >4 seconds
  Impacts: User perception of speed

First Input Delay (FID):
  Measure: Time from user input to response
  Good: <100 milliseconds
  Poor: >300 milliseconds
  Impacts: Responsiveness

Cumulative Layout Shift (CLS):
  Measure: Visual stability (unexpected layout shifts)
  Good: <0.1
  Poor: >0.25
  Impacts: User frustration

---

Additional Metrics:

First Contentful Paint (FCP):
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Performance Metrics	Performance Metrics
Performance Analysis Process	Performance Analysis Process
Optimization Strategies	Optimization Strategies
Monitoring & Continuous Improvement	Monitoring & Continuous Improvement
Best Practices
✅ DO
Measure regularly (not just once)
Use field data (real users) + lab data
Focus on Core Web Vitals
Set realistic targets
Prioritize by impact
Monitor continuously
Setup performance budgets
Test on slow networks
Include mobile in testing
Document improvements
❌ DON'T
Ignore field data
Focus on one metric only
Set impossible targets
Optimize without measurement
Forget about images
Ignore JavaScript costs
Skip mobile performance
Over-optimize prematurely
Forget about monitoring
Expect improvements without effort
Weekly Installs
334
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn