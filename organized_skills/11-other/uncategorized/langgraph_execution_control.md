---
rating: ⭐⭐⭐⭐⭐
title: langgraph execution control
url: https://skills.sh/langchain-ai/langchain-skills/langgraph-execution-control
---

# langgraph execution control

skills/langchain-ai/langchain-skills/LangGraph Execution Control
LangGraph Execution Control
Installation
$ npx skills add https://github.com/langchain-ai/langchain-skills --skill 'LangGraph Execution Control'
SKILL.md
Workflows vs Agents: Predetermined paths vs dynamic decision-making
Send API: Fan-out to parallel workers (map-reduce)
Interrupts: Pause for human input, resume with Command
Streaming: Real-time state, tokens, and custom data
Characteristic	Workflow	Agent
Control Flow	Fixed, predetermined	Dynamic, model-driven
Predictability	High	Low
Use Case	Sequential tasks	Open-ended problems
Workflows and Agents

class AgentState(TypedDict): messages: Annotated[list, operator.add]

model_with_tools = model.bind_tools([search])

def agent_node(state: AgentState) -> dict: return {"messages": [model_with_tools.invoke(state["messages"])]}

def tool_node(state: AgentState) -> dict: """Execute tool calls from the last AI message.""" result = [] for tc in state["messages"][-1].tool_calls: observation = tools_by_name[tc["name"]].invoke(tc["args"]) result.append(ToolMessage(content=observation, tool_call_id=tc["id"])) return {"messages": result}

def should_continue(state: AgentState): return "tools" if state["messages"][-1].tool_calls else END

agent = ( StateGraph(AgentState) .add_node("agent", agent_node) .add_node("tools", tool_node) .add_edge(START, "agent") .add_conditional_edges("agent", should_continue) .add_edge("tools", "agent") # Loop back after tool execution .compile() )

</python>
<typescript>
ReAct agent pattern: model decides when to call tools, loop until done.
```typescript
import { StateGraph, StateSchema, MessagesValue, START, END } from "@langchain/langgraph";
import { ToolMessage } from "@langchain/core/messages";

const State = new StateSchema({ messages: MessagesValue });
const modelWithTools = model.bindTools([searchTool]);

const agentNode = async (state: typeof State.State) => ({
  messages: [await modelWithTools.invoke(state.messages)]
});

const toolNode = async (state: typeof State.State) => ({
  messages: await Promise.all(
    (state.messages.at(-1)?.tool_calls ?? []).map(async (tc) =>
      new ToolMessage({ content: await searchTool.invoke(tc.args), tool_call_id: tc.id })
    )
  )
});

const shouldContinue = (state: typeof State.State) =>
  state.messages.at(-1)?.tool_calls?.length ? "tools" : END;

const agent = new StateGraph(State)
  .addNode("agent", agentNode)
  .addNode("tools", toolNode)
  .addEdge(START, "agent")
  .addConditionalEdges("agent", shouldContinue)
  .addEdge("tools", "agent")
  .compile();


class OrchestratorState(TypedDict): tasks: list[str] results: Annotated[list, operator.add] summary: str

def orchestrator(state: OrchestratorState): """Fan out tasks to workers.""" return [Send("worker", {"task": task}) for task in state["tasks"]]

def worker(state: dict) -> dict: return {"results": [f"Completed: {state['task']}"]}

def synthesize(state: OrchestratorState) -> dict: return {"summary": f"Processed {len(state['results'])} tasks"}

graph = ( StateGraph(OrchestratorState) .add_node("worker", worker) .add_node("synthesize", synthesize) .add_conditional_edges(START, orchestrator, ["worker"]) .add_edge("worker", "synthesize") .add_edge("synthesize", END) .compile() )

result = graph.invoke({"tasks": ["Task A", "Task B", "Task C"]})

</python>
<typescript>
Fan out tasks to parallel workers using the Send API and aggregate results.
```typescript
import { Send, StateGraph, StateSchema, ReducedValue, START, END } from "@langchain/langgraph";
import { z } from "zod";

const State = new StateSchema({
  tasks: z.array(z.string()),
  results: new ReducedValue(
    z.array(z.string()).default(() => []),
    { reducer: (curr, upd) => curr.concat(upd) }
  ),
  summary: z.string().default(""),
});

const orchestrator = (state: typeof State.State) => {
  return state.tasks.map((task) => new Send("worker", { task }));
};

const worker = async (state: { task: string }) => {
  return { results: [`Completed: ${state.task}`] };
};

const synthesize = async (state: typeof State.State) => {
  return { summary: `Processed ${state.results.length} tasks` };
};

const graph = new StateGraph(State)
  .addNode("worker", worker)
  .addNode("synthesize", synthesize)
  .addConditionalEdges(START, orchestrator, ["worker"])
  .addEdge("worker", "synthesize")
  .addEdge("synthesize", END)
  .compile();

Interrupts (Human-in-the-Loop)
Type	When Set	Use Case
interrupt() (recommended)	Inside node code	Human-in-the-loop, conditional pausing. Resume with Command(resume=value)
interrupt_before	At compile time	Debugging only, not for HITL. Resume with invoke(None, config)
interrupt_after	At compile time	Debugging only, not for HITL. Resume with invoke(None, config)

def review_node(state): if state["needs_review"]: user_response = interrupt({ "action": "review", "data": state["draft"], "question": "Approve this draft?" }) if user_response == "reject": return {"status": "rejected"} return {"status": "approved"}

checkpointer = InMemorySaver()

graph = ( StateGraph(State) .add_node("review", review_node) .add_edge(START, "review") .add_edge("review", END) .compile(checkpointer=checkpointer) )

config = {"configurable": {"thread_id": "1"}} result = graph.invoke({"needs_review": True, "draft": "content"}, config)

Check for interrupt

if "interrupt" in result: print(result["interrupt"])

Resume with user decision

result = graph.invoke(Command(resume="approve"), config)

</python>
<typescript>
Pause execution for human review using dynamic interrupt and resume with Command.
```typescript
import { interrupt, Command, MemorySaver, StateGraph, START, END } from "@langchain/langgraph";

const reviewNode = async (state: typeof State.State) => {
  if (state.needsReview) {
    const userResponse = interrupt({
      action: "review",
      data: state.draft,
      question: "Approve this draft?"
    });
    if (userResponse === "reject") {
      return { status: "rejected" };
    }
  }
  return { status: "approved" };
};

const checkpointer = new MemorySaver();

const graph = new StateGraph(State)
  .addNode("review", reviewNode)
  .addEdge(START, "review")
  .addEdge("review", END)
  .compile({ checkpointer });

const config = { configurable: { thread_id: "1" } };
let result = await graph.invoke({ needsReview: true, draft: "content" }, config);

// Check for interrupt
if (result.__interrupt__) {
  console.log(result.__interrupt__);
}

// Resume with user decision
result = await graph.invoke(new Command({ resume: "approve" }), config);


config = {"configurable": {"thread_id": "1"}} graph.invoke({"data": "test"}, config) # Runs until step2 graph.invoke(None, config) # Resume

</python>
<typescript>
Set compile-time breakpoints for debugging. Not recommended for human-in-the-loop — use `interrupt()` instead.
```typescript
const graph = new StateGraph(State)
  .addNode("step1", step1)
  .addNode("step2", step2)
  .addEdge(START, "step1")
  .addEdge("step1", "step2")
  .addEdge("step2", END)
  .compile({
    checkpointer,
    interruptBefore: ["step2"],  // Pause before step2
  });

const config = { configurable: { thread_id: "1" } };
await graph.invoke({ data: "test" }, config);  // Runs until step2
await graph.invoke(null, config);  // Resume

Streaming
Mode	What it Streams	Use Case
values	Full state after each step	Monitor complete state
updates	State deltas	Track incremental updates
messages	LLM tokens + metadata	Chat UIs
custom	User-defined data	Progress indicators

def my_node(state): writer = get_stream_writer() writer("Processing step 1...") # Do work writer("Complete!") return {"result": "done"}

for chunk in graph.stream({"data": "test"}, stream_mode="custom"): print(chunk)

</python>
<typescript>
Emit custom progress updates from within nodes using the stream writer.
```typescript
import { getWriter } from "@langchain/langgraph";

const myNode = async (state: typeof State.State) => {
  const writer = getWriter();
  writer("Processing step 1...");
  // Do work
  writer("Complete!");
  return { result: "done" };
};

for await (const chunk of graph.stream({ data: "test" }, { streamMode: "custom" })) {
  console.log(chunk);
}

Choose workflow vs agent pattern
Use Send API for parallel execution
Call interrupt() anywhere in nodes
Set compile-time breakpoints
Resume with Command(resume=...)
Choose stream modes
What You CANNOT Configure
Interrupt without checkpointer
Resume without thread_id
Change Send API message-passing model
CORRECT

class State(TypedDict): results: Annotated[list, operator.add] # Accumulates

</python>
<typescript>
Use ReducedValue to accumulate parallel worker results.
```typescript
// WRONG: No reducer
const State = new StateSchema({ results: z.array(z.string()) });

// CORRECT
const State = new StateSchema({
  results: new ReducedValue(z.array(z.string()).default(() => []), { reducer: (curr, upd) => curr.concat(upd) }),
});

CORRECT

graph = builder.compile(checkpointer=InMemorySaver())

</python>
<typescript>
Checkpointer required for interrupt functionality.
```typescript
// WRONG
const graph = builder.compile();

// CORRECT
const graph = builder.compile({ checkpointer: new MemorySaver() });

CORRECT

graph.invoke(Command(resume="approve"), config)

</python>
<typescript>
Use Command to resume from an interrupt (regular object restarts graph).
```typescript
// WRONG
await graph.invoke({ resumeData: "approve" }, config);

// CORRECT
await graph.invoke(new Command({ resume: "approve" }), config);

BETTER

def should_continue(state): if state["iterations"] > 10: return END if state["messages"][-1].tool_calls: return "tools" return END

</python>
<typescript>
Add max iterations check to prevent infinite loops.
```typescript
// RISKY: Might loop forever
const shouldContinue = (state) => state.messages.at(-1)?.tool_calls?.length ? "tools" : END;

// BETTER
const shouldContinue = (state) => {
  if (state.iterations > 10) return END;
  return state.messages.at(-1)?.tool_calls?.length ? "tools" : END;
};

CORRECT

def node(state): response = model.invoke(state["messages"]) return {"messages": [response]}

</python>
</fix-messages-mode-requires-llm>

<fix-custom-mode-needs-stream-writer>
<python>
Use get_stream_writer() to emit custom data.
```python
# WRONG: print() isn't streamed
def node(state):
    print("Processing...")
    return {"data": "done"}

# CORRECT
def node(state):
    writer = get_stream_writer()
    writer("Processing...")  # Streamed!
    return {"data": "done"}

CORRECT

graph.stream({}, stream_mode=["updates", "messages"])

</python>
</fix-stream-modes-are-lists>

Weekly Installs
–
Repository
langchain-ai/la…n-skills
GitHub Stars
643
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass