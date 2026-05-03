---
rating: ⭐⭐
title: pm-cli-usage
url: https://skills.sh/jogi47/pm-cli/pm-cli-usage
---

# pm-cli-usage

skills/jogi47/pm-cli/pm-cli-usage
pm-cli-usage
Installation
$ npx skills add https://github.com/jogi47/pm-cli --skill pm-cli-usage
SKILL.md
pm-cli Usage Guide

You are operating pm, a unified CLI for task management across multiple project management providers.

Tool Overview

pm supports:

provider connection and auth
assigned / overdue / search task views
single-task show / open / update
task creation, including Asana project/section placement
comments
complete / delete batch actions
summary and today dashboard views
Asana task thread and attachment inspection
config and cache management
task-based git branch creation

Supported providers:

asana
notion
trello
linear
clickup

Current capability notes:

task thread and task attachment commands are implemented on the Asana path
image download support for thread/attachment commands is implemented on the Asana path
workspace switching is currently useful for Asana
planned but not implemented yet: pm ui, pm bulk update, pm bulk move, pm bulk create --file
Setup
Connect interactively
pm connect asana
pm connect notion
pm connect trello
pm connect linear
pm connect clickup

Environment variable auth
export ASANA_TOKEN=<token>
export NOTION_TOKEN=<token>
export TRELLO_API_KEY=<api-key>
export TRELLO_TOKEN=<token>
export LINEAR_API_KEY=<token>
export CLICKUP_TOKEN=<token>


Notes:

Notion also needs a database ID during pm connect notion
credentials are prompted interactively when using pm connect
pm providers shows connection state and current workspace/user details
Workspace switching
pm workspace
pm workspace list -s asana
pm workspace switch -s asana

Task ID Format

All tasks use PROVIDER-externalId, for example:

ASANA-1234567890
NOTION-abc123def456
LINEAR-ENG-42

The provider prefix is case-insensitive.

Current Command Surface

Implemented commands:

pm connect
pm disconnect
pm providers
pm workspace
pm today
pm summary
pm open
pm branch
pm comment
pm done
pm delete
pm cache stats
pm cache clear
pm config init
pm config path
pm config list
pm config get
pm config set
pm tasks assigned
pm tasks overdue
pm tasks search
pm tasks show
pm tasks thread
pm tasks attachments
pm tasks create
pm tasks update


Not implemented yet:

pm ui
pm bulk update
pm bulk move
pm bulk create --file

Commands Reference
pm connect <provider>

Connect to a provider.

Values:

asana
notion
trello
linear
clickup

Example:

pm connect asana

pm disconnect <provider>

Disconnect from a provider and clear stored credentials.

Example:

pm disconnect asana

pm providers

Show provider connection status.

Flags:

--json
pm workspace [action]

List or switch workspaces.

Arguments:

action: list or switch (default: list)

Flags:

--source, -s: asana, notion, trello, linear, clickup

Example:

pm workspace switch -s asana

Task List Commands
pm tasks assigned

List tasks assigned to the current user.

Flags:

--source, -s
--limit, -l
--json
--refresh, -r
--status
--priority
--sort
--plain
--ids-only

Example:

pm tasks assigned --status=todo --sort=priority
pm tasks assigned --plain
pm tasks assigned --ids-only

pm tasks overdue

List overdue tasks.

Flags:

--source, -s
--limit, -l
--json
--refresh, -r
--status
--priority
--sort
--plain
--ids-only

Example:

pm tasks overdue --sort=due --plain

pm tasks search "<query>"

Search for tasks.

Flags:

--source, -s
--limit, -l
--json
--status
--priority
--sort
--plain
--ids-only

Notes:

search does not have a --refresh flag

Example:

pm tasks search "deploy" --sort=due --ids-only

Task Detail Commands
pm tasks show <id>

Show one task in detail.

Flags:

--json
--open, -o
pm open <id>

Open a task in the default browser.

pm comment <id> "<message>"

Add a comment to a task.

Example:

pm comment ASANA-123456 "Deployed to staging"

Thread and Attachment Commands
pm tasks thread <id>

Show task conversation history. On Asana, this can include comments, activity entries, and attachment entries.

Flags:

--json
--comments-only, -c
--with-task
--limit, -l
--download-images
--temp-dir
--cleanup

Notes:

--comments-only removes system activity entries but keeps attachment-related comment output
downloaded images are saved under a task-scoped directory in the chosen temp dir

Examples:

pm tasks thread ASANA-1234567890 --comments-only --with-task
pm tasks thread ASANA-1234567890 --download-images --temp-dir /tmp/pm-cli --cleanup
pm tasks thread ASANA-1234567890 --json

pm tasks attachments <id>

Show task attachments without the full thread body.

Flags:

--json
--download-images
--temp-dir
--cleanup

Examples:

pm tasks attachments ASANA-1234567890
pm tasks attachments ASANA-1234567890 --download-images --temp-dir /tmp/pm-cli
pm tasks attachments ASANA-1234567890 --json

Create and Update Commands
pm tasks create <title>

Create a new task.

Flags:

--description, -d
--title, -t (repeatable; supports multi-create)
--source, -s
--project, -p
--section
--workspace
--difficulty
--field (repeatable)
--refresh
--due
--assignee, -a
--json

Important rules:

if only one provider is connected, --source is inferred
--section requires --project
--difficulty requires --project
--field requires --project
project/section/workspace can be passed by ID or exact case-insensitive name
Asana project/section/workspace resolution can use --refresh to bypass metadata cache

Examples:

pm tasks create "Fix login bug"
pm tasks create "Automated ticket" --source asana --project "Platform Roadmap" --section "Ready"
pm tasks create "Tune dashboard UX" --source asana --project "Platform Roadmap" --section "Ready" --difficulty "S"
pm tasks create "Ship API integration" --source asana --project "Platform Roadmap" --section "Ready" --field "Difficulty=XS" --field "Area=Backend,Analytics"
pm tasks create --source asana --project "Platform Roadmap" --title "Task A" --title "Task B"

pm tasks update <id>

Update an existing task. At least one update flag is required.

Flags:

--title, -t
--description, -d
--due
--status
--project, -p
--workspace
--field (repeatable)
--refresh
--json

Examples:

pm tasks update ASANA-123456 --title "New title"
pm tasks update ASANA-123456 --due 2026-03-15 --status in_progress
pm tasks update ASANA-123456 --due none
pm tasks update ASANA-123456 --project "Platform Roadmap" --field "Difficulty=S"

Batch-Style Top-Level Actions
pm done <id> [id...]

Mark one or more tasks done.

pm delete <id> [id...]

Delete one or more tasks.

pm today

Show overdue, due today, and in-progress tasks in a grouped view.

Flags:

--source, -s
--json
pm summary

Show provider connection status and task count summary.

Flags:

--json
Git Helper
pm branch <id>

Create a git branch from a task title.

Flags:

--prefix, -p: feat, fix, chore
--checkout, -c
--no-id

Example:

pm branch ASANA-123456 --prefix feat --checkout

Config and Cache
pm cache stats

Show cache file path and entry counts.

pm cache clear

Clear cache globally or for one provider.

Flags:

--source
pm config init

Create a default .pmrc.json in the current project.

Flags:

--force, -f
pm config list

List merged config values as JSON.

pm config get <key>

Read a config value by dot path.

pm config set <key> <value>

Write a project-level config value into .pmrc.json.

pm config path

Show user and project config file paths.

Config behavior:

user config lives under ~/.config/pm-cli/config.json
project config lives in .pmrc.json
project config overrides user config on merge
Output Modes

The CLI supports:

default human/table output
--json
--plain
--ids-only

Examples:

pm tasks assigned --json
pm tasks overdue --plain
pm tasks search "deploy" --ids-only

Caching Behavior
cache TTL is about 5 minutes
use --refresh on tasks assigned and tasks overdue to bypass cache
tasks search can return cached results and does not expose --refresh
tasks show fetches directly from the provider path
Normalized Task Model

Every task returned by pm is normalized roughly like this:

id            PROVIDER-externalId
externalId    Original provider ID
title         Task title
description   Task description
status        todo | in_progress | done
dueDate       Due date when present
assignee      Assignee display name
project       Project or parent container name
placement     Structured project/section placement when available
tags          Tag/label array
source        asana | notion | trello | linear | clickup
url           Direct provider URL
priority      low | medium | high | urgent
createdAt     Creation timestamp
updatedAt     Update timestamp


Thread and attachment-related data can also include:

kind          comment | attachment | activity
attachments   Attachment metadata on thread entries
localPath     Downloaded image path when image download is enabled

Common Workflows

Morning dashboard:

pm today
pm summary


Review task thread with attachments:

pm tasks thread ASANA-123456 --comments-only --with-task
pm tasks attachments ASANA-123456 --download-images --temp-dir /tmp/pm-cli


Create directly in an Asana board column:

pm tasks create "Tune lesson plan UX" \
  --source asana \
  --project "Platform Roadmap" \
  --section "Ready" \
  --difficulty "S"


Filter and pipe IDs:

pm tasks assigned --priority=high,urgent --sort=due
pm tasks overdue --ids-only | xargs -I{} pm done {}

Help Commands

Use built-in help when in doubt:

pm --help
pm tasks --help
pm tasks create --help
pm tasks update --help
pm tasks thread --help
pm tasks attachments --help

Weekly Installs
20
Repository
jogi47/pm-cli
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn