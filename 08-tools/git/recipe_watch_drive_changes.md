---
rating: ⭐⭐
title: recipe-watch-drive-changes
url: https://skills.sh/googleworkspace/cli/recipe-watch-drive-changes
---

# recipe-watch-drive-changes

skills/googleworkspace/cli/recipe-watch-drive-changes
recipe-watch-drive-changes
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-watch-drive-changes
Summary

Subscribe to Google Drive file and folder changes via Pub/Sub notifications.

Requires the gws-events skill and gws binary to execute
Creates event subscriptions on Drive resources with configurable notification endpoints and payload options
Supports subscription lifecycle management: create, list, and renew subscriptions before expiry
Delivers change events (file updates) to Google Cloud Pub/Sub topics for downstream processing
SKILL.md
Watch for Drive Changes

PREREQUISITE: Load the following skills to execute this recipe: gws-events

Subscribe to change notifications on a Google Drive file or folder.

Steps
Create subscription: gws events subscriptions create --json '{"targetResource": "//drive.googleapis.com/drives/DRIVE_ID", "eventTypes": ["google.workspace.drive.file.v1.updated"], "notificationEndpoint": {"pubsubTopic": "projects/PROJECT/topics/TOPIC"}, "payloadOptions": {"includeResource": true}}'
List active subscriptions: gws events subscriptions list
Renew before expiry: gws events +renew --subscription SUBSCRIPTION_ID
Weekly Installs
11.4K
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