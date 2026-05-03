---
rating: ⭐⭐
title: replicate
url: https://skills.sh/replicate/skills/replicate
---

# replicate

skills/replicate/skills/replicate
replicate
Installation
$ npx skills add https://github.com/replicate/skills --skill replicate
SKILL.md
Docs
Reference docs: https://replicate.com/docs/llms.txt
HTTP API schema: https://api.replicate.com/openapi.json
MCP server: https://mcp.replicate.com
Set an Accept: text/markdown header when requesting docs pages to get a Markdown response.
Workflow

Here's a common workflow for using Replicate's API to run a model:

Choose the right model - Search with the API or ask the user
Get model metadata - Fetch model input and output schema via API
Create prediction - POST to /v1/predictions
Poll for results - GET prediction until status is "succeeded"
Return output - Usually URLs to generated content
Choosing models
Use the search and collections APIs to find and compare the best models. Do not list all the models via API, as it's basically a firehose.
Collections are curated by Replicate staff, so they're vetted.
Official models are in the "official" collection.
Use official models because they:
are always running
have stable API interfaces
have predictable output pricing
are maintained by Replicate staff
If you must use a community model, be aware that it can take a long time to boot.
You can create always-on deployments of community models, but you pay for model uptime.
Running models

Models take time to run. There are three ways to run a model via API and get its output:

Create a prediction, store its id from the response, and poll until completion.
Set a Prefer: wait header when creating a prediction for a blocking synchronous response. Only recommended for very fast models.
Set an HTTPS webhook URL when creating a prediction, and Replicate will POST to that URL when the prediction completes.

Follow these guideliness when running models:

Use the "POST /v1/predictions" endpoint, as it supports both official and community models.
Every model has its own OpenAPI schema. Always fetch and check model schemas to make sure you're setting valid inputs. Even popular models change their schemas.
Validate input parameters against schema constraints (minimum, maximum, enum values). Don't generate values that violate them.
When unsure about a parameter value, use the model's default example or omit the optional parameter.
Don't set optional inputs unless you have a reason to. Stick to the required inputs and let the model's defaults do the work.
Use HTTPS URLs for file inputs whenever possible. You can also send base64-encoded files, but they should be avoided.
Fire off multiple predictions concurrently. Don't wait for one to finish before starting the next.
Output file URLs expire after 1 hour, so back them up if you need to keep them, using a service like Cloudflare R2.
Webhooks are a good mechanism for receiving and storing prediction output.
Weekly Installs
460
Repository
replicate/skills
GitHub Stars
35
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn