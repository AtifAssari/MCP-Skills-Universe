---
rating: ⭐⭐⭐
title: react18-legacy-context
url: https://skills.sh/github/awesome-copilot/react18-legacy-context
---

# react18-legacy-context

skills/github/awesome-copilot/react18-legacy-context
react18-legacy-context
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill react18-legacy-context
SKILL.md
React 18 Legacy Context Migration

Legacy context (contextTypes, childContextTypes, getChildContext) was deprecated in React 16.3 and warns in React 18.3.1. It is removed in React 19.

This Is Always a Cross-File Migration

Unlike most other migrations that touch one file at a time, context migration requires coordinating:

Create the context object (usually a new file)
Update the provider component
Update every consumer component

Missing any consumer leaves the app broken - it will read from the wrong context or get undefined.

Migration Steps (Always Follow This Order)
Step 1: Find the provider (childContextTypes + getChildContext)
Step 2: Find ALL consumers (contextTypes)
Step 3: Create the context file
Step 4: Update the provider
Step 5: Update each consumer (class components → contextType, function components → useContext)
Step 6: Verify - run the app, check no legacy context warnings remain

Scan Commands
# Find all providers
grep -rn "childContextTypes\|getChildContext" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\."

# Find all consumers
grep -rn "contextTypes\s*=" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\."

# Find this.context usage (may be legacy or modern - check which)
grep -rn "this\.context\." src/ --include="*.js" --include="*.jsx" | grep -v "\.test\."

Reference Files
references/single-context.md - complete migration for one context (theme, auth, etc.) with provider + class consumer + function consumer
references/multi-context.md - apps with multiple legacy contexts (nested providers, multiple consumers of different contexts)
references/context-file-template.md - the standard file structure for a new context module
Weekly Installs
521
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass