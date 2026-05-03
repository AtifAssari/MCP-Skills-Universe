---
title: uni-helper
url: https://skills.sh/uni-helper/skills/uni-helper
---

# uni-helper

skills/uni-helper/skills/uni-helper
uni-helper
Installation
$ npx skills add https://github.com/uni-helper/skills --skill uni-helper
SKILL.md

The skill is based on uni-helper documentation, generated at 2026-01-30.

uni-helper is an ecosystem of AI-powered development tools for uni-app, providing Vite plugins, utility libraries, TypeScript support, and development tools to enhance the uni-app development experience.

Vite Plugins
Topic	Description	Reference
vite-plugin-uni-pages	File-based routing system for uni-app with auto page discovery	plugin-pages
vite-plugin-uni-layouts	Nuxt-like layouts system for uni-app	plugin-layouts
vite-plugin-uni-components	On-demand automatic component imports	plugin-components
vite-plugin-uni-manifest	Write manifest.json in TypeScript	plugin-manifest
vite-plugin-uni-platform	File-based platform compilation (*.h5	mp-weixin
vite-plugin-uni-platform-modifier	Platform modifiers for attributes/directives	plugin-platform-modifier
vite-plugin-uni-middleware	Middleware support for uni-app routing	plugin-middleware
Libraries
Topic	Description	Reference
uni-use	VueUse-style composable utilities for uni-app	lib-uni-use
uni-network	Promise-based HTTP client for uni-app	lib-uni-network
uni-promises	Promise wrappers for uni-app APIs	lib-uni-promises
uni-typed	TypeScript type definitions for uni-app templates	lib-uni-typed
Utilities
Topic	Description	Reference
uni-env	Environment detection utilities for uni-app	util-uni-env
unocss-preset-uni	UnoCSS preset for uni-app	util-unocss-preset
Project Starters
Topic	Description	Reference
create-uni	CLI scaffolding tool for uni-app projects	starter-create-uni
vitesse-uni-app	Vite-powered uni-app starter template	starter-vitesse
Plugin Order Best Practices

When using multiple uni-helper Vite plugins, the recommended order is:

// vite.config.ts
export default defineConfig({
  plugins: [
    UniComponents(),  // 1. Component auto-import
    UniPages(),       // 2. File-based routing
    UniLayouts(),     // 3. Layout system
    UniManifest(),    // 4. Manifest generation
    UniPlatform(),    // 5. Platform-specific files
    UniPlatformModifier(), // 6. Platform modifiers
    UniMiddleware(),  // 7. Route middleware
    Uni(),            // 8. Official uni-app plugin (always last)
  ],
})

Quick Start

Create a new uni-app project with create-uni:

# npm 7+, extra double-dash is needed
npm create uni@latest

# pnpm
pnpm create uni

# yarn
yarn create uni

Official Resources
Website: https://uni-helper.js.org
GitHub: https://github.com/uni-helper
NPM Scope: @uni-helper
Weekly Installs
382
Repository
uni-helper/skills
GitHub Stars
58
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass