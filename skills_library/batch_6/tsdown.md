---
title: tsdown
url: https://skills.sh/antfu/skills/tsdown
---

# tsdown

skills/antfu/skills/tsdown
tsdown
Originally fromsanity-io/next-sanity
Installation
$ npx skills add https://github.com/antfu/skills --skill tsdown
Summary

Fast TypeScript/JavaScript library bundler powered by Rolldown with multi-format output and type declaration generation.

Supports bundling to ESM, CJS, IIFE, and UMD formats with automatic peer dependency externalization and tree shaking
Generates TypeScript declaration files (.d.ts) with source map and compiler option control, plus experimental CSS pipeline with preprocessor and PostCSS support
Includes watch mode, minification, source maps, unbundle mode for preserving directory structure, and framework-specific recipes for React, Vue, Solid, and Svelte
Offers CLI commands, programmatic API, lifecycle hooks, workspace/monorepo support, and direct Rolldown option passthrough for advanced customization
Provides migration tooling from tsup and experimental features for standalone executable bundling and package validation (publint, attw)
SKILL.md
tsdown - The Elegant Library Bundler

Blazing-fast bundler for TypeScript/JavaScript libraries powered by Rolldown and Oxc.

When to Use
Building TypeScript/JavaScript libraries for npm
Generating TypeScript declaration files (.d.ts)
Bundling for multiple formats (ESM, CJS, IIFE, UMD)
Optimizing bundles with tree shaking and minification
Migrating from tsup with minimal changes
Building React, Vue, Solid, or Svelte component libraries
Quick Start
# Install
pnpm add -D tsdown

# Basic usage
npx tsdown

# With config file
npx tsdown --config tsdown.config.ts

# Watch mode
npx tsdown --watch

# Migrate from tsup
npx tsdown-migrate

Basic Configuration
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['./src/index.ts'],
  format: ['esm', 'cjs'],
  dts: true,
  clean: true,
})

Core References
Topic	Description	Reference
Getting Started	Installation, first bundle, CLI basics	guide-getting-started
Configuration File	Config file formats, multiple configs, workspace	option-config-file
CLI Reference	All CLI commands and options	reference-cli
Migrate from tsup	Migration guide and compatibility notes	guide-migrate-from-tsup
Plugins	Rolldown, Rollup, Unplugin support	advanced-plugins
Hooks	Lifecycle hooks for custom logic	advanced-hooks
Programmatic API	Build from Node.js scripts	advanced-programmatic
Rolldown Options	Pass options directly to Rolldown	advanced-rolldown-options
CI Environment	CI detection, 'ci-only' / 'local-only' values	advanced-ci
Build Options
Option	Usage	Reference
Entry points	entry: ['src/*.ts', '!**/*.test.ts']	option-entry
Output formats	format: ['esm', 'cjs', 'iife', 'umd']	option-output-format
Output directory	outDir: 'dist', outExtensions	option-output-directory
Type declarations	dts: true, dts: { sourcemap, compilerOptions, vue }	option-dts
Target environment	target: 'es2020', target: 'esnext'	option-target
Platform	platform: 'node', platform: 'browser'	option-platform
Tree shaking	treeshake: true, custom options	option-tree-shaking
Minification	minify: true, minify: 'dce-only'	option-minification
Source maps	sourcemap: true, 'inline', 'hidden'	option-sourcemap
Watch mode	watch: true, watch options	option-watch-mode
Cleaning	clean: true, clean patterns	option-cleaning
Log level	logLevel: 'silent', failOnWarn: false	option-log-level
Dependency Handling
Feature	Usage	Reference
Never bundle	deps: { neverBundle: ['react', /^@myorg\//] }	option-dependencies
Always bundle	deps: { alwaysBundle: ['dep-to-bundle'] }	option-dependencies
Only bundle	deps: { onlyBundle: ['cac', 'bumpp'] } - Whitelist	option-dependencies
Skip node_modules	deps: { skipNodeModulesBundle: true }	option-dependencies
Auto external	Automatic peer/dependency externalization	option-dependencies
Output Enhancement
Feature	Usage	Reference
Shims	shims: true - Add ESM/CJS compatibility	option-shims
CJS default	cjsDefault: true (default) / false	option-cjs-default
Package exports	exports: true - Auto-generate exports field	option-package-exports
CSS handling	[experimental] css: { ... } — full pipeline with preprocessors, Lightning CSS, PostCSS, code splitting; requires @tsdown/css	option-css
CSS inject	css: { inject: true } — preserve CSS imports in JS output	option-css
Unbundle mode	unbundle: true - Preserve directory structure	option-unbundle
Root directory	root: 'src' - Control output directory mapping	option-root
Executable	[experimental] exe: true - Bundle as standalone executable, cross-platform via @tsdown/exe	option-exe
Package validation	publint: true, attw: true - Validate package	option-lint
Framework & Runtime Support
Framework	Guide	Reference
React	JSX transform, React Compiler	recipe-react
Vue	SFC support, JSX	recipe-vue
Solid	SolidJS JSX transform	recipe-solid
Svelte	Svelte component libraries (source distribution recommended)	recipe-svelte
WASM	WebAssembly modules via rolldown-plugin-wasm	recipe-wasm
Common Patterns
Basic Library Bundle
export default defineConfig({
  entry: ['src/index.ts'],
  format: ['esm', 'cjs'],
  dts: true,
  clean: true,
})

Multiple Entry Points
export default defineConfig({
  entry: {
    index: 'src/index.ts',
    utils: 'src/utils.ts',
    cli: 'src/cli.ts',
  },
  format: ['esm', 'cjs'],
  dts: true,
})

Browser Library (IIFE/UMD)
export default defineConfig({
  entry: ['src/index.ts'],
  format: ['iife'],
  globalName: 'MyLib',
  platform: 'browser',
  minify: true,
})

React Component Library
export default defineConfig({
  entry: ['src/index.tsx'],
  format: ['esm', 'cjs'],
  dts: true,
  deps: {
    neverBundle: ['react', 'react-dom'],
  },
  inputOptions: {
    jsx: { runtime: 'automatic' },
  },
})

Preserve Directory Structure
export default defineConfig({
  entry: ['src/**/*.ts', '!**/*.test.ts'],
  unbundle: true, // Preserve file structure
  format: ['esm'],
  dts: true,
})

CI-Aware Configuration
export default defineConfig({
  entry: ['src/index.ts'],
  format: ['esm', 'cjs'],
  dts: true,
  failOnWarn: 'ci-only',  // opt-in: fail on warnings in CI
  publint: 'ci-only',
  attw: 'ci-only',
})

WASM Support
import { wasm } from 'rolldown-plugin-wasm'
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['src/index.ts'],
  plugins: [wasm()],
})

Library with CSS and Sass
export default defineConfig({
  entry: ['src/index.ts'],
  format: ['esm', 'cjs'],
  dts: true,
  target: 'chrome100',
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "src/styles/variables" as *;`,
      },
    },
  },
})

Standalone Executable
export default defineConfig({
  entry: ['src/cli.ts'],
  exe: true,
})

Cross-Platform Executable (requires @tsdown/exe)
export default defineConfig({
  entry: ['src/cli.ts'],
  exe: {
    targets: [
      { platform: 'linux', arch: 'x64', nodeVersion: '25.7.0' },
      { platform: 'darwin', arch: 'arm64', nodeVersion: '25.7.0' },
      { platform: 'win', arch: 'x64', nodeVersion: '25.7.0' },
    ],
  },
})

Advanced with Hooks
export default defineConfig({
  entry: ['src/index.ts'],
  format: ['esm', 'cjs'],
  dts: true,
  hooks: {
    'build:before': async (context) => {
      console.log('Building...')
    },
    'build:done': async (context) => {
      console.log('Build complete!')
    },
  },
})

Configuration Features
Multiple Configs

Export an array for multiple build configurations:

export default defineConfig([
  {
    entry: ['src/index.ts'],
    format: ['esm', 'cjs'],
    dts: true,
  },
  {
    entry: ['src/cli.ts'],
    format: ['esm'],
    platform: 'node',
  },
])

Conditional Config

Use functions for dynamic configuration:

export default defineConfig((options) => {
  const isDev = options.watch
  return {
    entry: ['src/index.ts'],
    format: ['esm', 'cjs'],
    minify: !isDev,
    sourcemap: isDev,
  }
})

Workspace/Monorepo

Use glob patterns to build multiple packages:

export default defineConfig({
  workspace: 'packages/*',
  entry: ['src/index.ts'],
  format: ['esm', 'cjs'],
  dts: true,
})

CLI Quick Reference
# Basic commands
tsdown                          # Build once
tsdown --watch                  # Watch mode
tsdown --config custom.ts       # Custom config
npx tsdown-migrate              # Migrate from tsup

# Output options
tsdown --format esm,cjs        # Multiple formats
tsdown -d lib                  # Custom output directory (--out-dir)
tsdown --minify                # Enable minification
tsdown --dts                   # Generate declarations
tsdown --exe                   # Bundle as standalone executable
tsdown --unbundle              # Bundleless mode

# Entry options
tsdown src/index.ts            # Single entry
tsdown src/*.ts                # Glob patterns
tsdown src/a.ts src/b.ts       # Multiple entries

# Workspace / Monorepo
tsdown -W                      # Enable workspace mode
tsdown -W -F my-package        # Filter specific package
tsdown --filter /^pkg-/        # Filter by regex

# Development
tsdown --watch                 # Watch mode
tsdown --sourcemap             # Generate source maps
tsdown --clean                 # Clean output directory
tsdown --from-vite             # Reuse Vite config
tsdown --tsconfig tsconfig.build.json  # Custom tsconfig

Best Practices

Always generate type declarations for TypeScript libraries:

{ dts: true }


Externalize dependencies to avoid bundling unnecessary code:

{ deps: { neverBundle: [/^react/, /^@myorg\//] } }


Use tree shaking for optimal bundle size:

{ treeshake: true }


Enable minification for production builds:

{ minify: true }


Add shims for better ESM/CJS compatibility:

{ shims: true }  // Adds __dirname, __filename, etc.


Auto-generate package.json exports:

{ exports: true }  // Creates proper exports field


Use watch mode during development:

tsdown --watch


Preserve structure for utilities with many files:

{ unbundle: true }  // Keep directory structure


Validate packages in CI before publishing:

{ publint: 'ci-only', attw: 'ci-only' }

Resources
Documentation: https://tsdown.dev
GitHub: https://github.com/rolldown/tsdown
Rolldown: https://rolldown.rs
Migration Guide: https://tsdown.dev/guide/migrate-from-tsup
Weekly Installs
7.5K
Repository
antfu/skills
GitHub Stars
4.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass