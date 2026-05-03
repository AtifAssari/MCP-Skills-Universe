---
rating: ⭐⭐⭐⭐⭐
title: write-prd
url: https://skills.sh/yonatangross/orchestkit/write-prd
---

# write-prd

skills/yonatangross/orchestkit/write-prd
write-prd
Installation
$ npx skills add https://github.com/yonatangross/orchestkit --skill write-prd
SKILL.md
PRD — Product Requirements Document

Translate product vision and research into clear, actionable engineering specifications. Produces PRD-[product-name].md output files following an 8-section structure.

Output file naming: PRD-[product-name].md (e.g., PRD-sso-invite-flow.md)

Argument Resolution
PRODUCT = "$ARGUMENTS"  # Product name or feature, e.g., "SSO invite flow"

STEP 0: Scope Clarification
AskUserQuestion(
  questions=[{
    "question": "What type of PRD?",
    "header": "PRD Scope",
    "options": [
      {"label": "Full PRD (Recommended)", "description": "All 8 sections with research, stories, and release plan", "markdown": "```\nFull PRD (8 sections)\n─────────────────────\n1. Executive Summary\n2. Problem Statement\n3. Objectives & KPIs\n4. User Stories (INVEST)\n5. Functional Requirements\n6. Non-Functional Requirements\n7. Release Plan\n8. Appendices\n```"},
      {"label": "Lightweight spec", "description": "Summary, objectives, user stories only", "markdown": "```\nLightweight Spec\n────────────────\n1. Summary (1 paragraph)\n2. Objectives (3-5 bullets)\n3. User Stories\n\nBest for: internal tools,\nsmall features, quick specs\n```"},
      {"label": "User stories only", "description": "INVEST stories with acceptance criteria", "markdown": "```\nUser Stories Only\n─────────────────\nAs a [role], I want [goal]\nso that [benefit].\n\nAcceptance Criteria:\nGiven... When... Then...\n\nINVEST: Independent,\nNegotiable, Valuable,\nEstimable, Small, Testable\n```"},
      {"label": "Update existing PRD", "description": "I have a PRD file to iterate on", "markdown": "```\nUpdate Existing PRD\n───────────────────\n→ Read current PRD file\n→ Identify gaps/changes\n→ Preserve approved sections\n→ Track change history\n```"}
    ],
    "multiSelect": false
  }]
)

Task Management
# 1. Create main task IMMEDIATELY
TaskCreate(subject="Write PRD: {PRODUCT}", description="8-section PRD with user stories and acceptance criteria", activeForm="Writing PRD for {PRODUCT}")

# 2. Create subtasks for each phase
TaskCreate(subject="Scope clarification", activeForm="Clarifying PRD scope")                       # id=2
TaskCreate(subject="Research and memory check", activeForm="Researching prior PRDs")               # id=3
TaskCreate(subject="Draft 8-section PRD", activeForm="Drafting PRD sections")                      # id=4
TaskCreate(subject="Write user stories and acceptance criteria", activeForm="Writing user stories") # id=5
TaskCreate(subject="Write output file", activeForm="Writing PRD file")                             # id=6

# 3. Set dependencies for sequential phases
TaskUpdate(taskId="3", addBlockedBy=["2"])  # Research needs scope first
TaskUpdate(taskId="4", addBlockedBy=["3"])  # Drafting needs research context
TaskUpdate(taskId="5", addBlockedBy=["4"])  # Stories need draft structure
TaskUpdate(taskId="6", addBlockedBy=["5"])  # Output needs all sections done

# 4. Before starting each task, verify it's unblocked
task = TaskGet(taskId="2")  # Verify blockedBy is empty

# 5. Update status as you progress
TaskUpdate(taskId="2", status="in_progress")  # When starting
TaskUpdate(taskId="2", status="completed")    # When done — repeat for each subtask

Memory Integration
# Search for prior PRDs and product decisions
mcp__memory__search_nodes(query="{PRODUCT} PRD requirements")

# After PRD is written, store key decisions
mcp__memory__create_entities(entities=[{
  "name": "PRD-{product-slug}",
  "entityType": "document",
  "observations": ["PRD written for {PRODUCT}", "Key objectives: ..."]
}])

The 8-Section PRD Template

Load Read("${CLAUDE_SKILL_DIR}/references/prd-template.md") for the full template with all 8 sections (Summary, Contacts, Background, Objective, Market Segments, Value Propositions, Solution, Release), priority levels, and NFR categories.

User Stories & Acceptance Criteria

Load Read("${CLAUDE_SKILL_DIR}/references/user-stories-guide.md") for INVEST criteria, story format, Gherkin acceptance criteria, and Definition of Ready/Done.

Value Proposition Canvas

Load Read("${CLAUDE_SKILL_DIR}/references/value-prop-canvas-guide.md") for the canvas template and fit check process. Every Value Map item must correspond to a Job, Pain, or Gain.

Go/No-Go Gate Criteria

Load from rules: Read("${CLAUDE_SKILL_DIR}/rules/strategy-go-no-go.md") for stage gate criteria and scoring thresholds (Go >= 7.0 | Conditional 5.0-6.9 | No-Go < 5.0).

Rules (Load On-Demand)
research-requirements-prd.md — INVEST user stories, PRD template, priority levels, DoR/DoD
strategy-value-prop.md — Value proposition canvas, JTBD framework, fit assessment
strategy-go-no-go.md — Stage gate criteria, scoring, build/buy/partner decision matrix
References
output-templates.md — Structured JSON output schemas for PRD, business case, and strategy artifacts
value-prop-canvas-guide.md — Detailed value proposition canvas facilitation guide
Output

After generating the PRD, write it to disk:

Write(f"PRD-{product_slug}.md", prd_content)
TaskUpdate(status="completed")


Plan-mode filenames (CC 2.1.111+): If this skill enters plan mode (via EnterPlanMode) before writing the PRD, CC 2.1.111 names the resulting plan file after the prompt stem rather than random words. To get a clean filename, include the product slug in the plan-mode prompt (e.g. EnterPlanMode("PRD: authentication-rework") → plans/prd-authentication-rework.md). Before 2.1.111, plan filenames were plans/swift-cobra.md etc. — review and rename as needed.

Chain: Next Steps

After PRD is approved, chain into implementation:

/ork:implement PRD-{product-slug}.md

Related Skills
ork:user-research — Build user understanding (personas, journey maps, interviews) before writing the PRD
ork:implement — Execute the implementation plan from the PRD
ork:brainstorm — Explore solution alternatives before committing to PRD scope
ork:assess — Rate PRD quality and completeness

Version: 2.0.0

Weekly Installs
152
Repository
yonatangross/orchestkit
GitHub Stars
162
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass