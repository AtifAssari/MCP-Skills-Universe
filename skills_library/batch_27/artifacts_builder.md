---
title: artifacts-builder
url: https://skills.sh/pixel-process-ug/superkit-agents/artifacts-builder
---

# artifacts-builder

skills/pixel-process-ug/superkit-agents/artifacts-builder
artifacts-builder
Installation
$ npx skills add https://github.com/pixel-process-ug/superkit-agents --skill artifacts-builder
SKILL.md
Artifacts Builder
Overview

Generate self-contained, production-quality HTML/CSS/JS artifacts that run in any modern browser without a build step. Each artifact is a single file (or minimal file set) containing everything needed for an interactive demo, prototype, data visualization, or utility tool. Emphasis on progressive enhancement, responsive design, and clean code.

Phase 1: Scope Definition
Clarify the artifact's purpose (demo, prototype, tool, visualization)
Determine interactivity level (static, interactive, data-driven)
Identify required dependencies (none, CDN-loaded, embedded)
Define responsive requirements (mobile, desktop, both)
Set constraints (file size, browser support, offline capability)

STOP — Confirm scope and constraints with user before architecture decisions.

Artifact Type Decision Table
Purpose	Complexity	Dependencies	Example
Static demo	Low	None	Product mockup, landing page
Interactive widget	Medium	None or Alpine.js	Calculator, form builder
Data visualization	Medium-High	D3.js or Chart.js	Dashboard, chart explorer
Prototype	Medium	Alpine.js or Petite-Vue	Clickable UI prototype
Utility tool	Medium-High	Varies	JSON formatter, color picker
Generative art	Medium	None	Canvas animation, pattern generator
Presentation	Medium	None or Mermaid	Slide deck, diagram viewer
Phase 2: Architecture
Choose single-file or multi-file approach
Select CDN dependencies (if any)
Plan component structure within the file
Define state management approach
Plan progressive enhancement layers

STOP — Present architecture and dependency choices for approval.

Architecture Decision Table
Constraint	Single-File	Multi-File
Easy sharing (email, paste)	Yes	No
File size < 100KB	Yes	Either
Multiple pages/views	Possible (SPA)	Better
Team collaboration	Difficult	Better
Offline use	Yes (self-contained)	Needs bundling
SEO requirements	N/A	N/A (artifacts are tools)
Dependency Decision Table
Need	Recommended	CDN URL	Size
Lightweight reactivity	Alpine.js	cdn.jsdelivr.net/npm/alpinejs@3	~15KB
Minimal Vue-like	Petite-Vue	unpkg.com/petite-vue	~6KB
Charts	Chart.js	cdn.jsdelivr.net/npm/chart.js@4	~65KB
Data visualization	D3.js	cdn.jsdelivr.net/npm/d3@7	~90KB
Diagrams	Mermaid	cdn.jsdelivr.net/npm/mermaid@10	~120KB
CSS framework (proto)	Tailwind Play CDN	cdn.tailwindcss.com	Runtime
Icons	Lucide	unpkg.com/lucide@latest	On-demand
No dependency needed	Vanilla JS	N/A	0KB
CDN Usage Rules
Rule	Rationale
Pin to major version (@3, @7)	Prevent breaking changes
Maximum 3 CDN dependencies	Keep artifacts lightweight
Add integrity and crossorigin	Security against CDN compromise
Provide graceful degradation	Work if CDN fails
Prefer smaller alternatives	Alpine over React, Petite-Vue over Vue
Phase 3: Implementation
Build semantic HTML structure
Add CSS (inline <style> or embedded)
Implement JavaScript functionality
Add error handling and fallbacks
Test across viewports and browsers

STOP — Verify the artifact works correctly before delivering to user.

Template Structure
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Artifact Title]</title>
  <style>
    /* Reset */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    /* Design Tokens */
    :root {
      --color-bg: #ffffff;
      --color-text: #1a1a2e;
      --color-primary: #3b82f6;
      --color-border: #e2e8f0;
      --radius: 0.5rem;
      --space: 1rem;
      --font: system-ui, -apple-system, sans-serif;
    }

    @media (prefers-color-scheme: dark) {
      :root {
        --color-bg: #0f172a;
        --color-text: #e2e8f0;
        --color-primary: #60a5fa;
        --color-border: #334155;
      }
    }

    /* Base Styles */
    body {
      font-family: var(--font);
      background: var(--color-bg);
      color: var(--color-text);
      line-height: 1.6;
    }

    /* Component Styles */
    /* ... */
  </style>
</head>
<body>
  <!-- Semantic HTML content -->

  <script>
    // Application logic
    (function() {
      'use strict';
      // ...
    })();
  </script>
</body>
</html>

Responsive Design Patterns
Container-Based Layout
.container {
  width: min(100% - 2rem, 1200px);
  margin-inline: auto;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
  gap: var(--space);
}

Mobile-First Media Queries
/* Base: mobile */
.layout { display: flex; flex-direction: column; }

/* Tablet and up */
@media (min-width: 768px) {
  .layout { flex-direction: row; }
  .sidebar { width: 280px; flex-shrink: 0; }
}

Progressive Enhancement
Layer	Purpose	Requirement
HTML	Content accessible and meaningful	Works without CSS or JS
CSS	Visual presentation and layout	Works without JS
JavaScript	Enhanced interactivity	Adds dynamic behavior
Feature Detection
// Check before using modern APIs
if ('IntersectionObserver' in window) {
  // Use lazy loading
} else {
  // Load all images immediately
}

if (CSS.supports('backdrop-filter', 'blur(10px)')) {
  element.classList.add('glass-effect');
}

State Management (No Framework)
Simple State Pattern
function createStore(initialState) {
  let state = { ...initialState };
  const listeners = new Set();

  return {
    getState: () => ({ ...state }),
    setState(updates) {
      state = { ...state, ...updates };
      listeners.forEach(fn => fn(state));
    },
    subscribe(fn) {
      listeners.add(fn);
      return () => listeners.delete(fn);
    },
  };
}

URL-Based State (for shareable artifacts)
function syncStateWithURL(store) {
  const params = new URLSearchParams(location.search);
  for (const [key, value] of params) {
    store.setState({ [key]: JSON.parse(value) });
  }
  store.subscribe(state => {
    const params = new URLSearchParams();
    Object.entries(state).forEach(([k, v]) => params.set(k, JSON.stringify(v)));
    history.replaceState(null, '', `?${params}`);
  });
}

Export Formats
Format	Use Case	Method
Single HTML file	Sharing, embedding	Self-contained <style> and <script>
HTML + assets	Complex artifacts	Separate CSS/JS files
Data URL	Inline embedding	data:text/html;base64,...
Screenshot/PNG	Documentation	html2canvas or browser screenshot
PDF	Print/report	window.print() with print styles
Quality Checklist
 Valid HTML5 (<!DOCTYPE html>, lang attribute)
 Responsive viewport meta tag
 Works without JavaScript (content visible)
 Dark mode support (prefers-color-scheme)
 Keyboard navigable
 No console errors
 File size under 100KB (excluding images)
 Cross-browser tested (Chrome, Firefox, Safari)
 Print styles if applicable
 Semantic HTML elements used appropriately
Anti-Patterns / Common Mistakes
Anti-Pattern	Why It Is Wrong	What to Do Instead
React/Vue/Angular in single-file artifact	Massive overhead for simple interactions	Use Alpine.js or vanilla JS
Heavy framework from CDN for simple UI	Slow load, wasted bandwidth	Match dependency weight to need
Inline styles instead of CSS custom properties	Cannot theme, cannot dark-mode	Use CSS custom properties (tokens)
No error handling on user input	Crashes on bad input	Validate and provide feedback
Fixed pixel dimensions	Breaks on mobile, tablets	Use responsive units (%, rem, vw)
Missing <meta viewport>	Mobile renders desktop-zoomed	Always include viewport meta tag
Blocking <script> in <head>	Delays page rendering	Use defer attribute or put at end of body
No IIFE wrapper for script	Global scope pollution	Wrap in (function() { ... })()
Hardcoded colors without tokens	Cannot switch themes	Use CSS custom properties
Integration Points
Skill	Integration
ui-ux-pro-max	Style selection and UX guidelines
ui-design-system	Design tokens for consistent theming
canvas-design	Canvas/SVG visualizations within artifacts
senior-frontend	Complex component patterns
mobile-design	Mobile-responsive artifact design
planning	Artifact scope is defined during planning
Skill Type

FLEXIBLE — Adapt the architecture, dependencies, and complexity to the artifact's requirements. Simple demos should remain as minimal as possible; complex tools may use lightweight frameworks and multiple CDN dependencies.

Weekly Installs
31
Repository
pixel-process-u…t-agents
GitHub Stars
1
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass