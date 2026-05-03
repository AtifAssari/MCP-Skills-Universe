---
rating: ⭐⭐
title: groq-upgrade-migration
url: https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/groq-upgrade-migration
---

# groq-upgrade-migration

skills/jeremylongshore/claude-code-plugins-plus-skills/groq-upgrade-migration
groq-upgrade-migration
Installation
$ npx skills add https://github.com/jeremylongshore/claude-code-plugins-plus-skills --skill groq-upgrade-migration
SKILL.md
Groq Upgrade & Migration
Overview

Guide for upgrading Groq SDK versions and handling breaking changes.

Prerequisites
Current Groq SDK installed
Git for version control
Test suite available
Staging environment
Instructions
Step 1: Check Current Version
set -euo pipefail
npm list @groq/sdk
npm view @groq/sdk version

Step 2: Review Changelog
open https://github.com/groq/sdk/releases

Step 3: Create Upgrade Branch
set -euo pipefail
git checkout -b upgrade/groq-sdk-vX.Y.Z
npm install @groq/sdk@latest
npm test

Step 4: Handle Breaking Changes

Update import statements, configuration, and method signatures as needed.

Output
Updated SDK version
Fixed breaking changes
Passing test suite
Documented rollback procedure
Error Handling
SDK Version	API Version	Node.js	Breaking Changes
3.x	2024-01	18+	Major refactor
2.x	2023-06	16+	Auth changes
1.x	2022-01	14+	Initial release
Examples
Import Changes
// Before (v1.x)
import { Client } from '@groq/sdk';

// After (v2.x)
import { GroqClient } from '@groq/sdk';

Configuration Changes
// Before (v1.x)
const client = new Client({ key: 'xxx' });

// After (v2.x)
const client = new GroqClient({
  apiKey: 'xxx',
});

Rollback Procedure
set -euo pipefail
npm install @groq/sdk@1.x.x --save-exact

Deprecation Handling
// Monitor for deprecation warnings in development
if (process.env.NODE_ENV === 'development') {
  process.on('warning', (warning) => {
    if (warning.name === 'DeprecationWarning') {
      console.warn('[Groq]', warning.message);
      // Log to tracking system for proactive updates
    }
  });
}

// Common deprecation patterns to watch for:
// - Renamed methods: client.oldMethod() -> client.newMethod()
// - Changed parameters: { key: 'x' } -> { apiKey: 'x' }
// - Removed features: Check release notes before upgrading

Resources
Groq Changelog
Groq Migration Guide
Next Steps

For CI integration during upgrades, see groq-ci-integration.

Weekly Installs
24
Repository
jeremylongshore…s-skills
GitHub Stars
2.1K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn