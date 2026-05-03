---
rating: ⭐⭐⭐
title: unity-csharp
url: https://skills.sh/alexanderstephenthompson/claude-hub/unity-csharp
---

# unity-csharp

skills/alexanderstephenthompson/claude-hub/unity-csharp
unity-csharp
Installation
$ npx skills add https://github.com/alexanderstephenthompson/claude-hub --skill unity-csharp
SKILL.md
Unity C# Skill

Version: 2.0 Stack: Unity, C#

Patterns for writing clean, performant Unity C# code. Includes VR/mobile optimization.

Scope and Boundaries

This skill covers:

MonoBehaviour lifecycle and component architecture
Unity-specific C# patterns (caching, events, coroutines, null safety)
Performance optimization (draw calls, batching, LODs, pooling)
VR/mobile performance targets and profiling
ScriptableObject usage

Defers to other skills:

vrc-udon: VRChat-specific scripting (UdonSharp)
vrc-worlds: VRChat world setup and limits
vrc-avatars: VRChat avatar setup and limits

Use this skill when: Writing C# scripts for Unity, or optimizing Unity performance for VR/mobile.

Core Principles
Composition Over Inheritance — Small, focused components.
Avoid Update() When Possible — Event-driven or coroutines instead.
Cache References — GetComponent is expensive; cache in Awake.
ScriptableObjects for Data — Decouple data from behavior.
Null-Safe Access — Unity objects can be destroyed at any time.
Measure First — Profile before optimizing; gut feelings lie.
Batch Aggressively — Same material = potential batch. Draw calls matter most in VR.
Patterns
Reference Caching
public class PlayerController : MonoBehaviour
{
    private Rigidbody _rb;
    private Animator _animator;

    [SerializeField] private Transform _cameraTarget;

    private void Awake()
    {
        _rb = GetComponent<Rigidbody>();
        _animator = GetComponent<Animator>();
    }

    private void FixedUpdate()
    {
        _rb.AddForce(Vector3.up);
    }
}

Event System (ScriptableObject)
[CreateAssetMenu(menuName = "Events/Game Event")]
public class GameEvent : ScriptableObject
{
    private readonly List<GameEventListener> _listeners = new();

    public void Raise()
    {
        for (int i = _listeners.Count - 1; i >= 0; i--)
            _listeners[i].OnEventRaised();
    }

    public void RegisterListener(GameEventListener listener) =>
        _listeners.Add(listener);

    public void UnregisterListener(GameEventListener listener) =>
        _listeners.Remove(listener);
}

public class GameEventListener : MonoBehaviour
{
    [SerializeField] private GameEvent _event;
    [SerializeField] private UnityEvent _response;

    private void OnEnable() => _event.RegisterListener(this);
    private void OnDisable() => _event.UnregisterListener(this);
    public void OnEventRaised() => _response.Invoke();
}

Null-Safe Pattern
// Unity overloads == for destroyed objects
if (_target != null)
{
    _target.DoSomething();
}

// Best: explicit destroyed check
if (_target != null && !_target.Equals(null))
{
    _target.DoSomething();
}

Coroutine Pattern
private IEnumerator FadeOut(float duration)
{
    float elapsed = 0f;
    Color startColor = _renderer.material.color;

    while (elapsed < duration)
    {
        elapsed += Time.deltaTime;
        float t = elapsed / duration;
        _renderer.material.color = Color.Lerp(startColor, Color.clear, t);
        yield return null;
    }

    gameObject.SetActive(false);
}

Object Pooling
public class ObjectPool : MonoBehaviour
{
    [SerializeField] private GameObject _prefab;
    [SerializeField] private int _initialSize = 10;

    private Queue<GameObject> _pool = new();

    private void Awake()
    {
        for (int i = 0; i < _initialSize; i++)
        {
            var obj = Instantiate(_prefab);
            obj.SetActive(false);
            _pool.Enqueue(obj);
        }
    }

    public GameObject Get()
    {
        if (_pool.Count == 0)
            return Instantiate(_prefab);

        var pooled = _pool.Dequeue();
        pooled.SetActive(true);
        return pooled;
    }

    public void Return(GameObject obj)
    {
        obj.SetActive(false);
        _pool.Enqueue(obj);
    }
}

Static Batching
gameObject.isStatic = true;

// Or specific flags
GameObjectUtility.SetStaticEditorFlags(gameObject,
    StaticEditorFlags.BatchingStatic |
    StaticEditorFlags.OcclusionStatic);

VR Performance Targets
Metric	Quest 2	Quest 3	PC VR
Draw Calls	<100	<150	<200
Triangles	<100K	<150K	<1M
Frame Time	<14ms (72fps)	<11ms (90fps)	<11ms (90fps)
Texture Memory	<200MB	<500MB	<1GB
LOD Configuration
LOD 0: 100% triangles (0-10m)
LOD 1: 50% triangles (10-25m)
LOD 2: 25% triangles (25-50m)
Culled: 0 triangles (50m+)

Material Atlasing
Before: 20 objects x 20 materials = 20 draw calls (no batching)
After:  20 objects x 1 atlas material = 1 draw call (batched)

Anti-Patterns
Anti-Pattern	Problem	Fix
GetComponent in Update	Expensive every frame	Cache in Awake
Find or FindObjectOfType	Slow, fragile	Inject references or use events
Heavy Update loops	Performance drain	Use events, coroutines, or FixedUpdate
String comparisons for tags	Typo-prone, slow	Use CompareTag or constants
Public fields for everything	No encapsulation	Use [SerializeField] private
Unique material per object	No batching possible	Share materials, use atlases
No LODs	Full detail at any distance	Add LOD groups
Instantiate/Destroy in gameplay	GC spikes, stutters	Object pooling
Realtime lights everywhere	Expensive shadows	Bake lighting, limit realtime
No occlusion culling	Render hidden objects	Bake occlusion data
Checklist
Code Quality
 References cached in Awake
 No GetComponent in Update/FixedUpdate
 No Find methods in runtime code
 ScriptableObjects for shared data
 Events for decoupled communication
 Null checks for destroyable objects
Performance
 Static objects marked static
 Materials shared where possible
 Texture atlases for small props
 LOD groups on significant meshes
 Occlusion culling baked
 Object pooling for spawned objects
 Lighting baked (not all realtime)
Profiling
 Frame Debugger checked for draw calls
 Profiler run for CPU spikes
 Memory Profiler checked for leaks
 Tested on target device (not just editor)
References
references/lifecycle.md — MonoBehaviour lifecycle and execution order
references/profiling.md — Unity Profiler usage and interpretation
Assets
assets/component-checklist.md — Unity component design checklist
assets/vr-performance-limits.md — VR platform performance limits and targets
Weekly Installs
34
Repository
alexanderstephe…aude-hub
GitHub Stars
1
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass