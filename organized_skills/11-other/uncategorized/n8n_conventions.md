---
rating: ⭐⭐⭐
title: n8n-conventions
url: https://skills.sh/n8n-io/n8n/n8n-conventions
---

# n8n-conventions

skills/n8n-io/n8n/n8n-conventions
n8n-conventions
Installation
$ npx skills add https://github.com/n8n-io/n8n --skill n8n-conventions
SKILL.md
n8n Quick Reference

📚 Full Documentation:

General: /AGENTS.md - Architecture, commands, workflows
Frontend: /packages/frontend/AGENTS.md - CSS variables, timing

Use this skill when you need quick reminders on critical patterns.

Critical Rules (Must Follow)

TypeScript:

Never any → use unknown
Prefer satisfies over as (except tests)
Shared types in @n8n/api-types

Error Handling:

import { UnexpectedError } from 'n8n-workflow';
throw new UnexpectedError('message', { extra: { context } });
// DON'T use deprecated ApplicationError


Frontend:

Vue 3 Composition API (<script setup lang="ts">)
CSS variables (never hardcode px) - see /packages/frontend/AGENTS.md
All text via i18n ($t('key'))
data-testid for E2E (single value, no spaces)

Backend:

Controller → Service → Repository
Dependency injection via @n8n/di
Config via @n8n/config
Zod schemas for validation

Testing:

Vitest (unit), Playwright (E2E)
Mock external dependencies
Work from package directory: pushd packages/cli && pnpm test

Database:

SQLite/PostgreSQL only (app DB)
Exception: DB nodes (MySQL Node, etc.) can use DB-specific features

Commands:

pnpm build > build.log 2>&1  # Always redirect
pnpm typecheck               # Before commit
pnpm lint                    # Before commit

Key Packages
Package	Purpose
packages/cli	Backend API
packages/frontend/editor-ui	Vue 3 frontend
packages/@n8n/api-types	Shared types
packages/@n8n/db	TypeORM entities
packages/workflow	Core interfaces
Common Patterns

Pinia Store:

import { STORES } from '@n8n/stores';
export const useMyStore = defineStore(STORES.MY_STORE, () => {
  const state = shallowRef([]);
  return { state };
});


Vue Component:

<script setup lang="ts">
type Props = { title: string };
const props = defineProps<Props>();
</script>


Service:

import { Service } from '@n8n/di';
import { Config } from '@n8n/config';

@Service()
export class MyService {
  constructor(private readonly config: Config) {}
}


📖 Need more details? Read /AGENTS.md and /packages/frontend/AGENTS.md

Weekly Installs
434
Repository
n8n-io/n8n
GitHub Stars
186.4K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass