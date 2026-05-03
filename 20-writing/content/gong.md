---
rating: ⭐⭐
title: gong
url: https://skills.sh/jdrhyne/agent-skills/gong
---

# gong

skills/jdrhyne/agent-skills/gong
gong
Installation
$ npx skills add https://github.com/jdrhyne/agent-skills --skill gong
SKILL.md
Gong

Access Gong conversation intelligence - calls, transcripts, users, and analytics.

Setup

Store credentials in ~/.config/gong/credentials.json:

{
  "base_url": "https://us-XXXXX.api.gong.io",
  "access_key": "YOUR_ACCESS_KEY",
  "secret_key": "YOUR_SECRET_KEY"
}


Get credentials from Gong: Settings → Ecosystem → API → Create API Key.

Authentication
GONG_CREDS=~/.config/gong/credentials.json
GONG_BASE=$(jq -r '.base_url' $GONG_CREDS)
GONG_AUTH=$(jq -r '"\(.access_key):\(.secret_key)"' $GONG_CREDS | base64)

curl -s "$GONG_BASE/v2/endpoint" \
  -H "Authorization: Basic $GONG_AUTH" \
  -H "Content-Type: application/json"

Safety Boundaries
Do not print raw access keys, secret keys, or full Authorization headers in chat output.
Do not call Gong endpoints other than the configured tenant base URL.
Do not export full transcripts or account data unless the user asked for that exact scope.
Do not persist Gong credentials anywhere outside the documented local config file.
Core Operations
List Users
curl -s "$GONG_BASE/v2/users" -H "Authorization: Basic $GONG_AUTH" | \
  jq '[.users[] | {id, email: .emailAddress, name: "\(.firstName) \(.lastName)"}]'

List Calls (with date range)
curl -s -X POST "$GONG_BASE/v2/calls/extensive" \
  -H "Authorization: Basic $GONG_AUTH" \
  -H "Content-Type: application/json" \
  -d '{
    "filter": {
      "fromDateTime": "2025-01-01T00:00:00Z",
      "toDateTime": "2025-01-31T23:59:59Z"
    },
    "contentSelector": {}
  }' | jq '{
    total: .records.totalRecords,
    calls: [.calls[] | {
      id: .metaData.id,
      title: .metaData.title,
      started: .metaData.started,
      duration_min: ((.metaData.duration // 0) / 60 | floor),
      url: .metaData.url
    }]
  }'

Get Call Transcript
curl -s -X POST "$GONG_BASE/v2/calls/transcript" \
  -H "Authorization: Basic $GONG_AUTH" \
  -H "Content-Type: application/json" \
  -d '{"filter": {"callIds": ["CALL_ID"]}}' | \
  jq '.callTranscripts[0].transcript[] | "\(.speakerName // "Speaker"): \(.sentences[].text)"' -r

Get Call Details
curl -s -X POST "$GONG_BASE/v2/calls/extensive" \
  -H "Authorization: Basic $GONG_AUTH" \
  -H "Content-Type: application/json" \
  -d '{
    "filter": {"callIds": ["CALL_ID"]},
    "contentSelector": {"exposedFields": {"content": true, "parties": true}}
  }' | jq '.calls[0]'

Activity Stats
curl -s -X POST "$GONG_BASE/v2/stats/activity/aggregate" \
  -H "Authorization: Basic $GONG_AUTH" \
  -H "Content-Type: application/json" \
  -d '{
    "filter": {
      "fromDateTime": "2025-01-01T00:00:00Z",
      "toDateTime": "2025-01-31T23:59:59Z"
    }
  }'

Endpoints Reference
Endpoint	Method	Use
/v2/users	GET	List users
/v2/calls/extensive	POST	List/filter calls
/v2/calls/transcript	POST	Get transcripts
/v2/stats/activity/aggregate	POST	Activity stats
/v2/meetings	GET	Scheduled meetings
Pagination

Responses include cursor for pagination:

{"records": {"totalRecords": 233, "cursor": "eyJ..."}}


Include cursor in next request: {"cursor": "eyJ..."}

Date Helpers
# Last 7 days
FROM=$(date -v-7d +%Y-%m-%dT00:00:00Z 2>/dev/null || date -d "7 days ago" +%Y-%m-%dT00:00:00Z)
TO=$(date +%Y-%m-%dT23:59:59Z)

Notes
Rate limit: ~3 requests/second
Call IDs are large integers as strings
Transcripts may take time to process after call ends
Date format: ISO 8601 (e.g., 2025-01-15T00:00:00Z)
Weekly Installs
21
Repository
jdrhyne/agent-skills
GitHub Stars
232
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass