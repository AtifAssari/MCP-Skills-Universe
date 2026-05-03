---
title: vercel-deploy
url: https://skills.sh/vercel-labs/vercel-deploy-codex-skill/vercel-deploy
---

# vercel-deploy

skills/vercel-labs/vercel-deploy-codex-skill/vercel-deploy
vercel-deploy
Installation
$ npx skills add https://github.com/vercel-labs/vercel-deploy-codex-skill --skill vercel-deploy
SKILL.md
Vercel Deploy

Deploy any project to Vercel instantly. No authentication required.

How It Works
Packages your project into a .tar.gz (excludes node_modules and .git)
Auto-detects framework from package.json
Uploads to deployment service
Returns Preview URL (live site) and Claim URL (transfer to your Vercel account)
Usage
bash scripts/deploy.sh [path]


Arguments:

path - Directory to deploy, or a .tgz file (defaults to current directory)

If you pass a directory, the script will create a .tar.gz before upload.

Examples:

# Deploy current directory
bash scripts/deploy.sh

# Deploy specific project
bash scripts/deploy.sh /path/to/project

# Deploy existing tarball
bash scripts/deploy.sh /path/to/project.tgz

Packaging Rules
Exclude node_modules and .git
If no package.json, keep framework as null
For static HTML with a single .html file, rename it to index.html before packaging
Output
Preparing deployment...
Creating deployment package...
Deploying...
✓ Deployment successful!

Preview URL: https://skill-deploy-abc123.vercel.app
Claim URL:   https://vercel.com/claim-deployment?code=...


The script also outputs JSON to stdout for programmatic use.

{
  "previewUrl": "https://skill-deploy-abc123.vercel.app",
  "claimUrl": "https://vercel.com/claim-deployment?code=...",
  "deploymentId": "dpl_...",
  "projectId": "prj_..."
}

Framework Detection

The script auto-detects frameworks from package.json. Supported frameworks include:

React: Next.js, Gatsby, Create React App, Remix, React Router
Vue: Nuxt, Vitepress, Vuepress, Gridsome
Svelte: SvelteKit, Svelte, Sapper
Other Frontend: Astro, Solid Start, Angular, Ember, Preact, Docusaurus
Backend: Express, Hono, Fastify, NestJS, Elysia, h3, Nitro
Build Tools: Vite, Parcel
And more: Blitz, Hydrogen, RedwoodJS, Storybook, Sanity, etc.

For static HTML projects (no package.json), framework is set to null.

Static HTML Projects

For projects without a package.json:

If there's a single .html file not named index.html, it gets renamed automatically
This ensures the page is served at the root URL (/)
Present Results to User

Always show both URLs:

✓ Deployment successful!

Preview URL: https://skill-deploy-abc123.vercel.app
Claim URL:   https://vercel.com/claim-deployment?code=...

View your site at the Preview URL.
To transfer this deployment to your Vercel account, visit the Claim URL.

Troubleshooting
Network Egress Error

If deployment fails due to network restrictions, tell the user:

Deployment failed due to network restrictions. To fix this:

1. Allow outbound access to *.vercel.com
2. Try deploying again

Weekly Installs
39
Repository
vercel-labs/ver…ex-skill
GitHub Stars
4
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail