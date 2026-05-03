---
title: n8n
url: https://skills.sh/sundial-org/awesome-openclaw-skills/n8n
---

# n8n

skills/sundial-org/awesome-openclaw-skills/n8n
n8n
Installation
$ npx skills add https://github.com/sundial-org/awesome-openclaw-skills --skill n8n
SKILL.md
n8n Workflow Management

Interact with n8n automation platform via REST API.

Setup

First-time setup:

API key must be stored in environment:
export N8N_API_KEY="your-api-key-here"

Verify connection:
python3 scripts/n8n_api.py list-workflows --pretty


For persistent storage, add to ~/.bashrc or ~/.zshrc:

echo 'export N8N_API_KEY="your-key"' >> ~/.bashrc

Quick Reference
List Workflows
python3 scripts/n8n_api.py list-workflows --pretty
python3 scripts/n8n_api.py list-workflows --active true --pretty

Get Workflow Details
python3 scripts/n8n_api.py get-workflow --id <workflow-id> --pretty

Activate/Deactivate
python3 scripts/n8n_api.py activate --id <workflow-id>
python3 scripts/n8n_api.py deactivate --id <workflow-id>

Executions
# List recent executions
python3 scripts/n8n_api.py list-executions --limit 10 --pretty

# Get execution details
python3 scripts/n8n_api.py get-execution --id <execution-id> --pretty

# Filter by workflow
python3 scripts/n8n_api.py list-executions --id <workflow-id> --limit 20 --pretty

Manual Execution
# Trigger workflow
python3 scripts/n8n_api.py execute --id <workflow-id>

# With data
python3 scripts/n8n_api.py execute --id <workflow-id> --data '{"key": "value"}'

Python API

For programmatic access:

from scripts.n8n_api import N8nClient

client = N8nClient()

# List workflows
workflows = client.list_workflows(active=True)

# Get workflow
workflow = client.get_workflow('workflow-id')

# Activate/deactivate
client.activate_workflow('workflow-id')
client.deactivate_workflow('workflow-id')

# Executions
executions = client.list_executions(workflow_id='workflow-id', limit=10)
execution = client.get_execution('execution-id')

# Execute workflow
result = client.execute_workflow('workflow-id', data={'key': 'value'})

Common Tasks
Debug Failed Workflows
List recent executions with failures
Get execution details to see error
Check workflow configuration
Deactivate if needed
Monitor Workflow Health
List active workflows
Check recent execution status
Review error patterns
Workflow Management
List all workflows
Review active/inactive status
Activate/deactivate as needed
Delete old workflows
API Reference

For detailed API documentation, see references/api.md.

Troubleshooting

Authentication error:

Verify N8N_API_KEY is set: echo $N8N_API_KEY
Check API key is valid in n8n UI

Connection error:

Check N8N_BASE_URL if using custom URL

Command errors:

Use --pretty flag for readable output
Check --id is provided when required
Validate JSON format for --data parameter
Weekly Installs
10
Repository
sundial-org/awe…w-skills
GitHub Stars
589
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn