---
title: vercel-deploy
url: https://skills.sh/vercel-labs/agent-skills/vercel-deploy
---

# vercel-deploy

skills/vercel-labs/agent-skills/vercel-deploy
vercel-deploy
Installation
$ npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-deploy
Summary

Instant deployment to Vercel with auto-detected frameworks and no authentication required.

Packages projects into tarballs, auto-detects frameworks from package.json, and returns a live preview URL plus a claimable deployment link for account transfer
Supports 20+ frameworks across React, Vue, Svelte, backend runtimes, and static HTML projects
Excludes node_modules and .git from deployments to minimize package size
Returns both human-readable URLs and JSON output for programmatic integration
SKILL.md
Vercel Deploy

Deploy any project to Vercel instantly. No authentication required.

How It Works
Packages your project into a tarball (excludes node_modules and .git)
Auto-detects framework from package.json
Uploads to deployment service
Returns Preview URL (live site) and Claim URL (transfer to your Vercel account)
Usage
bash /mnt/skills/user/vercel-deploy/scripts/deploy.sh [path]


Arguments:

path - Directory to deploy, or a .tgz file (defaults to current directory)

Examples:

# Deploy current directory
bash /mnt/skills/user/vercel-deploy/scripts/deploy.sh

# Deploy specific project
bash /mnt/skills/user/vercel-deploy/scripts/deploy.sh /path/to/project

# Deploy existing tarball
bash /mnt/skills/user/vercel-deploy/scripts/deploy.sh /path/to/project.tgz

Output
Preparing deployment...
Detected framework: nextjs
Creating deployment package...
Deploying...
✓ Deployment successful!

Preview URL: https://skill-deploy-abc123.vercel.app
Claim URL:   https://vercel.com/claim-deployment?code=...


The script also outputs JSON to stdout for programmatic use:

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

If deployment fails due to network restrictions (common on claude.ai), tell the user:

Deployment failed due to network restrictions. To fix this:

1. Go to https://claude.ai/settings/capabilities
2. Add *.vercel.com to the allowed domains
3. Try deploying again

Weekly Installs
519
Repository
vercel-labs/agent-skills
GitHub Stars
26.0K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail