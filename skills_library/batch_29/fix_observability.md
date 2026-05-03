---
title: fix-observability
url: https://skills.sh/phrazzld/claude-config/fix-observability
---

# fix-observability

skills/phrazzld/claude-config/fix-observability
fix-observability
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill fix-observability
SKILL.md
/fix-observability

Fix the highest priority observability gap.

What This Does
Invoke /check-observability to audit monitoring
Identify highest priority gap
Fix that one issue
Verify the fix
Report what was done

This is a fixer. It fixes one issue at a time. Run again for next issue. Use /observability for full setup.

Process
1. Run Primitive

Invoke /check-observability skill to get prioritized findings.

2. Fix Priority Order

Fix in this order:

P0: No error tracking, no health endpoint
P1: Sentry config, structured logging, alerting
P2: Analytics, console cleanup
P3: Performance monitoring
3. Execute Fix

No error tracking (P0):

pnpm add @sentry/nextjs
npx @sentry/wizard@latest -i nextjs


Or manual setup:

~/.claude/skills/sentry-observability/scripts/init_sentry.sh


No health endpoint (P0): Create app/api/health/route.ts:

export async function GET() {
  const checks = {
    status: 'ok',
    timestamp: new Date().toISOString(),
    // Add service checks as needed
  };
  return Response.json(checks);
}


Sentry misconfigured (P1): Add to .env.local:

NEXT_PUBLIC_SENTRY_DSN=your-dsn
SENTRY_AUTH_TOKEN=your-token
SENTRY_ORG=your-org
SENTRY_PROJECT=your-project


No structured logging (P1):

pnpm add pino


Create lib/logger.ts:

import pino from 'pino';

export const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
});


No alerting (P1): Create alert via Sentry CLI or scripts:

~/.claude/skills/sentry-observability/scripts/create_alert.sh --name "New Errors" --type issue


No PostHog analytics (P1):

Install dependency:
pnpm add posthog-js


Create analytics module from template:

Source: ~/.claude/skills/observability/references/posthog-patterns.md
Target: lib/analytics/posthog.ts

Create PostHogProvider:

Target: components/providers/PostHogProvider.tsx
If Clerk detected, include user identification integration

Update app/layout.tsx:

Wrap children with <PostHogProvider>
Place inside existing providers (ClerkProvider, ConvexClientProvider)

Add env vars to .env.example:

# PostHog [REQUIRED] - Product analytics
NEXT_PUBLIC_POSTHOG_KEY=
NEXT_PUBLIC_POSTHOG_HOST=https://us.i.posthog.com

Verify setup:
pnpm dev
# Open browser, check PostHog debug mode shows events
# Check PostHog dashboard for incoming events


PostHog installed but not configured (P2): Add to .env.local:

NEXT_PUBLIC_POSTHOG_KEY=phc_xxx  # From PostHog project settings
NEXT_PUBLIC_POSTHOG_HOST=https://us.i.posthog.com

4. Verify

After fix:

# Sentry works
~/.claude/skills/sentry-observability/scripts/verify_setup.sh

# Health endpoint works
curl -s http://localhost:3000/api/health | jq

5. Report
Fixed: [P0] No error tracking

Installed: @sentry/nextjs
Configured: sentry.client.config.ts, sentry.server.config.ts
Added: SENTRY_DSN to .env.local

Verified: Sentry SDK initialized

Next highest priority: [P0] No health endpoint
Run /fix-observability again to continue.

Branching

Before making changes:

git checkout -b infra/observability-$(date +%Y%m%d)

Single-Issue Focus

This skill fixes one issue at a time. Benefits:

Test each monitoring component independently
Easy to troubleshoot if something fails
Clear audit trail

Run /fix-observability repeatedly to work through the backlog.

Related
/check-observability - The primitive (audit only)
/log-observability-issues - Create issues without fixing
/observability - Full observability setup
/triage - Production incident response
Weekly Installs
23
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass