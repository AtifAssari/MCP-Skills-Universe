---
title: audit_logging
url: https://skills.sh/cityfish91159/maihouses/audit_logging
---

# audit_logging

skills/cityfish91159/maihouses/audit_logging
audit_logging
Installation
$ npx skills add https://github.com/cityfish91159/maihouses --skill audit_logging
SKILL.md
Audit Logging Protocol
1. Principles
No Invisible Actions: Every state-changing API call (POST, PUT, DELETE) must produce a log entry.
Traceability: Logs must include userId, action, resourceId, and metadata.
2. Implementation Standards
Backend (API):
Use the project's standard Logger service (e.g., src/services/logger.ts or similar).
Example:
await Logger.info({
  event: 'POST_CREATED',
  userId: user.id,
  metadata: { postId: newPost.id },
});

Database (Supabase):
Ensure tables have created_at, updated_at, and created_by columns.
Check if specific Audit Table inserts are required (e.g. audit_logs table).
3. Verification Checklist
 Does the new API endpoint call Logger?
 Are logs visible in Supabase/Dashboards?
 Is the log level appropriate (Info vs Error)?
 Does the log contain enough context to debug issues later?
Weekly Installs
17
Repository
cityfish91159/maihouses
GitHub Stars
1
First Seen
Jan 25, 2026