---
rating: ⭐⭐⭐
title: devonthink
url: https://skills.sh/dvcrn/devonthink-cli/devonthink
---

# devonthink

skills/dvcrn/devonthink-cli/devonthink
devonthink
Installation
$ npx skills add https://github.com/dvcrn/devonthink-cli --skill devonthink
SKILL.md
DEVONthink CLI
Overview

Use this skill to run the DEVONthink CLI safely and produce exact commands for the current command surface.

Prefer read-only commands first when verifying identifiers or database context. Use JSON output when the result will be piped to other tools or parsed by code.

Read references/commands.md for the supported command surface. Read references/examples.md for concrete examples.

Exact Command Surface

Use these exact command names. Do not invent get_* variants unless they are listed here.

tools
schema <tool>
is_running
open_databases
current_database
selected_records
search [query]
lookup_record [lookupType]
list_group_content [uuid]
record_properties [uuid]
record_content [uuid]
record_by_identifier [uuid]
create_record [name]
create_from_url [url]
rename_record [uuid]
move_record [uuid]
delete_record [uuid]
add_tags [uuid]
remove_tags [uuid]
update_record_content [uuid]
set_record_properties [uuid]
classify [recordUuid]
compare [recordUuid]
replicate_record [uuid]
duplicate_record [uuid]
convert_record [uuid]
check_ai_health
ask_ai_about_documents [question]
create_summary_document
ai_tool_documentation [toolName]

Runbook
Confirm DEVONthink is running with devonthink is_running.
Confirm the active or target database with devonthink current_database or devonthink open_databases.
Resolve record UUIDs with read-only commands before write operations.
Prefer --json for automation and downstream parsing.
Before mutating records, verify the target with record_properties, record_by_identifier, search, or lookup_record.
Use schema <tool> when you need exact parameter names.
Installation And Agent Setup

Install from npm:

npm install -g devonthink


After installation, you can use any equivalent executable:

devonthink --help
dt --help
dt-cli --help


For Claude Desktop, add dvcrn/devonthink-cli as a marketplace plugin, then install the devonthink plugin from that marketplace.

For Claude Code, the equivalent commands are:

claude plugins marketplace add dvcrn/devonthink-cli
claude plugins install devonthink@dvcrn-devonthink-cli --scope user


For npx skills, run:

npx skills add dvcrn/devonthink-cli

Output Strategy

Use default human-readable output for interactive use. Use --json for automation and downstream parsing.

devonthink search invoice --json
devonthink record_properties <uuid> --json

Positional Arguments

Many tools support the first obvious required argument positionally.

devonthink search invoice
devonthink record_content <uuid>
devonthink record_properties <uuid>
devonthink rename_record <uuid> --new-name "Renamed note"
devonthink create_record "New Note" --type markdown --content "Hello"
devonthink create_from_url https://example.com --format markdown

Common Tasks

Use these as canonical examples:

# verify DEVONthink is running
devonthink is_running

# list open databases
devonthink open_databases

# inspect the current database
devonthink current_database

# search for records
devonthink search invoice --database-name Test

# get a record by UUID
devonthink record_properties <uuid>

# read record content
devonthink record_content <uuid>

# create a note
devonthink create_record "Meeting Notes" --type markdown --content "# Notes" --database-name Test

# update content
devonthink update_record_content <uuid> --content "Updated body"

# rename a record
devonthink rename_record <uuid> --new-name "Renamed note"

# add tags
devonthink add_tags <uuid> --tags work --tags important

# remove tags
devonthink remove_tags <uuid> --tags old-tag

Safety Checks

Before write operations:

Confirm the target database with current_database or open_databases.
Confirm the target record with record_properties, record_by_identifier, search, or lookup_record.
Confirm the destination group before move_record, duplicate_record, replicate_record, or convert_record.
Prefer UUIDs over names when mutating records.
Notes
devonthink, dt, and dt-cli are equivalent and map to the same implementation.
schema <tool> prints the exact JSON schema for a tool.
tools lists the available command surface.
Weekly Installs
16
Repository
dvcrn/devonthink-cli
GitHub Stars
14
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn