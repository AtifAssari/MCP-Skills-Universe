---
title: responsive-web-design
url: https://skills.sh/aj-geddes/useful-ai-prompts/responsive-web-design
---

# responsive-web-design

skills/aj-geddes/useful-ai-prompts/responsive-web-design
responsive-web-design
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill responsive-web-design
Summary

Mobile-first responsive layouts using CSS Grid, Flexbox, and media queries.

Covers three core layout techniques: Flexbox for flexible component layouts, CSS Grid for structured multi-column designs, and mobile-first media queries for device adaptation
Includes reference guides for navigation, typography, cards, and grid-based layouts with working code examples
Emphasizes mobile-first development strategy, cross-browser compatibility, and accessible design patterns across all device sizes
SKILL.md
Responsive Web Design
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build mobile-first responsive interfaces using modern CSS techniques including Flexbox, Grid, and media queries to create adaptable user experiences.

When to Use
Multi-device applications
Mobile-first development
Accessible layouts
Flexible UI systems
Cross-browser compatibility
Quick Start

Minimal working example:

/* Mobile styles (default) */
.container {
  display: flex;
  flex-direction: column;
  padding: 16px;
  gap: 16px;
}

.card {
  padding: 16px;
  border-radius: 8px;
  background: white;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

/* Tablet (640px and up) */
@media (min-width: 640px) {
  .container {
    flex-direction: row;
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Mobile-First Media Query Strategy	Mobile-First Media Query Strategy
Flexbox Responsive Navigation	Flexbox Responsive Navigation
CSS Grid Responsive Layout	CSS Grid Responsive Layout
Responsive Typography	Responsive Typography
Responsive Cards Component	Responsive Cards Component
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
532
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