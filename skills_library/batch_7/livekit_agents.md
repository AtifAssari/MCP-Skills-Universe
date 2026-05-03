---
title: livekit-agents
url: https://skills.sh/livekit/agent-skills/livekit-agents
---

# livekit-agents

skills/livekit/agent-skills/livekit-agents
livekit-agents
Installation
$ npx skills add https://github.com/livekit/agent-skills --skill livekit-agents
Summary

Build voice AI agents on LiveKit Cloud with structured workflows, minimal latency, and mandatory test coverage.

Use LiveKit Cloud and LiveKit Inference for managed infrastructure and AI models without separate API keys
Design agents around handoffs (agent-to-agent transitions) and tasks (scoped operations) to isolate context and reduce latency
Every agent implementation requires tests covering basic conversation flow, tool invocation, error handling, and edge cases before deployment
Always verify APIs against live documentation via MCP or web search; never rely on model memory for LiveKit SDK specifics
Minimize system prompts and tool lists to keep voice interactions responsive; context bloat directly increases latency
SKILL.md
LiveKit Agents Development for LiveKit Cloud

This skill provides opinionated guidance for building voice AI agents with LiveKit Cloud. It assumes you are using LiveKit Cloud (the recommended path) and encodes how to approach agent development, not API specifics. All factual information about APIs, methods, and configurations must come from live documentation.

This skill is for LiveKit Cloud developers. If you're self-hosting LiveKit, some recommendations (particularly around LiveKit Inference) won't apply directly.

MANDATORY: Read This Checklist Before Starting

Before writing ANY code, complete this checklist:

Read this entire skill document - Do not skip sections even if MCP is available
Ensure LiveKit Cloud project is connected - You need LIVEKIT_URL, LIVEKIT_API_KEY, and LIVEKIT_API_SECRET from your Cloud project
Set up documentation access - Use MCP if available, otherwise use web search
Plan to write tests - Every agent implementation MUST include tests (see testing section below)
Verify all APIs against live docs - Never rely on model memory for LiveKit APIs

This checklist applies regardless of whether MCP is available. MCP provides documentation access but does NOT replace the guidance in this skill.

LiveKit Cloud Setup

LiveKit Cloud is the fastest way to get a voice agent running. It provides:

Managed infrastructure (no servers to deploy)
LiveKit Inference for AI models (no separate API keys needed)
Built-in noise cancellation, turn detection, and other voice features
Simple credential management
Connect to Your Cloud Project

Sign up at cloud.livekit.io if you haven't already

Create a project (or use an existing one)

Get your credentials from the project settings:

LIVEKIT_URL - Your project's WebSocket URL (e.g., wss://your-project.livekit.cloud)
LIVEKIT_API_KEY - API key for authentication
LIVEKIT_API_SECRET - API secret for authentication

Set these as environment variables (typically in .env.local):

LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret


The LiveKit CLI can automate credential setup. Consult the CLI documentation for current commands.

Use LiveKit Inference for AI Models

LiveKit Inference is the recommended way to use AI models with LiveKit Cloud. It provides access to leading AI model providers—all through your LiveKit credentials with no separate API keys needed.

Benefits of LiveKit Inference:

No separate API keys to manage for each AI provider
Billing consolidated through your LiveKit Cloud account
Optimized for voice AI workloads

Consult the documentation for available models, supported providers, and current usage patterns. The documentation always has the most up-to-date information.

Critical Rule: Never Trust Model Memory for LiveKit APIs

LiveKit Agents is a fast-evolving SDK. Model training data is outdated the moment it's created. When working with LiveKit:

Never assume API signatures, method names, or configuration options from memory
Never guess SDK behavior or default values
Always verify against live documentation before writing code
Always cite the documentation source when implementing features

This rule applies even when confident about an API. Verify anyway.

REQUIRED: Use LiveKit MCP Server for Documentation

Before writing any LiveKit code, ensure access to the LiveKit documentation MCP server. This provides current, verified API information and prevents reliance on stale model knowledge.

Check for MCP Availability

Look for livekit-docs MCP tools. If available, use them for all documentation lookups:

Search documentation before implementing any feature
Verify API signatures and method parameters
Look up configuration options and their valid values
Find working examples for the specific task at hand
If MCP Is Not Available

If the LiveKit MCP server is not configured, inform the user and recommend installation. Installation instructions for all supported platforms are available at:

https://docs.livekit.io/intro/mcp-server/

Fetch the installation instructions appropriate for the user's coding agent from that page.

Fallback When MCP Unavailable

If MCP cannot be installed in the current session:

Inform the user immediately that documentation cannot be verified in real-time
Use web search to fetch current documentation from docs.livekit.io
Explicitly mark all LiveKit-specific code with a comment like # UNVERIFIED: Please check docs.livekit.io for current API
State clearly when you cannot verify something: "I cannot verify this API signature against current documentation"
Recommend the user verify against https://docs.livekit.io before using the code
Voice Agent Architecture Principles

Voice AI agents have fundamentally different requirements than text-based agents or traditional software. Internalize these principles:

Latency Is Critical

Voice conversations are real-time. Users expect responses within hundreds of milliseconds, not seconds. Every architectural decision should consider latency impact:

Minimize LLM context size to reduce inference time
Avoid unnecessary tool calls during active conversation
Prefer streaming responses over batch responses
Design for the unhappy path (network delays, API timeouts)
Context Bloat Kills Performance

Large system prompts and extensive tool lists directly increase latency. A voice agent with 50 tools and a 10,000-token system prompt will feel sluggish regardless of model speed.

Design agents with minimal viable context:

Include only tools relevant to the current conversation phase
Keep system prompts focused and concise
Remove tools and context that aren't actively needed
Users Don't Read, They Listen

Voice interface constraints differ from text:

Long responses frustrate users—keep outputs concise
Users cannot scroll back—ensure clarity on first delivery
Interruptions are normal—design for graceful handling
Silence feels broken—acknowledge processing when needed
Workflow Architecture: Handoffs and Tasks

Complex voice agents should not be monolithic. LiveKit Agents supports structured workflows that maintain low latency while handling sophisticated use cases.

The Problem with Monolithic Agents

A single agent handling an entire conversation flow accumulates:

Tools for every possible action (bloated tool list)
Instructions for every conversation phase (bloated context)
State management for all scenarios (complexity)

This creates latency and reduces reliability.

Handoffs: Agent-to-Agent Transitions

Handoffs allow one agent to transfer control to another. Use handoffs to:

Separate distinct conversation phases (greeting → intake → resolution)
Isolate specialized capabilities (general support → billing specialist)
Manage context boundaries (each agent has only what it needs)

Design handoffs around natural conversation boundaries where context can be summarized rather than transferred wholesale.

Tasks: Scoped Operations

Tasks are tightly-scoped prompts designed to achieve a specific outcome. Use tasks for:

Discrete operations that don't require full agent capabilities
Situations where a focused prompt outperforms a general-purpose agent
Reducing context when only a specific capability is needed

Consult the documentation for implementation details on handoffs and tasks.

REQUIRED: Write Tests for Agent Behavior

Voice agent behavior is code. Every agent implementation MUST include tests. Shipping an agent without tests is shipping untested code.

Mandatory Testing Workflow

When building or modifying a LiveKit agent:

Create a tests/ directory if one doesn't exist
Write at least one test before considering the implementation complete
Test the core behavior the user requested
Run the tests to verify they pass
Test-Driven Development Process

When modifying agent behavior—instructions, tool descriptions, workflows—begin by writing tests for the desired behavior:

Define what the agent should do in specific scenarios
Write test cases that verify this behavior
Implement the feature
Iterate until tests pass

This approach prevents shipping agents that "seem to work" but fail in production.

What Every Agent Test Should Cover

At minimum, write tests for:

Basic conversation flow: Agent responds appropriately to a greeting
Tool invocation (if tools exist): Tools are called with correct parameters
Error handling: Agent handles unexpected input gracefully

Focus tests on:

Tool invocation: Does the agent call the right tools with correct parameters?
Response quality: Does the agent produce appropriate responses for given inputs?
Workflow transitions: Do handoffs and tasks trigger correctly?
Edge cases: How does the agent handle unexpected input, interruptions, silence?
Test Implementation Pattern

Use LiveKit's testing framework. Consult the testing documentation via MCP for current patterns:

search: "livekit agents testing"


The framework supports:

Simulated user input
Verification of agent responses
Tool call assertions
Workflow transition testing
Why This Is Non-Negotiable

Agents that "seem to work" in manual testing frequently fail in production:

Prompt changes silently break behavior
Tool descriptions affect when tools are called
Model updates change response patterns

Tests catch these issues before users do.

Skipping Tests

If a user explicitly requests no tests, proceed without them but inform them:

"I've built the agent without tests as requested. I strongly recommend adding tests before deploying to production. Voice agents are difficult to verify manually and tests prevent silent regressions."

Common Mistakes to Avoid
Overloading the Initial Agent

Starting with one agent that "does everything" and adding tools/instructions over time. Instead, design workflow structure upfront, even if initial implementation is simple.

Ignoring Latency Until It's a Problem

Latency issues compound. An agent that feels "a bit slow" in development becomes unusable in production with real network conditions. Measure and optimize latency continuously.

Copying Examples Without Understanding

Examples in documentation demonstrate specific patterns. Copying code without understanding its purpose leads to bloated, poorly-structured agents. Understand what each component does before including it.

Skipping Tests Because "It's Just Prompts"

Agent behavior is code. Prompt changes affect behavior as much as code changes. Test agent behavior with the same rigor as traditional software. Never deliver an agent implementation without at least one test file.

Assuming Model Knowledge Is Current

Reiterating the critical rule: never trust model memory for LiveKit APIs. The SDK evolves faster than model training cycles. Verify everything.

When to Consult Documentation

Always consult documentation for:

API method signatures and parameters
Configuration options and their valid values
SDK version-specific features or changes
Deployment and infrastructure setup
Model provider integration details
CLI commands and flags

This skill provides guidance on:

Architectural approach and design principles
Workflow structure decisions
Testing strategy
Common pitfalls to avoid

The distinction matters: this skill tells you how to think about building voice agents. The documentation tells you how to implement specific features.

Feedback Loop

When using LiveKit documentation via MCP, note any gaps, outdated information, or confusing content. Reporting documentation issues helps improve the ecosystem for all developers.

Summary

Building effective voice agents with LiveKit Cloud requires:

Use LiveKit Cloud + LiveKit Inference as the foundation—it's the fastest path to production
Verify everything against live documentation—never trust model memory
Minimize latency at every architectural decision point
Structure workflows using handoffs and tasks to manage complexity
Test behavior before and after changes—never ship without tests
Keep context minimal—only include what's needed for the current phase

These principles remain valid regardless of SDK version or API changes. For all implementation specifics, consult the LiveKit documentation via MCP.

Weekly Installs
1.8K
Repository
livekit/agent-skills
GitHub Stars
46
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass