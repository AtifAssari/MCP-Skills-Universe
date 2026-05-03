---
rating: ⭐⭐
title: rpgjs-studio
url: https://skills.sh/rsamaium/rpg-js/rpgjs-studio
---

# rpgjs-studio

skills/rsamaium/rpg-js/rpgjs-studio
rpgjs-studio
Installation
$ npx skills add https://github.com/rsamaium/rpg-js --skill rpgjs-studio
SKILL.md
RPGJS Studio API Skill

Use this skill to execute content-management tasks against an RPGJS Studio instance.

Inputs
Check whether a local RPGSTUDIO.md file exists in the current working directory.
If RPGSTUDIO.md exists, treat it as local project context and read it first.
Use it to recover persistent values such as:
BASE_URL
any other project-specific instructions relevant to API usage
Do not recover, request, or persist a projectId. The API key is scoped to the RPGJS Studio project, so work directly on the user's requested resource.
If RPGSTUDIO.md does not exist, continue normally.
Resolve BASE_URL from the user if provided.
Default BASE_URL to https://rpgjs.studio when the user did not specify another host.
Read the API key from the environment variable RPGSTUDIO_API_KEY.
Mandatory startup workflow
Check whether RPGSTUDIO_API_KEY exists before any API call.
When checking RPGSTUDIO_API_KEY, never print its value in the terminal and never echo it back in the response.
If the variable is missing or empty, stop and tell the user to create an API key first on ${BASE_URL}/api-keys, then export RPGSTUDIO_API_KEY.
Build authenticated requests with these headers:
-H "x-api-key:$RPGSTUDIO_API_KEY"
-H "Content-Type: application/json"

Prefer curl for HTTP calls. Use another HTTP client only if there is a clear reason.
Fail fast on authentication errors. If the API returns an invalid-key style response, 401, or 403, stop the task and tell the user to verify the key or contact support.
Read only the reference file that matches the user task:
references/database.md
references/maps.md
references/events.md
references/event-examples.md
references/blocks.md
references/media.md
references/settings.md
Local memory file

Use RPGSTUDIO.md as a lightweight local memory file for the current project.

Read it at the start if it exists.
Reuse values already stored there instead of asking again.
After the task, update or create it with stable, non-secret context discovered during execution.

Typical contents:

last used BASE_URL
project-specific conventions or notes useful for future calls

Do not use RPGSTUDIO.md to select a project. The current RPGSTUDIO_API_KEY already identifies the target project, so proceed directly with the user's request.

Never store secrets in this file.

Do not store RPGSTUDIO_API_KEY.
Do not print RPGSTUDIO_API_KEY.
Do not copy raw secret values into logs, terminal output, or markdown.
Request pattern

Define the base command once and reuse it:

BASE_URL="${BASE_URL:-https://rpgjs.studio}"
curl -sS \
  -H "x-api-key:$RPGSTUDIO_API_KEY" \
  -H "Content-Type: application/json"


For write operations, prefer:

curl -sS -X POST "$BASE_URL/..." \
  -H "x-api-key:$RPGSTUDIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{...}'

Execution rules
Start by identifying the resource domain, then load the matching reference file.
Use REST semantics: GET, POST, PUT, DELETE.
Resolve foreign keys before creation or update:
Search media with /api/media?query=<search>.
Search database records with /api/database/:type?query=<search>.
If a matching dependency exists, reuse its returned _id.
If not found, create it first, then continue with the returned _id.
Never call a project listing endpoint just to choose a project. The API key determines the project context.
When the user asks to create game objects, send the smallest valid payload first, then enrich it only if the task requires more fields.
Reuse IDs returned by the API instead of guessing them.
When the user provides a database _id for a read, update, or delete task, call GET /api/database/:type/:id first and inspect the existing record before deciding the payload or reporting the content.
If an endpoint shape is uncertain, inspect the response from a nearby GET endpoint first and adapt from that live payload.
Do not continue after an auth failure.
If a missing dependency would require AI media generation, always call the unified media generation endpoint with action: "estimate" first.
After the estimate, report the required credits to the user and ask for confirmation before calling action: "execute".
Never start an AI media generation directly without this estimate and confirmation step.
For POST /api/maps/generate, rely on references/maps.md for the AI map generation workflow and endpoint-specific failure behavior.
Summarize the exact records created, updated, or deleted in the final response.
When a task reveals stable project context such as BASE_URL or local conventions, persist that non-secret context into RPGSTUDIO.md for future runs.
Common checks
database task: read references/database.md
map task: read references/maps.md
event task: read references/events.md
event example task: read references/event-examples.md
event workflow block task: read references/blocks.md
media task: read references/media.md
settings task: read references/settings.md
Current schema notes
Project settings and database enemies both support combat animation spritesheet media IDs under animations: attack, hurt, die, and castSpell.
The RPGJS starter runtime uses these spritesheets in action battle: attack actions, damage/hurt feedback, delayed death removal, and skill/cast usage can temporarily switch to the configured spritesheet.
Database enemies support action battle AI options under behavior: enemyType, attackCooldown, visionRange, attackRange, dodgeChance, dodgeCooldown, fleeThreshold, attackPatterns, patrolWaypoints, and groupBehavior.
Project settings and database enemies both support level-gated skill acquisition under skills: { skillId, level }.
Database skills support media IDs under icon, animation, and sound.
Game/runtime code can read media data usable in the game with GET /api/game/media/:mediaId; use references/media.md for details.
Weekly Installs
10
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