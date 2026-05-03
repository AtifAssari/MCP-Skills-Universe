---
rating: ⭐⭐⭐
title: nathan-standards
url: https://skills.sh/89jobrien/steve/nathan-standards
---

# nathan-standards

skills/89jobrien/steve/nathan-standards
nathan-standards
Installation
$ npx skills add https://github.com/89jobrien/steve --skill nathan-standards
SKILL.md
Nathan Development Standards

Standards and patterns for developing within the Nathan project - an n8n-Jira agent automation system.

When to Use

Invoke this skill when:

Creating or modifying n8n workflow JSON files
Writing Python code for the Nathan helpers or templating modules
Designing webhook command contracts
Building workflow registry configurations
Implementing spec-driven features via agent-os
Project Architecture

Nathan follows a layered architecture:

External Service (Jira) <-- n8n Workflows <-- Python Agent Service
                             (credentials)      (webhook calls)


Core Principle: n8n owns all external credentials. Python services call n8n webhooks with shared secret authentication.

n8n Workflow Standards

For detailed workflow patterns, load references/n8n-workflow-patterns.md.

Standard Workflow Structure

Every webhook workflow must follow this pattern:

Webhook --> Validate Secret --> Operation --> Respond to Webhook
               |                   |              |
               v                   v              v
           Unauthorized       Error Response   Success Response
           Response (401)     (500)            (200)

Required Node Pattern
{
  "id": "validate-secret",
  "name": "Validate Secret",
  "type": "n8n-nodes-base.if",
  "typeVersion": 2,
  "parameters": {
    "conditions": {
      "conditions": [{
        "leftValue": "={{ $json.headers['x-n8n-secret'] }}",
        "rightValue": "={{ $env.N8N_WEBHOOK_SECRET }}",
        "operator": { "type": "string", "operation": "equals" }
      }]
    }
  }
}

Response Format

All responses must follow this shape:

{ "success": true, "data": {...}, "status_code": 200, "error": null }
{ "success": false, "data": {}, "status_code": 500, "error": "message" }

JQL Expression Escaping

In n8n expressions within JSON, escape properly:

Wrong	Correct
.map(x => "${x}")	.map(x => '"' + x + '"')
.join('\n')	.join('\\n')
.replaceAll('\n', ' ')	.replaceAll('\\n', ' ')
Python Standards

For detailed patterns, load references/python-patterns.md.

Module Structure
nathan/
  helpers/           # Shared utilities (workflow registry, etc.)
  workflows/         # n8n workflow JSON + registry.yaml per category
  templating/        # YAML-to-JSON template engine
  scripts/           # Standalone runnable scripts

Code Style
# Required imports pattern
from __future__ import annotations
from typing import Any
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# Type hints required, use T | None not Optional[T]
async def trigger_workflow(url: str, params: dict[str, Any]) -> dict[str, Any]:
    ...

Registry Pattern
# registry.yaml
version: "1.0.0"
description: "Registry description"

commands:
  command_name:
    endpoint: /webhook/endpoint-path
    method: POST
    required_params:
      - param1
    optional_params:
      - param2
    description: What this command does
    example:
      param1: "value"

Spec-Driven Development

Use agent-os commands for feature development:

/shape-spec - Initialize and shape specification
/write-spec - Write detailed spec document
/create-tasks - Generate task list from spec
/orchestrate-tasks - Delegate to subagents

Specs live in agent-os/specs/[spec-name]/ with:

spec.md - Feature specification
tasks.md - Implementation tasks with checkboxes
orchestration.yml - Subagent delegation config
Quick Reference
Common Commands
uv sync                              # Install dependencies
uv run pytest                        # Run tests
uv run pytest path/to/test.py -v     # Single test file
uvx ruff check .                     # Lint
uvx ruff format .                    # Format
docker compose -f docker-compose.n8n.yml up -d  # Start n8n

Environment Variables
Variable	Purpose
N8N_WEBHOOK_SECRET	Shared secret for webhook auth
N8N_API_KEY	n8n Public API key
JIRA_DOMAIN	Jira Cloud domain
JIRA_EMAIL	Jira account email
JIRA_API_TOKEN	Jira API token
File Naming Conventions
Type	Convention	Example
Workflow JSON	kebab-case.json	jira-get-ticket.json
Python modules	snake_case.py	n8n_workflow_registry.py
Test files	test_*.py	test_parser.py
Registry	registry.yaml	per workflow category
Weekly Installs
21
Repository
89jobrien/steve
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn