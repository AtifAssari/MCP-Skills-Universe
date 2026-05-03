---
rating: ⭐⭐
title: download-openapi
url: https://skills.sh/haibaraaiaptx/frontend-openapi-skills/download-openapi
---

# download-openapi

skills/haibaraaiaptx/frontend-openapi-skills/download-openapi
download-openapi
Installation
$ npx skills add https://github.com/haibaraaiaptx/frontend-openapi-skills --skill download-openapi
SKILL.md
Download OpenAPI JSON

Download OpenAPI 3.x JSON specification from a remote URL.

Prerequisites
pnpm add -D @aptx/frontend-tk-cli

Usage
pnpm exec aptx-ft input download --url <url> --output <file>


Alternative (without pnpm):

npx aptx-ft input download --url <url> --output <file>

Example
pnpm exec aptx-ft input download --url https://api.example.com/swagger.json --output ./openapi.json

Workflow
Confirm the OpenAPI URL with user
Choose output path (recommended: ./openapi.json)
Execute download command
Pass the file path to other skills (generate-models, generate-artifacts)
Output
Local OpenAPI JSON file (e.g., ./openapi.json)
Boundaries

This skill only handles OpenAPI JSON format downloads:

Does NOT support YAML format
Does NOT handle authenticated URLs (Bearer Token, etc.)
Does NOT support custom request headers
Only validates JSON syntax, not OpenAPI specification validity

For these cases, download manually and use other tools.

Weekly Installs
25
Repository
haibaraaiaptx/f…i-skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn