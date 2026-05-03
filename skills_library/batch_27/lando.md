---
title: lando
url: https://skills.sh/jwmossmoz/agent-skills/lando
---

# lando

skills/jwmossmoz/agent-skills/lando
lando
Installation
$ npx skills add https://github.com/jwmossmoz/agent-skills --skill lando
SKILL.md
Lando

Check the status of Mozilla Lando landing jobs using the public API.

Usage
# Check landing job status
curl -s "https://lando.services.mozilla.com/api/v1/landing_jobs/<JOB_ID>" | jq

# Example
curl -s "https://lando.services.mozilla.com/api/v1/landing_jobs/173397" | jq

# Check only the status field
curl -s "https://lando.services.mozilla.com/api/v1/landing_jobs/173397" | jq -r '.status'

# Poll every 90 seconds until landed or failed
JOB_ID=173397
while true; do
  STATUS=$(curl -s "https://lando.services.mozilla.com/api/v1/landing_jobs/$JOB_ID" | jq -r '.status')
  echo "$(date): $STATUS"
  [[ "$STATUS" == "landed" || "$STATUS" == "failed" ]] && break
  sleep 90
done

API Response

The API returns a JSON object with these key fields:

Field	Description
status	Job status: submitted, in_progress, landed, failed
error	Error message if status is failed
landed_commit_id	Commit hash if successfully landed
created_at	When the job was submitted
updated_at	Last status update time
Common Statuses
submitted - Job is queued
in_progress - Currently being processed
landed - Successfully landed to the repository
failed - Landing failed (check error field)
Prerequisites

None - the API is publicly accessible. No authentication required for read operations.

Documentation
Lando Service: https://lando.services.mozilla.com/
API Base: https://lando.services.mozilla.com/api/v1/
Mozilla Conduit Documentation: https://moz-conduit.readthedocs.io/
Source Code: https://github.com/mozilla-conduit/lando-api
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
SnykPass