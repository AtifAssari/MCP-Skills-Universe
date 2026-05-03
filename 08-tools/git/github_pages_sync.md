---
rating: ⭐⭐
title: github-pages-sync
url: https://skills.sh/s-hiraoku/synapse-a2a/github-pages-sync
---

# github-pages-sync

skills/s-hiraoku/synapse-a2a/github-pages-sync
github-pages-sync
Installation
$ npx skills add https://github.com/s-hiraoku/synapse-a2a --skill github-pages-sync
SKILL.md
GitHub Pages Sync

This skill ensures the public GitHub Pages site (site-docs/) stays synchronized with source code and internal documentation changes.

When This Skill Activates
Automatic Triggers
Code changes in core modules - synapse/*.py, synapse/commands/*.py
Profile changes - synapse/profiles/*.yaml
Plugin/Skill changes - plugins/**/*
Configuration changes - pyproject.toml (version, dependencies, entry points)
Internal doc changes - guides/*.md, docs/*.md, README.md
Site-docs changes - site-docs/** (direct edits to the published site)
Manual Invocation
/github-pages-sync - Run full site-docs synchronization check
Workflow
Phase 1: Detect Changes

When code or internal docs are modified, identify affected site-docs pages by consulting references/source-site-mapping.md.

Quick Reference - Common Patterns:

Change Type	Primary site-docs Pages	Secondary Pages
CLI command	reference/cli.md	guide/agent-management.md, guide/communication.md
API endpoint	reference/api.md	advanced/authentication.md
Profile setting	concepts/profiles.md, reference/profiles-yaml.md	reference/ports.md
Environment variable	reference/configuration.md	guide/settings.md
New feature	index.md	Relevant guide/ or concepts/ page
Version bump	changelog.md	index.md (badges)
Phase 2: Propose Updates

For each affected site-docs page:

Read the current page content
Identify the specific section to update
Propose the minimal necessary change
Present changes to user for approval

Update Principles:

Maintain MkDocs Material formatting (admonitions, tabs, code annotations)
Update only affected sections — do not rewrite entire pages
Keep index.md concise; put details in guide/ or reference/ pages
Preserve existing Mermaid diagrams unless the architecture changed
Ensure nav structure in mkdocs.yml stays consistent
Phase 3: Apply Updates

After user approval:

Apply changes to affected site-docs/ pages
Update mkdocs.yml nav if new pages were added
Update changelog.md if the change is user-facing
Phase 4: Verify

Run build verification:

uv run mkdocs build --strict


Check for:

Build success - No warnings or errors in strict mode
Broken links - All internal cross-references resolve
Nav consistency - mkdocs.yml nav matches actual files in site-docs/
Page Categories
High Traffic (Update Promptly)
Page	Purpose	Update Frequency
index.md	Landing page, first impression	Every major feature
getting-started/quickstart.md	First-time user experience	Install/setup changes
reference/cli.md	CLI command reference	Every CLI change
reference/api.md	API endpoint reference	Every API change
Core Guides
Page	Purpose	Update Frequency
guide/agent-management.md	Agent lifecycle	Agent workflow changes
guide/communication.md	Inter-agent messaging	Protocol changes
guide/agent-teams.md	Team orchestration	Team feature changes
guide/settings.md	Configuration guide	Setting changes
Deep Reference
Page	Purpose	Update Frequency
concepts/architecture.md	System design	Architecture changes
concepts/a2a-protocol.md	A2A protocol details	Protocol changes
reference/configuration.md	Full config reference	Setting additions
reference/profiles-yaml.md	YAML schema	Profile format changes
Reference Files

For detailed page inventory and source-to-page mappings, consult:

references/source-site-mapping.md - Source file to site-docs page relationships
references/site-inventory.md - Complete list of all site-docs pages and their roles
Special Cases
Version Updates

When pyproject.toml version changes:

Update changelog.md with release notes
Check if index.md badges need updating
New Feature Addition

For major new features:

Add to index.md feature highlights
Create or update relevant page in guide/ or concepts/
Update reference/cli.md and/or reference/api.md
Add to mkdocs.yml nav if a new page was created
Update getting-started/quickstart.md if the feature affects onboarding
New CLI Command
Add to reference/cli.md with full syntax and examples
Update relevant guide/ page with usage context
Update getting-started/quickstart.md if commonly used
Deprecation

When deprecating features:

Mark as deprecated with admonition in relevant pages
Add migration guide if needed
Update changelog.md
Remove from getting-started/quickstart.md examples
Weekly Installs
27
Repository
s-hiraoku/synapse-a2a
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass