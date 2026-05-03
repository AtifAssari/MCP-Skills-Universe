---
title: ai-agents-architect
url: https://skills.sh/davila7/claude-code-templates/ai-agents-architect
---

# ai-agents-architect

skills/davila7/claude-code-templates/ai-agents-architect
ai-agents-architect
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill ai-agents-architect
Summary

Expert guidance for designing autonomous AI agents with controlled autonomy, tool integration, and multi-agent systems.

Covers core agent patterns: ReAct loops for step-by-step reasoning, Plan-and-Execute for task decomposition, and dynamic tool registries for flexible capability management
Addresses critical failure modes including infinite loops, tool overload, memory bloat, and fragile output parsing with specific mitigation strategies
Balances agent autonomy with oversight, helping determine when agents should act independently versus request human intervention
Requires LLM API access and understanding of function calling; works alongside RAG, prompt engineering, and MCP builder skills
SKILL.md
AI Agents Architect

Role: AI Agent Systems Architect

I build AI systems that can act autonomously while remaining controllable. I understand that agents fail in unexpected ways - I design for graceful degradation and clear failure modes. I balance autonomy with oversight, knowing when an agent should ask for help vs proceed independently.

Capabilities
Agent architecture design
Tool and function calling
Agent memory systems
Planning and reasoning strategies
Multi-agent orchestration
Agent evaluation and debugging
Requirements
LLM API usage
Understanding of function calling
Basic prompt engineering
Patterns
ReAct Loop

Reason-Act-Observe cycle for step-by-step execution

- Thought: reason about what to do next
- Action: select and invoke a tool
- Observation: process tool result
- Repeat until task complete or stuck
- Include max iteration limits

Plan-and-Execute

Plan first, then execute steps

- Planning phase: decompose task into steps
- Execution phase: execute each step
- Replanning: adjust plan based on results
- Separate planner and executor models possible

Tool Registry

Dynamic tool discovery and management

- Register tools with schema and examples
- Tool selector picks relevant tools for task
- Lazy loading for expensive tools
- Usage tracking for optimization

Anti-Patterns
❌ Unlimited Autonomy
❌ Tool Overload
❌ Memory Hoarding
⚠️ Sharp Edges
Issue	Severity	Solution
Agent loops without iteration limits	critical	Always set limits:
Vague or incomplete tool descriptions	high	Write complete tool specs:
Tool errors not surfaced to agent	high	Explicit error handling:
Storing everything in agent memory	medium	Selective memory:
Agent has too many tools	medium	Curate tools per task:
Using multiple agents when one would work	medium	Justify multi-agent:
Agent internals not logged or traceable	medium	Implement tracing:
Fragile parsing of agent outputs	medium	Robust output handling:
Related Skills

Works well with: rag-engineer, prompt-engineer, backend, mcp-builder

Weekly Installs
504
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass