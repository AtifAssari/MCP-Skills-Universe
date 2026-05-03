---
title: tools-ui
url: https://skills.sh/inference-sh/skills/tools-ui
---

# tools-ui

skills/inference-sh/skills/tools-ui
tools-ui
Installation
$ npx skills add https://github.com/inference-sh/skills --skill tools-ui
SKILL.md
Tool UI Components

Tool lifecycle components from ui.inference.sh.

Quick Start
npx shadcn@latest add https://ui.inference.sh/r/tools.json

Tool States
State	Description
pending	Tool call requested, waiting to execute
running	Tool is currently executing
approval	Requires human approval before execution
success	Tool completed successfully
error	Tool execution failed
Components
Tool Call Display
import { ToolCall } from "@/registry/blocks/tools/tool-call"

<ToolCall
  name="search_web"
  args={{ query: "latest AI news" }}
  status="running"
/>

Tool Result
import { ToolResult } from "@/registry/blocks/tools/tool-result"

<ToolResult
  name="search_web"
  result={{ results: [...] }}
  status="success"
/>

Tool Approval
import { ToolApproval } from "@/registry/blocks/tools/tool-approval"

<ToolApproval
  name="send_email"
  args={{ to: "user@example.com", subject: "Hello" }}
  onApprove={() => executeTool()}
  onDeny={() => cancelTool()}
/>

Full Example
import { ToolCall, ToolResult, ToolApproval } from "@/registry/blocks/tools"

function ToolDisplay({ tool }) {
  if (tool.status === 'approval') {
    return (
      <ToolApproval
        name={tool.name}
        args={tool.args}
        onApprove={tool.approve}
        onDeny={tool.deny}
      />
    )
  }

  if (tool.result) {
    return (
      <ToolResult
        name={tool.name}
        result={tool.result}
        status={tool.status}
      />
    )
  }

  return (
    <ToolCall
      name={tool.name}
      args={tool.args}
      status={tool.status}
    />
  )
}

Styling Tool Cards
<ToolCall
  name="read_file"
  args={{ path: "/src/index.ts" }}
  status="running"
  className="border-blue-500"
/>

Tool Icons

Tools automatically get icons based on their name:

Pattern	Icon
search*, find*	Search
read*, get*	File
write*, create*	Pencil
delete*, remove*	Trash
send*, email*	Mail
Default	Wrench
With Agent Component

The Agent component handles tool lifecycle automatically:

import { Agent } from "@/registry/blocks/agent/agent"

<Agent
  proxyUrl="/api/inference/proxy"
  config={{
    core_app: { ref: 'openrouter/claude-sonnet-45@0fkg6xwb' },
    tools: [
      {
        name: 'search_web',
        description: 'Search the web',
        parameters: { query: { type: 'string' } },
        requiresApproval: true, // Enable approval flow
      },
    ],
  }}
/>

Related Skills
# Full agent component (recommended)
npx skills add inference-sh/skills@agent-ui

# Chat UI blocks
npx skills add inference-sh/skills@chat-ui

# Widgets for tool results
npx skills add inference-sh/skills@widgets-ui

Documentation
Adding Tools to Agents - Equip agents with tools
Human-in-the-Loop - Approval flows
Tool Approval Gates - Implementing approvals

Component docs: ui.inference.sh/blocks/tools

Weekly Installs
336
Repository
inference-sh/skills
GitHub Stars
395
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn