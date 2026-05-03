---
title: context-engineering
url: https://skills.sh/mrgoonie/claudekit-skills/context-engineering
---

# context-engineering

skills/mrgoonie/claudekit-skills/context-engineering
context-engineering
Installation
$ npx skills add https://github.com/mrgoonie/claudekit-skills --skill context-engineering
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
Quick Reference
Topic	When to Use	Reference
Fundamentals	Understanding context anatomy, attention mechanics	context-fundamentals.md
Degradation	Debugging failures, lost-in-middle, poisoning	context-degradation.md
Optimization	Compaction, masking, caching, partitioning	context-optimization.md
Compression	Long sessions, summarization strategies	context-compression.md
Memory	Cross-session persistence, knowledge graphs	memory-systems.md
Multi-Agent	Coordination patterns, context isolation	multi-agent-patterns.md
Evaluation	Testing agents, LLM-as-Judge, metrics	evaluation.md
Tool Design	Tool consolidation, description engineering	tool-design.md
Pipelines	Project development, batch processing	project-development.md
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
Design tools with 4-question framework (what, when, inputs, returns)
Optimize for tokens-per-task, not tokens-per-request
Validate with probe-based evaluation
Monitor KV-cache hit rates in production
Start minimal, add complexity only when proven necessary
Scripts
context_analyzer.py - Context health analysis, degradation detection
compression_evaluator.py - Compression quality evaluation
Weekly Installs
334
Repository
mrgoonie/claude…t-skills
GitHub Stars
2.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass