---
title: bmad-sprint-status
url: https://skills.sh/bmad-code-org/bmad-method/bmad-sprint-status
---

# bmad-sprint-status

skills/bmad-code-org/bmad-method/bmad-sprint-status
bmad-sprint-status
Installation
$ npx skills add https://github.com/bmad-code-org/bmad-method --skill bmad-sprint-status
SKILL.md
Sprint Status Workflow

Goal: Summarize sprint status, surface risks, and recommend the next workflow action.

Your Role: You are a Developer providing clear, actionable sprint visibility. No time estimates — focus on status, risks, and next steps.

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
implementation_artifacts
date as system-generated current datetime
YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config {communication_language}
Step 5: Greet the User

Greet {user_name}, speaking in {communication_language}.

Step 6: Execute Append Steps

Execute each entry in {workflow.activation_steps_append} in order.

Activation is complete. Begin the workflow below.

Paths
sprint_status_file = {implementation_artifacts}/sprint-status.yaml
Input Files
Input	Path	Load Strategy
Sprint status	{sprint_status_file}	FULL_LOAD
Execution

Validate all statuses against known values:

Valid story statuses: backlog, ready-for-dev, in-progress, review, done, drafted (legacy)

Valid epic statuses: backlog, in-progress, done, contexted (legacy)

Valid retrospective statuses: optional, done

Unknown status detected: {{#each invalid_entries}}

{{key}}: "{{status}}" (not recognized) {{/each}}

Valid statuses:

Stories: backlog, ready-for-dev, in-progress, review, done
Epics: backlog, in-progress, done
Retrospectives: optional, done How should these be corrected? {{#each invalid_entries}} {{@index}}. {{key}}: "{{status}}" → [select valid status] {{/each}}

Enter corrections (e.g., "1=in-progress, 2=backlog") or "skip" to continue without fixing: Update sprint-status.yaml with corrected values Re-parse the file with corrected statuses

Detect risks:

IF any story has status "review": suggest /bmad:bmm:workflows:code-review
IF any story has status "in-progress" AND no stories have status "ready-for-dev": recommend staying focused on active story
IF all epics have status "backlog" AND no stories have status "ready-for-dev": prompt /bmad:bmm:workflows:create-story
IF last_updated timestamp is more than 7 days old (or last_updated is missing, fall back to generated): warn "sprint-status.yaml may be stale"
IF any story key doesn't match an epic pattern (e.g., story "5-1-..." but no "epic-5"): warn "orphaned story detected"
IF any epic has status in-progress but has no associated stories: warn "in-progress epic has no stories"
Project: {{project}} ({{project_key}})
Tracking: {{tracking_system}}
Status file: {sprint_status_file}

Stories: backlog {{count_backlog}}, ready-for-dev {{count_ready}}, in-progress {{count_in_progress}}, review {{count_review}}, done {{count_done}}

Epics: backlog {{epic_backlog}}, in-progress {{epic_in_progress}}, done {{epic_done}}

Next Recommendation: /bmad:bmm:workflows:{{next_workflow_id}} ({{next_story_id}})

{{#if risks}} Risks: {{#each risks}}

{{this}} {{/each}} {{/if}}

Read and parse {sprint_status_file}

Validate required metadata fields exist: generated, project, project_key, tracking_system, story_location (last_updated is optional for backward compatibility) is_valid = false error = "Missing required field(s): {{missing_fields}}" suggestion = "Re-run sprint-planning or add missing fields manually" Return

Verify development_status section exists with at least one entry is_valid = false error = "development_status missing or empty" suggestion = "Re-run sprint-planning or repair the file manually" Return

Validate all status values against known valid statuses:

Stories: backlog, ready-for-dev, in-progress, review, done (legacy: drafted)
Epics: backlog, in-progress, done (legacy: contexted)
Retrospectives: optional, done is_valid = false error = "Invalid status values: {{invalid_entries}}" suggestion = "Fix invalid statuses in sprint-status.yaml" Return

is_valid = true message = "sprint-status.yaml valid: metadata complete, all statuses recognized" Run: python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow.on_complete — if the resolved value is non-empty, follow it as the final terminal instruction before exiting.

Weekly Installs
131
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