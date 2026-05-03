---
rating: ⭐⭐
title: develop
url: https://skills.sh/subframeapp/subframe/develop
---

# develop

skills/subframeapp/subframe/develop
develop
Installation
$ npx skills add https://github.com/subframeapp/subframe --skill develop
Summary

Implement Subframe designs with business logic into your codebase.

Fetches designs via MCP from Subframe by URL, page ID, or name, then syncs required components locally
Detects project state and guides you through either full Subframe integration or using designs as inspiration in existing non-Subframe projects
Handles component syncing, page creation in the correct directory structure, and preservation of existing business logic when updating designs
Provides patterns for adding data fetching, form handling, event handlers, and loading/error states to generated presentational code
SKILL.md

Implement Subframe designs in the codebase. Fetch the design via MCP, sync components, and add business logic.

MCP Authentication

If you cannot find the get_page_info tool (or any Subframe MCP tools), the MCP server likely needs to be authenticated. Ask the user to authenticate the Subframe MCP server. If the user is using Claude Code, instruct them to run /mcp to view and authenticate their MCP servers, and then say "done" when they're finished.

Detect Project State

Before starting, check for package.json and .subframe/ folder in the current directory:

Condition	Action
No package.json	Run /subframe:setup first — there's no project to implement into yet.
Has package.json AND has .subframe/ folder	Proceed with the workflow below.
Has package.json but NO .subframe/ folder	Ask the user (see below).
Existing non-Subframe project

If the current directory has a package.json but no .subframe/ folder, ask the user which approach they prefer:

Use the design as inspiration — Fetch the design via MCP for reference, but implement the page using the existing styles, components, and patterns already in the repo. Translate the Subframe design's layout and structure into whatever UI framework the project already uses (e.g., existing component library, CSS modules, styled-components). Do NOT install Subframe or sync components. Skip to Inspiration Workflow.
Use Subframe styles and components — Install Subframe into the project so the design renders pixel-perfect with Subframe's generated code. Run /subframe:setup first, then continue with the Workflow below.
Workflow
Fetch the design - Use get_page_info with the URL, ID, or name.
Sync components if needed - Only if components don't exist locally
Create the page - Put it in the right place per codebase patterns
Add business logic - Data fetching, forms, events, loading/error states
Inspiration Workflow

Use this workflow when the user chose to use the design as inspiration in an existing non-Subframe project.

Fetch the design — Use get_page_info with the URL, ID, or name to get the page's layout and structure. If you encounter Subframe components or tokens you're unfamiliar with, use get_component_info to understand a component's props and behavior, or get_theme to see the Subframe project's design tokens (colors, fonts, spacing, shadows).
Study existing patterns — Look at the codebase's existing components, styles, and conventions. Identify local equivalents for Subframe components used in the design.
Create the page — Implement the design using the codebase's existing UI framework, translating the Subframe layout and component structure into local components and styling.
Add business logic — Data fetching, forms, events, loading/error states.
Fetching Designs
// By URL
get_page_info({ url: "https://app.subframe.com/PROJECT_ID/design/PAGE_ID/edit" })

// By ID (e.g., from /subframe:design)
get_page_info({ id: "PAGE_ID", projectId: "PROJECT_ID" })

// By name
get_page_info({ name: "Settings Page", projectId: "PROJECT_ID" })

// List all pages first if needed
list_pages({ projectId: "PROJECT_ID" })


Get the projectId from .subframe/sync.json. If .subframe/sync.json doesn't exist or doesn't contain a projectId, call list_projects to get the available projects. Each project includes a projectId, name, teamId, and teamName.

One project: Use it automatically.
Multiple projects: Always ask the user which project to use. Present each project with its teamName to disambiguate. If the user already mentioned a specific team or project name, match it against the teamName and name fields — but still confirm before proceeding. Never silently pick a project when multiple exist.
Syncing Components

Sync components when they don't exist locally. You can sync specific components by name:

npx @subframe/cli@latest sync Button Alert TextField


Or sync all components:

npx @subframe/cli@latest sync --all


When to sync:

Components don't exist locally → Sync those specific components before implementing
Components already exist → Don't sync automatically. If the user wants the latest versions, they'll ask.

Never modify synced component files - they get overwritten. Create wrapper components if you need to add logic.

Sync Disable

If you must modify a synced component file directly, add // @subframe/sync-disable to the top of the file:

// @subframe/sync-disable
import * as React from "react"
// ... rest of component


This prevents the file from being overwritten on future syncs.

Updating a sync-disabled component:

If the user wants to update a component that has sync-disable, the sync command will skip it. To get the latest version:

Use get_component_info to fetch the latest code from Subframe
Manually merge the changes with the local modifications
Adding Business Logic

Subframe generates presentational code with placeholder data. You add:

Data fetching:

const { data, isLoading, error } = useQuery(...)

if (isLoading) return <Skeleton />
if (error) return <Alert variant="error">{error.message}</Alert>

return <PageComponent {...data} />


Form handling:

const handleSubmit = async (e: FormEvent) => {
  e.preventDefault()
  await submitForm(formData)
}


Event handlers:

<Button onClick={handleClick}>Submit</Button>
<Card actionSlot={<IconButton onClick={handleDelete} />} />

Dark Mode

If the Subframe project has dark mode enabled, the synced theme uses CSS variables with .dark class overrides. To activate dark mode in the app, set the dark class on the <html> element — using next-themes, a React theme provider context, or any other method.

Updating Existing Pages

When a design changes:

Fetch the updated design
Update layout/structure from new design
Preserve existing hooks, handlers, and state management
Sync any new components

When diffing the updated design against the existing code, if there are design changes beyond what the user asked you to design (e.g., layout tweaks, new elements, removed sections), call those out and ask whether to include them.

MCP Tools Reference
Tool	Purpose	Key Parameters
get_page_info	Fetch page code	url, id, or name; projectId
get_component_info	Fetch component code	url, id, or name; projectId
list_pages	List all pages	projectId
list_components	List all components	projectId
get_theme	Get Tailwind config	projectId, cssType
Weekly Installs
430
Repository
subframeapp/subframe
GitHub Stars
383
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn