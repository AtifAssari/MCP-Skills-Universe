---
rating: ⭐⭐⭐
title: sandbox-agent
url: https://skills.sh/rivet-dev/skills/sandbox-agent
---

# sandbox-agent

skills/rivet-dev/skills/sandbox-agent
sandbox-agent
Installation
$ npx skills add https://github.com/rivet-dev/skills --skill sandbox-agent
Summary

Universal API for orchestrating multiple AI coding agents in sandboxed environments.

Supports four coding agents (Claude Code, Codex, OpenCode, Amp) with a unified schema for responses, events, and session management
Deploy locally or to cloud sandboxes including E2B, Daytona, Docker, Vercel, and Cloudflare with environment-specific configuration
Stream agent events, manage session persistence across multiple backends (in-memory, SQLite, Postgres, IndexedDB), and handle human-in-the-loop interactions
Includes TypeScript and Python SDKs, REST API, CLI tools, and a built-in Inspector UI for debugging sessions and events
SKILL.md
Sandbox Agent

Sandbox Agent provides a universal API for orchestrating AI coding agents in sandboxed environments.

What To Do If You Get Stuck

If something is not working as intended or you are stuck, prompt the user to join the Rivet Discord or file an issue on GitHub to report an issue and get help.

Provide the user with a pre-generated report with:

Symptoms
If this is happening in local dev, deployed, or both
The error you're seeing
Relevant source code related to this
What you've tried to solve it
Environment
Sandbox Agent version
SDK in use (TypeScript, Python, or HTTP)
Agent in use (Claude Code, Codex, OpenCode, Amp, Mock)
Sandbox provider (E2B, Daytona, Docker, local)
Quickstart
Install skill (optional)
npx
npx skills add rivet-dev/skills -s sandbox-agent

bunx
bunx skills add rivet-dev/skills -s sandbox-agent

Set environment variables

Each coding agent requires API keys to connect to their respective LLM providers.

Local shell
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."

E2B
import { Sandbox } from "@e2b/code-interpreter";

const envs: Record<string, string> = {};
if (process.env.ANTHROPIC_API_KEY) envs.ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
if (process.env.OPENAI_API_KEY) envs.OPENAI_API_KEY = process.env.OPENAI_API_KEY;

const sandbox = await Sandbox.create({ envs });

Daytona
import { Daytona } from "@daytonaio/sdk";

const envVars: Record<string, string> = {};
if (process.env.ANTHROPIC_API_KEY) envVars.ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
if (process.env.OPENAI_API_KEY) envVars.OPENAI_API_KEY = process.env.OPENAI_API_KEY;

const daytona = new Daytona();
const sandbox = await daytona.create({
  snapshot: "sandbox-agent-ready",
  envVars,
});

Docker
docker run -p 2468:2468 \
  -e ANTHROPIC_API_KEY="sk-ant-..." \
  -e OPENAI_API_KEY="sk-..." \
  rivetdev/sandbox-agent:0.4.2-full \
  server --no-token --host 0.0.0.0 --port 2468

Extracting API keys from current machine

Use sandbox-agent credentials extract-env --export to extract your existing API keys (Anthropic, OpenAI, etc.) from local Claude Code or Codex config files.

Testing without API keys

Use the mock agent for SDK and integration testing without provider credentials.

Multi-tenant and per-user billing

For per-tenant token tracking, budget enforcement, or usage-based billing, see LLM Credentials for gateway options like OpenRouter, LiteLLM, and Portkey.

Run the server
curl

Install and run the binary directly.

curl -fsSL https://releases.rivet.dev/sandbox-agent/0.4.x/install.sh | sh
sandbox-agent server --no-token --host 0.0.0.0 --port 2468

npx

Run without installing globally.

npx @sandbox-agent/cli@0.4.x server --no-token --host 0.0.0.0 --port 2468

bunx

Run without installing globally.

bunx @sandbox-agent/cli@0.4.x server --no-token --host 0.0.0.0 --port 2468

npm i -g

Install globally, then run.

npm install -g @sandbox-agent/cli@0.4.x
sandbox-agent server --no-token --host 0.0.0.0 --port 2468

bun add -g

Install globally, then run.

bun add -g @sandbox-agent/cli@0.4.x
# Allow Bun to run postinstall scripts for native binaries (required for SandboxAgent.start()).
bun pm -g trust @sandbox-agent/cli-linux-x64 @sandbox-agent/cli-linux-arm64 @sandbox-agent/cli-darwin-arm64 @sandbox-agent/cli-darwin-x64 @sandbox-agent/cli-win32-x64
sandbox-agent server --no-token --host 0.0.0.0 --port 2468

Node.js (local)

For local development, use SandboxAgent.start() to spawn and manage the server as a subprocess.

npm install sandbox-agent@0.4.x

import { SandboxAgent } from "sandbox-agent";

const sdk = await SandboxAgent.start();

Bun (local)

For local development, use SandboxAgent.start() to spawn and manage the server as a subprocess.

bun add sandbox-agent@0.4.x
# Allow Bun to run postinstall scripts for native binaries (required for SandboxAgent.start()).
bun pm trust @sandbox-agent/cli-linux-x64 @sandbox-agent/cli-linux-arm64 @sandbox-agent/cli-darwin-arm64 @sandbox-agent/cli-darwin-x64 @sandbox-agent/cli-win32-x64

import { SandboxAgent } from "sandbox-agent";

const sdk = await SandboxAgent.start();

Build from source

If you're running from source instead of the installed CLI.

cargo run -p sandbox-agent -- server --no-token --host 0.0.0.0 --port 2468


Binding to 0.0.0.0 allows the server to accept connections from any network interface, which is required when running inside a sandbox where clients connect remotely.

Configuring token

Tokens are usually not required. Most sandbox providers (E2B, Daytona, etc.) already secure networking at the infrastructure layer.

If you expose the server publicly, use --token "$SANDBOX_TOKEN" to require authentication:

sandbox-agent server --token "$SANDBOX_TOKEN" --host 0.0.0.0 --port 2468


Then pass the token when connecting:

TypeScript
import { SandboxAgent } from "sandbox-agent";

const sdk = await SandboxAgent.connect({
  baseUrl: "http://your-server:2468",
  token: process.env.SANDBOX_TOKEN,
});

curl
curl "http://your-server:2468/v1/health" \
  -H "Authorization: Bearer $SANDBOX_TOKEN"

CLI
sandbox-agent --token "$SANDBOX_TOKEN" api agents list \
  --endpoint http://your-server:2468

CORS

If you're calling the server from a browser, see the CORS configuration guide.

Install agents (optional)

To preinstall agents:

sandbox-agent install-agent --all


If agents are not installed up front, they are lazily installed when creating a session.

Install desktop dependencies (optional, Linux only)

If you want to use /v1/desktop/*, install the desktop runtime packages first:

sandbox-agent install desktop --yes


Then use GET /v1/desktop/status or sdk.getDesktopStatus() to verify the runtime is ready before calling desktop screenshot or input APIs.

Create a session
import { SandboxAgent } from "sandbox-agent";

const sdk = await SandboxAgent.connect({
  baseUrl: "http://127.0.0.1:2468",
});

const session = await sdk.createSession({
  agent: "claude",
  sessionInit: {
    cwd: "/",
    mcpServers: [],
  },
});

console.log(session.id);

Send a message
const result = await session.prompt([
  { type: "text", text: "Summarize the repository and suggest next steps." },
]);

console.log(result.stopReason);

Read events
const off = session.onEvent((event) => {
  console.log(event.sender, event.payload);
});

const page = await sdk.getEvents({
  sessionId: session.id,
  limit: 50,
});

console.log(page.items.length);
off();

Test with Inspector

Open the Inspector UI at /ui/ on your server (for example, http://localhost:2468/ui/) to inspect sessions and events in a GUI.

Next steps

Session Persistence — Configure in-memory, Rivet Actor state, IndexedDB, SQLite, and Postgres persistence.

Deploy to a Sandbox — Deploy your agent to E2B, Daytona, Docker, Vercel, or Cloudflare.

SDK Overview — Use the latest TypeScript SDK API.

Reference Map
Agents
Amp
Claude
Codex
Cursor
OpenCode
Pi
AI
llms.txt
skill.md
Deploy
Agent Computer
BoxLite
Cloudflare
ComputeSDK
Daytona
Docker
E2B
Local
Modal
Vercel
General
Agent Sessions
Architecture
Attachments
CLI Reference
Common Software
Computer Use
CORS Configuration
Custom Tools
Daemon
File System
Inspector
LLM Credentials
Manage Sessions
MCP
Multiplayer
Observability
OpenCode Compatibility
Orchestration Architecture
Persisting Sessions
Processes
Quickstart
React Components
SDK Overview
Security
Session Restoration
Skills
Telemetry
Troubleshooting
Weekly Installs
5.4K
Repository
rivet-dev/skills
GitHub Stars
14
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn