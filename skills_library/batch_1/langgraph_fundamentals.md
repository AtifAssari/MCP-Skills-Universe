---
title: langgraph-fundamentals
url: https://skills.sh/langchain-ai/langchain-skills/langgraph-fundamentals
---

# langgraph-fundamentals

skills/langchain-ai/langchain-skills/langgraph-fundamentals
langgraph-fundamentals
Installation
$ npx skills add https://github.com/langchain-ai/langchain-skills --skill langgraph-fundamentals
Summary

Directed graph framework for building stateful, multi-step agent workflows with fine-grained control.

StateGraph with typed state schemas, reducers for accumulating lists/values, and nodes that return partial state updates
Static edges for fixed flow, conditional edges for branching, and Command for combining state updates with dynamic routing
Send API for fan-out parallelism to worker nodes with result aggregation via reducers
Invoke for single execution and stream modes (values, updates, messages, custom) for real-time monitoring and token streaming
RetryPolicy for transient errors and ToolNode with error handling for LLM-recoverable failures; human-in-the-loop via interrupt for user input
SKILL.md
StateGraph: Main class for building stateful graphs
Nodes: Functions that perform work and update state
Edges: Define execution order (static or conditional)
START/END: Special nodes marking entry and exit points
State with Reducers: Control how state updates are merged

Graphs must be compile()d before execution.

Designing a LangGraph application

Follow these 5 steps when building a new graph:

Map out discrete steps — sketch a flowchart of your workflow. Each step becomes a node.
Identify what each step does — categorize nodes: LLM step, data step, action step, or user input step. For each, determine static context (prompt), dynamic context (from state), retry strategy, and desired outcome.
Design your state — state is shared memory for all nodes. Store raw data, format prompts on-demand inside nodes.
Build your nodes — implement each step as a function that takes state and returns partial updates.
Wire it together — connect nodes with edges, add conditional routing, compile with a checkpointer if needed.
Use LangGraph When	Use Alternatives When
Need fine-grained control over agent orchestration	Quick prototyping → LangChain agents
Building complex workflows with branching/loops	Simple stateless workflows → LangChain direct
Require human-in-the-loop, persistence	Batteries-included features → Deep Agents
State Management
Need	Solution	Example
Overwrite value	No reducer (default)	Simple fields like counters
Append to list	Reducer (operator.add / concat)	Message history, logs
Custom logic	Custom reducer function	Complex merging

class State(TypedDict): name: str # Default: overwrites on update messages: Annotated[list, operator.add] # Appends to list total: Annotated[int, operator.add] # Sums integers

</python>
<typescript>
Use StateSchema with ReducedValue for accumulating arrays.
```typescript
import { StateSchema, ReducedValue, MessagesValue } from "@langchain/langgraph";
import { z } from "zod";

const State = new StateSchema({
  name: z.string(),  // Default: overwrites
  messages: MessagesValue,  // Built-in for messages
  items: new ReducedValue(
    z.array(z.string()).default(() => []),
    { reducer: (current, update) => current.concat(update) }
  ),
});

Node 1 returns: {"messages": ["A"]}
Node 2 returns: {"messages": ["B"]}
Final: {"messages": ["B"]} # "A" is LOST!
CORRECT: Use Annotated with operator.add

from typing import Annotated import operator

class State(TypedDict): messages: Annotated[list, operator.add]

Final: {"messages": ["A", "B"]}
</python>
<typescript>
Without ReducedValue, arrays are overwritten not appended.
```typescript
// WRONG: Array will be overwritten
const State = new StateSchema({
  items: z.array(z.string()),  // No reducer!
});
// Node 1: { items: ["A"] }, Node 2: { items: ["B"] }
// Final: { items: ["B"] }  // A is lost!

// CORRECT: Use ReducedValue
const State = new StateSchema({
  items: new ReducedValue(
    z.array(z.string()).default(() => []),
    { reducer: (current, update) => current.concat(update) }
  ),
});
// Final: { items: ["A", "B"] }

CORRECT: Return dict with only the updates

def my_node(state: State) -> dict: return {"field": "updated"}

</python>
<typescript>
Return partial updates only, not the full state object.
```typescript
// WRONG: Returning entire state
const myNode = async (state: typeof State.State) => {
  state.field = "updated";
  return state;  // Don't do this!
};

// CORRECT: Return partial updates
const myNode = async (state: typeof State.State) => {
  return { field: "updated" };
};

Nodes

Node functions accept these arguments:

Signature	When to Use
def node(state: State)	Simple nodes that only need state
def node(state: State, config: RunnableConfig)	Need thread_id, tags, or configurable values
def node(state: State, runtime: Runtime[Context])	Need runtime context, store, or stream_writer
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime

def plain_node(state: State):
    return {"results": "done"}

def node_with_config(state: State, config: RunnableConfig):
    thread_id = config["configurable"]["thread_id"]
    return {"results": f"Thread: {thread_id}"}

def node_with_runtime(state: State, runtime: Runtime[Context]):
    user_id = runtime.context.user_id
    return {"results": f"User: {user_id}"}

Signature	When to Use
(state) => {...}	Simple nodes that only need state
(state, config) => {...}	Need thread_id, tags, or configurable values
import { GraphNode, StateSchema } from "@langchain/langgraph";

const plainNode: GraphNode<typeof State> = (state) => {
  return { results: "done" };
};

const nodeWithConfig: GraphNode<typeof State> = (state, config) => {
  const threadId = config?.configurable?.thread_id;
  return { results: `Thread: ${threadId}` };
};

Edges
Need	Edge Type	When to Use
Always go to same node	add_edge()	Fixed, deterministic flow
Route based on state	add_conditional_edges()	Dynamic branching
Update state AND route	Command	Combine logic in single node
Fan-out to multiple nodes	Send	Parallel processing with dynamic inputs

class State(TypedDict): input: str output: str

def process_input(state: State) -> dict: return {"output": f"Processed: {state['input']}"}

def finalize(state: State) -> dict: return {"output": state["output"].upper()}

graph = ( StateGraph(State) .add_node("process", process_input) .add_node("finalize", finalize) .add_edge(START, "process") .add_edge("process", "finalize") .add_edge("finalize", END) .compile() )

result = graph.invoke({"input": "hello"}) print(result["output"]) # "PROCESSED: HELLO"

</python>
<typescript>
Chain nodes with addEdge and compile before invoking.
```typescript
import { StateGraph, StateSchema, START, END } from "@langchain/langgraph";
import { z } from "zod";

const State = new StateSchema({
  input: z.string(),
  output: z.string().default(""),
});

const processInput = async (state: typeof State.State) => {
  return { output: `Processed: ${state.input}` };
};

const finalize = async (state: typeof State.State) => {
  return { output: state.output.toUpperCase() };
};

const graph = new StateGraph(State)
  .addNode("process", processInput)
  .addNode("finalize", finalize)
  .addEdge(START, "process")
  .addEdge("process", "finalize")
  .addEdge("finalize", END)
  .compile();

const result = await graph.invoke({ input: "hello" });
console.log(result.output);  // "PROCESSED: HELLO"


class State(TypedDict): query: str route: str result: str

def classify(state: State) -> dict: if "weather" in state["query"].lower(): return {"route": "weather"} return {"route": "general"}

def route_query(state: State) -> Literal["weather", "general"]: return state["route"]

graph = ( StateGraph(State) .add_node("classify", classify) .add_node("weather", lambda s: {"result": "Sunny, 72F"}) .add_node("general", lambda s: {"result": "General response"}) .add_edge(START, "classify") .add_conditional_edges("classify", route_query, ["weather", "general"]) .add_edge("weather", END) .add_edge("general", END) .compile() )

</python>
<typescript>
addConditionalEdges routes based on function return value.
```typescript
import { StateGraph, StateSchema, START, END } from "@langchain/langgraph";
import { z } from "zod";

const State = new StateSchema({
  query: z.string(),
  route: z.string().default(""),
  result: z.string().default(""),
});

const classify = async (state: typeof State.State) => {
  if (state.query.toLowerCase().includes("weather")) {
    return { route: "weather" };
  }
  return { route: "general" };
};

const routeQuery = (state: typeof State.State) => state.route;

const graph = new StateGraph(State)
  .addNode("classify", classify)
  .addNode("weather", async () => ({ result: "Sunny, 72F" }))
  .addNode("general", async () => ({ result: "General response" }))
  .addEdge(START, "classify")
  .addConditionalEdges("classify", routeQuery, ["weather", "general"])
  .addEdge("weather", END)
  .addEdge("general", END)
  .compile();

Command

Command combines state updates and routing in a single return value. Fields:

update: State updates to apply (like returning a dict from a node)
goto: Node name(s) to navigate to next
resume: Value to resume after interrupt() — see human-in-the-loop skill

class State(TypedDict): count: int result: str

def node_a(state: State) -> Command[Literal["node_b", "node_c"]]: """Update state AND decide next node in one return.""" new_count = state["count"] + 1 if new_count > 5: return Command(update={"count": new_count}, goto="node_c") return Command(update={"count": new_count}, goto="node_b")

graph = ( StateGraph(State) .add_node("node_a", node_a) .add_node("node_b", lambda s: {"result": "B"}) .add_node("node_c", lambda s: {"result": "C"}) .add_edge(START, "node_a") .add_edge("node_b", END) .add_edge("node_c", END) .compile() )

</python>
<typescript>
Return Command with update and goto to combine state change with routing.
```typescript
import { StateGraph, StateSchema, START, END, Command } from "@langchain/langgraph";
import { z } from "zod";

const State = new StateSchema({
  count: z.number().default(0),
  result: z.string().default(""),
});

const nodeA = async (state: typeof State.State) => {
  const newCount = state.count + 1;
  if (newCount > 5) {
    return new Command({ update: { count: newCount }, goto: "node_c" });
  }
  return new Command({ update: { count: newCount }, goto: "node_b" });
};

const graph = new StateGraph(State)
  .addNode("node_a", nodeA, { ends: ["node_b", "node_c"] })
  .addNode("node_b", async () => ({ result: "B" }))
  .addNode("node_c", async () => ({ result: "C" }))
  .addEdge(START, "node_a")
  .addEdge("node_b", END)
  .addEdge("node_c", END)
  .compile();


Python: Use Command[Literal["node_a", "node_b"]] as the return type annotation to declare valid goto destinations.

TypeScript: Pass { ends: ["node_a", "node_b"] } as the third argument to addNode to declare valid goto destinations.

Warning: Command only adds dynamic edges — static edges defined with add_edge / addEdge still execute. If node_a returns Command(goto="node_c") and you also have graph.add_edge("node_a", "node_b"), both node_b and node_c will run.

Send API

Fan-out with Send: return [Send("worker", {...})] from a conditional edge to spawn parallel workers. Requires a reducer on the results field.

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

Running Graphs: Invoke and Stream

Call graph.invoke(input, config) to run a graph to completion and return the final state.

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

Error Handling

Match the error type to the right handler:

Error Type	Who Fixes	Strategy	Example
Transient (network, rate limits)	System	RetryPolicy(max_attempts=3)	add_node(..., retry_policy=...)
LLM-recoverable (tool failures)	LLM	ToolNode(tools, handle_tool_errors=True)	Error returned as ToolMessage
User-fixable (missing info)	Human	interrupt({"message": ...})	Collect missing data (see HITL skill)
Unexpected	Developer	Let bubble up	raise

workflow.add_node( "search_documentation", search_documentation, retry_policy=RetryPolicy(max_attempts=3, initial_interval=1.0) )

</python>
<typescript>
Use retryPolicy for transient errors.
```typescript
workflow.addNode(
  "searchDocumentation",
  searchDocumentation,
  {
    retryPolicy: { maxAttempts: 3, initialInterval: 1.0 },
  },
);


tool_node = ToolNode(tools, handle_tool_errors=True)

workflow.add_node("tools", tool_node)

</python>
<typescript>
Use ToolNode from @langchain/langgraph/prebuilt to handle tool execution and errors. When handleToolErrors is true, errors are returned as ToolMessages so the LLM can recover.
```typescript
import { ToolNode } from "@langchain/langgraph/prebuilt";

const toolNode = new ToolNode(tools, { handleToolErrors: true });

workflow.addNode("tools", toolNode);

Common Fixes
CORRECT

graph = builder.compile() graph.invoke({"input": "test"})

</python>
<typescript>
Must compile() to get executable graph.
```typescript
// WRONG
await builder.invoke({ input: "test" });

// CORRECT
const graph = builder.compile();
await graph.invoke({ input: "test" });

CORRECT

def should_continue(state): return END if state["count"] > 10 else "node_b" builder.add_conditional_edges("node_a", should_continue)

</python>
<typescript>
Use conditional edges with END return to break loops.
```typescript
// WRONG: Loops forever
builder.addEdge("node_a", "node_b").addEdge("node_b", "node_a");

// CORRECT
builder.addConditionalEdges("node_a", (state) => state.count > 10 ? END : "node_b");

Command return type needs Literal for routing destinations (Python)

def node_a(state) -> Command[Literal["node_b", "node_c"]]: return Command(goto="node_b")

START is entry-only - cannot route back to it

builder.add_edge("node_a", START) # WRONG! builder.add_edge("node_a", "entry") # Use a named entry node instead

Reducer expects matching types

return {"items": ["item"]} # List for list reducer, not a string

```typescript
// Always await graph.invoke() - it returns a Promise
const result = await graph.invoke({ input: "test" });

// TS Command nodes need { ends } to declare routing destinations
builder.addNode("router", routerFn, { ends: ["node_b", "node_c"] });

Mutate state directly — always return partial update dicts from nodes
Route back to START — it's entry-only; use a named node instead
Forget reducers on list fields — without one, last write wins
Mix static edges with Command goto without understanding both will execute
Weekly Installs
6.3K
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