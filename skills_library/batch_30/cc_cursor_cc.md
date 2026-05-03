---
title: cc-cursor-cc
url: https://skills.sh/chachamaru127/claude-code-harness/cc-cursor-cc
---

# cc-cursor-cc

skills/chachamaru127/claude-code-harness/cc-cursor-cc
cc-cursor-cc
Installation
$ npx skills add https://github.com/chachamaru127/claude-code-harness --skill cc-cursor-cc
SKILL.md
CC-Cursor-CC Skill (Plan Validation Round Trip)

Supports the flow of sending brainstormed content from Claude Code to Cursor (PM) for feasibility validation.

Prerequisites

This skill assumes 2-agent operation.

Role	Agent	Description
PM	Cursor	Validate plans, update Plans.md
Impl	Claude Code	Brainstorming, implementation
Execution Flow
Step 1: Extract Brainstorming Context

Extract from recent conversation:

Goal (feature/purpose)
Technology choices
Decisions made
Undecided items
Concerns
Step 2: Add Provisional Tasks to Plans.md
## 🟠 Under Validation: {{Project}} `pm:awaiting-validation`

### Provisional Tasks (To Validate)
- [ ] {{task1}} `awaiting-validation`
- [ ] {{task2}} `awaiting-validation`

### Undecided Items
- {{item1}} → **Requesting PM decision**

Step 3: Generate Validation Request for Cursor

Generate text to copy-paste to Cursor:

## 📋 Plan Validation Request

**Goal**: {{summary}}

**Provisional tasks**:
1. {{task1}}
2. {{task2}}

### ✅ Requesting Cursor (PM) to:
1. Validate feasibility
2. Break down tasks
3. Decide undecided items
4. Update Plans.md (awaiting → cc:TODO)

Step 4: Guide Next Action
Copy & paste request to Cursor
Run /plan-with-cc in Cursor
Cursor updates Plans.md
Cursor runs /handoff-to-claude
Copy & paste back to Claude Code
Overall Flow
Claude Code (Brainstorm)
    ↓ /cc-cursor-cc
Cursor (PM validates & breaks down)
    ↓ /handoff-to-claude
Claude Code (/work implements)

Weekly Installs
27
Repository
chachamaru127/c…-harness
GitHub Stars
598
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass