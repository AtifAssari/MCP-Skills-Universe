---
title: kibana-agent-builder
url: https://skills.sh/elastic/agent-skills/kibana-agent-builder
---

# kibana-agent-builder

skills/elastic/agent-skills/kibana-agent-builder
kibana-agent-builder
Installation
$ npx skills add https://github.com/elastic/agent-skills --skill kibana-agent-builder
SKILL.md
Manage Agent Builder Agents and Tools in Kibana

Create, update, delete, inspect, and chat with Agent Builder agents. Create, update, delete, list, and test custom tools (ES|QL, index search, workflow). If the user provided a name, use $ARGUMENTS as the default agent name.

Prerequisites

Set these environment variables before running any script:

Variable	Required	Description
KIBANA_URL	Yes	Kibana base URL (e.g., https://my-deployment.kb.us-east-1.aws.elastic.cloud)
KIBANA_API_KEY	No	API key for authentication (preferred)
KIBANA_USERNAME	No	Username for basic auth (falls back to ELASTICSEARCH_USERNAME)
KIBANA_PASSWORD	No	Password for basic auth (falls back to ELASTICSEARCH_PASSWORD)
KIBANA_SPACE_ID	No	Kibana space ID (omit for default space)
KIBANA_INSECURE	No	Set to true to skip TLS verification

Provide either KIBANA_API_KEY or KIBANA_USERNAME + KIBANA_PASSWORD.

Agent Management
Create an Agent
Step 1: List available tools
node skills/kibana/agent-builder/scripts/agent-builder.js list-tools


If the script reports a connection error, stop and tell the user to verify their KIBANA_URL and authentication environment variables.

Review the list of available tools. Tools prefixed with platform.core. are built-in. Other tools are custom or connector-provided.

Step 2: List existing agents
node skills/kibana/agent-builder/scripts/agent-builder.js list-agents


This helps avoid name conflicts and shows what is already configured.

Step 3: Gather agent details

Using $ARGUMENTS as the default name, confirm or collect from the user:

Name (required) — The agent's display name. Default: $ARGUMENTS.
Description (optional) — Brief description of what the agent does. Default: same as name.
System instructions (optional) — Custom system prompt for the agent. Default: none.
Step 4: Select tools

Present the available tools from Step 1 and ask the user which ones to include. Suggest a reasonable default based on the agent's purpose. Let the user add or remove tools from the suggested list.

Step 5: Create the agent
node skills/kibana/agent-builder/scripts/agent-builder.js create-agent \
  --name "<agent_name>" \
  --description "<description>" \
  --instructions "<system_instructions>" \
  --tool-ids "<tool_id_1>,<tool_id_2>,<tool_id_3>"


Where:

--name is required
--tool-ids is a comma-separated list of tool IDs from Step 4
--description defaults to the name if omitted
--instructions can be omitted if the user did not provide any
Step 6: Verify creation
node skills/kibana/agent-builder/scripts/agent-builder.js list-agents


Show the user the newly created agent entry. If it appears, report success. If not, show any error output from Step 5.

Get an Agent
node skills/kibana/agent-builder/scripts/agent-builder.js get-agent --id "<agent_id>"

Update an Agent
node skills/kibana/agent-builder/scripts/agent-builder.js update-agent \
  --id "<agent_id>" \
  --description "<new_description>" \
  --instructions "<new_instructions>" \
  --tool-ids "<tool_id_1>,<tool_id_2>"


All flags except --id are optional — only provided fields are updated. The agent's id and name are immutable.

API constraint: PUT only accepts description, configuration, and tags. Including id, name, or type causes a 400 error.

Delete an Agent
node skills/kibana/agent-builder/scripts/agent-builder.js delete-agent --id "<agent_id>"


Always confirm with the user before deleting. Deletion is permanent.

Chat with an Agent
node skills/kibana/agent-builder/scripts/agent-builder.js chat \
  --id "<agent_id>" \
  --message "<user_message>"


Uses the streaming endpoint POST /api/agent_builder/converse/async with agent_id and input in the request body. Output shows [Reasoning], [Tool Call], [Tool Result], and [Response] as events arrive. Pass --conversation-id to continue an existing conversation.

Note: This command may take 30-60 seconds as the agent reasons and calls tools. Use a longer timeout (e.g., 120s or 180s) when running via Bash.

Tool Management

Custom tools extend what agents can do beyond the built-in platform tools.

Tool Types
ES|QL Tools

Pre-defined, parameterized ES|QL queries. Use when you need guaranteed query correctness, enforced business rules, analytics aggregations, or fine-grained data access control.

Parameter syntax: Use ?param_name in the query. Define each parameter with type and description only. Valid types: string, integer, float, boolean, date, array.

{
  "id": "campaign_revenue_by_region",
  "type": "esql",
  "description": "Calculates confirmed revenue for a region by quarter.",
  "configuration": {
    "query": "FROM finance-orders-* | WHERE order_status == \"completed\" AND region == ?region | STATS total_revenue = SUM(amount) BY quarter | LIMIT 10",
    "params": {
      "region": {
        "type": "string",
        "description": "Region code, e.g. 'US', 'EU', 'APAC'"
      }
    }
  }
}

Index Search Tools

Scope the built-in search capability to a specific index pattern. The LLM decides how to query; you control which indices are accessible.

{
  "id": "customer_feedback_search",
  "type": "index_search",
  "description": "Searches customer feedback and support tickets.",
  "configuration": {
    "pattern": "customer-feedback-*"
  }
}

Workflow Tools

Connect an agent to an Elastic Workflow — a YAML-defined multi-step automation. Use when the agent needs to take action beyond data retrieval (send notifications, create tickets, call external APIs).

{
  "id": "investigate-alert-workflow",
  "type": "workflow",
  "description": "Triggers automated alert investigation.",
  "configuration": {
    "workflow_id": "security-alert-investigation"
  }
}


Parameters are auto-detected from the workflow's inputs section.

Tool API Constraints

Read these before creating tools — violations cause 400 errors.

POST body fields: Only id, type, description, configuration, and tags are accepted. name is not a valid field — omit it entirely.
params is always required for ES|QL tools, even when empty — use "params": {}.
Param fields: Only type and description are accepted per parameter. default and optional are not valid and cause 400 errors. Hard-code sensible defaults in the query instead.
Index search config: Use "pattern", not "index". Using "index" causes a validation error.
PUT restrictions: Only description, configuration, and tags are accepted. Including id or type causes a 400 error — these fields are immutable after creation.
Tool Script Commands
List all tools
node skills/kibana/agent-builder/scripts/agent-builder.js list-custom-tools

Get a specific tool
node skills/kibana/agent-builder/scripts/agent-builder.js get-tool --id "<tool_id>"

Create a tool
node skills/kibana/agent-builder/scripts/agent-builder.js create-tool \
  --id "<tool_id>" \
  --type "esql" \
  --description "<description>" \
  --query "<esql_query>" \
  --params '{"region": {"type": "string", "description": "Region code"}}'


For index search tools:

node skills/kibana/agent-builder/scripts/agent-builder.js create-tool \
  --id "<tool_id>" \
  --type "index_search" \
  --description "<description>" \
  --pattern "my-index-*"


For workflow tools:

node skills/kibana/agent-builder/scripts/agent-builder.js create-tool \
  --id "<tool_id>" \
  --type "workflow" \
  --description "<description>" \
  --workflow-id "my-workflow-name"

Update a tool
node skills/kibana/agent-builder/scripts/agent-builder.js update-tool \
  --id "<tool_id>" \
  --description "<new_description>" \
  --query "<new_query>"


Only description, configuration, and tags can be updated. id and type are immutable.

Delete a tool
node skills/kibana/agent-builder/scripts/agent-builder.js delete-tool --id "<tool_id>"

Test a tool
node skills/kibana/agent-builder/scripts/agent-builder.js test-tool \
  --id "<tool_id>" \
  --params '{"region": "US"}'


Executes the tool via POST /api/agent_builder/tools/_execute and displays column names and row counts for ES|QL results.

Examples
Create an agent
User: /kibana-agent-builder sales-helper

List tools — finds platform.core.search, platform.core.list_indices, and a custom esql-sales-data tool
List agents — no conflicts
Name: "sales-helper", Description: "Helps query sales data"
Tools: esql-sales-data, platform.core.search, platform.core.list_indices
Create with --name "sales-helper" --tool-ids "esql-sales-data,platform.core.search,platform.core.list_indices"
Verify — agent appears in list
Update an agent's instructions
User: Update the sales-helper agent to focus on the APAC region

Get agent — get-agent --id "sales-helper" to see current config
Update — update-agent --id "sales-helper" --instructions "Focus on APAC sales data. Use esql-sales-data for queries."
Verify — get-agent --id "sales-helper" to confirm new instructions
Chat with an agent
User: Ask sales-helper what the top revenue products are

Chat — chat --id "sales-helper" --message "What are the top revenue products?"
Display the agent's response
Create an ES|QL tool with parameters
User: Create a tool that shows billing complaints by category for the last N days


Consult the elasticsearch-esql skill for ES|QL syntax

Create tool:

node skills/kibana/agent-builder/scripts/agent-builder.js create-tool \
  --id "billing_complaint_summary" \
  --type "esql" \
  --description "Returns billing complaints grouped by sub-category for the last N days." \
  --query "FROM customer-feedback-* | WHERE @timestamp >= NOW() - ?days::integer * 1d AND MATCH(feedback_text, 'billing') | STATS count = COUNT(*) BY sub_category | SORT count DESC | LIMIT 10" \
  --params '{"days": {"type": "integer", "description": "Number of days to look back"}}'


Test: test-tool --id "billing_complaint_summary" --params '{"days": 30}'

Create an index search tool
User: Create a tool to search support transcripts

node skills/kibana/agent-builder/scripts/agent-builder.js create-tool \
  --id "transcript_search" \
  --type "index_search" \
  --description "Searches support call transcripts by topic, agent, or customer issue." \
  --pattern "support-transcripts"

References

Read these for detailed guidance:

references/architecture-guide.md — Core concepts, built-in tools, context engineering, best practices, token optimization, REST API endpoints, MCP/A2A integration, permissions
references/use-cases.md — Full playbooks for Customer Feedback Analysis, Marketing Campaign Analysis, and Contract Analysis agents

For ES|QL syntax, functions, operators, and parameter rules, use the elasticsearch-esql skill. For workflow YAML structure, trigger types, step types, and agent-workflow patterns, use the security-workflows skill.

Guidelines
Always run list-tools before creating an agent so the user can choose from real, available tools.
Always run list-agents before and after creation to detect conflicts and verify success.
Do not invent tool IDs — only use IDs returned by list-tools.
If no custom tools exist yet, suggest creating one or using the built-in platform tools.
The agent ID is auto-generated from the name (lowercased, hyphens, alphanumeric only).
For non-default Kibana spaces, set KIBANA_SPACE_ID before running the script.
Confirm with the user before running delete-agent or delete-tool — deletion is permanent.
Always include | LIMIT N in ES|QL queries to prevent context window overflow.
Write descriptive tool descriptions — the agent decides which tool to call based solely on the description.
Scope index search tools narrowly (e.g., customer-feedback-* not *).
Use KEEP to return only needed columns and reduce token consumption.
Validate ES|QL queries with test-tool before assigning to an agent.
For ES|QL tools with no parameters, still include "params": {}.
Weekly Installs
468
Repository
elastic/agent-skills
GitHub Stars
451
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass