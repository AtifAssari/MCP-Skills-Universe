---
rating: ⭐⭐
title: 1k-coding-patterns
url: https://skills.sh/onekeyhq/app-monorepo/1k-coding-patterns
---

# 1k-coding-patterns

skills/onekeyhq/app-monorepo/1k-coding-patterns
1k-coding-patterns
Installation
$ npx skills add https://github.com/onekeyhq/app-monorepo --skill 1k-coding-patterns
SKILL.md
OneKey Coding Patterns and Best Practices
Quick Reference
Topic	Guide	Key Points
Promise handling	promise-handling.md	Always await or use void, never floating promises
React components	react-components.md	Named imports, functional components, no FC type
Restricted patterns	restricted-patterns.md	Forbidden: toLocaleLowerCase, direct hd-core import
Critical Rules Summary
Promise Handling
// ❌ FORBIDDEN - floating promise
apiCall();

// ✅ CORRECT
await apiCall();
// or
void apiCall(); // intentionally not awaited

React Components
// ❌ FORBIDDEN
import React, { FC } from 'react';
const MyComponent: FC<Props> = () => {};

// ✅ CORRECT
import { useState, useCallback } from 'react';
function MyComponent({ prop }: { prop: string }) {}

Restricted Patterns
// ❌ FORBIDDEN
string.toLocaleLowerCase()
import { x } from '@onekeyfe/hd-core';
import { localDbInstance } from '...';

// ✅ CORRECT
string.toLowerCase()
const { x } = await CoreSDKLoader();
import { localDb } from '...';

Related Skills
/1k-date-formatting - Date and time formatting
/1k-i18n - Internationalization and translations
/1k-error-handling - Error handling patterns
/1k-cross-platform - Platform-specific code
/1k-code-quality - Linting and code quality
/1k-performance - Performance optimization
/1k-state-management - Jotai atom patterns
/1k-architecture - Project structure and import rules
/1k-code-quality - Lint fixes, pre-commit tasks
Weekly Installs
69
Repository
onekeyhq/app-monorepo
GitHub Stars
2.4K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass