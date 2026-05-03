---
title: vite
url: https://skills.sh/antfu/skills/vite
---

# vite

skills/antfu/skills/vite
vite
Installation
$ npx skills add https://github.com/antfu/skills --skill vite
Summary

Next-generation frontend build tool with native ESM dev server, HMR, and Rolldown-powered production builds.

Fast dev server using native ES modules and hot module replacement; production builds optimized with Rolldown bundler and Oxc transformer
Configuration via vite.config.ts with support for conditional configs, environment variables, and plugin API for extending build behavior
Built-in features include import.meta.glob for dynamic imports, asset queries (?raw, ?url), and HMR API for custom refresh logic
Library mode and SSR support with ssrLoadModule and JavaScript API for programmatic builds
Vite 8 introduces multi-environment API for custom runtimes and migration path from traditional bundlers
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
Weekly Installs
20.2K
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