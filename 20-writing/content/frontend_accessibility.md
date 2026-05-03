---
rating: ⭐⭐
title: frontend-accessibility
url: https://skills.sh/aj-geddes/useful-ai-prompts/frontend-accessibility
---

# frontend-accessibility

skills/aj-geddes/useful-ai-prompts/frontend-accessibility
frontend-accessibility
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill frontend-accessibility
SKILL.md
Frontend Accessibility
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build accessible web applications following WCAG guidelines with semantic HTML, ARIA attributes, keyboard navigation, and screen reader support for inclusive user experiences.

When to Use
Compliance with accessibility standards
Inclusive design requirements
Screen reader support
Keyboard navigation
Color contrast issues
Quick Start

Minimal working example:

<!-- Good semantic structure -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

<main>
  <article>
    <header>
      <h1>Article Title</h1>
      <time datetime="2024-01-15">January 15, 2024</time>
    </header>
    <p>Article content...</p>
  </article>

  <aside aria-label="Related articles">
    <h2>Related Articles</h2>
    <ul>
      <li><a href="/article1">Article 1</a></li>
      <li><a href="/article2">Article 2</a></li>
    </ul>
  </aside>
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Semantic HTML and ARIA	Semantic HTML and ARIA
Keyboard Navigation	Keyboard Navigation
Color Contrast and Visual Accessibility	Color Contrast and Visual Accessibility
Screen Reader Announcements	Screen Reader Announcements
Accessibility Testing	Accessibility Testing
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
320
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