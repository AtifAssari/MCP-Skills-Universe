---
rating: ⭐⭐
title: auth0-migration
url: https://skills.sh/auth0/agent-skills/auth0-migration
---

# auth0-migration

skills/auth0/agent-skills/auth0-migration
auth0-migration
Installation
$ npx skills add https://github.com/auth0/agent-skills --skill auth0-migration
SKILL.md
Auth0 Migration Guide

Migrate users and authentication flows from existing auth providers to Auth0.

Overview
When to Use This Skill
Migrating from another auth provider to Auth0
Bulk importing existing users
Gradually transitioning active user bases
Updating JWT validation in APIs
When NOT to Use
Starting fresh with Auth0 - Use auth0-quickstart for new projects without existing users
Already using Auth0 - This is for migrating TO Auth0, not between Auth0 tenants
Only adding MFA or features - Use feature-specific skills if just adding capabilities
Migration Approaches
Bulk Migration: One-time user import (recommended for small/inactive bases)
Gradual Migration: Lazy migration over time (recommended for large active bases)
Hybrid: Import inactive users, lazy-migrate active users
Step 0: Detect Existing Auth Provider

Check if the project already has authentication:

Search for common auth-related patterns in the codebase:

Pattern	Indicates
signInWithEmailAndPassword, onAuthStateChanged	Firebase Auth
useUser, useSession, isSignedIn	Existing auth hooks
passport.authenticate, LocalStrategy	Passport.js
authorize, getAccessToken, oauth	OAuth/OIDC
JWT, jwt.verify, jsonwebtoken	Token-based auth
/api/auth/, /login, /callback	Auth routes

If existing auth detected, ask:

I detected existing authentication in your project. Are you:

Migrating to Auth0 (replace existing auth)
Adding Auth0 alongside (keep both temporarily)
Starting fresh (remove old auth, new Auth0 setup)
Migration Workflow
Step 1: Export Existing Users

Export users from your current provider. See User Import Guide for detailed instructions:

Exporting from Firebase
Exporting from AWS Cognito
Exporting from Supabase
Exporting from Custom Database

Required data per user:

Email address
Email verified status
Password hash (if available)
User metadata/profile data
Creation timestamp
Step 2: Import Users to Auth0

Import users via Dashboard, CLI, or Management API.

Quick start:

# Via Auth0 CLI
auth0 api post "jobs/users-imports" \
  --data "connection_id=con_ABC123" \
  --data "users=@users.json"


For detailed instructions:

User JSON Format
Password Hash Algorithms
Import Methods
Monitoring Import Progress
Common Import Errors
Step 3: Migrate Application Code

Update your application code to use Auth0 SDKs.

See Code Migration Patterns for detailed before/after examples:

Frontend:

React Migration
Next.js Migration
Vue.js Migration
Angular Migration
React Native Migration

Backend:

Express.js Migration
API JWT Validation

Provider-Specific:

Firebase to Auth0
Supabase to Auth0
Clerk to Auth0

After migrating code, use framework-specific skills:

auth0-react for React applications
auth0-nextjs for Next.js applications
auth0-vue for Vue.js applications
auth0-angular for Angular applications
auth0-express for Express.js applications
auth0-react-native for React Native/Expo applications
Step 4: Update API JWT Validation

If your API validates JWTs, update to validate Auth0 tokens.

Key differences:

Algorithm: HS256 (symmetric) → RS256 (asymmetric)
Issuer: Custom → https://YOUR_TENANT.auth0.com/
JWKS URL: https://YOUR_TENANT.auth0.com/.well-known/jwks.json

See JWT Validation Examples for:

Node.js / Express implementation
Python / Flask implementation
Key differences and migration checklist
Gradual Migration Strategy

For production applications with active users, use a phased approach:

Phase 1: Parallel Auth

Support both Auth0 and legacy provider simultaneously:

// Support both providers during migration
const getUser = async () => {
  // Try Auth0 first
  const auth0User = await getAuth0User();
  if (auth0User) return auth0User;

  // Fall back to legacy provider
  return await getLegacyUser();
};

Phase 2: New Users on Auth0
All new signups go to Auth0
Existing users continue on legacy provider
Migrate users on next login (lazy migration)
Phase 3: Forced Migration
Prompt remaining users to "update account"
Send password reset emails via Auth0
Set deadline for legacy system shutdown
Phase 4: Cleanup
Remove legacy auth code
Archive user export for compliance
Update documentation
Common Migration Issues
Issue	Solution
Password hashes incompatible	Use Auth0 custom DB connection with lazy migration
Social logins don't link	Configure same social connection, users auto-link by email
Custom claims missing	Add claims via Auth0 Actions
Token format different	Update API to validate RS256 JWTs with Auth0 issuer
Session persistence	Auth0 uses rotating refresh tokens; update token storage
Users must re-login	Expected for redirect-based auth; communicate to users
Reference Documentation
User Import

Complete guide to exporting and importing users:

Exporting from Common Providers
User JSON Format
Password Hash Algorithms
Import Methods
Monitoring & Troubleshooting
Code Migration

Before/after examples for all major frameworks:

React Patterns
Next.js Patterns
Express Patterns
Vue.js Patterns
Angular Patterns
React Native Patterns
API JWT Validation
Related Skills
Core Integration
auth0-quickstart - Initial Auth0 setup after migration
SDK Skills
auth0-react - React SPA integration
auth0-nextjs - Next.js integration
auth0-vue - Vue.js integration
auth0-angular - Angular integration
auth0-express - Express.js integration
auth0-react-native - React Native/Expo integration
References
Auth0 User Migration Documentation
Bulk User Import
Password Hash Algorithms
Management API - User Import
Weekly Installs
256
Repository
auth0/agent-skills
GitHub Stars
18
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass