---
title: nuxt-better-auth
url: https://skills.sh/onmax/nuxt-skills/nuxt-better-auth
---

# nuxt-better-auth

skills/onmax/nuxt-skills/nuxt-better-auth
nuxt-better-auth
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill nuxt-better-auth
Summary

Authentication for Nuxt 4+ with composables, server helpers, and route protection.

Provides useUserSession() composable for client-side auth flows (login, signup, signout) and requireUserSession() server helper for API route protection
Supports route protection via routeRules and definePageMeta with role-based access control
Integrates Better Auth plugins including admin, passkey, and 2FA capabilities
Includes NuxtHub database setup with Drizzle schema and clientOnly mode for external auth backends
Currently in alpha (v0.0.2-alpha.19) and not recommended for production use
SKILL.md
Nuxt Better Auth

Authentication module for Nuxt 4+ built on Better Auth. Provides composables, server utilities, and route protection.

Alpha Status: This module is currently in alpha (v0.0.2-alpha.19) and not recommended for production use. APIs may change.

When to Use
Installing/configuring @onmax/nuxt-better-auth
Implementing login/signup/signout flows
Protecting routes (client and server)
Accessing user session in API routes
Integrating Better Auth plugins (admin, passkey, 2FA)
Setting up database with NuxtHub
Using clientOnly mode for external auth backends
Adding i18n support with @nuxtjs/i18n

For Nuxt patterns: use nuxt skill For NuxtHub database: use nuxthub skill

Available Guidance
File	Topics
references/installation.md	Module setup, env vars, config files
references/client-auth.md	useUserSession, signIn/signUp/signOut, BetterAuthState, safe redirects
references/server-auth.md	serverAuth, getUserSession, requireUserSession
references/route-protection.md	routeRules, definePageMeta, middleware
references/plugins.md	Better Auth plugins (admin, passkey, 2FA)
references/database.md	NuxtHub integration, Drizzle schema, custom tables with FKs
references/client-only.md	External auth backend, clientOnly mode, CORS
references/types.md	AuthUser, AuthSession, type augmentation
Loading Files

Consider loading these reference files based on your task:

 references/installation.md - if installing or configuring the module
 references/client-auth.md - if building login/signup/signout flows
 references/server-auth.md - if protecting API routes or accessing user session server-side
 references/route-protection.md - if using routeRules or definePageMeta for auth
 references/plugins.md - if integrating Better Auth plugins (admin, passkey, 2FA)
 references/database.md - if setting up database with NuxtHub or Drizzle
 references/client-only.md - if using external auth backend with clientOnly mode
 references/types.md - if working with AuthUser, AuthSession, or type augmentation

DO NOT load all files at once. Load only what's relevant to your current task.

Key Concepts
Concept	Description
useUserSession()	Client composable - user, session, loggedIn, signIn/Out methods
requireUserSession()	Server helper - throws 401/403 if not authenticated
auth route mode	'user', 'guest', { user: {...} }, or false
serverAuth()	Get Better Auth instance in server routes
Quick Reference
// Client: useUserSession()
const { user, loggedIn, signIn, signOut } = useUserSession()
await signIn.email({ email, password }, { onSuccess: () => navigateTo('/') })

// Server: requireUserSession()
const { user } = await requireUserSession(event, { user: { role: 'admin' } })

// nuxt.config.ts: Route protection
routeRules: {
  '/admin/**': { auth: { user: { role: 'admin' } } },
  '/login': { auth: 'guest' },
  '/app/**': { auth: 'user' }
}

Resources
Module Docs
Better Auth Docs

Token efficiency: Main skill ~300 tokens, each sub-file ~800-1200 tokens

Weekly Installs
1.2K
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass