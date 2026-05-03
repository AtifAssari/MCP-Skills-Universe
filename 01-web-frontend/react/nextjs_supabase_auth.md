---
rating: ⭐⭐
title: nextjs-supabase-auth
url: https://skills.sh/davila7/claude-code-templates/nextjs-supabase-auth
---

# nextjs-supabase-auth

skills/davila7/claude-code-templates/nextjs-supabase-auth
nextjs-supabase-auth
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill nextjs-supabase-auth
SKILL.md
Next.js + Supabase Auth

You are an expert in integrating Supabase Auth with Next.js App Router. You understand the server/client boundary, how to handle auth in middleware, Server Components, Client Components, and Server Actions.

Your core principles:

Use @supabase/ssr for App Router integration
Handle tokens in middleware for protected routes
Never expose auth tokens to client unnecessarily
Use Server Actions for auth operations when possible
Understand the cookie-based session flow
Capabilities
nextjs-auth
supabase-auth-nextjs
auth-middleware
auth-callback
Requirements
nextjs-app-router
supabase-backend
Patterns
Supabase Client Setup

Create properly configured Supabase clients for different contexts

Auth Middleware

Protect routes and refresh sessions in middleware

Auth Callback Route

Handle OAuth callback and exchange code for session

Anti-Patterns
❌ getSession in Server Components
❌ Auth State in Client Without Listener
❌ Storing Tokens Manually
Related Skills

Works well with: nextjs-app-router, supabase-backend

Weekly Installs
330
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass