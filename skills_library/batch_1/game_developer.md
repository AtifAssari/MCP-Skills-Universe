---
title: game-developer
url: https://skills.sh/jeffallan/claude-skills/game-developer
---

# game-developer

skills/jeffallan/claude-skills/game-developer
game-developer
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill game-developer
Summary

Game systems implementation for Unity and Unreal with ECS architecture, physics, networking, and performance optimization.

Covers core game development workflows: architecture design, ECS/component systems, physics configuration, multiplayer networking with lag compensation, and shader programming
Enforces 60+ FPS performance targets with profiling checkpoints; includes object pooling, LOD systems, async loading, and component caching patterns to eliminate frame-time bottlenecks
Provides reference guides for Unity C# patterns (MonoBehaviour, ScriptableObjects, state machines) and Unreal C++/Blueprints workflows
Includes ready-to-use code templates for object pooling, component caching, and state machines; validates performance and multiplayer stability before shipping
SKILL.md
Game Developer
Core Workflow
Analyze requirements — Identify genre, platforms, performance targets, multiplayer needs
Design architecture — Plan ECS/component systems, optimize for target platforms
Implement — Build core mechanics, graphics, physics, AI, networking
Optimize — Profile and optimize for 60+ FPS, minimize memory/battery usage
✅ Validation checkpoint: Run Unity Profiler or Unreal Insights; verify frame time ≤16 ms (60 FPS) before proceeding. Identify and resolve CPU/GPU bottlenecks iteratively.
Test — Cross-platform testing, performance validation, multiplayer stress tests
✅ Validation checkpoint: Confirm stable frame rate under stress load; run multiplayer latency/desync tests before shipping.
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Unity Development	references/unity-patterns.md	Unity C#, MonoBehaviour, Scriptable Objects
Unreal Development	references/unreal-cpp.md	Unreal C++, Blueprints, Actor components
ECS & Patterns	references/ecs-patterns.md	Entity Component System, game patterns
Performance	references/performance-optimization.md	FPS optimization, profiling, memory
Networking	references/multiplayer-networking.md	Multiplayer, client-server, lag compensation
Constraints
MUST DO
Target 60+ FPS on all platforms
Use object pooling for frequent instantiation
Implement LOD systems for optimization
Profile performance regularly (CPU, GPU, memory)
Use async loading for resources
Implement proper state machines for game logic
Cache component references (avoid GetComponent in Update)
Use delta time for frame-independent movement
MUST NOT DO
Instantiate/Destroy in tight loops or Update()
Skip profiling and performance testing
Use string comparisons for tags (use CompareTag)
Allocate memory in Update/FixedUpdate loops
Ignore platform-specific constraints (mobile, console)
Use Find methods in Update loops
Hardcode game values (use ScriptableObjects/data files)
Output Templates

When implementing game features, provide:

Core system implementation (ECS component, MonoBehaviour, or Actor)
Associated data structures (ScriptableObjects, structs, configs)
Performance considerations and optimizations
Brief explanation of architecture decisions
Key Code Patterns
Object Pooling (Unity C#)
public class ObjectPool<T> where T : Component
{
    private readonly Queue<T> _pool = new();
    private readonly T _prefab;
    private readonly Transform _parent;

    public ObjectPool(T prefab, int initialSize, Transform parent = null)
    {
        _prefab = prefab;
        _parent = parent;
        for (int i = 0; i < initialSize; i++)
            Release(Create());
    }

    public T Get()
    {
        T obj = _pool.Count > 0 ? _pool.Dequeue() : Create();
        obj.gameObject.SetActive(true);
        return obj;
    }

    public void Release(T obj)
    {
        obj.gameObject.SetActive(false);
        _pool.Enqueue(obj);
    }

    private T Create() => Object.Instantiate(_prefab, _parent);
}

Component Caching (Unity C#)
public class PlayerController : MonoBehaviour
{
    // Cache all component references in Awake — never call GetComponent in Update
    private Rigidbody _rb;
    private Animator _animator;
    private PlayerInput _input;

    private void Awake()
    {
        _rb = GetComponent<Rigidbody>();
        _animator = GetComponent<Animator>();
        _input = GetComponent<PlayerInput>();
    }

    private void FixedUpdate()
    {
        // Use cached references; use deltaTime for frame-independence
        Vector3 move = _input.MoveDirection * (speed * Time.fixedDeltaTime);
        _rb.MovePosition(_rb.position + move);
    }
}

State Machine (Unity C#)
public abstract class State
{
    public abstract void Enter();
    public abstract void Tick(float deltaTime);
    public abstract void Exit();
}

public class StateMachine
{
    private State _current;

    public void TransitionTo(State next)
    {
        _current?.Exit();
        _current = next;
        _current.Enter();
    }

    public void Tick(float deltaTime) => _current?.Tick(deltaTime);
}

// Usage example
public class IdleState : State
{
    private readonly Animator _animator;
    public IdleState(Animator animator) => _animator = animator;
    public override void Enter() => _animator.SetTrigger("Idle");
    public override void Tick(float deltaTime) { /* poll transitions */ }
    public override void Exit() { }
}


Documentation

Weekly Installs
1.9K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass