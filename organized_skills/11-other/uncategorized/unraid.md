---
rating: ⭐⭐⭐
title: unraid
url: https://skills.sh/jmagar/claude-homelab/unraid
---

# unraid

skills/jmagar/claude-homelab/unraid
unraid
Installation
$ npx skills add https://github.com/jmagar/claude-homelab --skill unraid
SKILL.md
Unraid API Skill

⚠️ MANDATORY SKILL INVOCATION ⚠️

YOU MUST invoke this skill (NOT optional) when the user mentions ANY of these triggers:

"Unraid status", "disk health", "array status"
"Unraid containers", "VMs on Unraid", "Unraid logs"
"check Unraid", "Unraid monitoring", "server health"
Any mention of Unraid servers or system monitoring

Failure to invoke this skill when triggers occur violates your operational requirements.

Query and monitor Unraid servers using the GraphQL API. Access all 27 read-only endpoints for system monitoring, disk health, logs, containers, VMs, and more.

Quick Start

Set your Unraid server credentials:

export UNRAID_URL="https://your-unraid-server/graphql"
export UNRAID_API_KEY="your-api-key"


Get API Key: Settings → Management Access → API Keys → Create (select "Viewer" role)

Use the helper script for any query:

./scripts/unraid-query.sh -q "{ online }"


Or run example scripts:

./scripts/dashboard.sh              # Complete multi-server dashboard
./examples/disk-health.sh           # Disk temperatures & health
./examples/read-logs.sh syslog 20   # Read system logs

Core Concepts
GraphQL API Structure

Unraid 7.2+ uses GraphQL (not REST). Key differences:

Single endpoint: /graphql for all queries
Request exactly what you need: Specify fields in query
Strongly typed: Use introspection to discover fields
No container logs: Docker container output logs not accessible
Two Resources for Stats
info - Static hardware specs (CPU model, cores, OS version)
metrics - Real-time usage (CPU %, memory %, current load)

Always use metrics for monitoring, info for specifications.

Common Tasks
System Monitoring

Check if server is online:

./scripts/unraid-query.sh -q "{ online }"


Get CPU and memory usage:

./scripts/unraid-query.sh -q "{ metrics { cpu { percentTotal } memory { used total percentTotal } } }"


Complete dashboard:

./scripts/dashboard.sh

Disk Management

Check disk health and temperatures:

./examples/disk-health.sh


Get array status:

./scripts/unraid-query.sh -q "{ array { state parityCheckStatus { status progress errors } } }"


List all physical disks (including cache/USB):

./scripts/unraid-query.sh -q "{ disks { name } }"

Storage Shares

List network shares:

./scripts/unraid-query.sh -q "{ shares { name comment } }"

Logs

List available logs:

./scripts/unraid-query.sh -q "{ logFiles { name size modifiedAt } }"


Read log content:

./examples/read-logs.sh syslog 20

Containers & VMs

List Docker containers:

./scripts/unraid-query.sh -q "{ docker { containers { names image state status } } }"


List VMs:

./scripts/unraid-query.sh -q "{ vms { name state cpus memory } }"


Note: Container output logs are NOT accessible via API. Use docker logs via SSH.

Notifications

Get notification counts:

./scripts/unraid-query.sh -q "{ notifications { overview { unread { info warning alert total } } } }"

Helper Script Usage

The scripts/unraid-query.sh helper supports:

# Basic usage
./scripts/unraid-query.sh -u URL -k API_KEY -q "QUERY"

# Use environment variables
export UNRAID_URL="https://unraid.local/graphql"
export UNRAID_API_KEY="your-key"
./scripts/unraid-query.sh -q "{ online }"

# Format options
-f json    # Raw JSON (default)
-f pretty  # Pretty-printed JSON
-f raw     # Just the data (no wrapper)

Additional Resources
Reference Files

For detailed documentation, consult:

references/endpoints.md - Complete list of all 27 API endpoints
references/troubleshooting.md - Common errors and solutions
references/api-reference.md - Detailed field documentation
Helper Scripts
scripts/unraid-query.sh - Main GraphQL query tool
scripts/dashboard.sh - Automated multi-server inventory reporter
Quick Command Reference
# System status
./scripts/unraid-query.sh -q "{ online metrics { cpu { percentTotal } } }"

# Disk health
./examples/disk-health.sh

# Array status
./scripts/unraid-query.sh -q "{ array { state } }"

# Read logs
./examples/read-logs.sh syslog 20

# Complete dashboard
./scripts/dashboard.sh

# List shares
./scripts/unraid-query.sh -q "{ shares { name } }"

# List containers
./scripts/unraid-query.sh -q "{ docker { containers { names state } } }"

🔧 Agent Tool Usage Requirements

CRITICAL: When invoking scripts from this skill via the zsh-tool, ALWAYS use pty: true.

Without PTY mode, command output will not be visible even though commands execute successfully.

Correct invocation pattern:

<invoke name="mcp__plugin_zsh-tool_zsh-tool__zsh">
<parameter name="command">./skills/SKILL_NAME/scripts/SCRIPT.sh [args]</parameter>
<parameter name="pty">true</parameter>
</invoke>

Weekly Installs
24
Repository
jmagar/claude-homelab
GitHub Stars
37
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass