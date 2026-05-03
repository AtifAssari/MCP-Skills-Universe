---
rating: ⭐⭐
title: integration-astro-hybrid
url: https://skills.sh/posthog/skills/integration-astro-hybrid
---

# integration-astro-hybrid

skills/posthog/skills/integration-astro-hybrid
integration-astro-hybrid
Installation
$ npx skills add https://github.com/posthog/skills --skill integration-astro-hybrid
SKILL.md
PostHog integration for Astro (Hybrid)

This skill helps you add PostHog analytics to Astro (Hybrid) applications.

Workflow

Follow these steps in order to complete the integration:

basic-integration-1.0-begin.md - PostHog Setup - Begin ← Start here
basic-integration-1.1-edit.md - PostHog Setup - Edit
basic-integration-1.2-revise.md - PostHog Setup - Revise
basic-integration-1.3-conclude.md - PostHog Setup - Conclusion
Reference files
references/EXAMPLE.md - Astro (Hybrid) example project code
references/astro.md - Astro - docs
references/identify-users.md - Identify users - docs
references/basic-integration-1.0-begin.md - PostHog setup - begin
references/basic-integration-1.1-edit.md - PostHog setup - edit
references/basic-integration-1.2-revise.md - PostHog setup - revise
references/basic-integration-1.3-conclude.md - PostHog setup - conclusion

The example project shows the target implementation pattern. Consult the documentation for API details.

Key principles
Environment variables: Always use environment variables for PostHog keys. Never hardcode them.
Minimal changes: Add PostHog code alongside existing integrations. Don't replace or restructure existing code.
Match the example: Your implementation should follow the example project's patterns as closely as possible.
Framework guidelines
Always use the is:inline directive on PostHog script tags to prevent Astro from processing them and causing TypeScript errors
Use PUBLIC_ prefix for client-side environment variables in Astro (e.g., PUBLIC_POSTHOG_PROJECT_TOKEN)
Create a posthog.astro component in src/components/ for reusable initialization across pages
Import the PostHog component in a Layout and wrap all pages with that layout
Use posthog-node in API routes under src/pages/api/ for server-side event tracking
Store the posthog-node client instance in a singleton pattern (src/lib/posthog-server.ts) to avoid creating multiple clients
In Astro 5, use output static (the default) with an adapter - pages are prerendered by default
Use export const prerender = false to opt specific pages into SSR when they need server-side rendering
Only pages that need server-side PostHog tracking (like API-backed forms) should opt out of prerendering
Identifying users

Identify users during login and signup events. Refer to the example code and documentation for the correct identify pattern for this framework. If both frontend and backend code exist, pass the client-side session and distinct ID using X-POSTHOG-DISTINCT-ID and X-POSTHOG-SESSION-ID headers to maintain correlation.

Error tracking

Add PostHog error tracking to relevant files, particularly around critical user flows and API boundaries.

Weekly Installs
47
Repository
posthog/skills
GitHub Stars
31
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn