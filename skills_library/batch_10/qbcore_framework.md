---
title: qbcore-framework
url: https://skills.sh/germanfndez/fiveai-skills/qbcore-framework
---

# qbcore-framework

skills/germanfndez/fiveai-skills/qbcore-framework
qbcore-framework
Installation
$ npx skills add https://github.com/germanfndez/fiveai-skills --skill qbcore-framework
SKILL.md
QBCore Framework Development

Complete guide for developing with QBCore Framework — a comprehensive FiveM roleplay framework providing core functionalities and modules.

When to use
Creating or editing QBCore resources/scripts
Working with player data (Player object, PlayerData)
Implementing jobs, gangs, economy, or inventory systems
Using QBCore client/server functions, callbacks, or events
Questions about QBCore best practices and optimization
How to use

Read individual rule files for detailed explanations and examples:

rules/core-concepts.md — QBCore architecture, PlayerData structure, Player object, framework initialization
rules/client-functions.md — Client-side QBCore functions, notifications, player state management
rules/server-functions.md — Server-side functions, player retrieval, callbacks, usable items
rules/player-methods.md — Player object methods: money, items, jobs, gangs, metadata, accounts
rules/jobs-gangs.md — Job system, gang system, payments, duty status
rules/inventory-items.md — Inventory management, item handling, usable items
rules/events-callbacks.md — QBCore events, server callbacks, client callbacks, event handling
rules/best-practices.md — QBCore coding standards, optimization, security, naming conventions
rules/reference-links.md — Official QBCore documentation links
Key principles
Always check for nil — if Player then ... end before using Player object
Use QBCore.Functions.GetPlayer — Standard player retrieval: local Player = QBCore.Functions.GetPlayer(source)
Wait for player load — Check player loaded state on client before accessing PlayerData
Never trust client — Validate all data server-side, secure your events
Follow QBCore patterns — Use QBCore functions instead of reinventing (callbacks, notifications, etc.)
Optimize loops — Cache player objects, use dynamic Wait times, avoid unnecessary calls
Use camelCase — Follow Lua naming: myVariable, local over global
Minimal globals — Keep variables local unless they need global scope
Use ox_lib for UI — Prefer ox_lib for menus, dialogs, notifications, progress bars
Weekly Installs
33
Repository
germanfndez/fiv…i-skills
GitHub Stars
5
First Seen
Feb 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass