---
title: 1k-sentry
url: https://skills.sh/onekeyhq/app-monorepo/1k-sentry
---

# 1k-sentry

skills/onekeyhq/app-monorepo/1k-sentry
1k-sentry
Installation
$ npx skills add https://github.com/onekeyhq/app-monorepo --skill 1k-sentry
SKILL.md
Sentry Integration

OneKey uses Sentry for error tracking across all platforms.

Architecture Overview
apps/
├── desktop/app/sentry.ts          # Desktop main process
├── ext/                           # Extension (uses shared)
├── mobile/                        # Mobile (uses shared)
└── web/                           # Web (uses shared)

packages/shared/src/modules3rdParty/sentry/
├── index.ts                       # Web/Extension entry
├── index.native.ts                # React Native entry
├── index.desktop.ts               # Desktop renderer entry
├── basicOptions.ts                # Shared config & error filtering
└── instance.ts                    # Sentry client instance

Platform Detection
import platformEnv from '@onekeyhq/shared/src/platformEnv';

platformEnv.isDesktop    // Electron desktop app
platformEnv.isNative     // React Native (iOS/Android)
platformEnv.isWeb        // Web browser
platformEnv.isExtension  // Browser extension
platformEnv.isWebEmbed   // Embedded web components

Common Tasks
Filter/Ignore Errors

See: references/rules/ignoring-errors.md

Key file: packages/shared/src/modules3rdParty/sentry/basicOptions.ts

Analyze Crash Reports
Get crash details from Sentry dashboard
Identify error type, message, and stack trace
Check platform-specific context
Use related skills for fixes:
Native crashes → /1k-patching-native-modules
JS errors → Fix in codebase
Add Custom Context
import * as Sentry from '@sentry/react-native'; // or @sentry/browser

// Add breadcrumb
Sentry.addBreadcrumb({
  category: 'action',
  message: 'User clicked button',
  level: 'info',
});

// Set user context
Sentry.setUser({ id: 'user-id' });

// Set tags
Sentry.setTag('feature', 'swap');

// Capture exception with context
Sentry.captureException(error, {
  extra: { additionalData: 'value' },
});

Key Files
Purpose	File
Error filtering	packages/shared/src/modules3rdParty/sentry/basicOptions.ts
Desktop main	apps/desktop/app/sentry.ts
Desktop renderer	packages/shared/src/modules3rdParty/sentry/index.desktop.ts
Web/Extension	packages/shared/src/modules3rdParty/sentry/index.ts
Native	packages/shared/src/modules3rdParty/sentry/index.native.ts
Error Filtering Quick Reference
// Filter by error type
const FILTERED_ERROR_TYPES = new Set(['AxiosError', 'HTTPClientError']);

// Filter by exact message
const FILTER_ERROR_VALUES = ['AbortError: AbortError'];

// Filter by pattern (in isFilterErrorAndSkipSentry function)
if (error.value?.includes('PATTERN')) return true;

Related Skills
/1k-patching-native-modules - Fix native crashes found in Sentry
/1k-coding-patterns - Error handling best practices
Weekly Installs
53
Repository
onekeyhq/app-monorepo
GitHub Stars
2.4K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn