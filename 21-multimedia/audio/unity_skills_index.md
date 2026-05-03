---
rating: ⭐⭐
title: unity-skills-index
url: https://skills.sh/besty0728/unity-skills/unity-skills-index
---

# unity-skills-index

skills/besty0728/unity-skills/unity-skills-index
unity-skills-index
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-skills-index
SKILL.md
Unity Skills - Module Index

Module docs. Start with ../SKILL.md for mode switching and schema-first rules.

Multi-instance: For version-specific projects, call unity_skills.set_unity_version(...) first. Schema-first: Use GET /skills/schema or unity_skills.get_skill_schema() for exact signatures. Load module docs for workflow guidance and guardrails.

Modules

Mode reminder: SA modules are available in Semi-Auto by default. FA modules require Full-Auto mode.

Module	Mode	Description	Batch Support
gameobject	FA	Object create/move/parent	Yes
component	FA	Component add/remove/configure	Yes
material	FA	Material property edits	Yes
light	FA	Light create/configure	Yes
prefab	FA	Prefab create/apply/spawn	Yes
asset	SA	Asset refresh/find/info	Yes
batch	FA	Batch and async jobs	Built-in
ui	FA	UGUI Canvas/UI creation	Yes
uitoolkit	FA	UXML/USS/UIDocument	No
script	SA	Script create/read/update	Yes
scene	SA	Scene load/save/query	No
editor	SA	Play/select/undo/redo	No
animator	FA	Animator controllers	No
shader	FA	Shader create/list	No
console	SA	Log capture/filter	No
validation	FA	Broken reference checks	No
importer	FA	Texture/audio/model import	Yes
cinemachine	FA	VCam operations	No
probuilder	FA	ProBuilder mesh edits	No
xr	FA	XRI setup	No
terrain	FA	Terrain create/paint	No
physics	FA	Raycast/overlap/gravity	No
navmesh	FA	NavMesh bake/query	No
timeline	FA	Timeline tracks/clips	No
workflow	SA	Task snapshots/undo	No
cleaner	FA	Unused/duplicate assets	No
smart	FA	Query/layout/auto-bind	No
perception	SA	Scene/project analysis	No
camera	FA	Scene View camera	No
event	FA	UnityEvent wiring	No
package	FA	UPM install/query	No
project	FA	Project info/settings	No
profiler	FA	Perf statistics	No
optimization	FA	Asset optimization	No
sample	FA	Demo/test skills	No
debug	SA	Compile/system diagnostics	No
test	FA	Unity Test Runner	No
bookmark	FA	Scene View bookmarks	No
history	FA	Undo/redo history	No
scriptableobject	FA	ScriptableObject assets	No
Advisory Design Modules

These modules provide design guidance only.

Module	Description
project-scout	Inspect existing project
architecture	Plan system boundaries
adr	Record tradeoffs
performance	Review hot paths
asmdef	Plan asmdef deps
blueprints	Small-game blueprints
script-roles	Assign class roles
scene-contracts	Define scene wiring
testability	Extract testable logic
patterns	Choose patterns
async	Choose async model
inspector	Design authoring UX
scriptdesign	Review script structure
Batch-First Rule

When a Full-Auto task touches 2+ objects, prefer *_batch skills over repeated single-item calls.

Skill Naming Convention

Skills follow <module>_<action> or <module>_<action>_batch. Use schema to verify the exact prefix list. Special: scene_analyze, hierarchy_describe, project_stack_detect → perception; job_* → batch. If a skill name does not match a valid prefix or a schema result, do not invent it.

Weekly Installs
13
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