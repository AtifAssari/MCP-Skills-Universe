---
title: arch-webext-vue
url: https://skills.sh/hairyf/skills/arch-webext-vue
---

# arch-webext-vue

skills/hairyf/skills/arch-webext-vue
arch-webext-vue
Installation
$ npx skills add https://github.com/hairyf/skills --skill arch-webext-vue
SKILL.md

arch-webext-vue skills cover Vitesse WebExt: a Vite-powered WebExtension starter with Vue 3, TypeScript, UnoCSS, and webext-bridge. It uses multi-entry Vite for popup/options/sidepanel, separate configs for background and content script, dynamic manifest generation, and shared setup and storage patterns. Use these skills when creating or maintaining a browser extension with this stack.

The skill is based on vitesse-webext (antfu-collective/vitesse-webext), generated at 2026-01-30.

Core References
Topic	Description	Reference
Overview	Features, stack, when to use	core-overview
Project structure	Folders, entry points, scripts	core-project-structure
Manifest	Dynamic manifest, MV3, Firefox vs Chrome	core-manifest
CI	GitHub Actions — lint, typecheck, build, test, optional E2E	core-ci
Features
Topic	Description	Reference
Vite build	Multi-config, shared config, background/content, dev stub	features-vite-build
Background	Entry, webext-bridge, side panel, content script HMR	features-background
Content script	Entry, Vue in shadow DOM, styles	features-content-script
Views	Popup, options, sidepanel—entry pattern, setupApp	features-views
Storage	useWebExtensionStorage, shared logic	features-storage
Cross-context	webext-bridge messaging between contexts	features-cross-context
Dev workflow	pnpm dev vs dev-firefox, load extension, stub HTML	features-dev-workflow
Pack & release	pack:zip, crx, xpi, clear, start:chromium/firefox	features-pack-release
Testing	Vitest unit tests, Playwright E2E, fixtures, extensionId	features-testing
Types & env	DEV, NAME, global/shim/modules.d.ts, env.ts	features-types-and-env
Components & icons	Auto-import components and icons, Iconify	features-components-icons
Best Practices
Topic	Description	Reference
Setup patterns	setupApp, common-setup, shared components/styles	best-practices-setup-patterns
Type-safe messaging	ProtocolMap in shim.d.ts for webext-bridge	best-practices-type-safe-messaging
Weekly Installs
42
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