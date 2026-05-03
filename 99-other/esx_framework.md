---
title: esx-framework
url: https://skills.sh/germanfndez/fiveai-skills/esx-framework
---

# esx-framework

skills/germanfndez/fiveai-skills/esx-framework
esx-framework
Installation
$ npx skills add https://github.com/germanfndez/fiveai-skills --skill esx-framework
SKILL.md
ESX Framework Development

Complete guide for developing with ESX Legacy Framework — the most trusted FiveM roleplay framework since 2017.

When to use
Creating or editing ESX resources/scripts
Working with player data (xPlayer, PlayerData)
Implementing jobs, economy, inventory, or weapon systems
Using ESX client/server functions, callbacks, or events
Questions about ESX best practices and optimization
How to use

Read individual rule files for detailed explanations and examples:

rules/core-concepts.md — ESX architecture, PlayerData, xPlayer object, framework initialization

rules/client-functions.md — Client-side ESX functions, UI systems, player state management

rules/server-functions.md — Server-side functions, player retrieval, callbacks, triggers

rules/xplayer-methods.md — xPlayer object methods: money, items, weapons, inventory, jobs, metadata

rules/jobs-economy.md — Job system, salaries, accounts (money/bank), society management

rules/inventory-items.md — Inventory system, item management, usable items, weight calculations

rules/weapons-loadout.md — Weapon system, loadout, components, ammo, tints

rules/events-callbacks.md — ESX events, server callbacks, client callbacks, secure net events

rules/best-practices.md — ESX coding standards, optimization, security, naming conventions

rules/reference-links.md — Official ESX documentation links

Key principles
Always check for nil — if xPlayer then ... end before using xPlayer
Use ESX.GetPlayerFromId — Standard player retrieval: local xPlayer = ESX.GetPlayerFromId(source)
Wait for player load — Check ESX.IsPlayerLoaded() on client before accessing PlayerData
Never trust client — Validate all data server-side, use SecureNetEvent for client events
Follow ESX patterns — Use ESX functions instead of reinventing (callbacks, notifications, etc.)
Optimize loops — Cache player objects, avoid unnecessary GetPlayerFromId calls
Use camelCase — Follow Lua naming: myVariable, MyGlobalFunction, MY_CONSTANT
Minimal globals — Keep variables local unless they need global scope
Use ox_lib for UI — Prefer ox_lib for menus, dialogs, notifications, progress bars instead of ESX UI
Weekly Installs
38
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