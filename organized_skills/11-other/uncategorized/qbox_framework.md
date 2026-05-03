---
rating: ⭐⭐⭐
title: qbox-framework
url: https://skills.sh/proelias7/fivem-skill/qbox-framework
---

# qbox-framework

skills/proelias7/fivem-skill/qbox-framework
qbox-framework
Installation
$ npx skills add https://github.com/proelias7/fivem-skill --skill qbox-framework
SKILL.md
Qbox Framework Development

This skill provides guidelines and patterns for developing resources using the Qbox Project (qbx_core).

1. Philosophy: Exports & Modules

Qbox moves away from the global "Core Object" pattern (though supported via bridge) in favor of direct exports and imported modules.

Modern Native Way (Preferred):

local player = exports.qbx_core:GetPlayer(source)


Bridge Way (Legacy/Porting):

local QBCore = exports['qb-core']:GetCoreObject() -- Works via qbx_core bridge

2. Key Dependencies

Qbox is built "Ox-First". You will frequently use:

ox_lib: For UI, callbacks, zones, and utilities.
ox_inventory: For items and inventory management.
oxmysql: For database interactions.
3. Player Management
Get Player: exports.qbx_core:GetPlayer(source)
Player Data: Unlike QBCore's lookup table, Qbox uses internal setters/getters exposed via exports.
Save/Load: Handled automatically, but custom data can be saved via GetPlayer(source).Functions.SetMetaData.
4. Resource Structure
my-resource/
├── fxmanifest.lua     # Depends on qbx_core
├── client/
│   └── main.lua
├── server/
│   └── main.lua
└── locales/           # Ox_lib uses .json locales usually
    └── en.json

5. Documentation
Official Docs: https://docs.qbox.re/
Github: https://github.com/Qbox-project/qbx_core
Weekly Installs
41
Repository
proelias7/fivem-skill
GitHub Stars
4
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass