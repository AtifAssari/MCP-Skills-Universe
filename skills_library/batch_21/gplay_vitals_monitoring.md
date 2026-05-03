---
title: gplay-vitals-monitoring
url: https://skills.sh/tamtom/gplay-cli-skills/gplay-vitals-monitoring
---

# gplay-vitals-monitoring

skills/tamtom/gplay-cli-skills/gplay-vitals-monitoring
gplay-vitals-monitoring
Installation
$ npx skills add https://github.com/tamtom/gplay-cli-skills --skill gplay-vitals-monitoring
SKILL.md
App Vitals Monitoring

Use this skill when you need to monitor app stability, performance, and errors from Google Play Console.

Preconditions
Ensure credentials are set (gplay auth login or GPLAY_SERVICE_ACCOUNT env var).
Service account needs "View app information and download bulk reports" permission.
App must have active installs generating vitals data.
Crash Monitoring
List crash clusters
gplay vitals crashes list \
  --package com.example.app

Get crash cluster details
gplay vitals crashes get \
  --package com.example.app \
  --cluster-id CLUSTER_ID

Filter by time range
gplay vitals crashes list \
  --package com.example.app \
  --start-time 2026-01-01T00:00:00Z \
  --end-time 2026-02-01T00:00:00Z

Filter by version code
gplay vitals crashes list \
  --package com.example.app \
  --version-code 42

Filter by app version name
gplay vitals crashes list \
  --package com.example.app \
  --version-name "1.2.0"

Paginate through all crash clusters
gplay vitals crashes list \
  --package com.example.app \
  --paginate

Output as table for readability
gplay vitals crashes list \
  --package com.example.app \
  --output table

ANR Monitoring
List ANR clusters
gplay vitals crashes list \
  --package com.example.app \
  --type anr

Get ANR cluster details
gplay vitals crashes get \
  --package com.example.app \
  --cluster-id CLUSTER_ID \
  --type anr

Performance Metrics
Get performance overview
gplay vitals performance overview \
  --package com.example.app

Startup time metrics
gplay vitals performance startup \
  --package com.example.app

Filter by device type
gplay vitals performance overview \
  --package com.example.app \
  --device-type phone

Filter by OS version
gplay vitals performance overview \
  --package com.example.app \
  --os-version 14

Rendering metrics (slow/frozen frames)
gplay vitals performance rendering \
  --package com.example.app

Battery metrics
gplay vitals performance battery \
  --package com.example.app

Permission denials
gplay vitals performance permissions \
  --package com.example.app

Error Reporting
List error clusters
gplay vitals errors list \
  --package com.example.app

Get error details
gplay vitals errors get \
  --package com.example.app \
  --error-id ERROR_ID

Filter errors by severity
gplay vitals errors list \
  --package com.example.app \
  --severity critical

Filter errors by time range
gplay vitals errors list \
  --package com.example.app \
  --start-time 2026-01-01T00:00:00Z \
  --end-time 2026-02-01T00:00:00Z

Common Flags
Flag	Description
--package	App package name (required)
--start-time	Start of time range (RFC 3339)
--end-time	End of time range (RFC 3339)
--version-code	Filter by version code
--version-name	Filter by version name
--type	Event type (crash, anr)
--output	Output format (json, table, markdown)
--paginate	Fetch all pages
--pretty	Pretty-print JSON output
Workflow Examples
Daily stability check
# Check crash rate for the latest version
gplay vitals crashes list \
  --package com.example.app \
  --version-name "2.1.0" \
  --output table

# Check ANR rate
gplay vitals crashes list \
  --package com.example.app \
  --version-name "2.1.0" \
  --type anr \
  --output table

# Review performance
gplay vitals performance overview \
  --package com.example.app \
  --output table

Investigate a crash spike
# 1. List top crash clusters
gplay vitals crashes list \
  --package com.example.app \
  --start-time 2026-02-10T00:00:00Z \
  --output table

# 2. Get details for the top cluster
CLUSTER=$(gplay vitals crashes list \
  --package com.example.app \
  --start-time 2026-02-10T00:00:00Z | jq -r '.[0].clusterId')

gplay vitals crashes get \
  --package com.example.app \
  --cluster-id $CLUSTER \
  --pretty

# 3. Check if it's version-specific
gplay vitals crashes list \
  --package com.example.app \
  --version-code 105 \
  --output table

CI/CD stability gate
# Check if crash rate exceeds threshold before promoting
CRASH_COUNT=$(gplay vitals crashes list \
  --package com.example.app \
  --version-name "$VERSION" | jq 'length')

if [ "$CRASH_COUNT" -gt 10 ]; then
  echo "Too many crash clusters ($CRASH_COUNT). Halting promotion."
  exit 1
fi

gplay promote \
  --package com.example.app \
  --from beta \
  --to production \
  --rollout 10

Best Practices
Monitor after every release - Check vitals within 24-48 hours of rollout.
Upload deobfuscation files - Ensure crash stack traces are readable.
Set up CI stability gates - Block promotion when crash rates exceed thresholds.
Track ANRs separately - ANRs impact Play Store ranking more than crashes.
Compare across versions - Filter by version code to detect regressions.
Use JSON output in scripts - Parse with jq for automated monitoring.
Weekly Installs
76
Repository
tamtom/gplay-cli-skills
GitHub Stars
33
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass