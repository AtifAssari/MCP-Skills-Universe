---
title: ue5-audio-mcp
url: https://skills.sh/koshimazaki/ue-audio-skills/ue5-audio-mcp
---

# ue5-audio-mcp

skills/koshimazaki/ue-audio-skills/ue5-audio-mcp
ue5-audio-mcp
Installation
$ npx skills add https://github.com/koshimazaki/ue-audio-skills --skill ue5-audio-mcp
SKILL.md
UE Audio MCP Plugin — TCP Control (42 Commands)

Drive the C++ TCP server inside Unreal Editor. All commands use 4-byte big-endian length prefix + UTF-8 JSON on 127.0.0.1:9877.

Requires the UE Audio MCP Plugin installed in your UE5 project.

Connection
# Python SDK
from ue_audio_mcp.ue5_connection import get_ue5_connection
conn = get_ue5_connection()
resp = conn.send_command({"action": "ping"})

# Raw TCP
python3 -c "
import socket, struct, json
s = socket.socket(); s.settimeout(5); s.connect(('127.0.0.1', 9877))
p = json.dumps({'action':'ping'}).encode()
s.sendall(struct.pack('>I', len(p)) + p)
r = s.recv(4); l = struct.unpack('>I', r)[0]; print(json.loads(s.recv(l)))
"

All 42 Commands
System (1)
Command	Params	Returns
ping	—	engine, version, project, features[]
MetaSounds Builder Lifecycle (3)
Command	Params	Returns
create_builder	asset_type (Source/Patch/Preset), name	asset_type, name
add_interface	interface	—
build_to_asset	name, path (/Game/...)	name, path
Graph I/O (2)
Command	Params	Returns
add_graph_input	name, type, default?	name, type
add_graph_output	name, type	name, type
Node Operations (3)
Command	Params	Returns
add_node	id, node_type, position? [x,y]	id, node_type
set_default	node_id, input, value	node_id, input
connect	from_node, from_pin, to_node, to_pin	all four

__graph__ = sentinel node ID for graph boundary connections.

Audition & Editor (3)
Command	Params	Returns
audition	name?	—
stop_audition	—	—
open_in_editor	—	—
Graph Variables (3, UE 5.7+)
Command	Params	Returns
add_graph_variable	name, type, default?	name, type
add_variable_get_node	id, variable_name, delayed?	id, variable_name
add_variable_set_node	id, variable_name	id, variable_name
Presets (2)
Command	Params	Returns
convert_to_preset	referenced_asset (/Game/...)	referenced_asset
convert_from_preset	—	—
Query & Export (7)
Command	Params	Returns
list_node_classes	filter?, limit? (200), include_pins?, include_metadata?	nodes[], total, shown
list_metasound_nodes	(alias for list_node_classes)	same
get_node_locations	asset_path	nodes[], edges[]
get_graph_input_names	—	names[], count
set_live_updates	enabled (bool)	enabled
export_metasound	asset_path	asset_type, is_preset, interfaces[], graph_inputs[], graph_outputs[], variables[], nodes[], edges[]
list_blueprint_functions	filter?, class_filter?, audio_only?, limit?, include_pins?, list_classes_only?	functions[], total
Blueprint & Assets (4)
Command	Params	Returns
call_function	function, args?	function, return_value?
list_assets	class_filter?, path?, limit?	assets[], total, shown
scan_blueprint	asset_path, audio_only?, include_pins?	graphs[], audio_summary
export_audio_blueprint	asset_path	nodes[], edges[], audio_summary

Allowlisted functions: PlaySound2D, PlaySoundAtLocation, SpawnSoundAtLocation, SpawnSound2D, SetSoundMixClassOverride, ClearSoundMixClassOverride, PushSoundMixModifier, PopSoundMixModifier, SetGlobalPitchModulation, SetGlobalListenerFocusParameters, PlayDialogue2D, PlayDialogueAtLocation, SpawnDialogue2D, SpawnDialogueAtLocation, GetPlayerCameraManager, GetPlayerController, GetPlayerPawn.

class_filter values: Blueprint, WidgetBlueprint, AnimBlueprint, MetaSoundSource, MetaSoundPatch, SoundWave, SoundCue, SoundAttenuation, SoundClass, SoundConcurrency, SoundMix, ReverbEffect.

Blueprint Builder (7)
Command	Params	Returns
bp_open_blueprint	asset_path	asset_path, graphs[]
bp_add_node	kind (CallFunction/CustomEvent/VariableGet/VariableSet), name, graph?	node_id, kind, name
bp_connect_pins	from_node, from_pin, to_node, to_pin	all four
bp_set_pin_default	node_id, pin_name, value	node_id, pin_name
bp_compile	—	success, errors[], warnings[]
bp_register_existing_node	node_id, graph?	node_id, name, kind
bp_list_pins	node_id	pins[] (name, type, direction, connected, default)

Node kinds: CallFunction (audio API calls), CustomEvent (event receivers), VariableGet/VariableSet (Blueprint variables). Security: Only allowlisted audio functions can be called — prevents arbitrary code execution.

World Audio Setup (7)
Command	Params	Returns
place_anim_notify	animation_path, notify_type, time, sound?	animation_path, notify_type, time
place_bp_anim_notify	animation_path, notify_class, time	animation_path, time
spawn_audio_emitter	sound_path, location [x,y,z], name?, attenuation?	name, location
import_sound_file	file_path, destination	source_path, destination, asset_name
set_physical_surface	material_path, surface_type	material_path, surface_type
place_audio_volume	location [x,y,z], extent [x,y,z], name?, reverb_effect?, priority?	name, location, volume_extent
spawn_blueprint_actor	blueprint_path, location [x,y,z], name?, rotation? [p,y,r]	name, blueprint_path, location
Assets (1)
Command	Params	Returns
duplicate_asset	source_path, dest_path, dest_name	source_path, dest_path
Key Pin Names
Sine/Saw/Square/Triangle: IN: Frequency, Phase Offset, Glide, Bias; OUT: Audio
AD Envelope: IN: Trigger, Attack Time, Decay Time; OUT: Out Envelope
ADSR Envelope: IN: Trigger Attack, Trigger Release, Attack Time, Decay Time, Sustain Level, Release Time; OUT: Out Envelope
Biquad Filter: IN: In, Cutoff Frequency, Bandwidth, Filter Type; OUT: Out
Wave Player: IN: Play, Stop, Wave Asset, Start Time, Loop, Pitch Shift; OUT: Out Audio, On Finished
Multiply/Add (Audio): IN: Primary Operand, Operand; OUT: Out
Map Range: IN: Value, In Range A, In Range B, Out Range A, Out Range B, Clamped; OUT: Out

Full pin reference: scripts/ms_node_specs.json (93 nodes, 464 pins)

Example Workflows
Simple Sine → Output
{"action":"create_builder", "asset_type":"Source", "name":"MySine"}
{"action":"add_interface", "interface":"MetaSound"}
{"action":"add_graph_output", "name":"Out Mono", "type":"Audio"}
{"action":"add_node", "id":"osc", "node_type":"UE::Sine::Audio"}
{"action":"set_default", "node_id":"osc", "input":"Frequency", "value":440}
{"action":"connect", "from_node":"osc", "from_pin":"Audio", "to_node":"__graph__", "to_pin":"Out Mono"}
{"action":"build_to_asset", "name":"MySine", "path":"/Game/Audio/MCP"}

Blueprint Audio Wiring
{"action":"bp_open_blueprint", "asset_path":"/Game/BP_Player"}
{"action":"bp_add_node", "kind":"CallFunction", "name":"PlaySound2D"}
{"action":"bp_add_node", "kind":"CustomEvent", "name":"OnFootstep"}
{"action":"bp_connect_pins", "from_node":"OnFootstep", "from_pin":"then", "to_node":"PlaySound2D", "to_pin":"execute"}
{"action":"bp_compile"}

World Audio Setup
{"action":"import_sound_file", "file_path":"/sounds/footstep_concrete_01.wav", "destination":"/Game/Audio/Footsteps"}
{"action":"spawn_audio_emitter", "sound_path":"/Game/Audio/Ambient/Wind", "location":[0,0,100], "name":"WindEmitter"}
{"action":"place_audio_volume", "location":[0,0,200], "extent":[500,500,300], "reverb_effect":"/Game/Audio/Reverb/LargeHall"}
{"action":"place_anim_notify", "animation_path":"/Game/Anims/Walk", "notify_type":"PlaySound", "time":0.3, "sound":"/Game/Audio/Footsteps/Step01"}

Project Scan & Export
{"action":"list_assets", "class_filter":"Blueprint"}
{"action":"scan_blueprint", "asset_path":"/Game/BP_Player", "audio_only":true}
{"action":"list_assets", "class_filter":"MetaSoundSource"}
{"action":"export_metasound", "asset_path":"/Game/Audio/MS_Gunshot"}


Or batch: python scripts/scan_project.py --full-export --import-db --rebuild-embeddings

Gotchas
Must call create_builder before any node/connection ops
__graph__ is NOT a real node — it's the boundary sentinel
Path must start with /Game/ or /Engine/, no ..
Audio vs Float: cannot cross-connect — use correct node variant
TCP drops after ~17 rapid commands — use reconnect with progressive delay
Builder state is global — only one active builder at a time
list_node_classes discovers real class names — the 65-name registry may miss some
BP Builder is additive-only — no node deletion (add nodes + wire, don't remove)
bp_compile may fail silently — check errors[] in response
World commands spawn into the current editor level — save before spawning
Source Files
C++ plugin: UE-AUDIO-MCP (42 commands, TCP:9877)
Python tools: src/ue_audio_mcp/tools/
Node registry: src/ue_audio_mcp/knowledge/metasound_nodes.py (195 nodes, 1053 entries)

$ARGUMENTS

Weekly Installs
10
Repository
koshimazaki/ue-…o-skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass