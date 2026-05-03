---
rating: ⭐⭐⭐
title: supabase-audit-buckets-list
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-audit-buckets-list
---

# supabase-audit-buckets-list

skills/yoanbernabeu/supabase-pentest-skills/supabase-audit-buckets-list
supabase-audit-buckets-list
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-audit-buckets-list
SKILL.md
List Storage Buckets

🔴 CRITICAL: PROGRESSIVE FILE UPDATES REQUIRED

You MUST write to context files AS YOU GO, not just at the end.

Write to .sb-pentest-context.json IMMEDIATELY after each bucket discovered
Log to .sb-pentest-audit.log BEFORE and AFTER each operation
DO NOT wait until the skill completes to update files
If the skill crashes or is interrupted, all prior findings must already be saved

This is not optional. Failure to write progressively is a critical error.

This skill discovers all storage buckets configured in a Supabase project.

When to Use This Skill
To inventory all storage buckets
Before testing bucket access permissions
To identify publicly accessible buckets
As part of storage security audit
Prerequisites
Supabase URL and anon key available
Detection completed
Understanding Supabase Storage

Supabase Storage provides:

https://[project].supabase.co/storage/v1/


Buckets can be:

Public: Files accessible without authentication
Private: Files require authentication and RLS policies
Storage API Endpoints
Endpoint	Purpose
/storage/v1/bucket	List buckets
/storage/v1/object/list/[bucket]	List files in bucket
/storage/v1/object/[bucket]/[path]	Access file
/storage/v1/object/public/[bucket]/[path]	Public file URL
Usage
Basic Bucket List
List storage buckets on my Supabase project

With Configuration Details
List all buckets with their security settings

Output Format
═══════════════════════════════════════════════════════════
 STORAGE BUCKETS
═══════════════════════════════════════════════════════════

 Project: abc123def.supabase.co
 Buckets Found: 5

 ─────────────────────────────────────────────────────────
 Bucket Inventory
 ─────────────────────────────────────────────────────────

 1. avatars
    ├── Public: ✅ YES
    ├── File Size Limit: 1MB
    ├── Allowed MIME: image/jpeg, image/png, image/webp
    ├── Files (estimated): 1,247
    └── Status: ℹ️ Expected public bucket

    Public URLs pattern:
    https://abc123def.supabase.co/storage/v1/object/public/avatars/[filename]

 2. documents
    ├── Public: ❌ NO (Private)
    ├── File Size Limit: 50MB
    ├── Allowed MIME: application/pdf, application/msword, *
    ├── Files (estimated): 523
    └── Status: ✅ Private, needs RLS verification

 3. uploads
    ├── Public: ✅ YES
    ├── File Size Limit: 100MB
    ├── Allowed MIME: */* (ANY)
    ├── Files (estimated): 3,891
    └── Status: 🟠 P1 - Public with unrestricted MIME types

    Risk: Any file type can be uploaded and accessed
    Recommendation: Restrict allowed MIME types

 4. backups
    ├── Public: ✅ YES ← UNEXPECTED
    ├── File Size Limit: 500MB
    ├── Allowed MIME: */*
    ├── Files (estimated): 45
    └── Status: 🔴 P0 - Sensitive bucket is PUBLIC

    Risk: Backup files publicly accessible!
    Immediate Action: Change to private bucket

 5. temp
    ├── Public: ❌ NO
    ├── File Size Limit: 10MB
    ├── Allowed MIME: */*
    ├── Files (estimated): 12
    └── Status: ✅ Private temporary storage

 ─────────────────────────────────────────────────────────
 Summary
 ─────────────────────────────────────────────────────────

 Total Buckets: 5
 Public Buckets: 3
   ├── Expected Public: 1 (avatars)
   ├── P1 Issues: 1 (uploads - unrestricted MIME)
   └── P0 Critical: 1 (backups - should be private)

 Private Buckets: 2
   └── Need RLS verification with supabase-audit-buckets-read

 Next Steps:
 ├── Fix 'backups' bucket - make private immediately
 ├── Restrict MIME types on 'uploads' bucket
 ├── Test RLS on private buckets
 └── Verify no sensitive files in public buckets

═══════════════════════════════════════════════════════════

Bucket Configuration Analysis
Config	Good	Bad
public: false	✅ Private by default	❌ public: true for sensitive data
fileSizeLimit	✅ Appropriate limits	❌ No limit or very large
allowedMimeTypes	✅ Restricted list	❌ */* allows anything
Context Output
{
  "storage": {
    "buckets": [
      {
        "name": "avatars",
        "public": true,
        "file_size_limit": 1048576,
        "allowed_mime_types": ["image/jpeg", "image/png", "image/webp"],
        "estimated_files": 1247,
        "risk_level": "info",
        "expected_public": true
      },
      {
        "name": "backups",
        "public": true,
        "file_size_limit": 524288000,
        "allowed_mime_types": ["*/*"],
        "estimated_files": 45,
        "risk_level": "P0",
        "finding": "Sensitive bucket publicly accessible"
      }
    ],
    "summary": {
      "total": 5,
      "public": 3,
      "private": 2,
      "p0_issues": 1,
      "p1_issues": 1
    }
  }
}

Security Recommendations
For Public Buckets
-- Create restrictive RLS policy even for public buckets
CREATE POLICY "Public read avatars"
  ON storage.objects FOR SELECT
  USING (bucket_id = 'avatars');

CREATE POLICY "Users upload own avatar"
  ON storage.objects FOR INSERT
  WITH CHECK (
    bucket_id = 'avatars'
    AND auth.uid()::text = (storage.foldername(name))[1]
  );

For Private Buckets
-- Only owners can access their files
CREATE POLICY "Users access own documents"
  ON storage.objects FOR ALL
  USING (
    bucket_id = 'documents'
    AND auth.uid()::text = (storage.foldername(name))[1]
  );

Fix Public Backup Bucket
-- Make bucket private
UPDATE storage.buckets
SET public = false
WHERE name = 'backups';

-- Add strict RLS
CREATE POLICY "Only admins access backups"
  ON storage.objects FOR ALL
  USING (
    bucket_id = 'backups'
    AND (SELECT is_admin FROM profiles WHERE id = auth.uid())
  );

Common Issues

❌ Problem: Cannot list buckets ✅ Solution: Storage API may be restricted. This is actually good security. Note as "unable to enumerate."

❌ Problem: Many buckets found ✅ Solution: Large applications may have many. Focus on public buckets first.

❌ Problem: Bucket count doesn't match expected ✅ Solution: Some buckets may be created dynamically. Check application code.

MANDATORY: Progressive Context File Updates

⚠️ This skill MUST update tracking files PROGRESSIVELY during execution, NOT just at the end.

Critical Rule: Write As You Go

DO NOT batch all writes at the end. Instead:

Before starting bucket enumeration → Log the action to .sb-pentest-audit.log
After each bucket discovered → Immediately update .sb-pentest-context.json
After each configuration analyzed → Log the result

This ensures that if the skill is interrupted, crashes, or times out, all findings up to that point are preserved.

Required Actions (Progressive)

Update .sb-pentest-context.json with results:

{
  "storage": {
    "buckets": [ ... ],
    "summary": { "total": 5, "public": 3, "private": 2 }
  }
}


Log to .sb-pentest-audit.log:

[TIMESTAMP] [supabase-audit-buckets-list] [START] Listing storage buckets
[TIMESTAMP] [supabase-audit-buckets-list] [SUCCESS] Found 5 buckets
[TIMESTAMP] [supabase-audit-buckets-list] [CONTEXT_UPDATED] .sb-pentest-context.json updated


If files don't exist, create them before writing.

FAILURE TO UPDATE CONTEXT FILES IS NOT ACCEPTABLE.

MANDATORY: Evidence Collection

📁 Evidence Directory: .sb-pentest-evidence/04-storage-audit/

Evidence Files to Create
File	Content
buckets-config.json	All bucket configurations
buckets/[name]/file-list.json	File listing per bucket
Evidence Format
{
  "evidence_id": "STG-LIST-001",
  "timestamp": "2025-01-31T10:35:00Z",
  "category": "storage-audit",
  "type": "bucket_enumeration",

  "request": {
    "method": "GET",
    "url": "https://abc123def.supabase.co/storage/v1/bucket",
    "curl_command": "curl -s '$URL/storage/v1/bucket' -H 'apikey: $ANON_KEY' -H 'Authorization: Bearer $ANON_KEY'"
  },

  "buckets": [
    {
      "name": "avatars",
      "public": true,
      "file_size_limit": 1048576,
      "allowed_mime_types": ["image/jpeg", "image/png"],
      "risk_level": "info",
      "assessment": "Appropriate for public avatars"
    },
    {
      "name": "backups",
      "public": true,
      "file_size_limit": 524288000,
      "allowed_mime_types": ["*/*"],
      "risk_level": "P0",
      "assessment": "CRITICAL: Backup bucket should not be public"
    }
  ],

  "summary": {
    "total_buckets": 5,
    "public_buckets": 3,
    "private_buckets": 2,
    "critical_misconfigurations": 1
  }
}

Add to curl-commands.sh
# === STORAGE BUCKET ENUMERATION ===
# List all buckets
curl -s "$SUPABASE_URL/storage/v1/bucket" \
  -H "apikey: $ANON_KEY" \
  -H "Authorization: Bearer $ANON_KEY"

# List files in specific bucket
curl -s "$SUPABASE_URL/storage/v1/object/list/backups" \
  -H "apikey: $ANON_KEY" \
  -H "Authorization: Bearer $ANON_KEY"

Related Skills
supabase-audit-buckets-read — Attempt to read files
supabase-audit-buckets-public — Find misconfigured public buckets
supabase-audit-storage-rls — Test storage RLS policies
Weekly Installs
148
Repository
yoanbernabeu/su…t-skills
GitHub Stars
37
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn