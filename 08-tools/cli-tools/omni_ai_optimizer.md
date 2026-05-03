---
title: omni-ai-optimizer
url: https://skills.sh/exploreomni/omni-agent-skills/omni-ai-optimizer
---

# omni-ai-optimizer

skills/exploreomni/omni-agent-skills/omni-ai-optimizer
omni-ai-optimizer
Installation
$ npx skills add https://github.com/exploreomni/omni-agent-skills --skill omni-ai-optimizer
SKILL.md
Omni AI Optimizer

Optimize your Omni semantic model so Blobby (the Omni Agent) returns accurate, contextual answers.

Tip: Use omni-model-explorer to inspect current AI context before making changes.

Prerequisites
# Verify the Omni CLI is installed — if not, ask the user to install it
# See: https://github.com/exploreomni/cli#readme
command -v omni >/dev/null || echo "ERROR: Omni CLI is not installed."

# Show available profiles and select the appropriate one
omni config show
# If multiple profiles exist, ask the user which to use, then switch:
omni config use <profile-name>


Requires Modeler or Connection Admin permissions.

Discovering Commands
omni models --help                    # List all model operations
omni models yaml-create --help        # Show flags for writing YAML


Tip: Use -o json to force structured output for programmatic parsing, or -o human for readable tables. The default is auto (human in a TTY, JSON when piped).

How Blobby Works

Blobby generates queries by examining:

Topic structure — which views and fields are joined
Field labels and descriptions — how fields are named
synonyms — alternative names for fields
ai_context — explicit instructions you write
ai_fields — which fields are visible to AI
sample_queries — example questions with correct queries
Hidden fields — hidden: true fields are excluded
ai_chat_topics — which topics are included/excluded from AI chat (model-level)

Impact order: ai_context > ai_fields > sample_queries > synonyms > field descriptions.

Writing ai_context

Add via the YAML API:

omni models yaml-create <modelId> --body '{
  "fileName": "order_transactions.topic",
  "yaml": "base_view: order_items\nlabel: Order Transactions\nai_context: |\n  Map \"revenue\" → total_revenue. Map \"orders\" → count.\n  Map \"customers\" → unique_users.\n  Status values: complete, pending, cancelled, returned.\n  Only complete orders for revenue unless specified otherwise.",
  "mode": "extension",
  "commitMessage": "Add AI context to order transactions topic"
}'

What Makes Good ai_context

Terminology mapping — map business language to field names:

ai_context: |
  "revenue" or "sales" → order_items.total_revenue
  "orders" → order_items.count
  "customers" → users.count or order_items.unique_users
  "AOV" → order_items.average_order_value


Data nuances — explain what isn't obvious from field names:

ai_context: |
  Each row is a line item, not an order. One order has multiple line items.
  total_revenue already excludes returns and cancellations.
  Dates are in UTC.


Behavioral guidance — direct common patterns:

ai_context: |
  For trends, default to weekly granularity, sort ascending.
  For "top N", sort descending and limit to 10.


Persona prompting — set the analytical perspective:

ai_context: |
  You are the head of finance analyzing customer payment data.
  Default to monetary values in USD with 2 decimal places.

Keeping Context Concise

Every token in ai_context, description, and label is sent to the AI on every query. Verbose values waste context window and push out other fields.

Target 1-2 sentences per ai_context entry. Focus on disambiguation and gotchas, not general explanation.
Keep labels short and human-readable — avoid redundant qualification (e.g., "Order Total Revenue Amount" → "Total Revenue").
Rewrite long description values to be direct. If a description restates the field name, remove it.
Curating Fields with ai_fields

The AI context window holds ~550 fields before truncation. If a topic approaches this limit, use ai_fields to curate which fields are included.

Reduce noise for large models:

ai_fields:
  - all_views.*
  - -tag:internal
  - -distribution_centers.*

# Or explicit list
ai_fields:
  - order_items.created_at
  - order_items.total_revenue
  - order_items.count
  - users.name
  - users.state
  - products.category


Same operators as topic fields: wildcard (*), negation (-), tags (tag:).

Controlling Topic Visibility with ai_chat_topics

ai_chat_topics is a model-level property that controls which topics Blobby can see:

No ai_chat_topics property (default) — Blobby can query across all topics.
ai_chat_topics: [] (empty list) — Blobby cannot query any topics. This effectively disables AI chat for the model.
Explicit list — only the listed topics (or tag matches) are available. Supports all_topics, tag selectors (tag:customer_facing), and negation (-tag:internal, -staging_events).

Check this first — if a topic isn't in ai_chat_topics, no amount of ai_context or ai_fields on it will matter. Use omni-model-builder to modify this property.

Adding sample_queries

Teach Blobby by example. Build the correct query in a workbook, retrieve its structure, then add to the topic YAML:

sample_queries:
  revenue_by_month:
    prompt: "What month has the highest revenue?"
    ai_context: "Use total_revenue grouped by month, sorted descending, limit 1"
    query:
      base_view: order_items
      fields:
        - order_items.created_at[month]
        - order_items.total_revenue
      topic: order_transactions
      limit: 1
      sorts:
        - field: order_items.total_revenue
          desc: true


Note: When exporting queries from Omni's workbook, you'll get JSON with table, join_paths_from_topic_name, and sorts using column_name/sort_descending. Map these to YAML as follows:

table → base_view
join_paths_from_topic_name → topic
column_name → field, sort_descending → desc
Workbook JSON includes filters, pivots, limit, column_limit which you can include in YAML (though filter syntax requires consulting the Model YAML API docs directly)

Focus on questions users actually ask — check Analytics > AI usage in Omni.

AI-Specific Topic Extensions

Create a curated topic variant for Blobby using extends:

# ai_order_transactions.topic
extends: [order_items]
label: AI - Order Transactions

fields:
  - order_items.created_at
  - order_items.status
  - order_items.total_revenue
  - order_items.count
  - users.name
  - users.state
  - products.category

ai_context: |
  Curated view of order data for AI analysis.
  [detailed context here]

sample_queries:
  top_categories_last_month:
    prompt: "Top selling categories last month?"
    query:
      base_view: order_items
      fields:
        - products.category
        - order_items.total_revenue
      topic: ai_order_transactions
      limit: 10
      sorts:
        - field: order_items.total_revenue
          desc: true

Improving Field Descriptions
dimensions:
  status:
    label: Order Status
    description: >
      Current fulfillment status. Values: complete, pending, cancelled, returned.
      Use 'complete' for revenue calculations.


Good descriptions help both Blobby and human analysts.

Enumerating Values for Categorical Fields

For closed-set enums, use all_values so Blobby knows every valid filter value:

dimensions:
  status:
    all_values: [complete, pending, cancelled, returned]
  payment_method:
    all_values: [credit_card, debit_card, bank_transfer, paypal, gift_card]


For open-ended categoricals where a full list isn't practical, use sample_values to give representative examples:

dimensions:
  product_category:
    sample_values: [Electronics, Clothing, Home & Garden, Sports, Books]
  city:
    sample_values: [New York, Los Angeles, Chicago, Houston, Phoenix]

Adding synonyms

Map alternative names, abbreviations, and domain-specific terminology so Blobby matches user queries to the correct field. Works on both dimensions and measures.

dimensions:
  customer_name:
    synonyms: [client, account, buyer, purchaser]
  order_date:
    synonyms: [purchase date, transaction date, order timestamp]

measures:
  total_revenue:
    synonyms: [sales, income, earnings, gross revenue, top line]
  average_order_value:
    synonyms: [AOV, avg order, basket size]


Synonyms vs ai_context: Use synonyms for field-level name mapping. Use ai_context for topic-level behavioral guidance, data nuances, and multi-field relationships.

Pruning caveat: When the model is large and context is tight, synonyms are pruned before descriptions. Reserve synonyms for high-value fields where users commonly use alternative names.

Avoid redundancy: Don't add synonyms that duplicate the field's label or field name — they add no signal and waste tokens.

Avoiding Duplication

ai_context and description serve different audiences. description is human-facing (shown in the field picker and docs). ai_context is an AI-only hint. Don't put the same text in both — ai_context should add guidance the description doesn't cover (disambiguation, gotchas, when to use one field over another).

Consolidate shared context at the view level. If multiple fields in a view share the same ai_context (e.g., "all monetary values are in USD"), move it to the view-level ai_context instead of repeating it on each field. Field-level ai_context should be specific to that field.

Example — before:

dimensions:
  gross_revenue:
    ai_context: "Monetary value in USD. This is revenue before refunds."
    description: "Monetary value in USD. This is revenue before refunds."
  net_revenue:
    ai_context: "Monetary value in USD. This is revenue after refunds."
    description: "Monetary value in USD. This is revenue after refunds."


After:

ai_context: "All monetary values in this view are in USD."

dimensions:
  gross_revenue:
    ai_context: "Revenue before refunds."
    description: "Total revenue before refunds and cancellations are applied."
  net_revenue:
    ai_context: "Revenue after refunds. Use this for profitability analysis."
    description: "Total revenue after refunds and cancellations."

Optimization Checklist

Prioritize high-impact changes. Improve wording without changing semantics.

Inspect current state with omni-model-explorer
Check model-level ai_chat_topics — ensure the right topics are visible to AI
Check AI usage dashboard for real user questions
Count fields — curate with ai_fields if approaching 550
Write ai_context mapping business terms to fields (keep to 1-2 sentences)
Add synonyms to key dimensions and measures (skip if they duplicate the label)
Improve field description and label values
Add all_values/sample_values for categorical fields
Add sample_queries for top 3-5 questions
Remove duplication between ai_context and description; consolidate shared context at view level
Consider extends for AI-specific topic variants
Test iteratively — ask Blobby and refine
Docs Reference
Optimizing Models for AI · Synonyms · Topic Parameters · Model YAML API · Omni AI Overview
Related Skills
omni-model-explorer — inspect existing AI context
omni-model-builder — modify views and topics
omni-query — test queries to verify Blobby's output
Weekly Installs
18
Repository
exploreomni/omn…t-skills
GitHub Stars
12
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass