---
rating: ⭐⭐
title: tanstack-start-best-practices
url: https://skills.sh/deckardger/tanstack-agent-skills/tanstack-start-best-practices
---

# tanstack-start-best-practices

skills/deckardger/tanstack-agent-skills/tanstack-start-best-practices
tanstack-start-best-practices
Installation
$ npx skills add https://github.com/deckardger/tanstack-agent-skills --skill tanstack-start-best-practices
Summary

Best practices for full-stack React development with TanStack Start, covering server functions, middleware, SSR, and authentication.

Organizes 31 rules across 10 categories (server functions, security, middleware, authentication, SSR, error handling, and more) with priority levels to guide implementation order
Covers critical patterns for server-side logic, input validation, secure session management, and client-server boundary handling
Includes middleware composition, selective SSR configuration, streaming for performance, and environment-based configuration management
Each rule provides explanation, anti-patterns, recommended implementations, and contextual guidance for when to apply or skip
SKILL.md
TanStack Start Best Practices

Comprehensive guidelines for implementing TanStack Start patterns in full-stack React applications. These rules cover server functions, middleware, SSR, authentication, and deployment.

When to Apply
Creating server functions for data mutations
Setting up middleware for auth/logging
Configuring SSR and hydration
Implementing authentication flows
Handling errors across client/server boundary
Organizing full-stack code
Deploying to various platforms
Rule Categories by Priority
Priority	Category	Rules	Impact
CRITICAL	Server Functions	5 rules	Core data mutation patterns
CRITICAL	Security	4 rules	Prevents vulnerabilities
HIGH	Middleware	4 rules	Request/response handling
HIGH	Authentication	4 rules	Secure user sessions
MEDIUM	API Routes	1 rule	External endpoint patterns
MEDIUM	SSR	6 rules	Server rendering patterns
MEDIUM	Error Handling	3 rules	Graceful failure handling
MEDIUM	Environment	1 rule	Configuration management
LOW	File Organization	3 rules	Maintainable code structure
LOW	Deployment	2 rules	Production readiness
Quick Reference
Server Functions (Prefix: sf-)
sf-create-server-fn — Use createServerFn for server-side logic
sf-input-validation — Always validate server function inputs
sf-method-selection — Choose appropriate HTTP method
sf-error-handling — Handle errors in server functions
sf-response-headers — Customize response headers when needed
Security (Prefix: sec-)
sec-validate-inputs — Validate all user inputs with schemas
sec-auth-middleware — Protect routes with auth middleware
sec-sensitive-data — Keep secrets server-side only
sec-csrf-protection — Implement CSRF protection for mutations
Middleware (Prefix: mw-)
mw-request-middleware — Use request middleware for cross-cutting concerns
mw-function-middleware — Use function middleware for server functions
mw-context-flow — Properly pass context through middleware
mw-composability — Compose middleware effectively
Authentication (Prefix: auth-)
auth-session-management — Implement secure session handling
auth-route-protection — Protect routes with beforeLoad
auth-server-functions — Verify auth in server functions
auth-cookie-security — Configure secure cookie settings
API Routes (Prefix: api-)
api-routes — Create API routes for external consumers
SSR (Prefix: ssr-)
ssr-data-loading — Load data appropriately for SSR
ssr-hydration-safety — Prevent hydration mismatches
ssr-streaming — Implement streaming SSR for faster TTFB
ssr-selective — Apply selective SSR when beneficial
ssr-prerender — Configure static prerendering and ISR
Environment (Prefix: env-)
env-functions — Use environment functions for configuration
Error Handling (Prefix: err-)
err-server-errors — Handle server function errors
err-redirects — Use redirects appropriately
err-not-found — Handle not-found scenarios
File Organization (Prefix: file-)
file-separation — Separate server and client code
file-functions-file — Use .functions.ts pattern
file-shared-validation — Share validation schemas
Deployment (Prefix: deploy-)
deploy-env-config — Configure environment variables
deploy-adapters — Choose appropriate deployment adapter
How to Use

Each rule file in the rules/ directory contains:

Explanation — Why this pattern matters
Bad Example — Anti-pattern to avoid
Good Example — Recommended implementation
Context — When to apply or skip this rule
Full Reference

See individual rule files in rules/ directory for detailed guidance and code examples.

Weekly Installs
5.1K
Repository
deckardger/tans…t-skills
GitHub Stars
151
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass