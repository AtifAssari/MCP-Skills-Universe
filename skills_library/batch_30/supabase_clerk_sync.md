---
title: supabase-clerk-sync
url: https://skills.sh/vanman2024/ai-dev-marketplace/supabase-clerk-sync
---

# supabase-clerk-sync

skills/vanman2024/ai-dev-marketplace/supabase-clerk-sync
supabase-clerk-sync
Installation
$ npx skills add https://github.com/vanman2024/ai-dev-marketplace --skill supabase-clerk-sync
SKILL.md
Supabase-Clerk Sync

Comprehensive integration patterns for syncing Clerk authentication with Supabase databases, including JWT configuration, RLS policies, webhook setup, and user data synchronization.

Instructions
When Integrating Clerk with Supabase

JWT Configuration Strategy

Configure Supabase to validate Clerk JWT tokens
Extract Clerk JWT template from dashboard
Configure Supabase auth settings with Clerk JWKS endpoint
Map Clerk user claims to Supabase RLS policies
Handle JWT expiration and refresh flows

User Sync Architecture

Choose sync strategy: Webhook-based (recommended) or Client-side
Set up Clerk webhooks for user lifecycle events
Create Supabase tables for user profile data
Implement idempotent sync operations
Handle race conditions and eventual consistency

RLS Policy Design

Use Clerk sub claim as user identifier in policies
Extract user metadata from JWT for policy decisions
Implement role-based access with Clerk organizations
Create policies for user-owned resources
Test policies with different JWT claims

Webhook Implementation

Verify Clerk webhook signatures (svix library)
Handle user.created, user.updated, user.deleted events
Implement retry logic for failed syncs
Log sync operations for debugging
Use Supabase service role key for webhook operations
Integration Workflow

Phase 1: JWT Setup

Get Clerk JWKS URL from dashboard
Configure Supabase auth.jwt_secret
Update Supabase JWT settings with Clerk issuer
Test JWT validation with sample tokens

Phase 2: Database Schema

Create users table with Clerk ID mapping
Add user metadata columns
Set up RLS policies using JWT claims
Create indexes for performance

Phase 3: Webhook Configuration

Deploy webhook endpoint (Supabase Edge Function or external)
Register webhook URL in Clerk dashboard
Select user events to sync
Implement signature verification

Phase 4: Client Integration

Configure Supabase client with Clerk session token
Implement token refresh in client
Test authenticated requests
Handle authentication errors
Security Best Practices

JWT Validation:

Always verify JWT signature with Clerk JWKS
Validate issuer matches Clerk instance
Check token expiration
Reject tokens with missing required claims

RLS Policies:

Use auth.uid() to extract Clerk user ID from JWT
Never trust client-provided user IDs
Test policies with different user roles
Implement least-privilege access

Webhook Security:

Verify Svix signatures on all webhook requests
Use HTTPS for webhook endpoints
Store Clerk webhook secret securely
Implement rate limiting on webhook endpoints

API Keys:

Never hardcode API keys in client code
Use environment variables for secrets
Rotate keys periodically
Use Supabase anon key for client, service role for webhooks
Sync Strategies

Webhook-Based Sync (Recommended):

Real-time synchronization
Server-side security
Centralized logic
Better error handling
Recommended for production

Client-Side Sync:

User initiates sync on login
Requires RLS policies for user writes
Simpler setup for prototypes
Race conditions possible
Common Integration Patterns

Pattern 1: Public Profile with Private Data

users_public (readable by all, RLS enforced)
  - clerk_id
  - username
  - avatar_url

users_private (readable only by owner)
  - clerk_id
  - email
  - metadata


Pattern 2: Organization-Based Access

RLS Policy:
  auth.jwt()->>'org_id' = organizations.clerk_org_id


Pattern 3: Role-Based Permissions

RLS Policy:
  auth.jwt()->>'role' IN ('admin', 'editor')

Troubleshooting

JWT Validation Fails:

Verify JWKS URL is correct
Check Supabase JWT secret configuration
Ensure token hasn't expired
Validate issuer claim matches

User Sync Delays:

Check webhook delivery in Clerk dashboard
Verify webhook endpoint is accessible
Review webhook logs for errors
Confirm Supabase connection

RLS Policy Denies Access:

Inspect JWT claims in request
Test policy SQL in Supabase SQL editor
Verify user ID extraction from JWT
Check table permissions
Scripts

Automated setup and configuration scripts:

scripts/setup-sync.sh - Configure Supabase for Clerk JWT validation
scripts/configure-rls.sh - Generate RLS policies for Clerk authentication
scripts/create-webhooks.sh - Deploy webhook infrastructure
scripts/test-jwt.sh - Test JWT validation and claim extraction
scripts/sync-users.sh - Manually trigger user synchronization
Templates

Integration code templates for different scenarios:

TypeScript Templates
templates/supabase-client-clerk.ts - Supabase client with Clerk session token
templates/webhook-sync.ts - Clerk webhook handler for user sync
templates/edge-function-webhook.ts - Supabase Edge Function webhook
templates/middleware-auth.ts - Next.js middleware with Clerk + Supabase
SQL Templates
templates/rls-policies-clerk.sql - Comprehensive RLS policies
templates/user-schema.sql - User tables schema
templates/triggers.sql - Database triggers for audit logging
Configuration Templates
templates/env.example - Environment variables template
templates/clerk-jwt-template.json - JWT template configuration
Examples

Complete working examples:

examples/complete-integration.tsx - Full Next.js app with Clerk + Supabase
examples/webhook-handler.ts - Production webhook implementation
examples/protected-route.tsx - Protected page with RLS
examples/organization-access.tsx - Multi-tenant with organizations
Migration Guide
From Supabase Auth to Clerk

Export Users:

Extract user data from Supabase auth.users
Prepare user import CSV for Clerk

Update Database:

Add clerk_id column to user tables
Migrate RLS policies to use JWT claims
Update foreign key references

Deploy Webhooks:

Set up webhook infrastructure
Enable user sync

Update Client:

Replace Supabase auth with Clerk
Update Supabase client initialization
Test authentication flows

Cutover:

Enable Clerk in production
Disable Supabase Auth
Monitor for issues
Performance Optimization

Database Indexes:

CREATE INDEX idx_users_clerk_id ON users(clerk_id);
CREATE INDEX idx_orgs_clerk_org_id ON organizations(clerk_org_id);


Webhook Performance:

Use database connection pooling
Batch user updates when possible
Implement async processing for large syncs
Cache frequently accessed user data

Client Performance:

Cache Supabase client instance
Refresh tokens proactively
Use Supabase realtime for live updates
Implement optimistic updates
Reference Documentation

Clerk:

JWT Templates: Configure custom claims for Supabase
Webhooks: Event types and payload structure
Organizations: Multi-tenant patterns

Supabase:

JWT Authentication: Custom JWT provider setup
RLS Policies: Policy syntax and testing
Edge Functions: Serverless webhook handlers
PostgreSQL Functions: Custom JWT claim extraction
Security Checklist

Before going to production:

 JWT signature validation configured
 Webhook signatures verified
 RLS policies tested with different users
 Service role key stored securely
 Webhook endpoint uses HTTPS
 Rate limiting implemented
 Error logging configured
 User data encrypted at rest
 API keys rotated
 Audit logging enabled
Use When
Integrating Clerk authentication with Supabase database
Syncing user profiles from Clerk to Supabase
Implementing Row Level Security with Clerk JWT tokens
Setting up webhooks for real-time user synchronization
Building multi-tenant applications with Clerk organizations
Migrating from Supabase Auth to Clerk
Configuring secure database access with external auth provider
Implementing organization-based data access patterns
Weekly Installs
11
Repository
vanman2024/ai-d…ketplace
GitHub Stars
10
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn