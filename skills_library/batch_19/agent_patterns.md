---
title: agent-patterns
url: https://skills.sh/markpitt/claude-skills/agent-patterns
---

# agent-patterns

skills/markpitt/claude-skills/agent-patterns
agent-patterns
Installation
$ npx skills add https://github.com/markpitt/claude-skills --skill agent-patterns
SKILL.md
Agent Patterns Orchestration Skill

This skill implements AI agent patterns and workflows from Anthropic's "Building Effective Agents" engineering guide. It uses modular resources to help you select, design, and implement the right patterns for your needs.

Quick Reference: Which Pattern Do I Need?
Task Characteristics	Best Pattern(s)	Load Resource
Fixed sequential steps, each requires different handling	Prompt Chaining	core-patterns.md
Input falls into distinct categories	Routing	core-patterns.md
Independent tasks to run in parallel	Parallelization (Sectioning)	core-patterns.md
Same task multiple times for robustness/consensus	Parallelization (Voting)	core-patterns.md
Unpredictable subtasks, determine at runtime	Orchestrator-Workers	dynamic-orchestration.md
Fully open-ended exploration needed	Autonomous Agents	dynamic-orchestration.md
Need iterative quality improvement	Evaluator-Optimizer	iterative-refinement.md
Multiple pattern combination needed	See decision table	pattern-combinations.md
Language-specific implementation	Choose language	language-implementation.md
Tool design/optimization	Interface design	tool-design.md
Pattern Category Index
Core Patterns (Deterministic Workflows)

When to use: Workflow fully predetermined upfront

Patterns:

Prompt Chaining - Sequential LLM calls with checkpoints
Routing - Classify and route to specialized handlers
Parallelization - Concurrent execution (sectioning or voting)

Resource: resources/core-patterns.md (350+ lines)

Complete pattern descriptions and architectures
When to use / when NOT to use
Real-world examples
Code skeletons for each pattern
Dynamic Orchestration Patterns (Unpredictable Workflows)

When to use: Workflow cannot be predetermined

Patterns:

Orchestrator-Workers - Central LLM decomposes, workers execute
Autonomous Agents - Open-ended exploration with tool usage

Resource: resources/dynamic-orchestration.md (400+ lines)

Detailed pattern descriptions and requirements
When to use each approach
Critical requirements for agents
Comprehensive implementation examples
Iterative Refinement

When to use: Output quality needs improvement through feedback

Pattern:

Evaluator-Optimizer - Generator + Evaluator feedback loop

Resource: resources/iterative-refinement.md (350+ lines)

Pattern implementation strategies
Evaluation criteria design
Stopping conditions
Cost and quality trade-offs
Advanced: Pattern Combinations

When to use: Combining multiple patterns for complex problems

Examples:

Routing + Prompt Chaining (different routes, different chains)
Orchestrator + Evaluator-Optimizer (decompose, then refine)
Routing by Complexity (route to appropriate pattern)
Parallel Orchestrators (multiple perspectives)

Resource: resources/pattern-combinations.md (400+ lines)

7 major combination patterns
Decision framework and tree
Cost-complexity trade-offs
Testing strategies
Tool Design & Implementation

When to use: Designing tools for agent use

Topics:

Poka-yoke (error-proofing) design
Natural format selection
Parameter design patterns
Common pitfalls

Resource: resources/tool-design.md (560+ lines, comprehensive reference)

Core principles and best practices
Real-world insights from SWE-bench
Language-specific considerations
Testing tool interfaces
Language-Specific Implementation

When to use: Implementing patterns in your chosen language

Languages:

TypeScript/JavaScript
Python
Rust
C#/.NET
Go
Dart

Resource: resources/language-implementation.md (450+ lines)

Full code examples for each language
Language strengths and weaknesses
Best practices and idioms
Concurrency models
Orchestration Protocol
Phase 1: Identify Your Task

Ask yourself:

1. Is the workflow predetermined?

YES → Use Core Patterns (Phase 2A)
NO → Use Dynamic Patterns (Phase 2B)

2. Is output quality iteration important?

YES → Consider adding Evaluator-Optimizer
NO → Direct to execution

3. Are multiple patterns needed?

YES → Review Pattern Combinations
NO → Single pattern sufficient
Phase 2A: Select Core Pattern (Predetermined Workflow)

Decision: Sequential or Parallel?

Sequential (Fixed Steps in Sequence):

Each step depends on previous → Prompt Chaining
Example: outline → write → proofread

Classification (Input Categories Determine Handling):

Input can be classified → Routing
Example: customer service tickets (refund/technical/complaint)

Parallel (Independent Subtasks):

Subtasks are independent → Parallelization (Sectioning)
Example: evaluate code for security AND performance simultaneously

Parallel (Same Task Multiple Times):

Need consensus/robustness → Parallelization (Voting)
Example: security review by multiple specialists

→ Load resources/core-patterns.md for implementation

Phase 2B: Select Dynamic Pattern (Unpredictable Workflow)

Decision: Can you predict subtask count?

Predictable Subtasks:

Know what needs doing, not how → Orchestrator-Workers
Example: code review (need to analyze, generate, test, document)
Example: research task (need search, analysis, synthesis)

Unpredictable Everything:

Open-ended exploration → Autonomous Agents
Example: solve GitHub issue (steps completely unpredictable)
Example: computer use task (many decisions and directions possible)

→ Load resources/dynamic-orchestration.md for implementation

Phase 3: Consider Quality & Refinement

Add Evaluator-Optimizer if:

Clear evaluation criteria exist
Iteration improves quality
First attempts often have fixable issues
Quality matters more than speed

Patterns to combine with:

Core patterns + Evaluator (refine outputs)
Orchestrator + Evaluator (refine each component)
Routing + Evaluator (route to different refinement strategies)

→ Load resources/iterative-refinement.md for implementation

Phase 4: Handle Complex Patterns

If combining multiple patterns:

Follow decision framework in pattern-combinations.md
Start simple; add complexity incrementally
Monitor costs at each stage
Test edge cases thoroughly
Phase 5: Implement in Your Language

Select language and load examples:

Load resources/language-implementation.md
Find your language section
Adapt examples to your use case
Reference tool-design.md for interface best practices
Pattern Selection Heuristics
By Problem Structure

Well-Defined, Fixed Workflow → Core Patterns

Use Prompt Chaining or Routing
Cost: 1-3x single call
Risk: Low

Flexible Workflow, Known Decomposition → Orchestrator-Workers

Central planner decomposes dynamically
Cost: 3-10x single call
Risk: Medium

Open-Ended Exploration → Autonomous Agents

Agent decides step by step
Cost: 10-100x single call
Risk: High (requires sandboxing)

Quality Iteration Important → Evaluator-Optimizer

Add to any pattern above
Cost: Multiplicative by iterations
Benefit: 5-15% quality improvement

Multiple Perspectives Valuable → Pattern Combinations

Combine patterns strategically
Cost: Depends on combination
Benefit: Robustness and comprehensiveness
By Domain

Customer Service → Routing (+ Orchestrator-Workers for complex cases) Content Generation → Prompt Chaining (+ Evaluator-Optimizer) Code Changes → Orchestrator-Workers (decompose, parallelize) Research → Orchestrator-Workers (+ Evaluator-Optimizer) Problem Solving → Autonomous Agents (or Routing by Complexity) Design → Parallel Orchestrators (multiple perspectives)

Usage Workflows
Workflow 1: I Don't Know What Pattern to Use
Describe your problem or use case
I'll ask clarifying questions about:
Workflow predictability
Input variability
Quality/cost trade-offs
Complexity constraints
I'll recommend appropriate pattern(s)
You choose which resource to deep-dive into
Workflow 2: I Know the Pattern, Need Implementation
Tell me:
Specific pattern needed
Programming language
Any constraints or requirements
I'll generate:
Production-ready code
Error handling and best practices
Usage examples
Testing recommendations
Workflow 3: I Need to Combine Multiple Patterns
Describe your requirements
I'll consult pattern-combinations.md
Show you how to orchestrate the combination
Provide integrated implementation
Workflow 4: I Need Tool Interface Design
Describe your tool's purpose
I'll review against best practices in tool-design.md
Suggest improvements using poka-yoke principles
Provide refined tool schema
Resource Navigation Guide
I Want To...	Load This	Timeframe
Understand basic patterns	core-patterns.md	15 min
Learn dynamic orchestration	dynamic-orchestration.md	20 min
Understand iterative refinement	iterative-refinement.md	15 min
Design tool interfaces	tool-design.md	20 min
Combine multiple patterns	pattern-combinations.md	20 min
Implement in specific language	language-implementation.md	20-30 min
Quick reference for all patterns	Read this SKILL.md	10 min
Core Principles (All Patterns)
Start Simple – Use simplest pattern that meets requirements
Measure Complexity – Only add complexity if demonstrably beneficial
Tool Design First – Invest in tool quality more than prompt engineering
Transparency – Show planning and decisions to enable debugging
Test Rigorously – Especially important for agents in production
Validation Checklist

Before implementing your chosen pattern:

Design Phase:

 Workflow complexity justified by requirements
 Pattern selection makes sense for problem
 Cost implications understood and acceptable
 Success metrics defined

Implementation Phase:

 Error handling at each step
 Tool interfaces follow poka-yoke principles
 Stopping conditions defined (especially for agents)
 Monitoring and logging planned
 External/retrieved content delimited and treated as untrusted data (W011 prompt injection defence)
 System prompts explicitly instruct model not to follow directives in retrieved content

Testing Phase:

 Happy path tested thoroughly
 Edge cases identified and handled
 Cost tracking implemented
 Production readiness verified
Key Files Reference
File	Purpose	Lines	Read When
SKILL.md (this file)	Orchestration hub and decision guide	280	First (overview)
resources/augmented-llm.md	The foundational building block	300+	Before any pattern
resources/core-patterns.md	Prompt Chaining, Routing, Parallelization	350+	Need basic patterns
resources/dynamic-orchestration.md	Orchestrator-Workers, Autonomous Agents	400+	Need dynamic patterns
resources/iterative-refinement.md	Evaluator-Optimizer pattern	350+	Need quality iteration
resources/tool-design.md	Tool interface design and optimization	560+	Designing tools
resources/pattern-combinations.md	Complex multi-pattern workflows	400+	Combining patterns
resources/language-implementation.md	Language-specific code examples	450+	Need implementation
resources/patterns-reference.md	Original comprehensive reference	500+	Deep dive reference
Examples
Example 1: Customer Support System

Use Case: Support tickets routed to appropriate handlers

Solution:

Route by category (routing pattern)
Different handlers for each type:
General → FAQ lookup (prompt chaining)
Refunds → Policy check + response generation (prompt chaining)
Technical → Diagnosis → Solution search → Response (orchestrator-workers)

Resources to load:

Start: core-patterns.md (routing)
Then: pattern-combinations.md (routing + chaining combination)
Finally: language-implementation.md (your language)
Example 2: High-Quality Content Generation

Use Case: Marketing copy that meets strict quality criteria

Solution:

Generator creates content (simple LLM call)
Evaluator checks against criteria
If not passing: Generator refines based on feedback
Iterate until criteria met

Resources to load:

Start: iterative-refinement.md (evaluator-optimizer)
Then: language-implementation.md (your language)
Example 3: Complex Code Changes

Use Case: Handle multi-file code modifications

Solution:

Orchestrator analyzes requirements
Workers decompose into: analyze codebase → generate code → write tests → document
All workers run in parallel
Orchestrator synthesizes into coherent changeset
Evaluator validates functionality

Resources to load:

Start: dynamic-orchestration.md (orchestrator-workers)
Then: pattern-combinations.md (orchestrator + evaluation)
Then: tool-design.md (design tools for code modification)
Finally: language-implementation.md (your language)
Next Steps
Identify Your Task Type → Use Quick Reference table above
Load Appropriate Resource → Read focused guide (15-30 min)
Choose Implementation Language → Load language examples
Start with Simple Version → Add complexity only if needed
Iterate and Test → Measure quality and cost continuously
Version History
2.0 - Refactored to modular orchestration pattern with focused resource files
1.0 - Original monolithic skill with all patterns in one document
Weekly Installs
29
Repository
markpitt/claude-skills
GitHub Stars
15
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn