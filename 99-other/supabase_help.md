---
title: supabase-help
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-help
---

# supabase-help

skills/yoanbernabeu/supabase-pentest-skills/supabase-help
supabase-help
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-help
SKILL.md
Supabase Pentest Skills Help

Quick reference for all 24 security audit skills.

When to Use This Skill
Need a quick overview of available skills
Looking for the right skill for a specific task
Want usage examples for a particular skill
Quick Start
# Full guided audit
/supabase-pentest https://myapp.example.com

# Check if app uses Supabase
/supabase-detect https://myapp.example.com

# Generate report from previous audit
/supabase-report

All Skills Reference
Orchestration
Skill	Command	Purpose
supabase-pentest	/supabase-pentest <url>	Full guided security audit
supabase-evidence	/supabase-evidence	Initialize evidence collection
supabase-help	/supabase-help	This help reference
Detection
Skill	Command	Purpose
supabase-detect	/supabase-detect <url>	Detect Supabase usage
Extraction
Skill	Command	Purpose
supabase-extract-url	/supabase-extract-url <url>	Find Supabase project URL
supabase-extract-anon-key	/supabase-extract-anon-key	Extract anon API key
supabase-extract-service-key	/supabase-extract-service-key	Find leaked service key
supabase-extract-jwt	/supabase-extract-jwt	Extract JWTs from code
supabase-extract-db-string	/supabase-extract-db-string	Find DB connection strings
API Audit
Skill	Command	Purpose
supabase-audit-tables-list	/supabase-audit-tables-list	List exposed tables
supabase-audit-tables-read	/supabase-audit-tables-read	Read table data
supabase-audit-rls	/supabase-audit-rls	Test RLS policies
supabase-audit-rpc	/supabase-audit-rpc	Test RPC functions
Storage Audit
Skill	Command	Purpose
supabase-audit-buckets-list	/supabase-audit-buckets-list	List storage buckets
supabase-audit-buckets-read	/supabase-audit-buckets-read	Read bucket files
supabase-audit-buckets-public	/supabase-audit-buckets-public	Find public buckets
Auth Audit
Skill	Command	Purpose
supabase-audit-auth-config	/supabase-audit-auth-config	Check auth settings
supabase-audit-auth-signup	/supabase-audit-auth-signup	Test signup access
supabase-audit-auth-users	/supabase-audit-auth-users	Test user enumeration
supabase-audit-authenticated	/supabase-audit-authenticated	Create test user to detect IDOR
Realtime & Functions
Skill	Command	Purpose
supabase-audit-realtime	/supabase-audit-realtime	Test Realtime channels
supabase-audit-functions	/supabase-audit-functions	Test Edge Functions
Reporting
Skill	Command	Purpose
supabase-report	/supabase-report	Generate Markdown report
supabase-report-compare	/supabase-report-compare <old> <new>	Compare two reports
Severity Levels
Level	Color	Description
P0	🔴	Critical: data exposure, user data, privilege escalation
P1	🟠	High: sensitive data, security misconfiguration
P2	🟡	Medium: minor exposure, best practice violations
Common Workflows
Quick Security Check
1. /supabase-detect https://myapp.com
2. /supabase-extract-anon-key
3. /supabase-audit-rls
4. /supabase-report

Full Audit
1. /supabase-pentest https://myapp.com
   (Follow guided prompts through all phases)

Storage-Only Audit
1. /supabase-detect https://myapp.com
2. /supabase-audit-buckets-list
3. /supabase-audit-buckets-public
4. /supabase-report

Compare After Fixes
1. Copy previous report to reports/audit-v1.md
2. Run new audit: /supabase-pentest https://myapp.com
3. /supabase-report-compare reports/audit-v1.md supabase-audit-report.md

Files and Directories Created
File/Directory	Description
.sb-pentest-context.json	Shared context between skills
.sb-pentest-audit.log	Action log with timestamps
.sb-pentest-evidence/	Evidence directory for professional audits
supabase-audit-report.md	Final security report
Evidence Directory Structure
.sb-pentest-evidence/
├── README.md                 # Evidence index
├── curl-commands.sh          # Reproducible commands
├── timeline.md               # Chronological findings
├── 01-detection/             # Detection evidence
├── 02-extraction/            # Key extraction evidence
├── 03-api-audit/             # API audit evidence
├── 04-storage-audit/         # Storage audit evidence
├── 05-auth-audit/            # Auth audit evidence
├── 06-realtime-audit/        # Realtime audit evidence
├── 07-functions-audit/       # Functions audit evidence
└── screenshots/              # Optional screenshots

Tips
Always run detection first — Most skills auto-invoke it, but it's faster to run explicitly
Check the context file — If a skill behaves unexpectedly, the context may have stale data
Use the orchestrator for full audits — It handles dependencies automatically
Save reports with dates — Rename supabase-audit-report.md to include the date for history
Need More Help?
Each skill has detailed documentation — run /supabase-<skill-name> for specifics
Check the README at the repository root
Open an issue on GitHub for bugs or feature requests
Weekly Installs
166
Repository
yoanbernabeu/su…t-skills
GitHub Stars
37
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail