---
title: env-vars
url: https://skills.sh/vercel/vercel-plugin/env-vars
---

# env-vars

skills/vercel/vercel-plugin/env-vars
env-vars
Installation
$ npx skills add https://github.com/vercel/vercel-plugin --skill env-vars
SKILL.md
Vercel Environment Variables

You are an expert in Vercel environment variable management — .env file conventions, the vercel env CLI, OIDC token lifecycle, and environment-specific configuration.

.env File Hierarchy

Vercel and Next.js load environment variables in a specific order. Later files override earlier ones:

File	Purpose	Git-tracked?
.env	Default values for all environments	Yes
.env.local	Local overrides and secrets	No (gitignored)
.env.development	Development-specific defaults	Yes
.env.development.local	Local dev overrides	No
.env.production	Production-specific defaults	Yes
.env.production.local	Local prod overrides	No
.env.test	Test-specific defaults	Yes
.env.test.local	Local test overrides	No
Load Order (Next.js)
.env (lowest priority)
.env.[environment] (development, production, or test)
.env.local (skipped in test environment)
.env.[environment].local (highest priority, skipped in test)
Critical Rules
Never commit secrets to .env, .env.development, or .env.production — use .local variants or Vercel environment variables
.env.local is always gitignored by Next.js — this is where vercel env pull writes secrets
Variables prefixed with NEXT_PUBLIC_ are exposed to the browser bundle — never put secrets in NEXT_PUBLIC_ vars
All other variables are server-only (API routes, Server Components, middleware)
vercel env CLI
Pull Environment Variables
# Pull all env vars for the current environment into .env.local
vercel env pull .env.local

# Pull for a specific environment
vercel env pull .env.local --environment=production
vercel env pull .env.local --environment=preview
vercel env pull .env.local --environment=development

# Overwrite existing file without prompting
vercel env pull .env.local --yes

# Pull to a custom file
vercel env pull .env.production.local --environment=production

Add Environment Variables
# Interactive — prompts for value and environments
vercel env add MY_SECRET

# Non-interactive
echo "secret-value" | vercel env add MY_SECRET production

# Add to multiple environments
echo "secret-value" | vercel env add MY_SECRET production preview development

# Add a sensitive variable (encrypted, not shown in logs)
vercel env add MY_SECRET --sensitive

List Environment Variables
# List all environment variables
vercel env ls

# Filter by environment
vercel env ls production

Remove Environment Variables
# Remove from specific environment
vercel env rm MY_SECRET production

# Remove from all environments
vercel env rm MY_SECRET

Bootstrap Flow (Fresh Clone / New Machine)

Use this sequence when setting up a project from scratch:

# 1) Link first so pulls target the correct Vercel project
vercel link --yes --project <name-or-id> --scope <team>

# 2) Pull env vars into .env.local
vercel env pull .env.local --yes

# 3) Verify required keys from .env.example exist in .env.local
while IFS='=' read -r key _; do
  [[ -z "$key" || "$key" == \#* ]] && continue
  grep -q "^${key}=" .env.local || echo "Missing in .env.local: $key"
done < .env.example

Temporary Path: Run With Vercel Envs Without Writing a File

If you need Vercel environment variables immediately but do not want to write .env.local yet:

vercel env run -- npm run dev


This is useful for quick validation during bootstrap, but still pull .env.local for a normal local workflow.

Re-pull After Secret or Provisioning Changes

After creating/updating secrets (vercel env add, dashboard changes) or provisioning integrations that add env vars (for example Neon/Upstash), re-run:

vercel env pull .env.local --yes

OIDC Token Lifecycle

Vercel uses OIDC (OpenID Connect) tokens for secure, keyless authentication between your app and Vercel services (AI Gateway, storage, etc.).

How It Works
On Vercel deployments: VERCEL_OIDC_TOKEN is automatically injected as a short-lived JWT and auto-refreshed — zero configuration needed
Local development: vercel env pull .env.local provisions a VERCEL_OIDC_TOKEN valid for ~12 hours
Token expiry: When the local OIDC token expires, re-run vercel env pull .env.local --yes to get a fresh one. Consider re-pulling at the start of each dev session to avoid mid-session auth failures
Common OIDC Patterns
// The @vercel/oidc package reads VERCEL_OIDC_TOKEN automatically
import { getVercelOidcToken } from '@vercel/oidc'

// AI Gateway uses OIDC by default — no manual token handling needed
import { gateway } from 'ai'
const result = await generateText({
  model: gateway('openai/gpt-5.2'),
  prompt: 'Hello',
})

Troubleshooting OIDC
Symptom	Cause	Fix
VERCEL_OIDC_TOKEN missing locally	Haven't pulled env vars	vercel env pull .env.local
Auth errors after ~12h locally	Token expired	vercel env pull .env.local --yes
Works on Vercel, fails locally	Token not in .env.local	vercel env pull .env.local
AI_GATEWAY_API_KEY vs OIDC	Both set, key takes priority	Remove AI_GATEWAY_API_KEY to use OIDC
Environment-Specific Configuration
Vercel Dashboard vs .env Files
Use Case	Where to Set
Secrets (API keys, tokens)	Vercel Dashboard (https://vercel.com/{team}/{project}/settings/environment-variables) or vercel env add
Public config (site URL, feature flags)	.env or .env.[environment] files
Local-only overrides	.env.local
CI/CD secrets	Vercel Dashboard (https://vercel.com/{team}/{project}/settings/environment-variables) with environment scoping
Environment Scoping on Vercel

Variables set in the Vercel Dashboard at https://vercel.com/{team}/{project}/settings/environment-variables can be scoped to:

Production — only vercel.app production deployments
Preview — branch/PR deployments
Development — vercel dev and vercel env pull

A variable can be assigned to one, two, or all three environments.

Git Branch Overrides

Preview environment variables can be scoped to specific Git branches:

# Add a variable only for the "staging" branch
echo "staging-value" | vercel env add DATABASE_URL preview --git-branch=staging

Gotchas
vercel env pull Overwrites Custom Variables

vercel env pull .env.local replaces the entire file — any manually added variables (custom secrets, local overrides, debug flags) are lost. Always back up or re-add custom vars after pulling:

# Save custom vars before pulling
grep -v '^#' .env.local | grep -v '^VERCEL_\|^POSTGRES_\|^NEXT_PUBLIC_' > .env.custom.bak
vercel env pull .env.local --yes
cat .env.custom.bak >> .env.local  # Re-append custom vars


Or maintain custom vars in a separate .env.development.local file (loaded after .env.local by Next.js).

Scripts Don't Auto-Load .env.local

Only Next.js auto-loads .env.local. Standalone scripts (drizzle-kit, tsx, custom Node scripts) need explicit loading:

# Use dotenv-cli
npm install -D dotenv-cli
npx dotenv -e .env.local -- npx drizzle-kit push
npx dotenv -e .env.local -- npx tsx scripts/seed.ts

# Or source manually
source <(grep -v '^#' .env.local | sed 's/^/export /') && node scripts/migrate.js

Best Practices
Use vercel env pull as part of your setup workflow — document it in your README
Never hardcode secrets — always use environment variables
Scope narrowly — don't give preview deployments production database access
Rotate OIDC tokens regularly in local dev — re-pull when you see auth errors
Use .env.example — commit a template with empty values so teammates know which vars are needed
Prefix client-side vars with NEXT_PUBLIC_ — and never put secrets in them
Keep custom vars in .env.development.local — protects them from vercel env pull overwrites
Official Documentation
Environment Variables
Vercel CLI: env
Next.js Environment Variables
Weekly Installs
228
Repository
vercel/vercel-plugin
GitHub Stars
156
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass