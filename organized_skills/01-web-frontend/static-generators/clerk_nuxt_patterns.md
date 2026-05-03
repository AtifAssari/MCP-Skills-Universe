---
rating: ⭐⭐
title: clerk-nuxt-patterns
url: https://skills.sh/clerk/skills/clerk-nuxt-patterns
---

# clerk-nuxt-patterns

skills/clerk/skills/clerk-nuxt-patterns
clerk-nuxt-patterns
Installation
$ npx skills add https://github.com/clerk/skills --skill clerk-nuxt-patterns
SKILL.md
Nuxt Patterns
What Do You Need?
Task	Reference
Protect routes with middleware	references/nuxt-middleware.md
Auth in server API routes (Nitro)	references/server-api-routes.md
useAuth / useUser in components	references/composables.md
SSR-safe auth patterns	references/ssr-auth.md
References
Reference	Description
references/nuxt-middleware.md	Route protection, clerkMiddleware()
references/server-api-routes.md	Nitro server route auth
references/composables.md	useAuth, useUser, useClerk
references/ssr-auth.md	SSR hydration, server vs client
Setup
npm install @clerk/nuxt


.env:

NUXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_...
NUXT_CLERK_SECRET_KEY=sk_...


nuxt.config.ts:

export default defineNuxtConfig({
  modules: ['@clerk/nuxt'],
})


This single line auto-configures middleware, plugins, and component auto-imports.

Mental Model

@clerk/nuxt auto-imports all Clerk components and composables — no explicit imports needed in <script setup>.

Composables (useAuth, useUser) — client-side reactive, inside <script setup>
Server routes (clerkClient) — Nitro server routes, event.context.auth
Middleware (clerkMiddleware) — auto-registered, use auth().protect() to lock routes
Minimal Pattern
<!-- pages/dashboard.vue -->
<script setup lang="ts">
definePageMeta({ middleware: 'auth' })
const { userId } = useAuth()
</script>

<template>
  <Show when="signed-in">
    <p>Hello {{ userId }}</p>
  </Show>
</template>


definePageMeta({ middleware: 'auth' }) uses the built-in auth middleware from @clerk/nuxt.

Common Pitfalls
Symptom	Cause	Fix
Composables return undefined on server	useAuth is client-only	Use event.context.auth in server routes
Route not protected	Missing middleware: 'auth' meta	Add definePageMeta({ middleware: 'auth' })
clerkClient not available	Wrong import path	Import from @clerk/nuxt/server
Hydration mismatch	Rendering auth state before mounted	Wrap in <ClientOnly> or check isLoaded
Env vars not picked up	Wrong prefix	Nuxt requires NUXT_PUBLIC_ for public, NUXT_ for server
Org-Aware Pattern
<script setup lang="ts">
const { orgId, orgRole } = useAuth()
</script>

<template>
  <div v-if="orgId">
    <p>Org: {{ orgId }}</p>
    <p v-if="orgRole === 'org:admin'">Admin panel</p>
  </div>
  <div v-else>
    <OrganizationSwitcher />
  </div>
</template>

See Also
clerk-setup - Initial Clerk install
clerk-custom-ui - Custom flows & appearance
clerk-orgs - B2B organizations
Docs

Nuxt SDK

Weekly Installs
848
Repository
clerk/skills
GitHub Stars
40
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass