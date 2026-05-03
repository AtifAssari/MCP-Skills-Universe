---
title: css-architecture
url: https://skills.sh/aj-geddes/useful-ai-prompts/css-architecture
---

# css-architecture

skills/aj-geddes/useful-ai-prompts/css-architecture
css-architecture
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill css-architecture
Summary

CSS architecture patterns for scalable, maintainable styling systems across teams and projects.

Covers three core methodologies: BEM (Block Element Modifier) for component naming, SMACSS for modular organization, and CSS-in-JS with Styled Components for dynamic styling
Includes reference guides for CSS Variables, Utility-First CSS (Tailwind pattern), and practical implementation examples
Best suited for large-scale stylesheets, component-based design systems, and multi-team collaboration scenarios
SKILL.md
CSS Architecture
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build maintainable CSS systems using methodologies like BEM (Block Element Modifier), SMACSS, and CSS-in-JS patterns with proper organization and conventions.

When to Use
Large-scale stylesheets
Component-based styling
Design system development
Multiple team collaboration
CSS scalability and reusability
Quick Start

Minimal working example:

/* Block - standalone component */
.button {
  display: inline-block;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
}

/* Element - component part */
.button__icon {
  margin-right: 8px;
  vertical-align: middle;
}

/* Modifier - variant */
.button--primary {
  background-color: #007bff;
  color: white;
}

.button--primary:hover {
  background-color: #0056b3;
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
BEM (Block Element Modifier) Pattern	BEM (Block Element Modifier) Pattern
SMACSS (Scalable and Modular Architecture for CSS)	SMACSS (Scalable and Modular Architecture for CSS)
CSS-in-JS with Styled Components	CSS-in-JS with Styled Components
CSS Variables (Custom Properties)	CSS Variables (Custom Properties)
Utility-First CSS (Tailwind Pattern)	Utility-First CSS (Tailwind Pattern)
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
590
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