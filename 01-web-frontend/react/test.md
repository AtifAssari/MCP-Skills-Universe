---
rating: ⭐⭐
title: test
url: https://skills.sh/facebook/react/test
---

# test

skills/facebook/react/test
test
Installation
$ npx skills add https://github.com/facebook/react --skill test
Summary

Run tests for React codebase across multiple release channels and configurations.

Supports six release channels: source (default), experimental, www, www with variant false, stable, and classic, each with distinct feature flag configurations
Accepts test patterns, watch mode for TDD, and variant flags to test different code paths
Requires explicit test pattern argument to avoid running the entire test suite; uses --silent flag to surface failures and --no-watchman for sandboxing compatibility
Common workflow: test the same pattern across www and www variant false to verify __VARIANT__ flag behavior; check @gate pragmas in feature-flags skill if tests skip unexpectedly
SKILL.md

Run tests for the React codebase.

Arguments:

$ARGUMENTS: Channel, flags, and test pattern

Usage Examples:

/test ReactFiberHooks - Run with source channel (default)
/test experimental ReactFiberHooks - Run with experimental channel
/test www ReactFiberHooks - Run with www-modern channel
/test www variant false ReactFiberHooks - Test VARIANT=false
/test stable ReactFiberHooks - Run with stable channel
/test classic ReactFiberHooks - Run with www-classic channel
/test watch ReactFiberHooks - Run in watch mode (TDD)

Release Channels:

(default) - Source/canary channel, uses ReactFeatureFlags.js defaults
experimental - Source/experimental channel with EXPERIMENTAL flags = true
www - www-modern channel with VARIANT flags = true
www variant false - www channel with VARIANT flags = false
stable - What ships to npm
classic - Legacy www-classic (rarely needed)

Instructions:

Parse channel from arguments (default: source)
Map to yarn command:
(default) → yarn test --silent --no-watchman <pattern>
experimental → yarn test -r=experimental --silent --no-watchman <pattern>
stable → yarn test-stable --silent --no-watchman <pattern>
classic → yarn test-classic --silent --no-watchman <pattern>
www → yarn test-www --silent --no-watchman <pattern>
www variant false → yarn test-www --variant=false --silent --no-watchman <pattern>
Report test results and any failures

Hard Rules:

Use --silent to see failures - This limits the test output to only failures.
Use --no-watchman - This is a common failure in sandboxing.

Common Mistakes:

Running without a pattern - Runs ALL tests, very slow. Always specify a pattern.
Forgetting both www variants - Test www AND www variant false for __VARIANT__ flags.
Test skipped unexpectedly - Check for @gate pragma; see feature-flags skill.
Weekly Installs
860
Repository
facebook/react
GitHub Stars
244.8K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass