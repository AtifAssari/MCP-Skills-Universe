---
rating: ⭐⭐⭐
title: godot-navigation-pathfinding
url: https://skills.sh/thedivergentai/gd-agentic-skills/godot-navigation-pathfinding
---

# godot-navigation-pathfinding

skills/thedivergentai/gd-agentic-skills/godot-navigation-pathfinding
godot-navigation-pathfinding
Installation
$ npx skills add https://github.com/thedivergentai/gd-agentic-skills --skill godot-navigation-pathfinding
SKILL.md
Navigation & Pathfinding

NavigationServer-powered pathfinding with avoidance and dynamic obstacles define robust AI movement.

Available Scripts
dynamic_nav_manager.gd

Expert runtime navigation mesh updates for moving platforms.

server_navigation_setup.gd

Low-level NavigationServer3D usage (bypassing nodes). Creates maps, regions, and registers navmeshes entirely via RID for maximum performance.

async_dynamic_baking.gd

Expert logic for bake_from_source_geometry_data_async. Parses geometry on main thread then bakes in background to prevent procedural-gen stutters.

memory_optimized_queries.gd

Pattern for reusing NavigationPathQueryParameters3D and NavigationPathQueryResult3D objects to prevent frame-by-frame GC allocations.

terrain_cost_manager.gd

Controlling pathfinding logic using region_set_enter_cost and region_set_travel_cost to define high-penalty areas (mud, fire, water).

low_level_avoidance.gd

Direct RVO (Reciprocal Velocity Obstacles) registration using server-side agents. Uses NavigationServer3D.agent_set_avoidance_callback for high-performance avoidance.

moving_obstacle_server.gd

Dynamic obstacle registration (e.g. for projectiles or rolling hazards) that push RVO agents away without full navmesh baking.

nav_link_traversal.gd

Advanced handling of NavigationLink3D for jumps, teleports, and elevators. Detects link traversal and overrides standard movement.

layer_mask_navigation.gd

Architecture for multi-type navigation (e.g. Flying vs Walking vs Swimming) using 32-bit navigation layers and bitmasks.

agent_stuck_detection.gd

Robust AI recovery logic. Detects distance-over-time stalls and triggers jitter recovery or path recalculation.

group_avoidance_formations.gd

Coordinating crowd behavior. Strategies for avoiding individual agent clumping by using leader-relative target offsets.

NEVER Do in Navigation & Pathfinding
NEVER set target_position before awaiting physics frame — NavigationServer not ready in _ready()? Path fails silently. MUST call_deferred() then await get_tree().physics_frame.
NEVER use NavigationRegion2D.bake_navigation_polygon() at runtime — Synchronous baking freezes game for 100+ ms. Use NavigationServer.bake_from_source_geometry_data_async() for stutter-free updates.
NEVER forget to check is_navigation_finished() — Calling get_next_path_position() after reaching target = stale path, AI walks to old position.
NEVER use avoidance_enabled without setting radius — Default radius = 0, agent passes through others. Set nav_agent.radius = collision_shape.radius for proper avoidance.
NEVER poll target_position every frame for chase AI — Setting target 60x/sec = path recalculation spam. Use timer (0.2s intervals) or distance threshold for updates.
NEVER assume path exists — Target unreachable (blocked by walls)? get_next_path_position() returns invalid. Check is_target_reachable() or validate path length.
NEVER use heavy node-based navigation for thousands of simple entities — Use NavigationServer3D/2D RIDs directly to bypass node overhead.
NEVER call get_path() every frame — Use query_path() with reused NavigationPathQueryResult objects to prevent massive heap allocation and GC pressure.
NEVER leave 'enter_cost' at 0 for high-penalty areas — Use costs to make AI prefer logical paths (roads over water) instead of just shortest geometric distance.
NEVER ignore agent_set_avoidance_callback — Always use the callback for safe velocity computation to avoid synchronization issues and "jittery" movement.
2D Navigation
# Scene structure:
# Node2D (Level)
#   ├─ NavigationRegion2D
#   │    └─ Polygon2D (draw walkable area)
#   └─ CharacterBody2D (Enemy)
#        └─ NavigationAgent2D


Setup NavigationRegion2D:

Add NavigationRegion2D node
Create New NavigationPolygon
Click "Edit" → Draw walkable area
Bake navigation mesh
Basic AI Movement
extends CharacterBody2D

@onready var nav_agent := $NavigationAgent2D
@export var speed := 200.0

var target_position: Vector2

func _ready() -> void:
    # Wait for navigation to be ready
    call_deferred("setup_navigation")

func setup_navigation() -> void:
    await get_tree().physics_frame
    nav_agent.target_position = target_position

func _physics_process(delta: float) -> void:
    if nav_agent.is_navigation_finished():
        return
    
    var next_position := nav_agent.get_next_path_position()
    var direction := (next_position - global_position).normalized()
    
    velocity = direction * speed
    move_and_slide()

func set_target(pos: Vector2) -> void:
    target_position = pos
    nav_agent.target_position = pos

NavigationAgent Properties
# Path recalculation
nav_agent.path_desired_distance = 10.0
nav_agent.target_desired_distance = 10.0

# Avoidance
nav_agent.radius = 20.0
nav_agent.avoidance_enabled = true

# Performance
nav_agent.path_max_distance = 500.0

Advanced Patterns
Chase Player
extends CharacterBody2D

@onready var nav_agent := $NavigationAgent2D
@export var speed := 150.0
@export var chase_range := 300.0

var player: Node2D

func _physics_process(delta: float) -> void:
    if not player:
        return
    
    var distance := global_position.distance_to(player.global_position)
    
    if distance <= chase_range:
        nav_agent.target_position = player.global_position
        
        if not nav_agent.is_navigation_finished():
            var next_pos := nav_agent.get_next_path_position()
            var direction := (next_pos - global_position).normalized()
            velocity = direction * speed
            move_and_slide()

Patrol Points
extends CharacterBody2D

@onready var nav_agent := $NavigationAgent2D
@export var patrol_points: Array[Vector2] = []
@export var speed := 100.0

var current_point_index := 0

func _ready() -> void:
    if patrol_points.size() > 0:
        nav_agent.target_position = patrol_points[0]

func _physics_process(delta: float) -> void:
    if nav_agent.is_navigation_finished():
        _go_to_next_patrol_point()
        return
    
    var next_pos := nav_agent.get_next_path_position()
    var direction := (next_pos - global_position).normalized()
    velocity = direction * speed
    move_and_slide()

func _go_to_next_patrol_point() -> void:
    current_point_index = (current_point_index + 1) % patrol_points.size()
    nav_agent.target_position = patrol_points[current_point_index]

3D Navigation
extends CharacterBody3D

@onready var nav_agent := $NavigationAgent3D
@export var speed := 5.0

func _physics_process(delta: float) -> void:
    if nav_agent.is_navigation_finished():
        return
    
    var next_position := nav_agent.get_next_path_position()
    var direction := (next_position - global_position).normalized()
    
    velocity = direction * speed
    move_and_slide()

Dynamic Obstacles
# Add NavigationObstacle2D to moving objects
# Scene:
# CharacterBody2D (MovingPlatform)
#   └─ NavigationObstacle2D

# Navigation automatically updates around it

Signals
func _ready() -> void:
    nav_agent.velocity_computed.connect(_on_velocity_computed)
    nav_agent.navigation_finished.connect(_on_navigation_finished)

func _on_velocity_computed(safe_velocity: Vector2) -> void:
    velocity = safe_velocity
    move_and_slide()

func _on_navigation_finished() -> void:
    print("Reached destination")

Best Practices
1. Defer Navigation Setup
# ✅ Good - wait for navigation to initialize
func _ready() -> void:
    call_deferred("setup_nav")

func setup_nav() -> void:
    await get_tree().physics_frame
    nav_agent.target_position = target

2. Check if Path Exists
if not nav_agent.is_target_reachable():
    print("Target unreachable!")

3. Use Avoidance for Crowds
nav_agent.avoidance_enabled = true
nav_agent.radius = 20.0
nav_agent.max_neighbors = 10

Reference
Godot Docs: Navigation
Related
Master Skill: godot-master
Weekly Installs
96
Repository
thedivergentai/…c-skills
GitHub Stars
141
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass