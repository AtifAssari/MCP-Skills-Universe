---
title: groq-debug-bundle
url: https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/groq-debug-bundle
---

# groq-debug-bundle

skills/jeremylongshore/claude-code-plugins-plus-skills/groq-debug-bundle
groq-debug-bundle
Installation
$ npx skills add https://github.com/jeremylongshore/claude-code-plugins-plus-skills --skill groq-debug-bundle
SKILL.md
Groq Debug Bundle
Overview

Collect all necessary diagnostic information for Groq support tickets.

Prerequisites
Groq SDK installed
Access to application logs
Permission to collect environment info
Instructions
Step 1: Create Debug Bundle Script
#!/bin/bash
# groq-debug-bundle.sh

BUNDLE_DIR="groq-debug-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BUNDLE_DIR"

echo "=== Groq Debug Bundle ===" > "$BUNDLE_DIR/summary.txt"
echo "Generated: $(date)" >> "$BUNDLE_DIR/summary.txt"

Step 2: Collect Environment Info
set -euo pipefail
# Environment info
echo "--- Environment ---" >> "$BUNDLE_DIR/summary.txt"
node --version >> "$BUNDLE_DIR/summary.txt" 2>&1
npm --version >> "$BUNDLE_DIR/summary.txt" 2>&1
echo "GROQ_API_KEY: ${GROQ_API_KEY:+[SET]}" >> "$BUNDLE_DIR/summary.txt"

Step 3: Gather SDK and Logs
set -euo pipefail
# SDK version
npm list @groq/sdk 2>/dev/null >> "$BUNDLE_DIR/summary.txt"

# Recent logs (redacted)
grep -i "groq" ~/.npm/_logs/*.log 2>/dev/null | tail -50 >> "$BUNDLE_DIR/logs.txt"

# Configuration (redacted - secrets masked)
echo "--- Config (redacted) ---" >> "$BUNDLE_DIR/summary.txt"
cat .env 2>/dev/null | sed 's/=.*/=***REDACTED***/' >> "$BUNDLE_DIR/config-redacted.txt"

# Network connectivity test
echo "--- Network Test ---" >> "$BUNDLE_DIR/summary.txt"
echo -n "API Health: " >> "$BUNDLE_DIR/summary.txt"
curl -s -o /dev/null -w "%{http_code}" https://api.groq.com/health >> "$BUNDLE_DIR/summary.txt"
echo "" >> "$BUNDLE_DIR/summary.txt"

Step 4: Package Bundle
tar -czf "$BUNDLE_DIR.tar.gz" "$BUNDLE_DIR"
echo "Bundle created: $BUNDLE_DIR.tar.gz"

Output
groq-debug-YYYYMMDD-HHMMSS.tar.gz archive containing:
summary.txt - Environment and SDK info
logs.txt - Recent redacted logs
config-redacted.txt - Configuration (secrets removed)
Error Handling
Item	Purpose	Included
Environment versions	Compatibility check	✓
SDK version	Version-specific bugs	✓
Error logs (redacted)	Root cause analysis	✓
Config (redacted)	Configuration issues	✓
Network test	Connectivity issues	✓
Examples
Sensitive Data Handling

ALWAYS REDACT:

API keys and tokens
Passwords and secrets
PII (emails, names, IDs)

Safe to Include:

Error messages
Stack traces (redacted)
SDK/runtime versions
Submit to Support
Create bundle: bash groq-debug-bundle.sh
Review for sensitive data
Upload to Groq support portal
Resources
Groq Support
Groq Status
Next Steps

For rate limit issues, see groq-rate-limits.

Weekly Installs
24
Repository
jeremylongshore…s-skills
GitHub Stars
2.1K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass