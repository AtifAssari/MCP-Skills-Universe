---
rating: ⭐⭐
title: spec-driven-develop
url: https://skills.sh/zhu1090093659/spec_driven_develop/spec-driven-develop
---

# spec-driven-develop

skills/zhu1090093659/spec_driven_develop/spec-driven-develop
spec-driven-develop
Installation
$ npx skills add https://github.com/zhu1090093659/spec_driven_develop --skill spec-driven-develop
SKILL.md
Spec-Driven Develop

You are executing the Spec-Driven Development workflow — a standardized pre-development pipeline for large-scale complex tasks. Your job is to complete all preparation phases before any actual coding begins, ensuring the project has full analysis, a clear plan, trackable progress documents, and a task-specific SKILL.

Configuration
Path	Default Value	Purpose
Analysis output	docs/analysis/	Phase 1 analysis documents
Plan output	docs/plan/	Phase 3 planning documents
Progress output	docs/progress/	Phase 4 tracking documents (incl. MASTER.md)
Archive output	docs/archives/<project>/	Phase 7 archived artifacts
Sub-SKILL install	Project level (auto-detect)	Platform-specific: .cursor/skills/, .claude/commands/, or project-local

Templates for all generated documents are in references/templates/. Behavioral rules are in references/behavioral-rules.md. The parallel execution protocol is in references/parallel-protocol.md.

Before You Begin: Cross-Conversation Continuity Check

CRITICAL: Before starting any phase, check if docs/progress/MASTER.md already exists in the project.

If it exists: Read it immediately. You are resuming an in-progress task. Identify which phase you are in, what has been completed, and continue from the exact point where the previous conversation left off. Do NOT restart from Phase 0.
If it does not exist: This is a fresh start. Proceed to Phase 0.

After loading your current state from MASTER.md, populate the platform's native task tracking tool (e.g. TodoWrite) with the active phase's pending tasks. For each task, set content to the task description, status to "in-progress" for the currently active task and "todo" for the rest, and priority mapped as P0=high, P1=medium, P2=low. This gives the user real-time visual progress in their IDE. If no native task tool is available, skip this step — MASTER.md alone is sufficient.

Phase 0: Quick Intent Capture

Goal: Capture the user's high-level transformation direction in 1-2 sentences — just enough to give Phase 1 analysis a focus, without deep clarification.

Actions:

Extract the big-picture direction from the user's message:

The type of transformation (language migration, framework change, architecture overhaul, new feature development, etc.)
The rough target state (e.g., "rewrite in Rust", "migrate to microservices")
Any constraints or preferences the user explicitly mentioned

Summarize the direction back to the user in 1-2 sentences. Do NOT ask deep clarifying questions at this stage — the analysis in Phase 1 will reveal the project reality needed for informed questions. Simply confirm: "I understand you want to [direction]. Let me first analyze the current project so I can ask you the right questions."

If the user's intent is completely unclear (e.g., they said something vague like "improve this project"), ask ONE high-level question to determine the transformation type. Keep it brief.

Output: A preliminary direction statement that guides Phase 1's analysis focus. This is NOT the final task definition — that comes in Phase 2 after analysis.

Phase 1: Deep Project Analysis

Goal: Build a comprehensive understanding of the current codebase, informed by the preliminary direction from Phase 0.

Actions:

Launch project-analyzer sub-agents in parallel to analyze the codebase concurrently. Split the work by focus area:

Agent 1 — Architecture & Stack: Project structure, directory layout, technology stack, entry points, build/run commands
Agent 2 — Module Inventory: Each module's responsibility, public API surface, size, internal/external dependencies. Must evaluate each module against all five S.U.P.E.R principles (Single Purpose, Unidirectional Flow, Ports over Implementation, Environment-Agnostic, Replaceable Parts) and assign a per-principle compliance rating.
Agent 3 — Risks & S.U.P.E.R Health: Transformation risks, complexity hotspots, platform-specific code, coding conventions. Must produce a S.U.P.E.R Architecture Health Summary evaluating the overall codebase against each principle, identifying violation hotspots that become priority targets in the transformation plan.

Provide each agent with the preliminary direction from Phase 0 AND references/super-philosophy.md so they can assess findings against S.U.P.E.R principles in context of the intended transformation.

If sub-agents are not available on the current platform, perform the analysis sequentially yourself — the scope is the same either way.

Consolidate agent outputs and resolve any contradictions or gaps. Write analysis documents to docs/analysis/ using the templates in references/templates/analysis.md:

project-overview.md — Architecture, tech stack, entry points, build system
module-inventory.md — Every module with: responsibility, dependencies, size, complexity rating, S.U.P.E.R compliance score per module
risk-assessment.md — Technical risks, compatibility risks, complexity hotspots, S.U.P.E.R Architecture Health Summary with violation hotspots

Output: Complete docs/analysis/ directory with three documents. The S.U.P.E.R assessment serves as the architectural baseline for all subsequent phases.

Phase 2: Intent Refinement & Confirmation

Goal: With the project fully analyzed, engage the user in a grounded, high-quality discussion to finalize the task definition. The analysis from Phase 1 enables asking precise, informed questions that would have been impossible before understanding the codebase.

Actions:

Present key findings from Phase 1 as context for the discussion:

Brief architecture summary (how the project is structured today)
Notable S.U.P.E.R health issues (violation hotspots, architectural risks)
Module coupling and complexity highlights relevant to the intended transformation

Ask the user targeted clarifying questions grounded in the analysis. These should be specific and informed, not generic. Examples of the quality expected:

"Module A and Module B are tightly coupled with circular dependencies. Do you want to decouple them as part of this migration, or preserve the current structure?"
"The risk assessment shows 3 modules with hardcoded environment assumptions. Should we fix these (aligning with S.U.P.E.R E principle) or defer that to a separate task?"
"The current codebase has no interface contracts between modules. Do you want to introduce schema-defined boundaries (S.U.P.E.R P principle) during this transformation?"

At minimum, confirm:

Scope: Which parts of the project are in scope? Reference specific modules from the inventory.
Target: Confirm the target technology/architecture/state, now informed by current architecture reality.
Constraints: Hard constraints (timeline, backward compatibility, specific libraries, deployment targets)?
Priorities: What matters most — performance, maintainability, feature parity, or something else? Reference the risk assessment to help the user prioritize.
S.U.P.E.R priorities: Which architectural violations should be fixed during this transformation vs. deferred?

Summarize the refined understanding back to the user and get explicit confirmation before proceeding.

Output: A clear, confirmed task definition grounded in project reality. This is the authoritative task definition that guides all subsequent phases (Phase 3-7).

Phase 3: Task Decomposition

Goal: Break down the transformation into manageable, trackable tasks organized in phases, with explicit parallel execution lanes.

Actions:

Launch task-architect sub-agents with the full analysis output from Phase 1 AND the confirmed task definition from Phase 2 — including the S.U.P.E.R health assessment from risk-assessment.md. If the project is large enough to warrant multiple strategies, launch 2 agents exploring different decomposition approaches (e.g., bottom-up vs. strangler fig) and pick the better result.

If sub-agents are not available, perform the decomposition yourself.

The decomposition must produce:

Phased approach with natural phase boundaries, ordered by dependency. Early phases should prioritize fixing S.U.P.E.R violation hotspots identified in Phase 1, establishing clean architecture foundations before building new features.
Concrete tasks for each phase, each with: description, priority (P0/P1/P2), effort (S/M/L/XL), dependencies, S.U.P.E.R design drivers (which principles are most relevant), acceptance criteria. Every task's acceptance criteria implicitly includes passing the S.U.P.E.R Quick Check for its listed principles.
Parallel execution lanes: For each phase, group tasks that have no mutual dependencies into lanes that can run simultaneously. Assess merge risk (file overlap) between lanes.
Dependency graph as a Mermaid diagram — use subgraphs to visualize parallel lanes
Milestones at natural phase boundaries

Write planning documents to docs/plan/ using the templates in references/templates/plan.md:

task-breakdown.md — All phases and tasks with full detail, including parallel lane assignments and S.U.P.E.R design constraints
dependency-graph.md — Mermaid diagram showing task/phase dependencies and parallel lanes
milestones.md — Milestone definitions with target criteria

Output: Complete docs/plan/ directory with three documents. Every task is annotated with its S.U.P.E.R design drivers.

Phase 4: Progress Tracking Documentation

Goal: Create a document-driven progress tracking system that survives across conversations.

Actions:

Use the templates in references/templates/progress.md for all progress documents.

Create the master control file docs/progress/MASTER.md with:

Task name and description (from Phase 2)
Link to each analysis document
Link to each plan document
A summary table of all phases with completion percentage
Links to each phase's detailed progress file
A "Current Status" section indicating which phase/task is active
A "Next Steps" section for the agent to quickly orient itself

Create one detailed progress file per phase: docs/progress/phase-N-<short-name>.md

Each file contains the phase's tasks as checkbox items: - [ ] Task description
Include acceptance criteria inline for each task
Include a "Notes" section for recording decisions, blockers, and context

The MASTER.md format must follow this convention:

Phases use the format: - [ ] Phase N: <name> (0/X tasks) [details](./phase-N-<name>.md)
When a phase is fully done: - [x] Phase N: <name> (X/X tasks) [details](./phase-N-<name>.md)
The "Current Status" section is updated by the agent at the start and end of each work session

Output: Complete docs/progress/ directory with MASTER.md and per-phase detail files.

Phase 5: Task-Specific Sub-SKILL Generation

Goal: Create a project-level SKILL tailored to this specific task, encoding the interaction patterns and development standards needed for the actual implementation work.

Actions:

The sub-SKILL is always installed at project level (e.g., .cursor/skills/, .claude/commands/, or project-local directory). Do not ask the user for installation location. This keeps the sub-SKILL co-located with the project it serves and avoids polluting the global skill space.

Determine what the sub-SKILL should contain (see references/templates/sub-skill.md for the full content outline):

S.U.P.E.R architecture principles — MUST be inlined verbatim, not merely referenced. The executing agent may not have access to references/super-philosophy.md, so the full five principles with litmus tests must be embedded directly in the sub-SKILL body. This is the #1 most important section.
S.U.P.E.R Code Review Checklist — a 10-point checklist that the agent must run after completing every task, before marking it as done. Include the scoring rule: all pass = proceed, 1-2 fail = fix first, 3+ fail = stop and refactor.
Task-specific coding standards and conventions for the target technology, framed through S.U.P.E.R principles (e.g., error handling aligned with U, dependency injection aligned with P, config management aligned with E)
The cross-conversation continuity protocol (read MASTER.md first)
Project-specific architecture context, including the S.U.P.E.R violation hotspots from docs/analysis/risk-assessment.md that must be addressed
Guidance on how to update progress documents after completing each task
Phase-specific instructions relevant to the transformation type
Parallel execution protocol: reference references/parallel-protocol.md for the full protocol
The archive trigger: when all tasks are done, initiate Phase 7

Delegate creation to the platform's native skill-creator:

On Claude Code or Codex: Invoke the platform's built-in skill-creator skill, providing it with the task context, the desired skill name, description, and content outline. Let the native tool handle the actual file generation and installation.
On Cursor: If a skill-creator skill is available, use it. Otherwise, create the SKILL.md directly following the standard frontmatter + markdown format and place it in the project's skills directory.

The generated sub-SKILL should instruct the agent to:

Always read docs/progress/MASTER.md at the start of every conversation
Run the S.U.P.E.R Code Review Checklist after completing each task, before marking it done
Update the checkbox status in the relevant phase file after completing each task
Update the completion count and "Current Status" in MASTER.md
When all checkboxes are checked, trigger Phase 7 (Archive)

Output: A project-level task-specific SKILL.

Phase 6: Handoff & Summary

Goal: Present all preparation artifacts to the user and confirm readiness to begin development.

Actions:

Present a structured summary to the user:

Task definition (from Phase 2)
Key findings from analysis (high-level, from Phase 1)
Phased plan overview with task counts (from Phase 3)
Progress tracking system description (from Phase 4)
Sub-SKILL name and installation location (from Phase 5)

List all generated artifacts:

docs/analysis/project-overview.md
docs/analysis/module-inventory.md
docs/analysis/risk-assessment.md
docs/plan/task-breakdown.md
docs/plan/dependency-graph.md
docs/plan/milestones.md
docs/progress/MASTER.md
docs/progress/phase-N-*.md (one per phase)
The generated sub-SKILL

Ask the user: "All preparation is complete. Ready to begin Phase 1 development?"

Output: User confirmation to proceed with actual implementation.

Phase 7: Archive

Trigger: This phase activates when ALL checkboxes in docs/progress/MASTER.md are marked complete ([x]).

Goal: Archive all workflow artifacts for future reference and traceability, then clean up the working directories.

Actions:

Announce to the user that all tasks have been completed. Congratulate them.

Determine the archive directory name from the task name established in Phase 2. Sanitize it for use as a directory name (lowercase, hyphens instead of spaces, no special characters). The archive path is: docs/archives/<project-name>/. See references/templates/archive.md for the target directory structure and index template.

Create the archive directory structure and move all artifacts into it:

Move docs/analysis/ to docs/archives/<project-name>/analysis/
Move docs/plan/ to docs/archives/<project-name>/plan/
Move docs/progress/ to docs/archives/<project-name>/progress/
Move the project-level sub-SKILL file to docs/archives/<project-name>/skill/SKILL.md
Move any other temporary files generated during development into the archive

Create or update the archive index file docs/archives/README.md:

If the file does not exist, create it with a header and the first project entry
If it already exists, append a new entry for this project
Each entry should include: project name, one-line description, date range (started — completed), and a link to the archived MASTER.md

After archiving, remove the now-empty docs/analysis/, docs/plan/, and docs/progress/ directories from the project root's docs/ folder, and remove the sub-SKILL's original directory if it is now empty. Only docs/archives/ should remain under docs/.

Suggest to the user that they might want to commit the archive to version control.

Output: All artifacts preserved under docs/archives/<project-name>/, with an updated index at docs/archives/README.md.

Behavioral Rules

All rules in references/behavioral-rules.md apply to every phase. Read and follow them.

Weekly Installs
8
Repository
zhu1090093659/s…_develop
GitHub Stars
701
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass