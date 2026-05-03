---
title: api-security-testing
url: https://skills.sh/sickn33/antigravity-awesome-skills/api-security-testing
---

# api-security-testing

skills/sickn33/antigravity-awesome-skills/api-security-testing
api-security-testing
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill api-security-testing
SKILL.md
API Security Testing Workflow
Overview

Specialized workflow for testing REST and GraphQL API security including authentication, authorization, rate limiting, input validation, and API-specific vulnerabilities.

When to Use This Workflow

Use this workflow when:

Testing REST API security
Assessing GraphQL endpoints
Validating API authentication
Testing API rate limiting
Bug bounty API testing
Workflow Phases
Phase 1: API Discovery
Skills to Invoke
api-fuzzing-bug-bounty - API fuzzing
scanning-tools - API scanning
Actions
Enumerate endpoints
Document API methods
Identify parameters
Map data flows
Review documentation
Copy-Paste Prompts
Use @api-fuzzing-bug-bounty to discover API endpoints

Phase 2: Authentication Testing
Skills to Invoke
broken-authentication - Auth testing
api-security-best-practices - API auth
Actions
Test API key validation
Test JWT tokens
Test OAuth2 flows
Test token expiration
Test refresh tokens
Copy-Paste Prompts
Use @broken-authentication to test API authentication

Phase 3: Authorization Testing
Skills to Invoke
idor-testing - IDOR testing
Actions
Test object-level authorization
Test function-level authorization
Test role-based access
Test privilege escalation
Test multi-tenant isolation
Copy-Paste Prompts
Use @idor-testing to test API authorization

Phase 4: Input Validation
Skills to Invoke
api-fuzzing-bug-bounty - API fuzzing
sql-injection-testing - Injection testing
Actions
Test parameter validation
Test SQL injection
Test NoSQL injection
Test command injection
Test XXE injection
Copy-Paste Prompts
Use @api-fuzzing-bug-bounty to fuzz API parameters

Phase 5: Rate Limiting
Skills to Invoke
api-security-best-practices - Rate limiting
Actions
Test rate limit headers
Test brute force protection
Test resource exhaustion
Test bypass techniques
Document limitations
Copy-Paste Prompts
Use @api-security-best-practices to test rate limiting

Phase 6: GraphQL Testing
Skills to Invoke
api-fuzzing-bug-bounty - GraphQL fuzzing
Actions
Test introspection
Test query depth
Test query complexity
Test batch queries
Test field suggestions
Copy-Paste Prompts
Use @api-fuzzing-bug-bounty to test GraphQL security

Phase 7: Error Handling
Skills to Invoke
api-security-best-practices - Error handling
Actions
Test error messages
Check information disclosure
Test stack traces
Verify logging
Document findings
Copy-Paste Prompts
Use @api-security-best-practices to audit API error handling

API Security Checklist
 Authentication working
 Authorization enforced
 Input validated
 Rate limiting active
 Errors sanitized
 Logging enabled
 CORS configured
 HTTPS enforced
Quality Gates
 All endpoints tested
 Vulnerabilities documented
 Remediation provided
 Report generated
Related Workflow Bundles
security-audit - Security auditing
web-security-testing - Web security
api-development - API development
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
311
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass