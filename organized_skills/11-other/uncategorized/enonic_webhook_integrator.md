---
rating: ⭐⭐
title: enonic-webhook-integrator
url: https://skills.sh/webmaxru/enonic-agent-skills/enonic-webhook-integrator
---

# enonic-webhook-integrator

skills/webmaxru/enonic-agent-skills/enonic-webhook-integrator
enonic-webhook-integrator
Installation
$ npx skills add https://github.com/webmaxru/enonic-agent-skills --skill enonic-webhook-integrator
SKILL.md
Enonic Webhook Integrator
Procedures

Step 1: Detect the Enonic XP project

Execute node scripts/find-enonic-targets.mjs . to locate Enonic XP project roots in the workspace.
If the script returns an empty array, stop and explain that no Enonic XP project was found.
If multiple projects are found, ask which project should receive the integration.
Identify the application key from gradle.properties (appName) or build.gradle.

Step 2: Determine integration direction

Classify the task as one of: outbound event listener (XP reacts to internal events and calls an external system), outbound webhook config (XP sends webhook payloads via built-in config), inbound webhook endpoint (XP receives payloads from an external system), or mixed (combination).
Read references/event-reference.md to identify the correct event types, listener patterns, and filtering strategies.
Read references/webhook-reference.md when the task involves outbound webhook configuration or inbound HTTP service endpoints.

Step 3: Implement outbound event listener (if applicable)

Read assets/event-listener.template.ts as a starting scaffold.
Register the event listener in the application's main.ts (or main.js) controller using lib-event's listener() function.
Use the type parameter with a pattern matching the target node events (e.g., node.pushed, node.created, node.updated, node.deleted).
Filter events by path within the callback by checking event.data.nodes[].path to restrict processing to the intended content tree.
When the listener must call an external HTTP endpoint, use lib-httpClient's request() function inside the callback or delegate to a background task.
For long-running processing, delegate work from the event callback to a background task using lib-task's executeFunction() to avoid blocking the event thread.
Read references/examples.md for complete integration patterns including CDN invalidation, search reindexing, and notification dispatch.

Step 4: Configure outbound webhooks (if applicable)

Read references/webhook-reference.md for the com.enonic.xp.webhooks.cfg configuration format.
Create or update the file at XP_HOME/config/com.enonic.xp.webhooks.cfg with webhook entries specifying the target URL and event types.
Validate that the configured event types match the intended content lifecycle events.
Use HTTPS URLs for webhook targets.
Never write actual secret values into configuration files or source code. Use descriptive placeholder tokens (e.g., REPLACE_WITH_CDN_SECRET) and instruct the operator to substitute real credentials out-of-band. Secrets must be managed by the operator through secure deployment pipelines, environment variables, or secret management tools—not committed to files.

Step 5: Implement inbound webhook endpoint (if applicable)

Read assets/http-service.template.ts as a starting scaffold.
Create an HTTP service controller at src/main/resources/services/<serviceName>/<serviceName>.ts.
Export a post(req) function that parses the incoming JSON payload from req.body.
Reject payloads exceeding a reasonable size limit (e.g., 1 MB) before parsing.
Validate the inbound payload by checking required fields, authentication headers, or HMAC signatures before processing.
Sanitize all string fields from the external payload before using them in content operations: trim whitespace, enforce maximum lengths, strip or escape HTML/script content, and reject values containing path traversal sequences (.., /, \).
Use an allowlist of expected field names rather than passing the raw payload object to content APIs.
Return appropriate HTTP status codes: 200 for success, 400 for malformed payloads, 401 for authentication failures, 413 for oversized payloads, 500 for unexpected errors.
When inbound payloads trigger content creation or modification, use lib-content or lib-node APIs within a context run to ensure proper permissions. Never pass unsanitized external values as content names, paths, or keys.

Step 6: Wire async processing with lib-task (if applicable)

When event handling or webhook processing requires heavy or time-consuming work, wrap it in executeFunction() from lib-task.
Report progress from long-running tasks using progress() to allow monitoring.
Read references/event-reference.md for the task event lifecycle (task.submitted, task.updated, task.finished, task.failed).

Step 7: Validate the integration

Execute node scripts/find-enonic-targets.mjs . to confirm the project still resolves correctly.
Verify that the event listener registration is in the application's main.ts or main.js file, which runs at application startup.
Confirm that outbound HTTP calls use HTTPS and include error handling for network failures and non-2xx responses.
Confirm that no actual secret values, API keys, or credentials appear in generated source code or configuration files—only placeholder tokens.
Confirm that inbound webhook endpoints sanitize and allowlist all fields from external payloads before passing them to content APIs.
If a webhook config file was created, confirm the event type patterns match the intended triggers.
Run the workspace build to verify no compilation errors.
Read references/troubleshooting.md when events do not fire, webhook deliveries fail, or inbound requests are rejected.
Error Handling
If node scripts/find-enonic-targets.mjs . finds no projects, confirm that build.gradle references com.enonic.xp plugins or that a src/main/resources/site/ directory exists.
If events do not fire after registering a listener, read references/troubleshooting.md to check listener registration location, event type patterns, and cluster vs. local event scope.
If outbound HTTP calls fail, verify the target URL, network access from the XP instance, and that the operator has substituted placeholder tokens with real credentials.
If inbound webhook requests return 404, confirm the service controller path follows services/<name>/<name>.ts and the application is deployed.
If background tasks fail silently, check task state using taskLib.list() and inspect logs for errors within the task function.
Weekly Installs
82
Repository
webmaxru/enonic…t-skills
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn