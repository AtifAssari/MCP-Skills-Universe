---
rating: ⭐⭐
title: umbraco-backoffice
url: https://skills.sh/umbraco/umbraco-cms-backoffice-skills/umbraco-backoffice
---

# umbraco-backoffice

skills/umbraco/umbraco-cms-backoffice-skills/umbraco-backoffice
umbraco-backoffice
Installation
$ npx skills add https://github.com/umbraco/umbraco-cms-backoffice-skills --skill umbraco-backoffice
SKILL.md
Umbraco Backoffice Extensions Overview
What This Skill Does

Backoffice customisations are combinations of extension types working together:

A "custom admin area" = Section + Menu + Dashboard
A "data management tool" = Section + Menu + Workspace
A "hierarchical browser" = Section + Menu + Tree + Workspace

This skill provides complete working blueprints. The source code is in ./examples/ - copy and adapt for your needs.

For details on individual extension types, invoke the referenced sub-skills.

TIP: If the Umbraco CMS source code is available in your workspace, use it as a reference and for inspiration. The backoffice client code in src/Umbraco.Web.UI.Client/src/packages/ shows production implementations of all extension types - study how the core team structures sections, workspaces, trees, and other patterns.

Required Workflow

CRITICAL: This workflow is MANDATORY for ALL extension development.

1. PLAN ──► Read PRE-BUILD-PLANNING.md FIRST
   │        Draw wireframe, label extension types, identify UUI components
   │        ⚠️ DO NOT write code until wireframe is approved
   ↓
2. BUILD ──► Use examples and sub-skills to create extension
   │
   │        ⛔ STOP - Do not skip validation
   ↓
3. VALIDATE ──► MANDATORY post-build steps:
               • npm run build (must pass)
               • Spawn umbraco-extension-reviewer agent
               • Fix High/Medium issues without asking
               • Browser test per POST-BUILD-VALIDATION.md


If you skip planning: You WILL build the wrong extension type. If you skip validation: Bugs WILL reach the user.

This workflow applies whether invoked via /umbraco-quickstart or directly.

CRITICAL: Follow this workflow for ALL extension development:

1. PLAN ──► Read PRE-BUILD-PLANNING.md, draw wireframes, identify extension types
      ↓
2. BUILD ──► Use examples and sub-skills to create extension
      ↓
3. VALIDATE ──► Read POST-BUILD-VALIDATION.md, run umbraco-extension-reviewer

Never skip planning - Wireframes prevent building the wrong extension type
Never skip validation - The reviewer catches issues before they reach users
Available Examples

Each example has a detailed README.md with full documentation. See the examples/ folder.

Example	Complexity	What It Shows
Blueprint	Starter	Section + Menu + Dashboard + Workspace - the fundamental pattern
tree-example	Intermediate	Tree navigation in Settings section with Workspace
TimeDashboard	Advanced	13+ extension types including Header Apps, Modals, Property Editors
notes-wiki	Full-stack	Complete C# backend with CRUD, hierarchical tree, multiple workspaces
Quick Reference
Need a new section? Start with Blueprint
Need tree navigation? See tree-example
Need specific extension type? Check TimeDashboard for examples
Need full-stack with API? Study notes-wiki
Using the Examples
Browse the examples/ folder and read the README.md for each example
Copy the example closest to your needs into your project
Rename aliases from the example namespace to your own (e.g., Blueprint.* to MyApp.*)
Update the entityType values to match your domain
Customise the UI components for your use case
Register with Umbraco via umbraco-package.json
Add project reference to the main Umbraco instance - use skill umbraco-add-extension-reference
Reference Documentation

Detailed reference material is available in separate files for on-demand loading:

Reference	When to Read
PRE-BUILD-PLANNING.md	Before building any extension - visual planning, wireframes, UUI components
EXTENSION-MAP.md	"Where does extension type X appear in the UI?" - ASCII diagram showing all extension locations
SUB-SKILLS-REFERENCE.md	"What skill do I need for X?" - Complete index of all sub-skills by category
POST-BUILD-VALIDATION.md	After building - complete validation workflow, browser testing, debugging
Weekly Installs
160
Repository
umbraco/umbraco…e-skills
GitHub Stars
23
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn