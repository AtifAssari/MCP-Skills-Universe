---
title: aixyz
url: https://skills.sh/agentlyhq/aixyz/aixyz
---

# aixyz

skills/agentlyhq/aixyz/aixyz
aixyz
Installation
$ npx skills add https://github.com/agentlyhq/aixyz --skill aixyz
SKILL.md
Working with aixyz
Where to Find the Latest Information

The project evolves quickly. Always consult these sources for up-to-date details:

Docs site: aixyz.sh — Getting Started guides, API reference, protocol docs, and templates
GitHub: github.com/AgentlyHQ/aixyz — source, issues, and examples
CLI help: every command has --help — run it to discover the current flags
Immutable Facts

These things will not change:

Runtime is always Bun — install with bun, run with bun, test with bun test
Agent logic uses the Vercel AI SDK (ai package) — ToolLoopAgent, tool(), stepCountIs() from "ai" — check ai-sdk.dev for the current version
LLM providers use @ai-sdk/* adapters — @ai-sdk/openai is the default but any Vercel AI SDK provider works (@ai-sdk/anthropic, @ai-sdk/google, @ai-sdk/amazon-bedrock, etc.)
MUST use create-aixyz-app to scaffold new agents — see below
aixyz CLI is always available — aixyz dev for the dev/test loop, aixyz build for building
Environment variables follow Next.js load order — .env, .env.local (don't commit), .env.<NODE_ENV>, .env.<NODE_ENV>.local
Getting Started

CRITICAL: You MUST use create-aixyz-app to create new agent projects. Do NOT manually create aixyz.config.ts, package.json, app/agent.ts, or any other project files by hand. Manually creating these files WILL result in broken builds, missing dependencies, and incorrect configurations. Always scaffold with bunx create-aixyz-app first, then modify the generated files.

# See all scaffolding options (TTY is disabled in AI/CI — every prompt has a flag)
bunx create-aixyz-app --help

# Scaffold with defaults
bunx create-aixyz-app my-agent --yes

# Dev/test loop
cd my-agent && bun run dev   # aixyz dev — hot reload at http://localhost:3000

# Build for deployment
bun run build                # aixyz build

Core Concepts
Project layout

Bare minimum to get started:

my-agent/
  aixyz.config.ts       # Agent identity, payment config, skills declaration
  app/
    agent.ts            # Root agent (ToolLoopAgent from "ai") — required
    tools/name.ts       # Tools (optional) — each file auto-registered; not exported directly
    agents/name.ts      # Sub-agents (optional) — each file → /name/agent endpoint
  package.json
  .env.local            # API keys — never commit


Full layout with optional files:

my-agent/
  aixyz.config.ts
  app/
    agent.ts
    agents/             # Sub-agents
    tools/              # Tools; _prefix files are ignored
    server.ts           # Custom server (overrides auto-generation)
    accepts.ts          # Custom x402 facilitator
    erc-8004.ts         # On-chain ERC-8004 identity
    icon.png            # Agent icon
  package.json
  vercel.json
  .env.local

Getting paid (x402)

Export accepts from app/agent.ts (gates /agent) or from a tool file (gates it on /mcp):

import type { Accepts } from "aixyz/accepts";

export const accepts: Accepts = { scheme: "exact", price: "$0.005" };


No accepts export → endpoint is not exposed. scheme: "free" → explicitly free. See aixyz.sh/getting-started/payments for full details.

A2A capabilities

Export capabilities from app/agent.ts to configure the A2A agent card and executor behavior:

import type { Capabilities } from "aixyz/app/plugins/a2a";

export const capabilities: Capabilities = { streaming: false, pushNotifications: false };


Defaults to { streaming: true, pushNotifications: false }. When streaming: false, the executor uses generate() instead of stream().

On-chain identity (ERC-8004)

Register your agent on-chain with:

aixyz erc-8004 register --help   # see all non-TTY flags
aixyz erc-8004 register --url https://my-agent.vercel.app --broadcast


See aixyz.sh/protocols/erc-8004 for full details.

Testing (optional)

Tests are optional but recommended for advanced users. Tests use Bun's built-in runner (bun:test). Write deterministic tests (no API calls) and use test.skipIf(!process.env.OPENAI_API_KEY) for non-deterministic ones. Use fake() from "aixyz/model" for fully offline CI-safe tests.

bun test                      # run all tests
bun test app/agent.test.ts    # run a specific file


See aixyz.sh/getting-started/testing for full details.

Protocol Endpoints

Every deployed agent exposes these endpoints automatically:

Endpoint	Protocol	Description
/.well-known/agent-card.json	A2A	Agent discovery card
/agent	A2A	JSON-RPC endpoint with x402 payment gate
/mcp	MCP	Tool sharing with MCP clients
Examples

The examples/ directory in github.com/AgentlyHQ/aixyz contains working agents for common patterns. When in doubt, find an example that matches what you need.

If you have GitHub access, clone the repo and explore examples/ directly:

gh repo clone AgentlyHQ/aixyz
ls aixyz/examples/


Each example has an aixyz.config.ts, app/agent.ts, and app/tools/ you can learn from. The Templates tab on aixyz.sh documents each example.

Repo Structure (for exploration)

If you clone the repo, the key areas are:

packages/
  aixyz/              # Framework core (server, adapters, x402)
  aixyz-cli/          # CLI: dev, build, erc-8004 commands
  aixyz-config/       # Config loading (Zod-validated aixyz.config.ts)
  aixyz-erc-8004/     # ERC-8004 ABIs, addresses, schemas
  create-aixyz-app/   # Scaffolding CLI
docs/                 # Mintlify docs
examples/             # Working agent examples


Use --help on any CLI command, read the docs at aixyz.sh, or browse examples in github.com/AgentlyHQ/aixyz/tree/main/examples for the most current information.

Weekly Installs
238
Repository
agentlyhq/aixyz
GitHub Stars
82
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn