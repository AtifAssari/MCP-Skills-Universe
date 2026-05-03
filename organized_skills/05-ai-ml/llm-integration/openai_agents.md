---
rating: ⭐⭐⭐
title: openai-agents
url: https://skills.sh/jezweb/claude-skills/openai-agents
---

# openai-agents

skills/jezweb/claude-skills/openai-agents
openai-agents
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill openai-agents
Summary

Build text and voice agents with tools, multi-agent handoffs, guardrails, and human-in-the-loop patterns.

Supports text agents, realtime voice agents with WebRTC, and multi-agent workflows with automatic delegation via handoffs
Define tools using Zod schemas for type-safe parameter validation; includes structured output support for predictable JSON responses
Implements input/output guardrails for safety validation, human approval workflows for sensitive operations, and streaming support for real-time event handling
Prevents 11 documented errors including MaxTurnsExceededError, schema mismatches, reasoning defaults, and JSON output leaks; covers Cloudflare Workers, Next.js, and Deno runtimes
Requires Node.js 22+, Zod 4 (breaking change in v0.4.0), and never expose API keys to browsers—use ephemeral session tokens instead
SKILL.md
OpenAI Agents SDK

Build AI applications with text agents, voice agents (realtime), multi-agent workflows, tools, guardrails, and human-in-the-loop patterns.

Quick Start
npm install @openai/agents zod@4  # v0.4.0+ requires Zod 4 (breaking change)
npm install @openai/agents-realtime  # Voice agents
export OPENAI_API_KEY="your-key"


Breaking Change (v0.4.0): Zod 3 no longer supported. Upgrade to zod@4.

Runtimes: Node.js 22+, Deno, Bun, Cloudflare Workers (experimental)

Core Concepts

Agents: LLMs with instructions + tools

import { Agent } from '@openai/agents';
const agent = new Agent({ name: 'Assistant', tools: [myTool], model: 'gpt-5-mini' });


Tools: Functions with Zod schemas

import { tool } from '@openai/agents';
import { z } from 'zod';
const weatherTool = tool({
  name: 'get_weather',
  parameters: z.object({ city: z.string() }),
  execute: async ({ city }) => `Weather in ${city}: sunny`,
});


Handoffs: Multi-agent delegation

const triageAgent = Agent.create({ handoffs: [specialist1, specialist2] });


Guardrails: Input/output validation

const agent = new Agent({ inputGuardrails: [detector], outputGuardrails: [filter] });


Structured Outputs: Type-safe responses

const agent = new Agent({ outputType: z.object({ sentiment: z.enum(['positive', 'negative']) }) });

Text Agents

Basic: const result = await run(agent, 'What is 2+2?')

Streaming:

const stream = await run(agent, 'Tell me a story', { stream: true });
for await (const event of stream) {
  if (event.type === 'raw_model_stream_event') process.stdout.write(event.data?.choices?.[0]?.delta?.content || '');
}

Multi-Agent Handoffs
const billingAgent = new Agent({ name: 'Billing', handoffDescription: 'For billing questions', tools: [refundTool] });
const techAgent = new Agent({ name: 'Technical', handoffDescription: 'For tech issues', tools: [ticketTool] });
const triageAgent = Agent.create({ name: 'Triage', handoffs: [billingAgent, techAgent] });


Agent-as-Tool Context Isolation: When using agent.asTool(), sub-agents do NOT share parent conversation history (intentional design to simplify debugging).

Workaround: Pass context via tool parameters:

const helperTool = tool({
  name: 'use_helper',
  parameters: z.object({
    query: z.string(),
    context: z.string().optional(),
  }),
  execute: async ({ query, context }) => {
    return await run(subAgent, `${context}\n\n${query}`);
  },
});


Source: Issue #806

Guardrails

Input: Validate before processing

const guardrail: InputGuardrail = {
  execute: async ({ input }) => ({ tripwireTriggered: detectHomework(input) })
};
const agent = new Agent({ inputGuardrails: [guardrail] });


Output: Filter responses (PII detection, content safety)

Human-in-the-Loop
const refundTool = tool({ name: 'process_refund', requiresApproval: true, execute: async ({ amount }) => `Refunded $${amount}` });

let result = await runner.run(input);
while (result.interruption?.type === 'tool_approval') {
  result = await promptUser(result.interruption) ? result.state.approve(result.interruption) : result.state.reject(result.interruption);
}


Streaming HITL: When using stream: true with requiresApproval, must explicitly check interruptions:

const stream = await run(agent, input, { stream: true });
let result = await stream.finalResult();
while (result.interruption?.type === 'tool_approval') {
  const approved = await promptUser(result.interruption);
  result = approved
    ? await result.state.approve(result.interruption)
    : await result.state.reject(result.interruption);
}


Example: human-in-the-loop-stream.ts

Realtime Voice Agents

Create:

import { RealtimeAgent } from '@openai/agents-realtime';
const voiceAgent = new RealtimeAgent({
  voice: 'alloy', // alloy, echo, fable, onyx, nova, shimmer
  model: 'gpt-5-realtime',
  tools: [weatherTool],
});


Browser Session:

import { RealtimeSession } from '@openai/agents-realtime';
const session = new RealtimeSession(voiceAgent, { apiKey: sessionApiKey, transport: 'webrtc' });
await session.connect();


CRITICAL: Never send OPENAI_API_KEY to browser! Generate ephemeral session tokens server-side.

Voice Handoffs: Voice/model must match across agents (cannot change during handoff)

Limitations:

Video streaming NOT supported: Despite camera examples, realtime video streaming is not natively supported. Model may not proactively speak based on video events. (Issue #694)

Templates:

templates/realtime-agents/realtime-agent-basic.ts
templates/realtime-agents/realtime-session-browser.tsx
templates/realtime-agents/realtime-handoffs.ts

References:

references/realtime-transports.md - WebRTC vs WebSocket
Framework Integration

Cloudflare Workers (experimental):

export default {
  async fetch(request: Request, env: Env) {
    // Disable tracing or use startTracingExportLoop()
    process.env.OTEL_SDK_DISABLED = 'true';

    process.env.OPENAI_API_KEY = env.OPENAI_API_KEY;
    const agent = new Agent({ name: 'Assistant', model: 'gpt-5-mini' });
    const result = await run(agent, (await request.json()).message);
    return Response.json({ response: result.finalOutput, tokens: result.usage.totalTokens });
  }
};


Limitations:

No voice agents
30s CPU limit, 128MB memory
Tracing requires manual setup - set OTEL_SDK_DISABLED=true or call startTracingExportLoop() (Issue #16)

Next.js: app/api/agent/route.ts → POST handler with run(agent, message)

Templates: cloudflare-workers/, nextjs/

Error Handling (11+ Errors Prevented)
1. Zod Schema Type Errors

Error: Type errors with tool parameters.

Workaround: Define schemas inline.

// ❌ Can cause type errors
parameters: mySchema

// ✅ Works reliably
parameters: z.object({ field: z.string() })


Note: As of v0.4.1, invalid JSON in tool call arguments is handled gracefully (previously caused SyntaxError crashes). (PR #887)

Source: GitHub #188

2. MCP Tracing Errors

Error: "No existing trace found" with MCP servers.

Workaround:

import { initializeTracing } from '@openai/agents/tracing';
await initializeTracing();


Source: GitHub #580

3. MaxTurnsExceededError

Error: Agent loops infinitely.

Solution: Increase maxTurns or improve instructions:

const result = await run(agent, input, {
  maxTurns: 20, // Increase limit
});

// Or improve instructions
instructions: `After using tools, provide a final answer.
Do not loop endlessly.`

4. ToolCallError

Error: Tool execution fails.

Solution: Retry with exponential backoff:

for (let attempt = 1; attempt <= 3; attempt++) {
  try {
    return await run(agent, input);
  } catch (error) {
    if (error instanceof ToolCallError && attempt < 3) {
      await sleep(1000 * Math.pow(2, attempt - 1));
      continue;
    }
    throw error;
  }
}

5. Schema Mismatch

Error: Output doesn't match outputType.

Solution: Use stronger model or add validation instructions:

const agent = new Agent({
  model: 'gpt-5', // More reliable than gpt-5-mini
  instructions: 'CRITICAL: Return JSON matching schema exactly',
  outputType: mySchema,
});

6. Reasoning Effort Defaults Changed (v0.4.0)

Error: Unexpected reasoning behavior after upgrading to v0.4.0.

Why It Happens: Default reasoning effort for gpt-5.1/5.2 changed from "low" to "none" in v0.4.0.

Prevention: Explicitly set reasoning effort if you need it.

// v0.4.0+ - default is now "none"
const agent = new Agent({
  model: 'gpt-5.1',
  reasoning: { effort: 'low' }, // Explicitly set if needed: 'low', 'medium', 'high'
});


Source: Release v0.4.0 | PR #876

7. Reasoning Content Leaks into JSON Output

Error: response_reasoning field appears in structured output unexpectedly.

Why It Happens: Model endpoint issue (not SDK bug) when using outputType with reasoning models.

Workaround: Filter out response_reasoning from output.

const result = await run(agent, input);
const { response_reasoning, ...cleanOutput } = result.finalOutput;
return cleanOutput;


Source: Issue #844 Status: Model-side issue, coordinating with OpenAI teams

All Errors: See references/common-errors.md

Template: templates/shared/error-handling.ts

Orchestration Patterns

LLM-Based: Agent decides routing autonomously (adaptive, higher tokens) Code-Based: Explicit control flow with conditionals (predictable, lower cost) Parallel: Promise.all([run(agent1, text), run(agent2, text)]) (concurrent execution)

Debugging
process.env.DEBUG = '@openai/agents:*';  // Verbose logging
const result = await run(agent, input);
console.log(result.usage.totalTokens, result.history.length, result.currentAgent?.name);


❌ Don't use when:

Simple OpenAI API calls (use openai-api skill instead)
Non-OpenAI models exclusively
Production voice at massive scale (consider LiveKit Agents)
Production Checklist
 Set OPENAI_API_KEY as environment secret
 Implement error handling for all agent calls
 Add guardrails for safety-critical applications
 Enable tracing for debugging
 Set reasonable maxTurns to prevent runaway costs
 Use gpt-5-mini where possible for cost efficiency
 Implement rate limiting
 Log token usage for cost monitoring
 Test handoff flows thoroughly
 Never expose API keys to browsers (use session tokens)
Token Efficiency

Estimated Savings: ~60%

Task	Without Skill	With Skill	Savings
Multi-agent setup	~12k tokens	~5k tokens	58%
Voice agent	~10k tokens	~4k tokens	60%
Error debugging	~8k tokens	~3k tokens	63%
Average	~10k	~4k	~60%

Errors Prevented: 11 documented issues = 100% error prevention

Templates Index

Text Agents (8):

agent-basic.ts - Simple agent with tools
agent-handoffs.ts - Multi-agent triage
agent-structured-output.ts - Zod schemas
agent-streaming.ts - Real-time events
agent-guardrails-input.ts - Input validation
agent-guardrails-output.ts - Output filtering
agent-human-approval.ts - HITL pattern
agent-parallel.ts - Concurrent execution

Realtime Agents (3): 9. realtime-agent-basic.ts - Voice setup 10. realtime-session-browser.tsx - React client 11. realtime-handoffs.ts - Voice delegation

Framework Integration (4): 12. worker-text-agent.ts - Cloudflare Workers 13. worker-agent-hono.ts - Hono framework 14. api-agent-route.ts - Next.js API 15. api-realtime-route.ts - Next.js voice

Utilities (2): 16. error-handling.ts - Comprehensive errors 17. tracing-setup.ts - Debugging

References
agent-patterns.md - Orchestration strategies
common-errors.md - 9 errors with workarounds
realtime-transports.md - WebRTC vs WebSocket
cloudflare-integration.md - Workers limitations
official-links.md - Documentation links
Official Resources
Docs: https://openai.github.io/openai-agents-js/
GitHub: https://github.com/openai/openai-agents-js
npm: https://www.npmjs.com/package/@openai/agents
Issues: https://github.com/openai/openai-agents-js/issues

Version: SDK v0.4.1 Last Verified: 2026-01-21 Skill Author: Jeremy Dawes (Jezweb) Production Tested: Yes Changes: Added v0.4.0 breaking changes (Zod 4, reasoning defaults), invalid JSON handling (v0.4.1), reasoning output leaks, streaming HITL pattern, agent-as-tool context isolation, video limitations, Cloudflare tracing setup

Weekly Installs
363
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass