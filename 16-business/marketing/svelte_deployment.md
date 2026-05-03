---
rating: ⭐⭐⭐
title: svelte-deployment
url: https://skills.sh/spences10/svelte-skills-kit/svelte-deployment
---

# svelte-deployment

skills/spences10/svelte-skills-kit/svelte-deployment
svelte-deployment
Installation
$ npx skills add https://github.com/spences10/svelte-skills-kit --skill svelte-deployment
SKILL.md
Svelte Deployment
Quick Start

pnpm 10+: Add prepare script (postinstall disabled by default):

{
	"scripts": {
		"prepare": "svelte-kit sync"
	}
}


Vite 7: Update both packages together:

pnpm add -D vite@7 @sveltejs/vite-plugin-svelte@6

Adapters
# Static site
pnpm add -D @sveltejs/adapter-static

# Node server
pnpm add -D @sveltejs/adapter-node

# Cloudflare
pnpm add -D @sveltejs/adapter-cloudflare

Reference Files
library-authoring.md - Publishing Svelte packages
pwa-setup.md - Offline-first with workbox
cloudflare-gotchas.md - Streaming issues
Notes
Cloudflare may strip Transfer-Encoding: chunked (breaks streaming)
Library authors: include svelte in keywords AND peerDependencies
Single-file bundle: kit.output.bundleStrategy: 'single'
Last verified: 2025-01-14
Weekly Installs
116
Repository
spences10/svelt…ills-kit
GitHub Stars
77
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass