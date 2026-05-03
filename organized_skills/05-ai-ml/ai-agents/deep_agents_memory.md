---
rating: ⭐⭐⭐⭐⭐
title: deep-agents-memory
url: https://skills.sh/langchain-ai/langchain-skills/deep-agents-memory
---

# deep-agents-memory

skills/langchain-ai/langchain-skills/deep-agents-memory
deep-agents-memory
Installation
$ npx skills add https://github.com/langchain-ai/langchain-skills --skill deep-agents-memory
Summary

Pluggable memory and file backends for Deep Agents with ephemeral, persistent, and hybrid routing options.

Four backend types: StateBackend (thread-scoped, ephemeral), StoreBackend (cross-session persistent), FilesystemBackend (real disk access for local dev), and CompositeBackend (route different paths to different backends)
FilesystemMiddleware provides six file operation tools: ls, read_file, write_file, edit_file, glob, grep
CompositeBackend uses longest-prefix matching to route paths; files in matched routes persist across threads, others remain ephemeral
StoreBackend requires a store instance (InMemoryStore for dev, PostgresStore for production); FilesystemBackend requires virtual_mode=True to prevent directory escape attacks
SKILL.md

Short-term (StateBackend): Persists within a single thread, lost when thread ends Long-term (StoreBackend): Persists across threads and sessions Hybrid (CompositeBackend): Route different paths to different backends

FilesystemMiddleware provides tools: ls, read_file, write_file, edit_file, glob, grep

Use Case	Backend	Why
Temporary working files	StateBackend	Default, no setup
Local development CLI	FilesystemBackend	Direct disk access
Cross-session memory	StoreBackend	Persists across threads
Hybrid storage	CompositeBackend	Mix ephemeral + persistent

agent = create_deep_agent() # Default: StateBackend result = agent.invoke({ "messages": [{"role": "user", "content": "Write notes to /draft.txt"}] }, config={"configurable": {"thread_id": "thread-1"}})

/draft.txt is lost when thread ends
</python>
<typescript>
Default StateBackend stores files ephemerally within a thread.
```typescript
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent();  // Default: StateBackend
const result = await agent.invoke({
  messages: [{ role: "user", content: "Write notes to /draft.txt" }]
}, { configurable: { thread_id: "thread-1" } });
// /draft.txt is lost when thread ends


store = InMemoryStore()

composite_backend = lambda rt: CompositeBackend( default=StateBackend(rt), routes={"/memories/": StoreBackend(rt)} )

agent = create_deep_agent(backend=composite_backend, store=store)

/draft.txt -> ephemeral (StateBackend)
/memories/user-prefs.txt -> persistent (StoreBackend)
</python>
<typescript>
Configure CompositeBackend to route paths to different storage backends.
```typescript
import { createDeepAgent, CompositeBackend, StateBackend, StoreBackend } from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore();

const agent = await createDeepAgent({
  backend: (config) => new CompositeBackend(
    new StateBackend(config),
    { "/memories/": new StoreBackend(config) }
  ),
  store
});

// /draft.txt -> ephemeral (StateBackend)
// /memories/user-prefs.txt -> persistent (StoreBackend)


config2 = {"configurable": {"thread_id": "thread-2"}} agent.invoke({"messages": [{"role": "user", "content": "Read /memories/style.txt"}]}, config=config2)

Thread 2 can read file saved by Thread 1
</python>
<typescript>
Files in /memories/ persist across threads via StoreBackend routing.
```typescript
// Using CompositeBackend from previous example
const config1 = { configurable: { thread_id: "thread-1" } };
await agent.invoke({ messages: [{ role: "user", content: "Save to /memories/style.txt" }] }, config1);

const config2 = { configurable: { thread_id: "thread-2" } };
await agent.invoke({ messages: [{ role: "user", content: "Read /memories/style.txt" }] }, config2);
// Thread 2 can read file saved by Thread 1


agent = create_deep_agent( backend=FilesystemBackend(root_dir=".", virtual_mode=True), # Restrict access interrupt_on={"write_file": True, "edit_file": True}, checkpointer=MemorySaver() )

Agent can read/write actual files on disk
</python>
<typescript>
Use FilesystemBackend for local development with real disk access and human-in-the-loop.
```typescript
import { createDeepAgent, FilesystemBackend } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const agent = await createDeepAgent({
  backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
  interruptOn: { write_file: true, edit_file: true },
  checkpointer: new MemorySaver()
});


Security: Never use FilesystemBackend in web servers - use StateBackend or sandbox instead.

@tool def get_user_preference(key: str, runtime: ToolRuntime) -> str: """Get a user preference from long-term storage.""" store = runtime.store result = store.get(("user_prefs",), key) return str(result.value) if result else "Not found"

@tool def save_user_preference(key: str, value: str, runtime: ToolRuntime) -> str: """Save a user preference to long-term storage.""" store = runtime.store store.put(("user_prefs",), key, {"value": value}) return f"Saved {key}={value}"

store = InMemoryStore()

agent = create_agent( model="gpt-4.1", tools=[get_user_preference, save_user_preference], store=store )

</python>
</ex-store-in-custom-tools>

<boundaries>
### What Agents CAN Configure

- Backend type and configuration
- Routing rules for CompositeBackend
- Root directory for FilesystemBackend
- Human-in-the-loop for file operations

### What Agents CANNOT Configure

- Tool names (ls, read_file, write_file, edit_file, glob, grep)
- Access files outside virtual_mode restrictions
- Cross-thread file access without proper backend setup
</boundaries>

<fix-storebackend-requires-store>
<python>
StoreBackend requires a store instance.
```python
# WRONG
agent = create_deep_agent(backend=lambda rt: StoreBackend(rt))

# CORRECT
agent = create_deep_agent(backend=lambda rt: StoreBackend(rt), store=InMemoryStore())


// CORRECT const agent = await createDeepAgent({ backend: (c) => new StoreBackend(c), store: new InMemoryStore() });

</typescript>
</fix-storebackend-requires-store>

<fix-statebackend-files-dont-persist>
<python>
StateBackend files are thread-scoped - use same thread_id or StoreBackend for cross-thread access.
```python
# WRONG: thread-2 can't read file from thread-1
agent.invoke({"messages": [...]}, config={"configurable": {"thread_id": "thread-1"}})  # Write
agent.invoke({"messages": [...]}, config={"configurable": {"thread_id": "thread-2"}})  # File not found!

Weekly Installs
6.8K
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