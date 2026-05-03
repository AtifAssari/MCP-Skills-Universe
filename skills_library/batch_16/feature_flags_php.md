---
title: feature-flags-php
url: https://skills.sh/posthog/skills/feature-flags-php
---

# feature-flags-php

skills/posthog/skills/feature-flags-php
feature-flags-php
Installation
$ npx skills add https://github.com/posthog/skills --skill feature-flags-php
SKILL.md
PostHog feature flags for PHP

This skill helps you add PostHog feature flags to PHP applications.

Reference files
references/php.md - Php feature flags installation - docs
references/adding-feature-flag-code.md - Adding feature flag code - docs
references/best-practices.md - Feature flag best practices - docs

Consult the documentation for API details and framework-specific patterns.

Key principles
Environment variables: Always use environment variables for PostHog keys. Never hardcode them.
Minimal changes: Add feature flag code alongside existing logic. Don't replace or restructure existing code.
Boolean flags first: Default to boolean flag checks unless the user specifically asks for multivariate flags.
Server-side when possible: Prefer server-side flag evaluation to avoid UI flicker.
PostHog MCP tools

Check if a PostHog MCP server is connected. If available, look for tools related to feature flag management (creating, listing, updating, deleting flags). Use these tools to manage flags directly in PostHog rather than requiring the user to do it manually in the dashboard.

Framework guidelines
Remember that source code is available in the vendor directory after composer install
posthog/posthog-php is the PHP SDK package name
Check composer.json for existing dependencies and autoload configuration before adding new files
The PHP SDK uses static methods (PostHog::capture, PostHog::identify) - initialize once with PostHog::init()
PHP SDK methods take associative arrays with 'distinctId', 'event', 'properties' keys - not positional arguments
Weekly Installs
45
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