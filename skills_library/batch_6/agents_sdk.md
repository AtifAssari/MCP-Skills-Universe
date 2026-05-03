---
title: agents-sdk
url: https://skills.sh/cloudflare/skills/agents-sdk
---

# agents-sdk

skills/cloudflare/skills/agents-sdk
agents-sdk
Installation
$ npx skills add https://github.com/cloudflare/skills --skill agents-sdk
Summary

Build stateful AI agents on Cloudflare Workers with persistent state, RPC methods, scheduling, and workflow orchestration.

Core features include SQLite-backed state management, callable RPC methods via @callable(), one-time and recurring task scheduling, and durable multi-step workflows
Supports MCP server integration (both client and server modes), email routing with secure replies, and streaming chat with resumable streams on disconnect
Includes React hooks (useAgent, useAgentChat) for client-side state binding and real-time WebSocket communication
Agents route to /agents/{agent-name}/{instance-name} and validate state changes synchronously before persistence; always fetch current docs from the GitHub repository to stay current with SDK updates
SKILL.md
Cloudflare Agents SDK

Your knowledge of the Agents SDK may be outdated. Prefer retrieval over pre-training for any Agents SDK task.

Retrieval Sources

Cloudflare docs: https://developers.cloudflare.com/agents/

Topic	Docs URL	Use for
Getting started	Quick start	First agent, project setup
Adding to existing project	Add to existing project	Install into existing Workers app
Configuration	Configuration	wrangler.jsonc, bindings, assets, deployment
Agent class	Agents API	Agent lifecycle, patterns, pitfalls
State	Store and sync state	setState, validateStateChange, persistence
Routing	Routing	URL patterns, routeAgentRequest
Callable methods	Callable methods	@callable, RPC, streaming, timeouts
Scheduling	Schedule tasks	schedule(), scheduleEvery(), cron
Workflows	Run workflows	AgentWorkflow, durable multi-step tasks
HTTP/WebSockets	WebSockets	Lifecycle hooks, hibernation
Chat agents	Chat agents	AIChatAgent, streaming, tools, persistence
Client SDK	Client SDK	useAgent, useAgentChat, React hooks
Client tools	Client tools	Client-side tools, autoContinueAfterToolResult
Server-driven messages	Trigger patterns	saveMessages, waitUntilStable, server-initiated turns
Resumable streaming	Resumable streaming	Stream recovery on disconnect
Email	Email	Email routing, secure reply resolver
MCP client	MCP client	Connecting to MCP servers
MCP server	MCP server	Building MCP servers with McpAgent
MCP transports	MCP transports	Streamable HTTP, SSE, RPC transport options
Securing MCP servers	Securing MCP	OAuth, proxy MCP, hardening
Human-in-the-loop	Human-in-the-loop	Approval flows, needsApproval, workflows
Durable execution	Durable execution	runFiber(), stash(), surviving DO eviction
Queue	Queue	Built-in FIFO queue, queue()
Retries	Retries	this.retry(), backoff/jitter
Observability	Observability	Diagnostics-channel events
Push notifications	Push notifications	Web Push + VAPID from agents
Webhooks	Webhooks	Receiving external webhooks
Cross-domain auth	Cross-domain auth	WebSocket auth, tokens, CORS
Readonly connections	Readonly	shouldConnectionBeReadonly
Voice	Voice	Experimental STT/TTS, withVoice
Browse the web	Browser tools	Experimental CDP browser automation
Think	Think	Experimental higher-level chat agent class
Migrations	AI SDK v5, AI SDK v6	Upgrading @cloudflare/ai-chat
Capabilities

The Agents SDK provides:

Persistent state — SQLite-backed, auto-synced to clients via setState
Callable RPC — @callable() methods invoked over WebSocket
Scheduling — One-time, recurring (scheduleEvery), and cron tasks
Workflows — Durable multi-step background processing via AgentWorkflow
Durable execution — runFiber() / stash() for work that survives DO eviction
Queue — Built-in FIFO queue with retries via queue()
Retries — this.retry() with exponential backoff and jitter
MCP integration — Connect to MCP servers or build your own with McpAgent
Email handling — Receive and reply to emails with secure routing
Streaming chat — AIChatAgent with resumable streams, message persistence, tools
Server-driven messages — saveMessages, waitUntilStable for proactive agent turns
React hooks — useAgent, useAgentChat for client apps
Observability — diagnostics_channel events for state, RPC, schedule, lifecycle
Push notifications — Web Push + VAPID delivery from agents
Webhooks — Receive and verify external webhooks
Voice (experimental) — STT/TTS via @cloudflare/voice
Browser tools (experimental) — CDP-powered browsing via agents/browser
Think (experimental) — Higher-level chat agent via @cloudflare/think
FIRST: Verify Installation
npm ls agents  # Should show agents package


If not installed:

npm install agents


For chat agents:

npm install agents @cloudflare/ai-chat ai @ai-sdk/react

Wrangler Configuration
{
  "compatibility_flags": ["nodejs_compat"],
  "durable_objects": {
    "bindings": [{ "name": "MyAgent", "class_name": "MyAgent" }]
  },
  "migrations": [{ "tag": "v1", "new_sqlite_classes": ["MyAgent"] }]
}


Gotchas:

Do NOT enable experimentalDecorators in tsconfig (breaks @callable)
Never edit old migrations — always add new tags
Each agent class needs its own DO binding + migration entry
Add "ai": { "binding": "AI" } for Workers AI
Agent Class
import { Agent, routeAgentRequest, callable } from "agents";

type State = { count: number };

export class Counter extends Agent<Env, State> {
  initialState = { count: 0 };

  validateStateChange(nextState: State, source: Connection | "server") {
    if (nextState.count < 0) throw new Error("Count cannot be negative");
  }

  onStateUpdate(state: State, source: Connection | "server") {
    console.log("State updated:", state);
  }

  @callable()
  increment() {
    this.setState({ count: this.state.count + 1 });
    return this.state.count;
  }
}

export default {
  fetch: (req, env) => routeAgentRequest(req, env) ?? new Response("Not found", { status: 404 })
};

Routing

Requests route to /agents/{agent-name}/{instance-name}:

Class	URL
Counter	/agents/counter/user-123
ChatRoom	/agents/chat-room/lobby

Client: useAgent({ agent: "Counter", name: "user-123" })

Custom routing: use getAgentByName(env.MyAgent, "instance-id") then agent.fetch(request).

Core APIs
Task	API
Read state	this.state.count
Write state	this.setState({ count: 1 })
SQL query	this.sql`SELECT * FROM users WHERE id = ${id}`
Schedule (delay)	await this.schedule(60, "task", payload)
Schedule (cron)	await this.schedule("0 * * * *", "task", payload)
Schedule (interval)	await this.scheduleEvery(30, "poll")
RPC method	@callable() myMethod() { ... }
Streaming RPC	@callable({ streaming: true }) stream(res) { ... }
Start workflow	await this.runWorkflow("ProcessingWorkflow", params)
Durable fiber	await this.runFiber("name", async (ctx) => { ... })
Enqueue work	this.queue("handler", payload)
Retry with backoff	await this.retry(fn, { maxAttempts: 5 })
Broadcast to clients	this.broadcast(message)
Get connections	this.getConnections(tag?)
React Client
import { useAgent } from "agents/react";

function App() {
  const [state, setLocalState] = useState({ count: 0 });

  const agent = useAgent({
    agent: "Counter",
    name: "my-instance",
    onStateUpdate: (newState) => setLocalState(newState),
    onIdentity: (name, agentType) => console.log(`Connected to ${name}`)
  });

  return (
    <button onClick={() => agent.setState({ count: state.count + 1 })}>
      Count: {state.count}
    </button>
  );
}

References
Core
references/state-scheduling.md — State persistence, scheduling, SQL
references/callable.md — RPC methods, streaming, timeouts
references/routing.md — URL patterns, custom routing, getAgentByName
references/configuration.md — Wrangler config, bindings, Vite setup
Chat & Streaming
references/streaming-chat.md — AIChatAgent, resumable streams, tools
references/client-sdk.md — useAgent, useAgentChat, AgentClient
references/server-driven-messages.md — Trigger patterns, saveMessages
references/human-in-the-loop.md — Approval flows, needsApproval
Background Processing
references/workflows.md — Durable Workflows integration
references/durable-execution.md — runFiber, stash, surviving eviction
references/queue-retries.md — Built-in queue, retry with backoff
Integrations
references/mcp.md — MCP client and server, transports, securing
references/email.md — Email routing and handling
references/webhooks-push.md — Webhooks, push notifications
references/observability.md — Diagnostics-channel events
Experimental
references/think.md — @cloudflare/think higher-level chat agent
references/voice.md — @cloudflare/voice STT/TTS
references/codemode.md — Code Mode for tool orchestration
references/browse-the-web.md — CDP browser tools
Weekly Installs
6.1K
Repository
cloudflare/skills
GitHub Stars
1.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn