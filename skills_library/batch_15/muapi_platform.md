---
title: muapi-platform
url: https://skills.sh/samuraigpt/generative-media-skills/muapi-platform
---

# muapi-platform

skills/samuraigpt/generative-media-skills/muapi-platform
muapi-platform
Installation
$ npx skills add https://github.com/samuraigpt/generative-media-skills --skill muapi-platform
SKILL.md
⚙️ MuAPI Platform Utilities

Setup and polling utilities for the muapi.ai platform.

Configure your API key, verify connectivity, and poll for async generation results.

Available Scripts
Script	Description
setup.sh	Configure API key, show config, test key validity
check-result.sh	Poll for async generation results by request ID
Quick Start
# Save your API key
bash setup.sh --add-key "YOUR_MUAPI_KEY"

# Show current configuration
bash setup.sh --show-config

# Test API key validity
bash setup.sh --test

# Poll for a result (waits for completion)
bash check-result.sh --id "your-request-id"

# Check once without polling
bash check-result.sh --id "your-request-id" --once

Requirements
curl
Weekly Installs
228
Repository
samuraigpt/gene…a-skills
GitHub Stars
3.2K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail