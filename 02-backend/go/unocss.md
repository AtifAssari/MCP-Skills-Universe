---
rating: ⭐⭐
title: unocss
url: https://skills.sh/antfu/skills/unocss
---

# unocss

skills/antfu/skills/unocss
unocss
Installation
$ npx skills add https://github.com/antfu/skills --skill unocss
Summary

Instant atomic CSS engine with Tailwind CSS compatibility and flexible preset-based architecture.

Superset of Tailwind CSS with un-opinionated core; all utilities provided via presets including Wind3, Wind4, Mini, Icons, Attributify, Typography, and Web Fonts
Supports static and dynamic rules, shortcuts, theming, variants, and CSS layers for fine-grained styling control
Includes transformers for variant grouping, CSS directives (@apply, @screen, theme()), and JSX attributify support
Integrates with Vite and Nuxt; always check for uno.config.* or unocss.config.* files before writing code to understand available presets and rules
SKILL.md

UnoCSS is an instant atomic CSS engine designed to be flexible and extensible. The core is un-opinionated - all CSS utilities are provided via presets. It's a superset of Tailwind CSS, so you can reuse your Tailwind knowledge for basic syntax usage.

Important: Before writing UnoCSS code, agents should check for uno.config.* or unocss.config.* files in the project root to understand what presets, rules, and shortcuts are available. If the project setup is unclear, avoid using attributify mode and other advanced features - stick to basic class usage.

The skill is based on UnoCSS 66.x, generated at 2026-01-28.

Core
Topic	Description	Reference
Configuration	Config file setup and all configuration options	core-config
Rules	Static and dynamic rules for generating CSS utilities	core-rules
Shortcuts	Combine multiple rules into single shorthands	core-shortcuts
Theme	Theming system for colors, breakpoints, and design tokens	core-theme
Variants	Apply variations like hover:, dark:, responsive to rules	core-variants
Extracting	How UnoCSS extracts utilities from source code	core-extracting
Safelist & Blocklist	Force include or exclude specific utilities	core-safelist
Layers & Preflights	CSS layer ordering and raw CSS injection	core-layers
Presets
Main Presets
Topic	Description	Reference
Preset Wind3	Tailwind CSS v3 / Windi CSS compatible preset (most common)	preset-wind3
Preset Wind4	Tailwind CSS v4 compatible preset with modern CSS features	preset-wind4
Preset Mini	Minimal preset with essential utilities for custom builds	preset-mini
Feature Presets
Topic	Description	Reference
Preset Icons	Pure CSS icons using Iconify with any icon set	preset-icons
Preset Attributify	Group utilities in HTML attributes instead of class	preset-attributify
Preset Typography	Prose classes for typographic defaults	preset-typography
Preset Web Fonts	Easy Google Fonts and other web fonts integration	preset-web-fonts
Preset Tagify	Use utilities as HTML tag names	preset-tagify
Preset Rem to Px	Convert rem units to px for utilities	preset-rem-to-px
Transformers
Topic	Description	Reference
Variant Group	Shorthand for grouping utilities with common prefixes	transformer-variant-group
Directives	CSS directives: @apply, @screen, theme(), icon()	transformer-directives
Compile Class	Compile multiple classes into one hashed class	transformer-compile-class
Attributify JSX	Support valueless attributify in JSX/TSX	transformer-attributify-jsx
Integrations
Topic	Description	Reference
Vite Integration	Setting up UnoCSS with Vite and framework-specific tips	integrations-vite
Nuxt Integration	UnoCSS module for Nuxt applications	integrations-nuxt
Weekly Installs
10.6K
Repository
antfu/skills
GitHub Stars
4.8K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn