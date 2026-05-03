---
title: n8n-v2
url: https://skills.sh/splinesreticulating/n8n-v2-workflow-skill/n8n-v2
---

# n8n-v2

skills/splinesreticulating/n8n-v2-workflow-skill/n8n-v2
n8n-v2
Installation
$ npx skills add https://github.com/splinesreticulating/n8n-v2-workflow-skill --skill n8n-v2
SKILL.md
n8n v2.0 Workflow Development
Overview

Comprehensive reference for building n8n workflows using v2.0 patterns and best practices. This skill provides complete documentation for nodes, expressions, patterns, troubleshooting, and production-ready examples.

Quick Start Guide
1. Test APIs First
curl -X GET "https://api.example.com/endpoint" \
  -H "Authorization: Bearer $TOKEN"

2. Create Workflow JSON

Generate workflow JSON with nodes and connections.

3. Import into n8n

n8n UI > Settings > Import from File

4. Configure & Fix
Replace Execute Sub-Workflow nodes (if needed)
Configure credentials
Test each node
5. Test Execution

Use MCP server mcp__n8n__execute_workflow or manual trigger

Core Concepts
n8n MCP Server Integration

What it CAN do:

✅ Search workflows
✅ View workflow details
✅ Execute workflows

What it CANNOT do:

❌ Create workflows
❌ Modify workflows
❌ Manage credentials

Workaround: Generate JSON files, import via UI

📖 Deep dive: references/mcp-limitations.md

Node Library

Complete reference for all n8n nodes:

Trigger Nodes: Manual Trigger, Execute Workflow Trigger Data Processing: Code, Set, Merge, Filter, Split in Batches Flow Control: IF, Wait Integration: HTTP Request, RSS Feed Read Action: Execute Workflow, Respond to Webhook

Each node documented with configuration examples, parameters, and patterns.

📖 Complete reference: references/node-library.md

Expression Syntax

Dynamic values in node parameters using ={{ expression }}:

{{ $json.field }}                      // Current item
{{ $('Node Name').first().json.field }} // Cross-node
{{ $json.url || 'default' }}           // Fallback
{{ new Date().toISOString() }}         // Date/time
`urn:li:person:${$json.sub}`          // Template literal


📖 Complete guide: references/expression-syntax.md

Common Workflows
Human-in-the-Loop Approval

Use Wait nodes with forms (NOT respondToWebhook):

Trigger → Generate Content → Wait Node (form) → IF → Action


📖 Complete patterns: references/wait-nodes-guide.md

Multi-Workflow Orchestration

Orchestrator coordinates sub-workflows:

Main Orchestrator
├── Trigger
├── Execute Sub-Workflow: Data Fetcher
├── Wait Node: Review
├── Execute Sub-Workflow: Processor
└── Execute Sub-Workflow: Output


📖 All patterns: references/workflow-patterns.md

News Aggregation

Multi-source data fetch, normalize, merge, deduplicate, rank:

Trigger
├── HTTP Request: Source 1 → Normalize
├── HTTP Request: Source 2 → Normalize
└── RSS Feed: Source 3 → Normalize
    → Merge → Deduplicate → Rank


📖 Detailed patterns: references/workflow-patterns.md

AI Content Generation

Sub-workflow pattern for AI content:

Execute Workflow Trigger
→ Code: Build Prompt
→ HTTP Request: AI API
→ Code: Extract Response


📖 Implementation: references/workflow-patterns.md

Critical Issues & Solutions
Execute Sub-Workflow "Out of Date" Error

Problem: Imported nodes show error after import

Solution:

Delete old Execute Sub-Workflow nodes
Add fresh nodes from palette
Select "Database" and choose workflow

📖 Detailed troubleshooting: references/execute-sub-workflow-issues.md

Wait Node Not Pausing

❌ Wrong: respondToWebhook, Set nodes, IF on unset fields ✅ Correct: Wait node with resume: "form"

📖 Complete guide: references/wait-nodes-guide.md

LinkedIn unauthorized_scope_error

❌ Turn OFF both: "Organization Support" and "Legacy" toggles

📖 All auth issues: references/api-credentials.md

Templates & Examples
Basic Templates

Starting points for common structures:

assets/templates/wait-node-approval-template.json
assets/templates/orchestrator-template.json
assets/templates/sub-workflow-template.json
Complete Workflow Examples

Production-ready workflows you can import and use:

News Aggregation - Multi-source fetch, normalize, deduplicate, rank assets/examples/news-aggregation-workflow.json

Content Generation - AI-powered content creation sub-workflow assets/examples/content-generation-workflow.json

LinkedIn Member ID - Retrieve your LinkedIn member URN assets/examples/linkedin-member-id-workflow.json

Multi-Source Deduplication - Merge and deduplicate pattern assets/examples/multi-source-deduplication-workflow.json

Code Snippet Library

Reusable JavaScript for Code nodes:

Deduplication - Remove duplicates by URL, title, ID, or multiple fields code-snippets/deduplication.js

Ranking Algorithms - Multi-factor ranking (relevance, recency, engagement) code-snippets/ranking-algorithms.js

Data Normalization - Unify data from different API sources code-snippets/data-normalization.js

Form Data Preparation - Format data for Wait node forms code-snippets/form-data-preparation.js

Cross-Node Data Access - Reference data from other nodes code-snippets/cross-node-data-access.js

API Credentials Quick Reference

LinkedIn OAuth2:

Scopes: openid, profile, w_member_social
❌ OFF: Organization Support, Legacy
URN format: urn:li:person:{id}

Anthropic API:

Header: x-api-key
Model: claude-3-5-sonnet-20241022
Temp: 0.7, Max tokens: 400

NewsAPI:

Header: X-Api-Key
Endpoints: /v2/everything, /v2/top-headlines
Free tier: 100 requests/day

📖 Complete setup: references/api-credentials.md

Reference Documentation
Core References
node-library.md - Comprehensive node documentation
expression-syntax.md - Complete expression guide
workflow-patterns.md - Common workflow architectures
wait-nodes-guide.md - Human-in-the-loop patterns
api-credentials.md - Authentication setup
mcp-limitations.md - MCP server constraints
execute-sub-workflow-issues.md - Sub-workflow troubleshooting
troubleshooting.md - Common issues and solutions
Official n8n Documentation
n8n Documentation
Execute Sub-Workflow Node
Sub-workflows Guide
Wait Node
Weekly Installs
15
Repository
splinesreticula…ow-skill
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn