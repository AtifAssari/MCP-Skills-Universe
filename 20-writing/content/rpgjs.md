---
title: rpgjs
url: https://skills.sh/rsamaium/rpg-js/rpgjs
---

# rpgjs

skills/rsamaium/rpg-js/rpgjs
rpgjs
Installation
$ npx skills add https://github.com/rsamaium/rpg-js --skill rpgjs
SKILL.md
RPGJS v5 Project
Overview

Use this skill to work inside an RPGJS v5 project with the live documentation as source of truth. Start by proving that the current codebase is an RPGJS project, then load the relevant RPGJS and CanvasEngine docs with curl or an equivalent CLI fetcher before making changes.

Start Here

Verify that the current workspace is an actual RPGJS project before doing anything else.

Inspect one or more package.json files and look for @rpgjs packages.

Useful commands:

rg -n '"@rpgjs|@rpgjs/' . --glob 'package.json'
rg --files . | rg 'package.json$'


If no project-local package.json uses @rpgjs/*, do not hand-build the project structure from memory.

Read the RPGJS v5 quick start first, then install the project from the documented flow.

Treat the quick start as mandatory before bootstrapping a missing project.

A fresh install already includes Tiled map editor integration and example maps, so use that scaffold as the baseline instead of assembling the project manually.

Use this URL:

https://v5.rpgjs.dev/guide/quick-start.md

Load Live Documentation

Do not rely on memory for RPGJS v5 usage details. Fetch the documentation with curl or a similar CLI tool and read the relevant pages before installing or changing code.

Fetch the RPGJS documentation index:

curl -fsSL https://v5.rpgjs.dev/llms.txt


Use the llms.txt file as the table of contents. Extract the relevant Markdown links from it, then fetch the pages you need.

Example workflow:

curl -fsSL https://v5.rpgjs.dev/llms.txt -o /tmp/rpgjs-v5-llms.txt
rg -o 'https://[^ )]+\\.md' /tmp/rpgjs-v5-llms.txt
curl -fsSL https://v5.rpgjs.dev/guide/quick-start.md


If the llms.txt uses relative links, resolve them against https://v5.rpgjs.dev/.

Prefer reading only the pages needed for the task. Keep the fetched docs small and targeted.

CanvasEngine Rule For .ce Files

Treat every .ce file as CanvasEngine code.

Before editing, creating, or explaining a .ce file, fetch the CanvasEngine documentation index:

curl -fsSL https://canvasengine.net/llms.txt


Then fetch the relevant Markdown pages referenced there. Do not invent CanvasEngine syntax from memory when the docs can be read directly.

If the task touches menus, HUDs, overlays, dialogs, title screens, or any file ending in .ce, load CanvasEngine docs first and then inspect nearby project components for local conventions.

GUI CSS Rule

For GUI styling, rely on the RPGJS UI CSS library instead of inventing an unrelated CSS system.

Fetch and read this documentation before changing GUI styles, classes, or layout rules:

curl -fsSL https://raw.githubusercontent.com/RSamaium/RPG-JS/refs/heads/v5/packages/ui-css/README.md


When the task affects GUI appearance, menus, HUDs, dialog boxes, notifications, shops, or title screens:

inspect the existing RPGJS UI CSS usage in the project
verify available classes, structure, and styling patterns against the UI CSS README
prefer extending the library’s conventions over custom one-off CSS
Physics Rule

RPGJS relies on its dedicated RPG-oriented physics engine for collisions and related behavior.

Fetch and read this documentation before changing collisions, movement constraints, hitboxes, map blocking, or other physics-adjacent gameplay behavior:

curl -fsSL https://raw.githubusercontent.com/RSamaium/RPG-JS/refs/heads/v5/packages/physic/README.md


Do not guess collision behavior from generic game-engine habits. Verify it against the physics library docs first.

Synchronization Rule

Client-server synchronization must go through synchronized player properties when the data represents state.

Fetch and read this guide before changing synchronized state, replicated player data, snapshot behavior, or cross-map persistence:

curl -fsSL https://v5.rpgjs.dev/guide/synchronization.md


Use player props for persistent state that must survive synchronization, snapshots, server restarts, or map transfers.

Do not use ad hoc side channels for durable gameplay state when props is the correct model.

Use map.broadcast(type, data) for ephemeral messages that should be broadcast on the current map without becoming saved state.

Use player.on(key, cb) to listen to client-sent socket data when that communication pattern is actually needed.

Working Sequence

Follow this order:

Confirm that the current workspace is an RPGJS project by checking package.json for @rpgjs/*.
If not, fetch and read https://v5.rpgjs.dev/guide/quick-start.md.
Install the project according to the documented quick-start flow.
Confirm that the scaffold now contains @rpgjs/* packages.
Fetch https://v5.rpgjs.dev/llms.txt with curl or equivalent.
Fetch the specific RPGJS Markdown pages needed for the task.
If .ce files are involved, fetch https://canvasengine.net/llms.txt and the relevant CanvasEngine Markdown pages too.
If GUI styling is involved, fetch the RPGJS UI CSS README and use it as the CSS reference.
If collisions or physics are involved, fetch the RPGJS physic README and use it as the physics reference.
If synchronized state or networked player data is involved, fetch the synchronization guide and use props as the default state model.
Inspect the local codebase for conventions before editing.
Implement changes and verify them with the project’s normal commands.
Installation Rule

When no RPGJS project exists yet:

Read the quick start page with curl or equivalent.
Follow the documented installation steps instead of guessing the package names or folder layout.
Keep the generated Tiled integration and example maps unless the user explicitly asks to remove or replace them.
Only start feature work after the scaffold is present and the project is recognized as an RPGJS codebase.

If installation requires network access or package-manager writes outside the sandbox, request approval and then proceed with the install instead of stopping at advice.

Project Cues

In an RPGJS v5 project, expect some mix of these signals:

@rpgjs/* dependencies in package.json
client.ts, server.ts, and sometimes standalone.ts entrypoints
config.client.* and config.server.* configuration files
server/client/common split
map or world content tied to Tiled
gameplay classes, event definitions, and map logic
UI components written as .ce files

Treat the existing project structure as the primary convention source after the docs.

Editing Guidance

Read the closest existing files before creating new gameplay objects, map logic, or UI components.

When working on gameplay or engine integration:

verify imports and APIs against the fetched RPGJS docs
prefer matching nearby project patterns over generic abstractions
keep server/client responsibilities aligned with the current codebase
check whether maps are loaded through provideTiledMap or a custom provideLoadMap

When working on .ce components:

verify CanvasEngine syntax against fetched docs
inspect sibling .ce files for established patterns
preserve the existing component style unless the user asks for a broader refactor

When working on GUI styles:

use the RPGJS UI CSS library as the default styling system
verify class names and structure against the UI CSS README
avoid replacing library conventions with ad hoc CSS unless the user explicitly asks for that

When working on collisions or movement rules:

verify assumptions against the RPGJS physic README
treat the dedicated physics engine as the source of truth for collision behavior
avoid importing generic physics patterns that are not supported by the library

When working on synchronized state:

use player props for state that must persist across maps, snapshots, or restarts
configure synchronization and permanence deliberately according to the documented options
use map.broadcast(...) for ephemeral, non-persistent map-wide messages
use player.on(...) only for explicit client-to-server socket communication
avoid storing durable gameplay state in a custom path when synchronized props already solve the problem
References

Read source-map.md when you need the canonical doc URLs, the minimal fetch workflow, and the bootstrap rule for a missing project. Read architecture-notes.md when you need the core RPGJS v5 project model used by this repository.

Weekly Installs
19
Repository
rsamaium/rpg-js
GitHub Stars
1.6K
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn