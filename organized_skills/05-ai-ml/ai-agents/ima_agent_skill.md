---
rating: ⭐⭐
title: ima-agent-skill
url: https://skills.sh/hyddd/ima_agent_skill/ima-agent-skill
---

# ima-agent-skill

skills/hyddd/ima_agent_skill/ima-agent-skill
ima-agent-skill
Installation
$ npx skills add https://github.com/hyddd/ima_agent_skill --skill ima-agent-skill
SKILL.md
IMA Skill

Control the IMA (ima.copilot) desktop application for AI search and private knowledge retrieval.

Tools
ima_search

Launches IMA and performs a search. Supports "Private Knowledge Base" mode via special tags.

query (required): The search query. Prefix with @个人知识库 or @knowledge to search your private knowledge base (requires config.json).
autoclose (optional): "true" to close the app after searching. Default: "false".

Implementation:

/usr/bin/python3 /opt/homebrew/lib/node_modules/clawdbot/skills/ima/scripts/ima.py "{query}" --autoclose="{autoclose}"

Configuration

To enable private knowledge base search, you must providing your knowledge_id. The script looks for config in:

~/.clawd_ima_config.json
skills/ima/config.json

Format:

{
  "knowledge_id": "your_id_string"
}

Examples
Public: clawdbot ima_search query="DeepSeek analysis"
Private: clawdbot ima_search query="@knowledge project update"
Weekly Installs
193
Repository
hyddd/ima_agent_skill
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn