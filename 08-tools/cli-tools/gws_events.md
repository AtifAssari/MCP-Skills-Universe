---
rating: ⭐⭐⭐
title: gws-events
url: https://skills.sh/googleworkspace/cli/gws-events
---

# gws-events

skills/googleworkspace/cli/gws-events
gws-events
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-events
Summary

Real-time event streaming and subscription management for Google Workspace.

Provides three core resource types: subscriptions (create, list, get, delete, patch, reactivate), operations (poll long-running tasks), and message/task streaming for real-time event delivery
Includes helper commands for subscribing to Workspace events as NDJSON streams and renewing suspended subscriptions
Requires Google Workspace authentication and the gws binary; use gws schema to inspect method parameters before execution
SKILL.md
events (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws events <resource> <method> [flags]

Helper Commands
Command	Description
+subscribe	Subscribe to Workspace events and stream them as NDJSON
+renew	Renew/reactivate Workspace Events subscriptions
API Resources
message
stream — SendStreamingMessage is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.
operations
get — Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.
subscriptions
create — Creates a Google Workspace subscription. To learn how to use this method, see Create a Google Workspace subscription.
delete — Deletes a Google Workspace subscription. To learn how to use this method, see Delete a Google Workspace subscription.
get — Gets details about a Google Workspace subscription. To learn how to use this method, see Get details about a Google Workspace subscription.
list — Lists Google Workspace subscriptions. To learn how to use this method, see List Google Workspace subscriptions.
patch — Updates or renews a Google Workspace subscription. To learn how to use this method, see Update or renew a Google Workspace subscription.
reactivate — Reactivates a suspended Google Workspace subscription. This method resets your subscription's State field to ACTIVE. Before you use this method, you must fix the error that suspended the subscription. This method will ignore or reject any subscription that isn't currently in a suspended state. To learn how to use this method, see Reactivate a Google Workspace subscription.
tasks
cancel — Cancel a task from the agent. If supported one should expect no more task updates for the task.
get — Get the current state of a task from the agent.
subscribe — TaskSubscription is a streaming call that will return a stream of task update events. This attaches the stream to an existing in process task. If the task is complete the stream will return the completed task (like GetTask) and close the stream.
pushNotificationConfigs — Operations on the 'pushNotificationConfigs' resource
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws events --help

# Inspect a method's required params, types, and defaults
gws schema events.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
11.8K
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