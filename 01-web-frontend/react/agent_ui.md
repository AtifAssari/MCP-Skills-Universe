---
rating: ⭐⭐⭐
title: agent-ui
url: https://skills.sh/inference-sh/skills/agent-ui
---

# agent-ui

skills/inference-sh/skills/agent-ui
agent-ui
Installation
$ npx skills add https://github.com/inference-sh/skills --skill agent-ui
SKILL.md
Agent Component

Batteries-included agent component from ui.inference.sh.

Quick Start
# Install the agent component
npx shadcn@latest add https://ui.inference.sh/r/agent.json

# Add the SDK for the proxy route
npm install @inferencesh/sdk

Setup
1. API Proxy Route (Next.js)
// app/api/inference/proxy/route.ts
import { route } from '@inferencesh/sdk/proxy/nextjs';
export const { GET, POST, PUT } = route;

2. Environment Variable
# .env.local
INFERENCE_API_KEY=inf_...

3. Use the Component
import { Agent } from "@/registry/blocks/agent/agent"

export default function Page() {
  return (
    <Agent
      proxyUrl="/api/inference/proxy"
      agentConfig={{
        core_app: { ref: 'openrouter/claude-haiku-45@0fkg6xwb' },
        description: 'a helpful ai assistant',
        system_prompt: 'you are helpful.',
      }}
    />
  )
}

Features
Feature	Description
Runtime included	No backend logic needed
Tool lifecycle	Pending, progress, approval, results
Human-in-the-loop	Built-in approval flows
Widgets	Declarative JSON UI from agent responses
Streaming	Real-time token streaming
Client-side tools	Tools that run in the browser
Client-Side Tools Example
import { Agent } from "@/registry/blocks/agent/agent"
import { createScopedTools } from "./blocks/agent/lib/client-tools"

const formRef = useRef<HTMLFormElement>(null)
const scopedTools = createScopedTools(formRef)

<Agent
  proxyUrl="/api/inference/proxy"
  config={{
    core_app: { ref: 'openrouter/claude-haiku-45@0fkg6xwb' },
    tools: scopedTools,
    system_prompt: 'You can fill forms using scan_ui and fill_field tools.',
  }}
/>

Props
Prop	Type	Description
proxyUrl	string	API proxy endpoint
name	string	Agent name (optional)
config	AgentConfig	Agent configuration
allowFiles	boolean	Enable file uploads
allowImages	boolean	Enable image uploads
Related Skills
# Chat UI building blocks
npx skills add inference-sh/skills@chat-ui

# Declarative widgets from JSON
npx skills add inference-sh/skills@widgets-ui

# Tool lifecycle UI
npx skills add inference-sh/skills@tools-ui

Documentation
Agents Overview - Building AI agents
Agent SDK - Programmatic agent control
Human-in-the-Loop - Approval flows
Agents That Generate UI - Building generative UIs
Agent UX Patterns - Best practices

Component docs: ui.inference.sh/blocks/agent

Weekly Installs
361
Repository
inference-sh/skills
GitHub Stars
395
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass