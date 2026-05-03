---
rating: ⭐⭐
title: unity-sample
url: https://skills.sh/besty0728/unity-skills/unity-sample
---

# unity-sample

skills/besty0728/unity-skills/unity-sample
unity-sample
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-sample
SKILL.md
Sample Skills

Basic examples for testing the API.

Guardrails

Mode: Full-Auto required

DO NOT (common hallucinations):

Sample skills are basic test/demo skills — do not use them for production work
sample_create is a simplified version of gameobject_create — prefer the full gameobject module
sample_hello / sample_ping are connectivity test skills only

Routing:

For actual GameObject operations → use gameobject module
For server health check → use Python helper's unity_skills.health()
Skills
create_cube

Create a cube primitive. Parameters: x, y, z, name

create_sphere

Create a sphere primitive. Parameters: x, y, z, name

delete_object

Delete object by name. Parameters: objectName

find_objects_by_name

Find objects containing string. Parameters: nameContains (name 也可作为兼容别名)

set_object_position

Set object position. Parameters: objectName, x, y, z

set_object_rotation

Set object rotation. Parameters: objectName, x, y, z

set_object_scale

Set object scale. Parameters: objectName, x, y, z

get_scene_info

Get current scene information. Parameters: None.

Exact Signatures

Exact names, parameters, defaults, and returns are defined by GET /skills/schema or unity_skills.get_skill_schema(), not by this file.

Weekly Installs
12
Repository
besty0728/unity-skills
GitHub Stars
894
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass