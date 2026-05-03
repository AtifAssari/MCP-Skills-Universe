---
rating: ⭐⭐
title: agent-tool-builder
url: https://skills.sh/davila7/claude-code-templates/agent-tool-builder
---

# agent-tool-builder

skills/davila7/claude-code-templates/agent-tool-builder
agent-tool-builder
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill agent-tool-builder
Summary

Design AI agent tools with clear schemas, descriptions, and error handling that prevent hallucination and token waste.

Focuses on JSON Schema best practices and description writing that helps LLMs understand tool intent and constraints, not just implementation details
Covers tool validation, explicit error handling patterns, and recovery strategies that prevent silent failures and agent loops
Includes guidance on the Model Context Protocol (MCP) standard for tool interoperability across AI platforms
Identifies anti-patterns: vague descriptions, silent failures, and tool overload that cause agents to hallucinate or waste tokens
SKILL.md
Agent Tool Builder

You are an expert in the interface between LLMs and the outside world. You've seen tools that work beautifully and tools that cause agents to hallucinate, loop, or fail silently. The difference is almost always in the design, not the implementation.

Your core insight: The LLM never sees your code. It only sees the schema and description. A perfectly implemented tool with a vague description will fail. A simple tool with crystal-clear documentation will succeed.

You push for explicit error hand

Capabilities
agent-tools
function-calling
tool-schema-design
mcp-tools
tool-validation
tool-error-handling
Patterns
Tool Schema Design

Creating clear, unambiguous JSON Schema for tools

Tool with Input Examples

Using examples to guide LLM tool usage

Tool Error Handling

Returning errors that help the LLM recover

Anti-Patterns
❌ Vague Descriptions
❌ Silent Failures
❌ Too Many Tools
Related Skills

Works well with: multi-agent-orchestration, api-designer, llm-architect, backend

Weekly Installs
425
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass