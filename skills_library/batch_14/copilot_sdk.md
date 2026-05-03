---
title: copilot-sdk
url: https://skills.sh/doggy8088/agent-skills/copilot-sdk
---

# copilot-sdk

skills/doggy8088/agent-skills/copilot-sdk
copilot-sdk
Installation
$ npx skills add https://github.com/doggy8088/agent-skills --skill copilot-sdk
SKILL.md
GitHub Copilot SDK
Overview

The GitHub Copilot SDK is a multi-platform agent runtime that embeds Copilot's agentic workflows into applications. It exposes the same engine behind Copilot CLI, enabling programmatic invocation without requiring custom orchestration development.

Status: Technical Preview (suitable for development and testing)

Supported Languages: TypeScript/Node.js, Python, Go, .NET

Primary Documentation
GitHub Copilot SDK Repository
Getting Started Guide
Cookbook with Recipes
Language-Specific SDK Docs
Node.js/TypeScript SDK
Python SDK
Go SDK
.NET SDK
CLI and Configuration Docs
About GitHub Copilot CLI
Using GitHub Copilot CLI
Creating Custom Agents
Custom Agents Configuration Reference
Enhancing Agent Mode with MCP
Supported AI Models
Prerequisites
GitHub Copilot Subscription - Pro, Pro+, Business, or Enterprise
GitHub Copilot CLI - Installed and authenticated (copilot --version)
Runtime: Node.js 18+, Python 3.8+, Go 1.21+, or .NET 8.0+
Installation
Language	Command
TypeScript/Node.js	npm install @github/copilot-sdk
Python	pip install github-copilot-sdk
Go	go get github.com/github/copilot-sdk/go
.NET	dotnet add package GitHub.Copilot.SDK
Architecture
Application → SDK Client → JSON-RPC → Copilot CLI (server mode)


The SDK manages CLI lifecycle automatically. External server connections supported via cliUrl / cli_url.

Quick Start (TypeScript)
import { CopilotClient } from "@github/copilot-sdk";

const client = new CopilotClient();
await client.start();

const session = await client.createSession({ model: "gpt-5" });

// Register handler BEFORE send()
session.on((event) => {
  if (event.type === "assistant.message") {
    console.log(event.data.content);
  }
});

await session.send({ prompt: "What is 2 + 2?" });

await session.destroy();
await client.stop();


Critical: Register event handlers before calling send() to capture all events.

For complete examples in all languages, see references/working-examples.md.

Core Concepts
Client

Main entry point. Manages CLI server lifecycle and session creation.

Operations: start(), stop(), createSession(), resumeSession()

Config: cliPath, cliUrl, port, useStdio, autoStart, autoRestart

Session

Individual conversation context with message history.

Operations: send(), sendAndWait(), on(), abort(), getMessages(), destroy()

Config: model, streaming, tools, systemMessage

Events

Key events during processing:

Event	Purpose
assistant.message	Complete response
assistant.message_delta	Streaming chunk
session.idle	Ready for next prompt
tool.execution_start/end	Tool invocations

For full event lifecycle and SessionEvent structure, see references/event-system.md.

Streaming
streaming: false (default) - Content arrives all at once
streaming: true - Content arrives incrementally via assistant.message_delta

Final assistant.message always fires regardless of streaming setting.

Available Models

See Supported AI Models for full list.

Provider	Model ID	Notes
OpenAI	gpt-4.1, gpt-5, gpt-5-mini	Included
OpenAI	gpt-5.1, gpt-5.1-codex, gpt-5.2	Premium
Anthropic	claude-sonnet-4.5	Premium (CLI default)
Anthropic	claude-opus-4.5	Premium (3× multiplier)
Google	gemini-3-pro-preview	Premium
Custom Tools

TypeScript (Zod):

const tool = defineTool("lookup_issue", {
  description: "Fetch issue details",
  parameters: z.object({ id: z.string() }),
  handler: async ({ id }) => fetchIssue(id),
});


Python (Pydantic):

@define_tool(description="Fetch issue details")
async def lookup_issue(params: IssueParams) -> dict:
    return fetch_issue(params.id)


For complete tool examples in all languages, see references/working-examples.md.

Language Conventions
Concept	TypeScript	Python	Go	.NET
Create session	createSession()	create_session()	CreateSession()	CreateSessionAsync()
Delta content	deltaContent	delta_content	DeltaContent	DeltaContent

For full conventions table, see references/event-system.md.

CLI Configuration

Config stored in ~/.copilot/:

config.json - General configuration
mcp-config.json - MCP server definitions

For custom agents and MCP setup, see references/cli-agents-mcp.md.

Troubleshooting
Problem	Solution
Events fire but content empty	Use event.data.content, not event.content
Handler never fires	Register before send()
Python enum issues	Use event.type.value
Go nil pointer	Check != nil before dereferencing

For debugging techniques, see references/troubleshooting.md.

Skill References

Detailed documentation in this skill:

references/working-examples.md - Complete examples for all languages, custom tools
references/event-system.md - Event lifecycle, SessionEvent structure, language conventions
references/troubleshooting.md - Common issues, debugging techniques
references/cli-agents-mcp.md - CLI configuration, custom agents, MCP server setup
Additional Resources
SDK Samples
SDK Releases
Cookbook
awesome-copilot
Weekly Installs
205
Repository
doggy8088/agent-skills
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn