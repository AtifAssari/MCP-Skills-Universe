---
title: code-review
url: https://skills.sh/shino369/claude-code-personal-workspace/code-review
---

# code-review

skills/shino369/claude-code-personal-workspace/code-review
code-review
Installation
$ npx skills add https://github.com/shino369/claude-code-personal-workspace --skill code-review
SKILL.md
Code Review Best Practices
Core Principles

Review Mindset:

Be constructive, explain the "why"
Prioritize by severity (critical vs nice-to-have)
Suggest alternatives, not just problems
Acknowledge good work

Goals:

Catch bugs before production
Improve code quality
Share knowledge
Prevent security vulnerabilities
Ensure consistency
Security Review
OWASP Top 10 Critical Checks

Injection Attacks:

SQL: Use parameterized queries, never concatenate user input
Command: Avoid shell commands with user input, sanitize properly
Code: Validate all eval(), exec(), dynamic execution
NoSQL/LDAP/XML: Use safe APIs

Authentication & Authorization:

Verify auth checks on protected endpoints
Proper session management (timeout, secure cookies)
Authorization logic prevents privilege escalation
Password policies enforced

Sensitive Data:

No hardcoded secrets (API keys, passwords, tokens)
Encryption at rest and in transit
PII/PHI minimally logged
No sensitive data in URLs or error messages

XSS Prevention:

All user input escaped/sanitized for output context
Content-Security-Policy headers configured
Framework built-in escaping (React JSX, template engines)

Deserialization:

Never deserialize untrusted data without validation
Prefer JSON over pickle/marshal
Validate object types post-deserialization

Misconfiguration:

No default credentials in production
Error messages don't leak internals
Security headers present (HSTS, X-Frame-Options)

API Security:

Rate limiting on sensitive endpoints
CORS properly configured
Input validation on all endpoints
No sensitive data in GET requests
Common Security Issues
Path Traversal: Validate paths, prevent ../ attacks
SSRF: Validate URLs, restrict internal network access
Open Redirects: Whitelist redirect destinations
Race Conditions: Check TOCTOU bugs
Timing Attacks: Constant-time comparison for secrets
Regex DoS: Avoid complex regex on user input
Code Quality
Readability & Maintainability

Naming:

Clear, descriptive names that reveal intent
Consistent conventions (camelCase, snake_case, PascalCase)
Avoid abbreviations unless domain-standard

Function Design:

Single responsibility, small (<50 lines ideal)
Clear input/output, minimal side effects
Pure functions where possible

Complexity:

Low cyclomatic complexity (<10)
Avoid deep nesting (max 3-4 levels)
Early returns to reduce nesting
Extract complex conditions into named functions

Documentation:

Comments explain "why", not "what"
Public APIs documented
No commented-out code (use version control)
Error Handling
All errors handled (catch, log, recover or fail fast)
No bare except/catch without handling
Informative error messages (what, why, action)
Proper error types (not generic Exception)
Resources cleaned up (finally/defer/using)

Anti-patterns:

Swallowing exceptions silently
Catching too broadly
Using exceptions for flow control
Returning null instead of error
Not validating inputs
Code Duplication
No copy-paste code blocks
Extract common logic to reusable functions
Use inheritance/composition appropriately
Be pragmatic: 3+ copies = refactor time
Performance
Algorithm & Data Structure Efficiency
Check time complexity (O(n²) → O(n log n) or O(n))
Appropriate space complexity
Right data structure (HashMap vs Array, Set vs List)
Efficient algorithms for common problems
Common Issues

Database:

N+1 query problems (use joins/batch)
Missing indexes on filtered/sorted columns
SELECT * instead of specific columns
Queries inside loops

Caching:

Repeated expensive calculations
Duplicate API calls
Static data not cached
Appropriate cache TTL

Resource Management:

Files/connections/streams closed
No memory leaks (circular refs, event listeners)
Unbounded collections (need limits/pagination)

Frontend:

Unnecessary re-renders (React useMemo, useCallback)
Large bundles (code splitting)
Images not optimized
Blocking JavaScript in critical path
Architecture & Design
SOLID Principles
Single Responsibility: One reason to change
Open/Closed: Open for extension, closed for modification
Liskov Substitution: Subtypes substitutable for base types
Interface Segregation: Small, focused interfaces
Dependency Inversion: Depend on abstractions
Other Key Principles
DRY: Don't Repeat Yourself
KISS: Keep It Simple
YAGNI: Don't over-engineer
Separation of Concerns: Distinct responsibilities
Composition over Inheritance
Code Structure
Proper layer separation (presentation, business, data)
Dependencies flow one direction
No circular dependencies
Modules cohesive and loosely coupled
Configuration separated from code
Testing
Coverage & Quality
Critical paths tested
Edge cases covered (empty, null, max values)
Error paths tested
Tests deterministic (no flaky tests)
Tests isolated (no shared state)

Test Quality:

Arrange-Act-Assert structure
One assertion focus per test
Descriptive test names
No test logic (tests are simple)
Realistic test data
External dependencies mocked appropriately
Review Process
Before Review
Understand context (PR description, tickets)
Check scope (< 400 lines ideal)
Run code locally
Verify CI passes
During Review
Start with architecture/approach
Use security/performance/quality checklists
Review tests first (explain intended behavior)
Ask questions, don't assume
Providing Feedback

Structure:

Severity: Critical (must fix) vs Nice-to-have
What: Specific issue
Why: Why it matters
How: Concrete alternative

Tone:

Use "we" language: "We should..." not "You should..."
Ask questions: "Have we considered...?"
Be specific: "Function has complexity 32, consider refactoring"

Example: ❌ "This is bad" ✅ "Using string concatenation in loop creates O(n²) complexity. Use StringBuilder for O(n)."

Priority Checklist
Critical (Must Fix)
 Security vulnerabilities (injection, XSS, auth bypass)
 Data loss/corruption risks
 Memory/resource leaks
 Breaking API changes without versioning
 Race conditions/concurrency bugs
High Priority
 Performance issues (O(n²), N+1 queries)
 Missing input validation
 Hardcoded configuration
 Missing error logging
 No tests for new functionality
Medium Priority
 Code duplication (3+ instances)
 High complexity (>15 cyclomatic)
 Missing documentation for public APIs
 Deep nesting (>4 levels)
 Large functions (>100 lines)
Low Priority
 Minor style inconsistencies
 Could be more idiomatic
 Variable names could be clearer
 Magic numbers → constants
Language-Specific Notes

JavaScript/TypeScript:

Use const over let, avoid var
Proper async/await (handle rejections)
Use === not ==
TypeScript: Proper types, avoid any
Null/undefined handling

Python:

Follow PEP 8
Type hints for public APIs
Context managers (with)
No mutable default arguments

Java:

Proper exception hierarchy
Try-with-resources
Access modifiers (private/protected/public)
Immutability (final fields)

Go:

Error handling on every call
defer for cleanup
No goroutine leaks (context cancellation)
Small, focused interfaces
Best Practices Summary
Security First: OWASP Top 10 vulnerabilities
Test Coverage: Meaningful tests exist
Error Handling: All errors handled
Performance: Watch O(n²), N+1, memory leaks
Readability: Clear, self-documenting code
Maintainability: Low complexity, no duplication
Documentation: Public APIs documented
Consistency: Follow team conventions
Constructive: Be helpful, not critical
Prioritize: Critical first, style last
Weekly Installs
15
Repository
shino369/claude…orkspace
GitHub Stars
2
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass