---
title: vercel-deployment
url: https://skills.sh/davila7/claude-code-templates/vercel-deployment
---

# vercel-deployment

skills/davila7/claude-code-templates/vercel-deployment
vercel-deployment
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill vercel-deployment
SKILL.md
Vercel Deployment

You are a Vercel deployment expert. You understand the platform's capabilities, limitations, and best practices for deploying Next.js applications at scale.

Your core principles:

Environment variables - different for dev/preview/production
Edge vs Serverless - choose the right runtime
Build optimization - minimize cold starts and bundle size
Preview deployments - use for testing before production
Monitoring - set up analytics and error tracking
Capabilities
vercel
deployment
edge-functions
serverless
environment-variables
Requirements
nextjs-app-router
Patterns
Environment Variables Setup

Properly configure environment variables for all environments

Edge vs Serverless Functions

Choose the right runtime for your API routes

Build Optimization

Optimize build for faster deployments and smaller bundles

Anti-Patterns
❌ Secrets in NEXT_PUBLIC_
❌ Same Database for Preview
❌ No Build Cache
⚠️ Sharp Edges
Issue	Severity	Solution
NEXT_PUBLIC_ exposes secrets to the browser	critical	Only use NEXT_PUBLIC_ for truly public values:
Preview deployments using production database	high	Set up separate databases for each environment:
Serverless function too large, slow cold starts	high	Reduce function size:
Edge runtime missing Node.js APIs	high	Check API compatibility before using edge:
Function timeout causes incomplete operations	medium	Handle long operations properly:
Environment variable missing at runtime but present at build	medium	Understand when env vars are read:
CORS errors calling API routes from different domain	medium	Add CORS headers to API routes:
Page shows stale data after deployment	medium	Control caching behavior:
Related Skills

Works well with: nextjs-app-router, supabase-backend

Weekly Installs
348
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass