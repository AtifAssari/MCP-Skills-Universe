---
title: tsdown
url: https://skills.sh/onmax/nuxt-skills/tsdown
---

# tsdown

skills/onmax/nuxt-skills/tsdown
tsdown
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill tsdown
Summary

Rolldown + Oxc powered TypeScript bundler with dual ESM/CJS output and .d.ts generation.

Drop-in tsup replacement supporting TypeScript library bundling with automatic declaration file generation
Configurable output formats (ESM, CJS, UMD), target environments, and package exports validation
Includes watch mode, framework integrations (Vue, React), plugin authoring, and programmatic API for advanced workflows
Built-in shims, unbundle mode, and WebAssembly support for specialized bundling scenarios
SKILL.md
tsdown

Rolldown + Oxc powered TypeScript bundler. Drop-in tsup replacement.

When to Use
Building TypeScript libraries
Generating .d.ts declarations
Publishing npm packages
Dual ESM/CJS output
Vue/React component libraries
Quick Start
npm i -D tsdown typescript

// tsdown.config.ts
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: 'src/index.ts',
  format: 'esm',
  dts: true,
  exports: true,
})

tsdown           # Build
tsdown --watch   # Watch mode

Reference Files
Task	File
Config file, CLI, entry points	config.md
Format, target, dts, exports, validation	output.md
Shims, unbundle, watch, frameworks, WASM	features.md
Plugins, hooks, lint, programmatic, migration	advanced.md
Loading Files

Consider loading these reference files based on your task:

 references/config.md - if setting up tsdown.config.ts, CLI, or entry points
 references/output.md - if configuring output format, target, .d.ts, exports, or validation
 references/features.md - if using shims, unbundle, watch mode, framework integrations, or WebAssembly
 references/advanced.md - if writing plugins, using linting/validation, programmatic API, or migrating from tsup

DO NOT load all files at once. Load only what's relevant to your current task.

Cross-Skill References
Library patterns → Use ts-library skill
Vue component libs → Use vue skill
Package management → Use pnpm skill
Weekly Installs
687
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass