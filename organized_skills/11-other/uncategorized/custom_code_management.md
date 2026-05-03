---
rating: ⭐⭐
title: custom-code-management
url: https://skills.sh/webflow/webflow-skills/custom-code-management
---

# custom-code-management

skills/webflow/webflow-skills/custom-code-management
custom-code-management
Installation
$ npx skills add https://github.com/webflow/webflow-skills --skill custom-code-management
SKILL.md
Custom Code Management

Add, review, and manage inline custom scripts on a Webflow site — analytics, tracking pixels, chat widgets, or any custom JavaScript.

Important Note

ALWAYS use Webflow MCP tools for all operations:

Use Webflow MCP's webflow_guide_tool to get best practices before any other tool call
Use Webflow MCP's data_sites_tool with action list_sites to identify available sites
Use Webflow MCP's data_scripts_tool with action list_registered_scripts to list all registered scripts
Use Webflow MCP's data_scripts_tool with action list_applied_scripts to list scripts applied to pages
Use Webflow MCP's data_scripts_tool with action add_inline_site_script to register a new inline script
Use Webflow MCP's data_scripts_tool with action delete_all_site_scripts to remove ALL site scripts (no selective delete)
Use Webflow MCP's data_scripts_tool with action get_page_script to get custom code for a specific page
Use Webflow MCP's data_scripts_tool with action upsert_page_script to add or update page-level custom code
Use Webflow MCP's data_scripts_tool with action delete_all_page_scripts to remove all custom code from a page
All tool calls must include the required context parameter (15-25 words, third-person perspective)
Instructions
Phase 1: Discovery
Call webflow_guide_tool first — always the first MCP tool call
Get the site: Use data_sites_tool with action list_sites. If only one site, use it automatically.
Phase 2: Analysis
List scripts: Call list_registered_scripts and list_applied_scripts in parallel
Check page-level scripts (if relevant): Use get_page_script for specific pages
Present findings: Name, version, location (header/footer), registration vs application status
Phase 3: Planning & Confirmation

Before any mutation, present the plan and require explicit confirmation:

Adding scripts: user must type "add"
Removing ALL site scripts: user must type "delete all" (warn: no selective delete)
Page-level changes: user must type "update"
Phase 4: Execution
Add site script: add_inline_site_script with displayName, sourceCode, version, location, canCopy
Remove all site scripts: delete_all_site_scripts
Add/update page script: upsert_page_script
Remove page scripts: delete_all_page_scripts
Phase 5: Verification
Re-list scripts to confirm success
Report what changed (name, location, version, char count)
Remind user to publish — suggest using safe-publish skill
Examples
Example 1: View scripts

User: "What scripts are on my site?"

webflow_guide_tool → data_sites_tool → list_registered_scripts + list_applied_scripts in parallel
Present summary of all scripts
Example 2: Add Google Tag Manager

User: "Add GTM to my site"

webflow_guide_tool → data_sites_tool → ask for GTM container ID
Preview script, require "add" → add_inline_site_script (header, version "1.0.0")
Verify and remind to publish
Example 3: Remove all scripts

User: "Remove all scripts"

webflow_guide_tool → data_sites_tool → list current scripts
Warn: removes ALL scripts. Require "delete all" → delete_all_site_scripts
Verify and remind to publish
Example 4: Page-specific tracking

User: "Add conversion tracking to my thank-you page"

webflow_guide_tool → data_sites_tool → get_page_script to check existing
Preview, require "update" → upsert_page_script
Verify and remind to publish
Guidelines
webflow_guide_tool always first — before any other MCP tool
No <script> tags — Webflow adds them automatically
Max 10,000 characters per script; displayName + version must be unique
Site-level scripts (add_inline_site_script) apply to all pages; page-level scripts (upsert_page_script) apply to one page
No selective delete — delete_all_site_scripts removes everything; always list scripts first so user knows what will be lost
Hosted/external scripts not available via MCP — inline only
Recommend header for analytics (GA, GTM); footer for chat widgets and non-critical scripts
If displayName + version exists, suggest incrementing the version
Always remind users to publish after changes
Weekly Installs
323
Repository
webflow/webflow-skills
GitHub Stars
64
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass