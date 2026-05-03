---
title: wow-addon-structure
url: https://skills.sh/jburlison/wowaddonapiagents/wow-addon-structure
---

# wow-addon-structure

skills/jburlison/wowaddonapiagents/wow-addon-structure
wow-addon-structure
Installation
$ npx skills add https://github.com/jburlison/wowaddonapiagents --skill wow-addon-structure
SKILL.md
WoW AddOn Structure (Retail)
Scope
Retail only, current as of Patch 12.0.0.
Focuses on folder layout, .toc metadata, loading order, and SavedVariables.
Avoid deprecated or removed APIs and call out restricted directives.
When to use this skill

Use this skill when you need to:

Design or review an AddOn folder layout.
Author or audit a .toc file.
Reason about file load order and login events.
Wire SavedVariables or troubleshoot persistence.
Query or load AddOns via C_AddOns APIs.
How to use this skill
Start with layout and naming rules in references/ADDON_STRUCTURE.md.
Build the .toc file using references/TOC_FORMAT.md.
Plan initialization order with references/LOADING_LIFECYCLE.md.
Wire persistence with references/SAVED_VARIABLES.md.
Use C_AddOns metadata APIs from references/C_ADDONS_API.md.
Cross-check patterns in Blizzard UI source from references/VIEWING_BLIZZARD_UI.md.
Reference files
references/ADDON_STRUCTURE.md - Folder layout rules, naming, and common patterns.
references/TOC_FORMAT.md - .toc syntax, directives, and file order rules.
references/LOADING_LIFECYCLE.md - Load order, events, and login timeline.
references/SAVED_VARIABLES.md - Persistence rules and file locations.
references/C_ADDONS_API.md - Key C_AddOns metadata and load APIs.
references/VIEWING_BLIZZARD_UI.md - How to inspect Blizzard UI source.
Key rules and reminders
The AddOn folder name and .toc filename must match.
The .toc file is required and defines file load order.
Files load top to bottom in the .toc list.
SavedVariables are available after ADDON_LOADED unless LoadSavedVariablesFirst is used.
Use LoadOnDemand and C_AddOns.LoadAddOn for heavy modules.
Some .toc directives are restricted to Blizzard AddOns and are not available to third-party AddOns.
Sources
https://warcraft.wiki.gg/wiki/TOC_format
https://warcraft.wiki.gg/wiki/AddOn
https://warcraft.wiki.gg/wiki/AddOn_loading_process
https://warcraft.wiki.gg/wiki/SavedVariables
https://warcraft.wiki.gg/wiki/Viewing_Blizzard%27s_interface_code
https://warcraft.wiki.gg/wiki/World_of_Warcraft_API
https://github.com/Gethe/wow-ui-source/tree/live/Interface/AddOns/Blizzard_APIDocumentationGenerated
Weekly Installs
20
Repository
jburlison/wowad…piagents
GitHub Stars
24
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass