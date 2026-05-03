---
rating: ⭐⭐
title: architect-nextjs
url: https://skills.sh/ivantsxx/my-next-skills/architect-nextjs
---

# architect-nextjs

skills/ivantsxx/my-next-skills/architect-nextjs
architect-nextjs
Installation
$ npx skills add https://github.com/ivantsxx/my-next-skills --skill architect-nextjs
SKILL.md
Scope Rule Architect (Next.js 15+)

This skill establishes the architectural foundation for scalable Next.js applications by enforcing strict Scope Rules and Screaming Architecture.

Core Principles
1. The Scope Rule (Absolute Law)

"Scope determines structure."

Local Scope: Code used by 1 feature → MUST stay local (e.g., (user)/profile/_components).
Shared Scope: Code used by 2+ features → MUST go to src/shared/.
No Exceptions: Do not pollute shared with single-use components.
2. Screaming Architecture

Directory structures must immediately declare what the application does.

Use Route Groups (feature) for top-level modules.
Avoid generic folders like containers or views at the top level.
3. Next.js 15 Standards
App Router Only: No pages/ directory.
Server-First: Components are Server Components by default.
Data Access: Fetch directly in Server Components or via Server Actions.
Decision Framework

When placing files, follow this decision tree:

Count Usage:

Used by 1 Feature: Place in app/(feature)/_components/.
Used by 2+ Features: Place in src/shared/components/.

Determine Type:

Server Component: Default. Used for static content and initial data fetching.
Client Component: Use ONLY for useState, useEffect, or event listeners.
Server Action: Use for mutations and form handling. Place in _actions/name.ts.
Implementation Guides
Project Structure

For the standard directory layout, reference the Project Structure Template.
Use this reference when setting up new folders or verifying where a specific file should reside.

Component Templates

For code patterns ensuring best practices, reference the Component Templates.
This includes:

Server Components with Suspense and data fetching.
Client Components isolated for interactivity.
Server Actions properly typed and validated.
Quality Checklist

Before finalizing a structure or file creation:

 Scope: Is this used in >1 feature? If no, move to _components.
 Server: Is "use client" absolutely necessary? Can it be pushed down the tree?
 Screaming: Does the folder name describe what it does (e.g., (invoices) vs pages)?
 Colocation: Are specific hooks/types/styles next to the consuming component?
Weekly Installs
32
Repository
ivantsxx/my-next-skills
GitHub Stars
2
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass