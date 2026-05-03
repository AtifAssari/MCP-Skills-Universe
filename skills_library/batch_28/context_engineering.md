---
title: context-engineering
url: https://skills.sh/siviter-xyz/dot-agent/context-engineering
---

# context-engineering

skills/siviter-xyz/dot-agent/context-engineering
context-engineering
Installation
$ npx skills add https://github.com/siviter-xyz/dot-agent --skill context-engineering
SKILL.md
Context Engineering

Context engineering curates the smallest high-signal token set for LLM tasks. The goal: maximize reasoning quality while minimizing token usage.

When to Activate
Designing/debugging agent systems
Context limits constrain performance
Optimizing cost/latency
Building multi-agent coordination
Implementing memory systems
Evaluating agent performance
Developing LLM-powered pipelines
Core Principles
Context quality > quantity - High-signal tokens beat exhaustive content
Attention is finite - U-shaped curve favors beginning/end positions
Progressive disclosure - Load information just-in-time
Isolation prevents degradation - Partition work across sub-agents
Measure before optimizing - Know your baseline
Key Metrics
Token utilization: Warning at 70%, trigger optimization at 80%
Token variance: Explains 80% of agent performance variance
Multi-agent cost: ~15x single agent baseline
Compaction target: 50-70% reduction, <5% quality loss
Cache hit target: 70%+ for stable workloads
Four-Bucket Strategy
Write: Save context externally (scratchpads, files)
Select: Pull only relevant context (retrieval, filtering)
Compress: Reduce tokens while preserving info (summarization)
Isolate: Split across sub-agents (partitioning)
Anti-Patterns
Exhaustive context over curated context
Critical info in middle positions
No compaction triggers before limits
Single agent for parallelizable tasks
Tools without clear descriptions
Guidelines
Place critical info at beginning/end of context
Implement compaction at 70-80% utilization
Use sub-agents for context isolation, not role-play
Design tools with clear descriptions (what, when, inputs, returns)
Optimize for tokens-per-task, not tokens-per-request
Validate with probe-based evaluation
Monitor token usage in production
Start minimal, add complexity only when proven necessary
Skill Coordination

When multiple skills are active:

Load only relevant skill content
Use skill metadata for discovery
Avoid loading full skill definitions unless needed
Reference skills by pattern detection, not direct names
References

For detailed guidance, see:

references/fundamentals.md - Context anatomy, attention mechanics
references/degradation.md - Debugging failures, lost-in-middle, poisoning
references/optimization.md - Compaction, masking, caching, partitioning
references/compression.md - Long sessions, summarization strategies
references/memory.md - Cross-session persistence, knowledge graphs
references/multi-agent.md - Coordination patterns, context isolation
references/evaluation.md - Testing agents, LLM-as-Judge, metrics
references/tool-design.md - Tool consolidation, description engineering
Weekly Installs
96
Repository
siviter-xyz/dot-agent
GitHub Stars
11
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass