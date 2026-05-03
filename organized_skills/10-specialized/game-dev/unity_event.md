---
rating: ⭐⭐
title: unity-event
url: https://skills.sh/besty0728/unity-skills/unity-event
---

# unity-event

skills/besty0728/unity-skills/unity-event
unity-event
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-event
SKILL.md
Event Skills

Inspect and modify UnityEvents (e.g. Button.onClick).

Guardrails

Mode: Full-Auto required

DO NOT (common hallucinations):

event_create / event_trigger do not exist → UnityEvents are triggered at runtime, not from editor skills
event_subscribe does not exist → use event_add_listener
event_remove does not exist → use event_remove_listener
event_add_listener requires exact component type and method name on the target

Routing:

For XR interaction events → use xr module's xr_add_interaction_event
For C# event code → write via script module
Skills
event_get_listeners

Get persistent listeners of a UnityEvent. Parameters:

name / instanceId / path: Target GameObject locator.
componentName (string): Component name.
eventName (string): Event field name (e.g. "onClick").
event_add_listener

Add a persistent listener to a UnityEvent (Editor time). Parameters:

name / instanceId / path, componentName, eventName: Target event.
targetObjectName, targetComponentName, methodName: Method to call.
mode (string, optional): "RuntimeOnly", "EditorAndRuntime", "Off".
argType (string, optional): "void", "int", "float", "string", "bool".
floatArg, intArg, stringArg, boolArg: Argument value if needed.
event_remove_listener

Remove a persistent listener by index. Parameters:

name / instanceId / path, componentName, eventName: Target event.
index (int): Listener index.
event_invoke

Invoke a UnityEvent explicitly (Runtime only). Parameters:

name / instanceId / path, componentName, eventName: Target event.
event_clear_listeners

Remove all persistent listeners from a UnityEvent.

Parameter	Type	Required	Default	Description
name	string	No	null	GameObject name
instanceId	int	No	0	GameObject instance ID
path	string	No	null	GameObject hierarchy path
componentName	string	No	null	Component name
eventName	string	No	null	Event field name (e.g. "onClick")

Returns: { success, removed }

event_set_listener_state

Set a listener's call state (Off, RuntimeOnly, EditorAndRuntime).

Parameter	Type	Required	Default	Description
name	string	No	null	GameObject name
instanceId	int	No	0	GameObject instance ID
path	string	No	null	GameObject hierarchy path
componentName	string	No	null	Component name
eventName	string	No	null	Event field name
index	int	No	0	Listener index
state	string	No	null	Call state: "Off", "RuntimeOnly", or "EditorAndRuntime"

Returns: { success, index, state }

event_list_events

List all UnityEvent fields on a component.

Parameter	Type	Required	Default	Description
name	string	No	null	GameObject name
instanceId	int	No	0	GameObject instance ID
path	string	No	null	GameObject hierarchy path
componentName	string	No	null	Component name

Returns: { success, component, count, events }

event_add_listener_batch

Add multiple listeners at once. items: JSON array of {targetObjectName, targetComponentName, methodName}.

Parameter	Type	Required	Default	Description
name	string	No	null	GameObject name
instanceId	int	No	0	GameObject instance ID
path	string	No	null	GameObject hierarchy path
componentName	string	No	null	Component name
eventName	string	No	null	Event field name
items	string	No	null	JSON array of {targetObjectName, targetComponentName, methodName}

Returns: { success, added, total }

event_copy_listeners

Copy listeners from one event to another.

Parameter	Type	Required	Default	Description
sourceObject	string	Yes	-	Source GameObject name
sourceComponent	string	Yes	-	Source component name
sourceEvent	string	Yes	-	Source event field name
targetObject	string	Yes	-	Target GameObject name
targetComponent	string	Yes	-	Target component name
targetEvent	string	Yes	-	Target event field name

Returns: { success, copied }

event_get_listener_count

Get the number of persistent listeners on a UnityEvent.

Parameter	Type	Required	Default	Description
name	string	No	null	GameObject name
instanceId	int	No	0	GameObject instance ID
path	string	No	null	GameObject hierarchy path
componentName	string	No	null	Component name
eventName	string	No	null	Event field name

Returns: { success, count }

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