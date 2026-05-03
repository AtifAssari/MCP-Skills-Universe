---
title: bundle-size-optimization
url: https://skills.sh/aj-geddes/useful-ai-prompts/bundle-size-optimization
---

# bundle-size-optimization

skills/aj-geddes/useful-ai-prompts/bundle-size-optimization
bundle-size-optimization
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill bundle-size-optimization
SKILL.md
Bundle Size Optimization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Smaller bundles download faster, parse faster, and execute faster, dramatically improving perceived performance especially on slower networks.

When to Use
Build process optimization
Bundle analysis before deployment
Performance baseline improvement
Mobile performance focus
After adding new dependencies
Quick Start

Minimal working example:

// Analyze bundle composition

class BundleAnalysis {
  analyzeBundle() {
    return {
      tools: [
        "webpack-bundle-analyzer",
        "Source Map Explorer",
        "Bundle Buddy",
        "Bundlephobia",
      ],
      metrics: {
        total_size: "850KB gzipped",
        main_js: "450KB",
        main_css: "120KB",
        vendor: "250KB",
        largest_lib: "moment.js (67KB)",
      },
      breakdown: {
        react: "85KB (10%)",
        lodash: "45KB (5%)",
        moment: "67KB (8%)",
        other: "653KB (77%)",
      },
    };
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Bundle Analysis	Bundle Analysis
Optimization Techniques	Optimization Techniques
Implementation Strategy	Implementation Strategy
Best Practices	Best Practices
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
348
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