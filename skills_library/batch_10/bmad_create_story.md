---
title: bmad-create-story
url: https://skills.sh/bmad-code-org/bmad-method/bmad-create-story
---

# bmad-create-story

skills/bmad-code-org/bmad-method/bmad-create-story
bmad-create-story
Installation
$ npx skills add https://github.com/bmad-code-org/bmad-method --skill bmad-create-story
SKILL.md
Create Story Workflow

Goal: Create a comprehensive story file that gives the dev agent everything needed for flawless implementation.

Your Role: Story context engine that prevents LLM developer mistakes, omissions, or disasters.

Communicate all responses in {communication_language} and generate all documents in {document_output_language}
Your purpose is NOT to copy from epics - it's to create a comprehensive, optimized story file that gives the DEV agent EVERYTHING needed for flawless implementation
COMMON LLM MISTAKES TO PREVENT: reinventing wheels, wrong libraries, wrong file locations, breaking regressions, ignoring UX, vague implementations, lying about completion, not learning from past work
EXHAUSTIVE ANALYSIS REQUIRED: You must thoroughly analyze ALL artifacts to extract critical context - do NOT be lazy or skim! This is the most important function in the entire development process!
UTILIZE SUBPROCESSES AND SUBAGENTS: Use research subagents, subprocesses or parallel processing if available to thoroughly analyze different artifacts simultaneously and thoroughly
SAVE QUESTIONS: If you think of questions or clarifications during analysis, save them for the end after the complete story is written
ZERO USER INTERVENTION: Process should be fully automated except for initial epic/story selection or missing documents
Conventions
Bare paths (e.g. discover-inputs.md) resolve from the skill root.
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
planning_artifacts, implementation_artifacts
date as system-generated current datetime
Step 5: Greet the User

Greet {user_name}, speaking in {communication_language}.

Step 6: Execute Append Steps

Execute each entry in {workflow.activation_steps_append} in order.

Activation is complete. Begin the workflow below.

Paths
sprint_status = {implementation_artifacts}/sprint-status.yaml
epics_file = {planning_artifacts}/epics.md
prd_file = {planning_artifacts}/prd.md
architecture_file = {planning_artifacts}/architecture.md
ux_file = {planning_artifacts}/*ux*.md
story_title = "" (will be elicited if not derivable)
default_output_file = {implementation_artifacts}/{{story_key}}.md
Input Files
Input	Description	Path Pattern(s)	Load Strategy
prd	PRD (fallback - epics file should have most content)	whole: {planning_artifacts}/*prd*.md, sharded: {planning_artifacts}/*prd*/*.md	SELECTIVE_LOAD
architecture	Architecture (fallback - epics file should have relevant sections)	whole: {planning_artifacts}/*architecture*.md, sharded: {planning_artifacts}/*architecture*/*.md	SELECTIVE_LOAD
ux	UX design (fallback - epics file should have relevant sections)	whole: {planning_artifacts}/*ux*.md, sharded: {planning_artifacts}/*ux*/*.md	SELECTIVE_LOAD
epics	Enhanced epics+stories file with BDD and source hints	whole: {planning_artifacts}/*epic*.md, sharded: {planning_artifacts}/*epic*/*.md	SELECTIVE_LOAD
Execution

Check if {{sprint_status}} file exists for auto discover 🚫 No sprint status file found and no story specified Required Options: 1. Run sprint-planning to initialize sprint tracking (recommended) 2. Provide specific epic-story number to create (e.g., "1-2-user-auth") 3. Provide path to story documents if sprint status doesn't exist yet Choose option [1], provide epic-story number, path to story docs, or [q] to quit:

<check if="user chooses 'q'">
  <action>HALT - No work needed</action>
</check>

<check if="user chooses '1'">
  <output>Run sprint-planning workflow first to create sprint-status.yaml</output>
  <action>HALT - User needs to run sprint-planning</action>
</check>

<check if="user provides epic-story number">
  <action>Parse user input: extract epic_num, story_num, story_title</action>
  <action>Set {{epic_num}}, {{story_num}}, {{story_key}} from user input</action>
  <action>GOTO step 2a</action>
</check>

<check if="user provides story docs path">
  <action>Use user-provided path for story documents</action>
  <action>GOTO step 2a</action>
</check>

<action>Find the FIRST story (by reading in order from top to bottom) where:
  - Key matches pattern: number-number-name (e.g., "1-2-user-auth")
  - NOT an epic key (epic-X) or retrospective (epic-X-retrospective)
  - Status value equals "backlog"
</action>

<check if="no backlog story found">
  <output>📋 No backlog stories found in sprint-status.yaml

    All stories are either already created, in progress, or done.

    **Options:**
    1. Run sprint-planning to refresh story tracking
    2. Load PM agent and run correct-course to add more stories
    3. Check if current sprint is complete and run retrospective
  </output>
  <action>HALT</action>
</check>

<action>Extract from found story key (e.g., "1-2-user-authentication"):
  - epic_num: first number before dash (e.g., "1")
  - story_num: second number after first dash (e.g., "2")
  - story_title: remainder after second dash (e.g., "user-authentication")
</action>
<action>Set {{story_id}} = "{{epic_num}}.{{story_num}}"</action>
<action>Store story_key for later use (e.g., "1-2-user-authentication")</action>

<!-- Mark epic as in-progress if this is first story -->
<action>Check if this is the first story in epic {{epic_num}} by looking for {{epic_num}}-1-* pattern</action>
<check if="this is first story in epic {{epic_num}}">
  <action>Load {{sprint_status}} and check epic-{{epic_num}} status</action>
  <action>If epic status is "backlog" → update to "in-progress"</action>
  <action>If epic status is "contexted" (legacy status) → update to "in-progress" (backward compatibility)</action>
  <action>If epic status is "in-progress" → no change needed</action>
  <check if="epic status is 'done'">
    <output>🚫 ERROR: Cannot create story in completed epic</output>
    <output>Epic {{epic_num}} is marked as 'done'. All stories are complete.</output>
    <output>If you need to add more work, either:</output>
    <output>1. Manually change epic status back to 'in-progress' in sprint-status.yaml</output>
    <output>2. Create a new epic for additional work</output>
    <action>HALT - Cannot proceed</action>
  </check>
  <check if="epic status is not one of: backlog, contexted, in-progress, done">
    <output>🚫 ERROR: Invalid epic status '{{epic_status}}'</output>
    <output>Epic {{epic_num}} has invalid status. Expected: backlog, in-progress, or done</output>
    <output>Please fix sprint-status.yaml manually or run sprint-planning to regenerate</output>
    <action>HALT - Cannot proceed</action>
  </check>
  <output>📊 Epic {{epic_num}} status updated to in-progress</output>
</check>

<action>GOTO step 2a</action>


Find the FIRST story (by reading in order from top to bottom) where: - Key matches pattern: number-number-name (e.g., "1-2-user-auth") - NOT an epic key (epic-X) or retrospective (epic-X-retrospective) - Status value equals "backlog"

  All stories are either already created, in progress, or done.

  **Options:**
  1. Run sprint-planning to refresh story tracking
  2. Load PM agent and run correct-course to add more stories
  3. Check if current sprint is complete and run retrospective
</output>
<action>HALT</action>


Extract from found story key (e.g., "1-2-user-authentication"): - epic_num: first number before dash (e.g., "1") - story_num: second number after first dash (e.g., "2") - story_title: remainder after second dash (e.g., "user-authentication") Set {{story_id}} = "{{epic_num}}.{{story_num}}" Store story_key for later use (e.g., "1-2-user-authentication")

Check if this is the first story in epic {{epic_num}} by looking for {{epic_num}}-1-* pattern Load {{sprint_status}} and check epic-{{epic_num}} status If epic status is "backlog" → update to "in-progress" If epic status is "contexted" (legacy status) → update to "in-progress" (backward compatibility) If epic status is "in-progress" → no change needed ERROR: Cannot create story in completed epic Epic {{epic_num}} is marked as 'done'. All stories are complete. If you need to add more work, either: 1. Manually change epic status back to 'in-progress' in sprint-status.yaml 2. Create a new epic for additional work HALT - Cannot proceed ERROR: Invalid epic status '{{epic_status}}' Epic {{epic_num}} has invalid status. Expected: backlog, in-progress, or done Please fix sprint-status.yaml manually or run sprint-planning to regenerate HALT - Cannot proceed Epic {{epic_num}} status updated to in-progress

GOTO step 2a

Read fully and follow ./discover-inputs.md to load all input files Available content: {epics_content}, {prd_content}, {architecture_content}, {ux_content}, plus the project-context facts loaded during activation via persistent_facts.

From {epics_content}, extract Epic {{epic_num}} complete context: EPIC ANALYSIS: - Epic objectives and business value - ALL stories in this epic for cross-story context - Our specific story's requirements, user story statement, acceptance criteria - Technical requirements and constraints - Dependencies on other stories/epics - Source hints pointing to original documents Extract our story ({{epic_num}}-{{story_num}}) details: STORY FOUNDATION: - User story statement (As a, I want, so that) - Detailed acceptance criteria (already BDD formatted) - Technical requirements specific to this story - Business context and value - Success criteria Find {{previous_story_num}}: scan {implementation_artifacts} for the story file in epic {{epic_num}} with the highest story number less than {{story_num}} Load previous story file: {implementation_artifacts}/{{epic_num}}-{{previous_story_num}}-*.md PREVIOUS STORY INTELLIGENCE: - Dev notes and learnings from previous story - Review feedback and corrections needed - Files that were created/modified and their patterns - Testing approaches that worked/didn't work - Problems encountered and solutions found - Code patterns established Extract all learnings that could impact current story implementation

Get last 5 commit titles to understand recent work patterns Analyze 1-5 most recent commits for relevance to current story: - Files created/modified - Code patterns and conventions used - Library dependencies added/changed - Architecture decisions implemented - Testing approaches used Extract actionable insights for current story implementation

📂 READ FILES BEING MODIFIED — skipping this is the primary cause of implementation failures and review cycles From the architecture directory structure, identify every file marked UPDATE (not NEW) that this story will touch Read each relevant UPDATE file completely. For each one, document in dev notes: - Current state: what it does today (state machine, API calls, data shapes, existing behaviors) - What this story changes: the specific sections or behaviors being modified - What must be preserved: existing interactions and behaviors the story must not break A story implementation must leave the system working end-to-end — not just satisfy its stated ACs. If a behavior is required for the feature to work correctly in the existing system, it is a requirement whether or not it is explicitly written in the story. The dev agent owns this.

From architecture analysis, identify specific libraries, APIs, or frameworks For each critical technology, research latest stable version and key changes: - Latest API documentation and breaking changes - Security vulnerabilities or updates - Performance improvements or deprecations - Best practices for current version EXTERNAL CONTEXT INCLUSION: Include in story any critical latest information the developer needs: - Specific library versions and why chosen - API endpoints with parameters and authentication - Recent security patches or considerations - Performance optimization techniques - Migration considerations if upgrading

Initialize from template.md: {default_output_file} story_header

story_requirements

previous_story_intelligence

git_intelligence_summary

project_context_reference

Set story Status to: "ready-for-dev" Add completion note: "Ultimate context engine analysis completed - comprehensive developer guide created"

Report completion 🎯 ULTIMATE BMad Method STORY CONTEXT CREATED, {user_name}!

**Story Details:**
- Story ID: {{story_id}}
- Story Key: {{story_key}}
- File: {{story_file}}
- Status: ready-for-dev

**Next Steps:**
1. Review the comprehensive story in {{story_file}}
2. Run dev agents `dev-story` for optimized implementation
3. Run `code-review` when complete (auto-marks done)
4. Optional: If Test Architect module installed, run `/bmad:tea:automate` after `dev-story` to generate guardrail tests

**The developer now has everything needed for flawless implementation!**

Weekly Installs
140
Repository
bmad-code-org/b…d-method
GitHub Stars
46.1K
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn