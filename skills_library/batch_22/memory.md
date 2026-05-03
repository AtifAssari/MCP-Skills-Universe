---
title: memory
url: https://skills.sh/tao3k/omni-dev-fusion/memory
---

# memory

skills/tao3k/omni-dev-fusion/memory
memory
Installation
$ npx skills add https://github.com/tao3k/omni-dev-fusion --skill memory
SKILL.md
Memory Skill Policy

This skill is an MCP-facing facade for memory operations. Core memory policy (lifecycle/revalidation/promotion) belongs to Rust memory core, not this skill surface.

Router Logic
Scenario 1: User wants to store a transient finding
Analyze: Determine if the item is transient operational memory (bug/workaround/incident note)
Store: Call save_memory(content, metadata)
Confirm: Show the saved memory ID
Scenario 2: User wants to remember/search
Search: Call search_memory(query, limit)
Format: Present results with relevance scores
Respond: "I found X memories about that..."
Scenario 3: User asks for current operational memory status
List: Call get_memory_stats()
Recall: Call search_memory() with relevant keywords
Present: Show structured summary with transient scope
Commands Reference
Command	Description	Example
save_memory	Store short-term operational memory item	save_memory("Temporary workaround for timeout in parser", {"tag": "incident"})
search_memory	Semantic search in memory	search_memory("git commit format", limit=5)
index_memory	Optimize vector index (IVF-FLAT)	index_memory()
get_memory_stats	Get memory count	get_memory_stats()
load_skill	Load skill manifest into memory	load_skill("git")
Workflow: Store a Transient Workaround
User: Remember this temporary fix: increase parser timeout when MCP queue spikes.

Claude:
  1. save_memory(
       content="Temporary workaround: increase parser timeout under MCP queue spike",
       metadata={"domain": "runtime", "kind": "workaround", "source": "user"}
     )
  2. → Saved memory [a1b2c3d4]: Temporary workaround: increase parser timeout...
  3. → "Stored as short-term operational memory."

Workflow: Recall Recent Operational Context
User: What workaround did we use for MCP queue timeout?

Claude:
  1. search_memory("MCP queue timeout workaround")
  2. → Found 2 matches:
     - [Score: 0.8921] Temporary workaround: increase parser timeout...
     - [Score: 0.7234] Queue backpressure note...
  3. → "I found recent operational memory for this issue..."

Memory vs Knowledge Skill
Aspect	Memory (this skill)	Knowledge skill
Scope	Short-term operational context	Long-term reusable knowledge
Nature	Transient (can be purged after revalidation)	Stable (promoted/curated)
Purpose	"What recent issue/workaround context exists?"	"What durable rule/pattern should be reused?"
Policy	Managed by Rust memory core lifecycle	Managed by knowledge ingestion/curation flows
Exposure	MCP tool facade	MCP tool interface
Best Practices
Store transient operational memory, not permanent rules
Include kind in metadata (incident, workaround, observation)
Use clear, searchable phrasing in content
Promote only proven durable patterns to knowledge
Weekly Installs
13
Repository
tao3k/omni-dev-fusion
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass