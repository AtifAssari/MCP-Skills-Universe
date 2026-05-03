---
rating: ⭐⭐⭐
title: cli-forge
url: https://skills.sh/bytelandtechnology/cli-forge/cli-forge
---

# cli-forge

skills/bytelandtechnology/cli-forge/cli-forge
cli-forge
Installation
$ npx skills add https://github.com/bytelandtechnology/cli-forge --skill cli-forge
SKILL.md
cli-forge Router

Use this parent skill as the stable entry point for the full cli-forge workflow.

This skill does not do any design, planning, or implementation work itself. Its job is to identify the current stage, recover the earliest incomplete phase from the repository state, assemble required inputs, and route work to the correct child skill.

Purpose

Act as the intake layer and traffic controller.

Classify requests into one of seven downstream stages: Design, Takeover, Plan, Scaffold, Extend, Validate, or Publish.
Check the current filesystem state (presence of directories, base files, validation reports).
Assemble inputs and generate the handoff.yml contract.
Resume interrupted workflows when the user provides partial context.
Canonical References
./contracts/handoff.yml.tpl
./planning-brief.md
Entry Gate
#	Check	Source
1	User request exists	User
Required Inputs
The user request (explicit or ambiguous)
Target directory path. CRITICAL: If the user does not provide the project path, you MUST actively search the workspace for .cli-forge/ directories to locate the active project. If the request appears to target a pre-existing Rust CLI project that has not yet adopted cli-forge, search for likely project roots such as Cargo.toml plus src/main.rs, or explicitly ask the user for the path. Do not assume the root directory is the target project.
Workflow
Read the user request and classify the expected outcome.
Inspect the filesystem to disambiguate the stage:
Missing target directory + new request -> Design
design-contract.yml exists but no cli-plan.yml -> Plan
Existing project with source files already present + missing .cli-forge/design-contract.yml -> Takeover
Existing project with source files already present + missing both .cli-forge/design-contract.yml and .cli-forge/cli-plan.yml -> Takeover
cli-plan.yml exists but no source files -> Scaffold
Existing project + feature request (stream or repl) + scaffold-compatible baseline -> Extend
Existing project + daemon capability request -> Plan
Existing project + audit request (or post-edit verification) -> Validate
Passed validation + release request (including npm publication) -> Publish
Confirm the required inputs for the chosen path:
Scaffold: skill_name
Takeover: project_path, post_adoption_objective, and takeover_mode
Extend: project_path and feature (stream or repl)
Plan: daemon capability requests, daemon contract changes, or daemon scope updates
Validate: project_path
Publish: publish_mode
Ensure the target project's .cli-forge/ directory exists before writing any router artifact. This first-write barrier also applies to first-adoption repositories that do not yet carry any pipeline files.
Use the template at contracts/handoff.yml.tpl to generate .cli-forge/handoff.yml in the target project directory. This explicitly records the classification and inputs for downstream consumption.
Provide a clear handoff response specifying which child skill should be invoked next. When there are 2 or 3 legal next-stage options, call the runtime's dialog-based chooser (e.g., AskUserQuestion) with those options (recommended path first) when it is available. If no dialog-based chooser is available, or if only one legal next stage remains, present a numbered text menu with 1 to 3 explicit next-stage options drawn only from the stages that remain valid under the current filesystem state. Use the smallest valid set, and when only one legal next stage exists, show a single 1. option for that stage. Put the recommended path first and add Other: explain a routing concern as an escape hatch. Accept only the exact digits that correspond to the numbered options actually shown, or Other: .... Do not auto-map plain-language replies onto numbered options. If a numeric reply includes additional text, or if an Other: reply asks for a stage that conflicts with the pipeline guardrails, ask for clarification and keep the handoff within the valid stage set. Do not require the user to type an exact phrase or skill name.
Outputs
.cli-forge/handoff.yml — The explicit routing contract
Exit Gate
#	Check
1	Request intent classified successfully
2	Required inputs for the downstream stage assembled
3	handoff.yml generated
4	Explicit handoff made to the correct child stage
Guardrails
CRITICAL DIRECTIVE TO THE ASSISTANT: You MUST NOT bypass the staged pipeline. Do not write, generate, or scaffold code yourself during this stage.
CRITICAL DIRECTIVE TO THE ASSISTANT: You MUST STOP and yield to the user after generating handoff.yml and explaining the next steps. Do not invoke the next stage autonomously. Use the runtime's dialog-based chooser (e.g., AskUserQuestion) for the handoff when it is available and there are 2 or 3 legal next-stage options. If no dialog-based chooser is available, or if only one legal next stage remains, use the standardized numbered text fallback with Other: explain a routing concern. Never require the user to explicitly type the next skill name, and never let fallback input bypass the valid stage set computed from repository state.
The Router must stay thin. Do not execute templates, run compilation steps, or define CLI contracts here.
Never force a workflow forward if an earlier stage is incomplete. For example, if the user asks to "validate" but the project is a pre-existing repository with no usable contract baseline, route to Takeover before Validate. If design-contract.yml already exists but cli-plan.yml does not, resume Plan instead of rebuilding contracts from implementation. If the user has an approved cli-plan.yml but no generated source tree yet, route to Scaffold.
If the user asks for a release but validation is missing or stale, route to Validate first.
If the user asks to add daemon support to an existing project, route to Plan first so the daemon capability contract can be updated explicitly. Do not send daemon requests to Extend until dedicated daemon implementation support exists there.
If an existing Rust CLI project with source files already present lacks a usable contract baseline, do not send it directly to Design, Scaffold, Extend, or Validate. Route it to Takeover only when the repository is missing .cli-forge/design-contract.yml, or when the user explicitly asks to refresh the adopted contracts, or when a downstream stage needs takeover baseline establishment because the contracts exist but no usable baseline receipt does. If design-contract.yml is already approved, preserve that Design -> Plan resume path instead of routing back through Takeover unless the user explicitly asked for takeover refresh or baseline establishment.
Do not route arbitrary takeover-adopted projects to Extend. Extend is only valid when the current project layout already matches the scaffold-compatible files that the feature templates patch directly.
Do not route new work to cli-forge-distribute. npm publication is part of Publish; the cli-forge-distribute module was archived in the daemon implementation commit and no longer exists.
If the target project directory is unknown, you MUST ask the user or search for .cli-forge/ folders. When takeover is likely, also search for probable Rust CLI project roots. Do not assume the current working directory applies.
Next Step

Route to one of:

../cli-forge-design/SKILL.md
../cli-forge-takeover/SKILL.md
../cli-forge-plan/SKILL.md
../cli-forge-scaffold/SKILL.md
../cli-forge-extend/SKILL.md
../cli-forge-validate/SKILL.md
../cli-forge-publish/SKILL.md
Weekly Installs
33
Repository
bytelandtechnol…li-forge
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass