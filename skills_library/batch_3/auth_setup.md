---
title: auth-setup
url: https://skills.sh/get-convex/agent-skills/auth-setup
---

# auth-setup

skills/get-convex/agent-skills/auth-setup
auth-setup
Installation
$ npx skills add https://github.com/get-convex/agent-skills --skill auth-setup
Summary

Convex authentication setup with provider selection, user management, and access control patterns.

Supports multiple auth providers: Convex Auth, Clerk, WorkOS AuthKit, Auth0, and custom JWT, with provider detection from repo signals before setup
Guides identity mapping to a users table, getCurrentUser helpers, and authorization patterns for ownership, admin, and team access checks
Includes provider-specific reference files for package installation, environment variables, client wiring, and convex/auth.config.ts configuration
Covers both local-only and production-ready setup workflows with validation checklists for login state, protected queries, and environment configuration
SKILL.md
Convex Authentication Setup

Implement secure authentication in Convex with user management and access control.

When to Use
Setting up authentication for the first time
Implementing user management (users table, identity mapping)
Creating authentication helper functions
Setting up auth providers (Convex Auth, Clerk, WorkOS AuthKit, Auth0, custom JWT)
First Step: Choose the Auth Provider

Convex supports multiple authentication approaches. Do not assume a provider.

Before writing setup code:

Ask the user which auth solution they want, unless the repository already makes it obvious
If the repo already uses a provider, continue with that provider unless the user wants to switch
If the user has not chosen a provider and the repo does not make it obvious, ask before proceeding

Common options:

Convex Auth - good default when the user wants auth handled directly in Convex
Clerk - use when the app already uses Clerk or the user wants Clerk's hosted auth features
WorkOS AuthKit - use when the app already uses WorkOS or the user wants AuthKit specifically
Auth0 - use when the app already uses Auth0
Custom JWT provider - use when integrating an existing auth system not covered above

Look for signals in the repo before asking:

Dependencies such as @clerk/*, @workos-inc/*, @auth0/*, or Convex Auth packages
Existing files such as convex/auth.config.ts, auth middleware, provider wrappers, or login components
Environment variables that clearly point at a provider
After Choosing a Provider

Read the provider's official guide and the matching local reference file:

Convex Auth: official docs, then references/convex-auth.md
Clerk: official docs, then references/clerk.md
WorkOS AuthKit: official docs, then references/workos-authkit.md
Auth0: official docs, then references/auth0.md

The local reference files contain the concrete workflow, expected files and env vars, gotchas, and validation checks.

Use those sources for:

package installation
client provider wiring
environment variables
convex/auth.config.ts setup
login and logout UI patterns
framework-specific setup for React, Vite, or Next.js

Then read references/common-patterns.md for the Convex-side patterns that apply across providers:

mapping ctx.auth.getUserIdentity() to a users table
getCurrentUser and getCurrentUserOrNull
authorization helpers such as requireAdmin
ownership checks and team membership checks
public, private, and hybrid query patterns

Do not invent provider-specific setup from memory when the docs are available. Do not assume provider initialization commands finish the entire integration. Verify generated files and complete the post-init wiring steps the provider reference calls out.

Workflow
Determine the provider, either by asking the user or inferring from the repo
Ask whether the user wants local-only setup or production-ready setup now
Read the matching provider reference file
Follow the official provider docs for current setup details
Apply the shared Convex patterns from references/common-patterns.md
Wire storeUser or equivalent identity sync only if the app needs a users table
Add authorization checks for ownership, admin access, or team access as needed
Verify login state, protected queries, environment variables, and production configuration if requested

If the flow blocks on interactive provider or deployment setup, ask the user explicitly for the exact human step needed, then continue after they complete it. For UI-facing auth flows, offer to validate the real sign-up or sign-in flow after setup is done. If the environment has browser automation tools, you can use them. If it does not, give the user a short manual validation checklist instead.

Reference Files
Provider References
references/convex-auth.md
references/clerk.md
references/workos-authkit.md
references/auth0.md
Shared Patterns
references/common-patterns.md
Checklist
 Chosen the correct auth provider before writing setup code
 Read the relevant provider reference file
 Asked whether the user wants local-only setup or production-ready setup
 Used the official provider docs for provider-specific wiring
 Users table with tokenIdentifier index
 getCurrentUser helper function
 storeUser mutation for first sign-in
 Authentication check in all protected functions
 Authorization check for resource access
 Clear error messages ("Not authenticated", "Unauthorized")
 Client auth provider configured for the chosen provider
 If requested, production auth setup is covered too
Weekly Installs
513
Repository
get-convex/agent-skills
GitHub Stars
25
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass