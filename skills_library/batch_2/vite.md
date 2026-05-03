---
title: vite
url: https://skills.sh/onmax/nuxt-skills/vite
---

# vite

skills/onmax/nuxt-skills/vite
vite
Originally fromantfu/skills
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill vite
Summary

Next-generation frontend build tool with native ESM dev server, HMR, and Rolldown-powered production builds.

Fast development server using native ES modules and hot module replacement; production builds optimized with Rolldown bundler and Oxc transformer
Configuration via vite.config.ts with support for conditional configs, environment variables, and TypeScript; plugin API for extending build behavior
Built-in asset handling with import queries (?raw, ?url), glob imports, and import.meta.env for environment-based logic
Library mode and SSR support including middleware mode, ssrLoadModule, and JavaScript API for programmatic builds
Official plugins available for Vue 3, React, JSX, and legacy browser support; Vite 8 migration guide for Rolldown adoption
SKILL.md
Vite

Based on Vite 8 beta (Rolldown-powered). Vite 8 uses Rolldown bundler and Oxc transformer.

Vite is a next-generation frontend build tool with fast dev server (native ESM + HMR) and optimized production builds.

Preferences
Use TypeScript: prefer vite.config.ts
Always use ESM, avoid CommonJS
Core
Topic	Description	Reference
Configuration	vite.config.ts, defineConfig, conditional configs, loadEnv	core-config
Features	import.meta.glob, asset queries (?raw, ?url), import.meta.env, HMR API	core-features
Plugin API	Vite-specific hooks, virtual modules, plugin ordering	core-plugin-api
Build & SSR
Topic	Description	Reference
Build & SSR	Library mode, SSR middleware mode, ssrLoadModule, JavaScript API	build-and-ssr
Advanced
Topic	Description	Reference
Environment API	Vite 6+ multi-environment support, custom runtimes	environment-api
Rolldown Migration	Vite 8 changes: Rolldown bundler, Oxc transformer, config migration	rolldown-migration
Quick Reference
CLI Commands
vite              # Start dev server
vite build        # Production build
vite preview      # Preview production build
vite build --ssr  # SSR build

Common Config
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [],
  resolve: { alias: { '@': '/src' } },
  server: { port: 3000, proxy: { '/api': 'http://localhost:8080' } },
  build: { target: 'esnext', outDir: 'dist' },
})

Official Plugins
@vitejs/plugin-vue - Vue 3 SFC support
@vitejs/plugin-vue-jsx - Vue 3 JSX
@vitejs/plugin-react - React with Oxc/Babel
@vitejs/plugin-react-swc - React with SWC
@vitejs/plugin-legacy - Legacy browser support
Cross-Skill References
Testing → Use vitest skill (Vite-native testing)
Vue projects → Use vue skill for component patterns
Library bundling → Use tsdown skill for TypeScript libs
Weekly Installs
1.2K
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass