---
title: parallel-data-enrichment
url: https://skills.sh/parallel-web/parallel-agent-skills/parallel-data-enrichment
---

# parallel-data-enrichment

skills/parallel-web/parallel-agent-skills/parallel-data-enrichment
parallel-data-enrichment
Installation
$ npx skills add https://github.com/parallel-web/parallel-agent-skills --skill parallel-data-enrichment
Summary

Bulk enrichment of company, people, or product data with web-sourced fields like CEO names, funding, and contact info.

Accepts inline JSON data or CSV files; outputs enriched results to CSV
Runs asynchronously with progress tracking via monitoring URL and polling commands
Requires parallel-cli tool and internet access; handles large datasets with configurable timeouts
Supports flexible field requests through natural language intent descriptions (e.g., "CEO name and founding year")
SKILL.md
Data Enrichment

Enrich: $ARGUMENTS

Before starting

Inform the user that enrichment may take several minutes depending on the number of rows and fields requested.

Step 1: Start the enrichment

Use ONE of these command patterns (substitute user's actual data):

For inline data:

parallel-cli enrich run --data '[{"company": "Google"}, {"company": "Microsoft"}]' --intent "CEO name and founding year" --target "output.csv" --no-wait --json


For CSV file:

parallel-cli enrich run --source-type csv --source "input.csv" --target "output.csv" --source-columns '[{"name": "company", "description": "Company name"}]' --intent "CEO name and founding year" --no-wait --json


If this is a follow-up to a previous research or enrichment task where you know the interaction_id, add context chaining:

parallel-cli enrich run --data '...' --intent "..." --target "output.csv" --no-wait --json --previous-interaction-id "$INTERACTION_ID"


By chaining interaction_id values across requests, each follow-up automatically has the full context of prior turns — so you can enrich entities discovered in earlier research without restating what was already found.

IMPORTANT: Always include --no-wait so the command returns immediately instead of blocking.

Parse the output to extract the taskgroup_id, interaction_id, and monitoring URL. Immediately tell the user:

Enrichment has been kicked off
The monitoring URL where they can track progress

Tell them they can background the polling step to continue working while it runs.

Step 2: Poll for results
parallel-cli enrich poll "$TASKGROUP_ID" --timeout 540 --output "/tmp/$TARGET"


Use the same target filename from step 1. The --target flag on enrich run does not carry over to the poll — you must pass --output here to save the results.

Important:

Use --timeout 540 (9 minutes) to stay within tool execution limits
If the poll times out

Enrichment of large datasets can take longer than 9 minutes. If the poll exits without completing:

Tell the user the enrichment is still running server-side
Re-run the same parallel-cli enrich poll command to continue waiting
Response format

After step 1: Share the monitoring URL (for tracking progress).

After step 2:

Report number of rows enriched
Preview first few rows of the output CSV
Tell user the full path to the output CSV file
Share the interaction_id and tell the user they can ask follow-up questions that build on this enrichment

Do NOT re-share the monitoring URL after completion — the results are in the output file.

Remember the interaction_id — if the user asks a follow-up question that relates to this enrichment, use it as --previous-interaction-id in the next research or enrichment command.

Setup

If parallel-cli is not found, install and authenticate:

curl -fsSL https://parallel.ai/install.sh | bash


If unable to install that way, install via pipx instead:

pipx install "parallel-web-tools[cli]"
pipx ensurepath


Then authenticate:

parallel-cli login


Or set an API key: export PARALLEL_API_KEY="your-key"

Weekly Installs
1.1K
Repository
parallel-web/pa…t-skills
GitHub Stars
46
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail