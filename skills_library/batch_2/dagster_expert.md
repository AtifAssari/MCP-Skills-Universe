---
title: dagster-expert
url: https://skills.sh/dagster-io/skills/dagster-expert
---

# dagster-expert

skills/dagster-io/skills/dagster-expert
dagster-expert
Installation
$ npx skills add https://github.com/dagster-io/skills --skill dagster-expert
Summary

Expert guidance for Dagster projects, asset definitions, and dg CLI workflows.

Provides deep knowledge of Dagster concepts (assets, components, schedules, sensors, jobs) and helps with project structure, debugging, and codebase navigation
Covers the dg CLI for common tasks: creating projects, scaffolding definitions, listing assets, launching runs, and exploring project structure
Includes guidance on automation approaches (schedules, sensors, declarative automation) and integration patterns with 40+ external tools
Always references official documentation before answering; use --json flags for machine-readable CLI output and uv for dependency management
SKILL.md
Core Dagster Concepts

Brief definitions only (see reference files for detailed examples):

Asset: Persistent object (table, file, model) produced by your pipeline
Component: Reusable building block that generates definitions (assets, schedules, sensors, jobs, etc.) relevant to a particular domain.
Integration Workflow

When integrating with ANY external tool or service, read the Integration libraries index. This contains information about which integration libraries exist, and references on how to create new custom integrations for tools that do not have a published library.

dg CLI

The dg CLI is the recommended way to programmatically interact with Dagster (adding definitions, launching runs, exploring project structure, etc.). It is installed as part of the dagster-dg-cli package. If a relevant CLI command for a given task exists, always attempt to use it.

ONLY explore the existing project structure if it is strictly necessary to accomplish the user's goal. In many cases, existing CLI tools will have sufficient understanding of the project structure, meaning listing and reading existing files is wasteful and unnecessary.

Almost all dg commands that return information have a --json flag that can be used to get the information in a machine-readable format. This should be preferred over the default table output unless you are directly showing the information to the user.

UV Compatibility

Projects typically use uv for dependency management, and it is recommended to use it for dg commands if possible:

uv run dg list defs
uv run dg launch --assets my_asset

CRITICAL: Always Read Reference Files Before Answering

NEVER answer from memory or guess at CLI commands, APIs, or syntax. ALWAYS read the relevant reference file(s) from the Reference Index below before responding.

For every question, identify which reference file(s) are relevant using the index descriptions, read them, then answer based on what you read.

Reference Index
Asset Selection Syntax — filtering assets by tag, group, kind, upstream, or downstream; AssetSelection in Python, UI search bar, or CLI
Environment Variables — configuring environment variables across different environments
Asset Patterns — defining assets, dependencies, metadata, partitions, or multi-asset definitions
Choosing an Automation Approach — deciding between schedules, sensors, and declarative automation
Schedules — time-based automation with cron expressions
Declarative Automation — asset-centric condition-based automation using AutomationCondition
Asset Sensors — triggering on asset materialization events
Basic Sensors — event-driven automation with file watching or custom polling
Run Status Sensors — reacting to run success, failure, or other status changes
dg check — validating project configuration or definitions
create-dagster — creating a new Dagster project from scratch
dg dev — starting a local Dagster development instance
dg launch — materializing assets or executing jobs locally
dg list components — seeing available component types for scaffolding
dg list defs — listing or filtering registered definitions
Dagster Plus API — dg api, programmatically querying or managing Dagster Plus resources (assets, runs, deployments, code locations, schedules, sensors, secrets, issues, etc.)
dg list — exploring project structure (component tree, environment variables, workspace projects)
Dagster Plus CLI — dg plus, Dagster Plus authentication, configuration, and deployment; logging in, setting config, creating API tokens, deploying code, pulling env vars, managing dbt manifests
dg scaffold component — creating a custom reusable component type
dg scaffold defs — adding new definitions (assets, schedules, sensors, components) to a project
dg utilities — dg utils, inspecting component types, viewing integrations, refreshing state-backed component cache
Creating Components — building a new custom component from scratch
Designing Component Integrations — designing a component that wraps an external service or tool; custom integrations
Resolved Framework — defining custom YAML schema types using Resolver, Model, or Resolvable
Subclassing Components — extending an existing component via subclassing; customize dagster integration component
Template Variables — using Jinja2 template variables in component YAML (env, dg, context, or custom scopes)
Creating State-Backed Components — building a component that fetches and caches external state
Using State-Backed Components — managing state-backed components in production, CI/CD, or refreshing state
Deployment Configuration Files — build.yaml, container_context.yaml, dagster_cloud.yaml; Dagster Plus deployment configuration; configuring Docker registry, container context, agent queue; Hybrid deployment files
Integration libraries index for 40+ tools and technologies (dbt, Fivetran, Snowflake, AWS, etc.). — integration, external tool, dagster-*; dbt, fivetran, airbyte, snowflake, bigquery, sling, aws, gcp
Migration Guides — sensor migration to declarative automation, sensor migration to automation condition
Weekly Installs
1.2K
Repository
dagster-io/skills
GitHub Stars
138
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass