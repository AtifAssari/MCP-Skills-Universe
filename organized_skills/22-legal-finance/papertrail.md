---
rating: ⭐⭐⭐
title: papertrail
url: https://skills.sh/jwmossmoz/agent-skills/papertrail
---

# papertrail

skills/jwmossmoz/agent-skills/papertrail
papertrail
Installation
$ npx skills add https://github.com/jwmossmoz/agent-skills --skill papertrail
SKILL.md
SolarWinds Observability Logs (paperctl)

Query and download logs from SolarWinds Observability (formerly Papertrail) using paperctl v2.0.

Prerequisites

Requires SWO_API_TOKEN environment variable or ~/.config/paperctl/config.toml.

Initialize config interactively:

paperctl config init

Commands
Pull logs from a system

Download all logs for a system to ~/.cache/paperctl/logs/<system>.txt:

paperctl pull <system-name>


Partial name matching is supported. Use Taskcluster worker IDs directly:

# Matches vm-abc123def.reddog.microsoft.com
paperctl pull vm-abc123def


Pull with time range:

paperctl pull vm-abc123 --since -24h
paperctl pull vm-abc123 --since "2026-01-29T00:00:00" --until "2026-01-29T12:00:00"


Pull to specific location:

paperctl pull vm-abc123 --output ~/logs/worker.txt
paperctl pull vm-abc123 --output ~/logs/  # Uses system name as filename


Pull multiple systems in parallel:

paperctl pull vm-abc,vm-def,vm-ghi --output ~/logs/

Search logs

Search across all systems:

paperctl search "error" --since -1h
paperctl search "error AND timeout" --since -24h --limit 100


Search specific system:

paperctl search "error" --system vm-abc123 --since -1h


Save search results to file:

paperctl search "error" --since -1h --file errors.txt

List entities (hosts)
paperctl entities list
paperctl entities list --type Host --output json
paperctl entities list --name web-1

Show entity details
paperctl entities show <entity-id>
paperctl entities show <entity-id> --output json

List available entity types
paperctl entities list-types

View configuration
paperctl config show

Query syntax

SWO search uses text matching with boolean operators. No regex or wildcards.

Operator	Example
AND	error AND timeout
OR	error OR warning
NOT	error NOT debug
Exact phrase	"connection refused"
Time formats
Format	Example
Relative	-1h, -24h, -7d, 2 hours ago
ISO timestamp	2026-01-29T00:00:00Z
Natural language	yesterday, last week
Output formats

Use --format to change output:

paperctl pull vm-abc123 --format json
paperctl pull vm-abc123 --format csv
paperctl search "error" --output json

Common workflows
Download Taskcluster worker logs

Get worker IDs from Taskcluster, then pull logs:

# Get recent workers from a pool
curl -s "https://firefox-ci-tc.services.mozilla.com/api/worker-manager/v1/workers/gecko-t%2Fwin11-64-24h2-alpha" | \
  jq -r '.workers | sort_by(.created) | reverse | .[0:3] | .[].workerId'

# Pull logs using partial worker ID
paperctl pull vm-abc123def

Search for errors across workers
paperctl search "error" --since -1h --file errors.txt

Investigate specific timeframe
paperctl pull vm-abc123 --since "2026-01-29T10:00:00" --until "2026-01-29T11:00:00" --output incident.txt

Migration from v1.x

v2.0 switched from Papertrail API to SolarWinds Observability API:

v1.x	v2.0
PAPERTRAIL_API_TOKEN	SWO_API_TOKEN
paperctl systems list	paperctl entities list
paperctl groups list	Removed (not in SWO API)
paperctl archives list	Removed (not in SWO API)
--group option on search	Removed
System IDs (integers)	Entity IDs (strings)
Weekly Installs
13
Repository
jwmossmoz/agent-skills
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn