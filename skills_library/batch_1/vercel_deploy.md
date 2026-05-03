---
title: vercel-deploy
url: https://skills.sh/supercent-io/skills-template/vercel-deploy
---

# vercel-deploy

skills/supercent-io/skills-template/vercel-deploy
vercel-deploy
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill vercel-deploy
Summary

Instant deployment to Vercel with preview and claimable links, no authentication required.

Supports 20+ frameworks including Next.js, React, Vue, Svelte, Angular, Express, and static HTML projects with automatic framework detection
Returns two URLs: a live Preview URL for immediate access and a Claim URL to transfer the deployment to your Vercel account
Packages projects efficiently by excluding node_modules and .git directories to minimize upload size
Works in Claude environment via a single bash command with optional path or tarball arguments
SKILL.md
Vercel Deploy

Deploy any project to Vercel instantly. No authentication required.

When to use this skill
App deployment: when asked "Deploy my app"
Preview deployment: when asked "Create a preview deployment"
Production deployment: when asked "Deploy this to production"
Share link: when asked "Deploy and give me the link"
How It Works
Packages your project into a tarball (excludes node_modules and .git)
Auto-detects framework from package.json
Uploads to deployment service
Returns Preview URL (live site) and Claim URL (transfer to your Vercel account)
Instructions
Step 1: Prepare Project

Confirm the project directory to deploy.

Supported frameworks:

React: Next.js, Gatsby, Create React App, Remix, React Router
Vue: Nuxt, Vitepress, Vuepress, Gridsome
Svelte: SvelteKit, Svelte, Sapper
Other Frontend: Astro, Solid Start, Angular, Ember, Preact, Docusaurus
Backend: Express, Hono, Fastify, NestJS, Elysia, h3, Nitro
Build Tools: Vite, Parcel
And more: Blitz, Hydrogen, RedwoodJS, Storybook, Sanity, etc.
Step 2: Run Deployment

Use the script (claude.ai environment):

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

Step 3: Verify Result

On successful deployment, two URLs are returned:

Preview URL: live site you can access immediately
Claim URL: transfer this deployment to your Vercel account
Output Format
Console Output
Preparing deployment...
Detected framework: nextjs
Creating deployment package...
Deploying...
✓ Deployment successful!

Preview URL: https://skill-deploy-abc123.vercel.app
Claim URL:   https://vercel.com/claim-deployment?code=...

JSON Output (for automation)
{
  "previewUrl": "https://skill-deploy-abc123.vercel.app",
  "claimUrl": "https://vercel.com/claim-deployment?code=...",
  "deploymentId": "dpl_...",
  "projectId": "prj_..."
}

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

Framework Not Detected

If the framework is not detected:

Check that package.json exists
Check that your dependencies include the framework package
Manually set the framework parameter
Constraints
Required Rules (MUST)
Show both URLs: show both the Preview URL and Claim URL to the user
Framework detection: auto-detect from package.json
Show error messages: show a clear error message if deployment fails
Prohibited (MUST NOT)
Include node_modules: do not include node_modules in the tarball
Include .git: do not include the .git directory in the tarball
Hardcode credentials: no authentication required (claimable deploy)
Best practices
Automatic framework detection: pick optimal settings by analyzing package.json
Clean Tarball: exclude node_modules and .git for faster uploads
Clear output: clearly distinguish the Preview URL and Claim URL
References
Vercel Documentation
Vercel CLI
Metadata
Version
Current version: 1.0.0
Last updated: 2026-01-22
Supported platforms: Claude (claude.ai)
Source: vercel/agent-skills
Related Skills
deployment-automation: CI/CD and Docker/K8s deployments
Tags

#deployment #vercel #preview #production #hosting #serverless #infrastructure

Weekly Installs
10.6K
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail