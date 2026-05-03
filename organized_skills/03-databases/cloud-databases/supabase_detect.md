---
rating: ⭐⭐⭐
title: supabase-detect
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-detect
---

# supabase-detect

skills/yoanbernabeu/supabase-pentest-skills/supabase-detect
supabase-detect
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-detect
SKILL.md
Supabase Detection

🔴 CRITICAL: PROGRESSIVE FILE UPDATES REQUIRED

You MUST write to context files AS YOU GO, not just at the end.

Write to .sb-pentest-context.json IMMEDIATELY after each discovery
Log to .sb-pentest-audit.log BEFORE and AFTER each action
DO NOT wait until the skill completes to update files
If the skill crashes or is interrupted, all prior findings must already be saved

This is not optional. Failure to write progressively is a critical error.

This skill determines whether a web application uses Supabase as its backend.

When to Use This Skill
Starting a security audit on an unknown application
Verifying Supabase usage before running other audit skills
Quickly checking multiple applications for Supabase presence
Prerequisites
Target URL must be publicly accessible
Internet connection to fetch and analyze the target
Detection Methods

The skill uses multiple detection vectors:

1. Domain Pattern Matching

Searches for Supabase-related domains in:

HTML source code
JavaScript bundles
Network requests (via inline scripts)

Patterns detected:

*.supabase.co
*.supabase.com
supabase-cdn.com

2. JavaScript Client Detection

Looks for Supabase client library signatures:

// Import patterns
import { createClient } from '@supabase/supabase-js'
const { createClient } = require('@supabase/supabase-js')

// Client initialization
supabase.createClient(
createClient('https://
SUPABASE_URL
NEXT_PUBLIC_SUPABASE
VITE_SUPABASE
REACT_APP_SUPABASE

3. API Endpoint Detection

Checks for characteristic Supabase endpoints:

/rest/v1/
/auth/v1/
/storage/v1/
/realtime/v1/
/functions/v1/

4. Response Header Analysis

Looks for Supabase-specific headers:

x-supabase-*
sb-*

Usage
Basic Detection
Check if https://myapp.example.com uses Supabase

Detection with Verbose Output
Detect Supabase on https://myapp.example.com with full details

Output Format
Supabase Detected
═══════════════════════════════════════════════════════════
 SUPABASE DETECTED
═══════════════════════════════════════════════════════════

 Target: https://myapp.example.com
 Status: ✅ Supabase usage confirmed

 Detection Evidence:
 ├── Domain: abc123def.supabase.co (found in main.js)
 ├── Client: @supabase/supabase-js v2.x detected
 ├── Endpoints: /rest/v1/, /auth/v1/, /storage/v1/
 └── Headers: x-supabase-api-version present

 Project Reference: abc123def
 Project URL: https://abc123def.supabase.co

 Context saved to: .sb-pentest-context.json
═══════════════════════════════════════════════════════════

Supabase Not Detected
═══════════════════════════════════════════════════════════
 DETECTION RESULT
═══════════════════════════════════════════════════════════

 Target: https://myapp.example.com
 Status: ❌ Supabase not detected

 Scanned:
 ├── HTML source: No Supabase patterns
 ├── JavaScript bundles: 3 files analyzed, no matches
 ├── Network patterns: No Supabase endpoints
 └── Response headers: No Supabase headers

 Note: The app may use a self-hosted Supabase or custom domain.
       Try providing a known Supabase URL manually if you have one.
═══════════════════════════════════════════════════════════

Context Output

When Supabase is detected, the skill saves to .sb-pentest-context.json:

{
  "target_url": "https://myapp.example.com",
  "detection": {
    "detected": true,
    "confidence": "high",
    "timestamp": "2025-01-31T10:00:00Z",
    "evidence": [
      {
        "type": "domain",
        "value": "abc123def.supabase.co",
        "location": "/static/js/main.js",
        "line": 1247
      },
      {
        "type": "client_library",
        "value": "@supabase/supabase-js",
        "version": "2.x"
      }
    ]
  },
  "supabase": {
    "project_ref": "abc123def",
    "project_url": "https://abc123def.supabase.co"
  }
}

Audit Log Entry

Each detection is logged to .sb-pentest-audit.log:

[2025-01-31T10:00:00Z] DETECTION_START target=https://myapp.example.com
[2025-01-31T10:00:01Z] FETCH_HTML status=200 size=45KB
[2025-01-31T10:00:02Z] FETCH_JS file=main.js status=200 size=1.2MB
[2025-01-31T10:00:03Z] PATTERN_MATCH type=domain value=abc123def.supabase.co
[2025-01-31T10:00:03Z] DETECTION_COMPLETE result=detected confidence=high

Confidence Levels
Level	Criteria
High	Multiple evidence types (domain + client + endpoints)
Medium	Single strong evidence (domain or explicit client init)
Low	Only indirect evidence (generic patterns, possible false positive)
Edge Cases
Custom Domains

Some Supabase projects use custom domains (e.g., api.mycompany.com). In this case:

Detect Supabase on https://myapp.com with custom API domain api.mycompany.com

Self-Hosted Supabase

Self-hosted instances won't have .supabase.co domains. Look for:

PostgREST patterns (/rest/v1/)
GoTrue auth patterns (/auth/v1/)
Supabase client library in code
Single Page Applications

For SPAs with lazy-loaded chunks:

Detect Supabase on https://myapp.com including all JS chunks

Common Issues

❌ Problem: Detection returns false negative on SPA ✅ Solution: The app may lazy-load Supabase. Try interacting with the app first to load all chunks, or provide known patterns.

❌ Problem: Multiple Supabase projects detected ✅ Solution: This can happen with multi-tenant setups. The skill will list all found projects.

❌ Problem: Detection is slow ✅ Solution: Large JS bundles take time to analyze. Use --quick mode for faster but less thorough detection:

Quick detect Supabase on https://myapp.com

Next Steps

After detection:

Run supabase-extract-url to confirm and extract the project URL
Run supabase-extract-anon-key to find the API key
Or use supabase-pentest for a full guided audit
MANDATORY: Progressive Context File Updates

⚠️ This skill MUST update tracking files PROGRESSIVELY during execution, NOT just at the end.

Critical Rule: Write As You Go

DO NOT batch all writes at the end. Instead:

Before starting any action → Log the action to .sb-pentest-audit.log
After each discovery → Immediately update .sb-pentest-context.json
After each significant step → Log completion to .sb-pentest-audit.log

This ensures that if the skill is interrupted, crashes, or times out, all findings up to that point are preserved.

Required Actions (Progressive)

Create/Update .sb-pentest-context.json with results:

{
  "target_url": "https://myapp.example.com",
  "detection": {
    "detected": true,
    "confidence": "high",
    "timestamp": "...",
    "evidence": [ ... ]
  },
  "supabase": {
    "project_ref": "abc123def",
    "project_url": "https://abc123def.supabase.co"
  }
}


Create/Log to .sb-pentest-audit.log:

[TIMESTAMP] [supabase-detect] [START] Starting Supabase detection
[TIMESTAMP] [supabase-detect] [SUCCESS] Supabase detected with high confidence
[TIMESTAMP] [supabase-detect] [CONTEXT_UPDATED] .sb-pentest-context.json created/updated


IMPORTANT: As the first skill in the audit chain, this skill is responsible for creating the context files if they don't exist.

FAILURE TO UPDATE CONTEXT FILES IS NOT ACCEPTABLE.

MANDATORY: Evidence Collection

📁 Evidence Directory: .sb-pentest-evidence/01-detection/

Evidence Files to Create
File	Content
initial-scan.json	Raw detection results with all evidence
supabase-endpoints.txt	List of discovered Supabase endpoints
client-code-snippets/	Directory with relevant code excerpts
Evidence Format
{
  "evidence_id": "DET-001",
  "timestamp": "2025-01-31T10:00:00Z",
  "category": "detection",
  "target_url": "https://myapp.example.com",

  "detection_results": {
    "supabase_detected": true,
    "confidence": "high",
    "project_url": "https://abc123def.supabase.co",
    "project_ref": "abc123def"
  },

  "evidence": [
    {
      "type": "domain_pattern",
      "value": "abc123def.supabase.co",
      "location": "/static/js/main.js",
      "line": 1247,
      "context": "const SUPABASE_URL = 'https://abc123def.supabase.co'"
    },
    {
      "type": "client_library",
      "value": "@supabase/supabase-js",
      "version": "2.x"
    }
  ],

  "curl_command": "curl -s 'https://abc123def.supabase.co/rest/v1/' -H 'apikey: [ANON_KEY]'"
}

Add to curl-commands.sh
# === DETECTION ===
# Check Supabase API availability
curl -s "$SUPABASE_URL/rest/v1/" -H "apikey: $ANON_KEY" | head -100

Add to timeline.md
## [TIMESTAMP] - Detection Phase Complete
- Supabase detected with [confidence] confidence
- Project: [project_ref]
- Evidence: `01-detection/initial-scan.json`

Related Skills
supabase-extract-url — Extract project URL from code
supabase-extract-anon-key — Find anon key
supabase-pentest — Full orchestrated audit
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