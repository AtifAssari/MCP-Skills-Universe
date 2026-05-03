---
title: n8n-workflow
url: https://skills.sh/claude-office-skills/skills/n8n-workflow
---

# n8n-workflow

skills/claude-office-skills/skills/n8n-workflow
n8n-workflow
Installation
$ npx skills add https://github.com/claude-office-skills/skills --skill n8n-workflow
SKILL.md
N8N Workflow Skill
Overview

This skill enables document workflow automation using n8n - the most popular workflow automation platform with 7800+ community templates. Chain document operations, integrate with 400+ apps, and build complex document pipelines.

How to Use
Describe what you want to accomplish
Provide any required input data or files
I'll execute the appropriate operations

Example prompts:

"Automate PDF → OCR → Translation → Email workflow"
"Watch folder for new contracts → Review → Notify Slack"
"Daily report generation from multiple data sources"
"Batch document processing with conditional logic"
Domain Knowledge
n8n Fundamentals

n8n uses a node-based workflow approach:

Trigger → Action → Action → Output
   │         │         │
   └─────────┴─────────┴── Data flows between nodes

Key Node Types
Type	Examples	Use Case
Triggers	Webhook, Schedule, File Watcher	Start workflow
Document	Read PDF, Write DOCX, OCR	Process files
Transform	Code, Set, Merge	Manipulate data
Output	Email, Slack, Google Drive	Deliver results
Workflow Example: Contract Review Pipeline
{
  "nodes": [
    {
      "name": "Watch Folder",
      "type": "n8n-nodes-base.localFileTrigger",
      "parameters": {
        "path": "/contracts/incoming",
        "events": ["add"]
      }
    },
    {
      "name": "Extract Text",
      "type": "n8n-nodes-base.readPdf"
    },
    {
      "name": "AI Review",
      "type": "n8n-nodes-base.anthropic",
      "parameters": {
        "model": "claude-sonnet-4-20250514",
        "prompt": "Review this contract for risks..."
      }
    },
    {
      "name": "Save Report",
      "type": "n8n-nodes-base.writeFile"
    },
    {
      "name": "Notify Team",
      "type": "n8n-nodes-base.slack"
    }
  ]
}

Self-Hosting vs Cloud
Option	Pros	Cons
Self-hosted	Free, full control, data privacy	Maintenance required
n8n Cloud	No setup, auto-updates	Costs at scale
# Docker quick start
docker run -it --rm \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n

Best Practices
Start with existing templates, customize as needed
Use error handling nodes for reliability
Store credentials securely with n8n's credential manager
Test workflows with sample data before production
Installation
# Install required dependencies
pip install python-docx openpyxl python-pptx reportlab jinja2

Resources
n8n Repository
Claude Office Skills Hub
Weekly Installs
794
Repository
claude-office-s…s/skills
GitHub Stars
94
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass