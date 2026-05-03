---
rating: ⭐⭐⭐
title: fresh-auth
url: https://skills.sh/fwfutures/skills/fresh-auth
---

# fresh-auth

skills/fwfutures/skills/fresh-auth
fresh-auth
Installation
$ npx skills add https://github.com/fwfutures/skills --skill fresh-auth
SKILL.md
Fresh Auth Workspace CLI

Use this skill as the single entry point for secure, identity-aware access to Microsoft 365 (Graph) and Notion.

Use this skill for
Drive operations, OneDrive file access, and share links through office-cli.
Outlook inbox, search, send, and reply actions through office-cli.
Calendar lookup and scheduling visibility through office-cli.
People lookups through office-cli.
Notion database search, query, page read/write, and markdown conversion through notion-query.
Any request that mixes Office and Notion data in one workflow.
Security model
Use the Auth Service Proxy at https://auth.freshhub.ai for Microsoft Graph and Notion actions.
Use agent-session grants and OAuth approvals, never raw provider tokens.
Keep ~/.config/fresh-auth/agent-session at secure mode (600).
Legacy ~/.config/office-cli/agent-session is still read for compatibility.
Store secrets in environment variables.
Use OPENROUTER_API_KEY for Office PDF/image conversion.
Use AUTH_SERVICE_URL only when overriding the default proxy endpoint.
Runtime prerequisites
Install Node.js (18+) for scripts/office-cli.js and scripts/notion-query.js.
Run commands from this skill folder or export explicit paths.
# Resolve skill location for common installers
export FRESH_AUTH_DIR="${HOME}/.agents/skills/fresh-auth"
[ -d "$FRESH_AUTH_DIR" ] || export FRESH_AUTH_DIR="${HOME}/.codex/skills/fresh-auth"

export OFFICE_CLI="${FRESH_AUTH_DIR}/scripts/office-cli.js"
export NOTION_CLI="${FRESH_AUTH_DIR}/scripts/notion-query.js"
export AUTH_SERVICE_URL="https://auth.freshhub.ai"

# Quick command discovery
[ -f "$OFFICE_CLI" ] && node "$OFFICE_CLI" status
[ -f "$NOTION_CLI" ] && node "$NOTION_CLI" status

Bundled scripts
scripts/office-cli.js for Microsoft Graph-backed Drive, Mail, Calendar, and People actions.
scripts/notion-query.js for Notion read/write workflows through auth service proxy.
Office + Graph: canonical flow

Follow this flow when granting access for Graph-backed tools.

# Register and create grants
node "$OFFICE_CLI" login
node "$OFFICE_CLI" request drive
node "$OFFICE_CLI" request mail
node "$OFFICE_CLI" request cal
node "$NOTION_CLI" request

# Verify active grants
node "$OFFICE_CLI" status
node "$NOTION_CLI" status

Agent-assisted verification handoff

When the agent runs login or request, the CLI may print a verification URL and code for human approval.

Agent runs the auth command and captures the exact verification output.
Agent sends the verification URL and code to the user (do not paraphrase).
Prefer sharing the prefilled URL format: https://auth.freshhub.ai/agent/verify?code=<CODE>
User opens the URL, confirms the code, clicks Verify Code, then manually clicks Approve on the next screen.
Agent waits for approval polling to complete, then continues with the requested task.

If approval fails, repeat the flow and confirm the user is signed into the intended Fresh Auth account before entering the code.

Command map: Office CLI
Drive / Graph storage
node "$OFFICE_CLI" drive list
node "$OFFICE_CLI" drive list "/Documents"
node "$OFFICE_CLI" drive search "Quarterly report"
node "$OFFICE_CLI" drive download <file-id> out.docx
node "$OFFICE_CLI" drive content <file-id>
node "$OFFICE_CLI" drive convert <file-id> --output=notes.md
node "$OFFICE_CLI" drive share <file-id> --type edit
node "$OFFICE_CLI" drive share <file-id> --anyone
node "$OFFICE_CLI" drive permissions <file-id>
node "$OFFICE_CLI" drive unshare <file-id> <permission-id>

Mail / Email
node "$OFFICE_CLI" mail inbox
node "$OFFICE_CLI" mail inbox --count 50
node "$OFFICE_CLI" mail unread
node "$OFFICE_CLI" mail search "team update"
node "$OFFICE_CLI" mail read <message-id>
node "$OFFICE_CLI" mail send --to "teammate@example.com" --subject "Brief" --body "Thanks for the update"
node "$OFFICE_CLI" mail send --to "brad" --subject "Quick check" --body "Approved" --yes
node "$OFFICE_CLI" mail reply <message-id> --body "Got it."
node "$OFFICE_CLI" mail reply-all <message-id> --body "Thanks everyone."

Calendar
node "$OFFICE_CLI" cal today
node "$OFFICE_CLI" cal tomorrow
node "$OFFICE_CLI" cal events --days 14
node "$OFFICE_CLI" cal events --full

People lookup (Graph contact helper)
node "$OFFICE_CLI" people "brad"
node "$OFFICE_CLI" people "brad" --verbose

Notion command map
node "$NOTION_CLI" login
node "$NOTION_CLI" request
node "$NOTION_CLI" status
node "$NOTION_CLI" me
node "$NOTION_CLI" find-db "my database"
node "$NOTION_CLI" search "my database"
node "$NOTION_CLI" get-db <database-id>
node "$NOTION_CLI" query-db <database-id>
node "$NOTION_CLI" get-page <page-id>
node "$NOTION_CLI" get-markdown <page-id>
node "$NOTION_CLI" create <database-id> "Title" -p "Status=In progress" -p "Priority=High"
node "$NOTION_CLI" update <page-id> -p "Status=Done"
node "$NOTION_CLI" set-body <page-id> -
node "$NOTION_CLI" append-body <page-id> -


Use find-db first when the database ID is unknown. It returns database id, title, and url so the ID can be copied directly into get-db, query-db, or create.

Notion backlog helper
# Optional: enable shortcuts for a specific Notion backlog database
export NOTION_BACKLOG_DB_ID="<database-id>"

node "$NOTION_CLI" backlog
node "$NOTION_CLI" backlog "In Progress"
node "$NOTION_CLI" create-backlog "New task"

Multi-tool patterns
Run people first, then mail send --to <resolved email> for safer identity resolution.
Pull a Notion task with search or query-db, then append context with append-body.
Convert a meeting PDF in Drive to markdown with drive convert, then store notes in Notion via append-body.
Error handling
no_agent_session: run node "$OFFICE_CLI" login.
no_grant: run node "$OFFICE_CLI" request <drive|mail|cal>.
token expired: run node "$OFFICE_CLI" status and follow the returned re-authorisation URL.
no agent session (Notion): run node "$NOTION_CLI" login.
no grant (Notion): run node "$NOTION_CLI" request.
NOTION_BACKLOG_DB_ID missing: set variable or call generic query-db/create commands instead of backlog shortcuts.
Microsoft account not linked: follow the URL output by Graph proxy responses.
Notion account not linked: follow the Notion connect URL output by the CLI.
Public publication checks
Keep proxy URL configurable by AUTH_SERVICE_URL.
Do not embed API keys or session IDs in skill outputs.
Keep all commands pointed at https://auth.freshhub.ai by default.
Include both CLIs under this skill's scripts/ folder for self-contained installation.
Mention both Microsoft 365 and Notion capabilities in onboarding docs because this is a unified user-facing access path.
Weekly Installs
28
Repository
fwfutures/skills
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail