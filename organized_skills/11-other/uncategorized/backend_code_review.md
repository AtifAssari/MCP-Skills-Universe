---
rating: ⭐⭐⭐
title: backend-code-review
url: https://skills.sh/langgenius/dify/backend-code-review
---

# backend-code-review

skills/langgenius/dify/backend-code-review
backend-code-review
Installation
$ npx skills add https://github.com/langgenius/dify --skill backend-code-review
SKILL.md
Backend Code Review
When to use this skill

Use this skill whenever the user asks to review, analyze, or improve backend code (e.g., .py) under the api/ directory. Supports the following review modes:

Pending-change review: when the user asks to review current changes (inspect staged/working-tree files slated for commit to get the changes).
Code snippets review: when the user pastes code snippets (e.g., a function/class/module excerpt) into the chat and asks for a review.
File-focused review: when the user points to specific files and asks for a review of those files (one file or a small, explicit set of files, e.g., api/..., api/app.py).

Do NOT use this skill when:

The request is about frontend code or UI (e.g., .tsx, .ts, .js, web/).
The user is not asking for a review/analysis/improvement of backend code.
The scope is not under api/ (unless the user explicitly asks to review backend-related changes outside api/).
How to use this skill

Follow these steps when using this skill:

Identify the review mode (pending-change vs snippet vs file-focused) based on the user’s input. Keep the scope tight: review only what the user provided or explicitly referenced.
Follow the rules defined in Checklist to perform the review. If no Checklist rule matches, apply General Review Rules as a fallback to perform the best-effort review.
Compose the final output strictly follow the Required Output Format.

Notes when using this skill:

Always include actionable fixes or suggestions (including possible code snippets).
Use best-effort File:Line references when a file path and line numbers are available; otherwise, use the most specific identifier you can.
Checklist
db schema design: if the review scope includes code/files under api/models/ or api/migrations/, follow references/db-schema-rule.md to perform the review
architecture: if the review scope involves controller/service/core-domain/libs/model layering, dependency direction, or moving responsibilities across modules, follow references/architecture-rule.md to perform the review
repositories abstraction: if the review scope contains table/model operations (e.g., select(...), session.execute(...), joins, CRUD) and is not under api/repositories, api/core/repositories, or api/extensions/*/repositories/, follow references/repositories-rule.md to perform the review
sqlalchemy patterns: if the review scope involves SQLAlchemy session/query usage, db transaction/crud usage, or raw SQL usage, follow references/sqlalchemy-rule.md to perform the review
General Review Rules
1. Security Review

Check for:

SQL injection vulnerabilities
Server-Side Request Forgery (SSRF)
Command injection
Insecure deserialization
Hardcoded secrets/credentials
Improper authentication/authorization
Insecure direct object references
2. Performance Review

Check for:

N+1 queries
Missing database indexes
Memory leaks
Blocking operations in async code
Missing caching opportunities
3. Code Quality Review

Check for:

Code forward compatibility
Code duplication (DRY violations)
Functions doing too much (SRP violations)
Deep nesting / complex conditionals
Magic numbers/strings
Poor naming
Missing error handling
Incomplete type coverage
4. Testing Review

Check for:

Missing test coverage for new code
Tests that don't test behavior
Flaky test patterns
Missing edge cases
Required Output Format

When this skill invoked, the response must exactly follow one of the two templates:

Template A (any findings)
# Code Review Summary

Found <X> critical issues need to be fixed:

## 🔴 Critical (Must Fix)

### 1. <brief description of the issue>

FilePath: <path> line <line>
<relevant code snippet or pointer>

#### Explanation

<detailed explanation and references of the issue>

#### Suggested Fix

1. <brief description of suggested fix>
2. <code example> (optional, omit if not applicable)

---
... (repeat for each critical issue) ...

Found <Y> suggestions for improvement:

## 🟡 Suggestions (Should Consider)

### 1. <brief description of the suggestion>

FilePath: <path> line <line>
<relevant code snippet or pointer>

#### Explanation

<detailed explanation and references of the suggestion>

#### Suggested Fix

1. <brief description of suggested fix>
2. <code example> (optional, omit if not applicable)

---
... (repeat for each suggestion) ...

Found <Z> optional nits:

## 🟢 Nits (Optional)
### 1. <brief description of the nit>

FilePath: <path> line <line>
<relevant code snippet or pointer>

#### Explanation

<explanation and references of the optional nit>

#### Suggested Fix

- <minor suggestions>

---
... (repeat for each nits) ...

## ✅ What's Good

- <Positive feedback on good patterns>

If there are no critical issues or suggestions or option nits or good points, just omit that section.
If the issue number is more than 10, summarize as "Found 10+ critical issues/suggestions/optional nits" and only output the first 10 items.
Don't compress the blank lines between sections; keep them as-is for readability.
If there is any issue requires code changes, append a brief follow-up question to ask whether the user wants to apply the fix(es) after the structured output. For example: "Would you like me to use the Suggested fix(es) to address these issues?"
Template B (no issues)
## Code Review Summary
✅ No issues found.

Weekly Installs
591
Repository
langgenius/dify
GitHub Stars
139.9K
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail