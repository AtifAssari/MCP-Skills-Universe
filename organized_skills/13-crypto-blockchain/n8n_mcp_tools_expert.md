---
rating: ⭐⭐
title: n8n-mcp-tools-expert
url: https://skills.sh/czlonkowski/n8n-skills/n8n-mcp-tools-expert
---

# n8n-mcp-tools-expert

skills/czlonkowski/n8n-skills/n8n-mcp-tools-expert
n8n-mcp-tools-expert
Installation
$ npx skills add https://github.com/czlonkowski/n8n-skills --skill n8n-mcp-tools-expert
Summary

Comprehensive guide for building n8n workflows using MCP tools with node discovery, validation, and workflow management.

Provides four tool categories: node discovery (search, get details), configuration validation with multiple profiles, workflow management (create, update, deploy), and access to 2,700+ templates
Critical distinction between nodeType formats: nodes-base.* for search/validate tools versus n8n-nodes-base.* for workflow creation and updates
Validation profiles (minimal, runtime, ai-friendly, strict) and detail levels (standard recommended, full for debugging) prevent common configuration errors and token waste
Iterative workflow building pattern with 56-second average between edits, auto-sanitization on all nodes, and smart parameters (branch, case) for multi-output node connections
Includes performance benchmarks, common mistakes, and unified tool reference covering get_node modes, validate_node profiles, and template deployment
SKILL.md
n8n MCP Tools Expert

Master guide for using n8n-mcp MCP server tools to build workflows.

Tool Categories

n8n-mcp provides tools organized into categories:

Node Discovery → SEARCH_GUIDE.md
Configuration Validation → VALIDATION_GUIDE.md
Workflow Management → WORKFLOW_GUIDE.md
Template Library - Search and deploy 2,700+ real workflows
Data Tables - Manage n8n data tables and rows (n8n_manage_datatable)
Credential Management - Full credential CRUD + schema discovery (n8n_manage_credentials)
Security & Audit - Instance security auditing with custom deep scan (n8n_audit_instance)
Documentation & Guides - Tool docs, AI agent guide, Code node guides
Quick Reference
Most Used Tools (by success rate)
Tool	Use When	Speed
search_nodes	Finding nodes by keyword	<20ms
get_node	Understanding node operations (detail="standard")	<10ms
validate_node	Checking configurations (mode="full")	<100ms
n8n_create_workflow	Creating workflows	100-500ms
n8n_update_partial_workflow	Editing workflows (MOST USED!)	50-200ms
validate_workflow	Checking complete workflow	100-500ms
n8n_deploy_template	Deploy template to n8n instance	200-500ms
n8n_manage_datatable	Managing data tables and rows	50-500ms
n8n_manage_credentials	Credential CRUD + schema discovery	50-500ms
n8n_audit_instance	Security audit (built-in + custom scan)	500-5000ms
n8n_autofix_workflow	Auto-fix validation errors	200-1500ms
Tool Selection Guide
Finding the Right Node

Workflow:

1. search_nodes({query: "keyword"})
2. get_node({nodeType: "nodes-base.name"})
3. [Optional] get_node({nodeType: "nodes-base.name", mode: "docs"})


Example:

// Step 1: Search
search_nodes({query: "slack"})
// Returns: nodes-base.slack

// Step 2: Get details
get_node({nodeType: "nodes-base.slack"})
// Returns: operations, properties, examples (standard detail)

// Step 3: Get readable documentation
get_node({nodeType: "nodes-base.slack", mode: "docs"})
// Returns: markdown documentation


Common pattern: search → get_node (18s average)

Validating Configuration

Workflow:

1. validate_node({nodeType, config: {}, mode: "minimal"}) - Check required fields
2. validate_node({nodeType, config, profile: "runtime"}) - Full validation
3. [Repeat] Fix errors, validate again


Common pattern: validate → fix → validate (23s thinking, 58s fixing per cycle)

Managing Workflows

Workflow:

1. n8n_create_workflow({name, nodes, connections})
2. n8n_validate_workflow({id})
3. n8n_update_partial_workflow({id, operations: [...]})
4. n8n_validate_workflow({id}) again
5. n8n_update_partial_workflow({id, operations: [{type: "activateWorkflow"}]})


Common pattern: iterative updates (56s average between edits)

Critical: nodeType Formats

Two different formats for different tools!

Format 1: Search/Validate Tools
// Use SHORT prefix
"nodes-base.slack"
"nodes-base.httpRequest"
"nodes-base.webhook"
"nodes-langchain.agent"


Tools that use this:

search_nodes (returns this format)
get_node
validate_node
validate_workflow
Format 2: Workflow Tools
// Use FULL prefix
"n8n-nodes-base.slack"
"n8n-nodes-base.httpRequest"
"n8n-nodes-base.webhook"
"@n8n/n8n-nodes-langchain.agent"


Tools that use this:

n8n_create_workflow
n8n_update_partial_workflow
Conversion
// search_nodes returns BOTH formats
{
  "nodeType": "nodes-base.slack",          // For search/validate tools
  "workflowNodeType": "n8n-nodes-base.slack"  // For workflow tools
}

Common Mistakes
Mistake 1: Wrong nodeType Format

Problem: "Node not found" error

// WRONG
get_node({nodeType: "slack"})  // Missing prefix
get_node({nodeType: "n8n-nodes-base.slack"})  // Wrong prefix

// CORRECT
get_node({nodeType: "nodes-base.slack"})

Mistake 2: Using detail="full" by Default

Problem: Huge payload, slower response, token waste

// WRONG - Returns 3-8K tokens, use sparingly
get_node({nodeType: "nodes-base.slack", detail: "full"})

// CORRECT - Returns 1-2K tokens, covers 95% of use cases
get_node({nodeType: "nodes-base.slack"})  // detail="standard" is default
get_node({nodeType: "nodes-base.slack", detail: "standard"})


When to use detail="full":

Debugging complex configuration issues
Need complete property schema with all nested options
Exploring advanced features

Better alternatives:

get_node({detail: "standard"}) - for operations list (default)
get_node({mode: "docs"}) - for readable documentation
get_node({mode: "search_properties", propertyQuery: "auth"}) - for specific property
Mistake 3: Not Using Validation Profiles

Problem: Too many false positives OR missing real errors

Profiles:

minimal - Only required fields (fast, permissive)
runtime - Values + types (recommended for pre-deployment)
ai-friendly - Reduce false positives (for AI configuration)
strict - Maximum validation (for production)
// WRONG - Uses default profile
validate_node({nodeType, config})

// CORRECT - Explicit profile
validate_node({nodeType, config, profile: "runtime"})

Mistake 4: Ignoring Auto-Sanitization

What happens: ALL nodes sanitized on ANY workflow update

Auto-fixes:

Binary operators (equals, contains) → removes singleValue
Unary operators (isEmpty, isNotEmpty) → adds singleValue: true
IF/Switch nodes → adds missing metadata

Cannot fix:

Broken connections
Branch count mismatches
Paradoxical corrupt states
// After ANY update, auto-sanitization runs on ALL nodes
n8n_update_partial_workflow({id, operations: [...]})
// → Automatically fixes operator structures

Mistake 5: Not Using Smart Parameters

Problem: Complex sourceIndex calculations for multi-output nodes

Old way (manual):

// IF node connection
{
  type: "addConnection",
  source: "IF",
  target: "Handler",
  sourceIndex: 0  // Which output? Hard to remember!
}


New way (smart parameters):

// IF node - semantic branch names
{
  type: "addConnection",
  source: "IF",
  target: "True Handler",
  branch: "true"  // Clear and readable!
}

{
  type: "addConnection",
  source: "IF",
  target: "False Handler",
  branch: "false"
}

// Switch node - semantic case numbers
{
  type: "addConnection",
  source: "Switch",
  target: "Handler A",
  case: 0
}

Mistake 7: Wrong Parameter Name for updateNode

Problem: Using parameters instead of updates

// WRONG
n8n_update_partial_workflow({
  id: "wf-123",
  operations: [{
    type: "updateNode",
    nodeName: "HTTP Request",
    parameters: {url: "..."}  // ❌ Wrong key
  }]
})

// CORRECT
n8n_update_partial_workflow({
  id: "wf-123",
  operations: [{
    type: "updateNode",
    nodeName: "HTTP Request",
    updates: {url: "..."}  // ✅ Correct key
  }]
})

Mistake 8: Wrong Credential Attachment Format

Problem: Credentials not attaching to nodes

// WRONG - credentials as flat object
updates: {credentials: "myApiKey"}

// CORRECT - credentials nested by type with id and name
updates: {
  credentials: {
    httpHeaderAuth: {
      id: "abc123",
      name: "My API Key"
    }
  }
}

Mistake 6: Not Using intent Parameter

Problem: Less helpful tool responses

// WRONG - No context for response
n8n_update_partial_workflow({
  id: "abc",
  operations: [{type: "addNode", node: {...}}]
})

// CORRECT - Better AI responses
n8n_update_partial_workflow({
  id: "abc",
  intent: "Add error handling for API failures",
  operations: [{type: "addNode", node: {...}}]
})

Tool Usage Patterns
Pattern 1: Node Discovery (Most Common)

Common workflow: 18s average between steps

// Step 1: Search (fast!)
const results = await search_nodes({
  query: "slack",
  mode: "OR",  // Default: any word matches
  limit: 20
});
// → Returns: nodes-base.slack, nodes-base.slackTrigger

// Step 2: Get details (~18s later, user reviewing results)
const details = await get_node({
  nodeType: "nodes-base.slack",
  includeExamples: true  // Get real template configs
});
// → Returns: operations, properties, metadata

Pattern 2: Validation Loop

Typical cycle: 23s thinking, 58s fixing

// Step 1: Validate
const result = await validate_node({
  nodeType: "nodes-base.slack",
  config: {
    resource: "channel",
    operation: "create"
  },
  profile: "runtime"
});

// Step 2: Check errors (~23s thinking)
if (!result.valid) {
  console.log(result.errors);  // "Missing required field: name"
}

// Step 3: Fix config (~58s fixing)
config.name = "general";

// Step 4: Validate again
await validate_node({...});  // Repeat until clean

Pattern 3: Workflow Editing

Most used update tool: 99.0% success rate, 56s average between edits

// Iterative workflow building (NOT one-shot!)
// Edit 1
await n8n_update_partial_workflow({
  id: "workflow-id",
  intent: "Add webhook trigger",
  operations: [{type: "addNode", node: {...}}]
});

// ~56s later...

// Edit 2
await n8n_update_partial_workflow({
  id: "workflow-id",
  intent: "Connect webhook to processor",
  operations: [{type: "addConnection", source: "...", target: "..."}]
});

// ~56s later...

// Edit 3 (validation)
await n8n_validate_workflow({id: "workflow-id"});

// Ready? Activate!
await n8n_update_partial_workflow({
  id: "workflow-id",
  intent: "Activate workflow for production",
  operations: [{type: "activateWorkflow"}]
});

Detailed Guides
Node Discovery Tools

See SEARCH_GUIDE.md for:

search_nodes
get_node with detail levels (minimal, standard, full)
get_node modes (info, docs, search_properties, versions)
Validation Tools

See VALIDATION_GUIDE.md for:

Validation profiles explained
validate_node with modes (minimal, full)
validate_workflow complete structure
Auto-sanitization system
Handling validation errors
Workflow Management

See WORKFLOW_GUIDE.md for:

n8n_create_workflow
n8n_update_partial_workflow (19 operation types including patchNodeField!)
Smart parameters (branch, case)
AI connection types (8 types)
Workflow activation (activateWorkflow/deactivateWorkflow)
n8n_deploy_template
n8n_workflow_versions
n8n_manage_credentials (credential CRUD + schema discovery)
n8n_audit_instance (security auditing)
Template Usage
Search Templates
// Search by keyword (default mode)
search_templates({
  query: "webhook slack",
  limit: 20
});

// Search by node types
search_templates({
  searchMode: "by_nodes",
  nodeTypes: ["n8n-nodes-base.httpRequest", "n8n-nodes-base.slack"]
});

// Search by task type
search_templates({
  searchMode: "by_task",
  task: "webhook_processing"
});

// Search by metadata (complexity, setup time)
search_templates({
  searchMode: "by_metadata",
  complexity: "simple",
  maxSetupMinutes: 15
});

Get Template Details
get_template({
  templateId: 2947,
  mode: "structure"  // nodes+connections only
});

get_template({
  templateId: 2947,
  mode: "full"  // complete workflow JSON
});

Deploy Template Directly
// Deploy template to your n8n instance
n8n_deploy_template({
  templateId: 2947,
  name: "My Weather to Slack",  // Custom name (optional)
  autoFix: true,  // Auto-fix common issues (default)
  autoUpgradeVersions: true  // Upgrade node versions (default)
});
// Returns: workflow ID, required credentials, fixes applied

Data Table Management
n8n_manage_datatable

Unified tool for managing n8n data tables and rows. Supports CRUD operations on tables and rows with filtering, pagination, and dry-run support.

Table Actions: createTable, listTables, getTable, updateTable, deleteTable Row Actions: getRows, insertRows, updateRows, upsertRows, deleteRows

// Create a data table
n8n_manage_datatable({
  action: "createTable",
  name: "Contacts",
  columns: [
    {name: "email", type: "string"},
    {name: "score", type: "number"}
  ]
})

// Get rows with filter
n8n_manage_datatable({
  action: "getRows",
  tableId: "dt-123",
  filter: {
    filters: [{columnName: "status", condition: "eq", value: "active"}]
  },
  limit: 50
})

// Insert rows
n8n_manage_datatable({
  action: "insertRows",
  tableId: "dt-123",
  data: [{email: "a@b.com", score: 10}],
  returnType: "all"
})

// Update with dry run (preview changes)
n8n_manage_datatable({
  action: "updateRows",
  tableId: "dt-123",
  filter: {filters: [{columnName: "score", condition: "lt", value: 5}]},
  data: {status: "inactive"},
  dryRun: true
})

// Upsert (update or insert)
n8n_manage_datatable({
  action: "upsertRows",
  tableId: "dt-123",
  filter: {filters: [{columnName: "email", condition: "eq", value: "a@b.com"}]},
  data: {score: 15},
  returnData: true
})


Filter conditions: eq, neq, like, ilike, gt, gte, lt, lte

Best practices:

Use dryRun: true before bulk updates/deletes to verify filter correctness
Define column types upfront (string, number, boolean, date)
Use returnType: "count" (default) for insertRows to minimize response size
deleteRows requires a filter - cannot delete all rows without one
Credential Management
n8n_manage_credentials

Unified tool for managing n8n credentials. Supports full CRUD operations and schema discovery.

Actions: list, get, create, update, delete, getSchema

// List all credentials
n8n_manage_credentials({action: "list"})
// → Returns: id, name, type, createdAt, updatedAt (never exposes secrets)

// Get credential by ID
n8n_manage_credentials({action: "get", id: "123"})
// → Returns: credential metadata (data field stripped for security)

// Discover required fields for a credential type
n8n_manage_credentials({action: "getSchema", credentialType: "httpHeaderAuth"})
// → Returns: required fields, types, descriptions

// Create credential
n8n_manage_credentials({
  action: "create",
  name: "My Slack Token",
  type: "slackApi",
  data: {accessToken: "xoxb-..."}
})

// Update credential
n8n_manage_credentials({
  action: "update",
  id: "123",
  name: "Updated Name",
  data: {accessToken: "xoxb-new-..."},
  type: "slackApi"  // Optional, needed by some n8n versions
})

// Delete credential
n8n_manage_credentials({action: "delete", id: "123"})


Security:

get, create, and update responses strip the data field (defense-in-depth)
get action falls back to list+filter if direct GET returns 403/405 (not all n8n versions expose this endpoint)
Credential request bodies are redacted from debug logs

Best practices:

Use getSchema before create to discover required fields for a credential type
The data field contains the actual secret values — provide it only on create/update
Always verify credential creation by listing afterward
Security & Audit
n8n_audit_instance

Security audit tool that combines n8n's built-in audit with custom deep scanning of all workflows.

// Full audit (default — runs both built-in + custom scan)
n8n_audit_instance()

// Built-in audit only (specific categories)
n8n_audit_instance({
  categories: ["credentials", "nodes"],
  includeCustomScan: false
})

// Custom scan only (specific checks)
n8n_audit_instance({
  customChecks: ["hardcoded_secrets", "unauthenticated_webhooks"]
})


Built-in audit categories: credentials, database, nodes, instance, filesystem

Custom deep scan checks:

hardcoded_secrets — Detects 50+ patterns for API keys, tokens, passwords (OpenAI, AWS, Stripe, GitHub, Slack, etc.) plus PII (email, phone, credit card). Secrets are masked in output (first 6 + last 4 chars).
unauthenticated_webhooks — Flags webhook/form triggers without authentication
error_handling — Flags workflows with 3+ nodes and no error handling
data_retention — Flags workflows saving all execution data (success + failure)

Parameters (all optional):

categories — Array of built-in audit categories
includeCustomScan — Boolean (default: true)
customChecks — Array subset of the 4 custom checks
daysAbandonedWorkflow — Days threshold for abandoned workflow detection

Output: Actionable markdown report with:

Summary table (critical/high/medium/low finding counts)
Findings grouped by workflow
Remediation Playbook with three sections:
Auto-fixable — Items you can fix with tool chains (e.g., add auth to webhooks)
Requires review — Items needing human judgment (e.g., PII detection)
Requires user action — Items needing manual intervention (e.g., rotate exposed keys)
Self-Help Tools
Get Tool Documentation
// Overview of all tools
tools_documentation()

// Specific tool details
tools_documentation({
  topic: "search_nodes",
  depth: "full"
})

// Code node guides
tools_documentation({topic: "javascript_code_node_guide", depth: "full"})
tools_documentation({topic: "python_code_node_guide", depth: "full"})

AI Agent Guide
// Comprehensive AI workflow guide
ai_agents_guide()
// Returns: Architecture, connections, tools, validation, best practices

// Or via tools_documentation
tools_documentation({topic: "ai_agents_guide", depth: "full"})

Health Check
// Quick health check
n8n_health_check()

// Detailed diagnostics
n8n_health_check({mode: "diagnostic"})
// → Returns: status, env vars, tool status, API connectivity

Tool Availability

Always Available (no n8n API needed):

search_nodes, get_node
validate_node, validate_workflow
search_templates, get_template
tools_documentation, ai_agents_guide

Requires n8n API (N8N_API_URL + N8N_API_KEY):

n8n_create_workflow
n8n_update_partial_workflow, n8n_update_full_workflow
n8n_validate_workflow (by ID)
n8n_list_workflows, n8n_get_workflow, n8n_delete_workflow
n8n_test_workflow
n8n_executions
n8n_deploy_template
n8n_workflow_versions
n8n_autofix_workflow
n8n_manage_datatable
n8n_manage_credentials
n8n_audit_instance

If API tools unavailable, use templates and validation-only workflows.

Unified Tool Reference
get_node (Unified Node Information)

Detail Levels (mode="info", default):

minimal (~200 tokens) - Basic metadata only
standard (~1-2K tokens) - Essential properties + operations (RECOMMENDED)
full (~3-8K tokens) - Complete schema (use sparingly)

Operation Modes:

info (default) - Node schema with detail level
docs - Readable markdown documentation
search_properties - Find specific properties (use with propertyQuery)
versions - List all versions with breaking changes
compare - Compare two versions
breaking - Show only breaking changes
migrations - Show auto-migratable changes
// Standard (recommended)
get_node({nodeType: "nodes-base.httpRequest"})

// Get documentation
get_node({nodeType: "nodes-base.webhook", mode: "docs"})

// Search for properties
get_node({nodeType: "nodes-base.httpRequest", mode: "search_properties", propertyQuery: "auth"})

// Check versions
get_node({nodeType: "nodes-base.executeWorkflow", mode: "versions"})

validate_node (Unified Validation)

Modes:

full (default) - Comprehensive validation with errors/warnings/suggestions
minimal - Quick required fields check only

Profiles (for mode="full"):

minimal - Very lenient
runtime - Standard (default, recommended)
ai-friendly - Balanced for AI workflows
strict - Most thorough (production)
// Full validation with runtime profile
validate_node({nodeType: "nodes-base.slack", config: {...}, profile: "runtime"})

// Quick required fields check
validate_node({nodeType: "nodes-base.webhook", config: {}, mode: "minimal"})

Performance Characteristics
Tool	Response Time	Payload Size
search_nodes	<20ms	Small
get_node (standard)	<10ms	~1-2KB
get_node (full)	<100ms	3-8KB
validate_node (minimal)	<50ms	Small
validate_node (full)	<100ms	Medium
validate_workflow	100-500ms	Medium
n8n_manage_credentials	50-500ms	Small-Medium
n8n_audit_instance	500-5000ms	Large
n8n_create_workflow	100-500ms	Medium
n8n_update_partial_workflow	50-200ms	Small
n8n_deploy_template	200-500ms	Medium
Best Practices
Do
For simple workflows (<=5 nodes), use MCP tools directly — don't over-engineer the investigation
Use patchNodeField for surgical edits to Code node content instead of replacing the entire node
Use get_node({detail: "standard"}) for most use cases
Specify validation profile explicitly (profile: "runtime")
Use smart parameters (branch, case) for clarity
Include intent parameter in workflow updates
Follow search → get_node → validate workflow
Iterate workflows (avg 56s between edits)
Validate after every significant change
Use includeExamples: true for real configs
Use n8n_deploy_template for quick starts
Don't
Use detail: "full" unless necessary (wastes tokens)
Forget nodeType prefix (nodes-base.*)
Skip validation profiles
Try to build workflows in one shot (iterate!)
Ignore auto-sanitization behavior
Use full prefix (n8n-nodes-base.*) with search/validate tools
Forget to activate workflows after building
Summary

Most Important:

Use get_node with detail: "standard" (default) - covers 95% of use cases
nodeType formats differ: nodes-base.* (search/validate) vs n8n-nodes-base.* (workflows)
Specify validation profiles (runtime recommended)
Use smart parameters (branch="true", case=0)
Include intent parameter in workflow updates
Auto-sanitization runs on ALL nodes during updates
Workflows can be activated via API (activateWorkflow operation)
Workflows are built iteratively (56s avg between edits)
Data tables managed with n8n_manage_datatable (CRUD + filtering)
Credentials managed with n8n_manage_credentials (CRUD + schema discovery)
Security audits via n8n_audit_instance (built-in + custom deep scan)
AI agent guide available via ai_agents_guide() tool

Common Workflow:

search_nodes → find node
get_node → understand config
validate_node → check config
n8n_create_workflow → build
n8n_validate_workflow → verify
n8n_update_partial_workflow → iterate
activateWorkflow → go live!

For details, see:

SEARCH_GUIDE.md - Node discovery
VALIDATION_GUIDE.md - Configuration validation
WORKFLOW_GUIDE.md - Workflow management

Related Skills:

n8n Expression Syntax - Write expressions in workflow fields
n8n Workflow Patterns - Architectural patterns from templates
n8n Validation Expert - Interpret validation errors
n8n Node Configuration - Operation-specific requirements
n8n Code JavaScript - Write JavaScript in Code nodes
n8n Code Python - Write Python in Code nodes
Weekly Installs
3.6K
Repository
czlonkowski/n8n-skills
GitHub Stars
4.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn