---
title: langgraph
url: https://skills.sh/yonatangross/orchestkit/langgraph
---

# langgraph

skills/yonatangross/orchestkit/langgraph
langgraph
Installation
$ npx skills add https://github.com/yonatangross/orchestkit --skill langgraph
SKILL.md
LangGraph Workflow Patterns

Comprehensive patterns for building production LangGraph workflows. LangGraph 1.x is LTS (Long Term Support) — the first stable major release, powering agents at Uber, LinkedIn, and Klarna. Each category has individual rule files in rules/ loaded on-demand.

LangGraph 1.2 (Q1 2026) — new in this bump:

Deferred nodes (defer=True on add_node) — the node runs only after all other upstream nodes for the current super-step have completed, which makes "aggregate once everyone else is done" patterns a one-liner instead of a custom reducer.
Pre/post model hooks on create_react_agent(...) and ToolNode — inject compression, summarization, or PII redaction without subclassing.
Node-level caching via CachePolicy(ttl=..., key_func=...) with SqliteCache and RedisCache backends (pluggable via graph.compile(cache=...)). Idempotent nodes skip recomputation on replay.
Quick Reference
Category	Rules	Impact	When to Use
State Management	4	CRITICAL	Designing workflow state schemas, accumulators, reducers
Routing & Branching	4	HIGH	Dynamic routing, retry loops, semantic routing, cross-graph
Parallel Execution	3	HIGH	Fan-out/fan-in, map-reduce, concurrent agents
Supervisor Patterns	3	HIGH	Central coordinators, round-robin, priority dispatch
Tool Calling	4	CRITICAL	Binding tools, ToolNode, dynamic selection, approvals
Checkpointing	3	HIGH	Persistence, recovery, cross-thread Store memory
Human-in-Loop	3	MEDIUM	Approval gates, feedback loops, interrupt/resume
Streaming	3	MEDIUM	Real-time updates, token streaming, custom events
Subgraphs	3	MEDIUM	Modular composition, nested graphs, state mapping
Functional API	3	MEDIUM	@entrypoint/@task decorators, migration from StateGraph
Platform	3	HIGH	Deployment, RemoteGraph, double-texting strategies

Total: 37 rules across 11 categories

State Management

State schemas determine how data flows between nodes. Wrong schemas cause silent data loss.

Rule	File	Key Pattern
TypedDict State	rules/state-typeddict.md	TypedDict + Annotated[list, add] for accumulators
Pydantic Validation	rules/state-pydantic.md	BaseModel at boundaries, TypedDict internally
MessagesState	rules/state-messages.md	MessagesState or add_messages reducer
Custom Reducers	rules/state-reducers.md	Annotated[T, reducer_fn] for merge/overwrite
Routing & Branching

Control flow between nodes. Always include END fallback to prevent hangs.

Rule	File	Key Pattern
Conditional Edges	rules/routing-conditional.md	add_conditional_edges with explicit mapping
Retry Loops	rules/routing-retry-loops.md	Loop-back edges with max retry counter
Semantic Routing	rules/routing-semantic.md	Embedding similarity or Command API routing
Cross-Graph Navigation	rules/routing-cross-graph.md	Command(graph=Command.PARENT) for parent/sibling routing
Parallel Execution

Run independent nodes concurrently. Use Annotated[list, add] to accumulate results.

Rule	File	Key Pattern
Fan-Out/Fan-In	rules/parallel-fanout-fanin.md	Send API for dynamic parallel branches
Map-Reduce	rules/parallel-map-reduce.md	asyncio.gather + result aggregation
Error Isolation	rules/parallel-error-isolation.md	return_exceptions=True + per-branch timeout
Supervisor Patterns

Central coordinator routes to specialized workers. Workers return to supervisor.

Rule	File	Key Pattern
Basic Supervisor	rules/supervisor-basic.md	Command API for state update + routing
Priority Routing	rules/supervisor-priority.md	Priority dict ordering agent execution
Round-Robin	rules/supervisor-round-robin.md	Completion tracking with agents_completed
Tool Calling

Integrate function calling into LangGraph agents. Keep tools under 10 per agent.

Rule	File	Key Pattern
Tool Binding	rules/tools-bind.md	model.bind_tools(tools) + tool_choice
ToolNode Execution	rules/tools-toolnode.md	ToolNode(tools) prebuilt parallel executor
Dynamic Selection	rules/tools-dynamic.md	Embedding-based tool relevance filtering
Tool Interrupts	rules/tools-interrupts.md	interrupt() for approval gates on tools
Checkpointing

Persist workflow state for recovery and debugging.

Rule	File	Key Pattern
Checkpointer Setup	rules/checkpoints-setup.md	MemorySaver dev / PostgresSaver prod
State Recovery	rules/checkpoints-recovery.md	thread_id resume + get_state_history
Cross-Thread Store	rules/checkpoints-store.md	Store for long-term memory across threads
Node-Level Caching (1.2+)

Independent of checkpointing. Cache individual node output so re-runs with identical inputs skip execution entirely.

from langgraph.graph import StateGraph
from langgraph.cache import CachePolicy, SqliteCache

graph = StateGraph(State)
graph.add_node(
    "expensive_fetch",
    fetch_fn,
    cache_policy=CachePolicy(ttl=3600, key_func=lambda s: s["query"]),
)
# RedisCache(url=...) for distributed workers
compiled = graph.compile(cache=SqliteCache("cache.db"))


Use when a node is idempotent and expensive (embeddings, external APIs). Do not use for nodes whose output depends on wall-clock time or mutable external state unless key_func captures that variance.

Deferred Nodes & Model Hooks (1.2+)
# defer=True — node waits for every other upstream node at this super-step
graph.add_node("aggregate", aggregate_fn, defer=True)

# Pre/post model hooks — no subclassing required
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model=model,
    tools=tools,
    pre_model_hook=compress_history,   # e.g. summarize if > N tokens
    post_model_hook=redact_pii,        # e.g. scrub emails/SSNs before persist
)

Human-in-Loop

Pause workflows for human intervention. Requires checkpointer for state persistence.

Rule	File	Key Pattern
Interrupt/Resume	rules/human-in-loop-interrupt.md	interrupt() function + Command(resume=)
Approval Gate	rules/human-in-loop-approval.md	interrupt_before + state update + resume
Feedback Loop	rules/human-in-loop-feedback.md	Iterative interrupt until approved
Streaming

Real-time updates and progress tracking for workflows. LangGraph 1.1 introduces version="v2" — an opt-in streaming format with full type safety on stream(), astream(), invoke(), and ainvoke().

Rule	File	Key Pattern
Stream Modes	rules/streaming-modes.md	5 modes: values, updates, messages, custom, debug
Token Streaming	rules/streaming-tokens.md	messages mode with node/tag filtering
Custom Events	rules/streaming-custom-events.md	get_stream_writer() for progress events
Streaming v2	rules/streaming-v2-format.md	version="v2" for typed streaming (LG 1.1+)
Subgraphs

Compose modular, reusable workflow components with nested graphs.

Rule	File	Key Pattern
Invoke from Node	rules/subgraphs-invoke.md	Different schemas, explicit state mapping
Add as Node	rules/subgraphs-add-as-node.md	Shared state, add_node(name, compiled_graph)
State Mapping	rules/subgraphs-state-mapping.md	Boundary transforms between parent/child
Functional API

Build workflows using @entrypoint and @task decorators instead of explicit graph construction.

Rule	File	Key Pattern
@entrypoint	rules/functional-entrypoint.md	Workflow entry point with optional checkpointer
@task	rules/functional-task.md	Returns futures, .result() to block
Migration	rules/functional-migration.md	StateGraph to Functional API conversion
Platform

Deploy graphs as managed APIs with persistence, streaming, and multi-tenancy.

Rule	File	Key Pattern
Deployment	rules/platform-deployment.md	langgraph.json + CLI + Assistants API
RemoteGraph	rules/platform-remote-graph.md	RemoteGraph for calling deployed graphs
Double Texting	rules/platform-double-texting.md	4 strategies: reject, rollback, enqueue, interrupt
Quick Start Example
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from typing import TypedDict, Annotated, Literal
from operator import add

class State(TypedDict):
    input: str
    results: Annotated[list[str], add]

def supervisor(state) -> Command[Literal["worker", END]]:
    if not state.get("results"):
        return Command(update={"input": state["input"]}, goto="worker")
    return Command(goto=END)

def worker(state) -> dict:
    return {"results": [f"Processed: {state['input']}"]}

graph = StateGraph(State)
graph.add_node("supervisor", supervisor)
graph.add_node("worker", worker)
graph.add_edge(START, "supervisor")
graph.add_edge("worker", "supervisor")
app = graph.compile()

2026 Key Patterns
Streaming v2 (LG 1.1): Use version="v2" for type-safe streaming — fully typed stream() and astream() returns. Default remains "v1" for backwards compat.
Command API: Use Command(update=..., goto=...) when updating state AND routing together
context_schema: Pass runtime config (temperature, provider) without polluting state
CachePolicy: Cache expensive node results with TTL via InMemoryCache
RemainingSteps: Proactively handle recursion limits
Store: Cross-thread memory separate from Checkpointer (thread-scoped)
interrupt(): Dynamic interrupts inside node logic (replaces interrupt_before for conditional cases)
add_edge(START, node): Not set_entry_point() (deprecated)
LTS release: LangGraph 1.x is LTS — will remain ACTIVE until v2.0
Key Decisions
Decision	Recommendation
State type	TypedDict internally, Pydantic at boundaries
Entry point	add_edge(START, node) not set_entry_point()
Routing + state update	Command API
Routing only	Conditional edges
Accumulators	Annotated[list[T], add] always
Dev checkpointer	MemorySaver
Prod checkpointer	PostgresSaver
Short-term memory	Checkpointer (thread-scoped)
Long-term memory	Store (cross-thread, namespaced)
Max parallel branches	5-10 concurrent
Tools per agent	5-10 max (dynamic selection for more)
Approval gates	interrupt() for high-risk operations
Stream modes	["updates", "custom"] for most UIs
Subgraph pattern	Invoke for isolation, Add-as-Node for shared state
Functional vs Graph	Functional for simple flows, Graph for complex topology
Common Mistakes
Forgetting add reducer (overwrites instead of accumulates)
Mutating state in place (breaks checkpointing)
No END fallback in routing (workflow hangs)
Infinite retry loops (no max counter)
Side effects in router functions
Too many tools per agent (context overflow)
Raising exceptions in tools (crashes agent loop)
No checkpointer in production (lose progress on crash)
Wrapping interrupt() in try/except (breaks the mechanism)
Not transforming state at subgraph boundaries
Forgetting .result() on Functional API tasks
Using set_entry_point() (deprecated, use add_edge(START, ...))
Evaluations

See test-cases.json for consolidated test cases across all categories.

Related Skills
ork:agent-orchestration - Higher-level multi-agent coordination, ReAct loop patterns, and framework comparisons
temporal-io - Durable execution alternative
ork:llm-integration - General LLM function calling
type-safety-validation - Pydantic model patterns
Weekly Installs
133
Repository
yonatangross/orchestkit
GitHub Stars
163
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn