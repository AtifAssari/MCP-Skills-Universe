---
title: bmad-document-project
url: https://skills.sh/bmad-code-org/bmad-method/bmad-document-project
---

# bmad-document-project

skills/bmad-code-org/bmad-method/bmad-document-project
bmad-document-project
Installation
$ npx skills add https://github.com/bmad-code-org/bmad-method --skill bmad-document-project
SKILL.md
Document Project Workflow

Goal: Document brownfield projects for AI context.

Your Role: Project documentation specialist.

Conventions
Bare paths (e.g. instructions.md) resolve from the skill root.
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

Use {user_name} for greeting
Use {communication_language} for all communications
Use {document_output_language} for output documents
Use {planning_artifacts} for output location and artifact scanning
Use {project_knowledge} for additional context scanning
Step 5: Greet the User

Greet {user_name} (if you have not already), speaking in {communication_language}.

Step 6: Execute Append Steps

Execute each entry in {workflow.activation_steps_append} in order.

Activation is complete. Begin the workflow below.

Execution

Read fully and follow: ./instructions.md

Weekly Installs
135
Repository
bmad-code-org/b…d-method
GitHub Stars
46.1K
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass