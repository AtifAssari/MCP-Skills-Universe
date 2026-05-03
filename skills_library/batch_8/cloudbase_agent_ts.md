---
title: cloudbase-agent-ts
url: https://skills.sh/tencentcloudbase/skills/cloudbase-agent-ts
---

# cloudbase-agent-ts

skills/tencentcloudbase/skills/cloudbase-agent-ts
cloudbase-agent-ts
Installation
$ npx skills add https://github.com/tencentcloudbase/skills --skill cloudbase-agent-ts
Summary

TypeScript SDK for deploying AI agents as HTTP services with AG-UI protocol support.

Supports three adapter patterns: LangGraph for stateful graph-based workflows, LangChain for chain-based agents, and custom adapters via AbstractAgent interface
Includes @cloudbase/agent-server for HTTP service deployment with built-in CORS, logging, and observability configuration
Provides UI client libraries for web applications (@ag-ui/client) and WeChat Mini Programs (@cloudbase/agent-ui-miniprogram)
Implements AG-UI protocol for event-driven message streaming and client-server communication
SKILL.md
Cloudbase Agent (TypeScript)

TypeScript SDK for deploying AI agents as HTTP services using the AG-UI protocol.

Note: This skill is for TypeScript/JavaScript projects only.

When to use this skill

Use this skill for AI agent development when you need to:

Deploy AI agents as HTTP services with AG-UI protocol support
Build agent backends using LangGraph or LangChain frameworks
Create custom agent adapters implementing the AbstractAgent interface
Understand AG-UI protocol events and message streaming
Build web UI clients that connect to AG-UI compatible agents
Build WeChat Mini Program UIs for AI agent interactions

Do NOT use for:

Simple AI model calling without agent capabilities (use ai-model-* skills)
CloudBase cloud functions (use cloud-functions skill)
CloudRun backend services without agent features (use cloudrun-development skill)
How to use this skill (for a coding agent)
MUST READ: Read ALL docs that match your task

Before writing any code, identify which docs you need and read ALL of them. Reading only a subset leads to incomplete implementations (missing CORS, wrong adapter patterns, no UI client code).

Scenario-based reading lists
If the task asks you to...	You MUST read these docs
Build a full-stack agent (backend + frontend)	server-quickstart.md + adapter doc + ui-clients.md
Deploy an agent server only	server-quickstart.md
Use LangGraph for agent logic	adapter-langgraph.md + server-quickstart.md
Use LangChain for agent logic	adapter-langchain.md + server-quickstart.md
Build a custom adapter (no LangGraph/LangChain)	adapter-development.md + agui-protocol.md + server-quickstart.md
Build a web/mini-program UI client	ui-clients.md + agui-protocol.md
Step-by-step workflow
Identify the adapter type from the task description (LangGraph / LangChain / custom)
Read the matching docs from the table above — read ALL listed docs, not just one
Set up the agent server using @cloudbase/agent-server — always include cors: true
Implement the agent logic using the chosen adapter
If building UI, read ui-clients.md and create the client code
Reference doc index
Doc	When to read
server-quickstart	Always — deployment, CORS, logging, endpoints
adapter-langgraph	Task mentions LangGraph, StateGraph, or graph-based workflows
adapter-langchain	Task mentions LangChain, chains, or chain-based patterns
adapter-development	Task requires custom adapter (no existing framework adapter)
agui-protocol	Task requires custom adapter or deep protocol understanding
ui-clients	Task mentions web UI, frontend, client, or SSE streaming
ui-miniprogram	Task mentions WeChat Mini Program or miniprogram UI
Quick Start
import { run } from "@cloudbase/agent-server";
import { LanggraphAgent } from "@cloudbase/agent-adapter-langgraph";

run({
  createAgent: () => ({ agent: new LanggraphAgent({ workflow }) }),
  port: 9000,
});

Weekly Installs
420
Repository
tencentcloudbase/skills
GitHub Stars
52
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass