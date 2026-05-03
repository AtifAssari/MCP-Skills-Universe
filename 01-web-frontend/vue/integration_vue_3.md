---
rating: ⭐⭐
title: integration-vue-3
url: https://skills.sh/posthog/skills/integration-vue-3
---

# integration-vue-3

skills/posthog/skills/integration-vue-3
integration-vue-3
Installation
$ npx skills add https://github.com/posthog/skills --skill integration-vue-3
SKILL.md
PostHog integration for Vue 3

This skill helps you add PostHog analytics to Vue 3 applications.

Workflow

Follow these steps in order to complete the integration:

basic-integration-1.0-begin.md - PostHog Setup - Begin ← Start here
basic-integration-1.1-edit.md - PostHog Setup - Edit
basic-integration-1.2-revise.md - PostHog Setup - Revise
basic-integration-1.3-conclude.md - PostHog Setup - Conclusion
Reference files
references/EXAMPLE.md - Vue 3 example project code
references/vue-js.md - Vue.js - docs
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

No specific framework guidelines.

Identifying users

Identify users during login and signup events. Refer to the example code and documentation for the correct identify pattern for this framework. If both frontend and backend code exist, pass the client-side session and distinct ID using X-POSTHOG-DISTINCT-ID and X-POSTHOG-SESSION-ID headers to maintain correlation.

Error tracking

Add PostHog error tracking to relevant files, particularly around critical user flows and API boundaries.

Weekly Installs
46
Repository
posthog/skills
GitHub Stars
31
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass