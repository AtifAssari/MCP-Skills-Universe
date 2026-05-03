---
title: cli-forge-scaffold
url: https://skills.sh/bytelandtechnology/cli-forge/cli-forge-scaffold
---

# cli-forge-scaffold

skills/bytelandtechnology/cli-forge/cli-forge-scaffold
cli-forge-scaffold
Installation
$ npx skills add https://github.com/bytelandtechnology/cli-forge --skill cli-forge-scaffold
SKILL.md
cli-forge Scaffold

Use this stage when the work is to create a brand-new Rust CLI Skill project from the baseline templates, and the detailed CLI contract (Plan) has already been explicitly defined and approved.

Purpose

Generate the baseline codebase for a new skill using the approved cli-plan.yml and the authoritative templates.

This stage does not make design decisions; it strictly follows the blueprint provided by the Plan stage.

Canonical References
./instructions/new.md
./planning-brief.md
./contracts/scaffold-receipt.yml.tpl
./templates/
Entry Gate
#	Check	Source
1	cli-plan.yml exists and is approved	Plan stage
2	skill_name is known	Plan stage
3	Target project directory DOES NOT exist	Filesystem
Required Inputs
skill_name
Approved cli-plan.yml
Optional author, version, rust_edition
Workflow
Run the pre-checks from ./instructions/new.md: require the skill name, verify cli-plan.yml, and refuse to overwrite an existing directory.
Create the directory structure.
Expand the templates from ./templates/ EXACTLY as defined by cli-plan.yml and the instruction file, restoring any install-safe dot-* resource alias to its intended dot-prefixed output path.
Verify that no {{token}} placeholders remain unresolved.
Run the required verification commands from the generated project root:
cargo build
cargo clippy -- -D warnings
cargo fmt --check
cargo test
Confirm the generated package layout stays within the documented boundary: baseline generated files plus feature-local support files. Repository-owned CI workflows and release scripts stay outside the generated project until Publish.
Generate .cli-forge/scaffold-receipt.yml using the template at ./contracts/scaffold-receipt.yml.tpl.
Outputs
A new Rust CLI package directory
.cli-forge/scaffold-receipt.yml
Exit Gate
#	Check
1	All templates expanded with no unresolved tokens
2	cargo build passes
3	cargo clippy -- -D warnings passes
4	cargo fmt --check passes
5	cargo test passes
6	scaffold-receipt.yml generated
Guardrails
Use templates EXCLUSIVELY from the bundled ./templates/ directory for this stage. Do not reach outside this skill package for scaffold templates.
Treat dot-* resource names inside ./templates/ as install-safe aliases only. Generated outputs must restore the intended dot-prefixed filename.
Do not improvise project structure or dependencies. Everything must be tied back to the cli-plan.yml.
The scaffold baseline generates a working one-shot CLI only. Optional capabilities (repl, stream, daemon) are not included in the baseline and must be added by the Extend stage (../cli-forge-extend/SKILL.md) after the baseline project is verified. If cli-plan.yml marks any capability as in_scope, proceed with baseline generation, record the deferred capabilities in scaffold-receipt.yml under deferred_capabilities, and inform the user which features require the Extend stage next.
If any Cargo verification step fails, block the workflow and fix the scaffolded files before handing the work forward.
Next Step

If scaffold-receipt.yml lists deferred capabilities, use AskUserQuestion to prompt before handing off. Offer to run extend immediately for each deferred capability. If the user confirms, invoke extend for each deferred capability in order. If the user declines, fall back to enumerating the exact /cli-forge-extend invocation for each (see instructions/new.md Capability Deferral). Otherwise, continue with ../cli-forge-validate/SKILL.md to run the full compliance rule set.

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