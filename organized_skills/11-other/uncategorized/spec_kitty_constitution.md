---
rating: ⭐⭐
title: spec-kitty-constitution
url: https://skills.sh/richfrem/agent-plugins-skills/spec-kitty-constitution
---

# spec-kitty-constitution

skills/richfrem/agent-plugins-skills/spec-kitty-constitution
spec-kitty-constitution
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill spec-kitty-constitution
SKILL.md
🔗 Workflow Provenance

Source: This skill augments the baseline workflow located at ./workflows/spec-kitty.constitution.md. It acts as an intelligent wrapper that is continuously improved with each execution.

/spec-kitty.constitution - Interview + Compile Constitution
User Input
$ARGUMENTS


You MUST consider the user input before proceeding (if not empty).

In repos with multiple features, always pass --feature <slug> to every spec-kitty command.

Command Contract

This command delegates constitution work to the CLI constitution workflow. Do not hand-author long governance content in chat unless the user explicitly asks for manual drafting.

Output location
Constitution markdown: .kittify/constitution/constitution.md
Interview answers: .kittify/constitution/interview/answers.yaml
Reference manifest: .kittify/constitution/references.yaml
Local reference docs: .kittify/constitution/library/*.md
Execution Paths
Path A: Deterministic minimal setup (fast)

Use when user wants speed, defaults, or bootstrap:

spec-kitty constitution interview --defaults --profile minimal --json
spec-kitty constitution generate --from-interview --json

Path B: Interactive interview (full)

Use when the user wants project-specific policy capture:

spec-kitty constitution interview --profile comprehensive
spec-kitty constitution generate --from-interview

Editing Rules
To revise policy inputs, rerun constitution interview (or edit answers.yaml) and regenerate.
Use --force with generate if the constitution already exists and must be replaced.
Keep constitution concise; full detail belongs in reference docs listed in references.yaml.
Validation + Status

After generation, verify status:

spec-kitty constitution status --json

Context Bootstrap Requirement

After constitution generation, first-run lifecycle actions should load context explicitly:

spec-kitty constitution context --action specify --json
spec-kitty constitution context --action plan --json
spec-kitty constitution context --action implement --json
spec-kitty constitution context --action review --json


Use JSON text as governance context. If mode=bootstrap, follow referenced docs as needed.

Weekly Installs
23
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass