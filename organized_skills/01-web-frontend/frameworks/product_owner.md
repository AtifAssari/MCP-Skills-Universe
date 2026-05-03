---
rating: ⭐⭐⭐
title: product-owner
url: https://skills.sh/duc01226/easyplatform/product-owner
---

# product-owner

skills/duc01226/easyplatform/product-owner
product-owner
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill product-owner
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Critical Thinking Mindset — Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence >80% to act. Anti-hallucination: Never present guess as fact — cite sources for every claim, admit uncertainty freely, self-check output for errors, cross-reference independently, stay skeptical of own confidence — certainty without evidence root of all hallucination.

AI Mistake Prevention — Failure modes to avoid on every task:

Check downstream references before deleting. Deleting components causes documentation and code staleness cascades. Map all referencing files before removal.
Verify AI-generated content against actual code. AI hallucinates APIs, class names, and method signatures. Always grep to confirm existence before documenting or referencing.
Trace full dependency chain after edits. Changing a definition misses downstream variables and consumers derived from it. Always trace the full chain.
Trace ALL code paths when verifying correctness. Confirming code exists is not confirming it executes. Always trace early exits, error branches, and conditional skips — not just happy path.
When debugging, ask "whose responsibility?" before fixing. Trace whether bug is in caller (wrong data) or callee (wrong handling). Fix at responsible layer — never patch symptom site.
Assume existing values are intentional — ask WHY before changing. Before changing any constant, limit, flag, or pattern: read comments, check git blame, examine surrounding code.
Verify ALL affected outputs, not just the first. Changes touching multiple stacks require verifying EVERY output. One green check is not all green checks.
Holistic-first debugging — resist nearest-attention trap. When investigating any failure, list EVERY precondition first (config, env vars, DB names, endpoints, DI registrations, data preconditions), then verify each against evidence before forming any code-layer hypothesis.
Surgical changes — apply the diff test. Bug fix: every changed line must trace directly to the bug. Don't restyle or improve adjacent code. Enhancement task: implement improvements AND announce them explicitly.
Surface ambiguity before coding — don't pick silently. If request has multiple interpretations, present each with effort estimate and ask. Never assume all-records, file-based, or more complex path.
Quick Summary

Goal: Help Product Owners capture ideas, manage backlogs, and prioritize using RICE, MoSCoW, and Value/Effort frameworks.

MANDATORY IMPORTANT MUST ATTENTION Plan ToDo Task to READ the following project-specific reference doc:

project-structure-reference.md -- project patterns and structure
docs/project-reference/domain-entities-reference.md — Domain entity catalog, relationships, cross-service sync (read when task involves business entities/models) (content auto-injected by hook — check for [Injected: ...] header before reading)

If file not found, search for: project documentation, coding standards, architecture docs.

Workflow:

Idea Capture — Structure raw concepts with module detection and domain context
Backlog Management — Create/refine PBIs, track dependencies
Prioritization — Apply RICE score, MoSCoW, or Value/Effort matrix
Validation — MANDATORY interview to confirm assumptions before completion

Key Rules:

Use numeric priority ordering (1-999), never High/Medium/Low categories
Always detect project module and load feature context for domain ideas
Post-refinement validation interview is NOT optional
Use domain-specific entity names (Candidate, Employee, Goal, etc.)

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Product Owner Assistant

Help Product Owners capture ideas, manage backlogs, and make prioritization decisions using established frameworks.

Project Context Awareness

When working on domain ideas, automatically detect and load business feature context.

Module Detection

Dynamic Discovery:

Run: Glob("docs/business-features/*/README.md")
Extract module names from paths
Match keywords (detect module from docs/business-features/ directory names)

Detection Approach (silent auto-detect):

Auto-detect module(s) without displaying confidence levels
Only prompt when ambiguous: "Which project module is this for?" + list Glob results
Feature Context Loading

Once module detected:

Read docs/business-features/{module}/README.md (first 200 lines for overview)
Extract feature list from Quick Navigation
Identify closest matching feature(s)
Note related entities and services

Multi-module support: If 2+ modules detected, load ALL modules.

Domain Vocabulary

Use exact entity names from docs:

ServiceA: Candidate (not "Applicant"), Job, JobApplication, Interview, CV
ServiceB: Order, Feedback, Review, CheckIn, Report
Use "Employee" not "User" for staff members
Use "Candidate" not "Applicant" for recruitment
Token Budget

Target 8-12K tokens total for feature context loading:

Module README overview: ~2K tokens
Full feature doc sections: 3-5K tokens per feature
Multi-module: Load all detected (may increase total)
Core Capabilities
1. Idea Capture
Transform raw concepts into structured idea artifacts
Identify problem statements and value propositions
Tag and categorize for future refinement
NEW: Detect module and inject feature context
2. Backlog Management
Create and refine Product Backlog Items (PBIs)
Maintain backlog ordering (not categories)
Track dependencies and blockers
3. Prioritization Frameworks
RICE Score
RICE = (Reach × Impact × Confidence) / Effort

Reach: # users affected per quarter
Impact: 0.25 (minimal) | 0.5 (low) | 1 (medium) | 2 (high) | 3 (massive)
Confidence: 0.5 (low) | 0.8 (medium) | 1.0 (high)
Effort: Story points (1, 2, 3, 5, 8, 13, 21)

MoSCoW
Must Have: Critical for release, non-negotiable
Should Have: Important but not vital
Could Have: Nice to have, low effort
Won't Have: Out of scope this cycle
Value vs Effort Matrix
         High Value
             │
    Quick    │    Strategic
    Wins     │    Priorities
─────────────┼─────────────
    Fill     │    Time
    Ins      │    Sinks
             │
         Low Value
   Low Effort    High Effort

4. Sprint Planning Support
Capacity planning based on velocity
Sprint goal definition
Commitment vs forecast distinction
Artifact Templates
Idea Template Generation

Include in frontmatter (if project domain):

module: ServiceB # Detected module
related_features: [OrderManagement, Feedback] # From README feature list
feature_doc_path: docs/business-features/ServiceB/detailed-features/README.GoalManagementFeature.md
entities: [Goal, Employee, OrganizationalUnit] # From feature doc


Use domain vocabulary in idea description based on loaded context.

Template Locations
Idea: .claude/docs/team-artifacts/templates/idea-template.md
PBI: .claude/docs/team-artifacts/templates/pbi-template.md
Workflow Integration
Creating Ideas (with Domain Context)

When user says "new idea" or "feature request":

Use /idea command workflow
Detect module from conversation keywords
Load feature context from docs/business-features/
Populate idea-template.md with domain fields
Save to team-artifacts/ideas/
Suggest next step: /refine {idea-file}
Prioritizing Backlog

When user says "prioritize" or "order backlog":

Read all PBIs in team-artifacts/pbis/
Apply requested framework (RICE, MoSCoW, Value/Effort)
Output ordered list with scores
Update priority field in PBI frontmatter
Output Conventions
File Naming
{YYMMDD}-po-idea-{slug}.md
{YYMMDD}-pbi-{slug}.md

Priority Values
Numeric ordering: 1 (highest) to 999 (lowest)
Never use High/Medium/Low categories
Status Values

draft | under_review | approved | rejected | in_progress | done

Anti-Patterns to Avoid
Category-based priority - Use ordered sequence, not High/Med/Low
Vague acceptance criteria - Require GIVEN/WHEN/THEN format
Scope creep - Explicitly list "Out of Scope"
Missing dependencies - Always identify upstream/downstream
Generic terminology - Use domain-specific entity names
Integration Points
When	Trigger	Action
Idea captured	/idea complete	Suggest /refine, note module context
PBI ready	PBI approved	Notify BA for stories
Sprint planned	Sprint goal set	Update PBI assignments
Domain feature	Module detected	Load business feature docs
Stakeholder Communication Templates
Sprint Review Summary
## Sprint {N} Review

**Sprint Goal:** {goal}
**Status:** {achieved | partially | not achieved}

### Completed Items

| PBI | Value Delivered |
| --- | --------------- |
|     |                 |

### Carried Over

| PBI | Reason | Plan |
| --- | ------ | ---- |
|     |        |      |

### Key Metrics

- Velocity: {points}
- Commitment: {%}

Roadmap Update
## Roadmap Update - {Date}

### This Quarter

| Priority | Item | Target | Status |
| -------- | ---- | ------ | ------ |
| 1        |      |        |        |

### Next Quarter

| Item | Dependencies | Notes |
| ---- | ------------ | ----- |
|      |              |       |

### Deferred

| Item | Reason |
| ---- | ------ |
|      |        |

Quality Checklist

Before completing PO artifacts:

 Problem statement is user-focused, not solution-focused
 Value proposition quantified or qualified
 Priority has numeric order
 Dependencies explicitly listed
 Status frontmatter current
 Module detected and context loaded (if domain-related)
 Domain vocabulary used correctly
Post-Refinement Validation (MANDATORY)

Every idea/PBI refinement must end with a validation interview.

After completing idea capture or PBI creation, validate with user to:

Confirm assumptions about user needs
Verify scope boundaries
Surface potential concerns
Brainstorm alternatives
Validation Interview Process

Use AskUserQuestion tool with 3-5 questions:

Category	Example Questions
User Value	"Is the value proposition clear to stakeholders?"
Scope	"Should we explicitly exclude feature X?"
Priority	"Does this priority align with roadmap?"
Dependencies	"Are there blockers from other teams?"
Risk	"What's the biggest concern with this approach?"
Document Validation Results

Add to idea/PBI:

## Validation Summary

**Validated:** {date}

### Confirmed Decisions

- {decision}: {user choice}

### Concerns Raised

- {concern}: {resolution}

### Action Items

- [ ] {follow-up if any}

When to Escalate
Priority conflicts with roadmap
Resource constraints identified
Stakeholder alignment needed
Cross-team dependency discovered

This step is NOT optional - always validate before marking complete.

Related
business-analyst
project-manager
Closing Reminders
IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
MUST ATTENTION apply critical thinking — every claim needs traced proof, confidence >80% to act. Anti-hallucination: never present guess as fact.
MUST ATTENTION apply AI mistake prevention — holistic-first debugging, fix at responsible layer, surface ambiguity before coding, re-read files after compaction.

[TASK-PLANNING] Before acting, analyze task scope and systematically break it into small todo tasks and sub-tasks using TaskCreate.

Weekly Installs
62
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass