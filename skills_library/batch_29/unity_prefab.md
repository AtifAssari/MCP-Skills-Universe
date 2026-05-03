---
title: unity-prefab
url: https://skills.sh/besty0728/unity-skills/unity-prefab
---

# unity-prefab

skills/besty0728/unity-skills/unity-prefab
unity-prefab
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-prefab
SKILL.md
Unity Prefab Skills

BATCH-FIRST: Use prefab_instantiate_batch when spawning 2+ prefab instances.

Guardrails

Mode: Full-Auto required

DO NOT (common hallucinations):

prefab_create_from_object does not exist → use prefab_create (takes scene object name/instanceId and savePath)
prefab_spawn does not exist → use prefab_instantiate
prefab_edit / prefab_modify do not exist → use prefab_set_property (edit prefab asset directly) or instantiate, modify, then prefab_apply
prefab_save does not exist → use prefab_apply (applies instance changes to source prefab)

Routing:

To modify components on a prefab instance in scene → use component module skills, then prefab_apply
To set a property directly on the prefab asset → prefab_set_property (this module)
To find all instances of a prefab → prefab_find_instances (this module)
Skills Overview
Single Object	Batch Version	Use Batch When
prefab_instantiate	prefab_instantiate_batch	Spawning 2+ instances

No batch needed:

prefab_create - Create prefab from scene object
prefab_apply - Apply instance changes to prefab
prefab_unpack - Unpack prefab instance
prefab_get_overrides - Get instance overrides
prefab_revert_overrides - Revert to prefab values
prefab_apply_overrides - Apply overrides to prefab
prefab_create_variant - Create a prefab variant
prefab_find_instances - Find all instances of a prefab in scene
prefab_set_property - Set a property on a component inside a Prefab asset (supports basic types, vectors, colors, and asset references)
Skills
prefab_create

Create a prefab from a scene GameObject.

Parameter	Type	Required	Description
name	string	No*	Source object name
instanceId	int	No*	Instance ID
path	string	No*	Object path
instanceId	int	No*	Instance ID
savePath	string	Yes	Prefab save path

Returns: {success, prefabPath, sourceObject}

prefab_instantiate

Instantiate a prefab into the scene.

Parameter	Type	Required	Default	Description
prefabPath	string	Yes	-	Prefab asset path
name	string	No	prefab name	Instance name
x, y, z	float	No	0	Local position (relative to parent if set)
parentName	string	No	null	Parent object name
parentInstanceId	int	No	0	Parent instance ID
parentPath	string	No	null	Parent hierarchy path

Returns: {success, name, instanceId, path, prefabPath, position}

prefab_instantiate_batch

Instantiate multiple prefabs in one call.

Parameter	Type	Required	Description
items	array	Yes	Array of instantiation configs

Item properties: prefabPath, name, x, y, z, rotX, rotY, rotZ, scaleX, scaleY, scaleZ, parentName, parentInstanceId, parentPath

Returns: {success, totalItems, successCount, failCount, results: [{success, name, instanceId, prefabPath, position}]}

unity_skills.call_skill("prefab_instantiate_batch", items=[
    {"prefabPath": "Assets/Prefabs/Enemy.prefab", "x": 0, "z": 0, "name": "Enemy_01"},
    {"prefabPath": "Assets/Prefabs/Enemy.prefab", "x": 2, "z": 0, "name": "Enemy_02"},
    {"prefabPath": "Assets/Prefabs/Enemy.prefab", "x": 4, "z": 0, "name": "Enemy_03"}
])

prefab_apply

Apply instance changes back to the prefab asset.

Parameter	Type	Required	Description
name	string	No*	Prefab instance name
instanceId	int	No*	Instance ID
path	string	No*	Object path
instanceId	int	No*	Instance ID

Returns: {success, gameObject, prefabPath}

prefab_unpack

Unpack a prefab instance (break prefab connection).

Parameter	Type	Required	Default	Description
name	string	No*	-	Prefab instance name
instanceId	int	No*	-	Instance ID
path	string	No*	-	Object path
instanceId	int	No*	-	Instance ID
completely	bool	No	false	Unpack all nested prefabs

Returns: {success, gameObject, mode}

prefab_get_overrides

Get list of property overrides on a prefab instance.

Parameter	Type	Required	Description
name	string	No*	Prefab instance name
instanceId	int	No*	Instance ID

Returns: {success, overrides: [{type, path, property}]}

prefab_revert_overrides

Revert all overrides on a prefab instance back to prefab values.

Parameter	Type	Required	Description
name	string	No*	Prefab instance name
instanceId	int	No*	Instance ID
prefab_apply_overrides

Apply all overrides from instance to source prefab asset.

Parameter	Type	Required	Description
name	string	No*	Prefab instance name
instanceId	int	No*	Instance ID
prefab_create_variant

Create a prefab variant from an existing prefab.

Parameter	Type	Required	Default	Description
sourcePrefabPath	string	Yes	-	Path to the source prefab asset
variantPath	string	Yes	-	Save path for the new variant

Returns: { success, sourcePath, variantPath, name }

prefab_find_instances

Find all instances of a prefab in the current scene.

Parameter	Type	Required	Default	Description
prefabPath	string	Yes	-	Prefab asset path to search for
limit	int	No	50	Maximum number of instances to return

Returns: { success, prefabPath, count, instances: [{ name, path, instanceId }] }

prefab_set_property

Set a property on a component inside a Prefab asset file (without instantiating it). Supports basic types, vectors, colors, enums, and asset references.

Parameter	Type	Required	Default	Description
prefabPath	string	Yes	-	Path to the prefab asset
componentType	string	Yes	-	Component type name
propertyName	string	Yes	-	Serialized property name
value	string	Cond.	null	Value for basic types (int/float/bool/string/enum/vector/color)
assetReferencePath	string	Cond.	null	Asset path for Object reference fields (Material, Texture, AudioClip, ScriptableObject, etc.)
gameObjectName	string	No	null	Child object name inside prefab (defaults to root)

Provide either value (basic types) or assetReferencePath (asset references).

Returns: { success, prefabPath, gameObject, component, property, valueSet }

# Set a float property on prefab root
unity_skills.call_skill("prefab_set_property",
    prefabPath="Assets/Prefabs/Enemy.prefab",
    componentType="EnemyStats",
    propertyName="maxHealth",
    value="100"
)

# Assign an asset reference to a prefab component
unity_skills.call_skill("prefab_set_property",
    prefabPath="Assets/Prefabs/Enemy.prefab",
    componentType="AudioSource",
    propertyName="m_audioClip",
    assetReferencePath="Assets/Audio/hit.wav"
)

# Edit a child object inside a prefab
unity_skills.call_skill("prefab_set_property",
    prefabPath="Assets/Prefabs/Player.prefab",
    componentType="MeshRenderer",
    propertyName="m_Materials.Array.data[0]",
    assetReferencePath="Assets/Materials/PlayerSkin.mat",
    gameObjectName="Body"
)

Example: Efficient Enemy Spawning
import unity_skills

# BAD: 10 API calls for 10 enemies
for i in range(10):
    unity_skills.call_skill("prefab_instantiate",
        prefabPath="Assets/Prefabs/Enemy.prefab",
        name=f"Enemy_{i}",
        x=i * 2
    )

# GOOD: 1 API call for 10 enemies
unity_skills.call_skill("prefab_instantiate_batch", items=[
    {"prefabPath": "Assets/Prefabs/Enemy.prefab", "name": f"Enemy_{i}", "x": i * 2}
    for i in range(10)
])

Best Practices
Organize prefabs in dedicated folders
Use prefabs for repeated objects
Apply changes to update all instances
Unpack only when unique modifications needed
Use batch instantiation for level generation
Exact Signatures

Exact names, parameters, defaults, and returns are defined by GET /skills/schema or unity_skills.get_skill_schema(), not by this file.

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