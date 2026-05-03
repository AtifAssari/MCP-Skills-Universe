---
rating: ⭐⭐
title: posthog
url: https://skills.sh/andrehfp/tinyplate/posthog
---

# posthog

skills/andrehfp/tinyplate/posthog
posthog
Installation
$ npx skills add https://github.com/andrehfp/tinyplate --skill posthog
SKILL.md
PostHog Implementation (Next.js 2025)
What This Skill Covers
Analytics - Event tracking, user identification, group analytics
Feature Flags - Boolean flags, multivariate, A/B testing
Session Replay - Recording setup, privacy controls
Analytics Queries - HogQL, Query API, extracting insights
Reporting - Funnel analysis, retention, error reports, SEO
Reference Files

Load these files as needed based on the task:

File	Load When
references/nextjs-implementation.md	Setting up PostHog from scratch, detailed code patterns
references/event-taxonomy.md	Designing event naming conventions, property patterns
references/feature-flags.md	Implementing feature flags, A/B tests, experiments
Quick Setup
Environment Variables
# .env.local
NEXT_PUBLIC_POSTHOG_KEY=phc_your_project_key
NEXT_PUBLIC_POSTHOG_HOST=https://us.i.posthog.com

Reverse Proxy Setup (RECOMMENDED)

IMPORTANT: Ad blockers block direct PostHog requests. Use a reverse proxy to route through your own domain.

Add to next.config.ts:

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: "/ingest/static/:path*",
        destination: "https://us-assets.i.posthog.com/static/:path*",
      },
      {
        source: "/ingest/:path*",
        destination: "https://us.i.posthog.com/:path*",
      },
      {
        source: "/ingest/decide",
        destination: "https://us.i.posthog.com/decide",
      },
    ];
  },
  // ... rest of config
};


Also update CSP headers to allow PostHog connections:

"connect-src 'self' ... https://*.posthog.com https://us.i.posthog.com https://us-assets.i.posthog.com",

PostHog Provider (Client-Side)

Create app/providers.tsx:

'use client'

import posthog from 'posthog-js'
import { PostHogProvider as PHProvider } from 'posthog-js/react'
import { useEffect } from 'react'

export function PostHogProvider({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    posthog.init(process.env.NEXT_PUBLIC_POSTHOG_KEY!, {
      // Use reverse proxy to bypass ad blockers
      api_host: '/ingest',
      ui_host: 'https://us.i.posthog.com',
      defaults: '2025-05-24',
      capture_pageview: false, // We handle manually for accurate funnels
      person_profiles: 'identified_only',
    })
  }, [])

  return <PHProvider client={posthog}>{children}</PHProvider>
}

PostHog Server Client

Create lib/posthog-server.ts:

import { PostHog } from 'posthog-node'

let posthogClient: PostHog | null = null

export function getPostHogServer(): PostHog {
  if (!posthogClient) {
    posthogClient = new PostHog(process.env.NEXT_PUBLIC_POSTHOG_KEY!, {
      host: process.env.NEXT_PUBLIC_POSTHOG_HOST || 'https://us.i.posthog.com',
      flushAt: 1,
      flushInterval: 0,
    })
  }
  return posthogClient
}

Event Naming Convention
Pattern	Example	Use Case
category:object_action	signup:form_submit	User actions
feature:action	dashboard:project_create	Feature usage
lifecycle:event	user:signup_complete	User journey
Property Naming
Pattern	Example	Type
object_adjective	user_id, item_price	Any
is_ prefix	is_subscribed, is_first_time	Boolean
has_ prefix	has_seen_onboarding	Boolean
_count suffix	item_count, generation_count	Number
_at suffix	created_at, upgraded_at	Timestamp
Server vs Client Decision Tree
Where to track?
├── User action in browser → Client (posthog-js)
├── API route / webhook → Server (posthog-node)
├── Server Component render → Server (posthog-node)
├── Need 100% accuracy → Server (no ad blockers)
└── Real-time UI feedback → Client (posthog-js)

Common Pitfalls
Pitfall	Solution
Ad blockers blocking PostHog	Use reverse proxy (/ingest → PostHog). See setup above
Events not appearing	Check ad blockers, verify API key, use reverse proxy
Duplicate pageviews	Use capture_pageview: false and handle manually
Feature flag flicker	Bootstrap flags via middleware
Missing user data	Call identify() BEFORE $pageview for accurate funnels
Inconsistent naming	Use category:object_action pattern
Failed to fetch errors	Browser extension blocking - use reverse proxy
503 from us-assets.i.posthog.com	Ad blocker injecting fake response - use reverse proxy
Clarifying Questions

Before implementing PostHog, ask:

What events are most important to track? (signups, conversions, feature usage)
Do you need server-side tracking? (for accuracy, API routes)
Are you running A/B tests? (need experiment setup)
What's your auth provider? (for user identification pattern)
Do you need session replay? (privacy considerations)
Weekly Installs
27
Repository
andrehfp/tinyplate
GitHub Stars
73
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass