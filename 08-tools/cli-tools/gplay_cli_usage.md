---
title: gplay-cli-usage
url: https://skills.sh/tamtom/gplay-cli-skills/gplay-cli-usage
---

# gplay-cli-usage

skills/tamtom/gplay-cli-skills/gplay-cli-usage
gplay-cli-usage
Installation
$ npx skills add https://github.com/tamtom/gplay-cli-skills --skill gplay-cli-usage
SKILL.md
Google Play CLI usage

Use this skill when you need to run or design gplay commands for Google Play Console.

Command discovery
Always use --help to discover commands and flags.
gplay --help
gplay tracks --help
gplay tracks list --help
Available commands
Command	Description
gplay auth	Authentication and profile management
gplay apps	List and manage apps in the developer account
gplay init	Initialize a project with default config
gplay release	High-level release workflow
gplay promote	Promote releases between tracks
gplay rollout	Manage staged rollouts
gplay tracks	Track management
gplay bundles	Bundle (AAB) management
gplay edits	Edit session management
gplay listings	Store listing management
gplay images	Screenshot and image management
gplay sync	Metadata sync (import/export)
gplay validate	Offline validation of metadata
gplay vitals	App vitals monitoring (crashes, performance, errors)
gplay users	User management for developer account
gplay grants	App-level permission grants
gplay reports	Financial and statistics reports (list/download from GCS)
gplay docs generate	Generate CLI documentation
gplay migrate	Migration tools (e.g., from Fastlane)
gplay notify	Send notifications (e.g., Slack, webhook)
gplay update	Self-update the CLI binary
Flag conventions
Use explicit long flags (e.g., --package, --output).
No interactive prompts; destructive operations require --confirm.
Use --paginate when the user wants all pages.
Use --dry-run to preview changes without executing them (supported by release, migrate, and other write commands).
Output formats
Default output is minified JSON.
Use --output table or --output markdown only for human-readable output.
--pretty is only valid with JSON output.
Set GPLAY_DEFAULT_OUTPUT environment variable to change the default output format (e.g., GPLAY_DEFAULT_OUTPUT=table).
Authentication and defaults
Prefer service account auth via gplay auth login --service-account /path/to/sa.json.
Fallback env vars: GPLAY_SERVICE_ACCOUNT, GPLAY_PACKAGE.
GPLAY_PACKAGE can provide a default package name.
Timeouts
GPLAY_TIMEOUT / GPLAY_TIMEOUT_SECONDS control request timeouts.
GPLAY_UPLOAD_TIMEOUT / GPLAY_UPLOAD_TIMEOUT_SECONDS control upload timeouts.
Environment Variables
Variable	Purpose
GPLAY_SERVICE_ACCOUNT	Path to service account JSON
GPLAY_PACKAGE	Default package name
GPLAY_PROFILE	Active profile name
GPLAY_TIMEOUT	Request timeout (e.g., 90s, 2m)
GPLAY_TIMEOUT_SECONDS	Timeout in seconds (alternative)
GPLAY_UPLOAD_TIMEOUT	Upload timeout (e.g., 5m, 10m)
GPLAY_DEBUG	Enable debug logging (set to api for HTTP requests)
GPLAY_NO_UPDATE	Disable update checks
GPLAY_MAX_RETRIES	Max retries for failed requests (default: 3)
GPLAY_RETRY_DELAY	Base delay between retries (default: 1s)
GPLAY_DEFAULT_OUTPUT	Default output format (json, table, markdown)
Common patterns
List with pagination
gplay tracks list --package com.example.app --paginate

Parse JSON output with jq
gplay tracks list --package com.example.app | jq '.tracks[] | select(.track == "production")'

Use profiles
gplay auth add-profile production --service-account /path/to/prod-sa.json
gplay auth use-profile production
gplay --profile production tracks list --package com.example.app

Debug mode
GPLAY_DEBUG=1 gplay tracks list --package com.example.app
GPLAY_DEBUG=api gplay tracks list --package com.example.app  # HTTP details

Dry run (preview changes)
gplay release --package com.example.app --track beta --bundle app.aab --dry-run
gplay migrate fastlane --source ./fastlane/metadata/android --output-dir ./metadata --dry-run

Initialize a project
gplay init --package com.example.app --service-account /path/to/sa.json

List apps in developer account
gplay apps list --developer-id 1234567890
gplay apps list --developer-id 1234567890 --output table

Generate CLI documentation
gplay docs generate --format markdown --output-dir ./docs

Self-update
gplay update
gplay update --check  # Check for updates without installing

Financial reports
gplay reports financial list --developer <id>
gplay reports financial list --developer <id> --type earnings --from 2026-01 --to 2026-06
gplay reports financial download --developer <id> --from 2026-01 --type earnings --dir ./reports

Statistics reports
gplay reports stats list --developer <id>
gplay reports stats list --developer <id> --package com.example.app --type installs
gplay reports stats download --developer <id> --package com.example.app --from 2026-01 --type installs --dir ./reports

Send notifications
gplay notify --webhook https://hooks.slack.com/... --message "Release deployed"

Edit sessions

Most write operations require an edit session:

# Create edit
gplay edits create --package com.example.app
# Returns: edit_id

# Make changes
gplay bundles upload --package com.example.app --edit <edit_id> --file app.aab

# Commit changes (publishes)
gplay edits commit --package com.example.app --edit <edit_id>

High-level vs manual commands
High-level: gplay release (creates edit, uploads, commits)
Manual: gplay edits create → gplay bundles upload → gplay edits commit

Use high-level for simplicity, manual for fine-grained control.

Weekly Installs
102
Repository
tamtom/gplay-cli-skills
GitHub Stars
33
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass