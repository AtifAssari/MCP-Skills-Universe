---
rating: ⭐⭐⭐
title: repomix-safe-mixer
url: https://skills.sh/daymade/claude-code-skills/repomix-safe-mixer
---

# repomix-safe-mixer

skills/daymade/claude-code-skills/repomix-safe-mixer
repomix-safe-mixer
Installation
$ npx skills add https://github.com/daymade/claude-code-skills --skill repomix-safe-mixer
SKILL.md
Repomix Safe Mixer
Overview

Safely package codebases with repomix by automatically detecting and removing hardcoded credentials.

This skill prevents accidental credential exposure when packaging code with repomix. It scans for hardcoded secrets (API keys, database credentials, tokens), reports findings, and ensures safe packaging.

When to use: When packaging code with repomix for distribution, creating shareable reference packages, or whenever security concerns exist about hardcoded credentials in code.

Core Workflow
Standard Safe Packaging

Use safe_pack.py from this skill's scripts/ directory for the complete workflow: scan → report → pack.

python3 scripts/safe_pack.py <directory>


What it does:

Scans directory for hardcoded credentials
Reports findings with file/line details
Blocks packaging if secrets found
Packs with repomix only if scan is clean

Example:

python3 scripts/safe_pack.py ./my-project


Output if clean:

🔍 Scanning ./my-project for hardcoded secrets...
✅ No secrets detected!
📦 Packing ./my-project with repomix...
✅ Packaging complete!
   Package is safe to distribute.


Output if secrets found:

🔍 Scanning ./my-project for hardcoded secrets...
⚠️  Security Scan Found 3 Potential Secrets:

🔴 supabase_url: 1 instance(s)
   - src/client.ts:5
     Match: https://ghyttjckzmzdxumxcixe.supabase.co

❌ Cannot pack: Secrets detected!

Options

Custom output file:

python3 scripts/safe_pack.py \
  ./my-project \
  --output package.xml


With repomix config:

python3 scripts/safe_pack.py \
  ./my-project \
  --config repomix.config.json


Exclude patterns from scanning:

python3 scripts/safe_pack.py \
  ./my-project \
  --exclude '.*test.*' '.*\.example'


Force pack (dangerous, skip scan):

python3 scripts/safe_pack.py \
  ./my-project \
  --force  # ⚠️ NOT RECOMMENDED

Standalone Secret Scanning

Use scan_secrets.py from this skill's scripts/ directory for scanning only (without packing).

python3 scripts/scan_secrets.py <directory>


Use cases:

Verify cleanup after removing credentials
Pre-commit security checks
Audit existing codebases

Example:

python3 scripts/scan_secrets.py ./my-project


JSON output for programmatic use:

python3 scripts/scan_secrets.py \
  ./my-project \
  --json


Exclude patterns:

python3 scripts/scan_secrets.py \
  ./my-project \
  --exclude '.*test.*' '.*example.*' '.*SECURITY_AUDIT\.md'

Detected Secret Types

The scanner detects common credential patterns including:

Cloud Providers:

AWS Access Keys (AKIA...)
Cloudflare R2 Account IDs and Access Keys
Supabase Project URLs and Anon Keys

API Keys:

Stripe Keys (sk_live_..., pk_live_...)
OpenAI API Keys (sk-...)
Google Gemini API Keys (AIza...)
Generic API Keys

Authentication:

JWT Tokens (eyJ...)
OAuth Client Secrets
Private Keys (-----BEGIN PRIVATE KEY-----)
Turnstile Keys (0x...)

See references/common_secrets.md for complete list and patterns.

Handling Detected Secrets

When secrets are found:

Step 1: Review Findings

Examine each finding to verify it's a real credential (not a placeholder or example).

Step 2: Replace with Environment Variables

Before:

const SUPABASE_URL = "https://ghyttjckzmzdxumxcixe.supabase.co";
const API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...";


After:

const SUPABASE_URL = import.meta.env.VITE_SUPABASE_URL || "https://your-project-ref.supabase.co";
const API_KEY = import.meta.env.VITE_API_KEY || "your-api-key-here";

// Validation
if (!import.meta.env.VITE_SUPABASE_URL) {
  console.error("⚠️ Missing VITE_SUPABASE_URL environment variable");
}

Step 3: Create .env.example
# Example environment variables
VITE_SUPABASE_URL=https://your-project-ref.supabase.co
VITE_API_KEY=your-api-key-here

# Instructions:
# 1. Copy this file to .env
# 2. Replace placeholders with real values
# 3. Never commit .env to version control

Step 4: Verify Cleanup

Run scanner again to confirm secrets removed:

python3 scripts/scan_secrets.py ./my-project

Step 5: Safe Pack

Once clean, package safely:

python3 scripts/safe_pack.py ./my-project

Post-Exposure Actions

If credentials were already exposed (e.g., committed to git, shared publicly):

Rotate credentials immediately - Generate new keys/tokens
Revoke old credentials - Disable compromised credentials
Audit usage - Check logs for unauthorized access
Monitor - Set up alerts for unusual activity
Update deployment - Deploy code with new credentials
Document incident - Record what was exposed and actions taken
Common False Positives

The scanner skips common false positives:

Placeholders:

your-api-key, example-key, placeholder-value
<YOUR_API_KEY>, ${API_KEY}, TODO: add key

Test/Example files:

Files matching .*test.*, .*example.*, .*sample.*

Comments:

Lines starting with //, #, /*, *

Environment variable references (correct usage):

process.env.API_KEY
import.meta.env.VITE_API_KEY
Deno.env.get('API_KEY')

Use --exclude to skip additional patterns if needed.

Integration with Repomix

This skill works with standard repomix:

Default usage (no config):

python3 scripts/safe_pack.py ./project


With repomix config:

python3 scripts/safe_pack.py \
  ./project \
  --config repomix.config.json


Custom output location:

python3 scripts/safe_pack.py \
  ./project \
  --output ~/Downloads/package-clean.xml


The skill runs repomix internally after security validation, passing through config and output options.

Example Workflows
Workflow 1: Package a Clean Project
# Scan and pack in one command
python3 scripts/safe_pack.py \
  ~/workspace/my-project \
  --output ~/Downloads/my-project-package.xml

Workflow 2: Clean and Package a Project with Secrets
# Step 1: Scan to discover secrets
python3 scripts/scan_secrets.py ~/workspace/my-project

# Step 2: Review findings and replace credentials with env vars
# (Edit files manually or with automation)

# Step 3: Verify cleanup
python3 scripts/scan_secrets.py ~/workspace/my-project

# Step 4: Package safely
python3 scripts/safe_pack.py \
  ~/workspace/my-project \
  --output ~/Downloads/my-project-clean.xml

Workflow 3: Audit Before Commit
# Pre-commit hook: scan for secrets
python3 scripts/scan_secrets.py . --json

# Exit code 1 if secrets found (blocks commit)
# Exit code 0 if clean (allows commit)

Resources

References:

references/common_secrets.md - Complete credential pattern catalog

Scripts:

scripts/scan_secrets.py - Standalone security scanner
scripts/safe_pack.py - Complete scan → pack workflow

Related Skills:

repomix-unmixer - Extracts files from repomix packages
skill-creator - Creates new Claude Code skills
Security Note

This skill detects common patterns but may not catch all credential types. Always:

Review findings manually
Rotate exposed credentials
Use .env.example templates
Validate environment variables
Monitor for unauthorized access

Not a replacement for: Secret scanning in CI/CD, git history scanning, or comprehensive security audits.

Weekly Installs
248
Repository
daymade/claude-…e-skills
GitHub Stars
968
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail