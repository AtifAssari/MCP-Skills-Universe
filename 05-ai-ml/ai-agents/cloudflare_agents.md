---
rating: ⭐⭐⭐
title: cloudflare-agents
url: https://skills.sh/jezweb/claude-skills/cloudflare-agents
---

# cloudflare-agents

skills/jezweb/claude-skills/cloudflare-agents
cloudflare-agents
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill cloudflare-agents
Summary

Build stateful AI agents on Cloudflare Workers with WebSockets, persistent state, scheduling, and multi-agent coordination.

WebSocket-based real-time communication with automatic state synchronization across clients and devices; resumable streaming persists across disconnects and page refreshes
Built-in SQLite storage (up to 1GB per agent), task scheduling with cron expressions, and Durable Objects for globally unique, persistent agent instances
Multi-agent coordination via routeAgentRequest(), workflow triggering, browser automation, and RAG support with Vectorize
Integrates with Vercel AI SDK for automatic streaming or Workers AI for cost-effective inference; prevents 23 documented configuration and runtime errors including idFromName() gotchas and WebSocket payload limits
SKILL.md
Cloudflare Agents SDK

Status: Production Ready ✅ Last Updated: 2026-01-09 Dependencies: cloudflare-worker-base (recommended) Latest Versions: agents@0.3.3, @modelcontextprotocol/sdk@latest Production Tested: Cloudflare's own MCP servers (https://github.com/cloudflare/mcp-server-cloudflare)

Recent Updates (2025-2026):

Jan 2026: Agents SDK v0.3.6 with callable methods fix, protocol version support updates
Nov 2025: Agents SDK v0.2.24+ with resumable streaming (streams persist across disconnects, page refreshes, and sync across tabs/devices), MCP client improvements, schedule fixes
Sept 2025: AI SDK v5 compatibility, automatic message migration
Aug 2025: MCP Elicitation support, http-streamable transport, task queues, email integration
April 2025: MCP support (MCPAgent class), import { context } from agents
March 2025: Package rename (agents-sdk → agents)
Resumable Streaming (agents@0.2.24+)

AIChatAgent now supports resumable streaming, enabling clients to reconnect and continue receiving streamed responses without data loss. This solves critical real-world scenarios:

Long-running AI responses that exceed connection timeout
Users on unreliable networks (mobile, airplane WiFi)
Users switching between devices mid-conversation
Background tasks where users navigate away and return
Real-time collaboration where multiple clients need to stay in sync

Key capability: Streams persist across page refreshes, broken connections, and sync across open tabs and devices.

Implementation (automatic in AIChatAgent):

export class ChatAgent extends AIChatAgent<Env> {
  async onChatMessage(onFinish) {
    return streamText({
      model: openai('gpt-4o-mini'),
      messages: this.messages,
      onFinish
    }).toTextStreamResponse();

    // ✅ Stream automatically resumable
    // - Client disconnects? Stream preserved
    // - Page refresh? Stream continues
    // - Multiple tabs? All stay in sync
  }
}


No code changes needed - just use AIChatAgent with agents@0.2.24 or later.

Source: Agents SDK v0.2.24 Changelog

What is Cloudflare Agents?

The Cloudflare Agents SDK enables building AI-powered autonomous agents that run on Cloudflare Workers + Durable Objects. Agents can:

Communicate in real-time via WebSockets and Server-Sent Events
Persist state with built-in SQLite database (up to 1GB per agent)
Schedule tasks using delays, specific dates, or cron expressions
Run workflows by triggering asynchronous Cloudflare Workflows
Browse the web using Browser Rendering API + Puppeteer
Implement RAG with Vectorize vector database + Workers AI embeddings
Build MCP servers implementing the Model Context Protocol
Support human-in-the-loop patterns for review and approval
Scale to millions of independent agent instances globally

Each agent instance is a globally unique, stateful micro-server that can run for seconds, minutes, or hours.

Do You Need Agents SDK?

STOP: Before using Agents SDK, ask yourself if you actually need it.

Use JUST Vercel AI SDK (Simpler) When:
✅ Building a basic chat interface
✅ Server-Sent Events (SSE) streaming is sufficient (one-way: server → client)
✅ No persistent agent state needed (or you manage it separately with D1/KV)
✅ Single-user, single-conversation scenarios
✅ Just need AI responses, no complex workflows or scheduling

This covers 80% of chat applications. For these cases, use Vercel AI SDK directly on Workers - it's simpler, requires less infrastructure, and handles streaming automatically.

Example (no Agents SDK needed):

// worker.ts - Simple chat with AI SDK only
import { streamText } from 'ai';
import { openai } from '@ai-sdk/openai';

export default {
  async fetch(request: Request, env: Env) {
    const { messages } = await request.json();

    const result = streamText({
      model: openai('gpt-4o-mini'),
      messages
    });

    return result.toTextStreamResponse(); // Automatic SSE streaming
  }
}

// client.tsx - React with built-in hooks
import { useChat } from 'ai/react';

function ChatPage() {
  const { messages, input, handleSubmit } = useChat({ api: '/api/chat' });
  // Done. No Agents SDK needed.
}


Result: 100 lines of code instead of 500. No Durable Objects setup, no WebSocket complexity, no migrations.

Use Agents SDK When You Need:
✅ WebSocket connections (true bidirectional real-time communication)
✅ Durable Objects (globally unique, stateful agent instances)
✅ Built-in state persistence (SQLite storage up to 1GB per agent)
✅ Multi-agent coordination (agents calling and communicating with each other)
✅ Scheduled tasks (delays, cron expressions, recurring jobs)
✅ Human-in-the-loop workflows (approval gates, review processes)
✅ Long-running agents (background processing, autonomous workflows)
✅ MCP servers with stateful tool execution

This is ~20% of applications - when you need the infrastructure that Agents SDK provides.

Key Understanding: What Agents SDK IS vs IS NOT

Agents SDK IS:

🏗️ Infrastructure layer for WebSocket connections, Durable Objects, and state management
🔧 Framework for building stateful, autonomous agents
📦 Wrapper around Durable Objects with lifecycle methods

Agents SDK IS NOT:

❌ AI inference provider (you bring your own: AI SDK, Workers AI, OpenAI, etc.)
❌ Streaming response handler (use AI SDK for automatic parsing)
❌ LLM integration (that's a separate concern)

Think of it this way:

Agents SDK = The building (WebSockets, state, rooms)
AI SDK / Workers AI = The AI brain (inference, reasoning, responses)

You can use them together (recommended for most cases), or use Workers AI directly (if you're willing to handle manual SSE parsing).

Decision Flowchart
Building an AI application?
│
├─ Need WebSocket bidirectional communication? ───────┐
│  (Client sends while server streams, agent-initiated messages)
│
├─ Need Durable Objects stateful instances? ──────────┤
│  (Globally unique agents with persistent memory)
│
├─ Need multi-agent coordination? ────────────────────┤
│  (Agents calling/messaging other agents)
│
├─ Need scheduled tasks or cron jobs? ────────────────┤
│  (Delayed execution, recurring tasks)
│
├─ Need human-in-the-loop workflows? ─────────────────┤
│  (Approval gates, review processes)
│
└─ If ALL above are NO ─────────────────────────────→ Use AI SDK directly
                                                       (Much simpler approach)

   If ANY above are YES ────────────────────────────→ Use Agents SDK + AI SDK
                                                       (More infrastructure, more power)

Architecture Comparison
Feature	AI SDK Only	Agents SDK + AI SDK
Setup Complexity	🟢 Low (npm install, done)	🔴 Higher (Durable Objects, migrations, bindings)
Code Volume	🟢 ~100 lines	🟡 ~500+ lines
Streaming	✅ Automatic (SSE)	✅ Automatic (AI SDK) or manual (Workers AI)
State Management	⚠️ Manual (D1/KV)	✅ Built-in (SQLite)
WebSockets	❌ Manual setup	✅ Built-in
React Hooks	✅ useChat, useCompletion	⚠️ Custom hooks needed
Multi-agent	❌ Not supported	✅ Built-in (routeAgentRequest)
Scheduling	❌ External (Queue/Workflow)	✅ Built-in (this.schedule)
Use Case	Simple chat, completions	Complex stateful workflows
Still Not Sure?

Start with AI SDK. You can always migrate to Agents SDK later if you discover you need WebSockets or Durable Objects. It's easier to add infrastructure later than to remove it.

For most developers: If you're building a chat interface and don't have specific requirements for WebSockets, multi-agent coordination, or scheduled tasks, use AI SDK directly. You'll ship faster and with less complexity.

Proceed with Agents SDK only if you've identified a specific need for its infrastructure capabilities.

Quick Start (10 Minutes)
1. Scaffold Project with Template
npm create cloudflare@latest my-agent -- \
  --template=cloudflare/agents-starter \
  --ts \
  --git \
  --deploy false


What this creates:

Complete Agent project structure
TypeScript configuration
wrangler.jsonc with Durable Objects bindings
Example chat agent implementation
React client with useAgent hook
2. Or Add to Existing Worker
cd my-existing-worker
npm install agents


Then create an Agent class:

// src/index.ts
import { Agent, AgentNamespace } from "agents";

export class MyAgent extends Agent {
  async onRequest(request: Request): Promise<Response> {
    return new Response("Hello from Agent!");
  }
}

export default MyAgent;

3. Configure Durable Objects Binding

Create or update wrangler.jsonc:

{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "my-agent",
  "main": "src/index.ts",
  "compatibility_date": "2025-10-21",
  "compatibility_flags": ["nodejs_compat"],
  "durable_objects": {
    "bindings": [
      {
        "name": "MyAgent",        // MUST match class name
        "class_name": "MyAgent"   // MUST match exported class
      }
    ]
  },
  "migrations": [
    {
      "tag": "v1",
      "new_sqlite_classes": ["MyAgent"]  // CRITICAL: Enables SQLite storage
    }
  ]
}


CRITICAL Configuration Rules:

✅ name and class_name MUST be identical
✅ new_sqlite_classes MUST be in first migration (cannot add later)
✅ Agent class MUST be exported (or binding will fail)
✅ Migration tags CANNOT be reused (each migration needs unique tag)
4. Deploy
npx wrangler@latest deploy


Your agent is now running at: https://my-agent.<subdomain>.workers.dev

Architecture Overview: How the Pieces Fit Together

Understanding what each tool does prevents confusion and helps you choose the right combination.

The Stack
┌─────────────────────────────────────────────────────────┐
│                    Your Application                      │
│                                                          │
│  ┌────────────────┐         ┌──────────────────────┐   │
│  │  Agents SDK    │         │   AI Inference       │   │
│  │  (Infra Layer) │   +     │   (Brain Layer)      │   │
│  │                │         │                      │   │
│  │ • WebSockets   │         │  Choose ONE:         │   │
│  │ • Durable Objs │         │  • Vercel AI SDK ✅   │   │
│  │ • State (SQL)  │         │  • Workers AI ⚠️      │   │
│  │ • Scheduling   │         │  • OpenAI Direct     │   │
│  │ • Multi-agent  │         │  • Anthropic Direct  │   │
│  └────────────────┘         └──────────────────────┘   │
│         ↓                             ↓                │
│  Manages connections          Generates responses      │
│  and state                    and handles streaming    │
└─────────────────────────────────────────────────────────┘
                          ↓
              Cloudflare Workers + Durable Objects

What Each Tool Provides
1. Agents SDK (This Skill)

Purpose: Infrastructure for stateful, real-time agents

Provides:

✅ WebSocket connection management (bidirectional real-time)
✅ Durable Objects wrapper (globally unique agent instances)
✅ Built-in state persistence (SQLite up to 1GB)
✅ Lifecycle methods (onStart, onConnect, onMessage, onClose)
✅ Task scheduling (this.schedule() with cron/delays)
✅ Multi-agent coordination (routeAgentRequest())
✅ Client libraries (useAgent, AgentClient, agentFetch)

Does NOT Provide:

❌ AI inference (no LLM calls)
❌ Streaming response parsing (bring your own)
❌ Provider integrations (OpenAI, Anthropic, etc.)

Think of it as: The building and infrastructure (rooms, doors, plumbing) but NOT the residents (AI).

2. Vercel AI SDK (Recommended for AI)

Purpose: AI inference with automatic streaming

Provides:

✅ Automatic streaming response handling (SSE parsing done for you)
✅ Multi-provider support (OpenAI, Anthropic, Google, etc.)
✅ React hooks (useChat, useCompletion, useAssistant)
✅ Unified API across providers
✅ Tool calling / function calling
✅ Works on Cloudflare Workers ✅

Example:

import { streamText } from 'ai';
import { openai } from '@ai-sdk/openai';

const result = streamText({
  model: openai('gpt-4o-mini'),
  messages: [...]
});

// Returns SSE stream - no manual parsing needed
return result.toTextStreamResponse();


When to use with Agents SDK:

✅ Most chat applications
✅ When you want React hooks
✅ When you use multiple AI providers
✅ When you want clean, abstracted AI calls

Combine with Agents SDK:

import { AIChatAgent } from "agents/ai-chat-agent";
import { streamText } from "ai";

export class MyAgent extends AIChatAgent<Env> {
  async onChatMessage(onFinish) {
    // Agents SDK provides: WebSocket, state, this.messages
    // AI SDK provides: Automatic streaming, provider abstraction

    return streamText({
      model: openai('gpt-4o-mini'),
      messages: this.messages  // Managed by Agents SDK
    }).toTextStreamResponse();
  }
}

3. Workers AI (Alternative for AI)

Purpose: Cloudflare's on-platform AI inference

Provides:

✅ Cost-effective inference (included in Workers subscription)
✅ No external API keys needed
✅ Models: LLaMA 3, Qwen, Mistral, embeddings, etc.
✅ Runs on Cloudflare's network (low latency)

Does NOT Provide:

❌ Automatic streaming parsing (returns raw SSE format)
❌ React hooks
❌ Multi-provider abstraction

Manual parsing required:

const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
  messages: [...],
  stream: true
});

// Returns raw SSE format - YOU must parse
for await (const chunk of response) {
  const text = new TextDecoder().decode(chunk);  // Uint8Array → string
  if (text.startsWith('data: ')) {              // Check SSE format
    const data = JSON.parse(text.slice(6));     // Parse JSON
    if (data.response) {                        // Extract .response field
      fullResponse += data.response;
    }
  }
}


When to use:

✅ Cost is critical (embeddings, high-volume)
✅ Need Cloudflare-specific models
✅ Willing to handle manual SSE parsing
✅ No external dependencies allowed

Trade-off: Save money, spend time on manual parsing.

Recommended Combinations
Option A: Agents SDK + Vercel AI SDK (Recommended ⭐)

Use when: You need WebSockets/state AND want clean AI integration

import { AIChatAgent } from "agents/ai-chat-agent";
import { streamText } from "ai";
import { openai } from "@ai-sdk/openai";

export class ChatAgent extends AIChatAgent<Env> {
  async onChatMessage(onFinish) {
    return streamText({
      model: openai('gpt-4o-mini'),
      messages: this.messages,  // Agents SDK manages history
      onFinish
    }).toTextStreamResponse();
  }
}


Pros:

✅ Best developer experience
✅ Automatic streaming
✅ WebSockets + state from Agents SDK
✅ Clean, maintainable code

Cons:

⚠️ Requires external API keys
⚠️ Additional cost for AI provider
Option B: Agents SDK + Workers AI

Use when: You need WebSockets/state AND cost is critical

import { Agent } from "agents";

export class BudgetAgent extends Agent<Env> {
  async onMessage(connection, message) {
    const response = await this.env.AI.run('@cf/meta/llama-3-8b-instruct', {
      messages: [...],
      stream: true
    });

    // Manual SSE parsing required (see Workers AI section above)
    for await (const chunk of response) {
      // ... manual parsing ...
    }
  }
}


Pros:

✅ Cost-effective
✅ No external dependencies
✅ WebSockets + state from Agents SDK

Cons:

❌ Manual SSE parsing complexity
❌ Limited model selection
❌ More code to maintain
Option C: Just Vercel AI SDK (No Agents)

Use when: You DON'T need WebSockets or Durable Objects

// worker.ts - Simple Workers route
export default {
  async fetch(request: Request, env: Env) {
    const { messages } = await request.json();

    const result = streamText({
      model: openai('gpt-4o-mini'),
      messages
    });

    return result.toTextStreamResponse();
  }
}

// client.tsx - Built-in React hooks
import { useChat } from 'ai/react';

function Chat() {
  const { messages, input, handleSubmit } = useChat({ api: '/api/chat' });
  return <form onSubmit={handleSubmit}>...</form>;
}


Pros:

✅ Simplest approach
✅ Least code
✅ Fast to implement
✅ Built-in React hooks

Cons:

❌ No WebSockets (only SSE)
❌ No Durable Objects state
❌ No multi-agent coordination

Best for: 80% of chat applications

Decision Matrix
Your Needs	Recommended Stack	Complexity	Cost
Simple chat, no state	AI SDK only	🟢 Low	$$ (AI provider)
Chat + WebSockets + state	Agents SDK + AI SDK	🟡 Medium	$$$ (infra + AI)
Chat + WebSockets + budget	Agents SDK + Workers AI	🔴 High	$ (infra only)
Multi-agent workflows	Agents SDK + AI SDK	🔴 High	$$$ (infra + AI)
MCP server with tools	Agents SDK (McpAgent)	🟡 Medium	$ (infra only)
Key Takeaway

Agents SDK is infrastructure, not AI. You combine it with AI inference tools:

For best DX: Agents SDK + Vercel AI SDK ⭐
For cost savings: Agents SDK + Workers AI (accept manual parsing)
For simplicity: Just AI SDK (if you don't need WebSockets/state)

The rest of this skill focuses on Agents SDK (the infrastructure layer). For AI inference patterns, see the ai-sdk-core or cloudflare-workers-ai skills.

Configuration (wrangler.jsonc)

Critical Required Configuration:

{
  "durable_objects": {
    "bindings": [{ "name": "MyAgent", "class_name": "MyAgent" }]
  },
  "migrations": [
    { "tag": "v1", "new_sqlite_classes": ["MyAgent"] }  // MUST be in first migration
  ]
}


Common Optional Bindings: ai, vectorize, browser, workflows, d1_databases, r2_buckets

CRITICAL Migration Rules:

✅ new_sqlite_classes MUST be in tag "v1" (cannot add SQLite to existing deployed class)
✅ name and class_name MUST match exactly
✅ Migrations are atomic (all instances updated simultaneously)
✅ Each tag must be unique, cannot edit/remove previous tags

See: https://developers.cloudflare.com/agents/api-reference/configuration/

Core Agent Patterns

Agent Class Basics - Extend Agent<Env, State> with lifecycle methods:

onStart() - Agent initialization
onRequest() - Handle HTTP requests
onConnect/onMessage/onClose() - WebSocket handling
onStateUpdate() - React to state changes

Key Properties:

this.env - Environment bindings (AI, DB, etc.)
this.state - Current agent state (read-only)
this.setState() - Update persisted state
this.sql - Built-in SQLite database
this.name - Agent instance identifier
this.schedule() - Schedule future tasks

See: Official Agent API docs at https://developers.cloudflare.com/agents/api-reference/agents-api/

WebSockets & Real-Time Communication

Agents support WebSockets for bidirectional real-time communication. Use when you need:

Client can send messages while server streams
Agent-initiated messages (notifications, updates)
Long-lived connections with state

Basic Pattern:

export class ChatAgent extends Agent<Env, State> {
  async onConnect(connection: Connection, ctx: ConnectionContext) {
    // Auth check, add to participants, send welcome
  }

  async onMessage(connection: Connection, message: WSMessage) {
    // Process message, update state, broadcast response
  }
}


SSE Alternative: For one-way server → client streaming (simpler, HTTP-based), use Server-Sent Events instead of WebSockets.

See: https://developers.cloudflare.com/agents/api-reference/websockets/

State Management

Two State Mechanisms:

this.setState(newState) - JSON-serializable state (up to 1GB)

Automatically persisted, syncs to WebSocket clients
Use for: User preferences, session data, small datasets

this.sql - Built-in SQLite database (up to 1GB)

Tagged template literals prevent SQL injection
Use for: Relational data, large datasets, complex queries

State Rules:

✅ JSON-serializable only (objects, arrays, primitives, null)
✅ Persists across restarts, immediately consistent
❌ No functions or circular references
❌ 1GB total limit (state + SQL combined)

SQL Pattern:

await this.sql`CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT)`
await this.sql`INSERT INTO users (email) VALUES (${userEmail})`  // ← Prepared statement
const users = await this.sql`SELECT * FROM users WHERE email = ${email}`  // ← Returns array

State Type Safety Gotcha

CRITICAL: Providing a type parameter to state methods does NOT validate that the result matches your type definition. In TypeScript, properties (fields) that do not exist or conform to the type you provided will be dropped silently.

interface MyState {
  count: number;
  name: string;
}

export class MyAgent extends Agent<Env, MyState> {
  initialState = { count: 0, name: "default" };

  async increment() {
    // TypeScript allows this, but runtime may differ
    const currentState = this.state; // Type is MyState

    // If state was corrupted/modified externally:
    // { count: "invalid", otherField: 123 }
    // TypeScript still shows it as MyState
    // count field doesn't match (string vs number)
    // otherField is dropped silently
  }
}


Prevention: Add runtime validation for critical state operations:

// Validate state shape at runtime
function validateState(state: unknown): state is MyState {
  return (
    typeof state === 'object' &&
    state !== null &&
    'count' in state &&
    typeof (state as MyState).count === 'number' &&
    'name' in state &&
    typeof (state as MyState).name === 'string'
  );
}

async increment() {
  if (!validateState(this.state)) {
    console.error('State validation failed', this.state);
    // Reset to valid state
    await this.setState(this.initialState);
    return;
  }

  // Safe to use
  const newCount = this.state.count + 1;
  await this.setState({ ...this.state, count: newCount });
}


See: https://developers.cloudflare.com/agents/api-reference/store-and-sync-state/

Schedule Tasks

Agents can schedule tasks to run in the future using this.schedule().

Delay (Seconds)
export class MyAgent extends Agent {
  async onRequest(request: Request): Promise<Response> {
    // Schedule task to run in 60 seconds
    const { id } = await this.schedule(60, "checkStatus", { requestId: "123" });

    return Response.json({ scheduledTaskId: id });
  }

  // This method will be called in 60 seconds
  async checkStatus(data: { requestId: string }) {
    console.log('Checking status for request:', data.requestId);
    // Perform check, update state, send notification, etc.
  }
}

Specific Date
export class MyAgent extends Agent {
  async scheduleReminder(reminderDate: string) {
    const date = new Date(reminderDate);

    const { id } = await this.schedule(date, "sendReminder", {
      message: "Time for your appointment!"
    });

    return id;
  }

  async sendReminder(data: { message: string }) {
    console.log('Sending reminder:', data.message);
    // Send email, push notification, etc.
  }
}

Cron Expressions
export class MyAgent extends Agent {
  async setupRecurringTasks() {
    // Every 10 minutes
    await this.schedule("*/10 * * * *", "checkUpdates", {});

    // Every day at 8 AM
    await this.schedule("0 8 * * *", "dailyReport", {});

    // Every Monday at 9 AM
    await this.schedule("0 9 * * 1", "weeklyReport", {});

    // Every hour on the hour
    await this.schedule("0 * * * *", "hourlyCheck", {});
  }

  async checkUpdates(data: any) {
    console.log('Checking for updates...');
  }

  async dailyReport(data: any) {
    console.log('Generating daily report...');
  }

  async weeklyReport(data: any) {
    console.log('Generating weekly report...');
  }

  async hourlyCheck(data: any) {
    console.log('Running hourly check...');
  }
}

Managing Scheduled Tasks
export class MyAgent extends Agent {
  async manageSchedules() {
    // Get all scheduled tasks
    const allTasks = this.getSchedules();
    console.log('Total tasks:', allTasks.length);

    // Get specific task by ID
    const taskId = "some-task-id";
    const task = await this.getSchedule(taskId);

    if (task) {
      console.log('Task:', task.callback, 'at', new Date(task.time));
      console.log('Payload:', task.payload);
      console.log('Type:', task.type);  // "scheduled" | "delayed" | "cron"

      // Cancel the task
      const cancelled = await this.cancelSchedule(taskId);
      console.log('Cancelled:', cancelled);
    }

    // Get tasks in time range
    const upcomingTasks = this.getSchedules({
      timeRange: {
        start: new Date(),
        end: new Date(Date.now() + 24 * 60 * 60 * 1000)  // Next 24 hours
      }
    });

    console.log('Upcoming tasks:', upcomingTasks.length);

    // Filter by type
    const cronTasks = this.getSchedules({ type: "cron" });
    const delayedTasks = this.getSchedules({ type: "delayed" });
  }
}


Scheduling Constraints:

Each task maps to a SQL database row (max 2 MB per task)
Total tasks limited by: (task_size * count) + other_state < 1GB
Cron tasks continue running until explicitly cancelled
Callback method MUST exist on Agent class (throws error if missing)

CRITICAL ERROR: If callback method doesn't exist:

// ❌ BAD: Method doesn't exist
await this.schedule(60, "nonExistentMethod", {});

// ✅ GOOD: Method exists
await this.schedule(60, "existingMethod", {});

async existingMethod(data: any) {
  // Implementation
}

Run Workflows

Agents can trigger asynchronous Cloudflare Workflows.

Workflow Binding Configuration

wrangler.jsonc:

{
  "workflows": [
    {
      "name": "MY_WORKFLOW",
      "class_name": "MyWorkflow"
    }
  ]
}


If Workflow is in a different script:

{
  "workflows": [
    {
      "name": "EMAIL_WORKFLOW",
      "class_name": "EmailWorkflow",
      "script_name": "email-workflows"  // Different project
    }
  ]
}

Triggering a Workflow
import { Agent } from "agents";
import { WorkflowEntrypoint, WorkflowEvent, WorkflowStep } from "cloudflare:workers";

interface Env {
  MY_WORKFLOW: Workflow;
  MyAgent: AgentNamespace<MyAgent>;
}

export class MyAgent extends Agent<Env> {
  async onRequest(request: Request): Promise<Response> {
    const userId = new URL(request.url).searchParams.get('userId');

    // Trigger a workflow immediately
    const instance = await this.env.MY_WORKFLOW.create({
      id: `user-${userId}`,
      params: { userId, action: "process" }
    });

    // Or schedule a delayed workflow trigger
    await this.schedule(300, "runWorkflow", { userId });

    return Response.json({ workflowId: instance.id });
  }

  async runWorkflow(data: { userId: string }) {
    const instance = await this.env.MY_WORKFLOW.create({
      id: `delayed-${data.userId}`,
      params: data
    });

    // Monitor workflow status periodically
    await this.schedule("*/5 * * * *", "checkWorkflowStatus", { id: instance.id });
  }

  async checkWorkflowStatus(data: { id: string }) {
    // Check workflow status (see Workflows docs for details)
    console.log('Checking workflow:', data.id);
  }
}

// Workflow definition (can be in same or different file/project)
export class MyWorkflow extends WorkflowEntrypoint<Env> {
  async run(event: WorkflowEvent<{ userId: string }>, step: WorkflowStep) {
    // Workflow implementation
    const result = await step.do('process-data', async () => {
      return { processed: true };
    });

    return result;
  }
}

Agents vs Workflows
Feature	Agents	Workflows
Purpose	Interactive, user-facing	Background processing
Duration	Seconds to hours	Minutes to hours
State	SQLite database	Step-based checkpoints
Interaction	WebSockets, HTTP	No direct interaction
Retry	Manual	Automatic per step
Use Case	Chat, real-time UI	ETL, batch processing

Best Practice: Use Agents to coordinate multiple Workflows. Agents can trigger, monitor, and respond to Workflow results while maintaining user interaction.

Browse the Web

Agents can use Browser Rendering for web scraping and automation:

Binding: Add "browser": { "binding": "BROWSER" } to wrangler.jsonc Package: @cloudflare/puppeteer Use Case: Web scraping, screenshots, automated browsing within agent workflows

See: cloudflare-browser-rendering skill for complete Puppeteer + Workers integration guide.

Retrieval Augmented Generation (RAG)

Agents can implement RAG using Vectorize (vector database) + Workers AI (embeddings):

Pattern: Ingest docs → generate embeddings → store in Vectorize → query → retrieve context → pass to AI

Bindings:

"ai": { "binding": "AI" } - Workers AI for embeddings
"vectorize": { "bindings": [{ "binding": "VECTORIZE", "index_name": "my-vectors" }] } - Vector search

Typical Workflow:

Generate embeddings with Workers AI (@cf/baai/bge-base-en-v1.5)
Upsert vectors to Vectorize (this.env.VECTORIZE.upsert(vectors))
Query similar vectors (this.env.VECTORIZE.query(queryVector, { topK: 5 }))
Use retrieved context in AI prompt

See: cloudflare-vectorize skill for complete RAG implementation guide.

Using AI Models

Agents can call AI models using:

Vercel AI SDK (recommended): Multi-provider, automatic streaming, tool calling
Workers AI: Cloudflare's on-platform inference (cost-effective, manual parsing)

Architecture Note: Agents SDK provides infrastructure (WebSockets, state, scheduling). AI inference is a separate layer - use AI SDK for the "brain".

See:

ai-sdk-core skill for complete AI SDK integration patterns
cloudflare-workers-ai skill for Workers AI streaming parsing
Calling Agents

Two Main Patterns:

routeAgentRequest(request, env) - Auto-route via URL pattern /agents/:agent/:name

Example: /agents/my-agent/user-123 routes to MyAgent instance "user-123"

getAgentByName<Env, T>(env.AgentBinding, instanceName) - Custom routing

Returns agent stub for calling methods or passing requests
Example: const agent = getAgentByName(env.MyAgent, 'user-${userId}')

Multi-Agent Communication:

export class AgentA extends Agent<Env> {
  async processData(data: any) {
    const agentB = getAgentByName<Env, AgentB>(this.env.AgentB, 'processor-1');
    return await (await agentB).analyze(data);
  }
}


CRITICAL Security: Always authenticate in Worker BEFORE creating/accessing agents. Agents should assume the caller is authorized.

See: https://developers.cloudflare.com/agents/api-reference/calling-agents/

Client APIs

Browser/React Integration:

AgentClient (from agents/client) - WebSocket client for browser
agentFetch (from agents/client) - HTTP requests to agents
useAgent (from agents/react) - React hook for WebSocket connections + state sync
useAgentChat (from agents/ai-react) - Pre-built chat UI hook

All client libraries automatically handle: WebSocket connections, state synchronization, reconnection logic.

See: https://developers.cloudflare.com/agents/api-reference/client-apis/

Model Context Protocol (MCP)

Build MCP servers using the Agents SDK.

MCP Server Setup
npm install @modelcontextprotocol/sdk agents

Basic MCP Server
import { McpAgent } from "agents/mcp";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

export class MyMCP extends McpAgent {
  server = new McpServer({ name: "Demo", version: "1.0.0" });

  async init() {
    // Define a tool
    this.server.tool(
      "add",
      "Add two numbers together",
      {
        a: z.number().describe("First number"),
        b: z.number().describe("Second number")
      },
      async ({ a, b }) => ({
        content: [{ type: "text", text: String(a + b) }]
      })
    );
  }
}

Stateful MCP Server
type State = { counter: number };

export class StatefulMCP extends McpAgent<Env, State> {
  server = new McpServer({ name: "Counter", version: "1.0.0" });

  initialState: State = { counter: 0 };

  async init() {
    // Resource
    this.server.resource(
      "counter",
      "mcp://resource/counter",
      (uri) => ({
        contents: [{ uri: uri.href, text: String(this.state.counter) }]
      })
    );

    // Tool
    this.server.tool(
      "increment",
      "Increment the counter",
      { amount: z.number() },
      async ({ amount }) => {
        this.setState({
          ...this.state,
          counter: this.state.counter + amount
        });

        return {
          content: [{
            type: "text",
            text: `Counter is now ${this.state.counter}`
          }]
        };
      }
    );
  }
}

MCP Transport Configuration
import { Hono } from 'hono';

const app = new Hono();

// Modern streamable HTTP transport (recommended)
app.mount('/mcp', MyMCP.serve('/mcp').fetch, { replaceRequest: false });

// Legacy SSE transport (deprecated)
app.mount('/sse', MyMCP.serveSSE('/sse').fetch, { replaceRequest: false });

export default app;


Transport Comparison:

/mcp: Streamable HTTP (modern, recommended)
/sse: Server-Sent Events (legacy, deprecated)
MCP Protocol Version Support

The Agents SDK supports multiple MCP protocol versions. As of agents@0.3.x, version validation is permissive to accept newer protocol versions:

Supported versions: 2024-11-05, 2025-11-25, and future versions
Error (before 0.3.x): Error: Unsupported MCP protocol version: 2025-11-25
Fixed: Version validation now accepts any non-ancient protocol version

This aligns with the MCP community's move to stateless transports. If you encounter protocol version errors, update to agents@0.3.x or later.

Source: GitHub Issue #769

MCP with OAuth
import { OAuthProvider } from '@cloudflare/workers-oauth-provider';

export default new OAuthProvider({
  apiHandlers: {
    '/sse': MyMCP.serveSSE('/sse'),
    '/mcp': MyMCP.serve('/mcp')
  },
  // OAuth configuration
  clientId: 'your-client-id',
  clientSecret: 'your-client-secret',
  // ... other OAuth settings
});

Testing MCP Server
# Run MCP inspector
npx @modelcontextprotocol/inspector@latest

# Connect to: http://localhost:8788/mcp


Cloudflare's MCP Servers: See reference for production examples.

Critical Rules
Always Do ✅
Export Agent class - Must be exported for binding to work
Include new_sqlite_classes in v1 migration - Cannot add SQLite later
Match binding name to class name - Prevents "binding not found" errors
Authenticate in Worker, not Agent - Security best practice
Use tagged template literals for SQL - Prevents SQL injection
Handle WebSocket disconnections - State persists, connections don't
Verify scheduled task callback exists - Throws error if method missing
Use idFromName() for user-specific agents - NEVER use newUniqueId() for persistent state (see Issue #23)
Check state size limits - Max 1GB total per agent
Monitor task payload size - Max 2MB per scheduled task
Use workflow bindings correctly - Must be configured in wrangler.jsonc
Create Vectorize indexes before inserting - Required for metadata filtering
Close browser instances - Prevent resource leaks
Use setState() for persistence - Don't just modify this.state
Test migrations locally first - Migrations are atomic, can't rollback
Prune WebSocket message history - Stay under 1MB cumulative payload (see Issue #17)
Validate state shape at runtime - TypeScript types don't enforce runtime validation (see State Type Safety)
Never Do ❌
Don't add SQLite to existing deployed class - Must be in first migration
Don't gradually deploy migrations - Atomic only
Don't skip authentication in Worker - Always auth before agent access
Don't construct SQL strings manually - Use tagged templates
Don't exceed 1GB state per agent - Hard limit
Don't schedule tasks with non-existent callbacks - Runtime error
Don't use newUniqueId() for user-specific agents - State won't persist (see Issue #23)
Don't use SSE for MCP - Deprecated, use /mcp transport
Don't forget browser binding - Required for web browsing
Don't modify this.state directly - Use setState() instead
Don't let WebSocket payloads exceed 1MB - Connection will crash (see Issue #17)
Don't trust TypeScript types for state validation - Add runtime checks (see State Type Safety)
Known Issues Prevention

This skill prevents 23 documented issues:

Issue 1: Migrations Not Atomic

Error: "Cannot gradually deploy migration" Source: https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/ Why: Migrations apply to all instances simultaneously Prevention: Deploy migrations independently of code changes, use npx wrangler versions deploy

Issue 2: Missing new_sqlite_classes

Error: "Cannot enable SQLite on existing class" Source: https://developers.cloudflare.com/agents/api-reference/configuration/ Why: SQLite must be enabled in first migration Prevention: Include new_sqlite_classes in tag "v1" migration

Issue 3: Agent Class Not Exported

Error: "Binding not found" or "Cannot access undefined" Source: https://developers.cloudflare.com/agents/api-reference/agents-api/ Why: Durable Objects require exported class Prevention: export class MyAgent extends Agent (with export keyword)

Issue 4: Binding Name Mismatch

Error: "Binding 'X' not found" Source: https://developers.cloudflare.com/agents/api-reference/configuration/ Why: Binding name must match class name exactly Prevention: Ensure name and class_name are identical in wrangler.jsonc

Issue 5: Global Uniqueness Not Understood

Error: Unexpected behavior with agent instances Source: https://developers.cloudflare.com/agents/api-reference/agents-api/ Why: Same name always returns same agent instance globally Prevention: Use unique identifiers (userId, sessionId) for instance names

Issue 6: WebSocket State Not Persisted

Error: Connection state lost after disconnect Source: https://developers.cloudflare.com/agents/api-reference/websockets/ Why: WebSocket connections don't persist, but agent state does Prevention: Store important data in agent state via setState(), not connection state

Issue 7: Scheduled Task Callback Doesn't Exist / Long AI Requests Timeout

Error: "Method X does not exist on Agent" or "IoContext timed out due to inactivity" or "A call to blockConcurrencyWhile() waited for too long" Source: https://developers.cloudflare.com/agents/api-reference/schedule-tasks/ and GitHub Issue #600 Why: this.schedule() calls method that isn't defined, OR scheduled callbacks failed when AI requests exceeded 30 seconds due to blockConcurrencyWhile wrapper (fixed in agents@0.2.x via PR #653) Prevention: Ensure callback method exists before scheduling. For long-running AI requests, update to agents@0.2.x or later.

Historical issue (before 0.2.x): Scheduled callbacks were wrapped in blockConcurrencyWhile, which enforced a 30-second limit. AI requests exceeding this would fail even though they were valid async operations.

// ✅ Fixed in 0.2.x - schedule callbacks can now run for their full duration
export class MyAgent extends Agent<Env> {
  async onRequest(request: Request) {
    await this.schedule(60, "processAIRequest", { query: "..." });
  }

  async processAIRequest(data: { query: string }) {
    // This can now take > 30s without timeout
    const result = await streamText({
      model: openai('gpt-4o'),
      messages: [{ role: 'user', content: data.query }]
    });
  }
}

Issue 8: State Size Limit Exceeded

Error: "Maximum database size exceeded" Source: https://developers.cloudflare.com/agents/api-reference/store-and-sync-state/ Why: Agent state + scheduled tasks exceed 1GB Prevention: Monitor state size, use external storage (D1, R2) for large data

Issue 9: Scheduled Task Too Large

Error: "Task payload exceeds 2MB" Source: https://developers.cloudflare.com/agents/api-reference/schedule-tasks/ Why: Each task maps to database row with 2MB limit Prevention: Keep task payloads minimal, store large data in agent state/SQL

Issue 10: Workflow Binding Missing

Error: "Cannot read property 'create' of undefined" Source: https://developers.cloudflare.com/agents/api-reference/run-workflows/ Why: Workflow binding not configured in wrangler.jsonc Prevention: Add workflow binding before using this.env.WORKFLOW

Issue 11: Browser Binding Required

Error: "BROWSER binding undefined" Source: https://developers.cloudflare.com/agents/api-reference/browse-the-web/ Why: Browser Rendering requires explicit binding Prevention: Add "browser": { "binding": "BROWSER" } to wrangler.jsonc

Issue 12: Vectorize Index Not Found

Error: "Index does not exist" Source: https://developers.cloudflare.com/agents/api-reference/rag/ Why: Vectorize index must be created before use Prevention: Run wrangler vectorize create before deploying agent

Issue 13: MCP Transport Confusion

Error: "SSE transport deprecated" Source: https://developers.cloudflare.com/agents/model-context-protocol/transport/ Why: SSE transport is legacy, streamable HTTP is recommended Prevention: Use /mcp endpoint with MyMCP.serve('/mcp'), not /sse

Issue 14: Authentication Bypass

Error: Security vulnerability Source: https://developers.cloudflare.com/agents/api-reference/calling-agents/ Why: Authentication done in Agent instead of Worker Prevention: Always authenticate in Worker before calling getAgentByName()

Issue 15: Instance Naming Errors

Error: Cross-user data leakage Source: https://developers.cloudflare.com/agents/api-reference/calling-agents/ Why: Poor instance naming allows access to wrong agent Prevention: Use namespaced names like user-${userId}, validate ownership

Issue 16: Workers AI Streaming Requires Manual Parsing

Error: "Cannot read property 'response' of undefined" or empty AI responses Source: https://developers.cloudflare.com/workers-ai/platform/streaming/ Why: Workers AI returns streaming responses as Uint8Array in Server-Sent Events (SSE) format, not plain objects Prevention: Use TextDecoder + SSE parsing pattern (see "Workers AI (Alternative for AI)" section above)

The problem - Attempting to access stream chunks directly fails:

const response = await env.AI.run(model, { stream: true });
for await (const chunk of response) {
  console.log(chunk.response);  // ❌ undefined - chunk is Uint8Array, not object
}


The solution - Parse SSE format manually:

const response = await env.AI.run(model, { stream: true });
for await (const chunk of response) {
  const text = new TextDecoder().decode(chunk);  // Step 1: Uint8Array → string
  if (text.startsWith('data: ')) {              // Step 2: Check SSE format
    const jsonStr = text.slice(6).trim();       // Step 3: Extract JSON from "data: {...}"
    if (jsonStr === '[DONE]') break;            // Step 4: Handle termination
    const data = JSON.parse(jsonStr);           // Step 5: Parse JSON
    if (data.response) {                        // Step 6: Extract .response field
      fullResponse += data.response;
    }
  }
}


Better alternative: Use Vercel AI SDK which handles this automatically:

import { streamText } from 'ai';
import { createCloudflare } from '@ai-sdk/cloudflare';

const cloudflare = createCloudflare();
const result = streamText({
  model: cloudflare('@cf/meta/llama-3-8b-instruct', { binding: env.AI }),
  messages
});
// No manual parsing needed ✅


When to accept manual parsing:

Cost is critical (Workers AI is cheaper)
No external dependencies allowed
Willing to maintain SSE parsing code

When to use AI SDK instead:

Value developer time over compute cost
Want automatic streaming
Need multi-provider support
Issue 17: WebSocket Payload Size Limit (1MB)

Error: Error: internal error; reference = [reference ID] Source: GitHub Issue #119 Why: WebSocket connections fail when cumulative message payload exceeds approximately 1 MB. After 5-6 tool calls returning large data (e.g., 200KB+ each), the payload exceeds the limit and the connection crashes with "internal error". Prevention: Prune message history client-side to stay under 950KB

The problem: All messages—including large tool results—are streamed back to the client and LLM for continued conversations, causing cumulative payload growth.

// Workaround: Prune old messages client-side
function pruneMessages(messages: Message[]): Message[] {
  let totalSize = 0;
  const pruned = [];

  // Keep recent messages until we hit size limit
  for (let i = messages.length - 1; i >= 0; i--) {
    const msgSize = JSON.stringify(messages[i]).length;
    if (totalSize + msgSize > 950_000) break; // 950KB limit
    pruned.unshift(messages[i]);
    totalSize += msgSize;
  }

  return pruned;
}

// Use before sending to agent
const prunedMessages = pruneMessages(allMessages);


Better solution (proposed): Server-side context management where only message summaries are sent to the client, not full tool results.

Issue 18: Duplicate Assistant Messages with needsApproval Tools

Error: Duplicate messages with identical toolCallId, original stuck in input-available state Source: GitHub Issue #790 Why: When using needsApproval: true on tools, the system creates duplicate assistant messages instead of updating the original one. The server-generated message (state input-available) never transitions to approval-responded when client approves. Prevention: Understand this is a known limitation. Track both message IDs in your UI until fixed.

// Current behavior (agents@0.3.3)
export class MyAgent extends AIChatAgent<Env> {
  tools = {
    sensitiveAction: tool({
      needsApproval: true,  // ⚠️ Causes duplicate messages
      execute: async (args) => {
        return { result: "action completed" };
      }
    })
  };
}

// Result: Two messages persist
// 1. Server message: ID "assistant_1768917665170_4mub00d32", state "input-available"
// 2. Client message: ID "oFwQwEpvLd8f1Gwd", state "approval-responded"


Workaround: Handle both messages in your UI or avoid needsApproval until this is resolved.

Issue 19: Duplicate Messages with Client-Side Tool Execution (Fixed in 0.2.31+)

Error: Duplicate item found with id rs_xxx (OpenAI API rejection) Source: GitHub Issue #728 Fixed In: agents@0.2.31+ Why: When using useAgentChat with client-side tools lacking server-side execute functions, the agents library created duplicate assistant messages sharing identical reasoning IDs, triggering OpenAI API rejection. Prevention: Update to agents@0.2.31 or later

Historical issue (before 0.2.31): Client-side tool execution created new messages instead of updating existing ones, leaving the original stuck in incomplete state and causing duplicate providerMetadata.openai.itemId values.

// ✅ Fixed in 0.2.31+ - no changes needed
// Just ensure you're on agents@0.2.31 or later

Issue 20: Async Querying Cache TTL Not Honored (Fixed)

Error: 401 Unauthorized errors after token expiration despite cacheTtl setting Source: GitHub Issue #725 Fixed In: Check agents release notes Why: The useAgent hook had a caching problem where the queryPromise was computed once per cacheKey and kept forever, even after TTL expired. The useMemo implementation didn't include time in dependencies, so TTL was never enforced. Prevention: Update to latest agents version

Historical workaround (before fix):

// Force cache invalidation by including token version in queryDeps
const [tokenVersion, setTokenVersion] = useState(0);

const { state } = useAgent({
  query: async () => ({ token: await getJWT() }),
  queryDeps: [tokenVersion], // ✅ Force new cache key
  cacheTtl: 60_000,
});

// Manually refresh token before expiry
useEffect(() => {
  const interval = setInterval(() => {
    setTokenVersion(v => v + 1);
  }, 50_000); // Refresh every 50s
  return () => clearInterval(interval);
}, []);

Issue 21: jsonSchemaValidator Breaks After DO Hibernation (Fixed)

Error: TypeError: validator.getValidator is not a function Source: GitHub Issue #663 Fixed In: Check agents release notes Why: When a Durable Object hibernated and restored, the Agents SDK serialized MCP connection options using JSON.stringify(), converting class instances like CfWorkerJsonSchemaValidator into plain objects without methods. Upon restoration via JSON.parse(), the validator lost its methods. Prevention: Update to latest agents version (validator now built-in)

Historical issue (before fix):

// ❌ Before fix - manual validator caused errors
import { CfWorkerJsonSchemaValidator } from '@modelcontextprotocol/sdk/cloudflare-worker';

const mcpAgent = new McpAgent({
  client: {
    jsonSchemaValidator: new CfWorkerJsonSchemaValidator(), // Got serialized to {}
  }
});


Current approach (fixed):

// ✅ Now automatic - no manual validator needed
const mcpAgent = new McpAgent({
  // SDK handles validator internally
});

Issue 22: WorkerTransport ClientCapabilities Lost After Hibernation (Fixed in 0.3.5+)

Error: Error: Client does not support form elicitation Source: GitHub Issue #777 Fixed In: agents@0.3.5+ Why: When using WorkerTransport with MCP servers in serverless environments, client capabilities failed to persist across Durable Object hibernation cycles because the TransportState interface only stored sessionId and initialized status, not clientCapabilities. Prevention: Update to agents@0.3.5 or later

Historical issue (before 0.3.5):

// Client advertised elicitation capability during handshake,
// but after hibernation, capability info was lost
await server.elicitInput({ /* form */ }); // ❌ Error: capabilities lost


Solution (fixed in 0.3.5):

// TransportState now includes clientCapabilities
interface TransportState {
  sessionId: string;
  initialized: boolean;
  clientCapabilities?: ClientCapabilities; // ✅ Now persisted
}

Issue 23: idFromName() vs newUniqueId() Critical Pattern

Error: State never persists, new agent instance every request Source: Cloudflare blog - Building agents with OpenAI Why: If you use newUniqueId() instead of idFromName(), you'll get a new agent instance each time, and your memory/state will never persist. This is a common early bug that silently kills statefulness. Prevention: Always use idFromName() for user-specific agents, never newUniqueId()

// ❌ WRONG: Creates new agent every time (state never persists)
export default {
  async fetch(request: Request, env: Env) {
    const id = env.MyAgent.newUniqueId(); // New ID = new instance
    const agent = env.MyAgent.get(id);

    // State never persists - different instance each time
    return agent.fetch(request);
  }
}

// ✅ CORRECT: Same user = same agent = persistent state
export default {
  async fetch(request: Request, env: Env) {
    const userId = getUserId(request);
    const id = env.MyAgent.idFromName(userId); // Same ID for same user
    const agent = env.MyAgent.get(id);

    // State persists across requests for this user
    return agent.fetch(request);
  }
}


Why It Matters:

newUniqueId(): Generates a random unique ID each call → new agent instance
idFromName(string): Deterministic ID from string → same agent for same input

Rule of thumb: Use idFromName() for 99% of cases. Only use newUniqueId() when you genuinely need a one-time, ephemeral agent instance.

Dependencies
Required
cloudflare-worker-base - Foundation (Hono, Vite, Workers setup)
Optional (by feature)
cloudflare-workers-ai - For Workers AI model calls
cloudflare-vectorize - For RAG with Vectorize
cloudflare-d1 - For additional persistent storage beyond agent state
cloudflare-r2 - For file storage
cloudflare-queues - For message queues
NPM Packages
agents - Agents SDK (required)
@modelcontextprotocol/sdk - For building MCP servers
@cloudflare/puppeteer - For web browsing
ai - AI SDK for model calls
@ai-sdk/openai - OpenAI models
@ai-sdk/anthropic - Anthropic models
Official Documentation
Agents SDK: https://developers.cloudflare.com/agents/
API Reference: https://developers.cloudflare.com/agents/api-reference/
Durable Objects: https://developers.cloudflare.com/durable-objects/
Workflows: https://developers.cloudflare.com/workflows/
Vectorize: https://developers.cloudflare.com/vectorize/
Browser Rendering: https://developers.cloudflare.com/browser-rendering/
Model Context Protocol: https://modelcontextprotocol.io/
Cloudflare MCP Servers: https://github.com/cloudflare/mcp-server-cloudflare
Bundled Resources
Templates (templates/)
wrangler-agents-config.jsonc - Complete configuration example
basic-agent.ts - Minimal HTTP agent
websocket-agent.ts - WebSocket handlers
state-sync-agent.ts - State management patterns
scheduled-agent.ts - Task scheduling
workflow-agent.ts - Workflow integration
browser-agent.ts - Web browsing
rag-agent.ts - RAG implementation
chat-agent-streaming.ts - Streaming chat
calling-agents-worker.ts - Agent routing
react-useagent-client.tsx - React client
mcp-server-basic.ts - MCP server
hitl-agent.ts - Human-in-the-loop
References (references/)
agent-class-api.md - Complete Agent class reference
client-api-reference.md - Browser client APIs
state-management-guide.md - State and SQL deep dive
websockets-sse.md - WebSocket vs SSE comparison
scheduling-api.md - Task scheduling details
workflows-integration.md - Workflows guide
browser-rendering.md - Web browsing patterns
rag-patterns.md - RAG best practices
mcp-server-guide.md - MCP server development
mcp-tools-reference.md - MCP tools API
hitl-patterns.md - Human-in-the-loop workflows
best-practices.md - Production patterns
Examples (examples/)
chat-bot-complete.md - Full chat agent
multi-agent-workflow.md - Agent orchestration
scheduled-reports.md - Recurring tasks
browser-scraper-agent.md - Web scraping
rag-knowledge-base.md - RAG system
mcp-remote-server.md - Production MCP server

Last Verified: 2026-01-21 Package Versions: agents@0.3.6 Compliance: Cloudflare Agents SDK official documentation Changes: Added 7 new issues from community research (WebSocket payload limits, state type safety, idFromName gotcha), updated to agents@0.3.6

Weekly Installs
332
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn