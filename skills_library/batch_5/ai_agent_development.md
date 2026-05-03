---
title: ai-agent-development
url: https://skills.sh/sickn33/antigravity-awesome-skills/ai-agent-development
---

# ai-agent-development

skills/sickn33/antigravity-awesome-skills/ai-agent-development
ai-agent-development
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill ai-agent-development
SKILL.md
AI Agent Development Workflow
Overview

Specialized workflow for building AI agents including single autonomous agents, multi-agent systems, agent orchestration, tool integration, and human-in-the-loop patterns.

When to Use This Workflow

Use this workflow when:

Building autonomous AI agents
Creating multi-agent systems
Implementing agent orchestration
Adding tool integration to agents
Setting up agent memory
Workflow Phases
Phase 1: Agent Design
Skills to Invoke
ai-agents-architect - Agent architecture
autonomous-agents - Autonomous patterns
Actions
Define agent purpose
Design agent capabilities
Plan tool integration
Design memory system
Define success metrics
Copy-Paste Prompts
Use @ai-agents-architect to design AI agent architecture

Phase 2: Single Agent Implementation
Skills to Invoke
autonomous-agent-patterns - Agent patterns
autonomous-agents - Autonomous agents
Actions
Choose agent framework
Implement agent logic
Add tool integration
Configure memory
Test agent behavior
Copy-Paste Prompts
Use @autonomous-agent-patterns to implement single agent

Phase 3: Multi-Agent System
Skills to Invoke
crewai - CrewAI framework
multi-agent-patterns - Multi-agent patterns
Actions
Define agent roles
Set up agent communication
Configure orchestration
Implement task delegation
Test coordination
Copy-Paste Prompts
Use @crewai to build multi-agent system with roles

Phase 4: Agent Orchestration
Skills to Invoke
langgraph - LangGraph orchestration
workflow-orchestration-patterns - Orchestration
Actions
Design workflow graph
Implement state management
Add conditional branches
Configure persistence
Test workflows
Copy-Paste Prompts
Use @langgraph to create stateful agent workflows

Phase 5: Tool Integration
Skills to Invoke
agent-tool-builder - Tool building
tool-design - Tool design
Actions
Identify tool needs
Design tool interfaces
Implement tools
Add error handling
Test tool usage
Copy-Paste Prompts
Use @agent-tool-builder to create agent tools

Phase 6: Memory Systems
Skills to Invoke
agent-memory-systems - Memory architecture
conversation-memory - Conversation memory
Actions
Design memory structure
Implement short-term memory
Set up long-term memory
Add entity memory
Test memory retrieval
Copy-Paste Prompts
Use @agent-memory-systems to implement agent memory

Phase 7: Evaluation
Skills to Invoke
agent-evaluation - Agent evaluation
evaluation - AI evaluation
Actions
Define evaluation criteria
Create test scenarios
Measure agent performance
Test edge cases
Iterate improvements
Copy-Paste Prompts
Use @agent-evaluation to evaluate agent performance

Agent Architecture
User Input -> Planner -> Agent -> Tools -> Memory -> Response
              |          |        |        |
         Decompose   LLM Core  Actions  Short/Long-term

Quality Gates
 Agent logic working
 Tools integrated
 Memory functional
 Orchestration tested
 Evaluation passing
Related Workflow Bundles
ai-ml - AI/ML development
rag-implementation - RAG systems
workflow-automation - Workflow patterns
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
325
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass