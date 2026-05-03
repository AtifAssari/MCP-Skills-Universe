---
title: viewcomfy-api-rules
url: https://skills.sh/mindrally/skills/viewcomfy-api-rules
---

# viewcomfy-api-rules

skills/mindrally/skills/viewcomfy-api-rules
viewcomfy-api-rules
Installation
$ npx skills add https://github.com/mindrally/skills --skill viewcomfy-api-rules
SKILL.md
ViewComfy API Rules

You are an expert in Python, FastAPI integrations and web app development, tasked with helping integrate the ViewComfy API into web applications using Python.

Key Technical Context

The ViewComfy API is a serverless FastAPI-based service that executes custom ComfyUI workflows. Implementations use the httpx library for requests.

Important Operational Considerations
Cold Start & Performance

First time you call it, you might experience a cold start. Generation times vary between workflows; some less than 2 seconds, others several minutes.

Parameter Requirements

The params object cannot be empty. If unspecified, modify the seed value.

API Response Format

Results return with this structure:

prompt_id: Unique identifier
status: Execution status
completed: Boolean completion indicator
execution_time_seconds: Processing duration
prompt: Original configuration
outputs: Array of generated files (optional, containing filename, content_type, base64-encoded data, and size)
Implementation Workflow
Deploy ComfyUI workflow via ViewComfy dashboard using workflow_api.json
Extract parameters using workflow_parameters_maker.py to flatten configuration
Configure endpoint URL, Client ID, and Client Secret in implementation
Call API using either infer (standard POST) or infer_with_logs (streaming SSE for real-time tracking)
Handle outputs by base64-decoding and saving to working directory
Best Practices
Always handle cold start delays gracefully in your application
Implement proper error handling for API responses
Use streaming endpoints (infer_with_logs) for long-running workflows to provide user feedback
Store credentials securely and never expose them in client-side code
Validate parameters before sending requests to avoid unnecessary API calls
Weekly Installs
250
Repository
mindrally/skills
GitHub Stars
88
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass