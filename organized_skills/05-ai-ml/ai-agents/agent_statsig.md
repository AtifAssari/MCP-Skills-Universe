---
rating: ⭐⭐⭐
title: agent-statsig
url: https://skills.sh/shhac/agent-statsig/agent-statsig
---

# agent-statsig

skills/shhac/agent-statsig/agent-statsig
agent-statsig
Installation
$ npx skills add https://github.com/shhac/agent-statsig --skill agent-statsig
SKILL.md
agent-statsig — Statsig Feature Flag CLI

Manage Statsig feature gates, dynamic configs, experiments, and segments via the Console API.

When to Use
User asks about a feature gate, feature flag, or rollout
User wants to check, modify, or create targeting rules
User asks about experiment status or wants to start/ship/abandon experiments
User asks about dynamic config values or wants to modify them
User wants to manage segment membership
User wants to organize entities with tags
Process
Always read before writing
Inspect first: Run agent-statsig gate get <name> (or config/experiment/segment get) to understand the current state before making changes
Check rules: Run gate rule list <name> to see rule IDs before updating/removing rules
Validate criteria: Run gate criteria if unsure which condition types or operators to use
Using tags

When creating gates, configs, or experiments, apply appropriate tags if the user's intent suggests a category (e.g., "mobile feature" → use --tag mobile if such a tag exists). Check available tags with tag list first. Tags must exist before they can be applied — create missing tags with tag create first.

Making changes
Read the current state
Identify what needs to change (add rule, modify values, change rollout %)
Make the change with the appropriate command
Verify by reading again
Error handling

All errors are JSON to stderr with a classification:

fixable_by: agent — you made a typo or used wrong syntax. Read the hint and retry.
fixable_by: human — credentials or permissions issue. Tell the user.
fixable_by: retry — transient error. Wait and retry once.
Quick Reference
# Explore (safe, read-only)
agent-statsig gate list [--search <text>] [--tag <tag>]
agent-statsig gate get <name>
agent-statsig config get <name>
agent-statsig experiment get <name>
agent-statsig segment get <name>

# Modify gates
agent-statsig gate enable <name>
agent-statsig gate disable <name>
agent-statsig gate rollout <name> --percent 50
agent-statsig gate rule add <name> --name "Rule" --criteria email --value user@co.com
agent-statsig gate rule update <name> --rule <id> --add-value new@co.com
agent-statsig gate rule remove <name> --rule <id>

# Modify configs (return values validated against schema)
agent-statsig config rule add <name> --name "Rule" --criteria email --value user@co.com --return-value '{"key":"val"}'

# Experiment lifecycle
agent-statsig experiment start <name>
agent-statsig experiment ship <name> --group <id> --reason "text"
agent-statsig experiment abandon <name> --reason "text"

# Segment IDs
agent-statsig segment ids add <name> --id user1 --id user2
agent-statsig segment ids remove <name> --id user1

# Manage tags
agent-statsig tag list
agent-statsig tag create <name> [--description <text>] [--is-core]
agent-statsig tag get <id>
agent-statsig tag update <id> [--name <name>] [--description <text>] [--is-core]
agent-statsig tag delete <id>

# Apply tags when creating/updating entities
agent-statsig gate create <name> --tag <tag-name>
agent-statsig config create <name> --tag <tag-name>
agent-statsig experiment create <name> --tag <tag-name>
agent-statsig gate update <name> '{}' --tag <tag-name>

Detailed Reference

For full command details with examples, run per-entity usage:

agent-statsig gate usage
agent-statsig config usage
agent-statsig experiment usage
agent-statsig segment usage
agent-statsig tag usage
agent-statsig usage                  # top-level overview

Key Concepts
Rules
Rules are evaluated top-to-bottom; first matching rule wins
Conditions within a rule are AND-ed together
Multiple rules act as OR (first match wins)
Default (no rule matches) = fail for gates, defaultValue for configs
Condition Types

25 built-in types. Most common:

email — match by email (operators: any, none, str_contains_any, str_contains_none)
user_id — match by user ID
country — match by country code
custom_field — match any user attribute (use --field to specify which)
public — matches everyone (used for rollout percentages)
passes_segment / passes_gate — compose with other entities

Default operator is any (case-insensitive match). Run gate criteria for the full list.

Dynamic Config Schemas

When a config has a JSON Schema, --return-value is validated before the API call. This catches type errors, missing required fields, and unknown fields locally.

Environments

Rules can be scoped to environments (staging, production, etc.) using --env. A rule with no environments applies to all environments.

Project Setup

If the project isn't configured yet:

agent-statsig project add <alias> --console-key <key> [--client-key <key>]
agent-statsig project test


Tell the user to get their Console API key from Statsig Console → Settings → Keys & Environments.

Weekly Installs
9
Repository
shhac/agent-statsig
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail