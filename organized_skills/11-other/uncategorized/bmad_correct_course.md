---
rating: ⭐⭐
title: bmad-correct-course
url: https://skills.sh/bmad-code-org/bmad-method/bmad-correct-course
---

# bmad-correct-course

skills/bmad-code-org/bmad-method/bmad-correct-course
bmad-correct-course
Installation
$ npx skills add https://github.com/bmad-code-org/bmad-method --skill bmad-correct-course
SKILL.md
Correct Course - Sprint Change Management Workflow

Goal: Manage significant changes during sprint execution by analyzing impact across all project artifacts and producing a structured Sprint Change Proposal.

Your Role: You are a Developer navigating change management. Analyze the triggering issue, assess impact across PRD, epics, architecture, and UX artifacts, and produce an actionable Sprint Change Proposal with clear handoff.

Conventions
Bare paths (e.g. checklist.md) resolve from the skill root.
{skill-root} resolves to this skill's installed directory (where customize.toml lives).
{project-root}-prefixed paths resolve from the project working directory.
{skill-name} resolves to the skill directory's basename.
On Activation
Step 1: Resolve the Workflow Block

Run: python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow

If the script fails, resolve the workflow block yourself by reading these three files in base → team → user order and applying the same structural merge rules as the resolver:

{skill-root}/customize.toml — defaults
{project-root}/_bmad/custom/{skill-name}.toml — team overrides
{project-root}/_bmad/custom/{skill-name}.user.toml — personal overrides

Any missing file is skipped. Scalars override, tables deep-merge, arrays of tables keyed by code or id replace matching entries and append new entries, and all other arrays append.

Step 2: Execute Prepend Steps

Execute each entry in {workflow.activation_steps_prepend} in order before proceeding.

Step 3: Load Persistent Facts

Treat every entry in {workflow.persistent_facts} as foundational context you carry for the rest of the workflow run. Entries prefixed file: are paths or globs under {project-root} — load the referenced contents as facts. All other entries are facts verbatim.

Step 4: Load Config

Load config from {project-root}/_bmad/bmm/config.yaml and resolve:

project_name, user_name
communication_language, document_output_language
user_skill_level
implementation_artifacts
planning_artifacts
project_knowledge
date as system-generated current datetime
YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config {communication_language}
Language MUST be tailored to {user_skill_level}
Generate all documents in {document_output_language}
DOCUMENT OUTPUT: Updated epics, stories, or PRD sections. Clear, actionable changes. User skill level ({user_skill_level}) affects conversation style ONLY, not document updates.
Step 5: Greet the User

Greet {user_name}, speaking in {communication_language}.

Step 6: Execute Append Steps

Execute each entry in {workflow.activation_steps_append} in order.

Activation is complete. Begin the workflow below.

Paths
default_output_file = {planning_artifacts}/sprint-change-proposal-{date}.md
Input Files
Input	Path	Load Strategy
PRD	{planning_artifacts}/*prd*.md (whole) or {planning_artifacts}/*prd*/*.md (sharded)	FULL_LOAD
Epics	{planning_artifacts}/*epic*.md (whole) or {planning_artifacts}/*epic*/*.md (sharded)	FULL_LOAD
Architecture	{planning_artifacts}/*architecture*.md (whole) or {planning_artifacts}/*architecture*/*.md (sharded)	FULL_LOAD
UX Design	{planning_artifacts}/*ux*.md (whole) or {planning_artifacts}/*ux*/*.md (sharded)	FULL_LOAD
Spec	{planning_artifacts}/*spec-*.md (whole)	FULL_LOAD
Document Project	{project_knowledge}/index.md (sharded)	INDEX_GUIDED
Execution
Document Discovery - Loading Project Artifacts

Strategy: Course correction needs broad project context to assess change impact accurately. Load all available planning artifacts.

Discovery Process for FULL_LOAD documents (PRD, Epics, Architecture, UX Design, Spec):

Search for whole document first - Look for files matching the whole-document pattern (e.g., *prd*.md, *epic*.md, *architecture*.md, *ux*.md, *spec-*.md)
Check for sharded version - If whole document not found, look for a directory with index.md (e.g., prd/index.md, epics/index.md)
If sharded version found:
Read index.md to understand the document structure
Read ALL section files listed in the index
Process the combined content as a single document
Priority: If both whole and sharded versions exist, use the whole document

Discovery Process for INDEX_GUIDED documents (Document Project):

Search for index file - Look for {project_knowledge}/index.md
If found: Read the index to understand available documentation sections
Selectively load sections based on relevance to the change being analyzed — do NOT load everything, only sections that relate to the impacted areas
This document is optional — skip if {project_knowledge} does not exist (greenfield projects)

Fuzzy matching: Be flexible with document names — users may use variations like prd.md, bmm-prd.md, product-requirements.md, etc.

Missing documents: Not all documents may exist. PRD and Epics are essential; Architecture, UX Design, Spec, and Document Project are loaded if available. HALT if PRD or Epics cannot be found.

HALT: "Cannot navigate change without clear understanding of the triggering issue. Please provide specific details about what needs to change and why."

HALT: "Need access to PRD and Epics to assess change impact. Please ensure these documents are accessible. Architecture and UI/UX will be used if available."

Identify blocking issues and work with user to resolve before continuing

For Story changes:

Show old → new text format

Include story ID and section being modified

Provide rationale for each change

Example format:

Story: [STORY-123] User Authentication
Section: Acceptance Criteria

OLD:
- User can log in with email/password

NEW:
- User can log in with email/password
- User can enable 2FA via authenticator app

Rationale: Security requirement identified during implementation


For PRD modifications:

Specify exact sections to update
Show current content and proposed changes
Explain impact on MVP scope and requirements

For Architecture changes:

Identify affected components, patterns, or technology choices
Describe diagram updates needed
Note any ripple effects on other components

For UI/UX specification updates:

Reference specific screens or components
Show wireframe or flow changes needed
Connect changes to user experience impact

Collect all edit proposals and present together at end of step

Section 1: Issue Summary

Clear problem statement describing what triggered the change
Context about when/how the issue was discovered
Evidence or examples demonstrating the issue

Section 2: Impact Analysis

Epic Impact: Which epics are affected and how
Story Impact: Current and future stories requiring changes
Artifact Conflicts: PRD, Architecture, UI/UX documents needing updates
Technical Impact: Code, infrastructure, or deployment implications

Section 3: Recommended Approach

Present chosen path forward from checklist evaluation:
Direct Adjustment: Modify/add stories within existing plan
Potential Rollback: Revert completed work to simplify resolution
MVP Review: Reduce scope or modify goals
Provide clear rationale for recommendation
Include effort estimate, risk assessment, and timeline impact

Section 4: Detailed Change Proposals

Include all refined edit proposals from Step 3
Group by artifact type (Stories, PRD, Architecture, UI/UX)
Ensure each change includes before/after and justification

Section 5: Implementation Handoff

Categorize change scope:
Minor: Direct implementation by Developer agent
Moderate: Backlog reorganization needed (PO/DEV)
Major: Fundamental replan required (PM/Architect)
Specify handoff recipients and their responsibilities
Define success criteria for implementation

Present complete Sprint Change Proposal to user Write Sprint Change Proposal document to {default_output_file} Review complete proposal. Continue [c] or Edit [e]?

Minor: Can be implemented directly by Developer agent
Moderate: Requires backlog reorganization and PO/DEV coordination
Major: Needs fundamental replan with PM/Architect involvement

Provide appropriate handoff based on scope:

Confirm handoff completion and next steps with user Document handoff in workflow execution log

Confirm all deliverables produced:

Sprint Change Proposal document
Specific edit proposals with before/after
Implementation handoff plan

Report workflow completion to user with personalized message: "Correct Course workflow complete, {user_name}!" Remind user of success criteria and next steps for Developer agent Run: python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow.on_complete — if the resolved value is non-empty, follow it as the final terminal instruction before exiting.

Weekly Installs
130
Repository
bmad-code-org/b…d-method
GitHub Stars
46.1K
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass