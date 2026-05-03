---
rating: ⭐⭐
title: gws-events-subscribe
url: https://skills.sh/googleworkspace/cli/gws-events-subscribe
---

# gws-events-subscribe

skills/googleworkspace/cli/gws-events-subscribe
gws-events-subscribe
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-events-subscribe
Summary

Subscribe to Google Workspace events and stream them as NDJSON output.

Connects to Workspace resources (Chat spaces, Drive, Calendar, etc.) via CloudEvents types and streams events in real-time or batch mode
Supports Pub/Sub-backed subscriptions with configurable polling intervals, batch sizes, and optional auto-acknowledgment
Offers flexible output modes: stream to stdout, write individual events to files, or reuse existing subscriptions for reconnection
Includes cleanup options to remove Pub/Sub resources on exit and one-shot polling with the --once flag
SKILL.md
events +subscribe

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Subscribe to Workspace events and stream them as NDJSON

Usage
gws events +subscribe

Flags
Flag	Required	Default	Description
--target	—	—	Workspace resource URI (e.g., //chat.googleapis.com/spaces/SPACE_ID)
--event-types	—	—	Comma-separated CloudEvents types to subscribe to
--project	—	—	GCP project ID for Pub/Sub resources
--subscription	—	—	Existing Pub/Sub subscription name (skip setup)
--max-messages	—	10	Max messages per pull batch (default: 10)
--poll-interval	—	5	Seconds between pulls (default: 5)
--once	—	—	Pull once and exit
--cleanup	—	—	Delete created Pub/Sub resources on exit
--no-ack	—	—	Don't auto-acknowledge messages
--output-dir	—	—	Write each event to a separate JSON file in this directory
Examples
gws events +subscribe --target '//chat.googleapis.com/spaces/SPACE' --event-types 'google.workspace.chat.message.v1.created' --project my-project
gws events +subscribe --subscription projects/p/subscriptions/my-sub --once
gws events +subscribe ... --cleanup --output-dir ./events

Tips
Without --cleanup, Pub/Sub resources persist for reconnection.
Press Ctrl-C to stop gracefully.

[!CAUTION] This is a write command — confirm with the user before executing.

See Also
gws-shared — Global flags and auth
gws-events — All subscribe to google workspace events commands
Weekly Installs
11.5K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass