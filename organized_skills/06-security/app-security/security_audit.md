---
rating: ⭐⭐
title: security_audit
url: https://skills.sh/cityfish91159/maihouses/security_audit
---

# security_audit

skills/cityfish91159/maihouses/security_audit
security_audit
Installation
$ npx skills add https://github.com/cityfish91159/maihouses --skill security_audit
SKILL.md
Security Audit Protocol
1. Critical "Guard" Files

WARNING: The following files are OFF-LIMITS for modification without explicit user approval.

scripts/ai-diff-gate.ts
.github/workflows/**
Any file with midlaw or policy in the name.
2. Database Security (Supabase)
RLS (Row Level Security):
EVERY table must have RLS enabled.
Policies must explicitly define USING and WITH CHECK clauses.
NEVER use service_role key in frontend client code.
SQL Injection:
Use parameterized queries or ORM methods (Supabase JS client) only.
Avoid raw SQL string concatenation.
3. API Security
Authentication:
Verify user exists in req (usually populated by middleware/auth helper).
Check permissions before performing actions (e.g. checkPermission(user.id, 'post.create')).
Input Validation:
Validate ALL inputs using zod schemas.
Sanitize HTML inputs if rendering user content (use DOMPurify).
4. Audit Checklist
 Are guards/policies untouched?
 Is RLS enabled and tested?
 Is input validation (zod) in place?
 Are no secrets committed to code?
 Did I run /security-review (if available) or manual check?
Weekly Installs
17
Repository
cityfish91159/maihouses
GitHub Stars
1
First Seen
Jan 25, 2026