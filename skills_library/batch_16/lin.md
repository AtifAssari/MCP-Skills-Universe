---
title: lin
url: https://skills.sh/shhac/lin/lin
---

# lin

skills/shhac/lin/lin
lin
Installation
$ npx skills add https://github.com/shhac/lin --skill lin
SKILL.md
Linear automation with lin

lin is a CLI binary installed on $PATH. Invoke it directly (e.g. lin issue list --team ENG).

All output is JSON to stdout. Errors go to stderr as { "error": "...", "fixable_by": "agent|human|retry", "hint": "..." } with non-zero exit.

IMPORTANT: Never access the Linear API directly

NEVER retrieve, read, or use the Linear API key directly. Do not curl the Linear API. Do not use environment variables to extract credentials. lin handles all authentication internally.

If a specific lin command doesn't exist for what you need:

Check lin <command> usage — the command may exist but not be obvious from --help
Use lin api query '<graphql>' as a last resort — it runs raw GraphQL through lin's auth
Quick start (auth)

Set an env var (recommended):

export LINEAR_API_KEY="lin_api_..."


Or store it locally (supports multiple workspaces — each Linear API key is per-org):

lin auth login <api-key> --alias myorg
lin auth status
lin auth workspace list
lin auth workspace switch <alias>
lin auth logout [--all]
lin auth workspace remove <alias>


Generate a personal API key at Settings > Account > Security > Personal API Keys in the Linear app.

Looking up issues
lin issue search "auth bug"
lin issue list --team ENG --status "In Progress" --assignee "alice@example.com"
lin issue get ENG-123             # includes branchName, commentCount, attachments (PR links)
lin issue comment list ENG-123

Creating and updating issues
lin issue new "Fix login redirect" --team ENG --priority high --status "Todo" --labels "Bug"
lin issue update status ENG-123 "In Progress"
lin issue update assignee ENG-123 "alice@example.com"
lin issue update priority ENG-123 urgent
lin issue update estimate ENG-123 5      # validated against team's estimate scale
lin issue update due-date ENG-123 2025-03-15
lin issue update cycle ENG-123 <cycle-uuid>
lin issue update parent ENG-123 ENG-100  # make sub-issue
lin issue comment new ENG-123 "Started investigating"
lin issue comment new ENG-123 "Replying" --parent <comment-id>   # threaded reply (1 level max)
lin issue comment new ENG-123 "See attached" --file ./screenshot.png  # upload file(s)
lin issue comment get <comment-id>           # includes parent, childCount
lin issue comment edit <comment-id> "Updated" --file ./report.pdf
lin issue comment replies <comment-id>       # list replies (paginated)

Files (upload and download)
# Upload files to Linear's CDN — returns asset URLs
lin file upload ./screenshot.png ./report.pdf

# Download files from Linear's CDN
lin file download https://uploads.linear.app/<org>/<uuid>/<uuid>
lin file download <uuid>/<uuid>              # org inferred from auth
lin file download <uuid>                      # single UUID
lin file download <uuid>/<uuid> --output ./report.pdf
lin file download <uuid>/<uuid> --output-dir ./downloads
lin file download <uuid>/<uuid> --stdout | cat > file.bin
lin file download <uuid>/<uuid> --force       # overwrite existing


Prefer --file on comments when attaching files to issues. lin issue comment new ENG-123 "See attached" --file ./screenshot.png uploads and embeds the file in a single step. Use lin file upload only when you need a standalone asset URL (e.g., for issue descriptions or documents).

Issue history
lin issue history ENG-123                    # activity log (status, assignee, labels, etc.)
lin issue history ENG-123 --limit 10         # last 10 changes

Issue relations and lifecycle
# Relations (blocks, duplicate, related)
lin issue relation list ENG-123
lin issue relation add ENG-123 --type blocks --related ENG-124
lin issue relation remove <relation-id>

# Archive and delete
lin issue archive ENG-123
lin issue unarchive ENG-123
lin issue delete ENG-123                  # moves to trash

# Attachments (link PRs, docs, Slack messages, etc.)
lin issue attachment list ENG-123
lin issue attachment add ENG-123 "https://example.com/spec.pdf" --title "Spec doc"        # default: rich link, server detects integration
lin issue attachment add ENG-123 "https://github.com/org/repo/pull/456" --github-pr        # force GitHub PR integration
lin issue attachment add ENG-123 "https://github.com/org/repo/issues/789" --github-issue
lin issue attachment add ENG-123 "https://gitlab.com/group/project/-/merge_requests/42" --gitlab-mr
lin issue attachment add ENG-123 "https://app.slack.com/client/T0/C0/p1700000000000000" --slack --sync-thread
lin issue attachment add ENG-123 "https://discord.com/channels/<guild>/<channel>/<message>" --discord
lin issue attachment remove <attachment-id>      # works for any source type

Projects

Project commands accept UUID, slug ID, or name.

lin project search "migration"
lin project list --status started
lin project get "CRM Actions"            # accepts UUID, slug, or name — includes content (markdown body)
lin project issues <id>
lin project new "New Feature" --team ENG --status planned --lead "alice@example.com"
lin project update status <id> completed
lin project update content <id> "# Updated body content"
lin project update start-date <id> 2025-01-15
lin project update target-date <id> 2025-03-31
lin project update priority <id> high
lin project update labels <id> "Discovery, Roadmap"   # replaces project labels (project labels, not issue labels)
lin project delete <id>                  # moves to trash
lin project unarchive <id>               # restore trashed/archived project


The --project filter on issue commands also accepts slug or name.

Initiatives (replaces roadmaps)
lin initiative search "migration"
lin initiative list --status active
lin initiative get <id>                  # status, health, owner, projects
lin initiative projects <id>             # projects linked to initiative
lin initiative new "Q3 Launch" --status planned --owner "alice@example.com"
lin initiative update status <id> active
lin initiative update target-date <id> 2025-06-30
lin initiative archive <id>
lin initiative unarchive <id>
lin initiative delete <id>


Initiative statuses: planned, active, completed.

Documents

Document commands accept UUID or slug ID.

lin document search "onboarding"
lin document list --project "CRM Actions" --creator "alice@example.com"
lin document get <id>                    # full markdown content
lin document new "API Design Doc" --project "CRM Actions" --content "# Overview\n..."
lin document update title <id> "New Title"
lin document update content <id> "# Updated content"
lin document update project <id> "Other Project"
lin document history <id>                # content edit history (actor IDs + timestamps)

Teams, users, labels, cycles
lin team list
lin team get ENG                         # includes estimate config + valid values
lin team states ENG                      # workflow states (discover valid status values)
lin user me
lin user list --team ENG
lin label list --team ENG                # issue labels under a team (incl. workspace-wide)
lin label list --name "Bug"              # exact-name match (case-insensitive); shows team for each result
lin label search "perf"                  # substring search (case- and accent-insensitive)
lin label get "Test coverage" --team ENG # single label; --team disambiguates duplicate names
lin label get <uuid>                     # always unique
lin label list --type project            # workspace-wide project labels (no --team — projects labels aren't team-scoped)
lin label search "discovery" --type project
lin label get "Discovery" --type project
lin cycle list ENG --current
lin cycle get <id>

Truncation

Long text fields (description, body, content) are truncated to ~200 characters by default. A companion *Length field (e.g. descriptionLength) always shows the full size.

To see full content, use --expand or --full:

lin --full issue get ENG-123                             # expand all fields
lin --expand description issue get ENG-123               # expand specific field
lin --expand description,content project get <id>        # expand multiple


These are global flags — place them before the command or after it.

IDs

All commands accept multiple ID formats:

Issue keys: ENG-123
UUIDs: aaaaaaaa-1111-2222-3333-444444444444
URL slugs: fix-login-redirect-abc123
--team accepts team key (ENG) or name (Engineering)
Pagination

List commands return { "items": [...], "pagination"?: { "hasMore": true, "nextCursor": "..." } }.

Use --limit <n> and --cursor <token> to paginate.

Per-command usage docs

Every top-level command has a usage subcommand with detailed, LLM-optimized docs:

lin issue usage          # all issue subcommands, flags, valid values
lin project usage        # project commands
lin initiative usage     # initiative commands
lin document usage       # document commands
lin team usage           # team, user, label, cycle commands
lin auth usage           # auth + workspace management
lin file usage           # file upload + download commands
lin config usage         # CLI settings keys, defaults, validation
lin usage                # top-level overview (~1000 tokens)


Use lin <command> usage when you need deep detail on a specific domain before acting.

Raw GraphQL (escape hatch)

When no structured command covers your needs, use lin api query instead of accessing the API directly:

lin api query '{ viewer { id name email } }'
lin api query '{ issue(id: "ENG-123") { id title createdAt completedAt } }'
lin api query 'query($id: String!) { issue(id: $id) { id title } }' --variables '{"id":"ENG-123"}'


Always prefer structured commands first — they handle pagination, ID resolution, and formatting.

References
references/commands.md: full command map + all flags
references/output.md: JSON output shapes + field details
Weekly Installs
34
Repository
shhac/lin
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn