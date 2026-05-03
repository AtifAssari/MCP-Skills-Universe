---
rating: ⭐⭐⭐
title: omni-model-explorer
url: https://skills.sh/exploreomni/omni-agent-skills/omni-model-explorer
---

# omni-model-explorer

skills/exploreomni/omni-agent-skills/omni-model-explorer
omni-model-explorer
Installation
$ npx skills add https://github.com/exploreomni/omni-agent-skills --skill omni-model-explorer
SKILL.md
Omni Model Explorer

Explore and understand an Omni semantic model through the Omni CLI. This is the starting point — understand what exists before building, querying, or modifying anything.

Tip: Start with the Shared model — it contains the curated analytics layer.

Prerequisites

Configure the Omni CLI:

# Verify the Omni CLI is installed — if not, ask the user to install it
# See: https://github.com/exploreomni/cli#readme
command -v omni >/dev/null || echo "ERROR: Omni CLI is not installed."

# Show available profiles and select the appropriate one
omni config show
# If multiple profiles exist, ask the user which to use, then switch:
omni config use <profile-name>


API keys: Settings > API Keys (Organization Admin) or User Profile > Manage Account > Generate Token (Personal Access Token).

Discovering Commands

When unsure what operations or flags are available:

omni models --help              # List all model operations
omni models <operation> --help  # Show flags and positional args


Tip: Use -o json to force structured output for programmatic parsing, or -o human for readable tables. The default is auto (human in a TTY, JSON when piped).

Core Workflow

Explore top-down: List models → Pick a model → List topics → Inspect a topic → Explore views and fields.

Step 1: List Available Models
omni models list


Returns models with id, name, connectionId, and modelKind (SCHEMA or SHARED). Use the SHARED model — it contains the curated semantic layer.

To also see active branches on each model:

omni models list --include activeBranches


Each model in the response will include a branches array. Each branch has an id (UUID) and name — use the id as the branchId parameter in other API calls.

Step 2: List Topics in a Model

Topics are entry points for querying. Each topic defines a base view and the set of joined views available.

omni models list-topics <modelId>


Returns topic names, base views, labels, and descriptions.

Step 3: Inspect a Topic

Get full detail including all views, dimensions, measures, relationships, and AI context:

omni models get-topic <modelId> <topicName>


The response includes:

base_view_name — the primary table
views[] — all accessible views, each with dimensions[] and measures[]
relationships[] — how views join together
default_filters — filters applied by default
ai_context — instructions for Blobby (Omni's AI)
Step 4: Read the Model YAML

For the full semantic model definition:

# All YAML files
omni models yaml-get <modelId>

# Specific file
omni models yaml-get <modelId> --filename order_items.view

# Regex filter
omni models yaml-get <modelId> --filename '.*sales.*'

# From a branch (branchId is a UUID from the list models response)
omni models yaml-get <modelId> --branchid <branchId>


The mode parameter: combined (default) merges schema + shared model; extension shows only shared model customizations.

Model Architecture

Omni has three layers:

Schema Model — auto-generated from your database (read-only)
Shared Model — analytics engineer customizations (dimensions, measures, labels, topics, AI context)
Workbook Model — per-dashboard customizations (ad-hoc, not shared)

When exploring, use the combined view to see everything available.

Key Concepts

Views correspond to database tables. Each has dimensions (groupable fields) and measures (aggregations).

Topics join views together into queryable units — curated starting points for analysis. A topic has a base view, joined views, default filters, and AI context.

Relationships define joins: join_from_view, join_to_view, on_sql, relationship_type (one_to_one, many_to_one, one_to_many, many_to_many), and join_type (always_left, inner, full_outer).

Field naming: view_name.field_name with bracket notation for date granularity: orders.created_at[week].

Exploration Patterns

"What data do we have about X?" — List topics → inspect the most relevant one → review views and fields.

"How do these tables relate?" — Inspect the topic's relationships[] — check join_from_view, join_to_view, on_sql, and relationship_type.

"What measures are available for Y?" — Inspect the topic containing view Y → review the measures[] array with aggregate_type and sql definitions.

Fallback: Expected View Missing from yaml-get

Use this pattern only when normal exploration comes up short — the user names a specific view and it's absent from the yaml-get or get-topic response, or a relationship references a view that doesn't appear. If yaml-get returned what you expected, skip this section.

Why it happens: yaml-get only returns views from currently-loaded schemas. If a schema is offloaded or inactive, its views won't show up. The get-schemas call surfaces all schemas the connection knows about — including offloaded and inactive ones — so it's the right next step before telling the user "not found."

Two-step recovery:

# 1. List every schema (loaded, offloaded, and inactive)
omni models get-schemas <modelId>
# → {"schemas": ["ANALYTICS", "PUBLIC", "STAGING", ...]}

# 2. If the target schema is in the list, load just that schema
omni models yaml-get <modelId> --includeschemas PUBLIC


If the schema isn't in the list at all, this isn't a lazy-load issue — the connection likely doesn't have access or the schema isn't synced. Check with a Connection Admin.

Rules for --includeschemas:

Accepts exactly one schema name per call — commas are rejected by the API. Load schemas one at a time if you need multiple.
When set, the response contains only views belonging to that schema. Relationships are preserved even when they reference views in other schemas.
To scope to a branch, add --branchid <id> to yaml-get or --branch-id <id> to get-schemas (the flag names differ per command — this matches the API's underlying casing).
Calculation Fields

Calculation fields in the model use a different format than regular dimensions/measures. The field key is calc_name and the expression property is sql_expression — not name/sql.

Field Impact Analysis

Assess the blast radius of a field migration or removal before pushing changes to dbt:

Create a model branch with omni-model-builder where the field is removed or renamed
Run the content validator against that branch:
omni models content-validator-get <modelId> --branch-id <branchId>


This returns all dashboards and tiles with broken references to the removed field.

Search model YAML for additional references (run in parallel with step 2):
omni models yaml-get <modelId> --filename '.*'


Search the response for the field name to find references in other views, topics, and calculated fields.

Report: Combine content-validator results (broken dashboards/tiles) with YAML search results (model references) into a structured blast-radius report.

Do NOT paginate documents and check queries individually — the content validator does this for you in one call.

Docs Reference
Models API · Topics API · Modeling Overview · Views · Topics · Dimensions · Measures
List model schemas · Get model YAML
Related Skills
omni-model-builder — create or modify views, topics, and fields
omni-query — run queries against discovered fields
omni-ai-optimizer — inspect and improve AI context on topics
Weekly Installs
22
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