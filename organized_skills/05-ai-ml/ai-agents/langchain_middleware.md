---
rating: ⭐⭐⭐⭐⭐
title: langchain-middleware
url: https://skills.sh/langchain-ai/langchain-skills/langchain-middleware
---

# langchain-middleware

skills/langchain-ai/langchain-skills/langchain-middleware
langchain-middleware
Installation
$ npx skills add https://github.com/langchain-ai/langchain-skills --skill langchain-middleware
Summary

Human-in-the-loop approval, custom middleware, and structured output patterns for LangChain agents.

HumanInTheLoopMiddleware pauses execution before dangerous tool calls, allowing humans to approve, edit arguments, or reject with feedback
Per-tool interrupt policies let you configure different approval rules based on risk level; requires a checkpointer and thread_id for state persistence
Command resume pattern continues execution after human decisions, with support for editing tool arguments before approval or providing rejection feedback
Custom middleware hooks (before_model, after_model, wrap_tool_call, before_agent, after_agent) enable error handling, logging, and retry logic across the agent lifecycle
SKILL.md
HumanInTheLoopMiddleware / humanInTheLoopMiddleware: Pause before dangerous tool calls for human approval
Custom middleware: Intercept tool calls for error handling, logging, retry logic
Command resume: Continue execution after human decisions (approve, edit, reject)

Requirements: Checkpointer + thread_id config for all HITL workflows.

Human-in-the-Loop

@tool def send_email(to: str, subject: str, body: str) -> str: """Send an email.""" return f"Email sent to {to}"

agent = create_agent( model="gpt-4.1", tools=[send_email], checkpointer=MemorySaver(), # Required for HITL middleware=[ HumanInTheLoopMiddleware( interrupt_on={ "send_email": {"allowed_decisions": ["approve", "edit", "reject"]}, } ) ], )

</python>
<typescript>
Set up an agent with HITL that pauses before sending emails for human approval.
```typescript
import { createAgent, humanInTheLoopMiddleware } from "langchain";
import { MemorySaver } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const sendEmail = tool(
  async ({ to, subject, body }) => `Email sent to ${to}`,
  {
    name: "send_email",
    description: "Send an email",
    schema: z.object({ to: z.string(), subject: z.string(), body: z.string() }),
  }
);

const agent = createAgent({
  model: "anthropic:claude-sonnet-4-5",
  tools: [sendEmail],
  checkpointer: new MemorySaver(),
  middleware: [
    humanInTheLoopMiddleware({
      interruptOn: { send_email: { allowedDecisions: ["approve", "edit", "reject"] } },
    }),
  ],
});


config = {"configurable": {"thread_id": "session-1"}}

Step 1: Agent runs until it needs to call tool

result1 = agent.invoke({ "messages": [{"role": "user", "content": "Send email to john@example.com"}] }, config=config)

Check for interrupt

if "interrupt" in result1: print(f"Waiting for approval: {result1['interrupt']}")

Step 2: Human approves

result2 = agent.invoke( Command(resume={"decisions": [{"type": "approve"}]}), config=config )

</python>
<typescript>
Run the agent, detect an interrupt, then resume execution after human approval.
```typescript
import { Command } from "@langchain/langgraph";

const config = { configurable: { thread_id: "session-1" } };

// Step 1: Agent runs until it needs to call tool
const result1 = await agent.invoke({
  messages: [{ role: "user", content: "Send email to john@example.com" }]
}, config);

// Check for interrupt
if (result1.__interrupt__) {
  console.log(`Waiting for approval: ${result1.__interrupt__}`);
}

// Step 2: Human approves
const result2 = await agent.invoke(
  new Command({ resume: { decisions: [{ type: "approve" }] } }),
  config
);

Which tools require approval (per-tool policies)
Allowed decisions per tool (approve, edit, reject)
Custom middleware hooks: before_model, after_model, wrap_tool_call, before_agent, after_agent
Tool-specific middleware (apply only to certain tools)
Custom Middleware Hooks

Six decorator hooks are available. Two patterns:

Wrap hooks (wrap_tool_call, wrap_model_call): (request, handler) — call handler(request) to proceed, or return early to short-circuit.
Before/after hooks (before_model, after_model, before_agent, after_agent): (state, runtime) — inspect or modify state. Return None or a dict of state updates.
from langchain.agents.middleware import wrap_tool_call

@wrap_tool_call
def retry_middleware(request, handler):
    for attempt in range(3):
        try:
            return handler(request)
        except Exception:
            if attempt == 2:
                raise

@wrap_tool_call
def guard_middleware(request, handler):
    if request.tool_call["name"] == "dangerous_tool":
        return "This tool is disabled"  # short-circuit
    return handler(request)

import { createMiddleware } from "langchain";

const retryMiddleware = createMiddleware({
  wrapToolCall: async (request, handler) => {
    for (let attempt = 0; attempt < 3; attempt++) {
      try { return await handler(request); }
      catch (e) { if (attempt === 2) throw e; }
    }
  },
});

from langchain.agents.middleware import before_model, after_model

@before_model
def log_calls(state, runtime):
    print(f"Calling model with {len(state['messages'])} messages")

@after_model
def check_output(state, runtime):
    print(f"Model responded")

import { createMiddleware } from "langchain";

const loggingMiddleware = createMiddleware({
  beforeModel: (state, runtime) => {
    console.log(`Calling model with ${state.messages.length} messages`);
  },
  afterModel: (state, runtime) => {
    console.log("Model responded");
  },
});

Interrupt after tool execution (must be before)
Skip checkpointer requirement for HITL
CORRECT

agent = create_agent( model="gpt-4.1", tools=[send_email], checkpointer=MemorySaver(), # Required middleware=[HumanInTheLoopMiddleware({...})] )

</python>
<typescript>
HITL requires a checkpointer to persist state.
```typescript
// WRONG: No checkpointer
const agent = createAgent({
  model: "anthropic:claude-sonnet-4-5", tools: [sendEmail],
  middleware: [humanInTheLoopMiddleware({ interruptOn: { send_email: true } })],
});

// CORRECT: Add checkpointer
const agent = createAgent({
  model: "anthropic:claude-sonnet-4-5", tools: [sendEmail],
  checkpointer: new MemorySaver(),
  middleware: [humanInTheLoopMiddleware({ interruptOn: { send_email: true } })],
});

CORRECT

agent.invoke(input, config={"configurable": {"thread_id": "user-123"}})

</python>
</fix-no-thread-id>

<fix-wrong-resume-syntax>
<python>
Use Command class to resume execution after an interrupt.
```python
# WRONG
agent.invoke({"resume": {"decisions": [...]}})

# CORRECT
from langgraph.types import Command
agent.invoke(Command(resume={"decisions": [{"type": "approve"}]}), config=config)


// CORRECT import { Command } from "@langchain/langgraph"; await agent.invoke(new Command({ resume: { decisions: [{ type: "approve" }] } }), config);

</typescript>
</fix-wrong-resume-syntax>

Weekly Installs
5.4K
Repository
langchain-ai/la…n-skills
GitHub Stars
643
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass