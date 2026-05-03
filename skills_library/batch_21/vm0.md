---
title: vm0
url: https://skills.sh/vm0-ai/vm0-skills/vm0
---

# vm0

skills/vm0-ai/vm0-skills/vm0
vm0
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill vm0
SKILL.md
VM0 Agent Self-Management

Use this skill to inspect and update the current agent's own configuration — its connectors (skills) and instructions — via the VM0 Zero Agents API.

Official docs: https://docs.vm0.ai

When to Use

Use this skill when you need to:

Read the current agent's configuration (connectors, metadata)
Add or remove connectors (skills) from the current agent
Read or update the agent's instructions
Redeploy the agent after configuration changes
Prerequisites

The VM0_API_TOKEN and VM0_AGENT_ORG_SLUG environment variables must be set. They are automatically injected when this skill is loaded.

The base URL defaults to https://www.vm0.ai. Override with VM0_API_URL if needed.

How to Use
1. Get Agent Configuration

Retrieve the current agent's connectors and metadata.

bash -c 'curl -s -X GET "https://www.vm0.ai/api/zero/agents/$VM0_AGENT_NAME?org=$VM0_AGENT_ORG_SLUG" --header "Authorization: Bearer $VM0_API_TOKEN"' | jq .


Response:

{
  "name": "agent-uuid",
  "agentComposeId": "compose-id",
  "description": "Agent description",
  "displayName": "My Agent",
  "sound": null,
  "connectors": ["github", "slack"]
}

2. Update Agent Configuration

Update the agent's connectors (skills) and metadata. The connectors field is required — it replaces the full list. The displayName, description, and sound fields are optional — only provided fields are updated.

bash -c 'curl -s -X PUT "https://www.vm0.ai/api/zero/agents/$VM0_AGENT_NAME?org=$VM0_AGENT_ORG_SLUG" --header "Content-Type: application/json" --header "Authorization: Bearer $VM0_API_TOKEN" -d '"'"'{"connectors": ["github", "slack", "gmail"], "displayName": "My Agent"}'"'"'' | jq .


Response: Same shape as GET.

3. Get Agent Instructions

Retrieve the current agent's instructions content and filename.

bash -c 'curl -s -X GET "https://www.vm0.ai/api/zero/agents/$VM0_AGENT_NAME/instructions?org=$VM0_AGENT_ORG_SLUG" --header "Authorization: Bearer $VM0_API_TOKEN"' | jq .


Response:

{
  "content": "# My Agent Instructions\n\nYou are a helpful agent...",
  "filename": "agent.md"
}

4. Update Agent Instructions

Replace the agent's instructions content.

bash -c 'curl -s -X PUT "https://www.vm0.ai/api/zero/agents/$VM0_AGENT_NAME/instructions?org=$VM0_AGENT_ORG_SLUG" --header "Content-Type: application/json" --header "Authorization: Bearer $VM0_API_TOKEN" -d '"'"'{"content": "# Updated Instructions\n\nNew instructions here..."}'"'"'' | jq .


Response: Same shape as GET agent configuration (name, agentComposeId, connectors, etc.).

Finding Skills

Skills come from two marketplaces. Search both when looking for new capabilities.

1. skills.sh (33,700+ community skills)
curl -s "https://skills.sh/api/search?q={keyword}"

2. vm0-ai/vm0-skills (70+ curated integrations)

Browse at: https://github.com/vm0-ai/vm0-skills

Priority rule: If a skill exists in both marketplaces, prefer the vm0-ai/vm0-skills version — it is optimized for VM0 agent workflows and has consistent quality.

Connector short names

Connectors in the API use short names that correspond to skill directory names in the vm0-ai/vm0-skills repository (e.g. github, slack, gmail, notion).

Checking required credentials

After picking a skill, read its SKILL.md frontmatter to see what secrets or vars it needs:

bash -c 'curl -s "https://raw.githubusercontent.com/vm0-ai/vm0-skills/main/{skill-name}/SKILL.md"' | head -20


Look for vm0_secrets and vm0_vars in the frontmatter. These are automatically injected when the skill is loaded — no manual setup needed. If a required secret is missing, guide the user to the VM0 console to configure it.

Operation: Self Update

Usage: self update or update myself or similar

This operation enables the agent to update itself based on user requirements.

Step 1: Understand the current agent

Read the current configuration and instructions via the API:

bash -c 'curl -s -X GET "https://www.vm0.ai/api/zero/agents/$VM0_AGENT_NAME?org=$VM0_AGENT_ORG_SLUG" --header "Authorization: Bearer $VM0_API_TOKEN"' | jq .

bash -c 'curl -s -X GET "https://www.vm0.ai/api/zero/agents/$VM0_AGENT_NAME/instructions?org=$VM0_AGENT_ORG_SLUG" --header "Authorization: Bearer $VM0_API_TOKEN"' | jq .

Step 2: Understand User Intent

Ask clarifying questions to understand what the user wants to update:

What new operation should be added?
What existing operation needs modification?
What skills need to be added/removed?
What configuration changes are needed?
Step 3: Apply Changes

To update connectors (add/remove skills):

Get the current connectors list from Step 1, modify it, then PUT:

bash -c 'curl -s -X PUT "https://www.vm0.ai/api/zero/agents/$VM0_AGENT_NAME?org=$VM0_AGENT_ORG_SLUG" --header "Content-Type: application/json" --header "Authorization: Bearer $VM0_API_TOKEN" -d '"'"'{"connectors": ["github", "slack", "new-skill"]}'"'"'' | jq .


To update instructions:

bash -c 'curl -s -X PUT "https://www.vm0.ai/api/zero/agents/$VM0_AGENT_NAME/instructions?org=$VM0_AGENT_ORG_SLUG" --header "Content-Type: application/json" --header "Authorization: Bearer $VM0_API_TOKEN" -d '"'"'{"content": "# Updated Instructions\n\nNew content here..."}'"'"'' | jq .

Operation: SaaS/Service Connection

Usage: connect to Gmail, access my Dropbox, integrate with Slack, or similar

This operation helps the user connect external SaaS services to their agent.

Step 1: Check existing skills

Read the current agent configuration and check if the requested service connector is already in the connectors list:

bash -c 'curl -s -X GET "https://www.vm0.ai/api/zero/agents/$VM0_AGENT_NAME?org=$VM0_AGENT_ORG_SLUG" --header "Authorization: Bearer $VM0_API_TOKEN"' | jq .connectors

Step 2: If skill exists

Guide the user to complete OAuth/connector setup on the VM0 console, then stop. Use this exact closing pattern:

Visit https://app.vm0.ai/team/<agent-name> to set up the {service} connector. Click Connect to complete OAuth authorization. The required secrets will be stored automatically — no manual configuration needed. Once connected, I'll be able to access {service} in the next conversation.

Step 3: If skill not found

Search for it in the vm0-ai/vm0-skills repository:

bash -c 'curl -s "https://api.github.com/repos/vm0-ai/vm0-skills/contents"' | jq -r '.[].name' | grep -i {service-name}

Step 4: If found in vm0-skills

Add the connector to the agent via the update API. Get current connectors, append the new one, then PUT:

bash -c 'curl -s -X PUT "https://www.vm0.ai/api/zero/agents/$VM0_AGENT_NAME?org=$VM0_AGENT_ORG_SLUG" --header "Content-Type: application/json" --header "Authorization: Bearer $VM0_API_TOKEN" -d '"'"'{"connectors": ["existing-1", "existing-2", "new-service"]}'"'"'' | jq .


Then guide the user to the VM0 console using the same closing pattern from Step 2.

Step 5: If not found anywhere

Inform the user: "This service is not supported yet. Please check the vm0-ai/vm0-skills repository for available integrations or request a new skill."

Note: Available skills can be browsed at https://github.com/vm0-ai/vm0-skills

Guidelines
Agent name: The current agent name is available in the VM0_AGENT_NAME environment variable.
Connectors replace the full list: The PUT endpoint replaces the entire connectors list. Always read the current list first, modify it, then PUT the complete list back.
Selective metadata updates: Only displayName, description, and sound fields that are explicitly included in the PUT body are updated. Omitted fields keep their current values.
422 errors: If the API returns 422, one or more connectors reference skills that are not cached on the platform. Verify the connector names are correct.
Secrets are never exposed: Secret values are never returned by the API — only ${{ secrets.NAME }} references are preserved.
Weekly Installs
50
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn