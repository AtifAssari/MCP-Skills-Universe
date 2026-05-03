---
title: gws-gmail-watch
url: https://skills.sh/googleworkspace/cli/gws-gmail-watch
---

# gws-gmail-watch

skills/googleworkspace/cli/gws-gmail-watch
gws-gmail-watch
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-gmail-watch
Summary

Stream new Gmail messages as NDJSON with Pub/Sub-backed polling and optional file output.

Monitors incoming emails via Gmail API with configurable label filtering (INBOX, UNREAD, etc.) and message format options (full, metadata, minimal, raw)
Supports two setup modes: automatic Pub/Sub topic and subscription creation, or connection to existing resources
Configurable polling interval, batch size, and one-time pull mode; graceful shutdown with optional resource cleanup
Can write each message to a separate JSON file or stream directly to stdout; watch sessions expire after 7 days and must be renewed
SKILL.md
gmail +watch

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Watch for new emails and stream them as NDJSON

Usage
gws gmail +watch

Flags
Flag	Required	Default	Description
--project	—	—	GCP project ID for Pub/Sub resources
--subscription	—	—	Existing Pub/Sub subscription name (skip setup)
--topic	—	—	Existing Pub/Sub topic with Gmail push permission already granted
--label-ids	—	—	Comma-separated Gmail label IDs to filter (e.g., INBOX,UNREAD)
--max-messages	—	10	Max messages per pull batch
--poll-interval	—	5	Seconds between pulls
--msg-format	—	full	Gmail message format: full, metadata, minimal, raw
--once	—	—	Pull once and exit
--cleanup	—	—	Delete created Pub/Sub resources on exit
--output-dir	—	—	Write each message to a separate JSON file in this directory
Examples
gws gmail +watch --project my-gcp-project
gws gmail +watch --project my-project --label-ids INBOX --once
gws gmail +watch --subscription projects/p/subscriptions/my-sub
gws gmail +watch --project my-project --cleanup --output-dir ./emails

Tips
Gmail watch expires after 7 days — re-run to renew.
Without --cleanup, Pub/Sub resources persist for reconnection.
Press Ctrl-C to stop gracefully.
See Also
gws-shared — Global flags and auth
gws-gmail — All send, read, and manage email commands
Weekly Installs
15.3K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn