---
title: arize-link
url: https://skills.sh/github/awesome-copilot/arize-link
---

# arize-link

skills/github/awesome-copilot/arize-link
arize-link
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill arize-link
SKILL.md
Arize Link

Generate deep links to the Arize UI for traces, spans, sessions, datasets, labeling queues, evaluators, and annotation configs.

When to Use
User wants a link to a trace, span, session, dataset, labeling queue, evaluator, or annotation config
You have IDs from exported data or logs and need to link back to the UI
User asks to "open" or "view" any of the above in Arize
Required Inputs

Collect from the user or context (exported trace data, parsed URLs):

Always required	Resource-specific
org_id (base64)	project_id + trace_id [+ span_id] — trace/span
space_id (base64)	project_id + session_id — session
	dataset_id — dataset
	queue_id — specific queue (omit for list)
	evaluator_id [+ version] — evaluator

All path IDs must be base64-encoded (characters: A-Za-z0-9+/=). A raw numeric ID produces a valid-looking URL that 404s. If the user provides a number, ask them to copy the ID directly from their Arize browser URL (https://app.arize.com/organizations/{org_id}/spaces/{space_id}/…). If you have a raw internal ID (e.g. Organization:1:abC1), base64-encode it before inserting into the URL.

URL Templates

Base URL: https://app.arize.com (override for on-prem)

Trace (add &selectedSpanId={span_id} to highlight a specific span):

{base_url}/organizations/{org_id}/spaces/{space_id}/projects/{project_id}?selectedTraceId={trace_id}&queryFilterA=&selectedTab=llmTracing&timeZoneA=America%2FLos_Angeles&startA={start_ms}&endA={end_ms}&envA=tracing&modelType=generative_llm


Session:

{base_url}/organizations/{org_id}/spaces/{space_id}/projects/{project_id}?selectedSessionId={session_id}&queryFilterA=&selectedTab=llmTracing&timeZoneA=America%2FLos_Angeles&startA={start_ms}&endA={end_ms}&envA=tracing&modelType=generative_llm


Dataset (selectedTab: examples or experiments):

{base_url}/organizations/{org_id}/spaces/{space_id}/datasets/{dataset_id}?selectedTab=examples


Queue list / specific queue:

{base_url}/organizations/{org_id}/spaces/{space_id}/queues
{base_url}/organizations/{org_id}/spaces/{space_id}/queues/{queue_id}


Evaluator (omit ?version=… for latest):

{base_url}/organizations/{org_id}/spaces/{space_id}/evaluators/{evaluator_id}
{base_url}/organizations/{org_id}/spaces/{space_id}/evaluators/{evaluator_id}?version={version_url_encoded}


The version value must be URL-encoded (e.g., trailing = → %3D).

Annotation configs:

{base_url}/organizations/{org_id}/spaces/{space_id}/annotation-configs

Time Range

CRITICAL: startA and endA (epoch milliseconds) are required for trace/span/session links — omitting them defaults to the last 7 days and will show "no recent data" if the trace falls outside that window.

Priority order:

User-provided URL — extract and reuse startA/endA directly.
Span start_time — pad ±1 day (or ±1 hour for a tighter window).
Fallback — last 90 days (now - 90d to now).

Prefer tight windows; 90-day windows load slowly.

Instructions
Gather IDs from user, exported data, or URL context.
Verify all path IDs are base64-encoded.
Determine startA/endA using the priority order above.
Substitute into the appropriate template and present as a clickable markdown link.
Troubleshooting
Problem	Solution
"No data" / empty view	Trace outside time window — widen startA/endA (±1h → ±1d → 90d).
404	ID wrong or not base64. Re-check org_id, space_id, project_id from the browser URL.
Span not highlighted	span_id may belong to a different trace. Verify against exported span data.
org_id unknown	ax CLI doesn't expose it. Ask user to copy from https://app.arize.com/organizations/{org_id}/spaces/{space_id}/….
Related Skills
arize-trace: Export spans to get trace_id, span_id, and start_time.
Examples

See references/EXAMPLES.md for a complete set of concrete URLs for every link type.

Weekly Installs
752
Repository
github/awesome-copilot
GitHub Stars
31.9K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass