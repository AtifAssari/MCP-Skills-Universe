---
title: auth0-quickstart
url: https://skills.sh/auth0/agent-skills/auth0-quickstart
---

# auth0-quickstart

skills/auth0/agent-skills/auth0-quickstart
auth0-quickstart
Installation
$ npx skills add https://github.com/auth0/agent-skills --skill auth0-quickstart
Summary

Framework detection and Auth0 account setup router for nine JavaScript and backend frameworks.

Detects your stack (React, Next.js, Vue, Nuxt, Angular, Express, Fastify, React Native) and routes to the correct framework-specific skill
Provides Auth0 CLI installation and application creation commands for SPAs, regular web apps, and native apps
Includes environment variable setup guides and common mistakes reference for each framework tier
Covers migration patterns from Firebase, Cognito, Supabase, and Clerk via the auth0-migration skill
SKILL.md
Auth0 Quickstart

Detect your framework and get started with Auth0 authentication.

Step 1: Detect Your Framework

Run this command to identify your framework:

# Check package.json dependencies (Node.js projects)
cat package.json | grep -E "react|next|vue|nuxt|angular|express|fastify|@nestjs|expo"

# Or check project files
ls -la | grep -E "angular.json|vue.config.js|next.config|app.json|Package.swift|build.gradle"


Framework Detection Table:

Framework	Detection	Skill to Use
React (Vite/CRA)	"react" in package.json, no Next.js	auth0-react
Next.js	"next" in package.json	auth0-nextjs
Vue.js	"vue" in package.json, no Nuxt	auth0-vue
Nuxt	"nuxt" in package.json	auth0-nuxt
Angular	angular.json exists or "@angular/core"	auth0-angular
Express.js	"express" in package.json	auth0-express
Fastify (web app)	"fastify" in package.json, has @fastify/view	auth0-fastify
Fastify (API)	"fastify" in package.json, no view engine	auth0-fastify-api
React Native	"react-native" or "expo" in package.json	auth0-react-native
Flask	"flask" in requirements.txt, Pipfile, or pyproject.toml	auth0-flask
Node.js API	"express-oauth2-jwt-bearer" in package.json	express-oauth2-jwt-bearer

Don't see your framework? See Tier 2 Frameworks below.

Step 2: Auth0 Account Setup
Install Auth0 CLI

macOS/Linux:

brew install auth0/auth0-cli/auth0


Windows:

scoop install auth0
# Or: choco install auth0-cli


Full installation guide: See CLI Reference

Login to Auth0
auth0 login


This opens your browser to authenticate with Auth0.

Step 3: Create Auth0 Application

Choose application type based on your framework:

Single Page Applications (React, Vue, Angular):

auth0 apps create --name "My App" --type spa \
  --callbacks "http://localhost:3000" \
  --logout-urls "http://localhost:3000" \
  --metadata "created_by=agent_skills"


Regular Web Apps (Next.js, Nuxt, Express, Fastify):

auth0 apps create --name "My App" --type regular \
  --callbacks "http://localhost:3000/api/auth/callback" \
  --logout-urls "http://localhost:3000" \
  --metadata "created_by=agent_skills"


Native Apps (React Native):

auth0 apps create --name "My App" --type native \
  --callbacks "myapp://callback" \
  --logout-urls "myapp://logout" \
  --metadata "created_by=agent_skills"


Get your credentials:

auth0 apps list          # Find your app
auth0 apps show <app-id> # Get client ID and secret


More CLI commands: See CLI Reference

Step 4: Use Framework-Specific Skill

Based on your framework detection, use the appropriate skill:

Tier 1 Frameworks (Dedicated Skills)

Frontend:

auth0-react - React SPAs (Vite, Create React App)
auth0-nextjs - Next.js (App Router and Pages Router)
auth0-vue - Vue.js 3 applications
auth0-nuxt - Nuxt 3/4 applications
auth0-angular - Angular 12+ applications

Backend:

auth0-express - Express.js web applications
auth0-flask - Flask web applications
auth0-fastify - Fastify web applications
auth0-fastify-api - Fastify API authentication
express-oauth2-jwt-bearer - Node.js/Express API JWT Bearer validation

Mobile:

auth0-react-native - React Native and Expo (iOS/Android)
Tier 2 Frameworks (Use Auth0 Docs)

Not yet available as separate skills. Use Auth0 documentation:

Frontend:

SvelteKit
Remix

Backend:

FastAPI (Python)
Django (Python)
Rails (Ruby)
Laravel (PHP)
Go
ASP.NET Core
Spring Boot

Mobile:

iOS (Swift)
Android (Kotlin)
Flutter
Migration from Other Providers

Migrating from another auth provider? Use the auth0-migration skill.

The migration skill covers:

User export from Firebase, Cognito, Supabase, Clerk, etc.
Bulk import to Auth0
Code migration patterns (before/after examples)
JWT validation updates
Gradual migration strategies
Reference Documentation
Environment Variables

Framework-specific environment variable setup:

Vite, Create React App, Angular
Next.js, Express
React Native, Expo
Auth0 Concepts

Core concepts and troubleshooting:

Application Types
Key Terms
OAuth Flows
Troubleshooting
Security Best Practices
CLI Commands

Complete Auth0 CLI reference:

CLI Installation
Creating Applications
User Management
Testing & Debugging
Command Quick Reference
Common Mistakes
Mistake	Fix
Wrong application type	SPAs need "Single Page Application", server apps need "Regular Web Application", mobile needs "Native"
Callback URL not configured	Add your app's callback URL to Allowed Callback URLs in Auth0 Dashboard
Using wrong credentials	Client Secret only needed for Regular Web Apps, not SPAs
Hardcoding credentials in code	Always use environment variables, never commit secrets to git
Not testing locally first	Set up localhost URLs in Auth0 before deploying to production
Mixing application types	Don't use SPA SDK for server-side apps or vice versa
Related Skills
Core Integration
auth0-migration - Migrate from other auth providers
SDK Skills
auth0-spa-js - SPA integration
auth0-react - React SPA integration
auth0-nextjs - Next.js integration
auth0-vue - Vue.js integration
auth0-nuxt - Nuxt 3/4 integration
auth0-angular - Angular integration
auth0-express - Express.js integration
auth0-flask - Flask web app integration
auth0-fastify - Fastify web app integration
auth0-fastify-api - Fastify API integration
express-oauth2-jwt-bearer - Node.js/Express API JWT Bearer validation
auth0-react-native - React Native CLI (bare workflow) integration
auth0-expo - Expo (managed workflow) integration
auth0-android - Android (Kotlin/Java) integration
auth0-swift - iOS/macOS (Swift) integration
auth0-fastapi-api - FastAPI API authentication
auth0-aspnetcore-api - ASP.NET Core API authentication
Advanced Features
auth0-mfa - Multi-Factor Authentication
References
Auth0 Documentation
Auth0 Quickstart Guides
Auth0 CLI Documentation
Auth0 Community Forum
Weekly Installs
1.4K
Repository
auth0/agent-skills
GitHub Stars
18
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass