---
rating: ⭐⭐
title: flow
url: https://skills.sh/facebook/react/flow
---

# flow

skills/facebook/react/flow
flow
Installation
$ npx skills add https://github.com/facebook/react --skill flow
Summary

Static type checking for React code across DOM and native platforms.

Four renderer options cover standard DOM, browser-specific code, React Native, and Fabric environments
Run yarn flow with optional renderer argument; use yarn flow-ci for comprehensive but slower checks
Reports type errors with file locations to help identify and fix issues quickly
Watch for common pitfalls: missing renderer specification, unexamined $FlowFixMe suppressions, and incorrect type imports
SKILL.md
Flow Type Checking

Arguments:

$ARGUMENTS: Renderer to check (default: dom-node)
Renderers
Renderer	When to Use
dom-node	Default, recommended for most changes
dom-browser	Browser-specific DOM code
native	React Native
fabric	React Native Fabric
Instructions
Run yarn flow $ARGUMENTS (use dom-node if no argument)
Report type errors with file locations
For comprehensive checking (slow), use yarn flow-ci
Common Mistakes
Running without a renderer - Always specify or use default dom-node
Ignoring suppressions - Check if $FlowFixMe comments are masking real issues
Missing type imports - Ensure types are imported from the correct package
Weekly Installs
806
Repository
facebook/react
GitHub Stars
244.8K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass