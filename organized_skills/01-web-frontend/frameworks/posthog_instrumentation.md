---
rating: ⭐⭐⭐
title: posthog-instrumentation
url: https://skills.sh/posthog/posthog-for-claude/posthog-instrumentation
---

# posthog-instrumentation

skills/posthog/posthog-for-claude/posthog-instrumentation
posthog-instrumentation
Installation
$ npx skills add https://github.com/posthog/posthog-for-claude --skill posthog-instrumentation
Summary

Automatically instrument PostHog analytics, event tracking, and feature flags across multiple frameworks.

Supports JavaScript/TypeScript, React, Python, and Node.js with framework-specific setup patterns
Covers three core capabilities: event capture with custom properties, feature flag evaluation for gradual rollouts, and user identification
Detects existing PostHog configuration and adds instrumentation without duplicating setup
Includes best practices for event naming conventions, property inclusion, and session-based user identification
SKILL.md
PostHog Instrumentation Skill

Help users add PostHog analytics, event tracking, and feature flags to their code.

When to Use
User asks to "add PostHog" or "add analytics"
User wants to track events or user actions
User needs to implement feature flags
User asks about instrumenting their code
Workflow
Identify the framework (React, Next.js, Python, Node.js, etc.)
Check for existing PostHog setup
Add appropriate instrumentation
Code Patterns
JavaScript/TypeScript
// Event tracking
posthog.capture('button_clicked', { button_name: 'signup' })

// Feature flags
if (posthog.isFeatureEnabled('new-feature')) {
  // Show new feature
}

// User identification
posthog.identify(userId, { email: user.email })

Python
from posthog import Posthog
posthog = Posthog(api_key='<ph_project_api_key>')

# Event tracking
posthog.capture(distinct_id='user_123', event='purchase_completed')

# Feature flags
if posthog.feature_enabled('new-feature', 'user_123'):
    # Show new feature

React
import { usePostHog } from 'posthog-js/react'

function MyComponent() {
  const posthog = usePostHog()

  const handleClick = () => {
    posthog.capture('button_clicked')
  }
}

Best Practices
Use consistent event naming (snake_case recommended)
Include relevant properties with events
Identify users early in their session
Use feature flags for gradual rollouts
Weekly Installs
808
Repository
posthog/posthog…r-claude
GitHub Stars
13
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail