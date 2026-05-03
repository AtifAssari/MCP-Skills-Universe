---
title: github-actions-generator
url: https://skills.sh/akin-ozer/cc-devops-skills/github-actions-generator
---

# github-actions-generator

skills/akin-ozer/cc-devops-skills/github-actions-generator
github-actions-generator
Installation
$ npx skills add https://github.com/akin-ozer/cc-devops-skills --skill github-actions-generator
SKILL.md
GitHub Actions Generator

Generate production-ready GitHub Actions workflows and custom actions following current best practices, security standards, and naming conventions. All generated resources are automatically validated using the devops-skills:github-actions-validator skill.

Quick Reference
Capability	When to Use	Reference
Workflows	CI/CD, automation, testing	references/best-practices.md
Composite Actions	Reusable step combinations	references/custom-actions.md
Docker Actions	Custom environments/tools	references/custom-actions.md
JavaScript Actions	API interactions, complex logic	references/custom-actions.md
Reusable Workflows	Shared patterns across repos	references/advanced-triggers.md
Security Scanning	Dependency review, SBOM	references/best-practices.md
Modern Features	Summaries, environments	references/modern-features.md
Trigger Decision Tree

Route every request through this decision tree before reading references or generating files:

If the user asks for .github/workflows/*.yml CI/CD automation, choose Workflow Generation.
If the user asks for action.yml or a reusable step package, choose Custom Action Generation.
If the user asks for workflow_call or shared pipelines across repositories, choose Reusable Workflow Generation.
If the request includes security-only scanning (dependency review, SBOM, CodeQL), stay on Workflow Generation with the security pattern.
If intent is ambiguous, ask one disambiguation question: "Do you want a workflow, a custom action, or a reusable workflow?"
Progressive Disclosure Route

Load only what is needed for the selected route, in this order:

Route	Load First (required)	Load Next (only if needed)	Primary Template
Workflow Generation	references/best-practices.md	references/common-actions.md, references/expressions-and-contexts.md, references/modern-features.md	assets/templates/workflow/basic_workflow.yml
Custom Action Generation	references/custom-actions.md	references/best-practices.md	assets/templates/action/composite/action.yml, assets/templates/action/docker/, assets/templates/action/javascript/
Reusable Workflow Generation	references/advanced-triggers.md	references/best-practices.md, references/common-actions.md	assets/templates/workflow/reusable_workflow.yml

If a required reference/template is unavailable, continue with the closest available reference and report the fallback explicitly in output.

Core Capabilities
1. Generate Workflows

Triggers: "Create a workflow for...", "Build a CI/CD pipeline..."

Process:

Understand requirements (triggers, runners, dependencies)
Define trust boundaries (internal branches vs fork PRs vs external triggers)
Set default permissions to read-only, then elevate only per job when required
Reference references/best-practices.md for patterns
Reference references/common-actions.md for action versions
Generate workflow with:
Semantic names, pinned actions (SHA), explicit permissions
Concurrency controls, caching, matrix strategies
Fork-safe PR handling (no secrets in untrusted contexts)
Validate with devops-skills:github-actions-validator skill
Fix issues and re-validate if needed

Minimal Example:

name: CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
      - uses: actions/setup-node@6044e13b5dc448c55e2357c09f80417699197238 # v6.2.0
        with:
          node-version: '24'
          cache: 'npm'
      - run: npm ci
      - run: npm test


Untrusted PR Guardrail (required for secret-using jobs):

jobs:
  deploy:
    if: github.event_name != 'pull_request' || github.event.pull_request.head.repo.full_name == github.repository

2. Generate Custom Actions

Triggers: "Create a composite action...", "Build a Docker action...", "Create a JavaScript action..."

Types:

Composite: Combine multiple steps → Fast startup
Docker: Custom environment/tools → Isolated
JavaScript: API access, complex logic → Fastest

Process:

Use templates from assets/templates/action/
Follow structure in references/custom-actions.md
Include branding, inputs/outputs, documentation
Validate with devops-skills:github-actions-validator skill

See references/custom-actions.md for:

Action metadata and branding
Directory structure patterns
Versioning and release workflows
3. Generate Reusable Workflows

Triggers: "Create a reusable workflow...", "Make this workflow callable..."

Key Elements:

workflow_call trigger with typed inputs
Explicit secrets (avoid secrets: inherit)
Explicit trusted-caller expectations (document org/repo boundaries)
Outputs mapped from job outputs
Minimal permissions
on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
    secrets:
      deploy-token:
        required: false
    outputs:
      result:
        value: ${{ jobs.build.outputs.result }}


When secrets are required, pass only the exact secret names needed and prefer environment protection rules for deployment stages.

See references/advanced-triggers.md for complete patterns.

4. Generate Security Workflows

Triggers: "Add security scanning...", "Add dependency review...", "Generate SBOM..."

Components:

Dependency Review: actions/dependency-review-action@v4
SBOM Attestations: actions/attest-sbom@v2
CodeQL Analysis: github/codeql-action

Permission Model: Use a read-only workflow-level baseline, then elevate only in the security job that requires write scopes.

permissions:
  contents: read

jobs:
  security-scan:
    permissions:
      contents: read
      security-events: write  # For CodeQL
      id-token: write         # For attestations
      attestations: write     # For attestations


See references/best-practices.md section on security.

5. Modern Features

Triggers: "Add job summaries...", "Use environments...", "Run in container..."

See references/modern-features.md for:

Job summaries ($GITHUB_STEP_SUMMARY)
Deployment environments with approvals
Container jobs with services
Workflow annotations
6. Third-Party Action Documentation and Citation

When using third-party actions (any uses: entry not in the same repository):

Search for documentation:

"[owner/repo] [version] github action documentation"


Or use Context7 MCP:

mcp__context7__resolve-library-id to find action
mcp__context7__query-docs for documentation

Pin to SHA with version comment:

- uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2


Cite source and version in the response:

Action source (repository URL)
Version source (release/tag/changelog URL)
Selected commit SHA and human-readable version
Access date for the source used

See references/common-actions.md for pre-verified action versions.

Validation Workflow

CRITICAL: Every generated resource MUST be validated.

Generate workflow/action file
Invoke devops-skills:github-actions-validator skill
If errors: fix and re-validate
If success: present with usage instructions

Skip validation only for:

Partial code snippets
Documentation examples
User explicitly requests skip
Fallback Behavior (Tooling and Environment Constraints)

If required tooling or network access is unavailable, use this deterministic fallback order:

If devops-skills:github-actions-validator is unavailable, run local fallback checks:
actionlint (if installed)
yamllint (if installed)
manual YAML/schema review with a clear "not tool-validated" note
If Context7 or internet access is unavailable:
use references/common-actions.md for known action versions
state that external version verification could not be completed
If a template path is missing:
generate from the closest template pattern in assets/templates/
document which template was substituted

Fallback usage must always be reported in the final output.

Mandatory Standards

All generated resources must follow:

Standard	Implementation
Security	Pin to SHA, minimal permissions, mask secrets
Performance	Caching, concurrency, shallow checkout
Naming	Descriptive names, lowercase-hyphen files
Error Handling	Timeouts, cleanup with if: always()

See references/best-practices.md for complete guidelines.

Resources
Reference Documents
Document	Content	When to Use
references/best-practices.md	Security, performance, patterns	Every workflow
references/common-actions.md	Action versions, inputs, outputs	Public action usage
references/expressions-and-contexts.md	${{ }} syntax, contexts, functions	Complex conditionals
references/advanced-triggers.md	workflow_run, dispatch, ChatOps	Workflow orchestration
references/custom-actions.md	Metadata, structure, versioning	Custom action creation
references/modern-features.md	Summaries, environments, containers	Enhanced workflows
Templates
Template	Location
Basic Workflow	assets/templates/workflow/basic_workflow.yml
Reusable Workflow	assets/templates/workflow/reusable_workflow.yml
Composite Action	assets/templates/action/composite/action.yml
Docker Action	assets/templates/action/docker/
JavaScript Action	assets/templates/action/javascript/
Common Patterns
Matrix Testing
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [18, 20, 22]
  fail-fast: false

Conditional Deployment
deploy:
  if: github.event_name == 'push' && github.ref == 'refs/heads/main'

Artifact Sharing
# Upload
- uses: actions/upload-artifact@5d5d22a31266ced268874388b861e4b58bb5c2f3 # v4.3.1
  with:
    name: build-${{ github.sha }}
    path: dist/

# Download (in dependent job)
- uses: actions/download-artifact@c850b930e6ba138125429b7e5c93fc707a7f8427 # v4.1.4
  with:
    name: build-${{ github.sha }}

Third-Party Action Citation Block
Third-party action citations:
- actions/checkout: https://github.com/actions/checkout (version: v6.0.2, sha: de0fac2e4500dabe0009e67214ff5f5447ce83dd, accessed: 2026-02-28)

Done Criteria

The task is complete only when all checks below pass:

The request route was selected using the trigger decision tree.
Only the minimum required references/templates were loaded first.
Every third-party action is pinned to a commit SHA and has source/version citation.
Validation was run, or a skip exception/fallback path was explicitly documented.
Output includes assumptions, security-sensitive decisions (permissions/secrets), and generated file paths.
Workflow Summary
Route the request using the trigger decision tree
Load the minimum references/templates for that route
Generate using mandatory security and naming standards
Cite and pin third-party actions (source, version, SHA)
Validate with devops-skills:github-actions-validator (or documented fallback)
Fix and re-validate until clean
Present validated output with citations, assumptions, and file paths
Weekly Installs
145
Repository
akin-ozer/cc-de…s-skills
GitHub Stars
200
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn