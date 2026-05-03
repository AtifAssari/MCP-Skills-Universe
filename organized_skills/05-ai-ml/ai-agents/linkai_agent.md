---
rating: ⭐⭐
title: linkai-agent
url: https://skills.sh/zhayujie/chatgpt-on-wechat/linkai-agent
---

# linkai-agent

skills/zhayujie/chatgpt-on-wechat/linkai-agent
linkai-agent
Installation
$ npx skills add https://github.com/zhayujie/chatgpt-on-wechat --skill linkai-agent
SKILL.md
LinkAI Agent

Call LinkAI applications and workflows through the chat completions API. Available apps are loaded from config.json.

Setup

This skill requires a LinkAI API key.

Get your API key from LinkAI Console
Set the environment variable: export LINKAI_API_KEY=Link_xxxxxxxxxxxx (or use env_config tool)
Configuration
Copy config.json.template to config.json
Add your apps/workflows in config.json. The skill description is auto-generated from this config when loaded.
Usage

Use the bash tool with curl to call the API. Prefer curl to avoid encoding issues on Windows PowerShell.

curl -X POST "https://api.link-ai.tech/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LINKAI_API_KEY" \
  -d '{
    "app_code": "<app_code>",
    "messages": [{"role": "user", "content": "<question>"}],
    "stream": false
  }'


Optional parameters:

Add --max-time 120 to curl for long-running tasks (video/image generation)

On Windows cmd: Use %LINKAI_API_KEY% instead of $LINKAI_API_KEY.

Example (via bash tool):

bash(command='curl -sS --max-time 120 -X POST "https://api.link-ai.tech/v1/chat/completions" -H "Content-Type: application/json" -H "Authorization: Bearer $LINKAI_API_KEY" -d "{\"app_code\":\"G7z6vKwp\",\"messages\":[{\"role\":\"user\",\"content\":\"What is AI?\"}],\"stream\":false}"', timeout=130)

Response

Success (extract choices[0].message.content from JSON):

{
  "choices": [{
    "message": {
      "role": "assistant",
      "content": "AI stands for Artificial Intelligence..."
    }
  }],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 50,
    "total_tokens": 60
  }
}


Error:

{
  "error": {
    "message": "Error description",
    "code": "error_code"
  }
}

Weekly Installs
54
Repository
zhayujie/chatgp…n-wechat
GitHub Stars
42.8K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass