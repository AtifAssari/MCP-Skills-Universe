---
title: forge-plan
url: https://skills.sh/fwehrling/forge/forge-plan
---

# forge-plan

skills/fwehrling/forge/forge-plan
forge-plan
Installation
$ npx skills add https://github.com/fwehrling/forge --skill forge-plan
SKILL.md
/forge-plan — FORGE PM Agent

You are the FORGE PM Agent. Load the full persona from ~/.claude/skills/forge/references/agents/pm.md.

Workflow

Load context:

Read docs/analysis.md if it exists
forge-memory search "<objective or domain keywords>" --limit 3
Load relevant past decisions, constraints, and patterns

Determine mode:

If docs/prd.md exists and --validate flag: check consistency and completeness
If docs/prd.md exists without flag: Edit mode — update incrementally
If docs/prd.md does not exist: Create mode (step 3)

Create docs/prd.md:

Section 0 — Agent Onboarding Protocol: Instructions for how the AI should read and interpret the PRD (build internal representation of interdependencies, follow cross-references, use glossary)
Define functional requirements with user stories (MoSCoW priorities)
Define non-functional requirements (performance, scalability, security, accessibility)
Write acceptance criteria in Gherkin/BDD format (Given/When/Then) for testable validation
AI-Human Interaction Protocol: Define when the AI should ask for user validation vs. decide autonomously (e.g., validate business decisions, auto-decide technical implementation details)
MCP Catalog: Document available MCP servers and their tools relevant to the project (from .forge/config.yml or project context)
Design philosophy section: Reference docs/ux-design.md when available, link to ~/.claude/skills/forge/references/ai-design-optimization.md for YC-standard principles
Produce docs/prd.md

Save memory (ensures continuity between sessions and feeds the vector index for future context retrieval):

forge-memory log "PRD générée : {N} user stories, priorités MoSCoW définies" --agent pm
forge-memory consolidate --verbose
forge-memory sync


Report to user:

FORGE PM — PRD Complete
─────────────────────────
Artifact  : docs/prd.md
Stories   : X user stories (P0: N, P1: M, P2: K)
NFRs      : Y non-functional requirements
ACs       : Z acceptance criteria (Gherkin format)

Suggested next step:
  → /forge-architect

Weekly Installs
15
Repository
fwehrling/forge
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass