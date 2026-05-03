---
title: add-provider-doc
url: https://skills.sh/lobehub/lobehub/add-provider-doc
---

# add-provider-doc

skills/lobehub/lobehub/add-provider-doc
add-provider-doc
Installation
$ npx skills add https://github.com/lobehub/lobehub --skill add-provider-doc
Summary

Step-by-step guide for documenting new AI provider integrations across docs, environment variables, and Docker configs.

Create bilingual usage documentation (English and Chinese) with 5-6 screenshots, cover images, registration URLs, and pricing callouts, using placeholder API keys only
Add environment variable documentation for both languages covering required API keys and optional model list configuration with examples
Update three Dockerfile variants and .env.example with provider-specific environment variable declarations
Prepare and host image resources (cover image, API dashboard screenshots, and LobeHub configuration screenshots) on the LobeHub CDN
SKILL.md
Adding New AI Provider Documentation

Complete workflow for adding documentation for a new AI provider.

Overview
Create usage documentation (EN + CN)
Add environment variable documentation (EN + CN)
Update Docker configuration files
Update .env.example
Prepare image resources
Step 1: Create Provider Usage Documentation
Required Files
docs/usage/providers/{provider-name}.mdx (English)
docs/usage/providers/{provider-name}.zh-CN.mdx (Chinese)
Key Requirements
5-6 screenshots showing the process
Cover image for the provider
Real registration and dashboard URLs
Pricing information callout
Never include real API keys - use placeholders

Reference: docs/usage/providers/fal.mdx

Step 2: Update Environment Variables Documentation
Files to Update
docs/self-hosting/environment-variables/model-provider.mdx (EN)
docs/self-hosting/environment-variables/model-provider.zh-CN.mdx (CN)
Content Format
### `{PROVIDER}_API_KEY`

- Type: Required
- Description: API key from {Provider Name}
- Example: `{api-key-format}`

### `{PROVIDER}_MODEL_LIST`

- Type: Optional
- Description: Control model list. Use `+` to add, `-` to hide
- Example: `-all,+model-1,+model-2=Display Name`

Step 3: Update Docker Files

Update all Dockerfiles at the end of ENV section:

Dockerfile
Dockerfile.database
Dockerfile.pglite
# {New Provider}
{PROVIDER}_API_KEY="" {PROVIDER}_MODEL_LIST=""

Step 4: Update .env.example
### {Provider Name} ###
# {PROVIDER}_API_KEY={prefix}-xxxxxxxx

Step 5: Image Resources
Cover image
3-4 API dashboard screenshots
2-3 LobeHub configuration screenshots
Host on LobeHub CDN: hub-apac-1.lobeobjects.space
Checklist
 EN + CN usage docs
 EN + CN env var docs
 All 3 Dockerfiles updated
 .env.example updated
 All images prepared
 No real API keys in docs
Weekly Installs
749
Repository
lobehub/lobehub
GitHub Stars
75.9K
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass