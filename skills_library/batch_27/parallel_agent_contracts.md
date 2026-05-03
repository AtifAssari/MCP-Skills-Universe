---
title: parallel-agent-contracts
url: https://skills.sh/parcadei/continuous-claude-v3/parallel-agent-contracts
---

# parallel-agent-contracts

skills/parcadei/continuous-claude-v3/parallel-agent-contracts
parallel-agent-contracts
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill parallel-agent-contracts
SKILL.md
Parallel Agent Type Contracts

When launching parallel agents for code implementation, prevent type duplication.

Required in Every Agent Prompt
1. Verification Command (MANDATORY)
## Before Marking Complete
Run verification:
\`\`\`bash
npx tsc --noEmit 2>&1 | head -20
\`\`\`
If ANY type errors exist, fix them before completing.

2. Grep-Before-Create
## Before Creating Any Type/Interface
First check if it exists:
\`\`\`bash
grep -r "interface YourTypeName\|type YourTypeName" src/
\`\`\`
If found, import it. NEVER duplicate existing types.

3. Canonical Type Map

Include relevant entries from this map in agent prompts:

Type	Owner File	Import From
NormalizedTool	src/sdk/agent.ts	'./agent'
ToolCall	src/sdk/agent.ts	'./agent'
ToolResult	src/sdk/agent.ts	'./agent'
ToolDefinition	src/sdk/agent.ts	'./agent'
Message	src/sdk/types.ts	'./types'
ContentBlock	src/sdk/types.ts	'./types'
TokenUsage	src/sdk/types.ts	'./types'
ProviderAdapter	src/sdk/providers/index.ts	'./providers'
RiggClient	src/sdk/client.ts	'./client'
Prompt Template

When spawning implementation agents:

# Task: [Description]

## Type Ownership (DO NOT recreate)
- [List relevant types from canonical map]

## Before Creating New Types
Run: `grep -r "interface TypeName" src/` - if exists, import it.

## Before Marking Complete
Run: `npx tsc --noEmit 2>&1 | head -20`
Fix all type errors before completing.

## Your Implementation
[Actual task description]

Why This Works
Type checker is the contract - tsc catches conflicts automatically
Grep is fast - 1 second to check if type exists
Explicit ownership - No ambiguity about where types live
Fail fast - Agent can't claim "done" with broken types
Weekly Installs
301
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass