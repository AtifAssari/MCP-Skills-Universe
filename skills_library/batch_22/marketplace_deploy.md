---
title: marketplace-deploy
url: https://skills.sh/vercel-labs/sitecore-skills/marketplace-deploy
---

# marketplace-deploy

skills/vercel-labs/sitecore-skills/marketplace-deploy
marketplace-deploy
Installation
$ npx skills add https://github.com/vercel-labs/sitecore-skills --skill marketplace-deploy
SKILL.md
Deploy to Vercel

You are helping the user deploy their Sitecore Marketplace app to Vercel.

Important: This skill has real side effects (deploying to production). Confirm each step with the user before executing.

Pre-Deploy Checklist

Before deploying, verify:

Build succeeds locally:
npm run build

CSP headers are configured — Check next.config.ts for frame-ancestors:
// next.config.ts must include:
headers: [
  {
    source: "/(.*)",
    headers: [
      {
        key: "Content-Security-Policy",
        value: "frame-ancestors 'self' https://*.sitecorecloud.io",
      },
    ],
  },
]


Environment variables are set — Check that .env.local exists and has required values

Extension points are registered — All routes defined in the app should be registered in the Developer Portal

Deploy Steps
Step 1: Install Vercel CLI (if needed)
npm i -g vercel

Step 2: Link to Vercel project
vercel link

Step 3: Set environment variables
# For client-side apps
vercel env add NEXT_PUBLIC_SITECORE_APP_ID

# For full-stack (Auth0) apps — add all Auth0 vars too
vercel env add AUTH0_SECRET
vercel env add AUTH0_BASE_URL
vercel env add AUTH0_ISSUER_BASE_URL
vercel env add AUTH0_CLIENT_ID
vercel env add AUTH0_CLIENT_SECRET
vercel env add AUTH0_AUDIENCE
vercel env add AUTH0_SCOPE

Step 4: Deploy
# Preview deployment
vercel

# Production deployment
vercel --prod

Step 5: Post-Deploy Configuration

After deploying:

Copy the production URL from Vercel
Go to Sitecore Developer Portal → Your App → Settings
Set the App URL to the Vercel production URL
Update AUTH0_BASE_URL env var in Vercel to match the production URL (if using Auth0)
Reference Files
Vercel Config — vercel.json and next.config.ts templates
Weekly Installs
11
Repository
vercel-labs/sit…e-skills
GitHub Stars
3
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass