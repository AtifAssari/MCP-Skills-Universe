---
rating: ⭐⭐
title: esx-framework
url: https://skills.sh/proelias7/fivem-skill/esx-framework
---

# esx-framework

skills/proelias7/fivem-skill/esx-framework
esx-framework
Installation
$ npx skills add https://github.com/proelias7/fivem-skill --skill esx-framework
SKILL.md
ESX Framework Development

This skill provides guidelines and patterns for developing resources using the ESX Framework (Legacy).

1. Core Object Retrieval

ESX Legacy (New Way):

local ESX = exports["es_extended"]:getSharedObject()


Legacy / Backwards Compatible:

local ESX = nil
TriggerEvent('esx:getSharedObject', function(obj) ESX = obj end)

2. Key Concepts
Player Data (Server-side)
xPlayer: The main object for player interaction server-side.
ESX.GetPlayerFromId(source): Retrieves the xPlayer object.
xPlayer Methods: xPlayer.addMoney, xPlayer.setJob, xPlayer.addInventoryItem.
Callbacks (Server -> Client Data)
ESX.RegisterServerCallback (Server): Respond to client requests.
ESX.TriggerServerCallback (Client): Request data from server.
Items & Database
Items are defined in the database (items table) or ox_inventory.
Database typically uses oxmysql.
3. Standard Resource Structure
my-resource/
├── fxmanifest.lua
├── config.lua
├── client/
│   └── main.lua
├── server/
│   └── main.lua
└── locales/
    └── en.lua

4. Best Practices
Use New Exports: Prefer exports["es_extended"]:getSharedObject() over the event trigger.
Validate xPlayer: Always check if xPlayer then before using it.
Secure Events: Use ESX.SecureNetEvent (if available) or manual checks.
OneSync: Develop with OneSync Infinity in mind (server-side entity creation).
5. Documentation
Official Docs: https://documentation.esx-framework.org/
Github: https://github.com/esx-framework/esx_core
Weekly Installs
51
Repository
proelias7/fivem-skill
GitHub Stars
4
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass