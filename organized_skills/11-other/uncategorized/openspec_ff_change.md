---
rating: ⭐⭐
title: openspec-ff-change
url: https://skills.sh/pbh-btn/peerbanhelper/openspec-ff-change
---

# openspec-ff-change

skills/pbh-btn/peerbanhelper/openspec-ff-change
openspec-ff-change
Installation
$ npx skills add https://github.com/pbh-btn/peerbanhelper --skill openspec-ff-change
SKILL.md

Fast-forward through artifact creation - generate everything needed to start implementation in one go.

Input: The user's request should include a change name (kebab-case) OR a description of what they want to build.

Steps

If no clear input provided, ask what they want to build

Use the AskUserQuestion tool (open-ended, no preset options) to ask:

"What change do you want to work on? Describe what you want to build or fix."

From their description, derive a kebab-case name (e.g., "add user authentication" → add-user-auth).

IMPORTANT: Do NOT proceed without understanding what the user wants to build.

Create the change directory

openspec new change "<name>"


This creates a scaffolded change at openspec/changes/<name>/.

Get the artifact build order

openspec status --change "<name>" --json


Parse the JSON to get:

applyRequires: array of artifact IDs needed before implementation (e.g., ["tasks"])
artifacts: list of all artifacts with their status and dependencies

Create artifacts in sequence until apply-ready

Use the TodoWrite tool to track progress through the artifacts.

Loop through artifacts in dependency order (artifacts with no pending dependencies first):

a. For each artifact that is ready (dependencies satisfied):

Get instructions:
openspec instructions <artifact-id> --change "<name>" --json

The instructions JSON includes:
context: Project background (constraints for you - do NOT include in output)
rules: Artifact-specific rules (constraints for you - do NOT include in output)
template: The structure to use for your output file
instruction: Schema-specific guidance for this artifact type
outputPath: Where to write the artifact
dependencies: Completed artifacts to read for context
Read any completed dependency files for context
Create the artifact file using template as the structure
Apply context and rules as constraints - but do NOT copy them into the file
Show brief progress: "✓ Created "

b. Continue until all applyRequires artifacts are complete

After creating each artifact, re-run openspec status --change "<name>" --json
Check if every artifact ID in applyRequires has status: "done" in the artifacts array
Stop when all applyRequires artifacts are done

c. If an artifact requires user input (unclear context):

Use AskUserQuestion tool to clarify
Then continue with creation

Show final status

openspec status --change "<name>"


Output

After completing all artifacts, summarize:

Change name and location
List of artifacts created with brief descriptions
What's ready: "All artifacts created! Ready for implementation."
Prompt: "Run /opsx:apply or ask me to implement to start working on the tasks."

Artifact Creation Guidelines

Follow the instruction field from openspec instructions for each artifact type
The schema defines what each artifact should contain - follow it
Read dependency artifacts for context before creating new ones
Use template as the structure for your output file - fill in its sections
IMPORTANT: context and rules are constraints for YOU, not content for the file
Do NOT copy <context>, <rules>, <project_context> blocks into the artifact
These guide what you write, but should never appear in the output

Guardrails

Create ALL artifacts needed for implementation (as defined by schema's apply.requires)
Always read dependency artifacts before creating a new one
If context is critically unclear, ask the user - but prefer making reasonable decisions to keep momentum
If a change with that name already exists, suggest continuing that change instead
Verify each artifact file exists after writing before proceeding to next
Weekly Installs
27
Repository
pbh-btn/peerbanhelper
GitHub Stars
5.9K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass