---
title: twill-cloud-coding-agent
url: https://skills.sh/twillai/skills/twill-cloud-coding-agent
---

# twill-cloud-coding-agent

skills/twillai/skills/twill-cloud-coding-agent
twill-cloud-coding-agent
Installation
$ npx skills add https://github.com/twillai/skills --skill twill-cloud-coding-agent
Summary

Manage Twill Cloud Coding Agent workflows through the public v1 API.

Create, list, retrieve, and manage tasks with support for custom branches, agent selection, and file attachments
Stream job logs in real time via Server-Sent Events and cancel running jobs at any point
Full lifecycle control: send follow-up messages, approve plans, archive tasks, and manage task state
Schedule recurring coding tasks with cron expressions, timezone support, and pause/resume capabilities
List repositories and export Claude teleport sessions for workspace integration
SKILL.md
Twill Cloud Coding Agent

Use this skill to run Twill workflows through the public v1 API.

Setup

Set API key and optional base URL:

export TWILL_API_KEY="your_api_key"
export TWILL_BASE_URL="${TWILL_BASE_URL:-https://twill.ai}"


All API calls use:

Authorization: Bearer $TWILL_API_KEY

Use this helper to reduce repetition:

api() {
  curl -sS "$@" -H "Authorization: Bearer $TWILL_API_KEY" -H "Content-Type: application/json"
}

Endpoint Coverage (Public v1)
GET /api/v1/auth/me
GET /api/v1/repositories
POST /api/v1/tasks
GET /api/v1/tasks
GET /api/v1/tasks/:taskIdOrSlug
POST /api/v1/tasks/:taskIdOrSlug/messages
GET /api/v1/tasks/:taskIdOrSlug/jobs
POST /api/v1/tasks/:taskIdOrSlug/approve-plan
POST /api/v1/tasks/:taskIdOrSlug/cancel
POST /api/v1/tasks/:taskIdOrSlug/archive
GET /api/v1/tasks/:taskIdOrSlug/teleport/claude
GET /api/v1/jobs/:jobId/logs/stream
POST /api/v1/jobs/:jobId/cancel
GET /api/v1/scheduled-tasks
POST /api/v1/scheduled-tasks
GET /api/v1/scheduled-tasks/:scheduledTaskId
PATCH /api/v1/scheduled-tasks/:scheduledTaskId
DELETE /api/v1/scheduled-tasks/:scheduledTaskId
POST /api/v1/scheduled-tasks/:scheduledTaskId/pause
POST /api/v1/scheduled-tasks/:scheduledTaskId/resume
Auth and Discovery

Validate key and workspace context:

curl -sS "$TWILL_BASE_URL/api/v1/auth/me" -H "Authorization: Bearer $TWILL_API_KEY"


List available GitHub repositories for the workspace:

curl -sS "$TWILL_BASE_URL/api/v1/repositories" -H "Authorization: Bearer $TWILL_API_KEY"

Tasks
Create Task
api -X POST "$TWILL_BASE_URL/api/v1/tasks" -d '{"command":"Fix flaky tests in CI","repository":"owner/repo","userIntent":"SWE"}'


Required fields:

command
repository (owner/repo or full GitHub URL)

Optional fields:

branch
agent (provider or provider/model, for example codex or codex/gpt-5.2)
userIntent (SWE, PLAN, ASK, DEV_ENVIRONMENT) — defaults to SWE
title
files (array of { filename, mediaType, url })

Always report task.url back to the user.

List Tasks
curl -sS "$TWILL_BASE_URL/api/v1/tasks?limit=20&cursor=BASE64_CURSOR" -H "Authorization: Bearer $TWILL_API_KEY"


Supports cursor pagination via limit and cursor.

Get Task Details
curl -sS "$TWILL_BASE_URL/api/v1/tasks/TASK_ID_OR_SLUG" -H "Authorization: Bearer $TWILL_API_KEY"


Returns task metadata plus latestJob including status, type, plan content, and plan outcome when available.

Send Follow-Up Message
api -X POST "$TWILL_BASE_URL/api/v1/tasks/TASK_ID_OR_SLUG/messages" -d '{"message":"Please prioritize login flow first","userIntent":"PLAN"}'


userIntent and files are optional.

List Task Jobs
curl -sS "$TWILL_BASE_URL/api/v1/tasks/TASK_ID_OR_SLUG/jobs?limit=30&cursor=BASE64_CURSOR" -H "Authorization: Bearer $TWILL_API_KEY"


Supports cursor pagination:

limit defaults to 30 (max 100)
cursor fetches older pages
response includes jobs and nextCursor
Approve Plan

Use when the latest plan job is completed and ready for approval.

api -X POST "$TWILL_BASE_URL/api/v1/tasks/TASK_ID_OR_SLUG/approve-plan" -d '{}'

Cancel Task
api -X POST "$TWILL_BASE_URL/api/v1/tasks/TASK_ID_OR_SLUG/cancel" -d '{}'

Archive Task
api -X POST "$TWILL_BASE_URL/api/v1/tasks/TASK_ID_OR_SLUG/archive" -d '{}'

Jobs
Stream Job Logs (SSE)
curl -N "$TWILL_BASE_URL/api/v1/jobs/JOB_ID/logs/stream" -H "Authorization: Bearer $TWILL_API_KEY" -H "Accept: text/event-stream"


Stream emits JSON payloads in data: lines and terminates with a complete event.

Cancel Job
api -X POST "$TWILL_BASE_URL/api/v1/jobs/JOB_ID/cancel" -d '{}'

Scheduled Tasks
List and Create
curl -sS "$TWILL_BASE_URL/api/v1/scheduled-tasks" -H "Authorization: Bearer $TWILL_API_KEY"

api -X POST "$TWILL_BASE_URL/api/v1/scheduled-tasks" -d '{
  "title":"Daily triage",
  "message":"Review urgent issues and open tasks",
  "repositoryUrl":"https://github.com/org/repo",
  "baseBranch":"main",
  "cronExpression":"0 9 * * 1-5",
  "timezone":"America/New_York",
  "agentProviderId":"claude-code/sonnet"
}'


Required: title, message, repositoryUrl, baseBranch, cronExpression.

Optional: timezone (defaults to "UTC"), agentProviderId (provider/model override).

Read, Update, Delete
curl -sS "$TWILL_BASE_URL/api/v1/scheduled-tasks/SCHEDULED_TASK_ID" -H "Authorization: Bearer $TWILL_API_KEY"

api -X PATCH "$TWILL_BASE_URL/api/v1/scheduled-tasks/SCHEDULED_TASK_ID" -d '{
  "message":"Updated instructions",
  "cronExpression":"0 10 * * 1-5",
  "agentProviderId":"codex/gpt-5.2"
}'

curl -sS -X DELETE "$TWILL_BASE_URL/api/v1/scheduled-tasks/SCHEDULED_TASK_ID" -H "Authorization: Bearer $TWILL_API_KEY"

Pause and Resume
api -X POST "$TWILL_BASE_URL/api/v1/scheduled-tasks/SCHEDULED_TASK_ID/pause" -d '{}'
api -X POST "$TWILL_BASE_URL/api/v1/scheduled-tasks/SCHEDULED_TASK_ID/resume" -d '{}'

Behavior
Use userIntent (SWE, PLAN, ASK, DEV_ENVIRONMENT) when calling API endpoints directly.
Create task, report task.url, and only poll/stream logs when requested.
Ask for TWILL_API_KEY if missing.
Do not print API keys or other secrets.
Weekly Installs
937
Repository
twillai/skills
GitHub Stars
8
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn