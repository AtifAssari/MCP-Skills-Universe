---
title: grace-ask
url: https://skills.sh/osovv/grace-marketplace/grace-ask
---

# grace-ask

skills/osovv/grace-marketplace/grace-ask
grace-ask
Installation
$ npx skills add https://github.com/osovv/grace-marketplace --skill grace-ask
SKILL.md

Answer a question about the current GRACE project.

Process
Step 1: Load Project Context

Read the following files (skip any that don't exist):

AGENTS.md — project principles and conventions
docs/knowledge-graph.xml — module map, dependencies, exports
docs/requirements.xml — use cases and requirements
docs/technology.xml — stack, runtime, libraries
docs/development-plan.xml — phases, modules, contracts
docs/verification-plan.xml — tests, traces, log markers, and execution gates
docs/operational-packets.xml — canonical packet, delta, and failure handoff shapes
Step 2: Identify Relevant Modules

Based on the question, find the most relevant modules:

Use the knowledge graph to locate modules related to the question
Follow CrossLinks to find connected modules
Read MODULE_CONTRACTs of relevant modules for detailed context
Read matching verification entries when the question is about behavior, failure modes, or testing

If the optional grace CLI is available, you may use:

grace module find <query> --path <project-root> to resolve module IDs from names, paths, dependencies, or verification refs
grace module show M-XXX --path <project-root> --with verification to pull the shared/public module snapshot
grace file show <path> --path <project-root> --contracts --blocks to pull file-local/private context for the implementation details
Step 3: Dive Into Code If Needed

If the question is about specific behavior or implementation:

Use MODULE_MAP to locate relevant functions/blocks
Read the specific START_BLOCK/END_BLOCK sections
Read function CONTRACTs for intent vs implementation details
Read nearby tests or log-marker assertions when they are the strongest evidence for expected behavior
Step 4: Answer

Provide a clear, concise answer grounded in the actual project artifacts. Always cite which files/modules/blocks your answer is based on.

Important
Never guess — if the information isn't in the project artifacts, say so
If the question reveals a gap in documentation or contracts, mention it
If the question reveals a gap in tests, traces, or verification docs, mention it
If the answer requires changes to the project, suggest the appropriate $grace-* skill
Weekly Installs
25
Repository
osovv/grace-marketplace
GitHub Stars
150
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass