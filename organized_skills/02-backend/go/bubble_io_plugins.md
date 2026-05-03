---
rating: ⭐⭐⭐
title: bubble-io-plugins
url: https://skills.sh/afaraha8403/bubble-io-plugin-boilerplate/bubble-io-plugins
---

# bubble-io-plugins

skills/afaraha8403/bubble-io-plugin-boilerplate/bubble-io-plugins
bubble-io-plugins
Installation
$ npx skills add https://github.com/afaraha8403/bubble-io-plugin-boilerplate --skill bubble-io-plugins
SKILL.md
Bubble.io Plugin Development — Project Rules
Project identity

This is a Bubble.io plugin development boilerplate. It provides the folder structure, coding conventions, and tooling for building plugins that run inside the Bubble.io no-code platform.

Plugins are deployed by copying code into the Bubble Plugin Editor — no build step, no npm publish.

Project structure
project-root/
  actions/
    client/                # Client-side workflow actions
      <action-name>/
        action-setup.md
        client.js
        params.json        # Optional: parameter definitions
    server/                # Server-side actions (runs on Bubble's Node.js server)
      <action-name>/
        action-setup.md
        server.js
  elements/                # Visual plugin elements
    <element-name>/
      element-setup.md
      initialize.js        # Runs once on element load
      update.js            # Runs on every property change + data load
      preview.js           # Renders placeholder in Bubble Editor
      header.html          # <head> content: CDN links, external scripts
      actions/             # Element-specific workflow actions
        <action>.js
  eslint.config.mjs        # ESLint flat config
  package.json             # ESLint scripts and dependencies
  README.md

Key architectural fact

Each local file maps 1:1 to a text field in the Bubble Plugin Editor:

Local file	Bubble Editor field
initialize.js	Function: initialize
update.js	Function: update
preview.js	Function: preview
header.html	Element Header
actions/<name>.js	Element Action code
server/<name>/server.js	Server-Side Action code
styles.css	Shared/Element Header (wrap in <style> tags)
Code quality expectations

When generating or editing any code in this project, follow these rules unconditionally.

Well-formatted, readable code

All code must be clean, consistently formatted, and easy to scan. This means:

Logical sections separated by blank lines — group related statements together (data loading, guards, rendering, event binding).
Descriptive variable names — avoid single-letter or cryptic abbreviations (container not c, itemCount not ic).
Consistent indentation — 2-space indent for all JS; match surrounding code if editing an existing file.
Section banners for update.js — use comment blocks (// === SECTION ===) to delimit lifecycle phases (data loading → guard → change detection → cleanup → render).
One concern per function — extract helpers for any logic longer than ~10 lines; define helpers inside the wrapper function to avoid global leaks.
Inline documentation

Every non-trivial block of code must include an inline comment explaining why it exists, not just what it does. Specifically:

Data loading — explain what each properties.* field contains and why it is loaded first.
Guards / early returns — explain the condition being checked and what would happen without the guard.
DOM mutations — explain the structure being built and any Bubble-specific constraints (e.g., why we use instance.canvas instead of document.body).
Event listeners — explain the namespace convention and why previous listeners are removed.
Workarounds — any Bubble quirk or browser compat hack must have a comment linking to the reason.
JSDoc comments

All functions (wrappers and helpers) must have JSDoc blocks. Follow the rules in documentation.md Section 1. Summary:

Wrapper functions (initialize, update, preview, actions) — include a top-level @description summarising the function's purpose, followed by @param tags for each argument (instance, properties, context).
Helper functions — @param, @returns, and a one-line description.
Placement — JSDoc goes inside the wrapper, not above it (the wrapper line is stripped when pasting into Bubble).

Example (initialize wrapper):

let initialize = function(instance, context) {
  /**
   * @description One-time setup for the PLUGIN_PREFIX element.
   * Creates the root DOM container, generates a unique event namespace,
   * and initialises default exposed states.
   *
   * @param {object} instance - Bubble element instance (canvas, data, publishState, etc.)
   * @param {object} context  - Bubble context (keys, currentUser, etc.)
   */

  // ... implementation ...
};

Debug logging (verbose_logging)

When scaffolding a new element or action from scratch, ask the user once:

"Should this component include a verbose_logging toggle? This adds a boolean field in the Bubble Plugin Editor that gates all console.log output at runtime."

Do not ask on edits, reviews, refactors, or bug fixes — only on new scaffolds.

If the user accepts:

Add a boolean field called verbose_logging to the element or action configuration in the Bubble Plugin Editor and document it in the relevant setup file.
Gate all console.log calls behind properties.verbose_logging:
if (properties.verbose_logging) {
  console.log('[PLUGIN_PREFIX] update called', { properties });
}

Log placement — add gated log statements at:
Entry point of update.js, client actions, and server actions
After data loading completes
Before and after external API calls (server actions)
console.error() in catch blocks is always unconditional — never gate error logging behind the verbose flag.
initialize.js does not receive properties — verbose logging is unavailable. Use a plain console.log only for temporary init-time debugging; remove before production.
preview.js and header.html run in the editor only — verbose logging does not apply.

If the user declines, omit all console.log statements. console.error() in catch blocks remains unconditionally.

Critical pitfalls — always keep in mind

These are the highest-consequence rules. Violating any of these causes hard-to-debug failures:

Never catch the 'not ready' exception — Bubble uses it as control flow for data loading. If you must use try/catch, re-throw when err.message === 'not ready'.
Load all data at the TOP of the function — before any DOM mutations. Bubble re-runs the entire function from the start when data arrives.
Never append to document.body — use instance.canvas for all visual output.
Never put API keys in client-side code — use server-side actions with context.keys.
Copy only the function BODY to the Bubble Plugin Editor — not the wrapper.
Prefix all CSS classes (e.g., myPlugin-root) — avoid collisions with the host app.
SSA in v4 must be async — use await on .get(), .length(), and fetch().
Headers only support <script>, <meta>, <link> — anything else gets auto-moved to <body>.
Do NOT use $(document).ready() inside plugin functions — it breaks Bubble's dependency detection.
Which reference to load

Do not preload all files. Determine the task type, then load only the relevant reference:

Determine the task:
Writing/reviewing element runtime code (initialize.js, update.js, preview.js, header.html)? → Load bubble-platform.md
Need instance/properties/context API details, or v4 migration? → Load bubble-api.md
Working on actions (client-side or server-side)? → Load actions-guide.md
Writing, reviewing, or refactoring any JavaScript? → Load code-standards.md
Writing docs, setup files, or user-facing text? → Load documentation.md
Multiple concerns? → Load the most relevant file first, add others only if needed.
File	Load when...
bubble-platform.md	Element lifecycle, DOM/canvas, data loading, headers, preview, events, debugging, hard limits.
bubble-api.md	instance, properties, context API reference. BubbleThing/BubbleList types. Custom data types / API Connector App Types. Plugin API v4 migration.
actions-guide.md	Client vs server actions. When to use which. SSA Node modules, return values, option sets.
code-standards.md	ESLint config, syntax rules, security, performance, error handling.
documentation.md	JSDoc, setup files, marketplace descriptions, field tooltips, changelog, publishing.
Starter templates

When scaffolding a new element or action, copy the relevant template from assets/templates/:

Template	Use for
initialize.js	New element — container setup, instance.data, event namespace
update.js	New element — data-first pattern, change detection, namespaced listeners
preview.js	New element — editor placeholder with responsive sizing
header.html	New element — idempotent <script> loading
client-action.js	New client-side action
server-action.js	New server-side action (v4 async/await)
General expectations
State reasoning. When recommending a change, explain why — do not just state the rule.
Preserve existing patterns. Before introducing a new pattern, check if the codebase already uses a convention for the same concern.
No unnecessary files. Do not create files unless the task requires it. Prefer editing existing files.
Linting is enforced via ESLint. Configuration lives in eslint.config.mjs (flat config format). VS Code auto-fixes on save via .vscode/settings.json (source.fixAll.eslint). Do not introduce a second formatter.
Weekly Installs
13
Repository
afaraha8403/bub…lerplate
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn