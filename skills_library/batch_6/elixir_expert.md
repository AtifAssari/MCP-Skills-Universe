---
title: elixir-expert
url: https://skills.sh/404kidwiz/claude-supercode-skills/elixir-expert
---

# elixir-expert

skills/404kidwiz/claude-supercode-skills/elixir-expert
elixir-expert
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill elixir-expert
SKILL.md
Elixir Expert
Purpose

Provides expertise in Elixir development, Phoenix Framework, and OTP patterns. Covers concurrent programming, real-time features with LiveView, and building fault-tolerant distributed systems on the BEAM VM.

When to Use
Building Elixir applications
Developing Phoenix web applications
Implementing real-time features with LiveView
Using OTP patterns (GenServer, Supervisor)
Building distributed systems on BEAM
Designing fault-tolerant architectures
Working with Ecto for database access
Quick Start

Invoke this skill when:

Building Elixir applications
Developing Phoenix web applications
Implementing real-time features with LiveView
Using OTP patterns
Designing fault-tolerant systems

Do NOT invoke when:

Building Ruby on Rails apps (use rails-expert)
Building Node.js backends (use javascript-pro)
Building Python backends (use python-pro)
Infrastructure automation (use terraform-engineer)
Decision Framework
Concurrency Pattern:
├── Stateful process → GenServer
├── Async work → Task
├── Background job → Oban or Task.Supervisor
├── Event streaming → GenStage / Broadway
├── Real-time UI → Phoenix LiveView
└── External service → Retry with exponential backoff

Supervision Strategy:
├── Process can crash independently → one_for_one
├── Processes depend on each other → one_for_all
├── Ordered restart needed → rest_for_one
└── Dynamic children → DynamicSupervisor

Core Workflows
1. Phoenix Application Setup
Generate Phoenix project
Configure database with Ecto
Define schemas and migrations
Create contexts for business logic
Build controllers or LiveViews
Add authentication
Deploy with releases
2. OTP Application Design
Identify stateful components
Design supervision tree
Implement GenServers for state
Add proper error handling
Implement graceful shutdown
Test supervision strategies
3. Real-Time with LiveView
Generate LiveView module
Define assigns and state
Implement handle_event callbacks
Use pubsub for broadcasts
Optimize with temporary_assigns
Add JS hooks if needed
Best Practices
Let it crash - design for failure recovery
Use supervision trees for fault tolerance
Keep GenServer state minimal
Use contexts to organize business logic
Prefer immutable data transformations
Test concurrent code with async: true
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
Large GenServer state	Memory and serialization	External storage, ETS
Defensive coding	Hides bugs	Let it crash, supervise
Blocking GenServer	Process bottleneck	Async tasks for I/O
No supervision	Unrecoverable crashes	Proper supervision tree
Mutable mindset	Bugs and race conditions	Embrace immutability
Weekly Installs
270
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass