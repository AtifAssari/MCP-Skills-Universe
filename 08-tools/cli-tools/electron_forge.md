---
rating: ⭐⭐
title: electron-forge
url: https://skills.sh/hairyf/skills/electron-forge
---

# electron-forge

skills/hairyf/skills/electron-forge
electron-forge
Installation
$ npx skills add https://github.com/hairyf/skills --skill electron-forge
SKILL.md

Electron Forge is an all-in-one tool for packaging and distributing Electron applications. It combines packaging, code signing, installers, and publishing into one pipeline and supports custom plugins, makers, and publishers.

Skills are based on Electron Forge (docs as of 2026-01-30), generated from electron-forge-docs.

Core References
Topic	Description	Reference
Why Electron Forge	Motivation, value proposition, Forge vs Builder	core-why-electron-forge
Build Lifecycle	Package → Make → Publish; hooks; cross-platform	core-build-lifecycle
CLI	Init, import, package, make, publish, start; flags; programmatic API	core-cli
Configuration
Topic	Description	Reference
Configuration	forge.config.js, packagerConfig, makers, publishers, plugins, hooks, buildIdentifier	config-configuration
Hooks	generateAssets, preStart, postPackage, preMake, postMake, readPackageJson, etc.	config-hooks
TypeScript config	forge.config.ts, ForgeConfig, constructor syntax	config-typescript
Plugins overview	Bundler (Webpack, Vite) and utility plugins	config-plugins-overview
Webpack plugin	main/renderer config, magic globals, HMR, native modules	config-plugins-webpack
Vite plugin	build/renderer entries, HMR globals, native externals	config-plugins-vite
Makers overview	Config, platforms; DMG, ZIP, Squirrel, deb, rpm, etc.	config-makers-overview
Publishers overview	GitHub, S3, Nucleus; config; auto-update	config-publishers-overview
Features
Topic	Description	Reference
Import existing project	import command and manual setup	features-import-existing-project
Built-in templates	webpack, vite, TypeScript variants; create-electron-app	features-templates
Guides
Topic	Description	Reference
Code signing	macOS and Windows; where to configure	guides-code-signing
Advanced
Topic	Description	Reference
Auto update	update.electronjs.org, S3, custom servers (Nucleus, etc.)	advanced-auto-update
Debugging	Main process: CLI, VS Code, JetBrains	advanced-debugging
Writing plugins	PluginBase, getHooks, startLogic	advanced-extending-plugins
Writing makers	MakerBase, isSupportedOnCurrentPlatform, make	advanced-extending-makers
Writing publishers	PublisherBase, publish; multi-call behavior	advanced-extending-publishers
Writing templates	ForgeTemplate, requiredForgeVersion, initializeTemplate	advanced-extending-templates
Weekly Installs
61
Repository
hairyf/skills
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass