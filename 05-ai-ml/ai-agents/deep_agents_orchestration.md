---
rating: ⭐⭐⭐⭐⭐
title: deep-agents-orchestration
url: https://skills.sh/langchain-ai/langchain-skills/deep-agents-orchestration
---

# deep-agents-orchestration

skills/langchain-ai/langchain-skills/deep-agents-orchestration
deep-agents-orchestration
Installation
$ npx skills add https://github.com/langchain-ai/langchain-skills --skill deep-agents-orchestration
Summary

Orchestrate subagents, plan multi-step tasks, and require human approval for sensitive operations.

Delegate work to specialized subagents via the task tool; custom subagents support isolated tool sets and system prompts, while the default "general-purpose" subagent inherits main agent configuration
Plan and track complex workflows with write_todos, organizing tasks across pending, in-progress, and completed states; requires a thread_id for persistence across invocations
Implement human-in-the-loop approval gates on specific tools with three decision types: approve, reject (with feedback), or edit (modify arguments before execution); requires a checkpointer and thread_id for resumption
All three capabilities are automatically included in create_deep_agent() and work together to support task delegation, planning, and compliance workflows
SKILL.md
SubAgentMiddleware: Delegate work via task tool to specialized agents
TodoListMiddleware: Plan and track tasks via write_todos tool
HumanInTheLoopMiddleware: Require approval before sensitive operations

All three are automatically included in create_deep_agent().

Subagents (Task Delegation)
Use Subagents When	Use Main Agent When
Task needs specialized tools	General-purpose tools sufficient
Want to isolate complex work	Single-step operation
Need clean context for main agent	Context bloat acceptable

Default subagent: "general-purpose" - automatically available with same tools/config as main agent.

@tool def search_papers(query: str) -> str: """Search academic papers.""" return f"Found 10 papers about {query}"

agent = create_deep_agent( subagents=[ { "name": "researcher", "description": "Conduct web research and compile findings", "system_prompt": "Search thoroughly, return concise summary", "tools": [search_papers], } ] )

Main agent delegates: task(agent="researcher", instruction="Research AI trends")
</python>
<typescript>
Create a custom "researcher" subagent with specialized tools for academic paper search.
```typescript
import { createDeepAgent } from "deepagents";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const searchPapers = tool(
  async ({ query }) => `Found 10 papers about ${query}`,
  { name: "search_papers", description: "Search papers", schema: z.object({ query: z.string() }) }
);

const agent = await createDeepAgent({
  subagents: [
    {
      name: "researcher",
      description: "Conduct web research and compile findings",
      systemPrompt: "Search thoroughly, return concise summary",
      tools: [searchPapers],
    }
  ]
});

// Main agent delegates: task(agent="researcher", instruction="Research AI trends")


agent = create_deep_agent( subagents=[ { "name": "code-deployer", "description": "Deploy code to production", "system_prompt": "You deploy code after tests pass.", "tools": [run_tests, deploy_to_prod], "interrupt_on": {"deploy_to_prod": True}, # Require approval } ], checkpointer=MemorySaver() # Required for interrupts )

</python>
</ex-subagent-with-hitl>

<fix-subagents-are-stateless>
<python>
Subagents are stateless - provide complete instructions in a single call.
```python
# WRONG: Subagents don't remember previous calls
# task(agent='research', instruction='Find data')
# task(agent='research', instruction='What did you find?')  # Starts fresh!

# CORRECT: Complete instructions upfront
# task(agent='research', instruction='Find data on AI, save to /research/, return summary')


// CORRECT: Complete instructions upfront // task research: Find data on AI, save to /research/, return summary

</typescript>
</fix-subagents-are-stateless>

<fix-custom-subagents-dont-inherit-skills>
<python>
Custom subagents don't inherit skills from the main agent.
```python
# WRONG: Custom subagent won't have main agent's skills
agent = create_deep_agent(
    skills=["/main-skills/"],
    subagents=[{"name": "helper", ...}]  # No skills inherited
)

# CORRECT: Provide skills explicitly (general-purpose subagent DOES inherit)
agent = create_deep_agent(
    skills=["/main-skills/"],
    subagents=[{"name": "helper", "skills": ["/helper-skills/"], ...}]
)

TodoList (Task Planning)
Use TodoList When	Skip TodoList When
Complex multi-step tasks	Simple single-action tasks
Long-running operations	Quick operations (< 3 steps)

Each todo item has:

content: Description of the task
status: One of "pending", "in_progress", "completed"

agent = create_deep_agent() # TodoListMiddleware included by default

result = agent.invoke({ "messages": [{"role": "user", "content": "Create a REST API: design models, implement CRUD, add auth, write tests"}] }, config={"configurable": {"thread_id": "session-1"}})

Agent's planning via write_todos:
[
{"content": "Design data models", "status": "in_progress"},
{"content": "Implement CRUD endpoints", "status": "pending"},
{"content": "Add authentication", "status": "pending"},
{"content": "Write tests", "status": "pending"}
]
</python>
<typescript>
Invoke an agent that automatically creates a todo list for a multi-step task.
```typescript
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent();  // TodoListMiddleware included

const result = await agent.invoke({
  messages: [{ role: "user", content: "Create a REST API: design models, implement CRUD, add auth, write tests" }]
}, { configurable: { thread_id: "session-1" } });

Access todo list from final state

todos = result.get("todos", []) for todo in todos: print(f"[{todo['status']}] {todo['content']}")

</python>
</ex-access-todo-state>

<fix-todolist-requires-thread-id>
<python>
Todo list state requires a thread_id for persistence across invocations.
```python
# WRONG: Fresh state each time without thread_id
agent.invoke({"messages": [...]})

# CORRECT: Use thread_id
config = {"configurable": {"thread_id": "user-session"}}
agent.invoke({"messages": [...]}, config=config)  # Todos preserved

Human-in-the-Loop (Approval Workflows)
Use HITL When	Skip HITL When
High-stakes operations (DB writes, deployments)	Read-only operations
Compliance requires human oversight	Fully automated workflows

agent = create_deep_agent( interrupt_on={ "write_file": True, # All decisions allowed "execute_sql": {"allowed_decisions": ["approve", "reject"]}, "read_file": False, # No interrupts }, checkpointer=MemorySaver() # REQUIRED for interrupts )

</python>
<typescript>
Configure which tools require human approval before execution.
```typescript
import { createDeepAgent } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const agent = await createDeepAgent({
  interruptOn: {
    write_file: true,
    execute_sql: { allowedDecisions: ["approve", "reject"] },
    read_file: false,
  },
  checkpointer: new MemorySaver()  // REQUIRED
});


agent = create_deep_agent( interrupt_on={"write_file": True}, checkpointer=MemorySaver() )

config = {"configurable": {"thread_id": "session-1"}}

Step 1: Agent proposes write_file - execution pauses

result = agent.invoke({ "messages": [{"role": "user", "content": "Write config to /prod.yaml"}] }, config=config)

Step 2: Check for interrupts

state = agent.get_state(config) if state.next: print(f"Pending action")

Step 3: Approve and resume

result = agent.invoke(Command(resume={"decisions": [{"type": "approve"}]}), config=config)

</python>
<typescript>
Complete workflow: trigger an interrupt, check state, approve action, and resume execution.
```typescript
import { createDeepAgent } from "deepagents";
import { MemorySaver, Command } from "@langchain/langgraph";

const agent = await createDeepAgent({
  interruptOn: { write_file: true },
  checkpointer: new MemorySaver()
});

const config = { configurable: { thread_id: "session-1" } };

// Step 1: Agent proposes write_file - execution pauses
let result = await agent.invoke({
  messages: [{ role: "user", content: "Write config to /prod.yaml" }]
}, config);

// Step 2: Check for interrupts
const state = await agent.getState(config);
if (state.next) {
  console.log("Pending action");
}

// Step 3: Approve and resume
result = await agent.invoke(
  new Command({ resume: { decisions: [{ type: "approve" }] } }), config
);

Subagent names, tools, models, system prompts
Which tools require approval
Allowed decision types per tool
TodoList content and structure
What Agents CANNOT Configure
Tool names (task, write_todos)
HITL protocol (approve/edit/reject structure)
Skip checkpointer requirement for interrupts
Make subagents stateful (they're ephemeral)
CORRECT

agent = create_deep_agent(interrupt_on={"write_file": True}, checkpointer=MemorySaver())

</python>
<typescript>
Checkpointer is required when using interruptOn for HITL workflows.
```typescript
// WRONG
const agent = await createDeepAgent({ interruptOn: { write_file: true } });

// CORRECT
const agent = await createDeepAgent({ interruptOn: { write_file: true }, checkpointer: new MemorySaver() });

CORRECT

config = {"configurable": {"thread_id": "session-1"}} agent.invoke({...}, config=config)

Resume with Command using same config

agent.invoke(Command(resume={"decisions": [{"type": "approve"}]}), config=config)

</python>
<typescript>
A consistent thread_id is required to resume interrupted workflows.
```typescript
// WRONG: Can't resume without thread_id
await agent.invoke({ messages: [...] });

// CORRECT
const config = { configurable: { thread_id: "session-1" } };
await agent.invoke({ messages: [...] }, config);
// Resume with Command using same config
await agent.invoke(new Command({ resume: { decisions: [{ type: "approve" }] } }), config);

Weekly Installs
5.6K
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