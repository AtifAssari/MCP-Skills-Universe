---
title: deploy-cloudflare
url: https://skills.sh/dralgorhythm/claude-agentic-framework/deploy-cloudflare
---

# deploy-cloudflare

skills/dralgorhythm/claude-agentic-framework/deploy-cloudflare
deploy-cloudflare
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill deploy-cloudflare
SKILL.md
Deploy to Cloudflare
Why Cloudflare?
Global edge network (300+ cities)
Zero cold starts (Workers)
Automatic HTTPS and DDoS protection
Integrated CDN and DNS
Generous free tier
Quick Start
# Install Wrangler
npm install -g wrangler

# Login
wrangler login

# Deploy Pages
wrangler pages deploy ./dist

# Deploy Worker
wrangler deploy

Cloudflare Pages
Deploy Static Site
# One-time deploy
wrangler pages deploy ./dist --project-name=my-app

# Connect Git repo (auto-deploy)
wrangler pages project create my-app --production-branch=main

Build Configuration
# wrangler.toml (Pages Functions)
name = "my-app"
compatibility_date = "2025-01-01"

[build]
command = "npm run build"

Cloudflare Workers
Worker Configuration
# wrangler.toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2025-01-01"

[vars]
ENVIRONMENT = "production"

[[kv_namespaces]]
binding = "MY_KV"
id = "abc123"

Basic Worker
export default {
  async fetch(request, env, ctx) {
    return new Response('Hello from the edge!', {
      headers: { 'Content-Type': 'text/plain' }
    });
  }
};

Environment & Secrets
# Set secret (encrypted)
wrangler secret put API_KEY

# Set variable (plain text)
wrangler pages secret put API_URL

# Bulk upload
echo "SECRET_KEY" | wrangler secret put SECRET_KEY

DNS Management
# List DNS records
wrangler dns list example.com

# Add A record
wrangler dns create example.com --type A --name www --content 1.2.3.4

# Update record
wrangler dns update example.com --type A --name www --content 5.6.7.8

Deployment Workflow
1. Initialize Project
wrangler init my-project
cd my-project

2. Develop Locally
wrangler dev

3. Deploy
# Production
wrangler deploy

# Preview
wrangler deploy --env staging

Best Practices
Use Environments: Separate staging and production
Versioning: Rollback via dashboard if needed
Edge Caching: Leverage Cache API for performance
Rate Limiting: Protect Workers with rate limits
Monitoring: Enable Workers Analytics
Common Commands
# View logs (tail)
wrangler tail

# List deployments
wrangler deployments list

# Rollback
wrangler rollback --message "Revert breaking change"

# KV operations
wrangler kv:key put --binding=MY_KV "key" "value"
wrangler kv:key get --binding=MY_KV "key"

Anti-Patterns
Don't store secrets in wrangler.toml (use wrangler secret)
Don't deploy without testing locally (wrangler dev)
Don't ignore compatibility_date (affects runtime behavior)
Don't use Workers for long-running tasks (30s limit)
Weekly Installs
33
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail