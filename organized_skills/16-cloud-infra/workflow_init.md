---
rating: ⭐⭐
title: workflow-init
url: https://skills.sh/vercel/workflow/workflow-init
---

# workflow-init

skills/vercel/workflow/workflow-init
workflow-init
Installation
$ npx skills add https://github.com/vercel/workflow --skill workflow-init
SKILL.md
workflow-init

Initial setup of Vercel Workflow SDK before workflow is installed. Fetch the official getting-started guide for the user's framework.

Decision Flow
0) Sanity check

Read package.json. If workflow is already a dependency, tell the user to use /workflow instead (it reads versioned docs from node_modules/workflow/docs/). Only continue if workflow is missing.

1) Determine the framework

Non-interactive: If the user named a framework in their prompt, use it directly.

Auto-detect: Inspect package.json deps and config files. Use the first match:

Next.js - next dep or next.config.*
Nuxt - nuxt dep or nuxt.config.*
SvelteKit - @sveltejs/kit dep or svelte.config.*
Astro - astro dep or astro.config.*
NestJS - @nestjs/core dep or nest-cli.json
Nitro - nitro dep or nitro.config.*
Express - express dep
Fastify - fastify dep
Hono - hono dep
Vite - vite dep (and not matched above)

If no match or multiple matches, ask the user to pick.

2) Fetch and follow the getting-started guide

Fetch exactly one of these URLs and follow the guide step-by-step:

Framework	URL
Next.js	https://workflow-sdk.dev/docs/getting-started/next
Express	https://workflow-sdk.dev/docs/getting-started/express
Hono	https://workflow-sdk.dev/docs/getting-started/hono
Fastify	https://workflow-sdk.dev/docs/getting-started/fastify
NestJS	https://workflow-sdk.dev/docs/getting-started/nestjs
Nitro	https://workflow-sdk.dev/docs/getting-started/nitro
Nuxt	https://workflow-sdk.dev/docs/getting-started/nuxt
Astro	https://workflow-sdk.dev/docs/getting-started/astro
SvelteKit	https://workflow-sdk.dev/docs/getting-started/sveltekit
Vite	https://workflow-sdk.dev/docs/getting-started/vite

Each guide covers: install deps, configure framework, create first workflow, create route handler, run + verify.

3) Verify setup
Start the dev server per the guide.
Trigger the example endpoint with the provided curl.
Confirm logs show the workflow and steps executing.
Optional: npx workflow web or npx workflow inspect runs.
4) No framework yet?

If no framework exists, ask what the user wants:

Web app: Next.js / Nuxt / SvelteKit / Astro
API server: Express / Fastify / Hono
Minimal server: Nitro or Vite

Then follow the "Create Your Project" section of the chosen guide.

Concept questions (pre-install)

If the user asks conceptual questions before installing, fetch:

https://workflow-sdk.dev/docs/foundations/workflows-and-steps
https://workflow-sdk.dev/cookbook
Handoff

When setup is complete, tell the user: Use /workflow for ongoing development - it reads the versioned docs bundled in node_modules/workflow/docs/.

Weekly Installs
938
Repository
vercel/workflow
GitHub Stars
2.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn