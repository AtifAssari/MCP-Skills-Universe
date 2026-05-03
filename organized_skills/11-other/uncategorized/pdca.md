---
rating: ⭐⭐⭐
title: pdca
url: https://skills.sh/popup-studio-ai/bkit-claude-code/pdca
---

# pdca

skills/popup-studio-ai/bkit-claude-code/pdca
pdca
Installation
$ npx skills add https://github.com/popup-studio-ai/bkit-claude-code --skill pdca
SKILL.md
PDCA Skill

Unified Skill for managing PDCA cycle. Supports the entire Plan → Design → Do → Check → Act flow.

Arguments
Argument	Description	Example
pm [feature]	Run PM Agent Team analysis (pre-Plan)	/pdca pm user-auth
plan [feature]	Create Plan document	/pdca plan user-auth
design [feature]	Create Design document	/pdca design user-auth
do [feature]	Do phase guide (start implementation)	/pdca do user-auth
analyze [feature]	Run Gap analysis (Check phase)	/pdca analyze user-auth
iterate [feature]	Auto improvement iteration (Act phase)	/pdca iterate user-auth
qa [feature]	Run QA phase (L1-L5 tests)	/pdca qa user-auth
report [feature]	Generate completion report	/pdca report user-auth
archive [feature]	Archive completed PDCA documents	/pdca archive user-auth
cleanup [feature]	Cleanup archived features from status	/pdca cleanup
team [feature]	Start PDCA Team Mode (requires Agent Teams)	/pdca team user-auth
team status	Show Team status	/pdca team status
team cleanup	Cleanup Team resources	/pdca team cleanup
status	Show current PDCA status	/pdca status
next	Guide to next phase	/pdca next
Action Details
pm (PM Analysis Phase)

Run PM Agent Team for product discovery and strategy analysis before Plan phase.

Call pm-lead Agent (orchestrates 4 sub-agents)
pm-lead runs Phase 1: Context Collection (project info, git history)
pm-lead runs Phase 2: Parallel Analysis (3 agents simultaneously)
pm-discovery: Opportunity Solution Tree (Teresa Torres)
pm-strategy: Value Proposition (JTBD 6-Part) + Lean Canvas
pm-research: 3 Personas + 5 Competitors + TAM/SAM/SOM
pm-lead runs Phase 3: PRD Synthesis via pm-prd agent
Beachhead Segment (Geoffrey Moore) + GTM Strategy
8-section PRD generation
Output PRD to docs/00-pm/{feature}.prd.md
Create Task: [PM] {feature}
Update .bkit-memory.json: phase = "pm"
Guide user to next step: /pdca plan {feature}

Output Path: docs/00-pm/{feature}.prd.md

Requirements:

Agent Teams enabled: CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
Project level: Dynamic or Enterprise (Starter not supported)
plan (Plan Phase)
Template Loading: Read templates/plan.template.md to understand the required Plan document structure and sections. Use this template's sections as your document outline. This is MANDATORY — do not generate Plan documents from memory or assumptions.
PRD Auto-Reference: Check if docs/00-pm/{feature}.prd.md exists
If found: Read PRD and use as context for Plan document (improves quality significantly)
If not found: Proceed normally (tip: run /pdca pm {feature} first for better results)
Check if docs/01-plan/features/{feature}.plan.md exists
If not, create based on plan.template.md
If exists, display content and suggest modifications
Checkpoint 1 — Requirements Confirmation: Present understanding of the feature (problem, scope, constraints) and use AskUserQuestion: "요구사항 이해가 맞나요? 빠진 건 없나요?" Wait for user confirmation before proceeding.
Checkpoint 2 — Clarifying Questions: Identify underspecified elements (edge cases, error handling, integration points, compatibility). Present organized question list. Wait for answers before generating the document.
Generate Plan document with user-confirmed requirements
Create Task: [Plan] {feature}
Update .bkit-memory.json: phase = "plan"
Write ## Executive Summary at document top with 4-perspective table (Problem/Solution/Function UX Effect/Core Value), each 1-2 sentences
Context Anchor Generation: After generating Plan document, extract Context Anchor (WHY/WHO/RISK/SUCCESS/SCOPE) from Executive Summary, Requirements, and Risk sections. Write as ## Context Anchor table between Executive Summary and Section 1. This anchor propagates to Design/Do documents for cross-session context continuity.
MANDATORY: After completing the document, also output the Executive Summary table in your response so the user sees it immediately without opening the file

Output Path: docs/01-plan/features/{feature}.plan.md

Tip: For features with ambiguous requirements or multiple implementation approaches, use /plan-plus {feature} instead. Plan Plus adds brainstorming phases (intent discovery, alternatives exploration, YAGNI review) before document generation for higher-quality plans.

design (Design Phase)
Template Loading: Read templates/design.template.md to understand the required Design document structure. Use this template's sections as your document outline. This is MANDATORY — do not generate Design documents from memory or assumptions.
Verify Plan document exists (required - suggest running plan first if missing)
Read Plan document to understand requirements and scope
PRD Context Loading: Check if docs/00-pm/{feature}.prd.md exists. If found, read the Executive Summary and Beachhead/GTM sections to inform architecture decisions with market context. This prevents strategic context loss at the Plan→Design handoff.
Context Anchor Embed: Copy Plan's ## Context Anchor table to Design document top (between header metadata and ## 1. Overview). If Plan has no Context Anchor (legacy), skip this step gracefully.
Generate 3 Architecture Options (inspired by feature-dev Phase 4):
Option A — Minimal Changes: Least modification, maximum reuse of existing code. Fast but potentially coupled.
Option B — Clean Architecture: Best separation of concerns, most maintainable. More files, more refactoring.
Option C — Pragmatic Balance: Good boundaries without over-engineering. Recommended default.
Present comparison table with trade-offs (complexity, maintainability, effort, risk)
Checkpoint 3 — Architecture Selection: Use AskUserQuestion: "3가지 설계안 중 어떤 걸 선택하시겠습니까?" Include recommendation. Wait for user selection.
Create docs/02-design/features/{feature}.design.md using selected architecture
Use design.template.md structure + reference Plan content
Session Guide Generation: Analyze Design's ## 11. Implementation Guide structure to generate Module Map and Recommended Session Plan. Add as ### 11.3 Session Guide within Implementation Guide section. This enables /pdca do {feature} --scope module-N for multi-session incremental implementation.
Design Anchor Integration (Pencil MCP): If the feature involves UI and Pencil MCP is available:
Suggest: "UI 컨셉 페이지를 1-2개 먼저 만든 후 /design-anchor capture {feature} 로 디자인 토큰을 잠그세요"
If Design Anchor already exists (docs/02-design/styles/{feature}.design-anchor.md), embed it in the Design document as ## Design Anchor section
This ensures design tokens (colors, typography, spacing) are locked before implementation
Create Task: [Design] {feature} (blockedBy: Plan task)
Update .bkit-memory.json: phase = "design"

Output Path: docs/02-design/features/{feature}.design.md

do (Do Phase)
Verify Design document exists (required)
Read Design document FULLY (read the entire document, not just a summary. This is critical — full context reload ensures each session starts with complete architectural context)
Full Upstream Context Loading (Phase 2+3): Load the COMPLETE upstream document chain:
Read PRD (docs/00-pm/{feature}.prd.md) — extract WHY context (JTBD, value proposition, market positioning)
Read Plan (docs/01-plan/features/{feature}.plan.md) — extract Context Anchor, Success Criteria, Requirements
This ensures implementation decisions are guided by strategic intent from PRD→Plan→Design, not just the Design spec
Decision Record Chain Display: Extract and display key decisions from PRD→Plan→Design as a unified chain. Format:
📋 Decision Record Chain
[PRD] Target: {market/user segment} — {rationale}
[Plan] Architecture: {selected option} — {rationale}
[Design] State Mgmt: {selected approach} — {rationale}

Success Criteria Tracking: Extract Success Criteria from Plan document. Display as implementation checklist — each criterion must be addressed during implementation. Mark criteria that are covered by the current --scope.
Parse --scope parameter: If arguments contain --scope <value>, extract module list (comma-separated scope keys). Match against Design's Session Guide Module Map. Filter implementation items to show only matching modules.
Display Context Anchor: Show the Context Anchor table from Design document header. Format: "📌 Context Anchor" + WHY/WHO/RISK/SUCCESS/SCOPE table. This reminds the user WHY we're building this feature.
Session Guide Display:
If no --scope: Show full Module Map from Design + recommend session split + proceed with full implementation guide
If --scope provided: Show only the selected modules' implementation items
Summarize implementation scope:
Files to create: N
Files to modify: M
Estimated changes: ~X lines
Checkpoint 4 — Implementation Approval: Present scope summary and use AskUserQuestion: "이 범위로 구현을 시작해도 되겠습니까?" DO NOT START IMPLEMENTATION WITHOUT USER APPROVAL.
After approval, provide implementation guide based on do.template.md
Reference implementation order from Design document (filtered by --scope if provided)
Code Comment Convention (Phase 3): During implementation, add Design reference comments for key architectural decisions:
At module/file level: // Design Ref: §{section} — {decision rationale}
At critical logic: // Plan SC: {success criteria being addressed}
These comments create traceable links from code back to design decisions
Create Task: [Do] {feature} (blockedBy: Design task)
Update .bkit-memory.json: phase = "do"

--scope Parameter:

/pdca do feature                      # Full scope (backward compatible) + session guide
/pdca do feature --scope module-1     # Only module-1
/pdca do feature --scope module-1,module-2  # Multiple modules


Guide Provided:

Context Anchor (WHY/WHO/RISK/SUCCESS/SCOPE)
Session scope (filtered or full)
Implementation order checklist
Key files/components list
Dependency installation commands
analyze (Check Phase)

Verify Do completion status (implementation code exists)

Full Upstream Context Loading (Phase 2+3): Load the COMPLETE upstream document chain for comprehensive evaluation:

Read PRD (docs/00-pm/{feature}.prd.md) — verify strategic alignment (was the right problem solved?)
Read Plan (docs/01-plan/features/{feature}.plan.md) — verify Requirements fulfillment + Success Criteria
Read Design (docs/02-design/features/{feature}.design.md) — verify structural implementation match
This 3-layer verification catches gaps that single-document comparison misses

Context Anchor Embed: Copy Context Anchor from Design to Analysis document header.

Strategic Alignment Check (Phase 3): Before structural gap analysis, verify:

Does the implementation address the PRD's core problem (WHY)?
Are Plan Success Criteria met or on track?
Were key Design decisions (architecture, data model, API) followed?
Flag strategic misalignments as Critical regardless of structural match rate

Plan Success Criteria Reference: Evaluate each Success Criteria from Plan:

Mark as ✅ Met / ⚠️ Partial / ❌ Not Met
Include evidence (file:line or test result)
Criteria violations are automatically Critical severity

Call gap-detector Agent (v2.3.0: Static Analysis + Runtime Verification Plan)

gap-detector performs static analysis (Structural + Functional + Contract)
gap-detector outputs a Runtime Verification Plan (L1/L2/L3 test specs)

Compare Design document vs implementation code on 3 static axes:

Structural Match: File existence, route coverage, component list
Functional Depth: Placeholder detection, Page UI Checklist verification, actual logic completeness
API Contract: 3-way verification (Design §4 ↔ Server route.ts ↔ Client fetch calls)

Runtime Verification (v2.3.0): After gap-detector completes, execute runtime tests.

Preferred: Run existing tests from tests/e2e/{feature}.spec.ts (written during Do phase)
Fallback: If no test file exists, generate from gap-detector's Runtime Verification Plan
Test scenarios are defined in Design §8 Test Plan, implemented during Do phase, executed here

L1 — API Endpoint Tests (always run if server is available):

Execute each curl command from gap-detector's L1 plan
Check: HTTP status code matches expected
Check: Response JSON shape matches expected (has .data, .error, .pagination)
Check: Auth guard returns 401 for protected endpoints
Check: Zod validation returns 400 with fieldErrors for invalid input
Check: Rate limiting returns 429 after threshold
Detect server: curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/
If no server running: skip L1, warn user, use static-only formula

L2 — UI Action Tests (run if Playwright is installed):

Generate Playwright test file from gap-detector's L2 plan
Write to tests/e2e/{feature}-actions.spec.ts
Run: npx playwright test tests/e2e/{feature}-actions.spec.ts
Each test: navigate to page → perform action → assert result
Check: API calls triggered by UI match expected endpoints
If Playwright not installed: skip L2, suggest pnpm add -D @playwright/test

L3 — E2E Scenario Tests (run if Playwright is installed):

Generate Playwright test file from gap-detector's L3 plan
Write to tests/e2e/{feature}-e2e.spec.ts
Run: npx playwright test tests/e2e/{feature}-e2e.spec.ts
Full user journey: multi-page flows with state persistence
Check: complete flow from start to end without errors

Match Rate Formula (v2.3.0):

If runtime executed:
  Overall = (Structural × 0.15) + (Functional × 0.25)
          + (Contract × 0.25) + (Runtime × 0.35)
If static only (no server):
  Overall = (Structural × 0.2) + (Functional × 0.4) + (Contract × 0.4)


Calculate Match Rate and generate Gap list. Report all rates separately.

Decision Record Verification (Phase 3): Check if key decisions from Decision Record Chain were followed in implementation. Flag deviations.

Checkpoint 5 — Review Decision: Present issues by severity (Critical/Important only, confidence ≥80%). Use AskUserQuestion with options:

"지금 모두 수정" — proceed to iterate
"Critical만 수정" — iterate critical only
"그대로 진행" — accept current state Wait for user decision before proceeding.

Create Task: [Check] {feature} (blockedBy: Do task)

Update .bkit-memory.json: phase = "check", matchRate

Output Path: docs/03-analysis/{feature}.analysis.md

qa (QA Phase)
Verify Iterate completion (Match Rate ≥ target or max iterations reached)
Delegate to qa-phase skill: Invoke the standalone /qa-phase {feature} skill, which owns L1-L5 test planning, generation, execution, and reporting.
The qa-phase skill:
Reads Design doc §8 Test Plan
Calls qa-test-planner to refine L1-L5 test specs
Calls qa-test-generator to emit runnable test files
Executes L1 (API) / L2 (UI actions) / L3 (E2E) tests via Chrome MCP
Optional L4 (perf) / L5 (security) for Enterprise level
Emit one of:
QA_PASS → auto-advance to report phase
QA_FAIL → fall back to iterate phase
QA_SKIP → mark qa as skipped, proceed to report
Create Task: [QA] {feature}
Update .bkit/state/pdca-status.json: phase = "qa", qaStatus = <PASS|FAIL|SKIP>

Output Path: docs/05-qa/{feature}.qa-report.md

Agent: bkit:qa-lead (mapped via frontmatter agents.qa)

iterate (Act Phase)
Check results (when matchRate < 90%)
Call pdca-iterator Agent
Auto-fix code based on Gap list
Auto re-run Check after fixes
Create Task: [Act-N] {feature} (N = iteration count)
Stop when >= 90% reached or max iterations (5) hit

Iteration Rules:

Max iterations: 5 (adjustable via bkit.config.json)
Stop conditions: matchRate >= 90% or maxIterations reached
report (Completion Report)
Template Loading: Read templates/report.template.md to understand the required Report document structure. Use this template's sections as your document outline. This is MANDATORY — do not generate Report documents from memory or assumptions.
Verify Check >= 90% (warn if below)
Full Upstream Context Loading (Phase 2+3): Load ALL upstream documents for comprehensive reporting:
Read PRD — compare original value proposition vs delivered value
Read Plan — compare planned Requirements/Success Criteria vs actual results
Read Design — note architecture decisions and deviations
Read Analysis — include final Match Rate and resolved gaps
This ensures the report reflects the FULL journey from PRD→Code
Call report-generator Agent
Integrated report of PRD, Plan, Design, Implementation, Analysis
Decision Record Summary (Phase 3): Include section "Key Decisions & Outcomes":
List decisions from PRD→Plan→Design chain
For each: was it followed? what was the outcome?
This creates a learnable record for future PDCA cycles
Success Criteria Final Status: Include Plan Success Criteria with final status:
Each criterion: ✅ Met (with evidence) / ❌ Not Met (with reason)
Overall Success Rate: X/Y criteria met
Include ## Executive Summary with ### 1.3 Value Delivered reflecting actual results (4 perspectives with metrics)
MANDATORY: After completing the report, also output the Executive Summary table in your response
Create Task: [Report] {feature}
Update .bkit-memory.json: phase = "completed"

Output Path: docs/04-report/{feature}.report.md

team (Team Mode) - v1.5.1

Start PDCA Team Mode using Claude Code Agent Teams (requires CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1).

team [feature] - Start Team Mode
Check if Agent Teams is available: call isTeamModeAvailable() from lib/team/coordinator.js
If not available, display: "Agent Teams is not enabled. Set CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 to enable."
Detect project level via detectLevel() - Starter projects cannot use Team Mode
Generate team strategy via generateTeamStrategy(level):
Dynamic: 3 teammates (developer, frontend, qa) — CTO Lead orchestrates
Enterprise: 5 teammates (architect, developer, qa, reviewer, security) — CTO Lead orchestrates
CTO Lead (cto-lead agent, opus) automatically:
Sets technical direction and selects orchestration pattern
Distributes tasks to teammates based on PDCA phase
Enforces quality gates (90% Match Rate threshold)
Show strategy and confirm with AskUserQuestion before starting
Assign PDCA tasks to teammates via assignNextTeammateWork()
team status - Show Team Status
Call formatTeamStatus() from lib/team/coordinator.js
Display: Team availability, enabled state, display mode, teammate count
Show current PDCA feature progress per teammate if active

Output Example:

📊 PDCA Team Status
─────────────────────────────
Agent Teams: Available ✅
Display Mode: in-process
Teammates: 4 / 4 (Enterprise)
─────────────────────────────
Feature: user-auth
  architect: [Design] in progress
  developer: [Do] waiting
  qa: idle
  reviewer: idle

team cleanup - Cleanup Team Resources
Stop all active teammates
Record team_session_ended in PDCA history via addPdcaHistory()
Return to single-session PDCA mode
Display: "Returning to single-session mode"

Required Environment: CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

Level Requirements:

Level	Available	Teammates	CTO Lead
Starter	No	-	-
Dynamic	Yes	3	cto-lead (opus)
Enterprise	Yes	5	cto-lead (opus)
archive (Archive Phase)
Verify Report completion status (phase = "completed" or matchRate >= 90%)
Verify PDCA documents exist (plan, design, analysis, report)
Create docs/archive/YYYY-MM/{feature}/ folder
Move documents (delete from original location)
Update Archive Index (docs/archive/YYYY-MM/_INDEX.md)
Update .pdca-status.json: phase = "archived", record archivedTo path
Remove feature from status (or preserve summary with --summary option)

Arguments:

Argument	Description	Example
archive {feature}	Archive with complete cleanup (default)	/pdca archive user-auth
archive {feature} --summary	Archive with summary preservation (FR-04)	/pdca archive user-auth --summary

Output Path: docs/archive/YYYY-MM/{feature}/

Documents to Archive:

docs/01-plan/features/{feature}.plan.md
docs/02-design/features/{feature}.design.md
docs/03-analysis/{feature}.analysis.md
docs/04-report/features/{feature}.report.md

FR-04: Summary Preservation Option (v1.4.8):

When using --summary (or --preserve-summary, -s), the feature data in .pdca-status.json is converted to a lightweight summary instead of being deleted:

// Summary format (70% size reduction)
{
  "my-feature": {
    "phase": "archived",
    "matchRate": 100,
    "iterationCount": 2,
    "startedAt": "2026-01-15T10:00:00Z",
    "archivedAt": "2026-01-20T15:30:00Z",
    "archivedTo": "docs/archive/2026-01/my-feature/"
  }
}


Use --summary when you need:

Historical statistics and metrics
Project duration tracking
PDCA efficiency analysis

Important Notes:

Cannot archive before Report completion
Documents are deleted from original location after move (irreversible)
Feature name must match exactly
Default behavior: complete deletion from status
Use --summary to preserve metrics for future reference
cleanup (Cleanup Phase) - v1.4.8

Clean up archived features from .pdca-status.json to reduce file size.

Read archived features from .pdca-status.json
Display list with timestamps and archive paths
Ask user for confirmation via AskUserQuestion (FR-06)
Delete selected features from status using cleanupArchivedFeatures()
Report cleanup results

Arguments:

Argument	Description	Example
cleanup	Interactive cleanup (shows list)	/pdca cleanup
cleanup all	Delete all archived features	/pdca cleanup all
cleanup {feature}	Delete specific feature	/pdca cleanup old-feature

Output Example:

🧹 PDCA Cleanup
─────────────────────────────
Archived features found: 3

1. feature-a (archived: 2026-01-15)
2. feature-b (archived: 2026-01-20)
3. feature-c (archived: 2026-01-25)

Select features to cleanup:
[ ] All archived features
[ ] Select specific features
[ ] Cancel


Related Functions (lib/pdca/status.js):

getArchivedFeatures() - Get list of archived features
cleanupArchivedFeatures(features?) - Cleanup specific or all archived
deleteFeatureFromStatus(feature) - Delete single feature
enforceFeatureLimit(max=50) - Auto cleanup when limit exceeded

Notes:

Only archived/completed features can be deleted
Active features are protected from deletion
Archive documents remain in docs/archive/ (only status is cleaned)
status (Status Check)
Read .bkit-memory.json
Display current feature, PDCA phase, Task status
Visualize progress

Output Example:

📊 PDCA Status
─────────────────────────────
Feature: user-authentication
Phase: Check (Gap Analysis)
Match Rate: 85%
Iteration: 2/5
─────────────────────────────
[Plan] ✅ → [Design] ✅ → [Do] ✅ → [Check] 🔄 → [Act] ⏳

next (Next Phase)
Check current PDCA phase
Suggest next phase guide and commands
Confirm with user via AskUserQuestion

Phase Guide:

Current	Next	Suggestion
None	pm	/pdca pm [feature] (recommended) or /pdca plan [feature]
pm	plan	/pdca plan [feature] (PRD auto-referenced)
plan	design	/pdca design [feature]
design	do	Implementation start guide
do	check	/pdca analyze [feature]
check (<90%)	act	/pdca iterate [feature]
check (>=90%)	report	/pdca report [feature]
report	archive	/pdca archive [feature]
Template References

Templates loaded from imports are used when executing each action:

Action	Template	Purpose
plan	plan.template.md	Plan document structure
design	design.template.md	Design document structure
do	do.template.md	Implementation guide structure
analyze	analysis.template.md	Analysis report structure
report	report.template.md	Completion report structure
Task Integration

Each PDCA phase automatically integrates with Task System:

Task Creation Pattern:
┌────────────────────────────────────────┐
│ [PM] {feature}                         │
│   ↓ (optional, pre-Plan)               │
│ [Plan] {feature}                       │
│   ↓ (blockedBy)                        │
│ [Design] {feature}                     │
│   ↓ (blockedBy)                        │
│ [Do] {feature}                         │
│   ↓ (blockedBy)                        │
│ [Check] {feature}                      │
│   ↓ (blockedBy, Check < 90%)           │
│ [Act-1] {feature}                      │
│   ↓ (on iteration)                     │
│ [Act-N] {feature}                      │
│   ↓ (Check >= 90%)                     │
│ [Report] {feature}                     │
│   ↓ (after Report completion)          │
│ [Archive] {feature}                    │
└────────────────────────────────────────┘

Agent Integration
Action	Agent	Role
pm	pm-lead	Orchestrate PM Agent Team (4 sub-agents)
analyze	gap-detector	Compare Design vs Implementation
iterate	pdca-iterator	Auto code fix and re-verification
report	report-generator	Generate completion report
Usage Examples
# Run PM analysis (recommended before planning)
/pdca pm user-authentication

# Start new feature
/pdca plan user-authentication

# Create design document
/pdca design user-authentication

# Implementation guide
/pdca do user-authentication

# Gap analysis after implementation
/pdca analyze user-authentication

# Auto improvement (if needed)
/pdca iterate user-authentication

# Completion report
/pdca report user-authentication

# Check current status
/pdca status

# Guide to next phase
/pdca next

Legacy Commands Mapping
Legacy Command	PDCA Skill
/pdca-plan	/pdca plan
/pdca-design	/pdca design
/pdca-analyze	/pdca analyze
/pdca-iterate	/pdca iterate
/pdca-report	/pdca report
/pdca-status	/pdca status
/pdca-next	/pdca next
/archive	/pdca archive
Output Style Integration (v1.5.1)

PDCA workflows benefit from the bkit-pdca-guide output style:

/output-style bkit-pdca-guide


This provides PDCA-specific response formatting:

Phase status badges: [Plan] -> [Design] -> [Do] -> [Check] -> [Act]
Gap analysis suggestions after code changes
Next-phase guidance with checklists
Feature usage report integration

When running PDCA commands, suggest this style if not already active.

Agent Teams Integration (v1.5.1)

For Dynamic/Enterprise projects, PDCA phases can run in parallel using Agent Teams:

/pdca team {feature}        Start parallel PDCA
/pdca team status            Monitor teammate progress
/pdca team cleanup           End team session


Suggest Agent Teams when:

Feature is classified as Major Feature (>= 1000 chars)
Match Rate < 70% (parallel iteration can speed up fixes)
Project level is Dynamic or Enterprise

CTO-Led Team Orchestration Patterns:

Level	Plan	Design	Do	Check	Act
Dynamic	leader	leader	swarm	council	leader
Enterprise	leader	council	swarm	council	watchdog
Auto Triggers

Auto-suggest related action when detecting these keywords:

Keyword	Suggested Action
"pm", "product discovery", "PRD", "market analysis"	pm
"plan", "planning", "roadmap"	plan
"design", "architecture", "spec"	design
"implement", "develop", "build"	do
"verify", "analyze", "check"	analyze
"improve", "iterate", "fix"	iterate
"complete", "report", "summary"	report
"archive", "store"	archive
"cleanup", "clean", "remove old"	cleanup
Slash Invoke Pattern (CC 2.1.0+)

Skills 2.0 enables direct slash invocation for all PDCA commands:

/pdca plan [feature] — Create Plan document
/pdca design [feature] — Create Design document
/pdca do [feature] — Implementation guide
/pdca analyze [feature] — Gap analysis (Check phase)
/pdca iterate [feature] — Auto-improvement (Act phase)
/pdca qa [feature] — Run QA phase (L1-L5 tests)
/pdca report [feature] — Completion report
/pdca status — Current PDCA status
/pdca next — Next phase guide
/plan-plus [feature] — Brainstorming-enhanced planning

Hot reload: SKILL.md changes reflect without session restart (CC 2.1.0+).

PDCA Auto-Monitoring (CC v2.1.71+)

CC v2.1.71 introduces /loop command and Cron tools for automated monitoring.

Usage Examples
/loop 5m /pdca status - Check PDCA status every 5 minutes
/loop 10m /pdca analyze [feature] - Run Gap analysis every 10 minutes
Use Cron tools for session-level scheduled checks
CTO Team Integration
Long CTO Team sessions benefit from /loop for progress monitoring
stdin freeze fixed in v2.1.71 ensures reliable long sessions
Background agent recovery (v2.1.71) makes background: true agents reliable
Weekly Installs
61
Repository
popup-studio-ai…ude-code
GitHub Stars
523
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass