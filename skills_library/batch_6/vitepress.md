---
title: vitepress
url: https://skills.sh/antfu/skills/vitepress
---

# vitepress

skills/antfu/skills/vitepress
vitepress
Installation
$ npx skills add https://github.com/antfu/skills --skill vitepress
Summary

Static site generator for documentation and blogs with Vue components in Markdown.

File-based routing with Markdown files, Vue 3 component support, and instant HMR updates
Configurable default theme with built-in search (local or Algolia), navigation, sidebar, and social links
Code block features include syntax highlighting, line highlighting, diffs, and focus regions
Build-time data loaders and dynamic route generation for content-driven sites
Multi-language support, custom theme building, and deployment guides for major platforms
SKILL.md

VitePress is a Static Site Generator (SSG) built on Vite and Vue 3. It takes Markdown content, applies a theme, and generates static HTML that becomes an SPA for fast navigation. Perfect for documentation, blogs, and marketing sites.

Key Characteristics:

File-based routing with .md files
Vue components work directly in Markdown
Fast HMR with instant updates (<100ms)
Default theme optimized for documentation
Built-in search (local or Algolia)

Before working with VitePress projects:

Check .vitepress/config.ts for site configuration
Look at .vitepress/theme/ for custom theme extensions
The public/ directory contains static assets served as-is

The skill is based on VitePress 1.x, generated at 2026-01-28.

Core
Topic	Description	Reference
Configuration	Config file setup, defineConfig, site metadata	core-config
CLI	Command-line interface: dev, build, preview, init	core-cli
Routing	File-based routing, source directory, rewrites	core-routing
Markdown	Frontmatter, containers, tables, anchors, includes	core-markdown
Features
Code & Content
Topic	Description	Reference
Code Blocks	Syntax highlighting, line highlighting, diffs, focus	features-code-blocks
Vue in Markdown	Components, script setup, directives, templating	features-vue
Data Loading	Build-time data loaders, createContentLoader	features-data-loading
Dynamic Routes	Generate pages from data, paths loader files	features-dynamic-routes
Theme
Topic	Description	Reference
Theme Config	Nav, sidebar, search, social links, footer	theme-config
Customization	CSS variables, slots, fonts, global components	theme-customization
Custom Theme	Building themes from scratch, theme interface	theme-custom
Advanced
Topic	Description	Reference
Internationalization	Multi-language sites, locale configuration	advanced-i18n
SSR Compatibility	Server-side rendering, ClientOnly, dynamic imports	advanced-ssr
Recipes
Topic	Description	Reference
Deployment	GitHub Pages, Netlify, Vercel, Cloudflare, Nginx	recipes-deploy
Weekly Installs
7.0K
Repository
antfu/skills
GitHub Stars
4.8K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn