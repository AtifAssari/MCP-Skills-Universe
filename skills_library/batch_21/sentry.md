---
title: sentry
url: https://skills.sh/vm0-ai/vm0-skills/sentry
---

# sentry

skills/vm0-ai/vm0-skills/sentry
sentry
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill sentry
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name SENTRY_TOKEN or zero doctor check-connector --url https://sentry.io/api/0/organizations/ --method GET

Organizations
List Organizations
curl -s "https://sentry.io/api/0/organizations/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Get Organization
curl -s "https://sentry.io/api/0/organizations/<org-slug>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Projects
List Organization Projects
curl -s "https://sentry.io/api/0/organizations/<org-slug>/projects/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Get Project
curl -s "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Update Project
curl -s -X PUT "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"Updated Project Name\", \"slug\": \"updated-slug\"}"

Delete Project
curl -s -X DELETE "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Issues
List Organization Issues
curl -s "https://sentry.io/api/0/organizations/<org-slug>/issues/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"


Params: query (Sentry search syntax), sort (date/new/freq/priority), cursor, limit.

Search Issues

Use query param with Sentry search syntax and -G with --data-urlencode:

curl -s -G "https://sentry.io/api/0/organizations/<org-slug>/issues/" \
  --header "Authorization: Bearer $SENTRY_TOKEN" \
  --data-urlencode "query=is:unresolved level:error"


Common queries: is:unresolved, is:resolved, level:error, error.type:TypeError, assigned:me, first-release:1.0.0.

List Project Issues
curl -s "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/issues/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Get Issue
curl -s "https://sentry.io/api/0/organizations/<org-slug>/issues/<issue-id>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Resolve Issue
curl -s -X PUT "https://sentry.io/api/0/organizations/<org-slug>/issues/<issue-id>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"status\": \"resolved\"}"

Ignore Issue
curl -s -X PUT "https://sentry.io/api/0/organizations/<org-slug>/issues/<issue-id>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"status\": \"ignored\"}"

Unresolve Issue
curl -s -X PUT "https://sentry.io/api/0/organizations/<org-slug>/issues/<issue-id>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"status\": \"unresolved\"}"

Assign Issue
curl -s -X PUT "https://sentry.io/api/0/organizations/<org-slug>/issues/<issue-id>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"assignedTo\": \"user@example.com\"}"

Bulk Update Issues
curl -s -X PUT "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/issues/" \
  --header "Authorization: Bearer $SENTRY_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"status\": \"resolved\", \"id\": [\"<issue-id-1>\", \"<issue-id-2>\"]}"

Delete Issue
curl -s -X DELETE "https://sentry.io/api/0/organizations/<org-slug>/issues/<issue-id>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Events
List Issue Events
curl -s "https://sentry.io/api/0/organizations/<org-slug>/issues/<issue-id>/events/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

List Project Events
curl -s "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/events/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Get Event by ID
curl -s "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/events/<event-id>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Releases
List Releases
curl -s "https://sentry.io/api/0/organizations/<org-slug>/releases/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Get Release
curl -s "https://sentry.io/api/0/organizations/<org-slug>/releases/<version>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Create Release
curl -s -X POST "https://sentry.io/api/0/organizations/<org-slug>/releases/" \
  --header "Authorization: Bearer $SENTRY_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"version\": \"2.0.0\", \"projects\": [\"<project-slug>\"]}"

Update Release
curl -s -X PUT "https://sentry.io/api/0/organizations/<org-slug>/releases/<version>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"dateReleased\": \"2026-04-08T12:00:00Z\"}"

Delete Release
curl -s -X DELETE "https://sentry.io/api/0/organizations/<org-slug>/releases/<version>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

List Release Commits
curl -s "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/releases/<version>/commits/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Monitors (Cron)
List Monitors
curl -s "https://sentry.io/api/0/organizations/<org-slug>/monitors/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Get Monitor
curl -s "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/monitors/<monitor-slug>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Get Monitor Check-Ins
curl -s "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/monitors/<monitor-slug>/checkins/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Update Monitor
curl -s -X PUT "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/monitors/<monitor-slug>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"Updated Monitor\", \"schedule\": {\"type\": \"crontab\", \"value\": \"0 * * * *\"}}"

Delete Monitor
curl -s -X DELETE "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/monitors/<monitor-slug>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Alert Rules
List Alert Rules
curl -s "https://sentry.io/api/0/organizations/<org-slug>/alert-rules/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Get Alert Rule
curl -s "https://sentry.io/api/0/organizations/<org-slug>/alert-rules/<rule-id>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Project Rules (Issue Alerts)
List Project Rules
curl -s "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/rules/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Get Rule
curl -s "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/rules/<rule-id>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Teams
List Organization Teams
curl -s "https://sentry.io/api/0/organizations/<org-slug>/teams/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Get Team
curl -s "https://sentry.io/api/0/teams/<org-slug>/<team-slug>/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

List Team's Projects
curl -s "https://sentry.io/api/0/teams/<org-slug>/<team-slug>/projects/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Members
List Organization Members
curl -s "https://sentry.io/api/0/organizations/<org-slug>/members/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Environments
List Project Environments
curl -s "https://sentry.io/api/0/projects/<org-slug>/<project-slug>/environments/" \
  --header "Authorization: Bearer $SENTRY_TOKEN"

Issue Status Values
Status	Description
unresolved	Active issue (default)
resolved	Manually resolved
resolvedInNextRelease	Auto-resolve on next release
ignored	Ignored (won't alert)
Guidelines
Discover org slug first: Call GET /organizations/ to get your org slug before using other endpoints.
Use organization endpoints: List projects via GET /organizations/{org}/projects/, not GET /projects/ (which is not in the API spec).
Pagination: Use cursor parameter. Response includes Link header with next/prev cursors.
Search syntax: Issues support Sentry's query language: is:unresolved, level:error, assigned:me, first-release:, error.type:, etc.
Rate limits: Back off on 429 responses.
Scopes: Ensure token has required scopes (project:read, event:read, org:read, etc.).
How to Look Up More API Details
API Reference: https://docs.sentry.io/api/
Issues: https://docs.sentry.io/api/events/
Projects: https://docs.sentry.io/api/projects/
Releases: https://docs.sentry.io/api/releases/
Monitors: https://docs.sentry.io/api/crons/
Teams: https://docs.sentry.io/api/teams/
Scopes: https://docs.sentry.io/api/permissions/
Weekly Installs
63
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass