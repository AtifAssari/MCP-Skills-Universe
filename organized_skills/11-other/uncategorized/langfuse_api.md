---
rating: ⭐⭐⭐
title: langfuse-api
url: https://skills.sh/langfuse/skills/langfuse-api
---

# langfuse-api

skills/langfuse/skills/langfuse-api
langfuse-api
Installation
$ npx skills add https://github.com/langfuse/skills --skill langfuse-api
SKILL.md
Langfuse API

Help users interact with Langfuse via the REST API.

When to Use
User wants to query or export traces
User wants to manage prompts programmatically
User wants to create/update datasets or dataset items
User wants to fetch or create scores
User wants to manage projects or API keys
Any other Langfuse API interaction
Workflow
1. Check Credentials

Before making any API call, verify credentials are available:

echo $LANGFUSE_PUBLIC_KEY   # pk-...
echo $LANGFUSE_SECRET_KEY   # sk-...
echo $LANGFUSE_HOST         # https://cloud.langfuse.com (or self-hosted/EU/US URL)


If not set, ask user:

"I need your Langfuse API credentials. You can find them in Settings → API Keys in the Langfuse UI."
"Which Langfuse host are you using? (cloud.langfuse.com, us.cloud.langfuse.com, eu.cloud.langfuse.com, or self-hosted URL)"
2. Fetch Fresh API Reference

Always fetch the current API reference before making calls. The API may have new endpoints or changed parameters.

Fetch: https://api.reference.langfuse.com

Look for the specific endpoint needed for the user's request. The reference contains:

All available endpoints
Required and optional parameters
Request/response schemas
Authentication details
3. Make the API Call

Authentication: Basic Auth with LANGFUSE_PUBLIC_KEY as username and LANGFUSE_SECRET_KEY as password.

Base URL: {LANGFUSE_HOST}/api/public

Example:

curl -X GET "${LANGFUSE_HOST}/api/public/traces" \
  -u "${LANGFUSE_PUBLIC_KEY}:${LANGFUSE_SECRET_KEY}" \
  -H "Content-Type: application/json"

4. Handle Pagination

Many endpoints return paginated results. Check for:

page and limit parameters
meta.totalItems and meta.totalPages in response
Iterate if user needs all results
Common Use Cases
User Request	Endpoint to Look Up
"Get my recent traces"	GET /traces
"Export traces from last week"	GET /traces with date filters
"Fetch a specific prompt"	GET /prompts/{name}
"Create a dataset"	POST /datasets
"Add items to dataset"	POST /dataset-items
"Get scores for a trace"	GET /scores with traceId filter
"List all prompts"	GET /prompts
Important Notes
Always fetch fresh docs - Don't rely on cached knowledge of the API
Check rate limits - The API has rate limits; handle 429 responses
Validate responses - Check for errors before processing data
Large exports - For bulk data, use pagination and consider streaming to file
OpenAPI Spec

For programmatic access or generating types:

https://cloud.langfuse.com/generated/api/openapi.yml

Weekly Installs
55
Repository
langfuse/skills
GitHub Stars
110
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail