---
title: draconian_rls_audit
url: https://skills.sh/cityfish91159/maihouses/draconian_rls_audit
---

# draconian_rls_audit

skills/cityfish91159/maihouses/draconian_rls_audit
draconian_rls_audit
Installation
$ npx skills add https://github.com/cityfish91159/maihouses --skill draconian_rls_audit
SKILL.md
Draconian RLS Audit Protocol
1. Zero Trust (Default-Deny)
Mandate: Every Table MUST have RLS enabled.
Policy: The default state of any table should be NO ACCESS. Access is granted explicitly via Policy.
Detector: Run SELECT ... WHERE rowsecurity = false to hunt down naked tables.
2. The "WITH CHECK" Imperative
Vulnerability: An INSERT or UPDATE policy without WITH CHECK allows users to write data they cannot read, or worse, escalate privileges (e.g., "Give myself admin role").
Rule: ALL modification policies MUST have a WITH CHECK clause matching the USING clause (or stricter).
3. Client-Side Key Ban
Strict Rule: The string service_role MUST NOT exist in any file within src/.
Enforcement: Grep for it. If found, STOP and warn the user.
4. Explicit auth.uid() Binding
Rule: Policies should almost always bind to auth.uid().
Ban: Never hardcode UUIDs or email addresses in SQL policies.
5. Audit Checklist
 RLS enabled?
 Default policy is DENY?
 WITH CHECK present on writes?
 No service_role in client code?
Weekly Installs
17
Repository
cityfish91159/maihouses
GitHub Stars
1
First Seen
Jan 25, 2026