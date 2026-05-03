---
rating: ⭐⭐⭐
title: expo-cicd-workflows
url: https://skills.sh/expo/skills/expo-cicd-workflows
---

# expo-cicd-workflows

skills/expo/skills/expo-cicd-workflows
expo-cicd-workflows
Installation
$ npx skills add https://github.com/expo/skills --skill expo-cicd-workflows
Summary

Write and validate EAS CI/CD workflow YAML files for Expo projects.

Fetches the latest JSON schema from Expo's API to ensure job types, parameters, triggers, and runner configurations are current
Supports dynamic expressions using ${{ }} syntax with contexts for GitHub events, workflow inputs, job outputs, and step results
Includes built-in validation script that checks workflow structure against the schema and reports errors before deployment
Provides reference documentation for syntax, pre-packaged job types, and workflow structure via cached fetch requests
SKILL.md
EAS Workflows Skill

Help developers write and edit EAS CI/CD workflow YAML files.

Reference Documentation

Fetch these resources before generating or validating workflow files. Use the fetch script (implemented using Node.js) in this skill's scripts/ directory; it caches responses using ETags for efficiency:

# Fetch resources
node {baseDir}/scripts/fetch.js <url>


JSON Schema — https://api.expo.dev/v2/workflows/schema

It is NECESSARY to fetch this schema
Source of truth for validation
All job types and their required/optional parameters
Trigger types and configurations
Runner types, VM images, and all enums

Syntax Documentation — https://raw.githubusercontent.com/expo/expo/refs/heads/main/docs/pages/eas/workflows/syntax.mdx

Overview of workflow YAML syntax
Examples and English explanations
Expression syntax and contexts

Pre-packaged Jobs — https://raw.githubusercontent.com/expo/expo/refs/heads/main/docs/pages/eas/workflows/pre-packaged-jobs.mdx

Documentation for supported pre-packaged job types
Job-specific parameters and outputs

Do not rely on memorized values; these resources evolve as new features are added.

Workflow File Location

Workflows live in .eas/workflows/*.yml (or .yaml).

Top-Level Structure

A workflow file has these top-level keys:

name — Display name for the workflow
on — Triggers that start the workflow (at least one required)
jobs — Job definitions (required)
defaults — Shared defaults for all jobs
concurrency — Control parallel workflow runs

Consult the schema for the full specification of each section.

Expressions

Use ${{ }} syntax for dynamic values. The schema defines available contexts:

github.* — GitHub repository and event information
inputs.* — Values from workflow_dispatch inputs
needs.* — Outputs and status from dependent jobs
jobs.* — Job outputs (alternative syntax)
steps.* — Step outputs within custom jobs
workflow.* — Workflow metadata
Generating Workflows

When generating or editing workflows:

Fetch the schema to get current job types, parameters, and allowed values
Validate that required fields are present for each job type
Verify job references in needs and after exist in the workflow
Check that expressions reference valid contexts and outputs
Ensure if conditions respect the schema's length constraints
Validation

After generating or editing a workflow file, validate it against the schema:

# Install dependencies if missing
[ -d "{baseDir}/scripts/node_modules" ] || npm install --prefix {baseDir}/scripts

node {baseDir}/scripts/validate.js <workflow.yml> [workflow2.yml ...]


The validator fetches the latest schema and checks the YAML structure. Fix any reported errors before considering the workflow complete.

Answering Questions

When users ask about available options (job types, triggers, runner types, etc.), fetch the schema and derive the answer from it rather than relying on potentially outdated information.

Weekly Installs
22.3K
Repository
expo/skills
GitHub Stars
1.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn