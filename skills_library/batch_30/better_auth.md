---
title: better-auth
url: https://skills.sh/the1studio/theone-training-skills/better-auth
---

# better-auth

skills/the1studio/theone-training-skills/better-auth
better-auth
Installation
$ npx skills add https://github.com/the1studio/theone-training-skills --skill better-auth
SKILL.md
Better Auth Skill

Better Auth is comprehensive, framework-agnostic authentication/authorization framework for TypeScript with built-in email/password, social OAuth, and powerful plugin ecosystem for advanced features.

When to Use
Implementing auth in TypeScript/JavaScript applications
Adding email/password or social OAuth authentication
Setting up 2FA, passkeys, magic links, advanced auth features
Building multi-tenant apps with organization support
Managing sessions and user lifecycle
Working with any framework (Next.js, Nuxt, SvelteKit, Remix, Astro, Hono, Express, etc.)
Quick Start
Installation
npm install better-auth
# or pnpm/yarn/bun add better-auth

Environment Setup

Create .env:

BETTER_AUTH_SECRET=<generated-secret-32-chars-min>
BETTER_AUTH_URL=http://localhost:3000

Basic Server Setup

Create auth.ts (root, lib/, utils/, or under src/app/server/):

import { betterAuth } from "better-auth";

export const auth = betterAuth({
  database: {
    // See references/database-integration.md
  },
  emailAndPassword: {
    enabled: true,
    autoSignIn: true
  },
  socialProviders: {
    github: {
      clientId: process.env.GITHUB_CLIENT_ID!,
      clientSecret: process.env.GITHUB_CLIENT_SECRET!,
    }
  }
});

Database Schema
npx @better-auth/cli generate  # Generate schema/migrations
npx @better-auth/cli migrate   # Apply migrations (Kysely only)

Mount API Handler

Next.js App Router:

// app/api/auth/[...all]/route.ts
import { auth } from "@/lib/auth";
import { toNextJsHandler } from "better-auth/next-js";

export const { POST, GET } = toNextJsHandler(auth);


Other frameworks: See references/email-password-auth.md#framework-setup

Client Setup

Create auth-client.ts:

import { createAuthClient } from "better-auth/client";

export const authClient = createAuthClient({
  baseURL: process.env.NEXT_PUBLIC_BETTER_AUTH_URL || "http://localhost:3000"
});

Basic Usage
// Sign up
await authClient.signUp.email({
  email: "user@example.com",
  password: "secure123",
  name: "John Doe"
});

// Sign in
await authClient.signIn.email({
  email: "user@example.com",
  password: "secure123"
});

// OAuth
await authClient.signIn.social({ provider: "github" });

// Session
const { data: session } = authClient.useSession(); // React/Vue/Svelte
const { data: session } = await authClient.getSession(); // Vanilla JS

Feature Selection Matrix
Feature	Plugin Required	Use Case	Reference
Email/Password	No (built-in)	Basic auth	email-password-auth.md
OAuth (GitHub, Google, etc.)	No (built-in)	Social login	oauth-providers.md
Email Verification	No (built-in)	Verify email addresses	email-password-auth.md
Password Reset	No (built-in)	Forgot password flow	email-password-auth.md
Two-Factor Auth (2FA/TOTP)	Yes (twoFactor)	Enhanced security	advanced-features.md
Passkeys/WebAuthn	Yes (passkey)	Passwordless auth	advanced-features.md
Magic Link	Yes (magicLink)	Email-based login	advanced-features.md
Username Auth	Yes (username)	Username login	email-password-auth.md
Organizations/Multi-tenant	Yes (organization)	Team/org features	advanced-features.md
Rate Limiting	No (built-in)	Prevent abuse	advanced-features.md
Session Management	No (built-in)	User sessions	advanced-features.md
Auth Method Selection Guide

Choose Email/Password when:

Building standard web app with traditional auth
Need full control over user credentials
Targeting users who prefer email-based accounts

Choose OAuth when:

Want quick signup with minimal friction
Users already have social accounts
Need access to social profile data

Choose Passkeys when:

Want passwordless experience
Targeting modern browsers/devices
Security is top priority

Choose Magic Link when:

Want passwordless without WebAuthn complexity
Targeting email-first users
Need temporary access links

Combine Multiple Methods when:

Want flexibility for different user preferences
Building enterprise apps with various auth requirements
Need progressive enhancement (start simple, add more options)
Core Architecture

Better Auth uses client-server architecture:

Server (better-auth): Handles auth logic, database ops, API routes
Client (better-auth/client): Provides hooks/methods for frontend
Plugins: Extend both server/client functionality
Implementation Checklist
 Install better-auth package
 Set environment variables (SECRET, URL)
 Create auth server instance with database config
 Run schema migration (npx @better-auth/cli generate)
 Mount API handler in framework
 Create client instance
 Implement sign-up/sign-in UI
 Add session management to components
 Set up protected routes/middleware
 Add plugins as needed (regenerate schema after)
 Test complete auth flow
 Configure email sending (verification/reset)
 Enable rate limiting for production
 Set up error handling
Reference Documentation
Core Authentication
Email/Password Authentication - Email/password setup, verification, password reset, username auth
OAuth Providers - Social login setup, provider configuration, token management
Database Integration - Database adapters, schema setup, migrations
Advanced Features
Advanced Features - 2FA/MFA, passkeys, magic links, organizations, rate limiting, session management
Scripts
scripts/better_auth_init.py - Initialize Better Auth configuration with interactive setup
Resources
Docs: https://www.better-auth.com/docs
GitHub: https://github.com/better-auth/better-auth
Plugins: https://www.better-auth.com/docs/plugins
Examples: https://www.better-auth.com/docs/examples
Weekly Installs
13
Repository
the1studio/theo…g-skills
GitHub Stars
71
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass