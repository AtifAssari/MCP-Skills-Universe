---
title: theone-unity-standards
url: https://skills.sh/the1studio/theone-training-skills/theone-unity-standards
---

# theone-unity-standards

skills/the1studio/theone-training-skills/theone-unity-standards
theone-unity-standards
Installation
$ npx skills add https://github.com/the1studio/theone-training-skills --skill theone-unity-standards
SKILL.md
TheOne Studio Unity Development Standards

⚠️ Unity 6 (C# 9): All patterns and examples are compatible with Unity 6, which uses C# 9. No C# 10+ features are used.

Skill Purpose

This skill enforces TheOne Studio's comprehensive Unity development standards with CODE QUALITY FIRST:

Priority 1: Code Quality & Hygiene (MOST IMPORTANT)

Nullable reference types, access modifiers, fix all warnings
Throw exceptions (never log errors)
TheOne.Logging.ILogger (runtime, no guards, no prefixes, no constructor logs) vs Debug.Log (editor only)
readonly/const, nameof, using directive scope
No inline comments (use descriptive names)

Priority 2: Modern C# Patterns

LINQ over loops, extension methods, expression bodies
Null-coalescing operators, pattern matching
Modern C# features (records, init, with)

Priority 3: Unity Architecture

VContainer + SignalBus OR TheOne.DI + Publisher/Subscriber
Data Controllers pattern (NEVER direct data access)
Resource management, UniTask async patterns

Priority 4: Performance & Review

LINQ optimization, allocation prevention
Code review guidelines
When This Skill Triggers
Writing or refactoring Unity C# code
Implementing Unity features with dependency injection
Working with events and signals
Accessing or modifying game data
Reviewing code changes or pull requests
Setting up project architecture
Quick Reference Guide
What Do You Need Help With?
Priority	Task	Reference
🔴 PRIORITY 1: Code Quality (Check FIRST)		
1	Nullable types, access modifiers, warnings, exceptions	Quality & Hygiene ⭐
1	TheOne.Logging.ILogger (no guards, no prefixes, no constructor logs) vs Debug.Log	Quality & Hygiene ⭐
1	readonly/const, nameof, using scope, no inline comments	Quality & Hygiene ⭐
🟡 PRIORITY 2: Modern C# Patterns		
2	LINQ, extension methods, var usage	LINQ Patterns
2	Expression bodies, null-coalescing, pattern matching	Modern C# Features
2	Records, init, with expressions	Modern C# Features
🟢 PRIORITY 3: Unity Architecture		
3	VContainer dependency injection	VContainer DI
3	SignalBus event system	SignalBus Events
3	Data Controllers pattern (NEVER direct data access)	Data Controllers
3	Service/Bridge/Adapter integration	Integration Patterns
3	TheOne.DI + Publisher/Subscriber alternative	TheOne Framework
3	UniTask async/await patterns	UniTask Patterns
🔵 PRIORITY 4: Performance & Review		
4	Performance, LINQ optimization, allocations	Performance
4	Architecture review (DI, events, controllers)	Architecture Review
4	C# quality review (LINQ, null handling)	C# Quality
4	Unity-specific review (components, lifecycle)	Unity Specifics
4	Performance review (allocations, hot paths)	Performance Review
🔴 CRITICAL: Code Quality Rules (CHECK FIRST!)
⚠️ MANDATORY QUALITY STANDARDS

ALWAYS enforce these BEFORE writing any code:

Enable nullable reference types - No nullable warnings allowed
Use least accessible access modifier - private by default
Fix ALL warnings - Zero tolerance for compiler warnings
Throw exceptions for errors - NEVER log errors, throw exceptions
TheOne.Logging.ILogger for runtime - No conditional guards (#if), no prefixes ([prefix]), NEVER in constructors; Debug.Log ONLY for editor scripts
Use readonly for fields - Mark fields that aren't reassigned
Use const for constants - Constants should be const, not readonly
Use nameof for strings - Never hardcode property/parameter names
Using directive in deepest scope - Method-level using when possible
No inline comments - Use descriptive names; code should be self-explanatory

Example: Enforce Quality First

// ✅ EXCELLENT: All quality rules enforced
#nullable enable // 1. Nullable enabled

public sealed class PlayerService
{
    private readonly TheOne.Logging.ILogger logger;
    private const int MaxHealth = 100;

    public PlayerService(TheOne.Logging.ILogger logger)
    {
        this.logger = logger;
    }

    public Player GetPlayer(string id)
    {
        using System.Text.Json;

        return players.TryGetValue(id, out var player)
            ? player
            : throw new KeyNotFoundException($"Player not found: {id}");
    }

    private void LoadGameData()
    {
        this.logger.Info("Game data loaded");
    }
}

#if UNITY_EDITOR
public class EditorTool
{
    public void Process()
    {
        Debug.Log("Processing..."); // 5. Debug.Log OK in editor
    }
}
#endif

⚠️ Unity Architecture Rules (AFTER Quality)
Choose ONE Framework Stack

Choose ONE stack per project:

Option 1: VContainer + SignalBus

✅ VContainer for dependency injection
✅ SignalBus for events
✅ [Preserve] attribute on constructors

Option 2: TheOne.DI + Publisher/Subscriber

✅ TheOne.DI wrapper
✅ IPublisher/ISubscriber for events
✅ [Inject] attribute on constructors

Universal Rules (Both Stacks):

✅ Use Data Controllers (NEVER direct data access)
✅ Use UniTask for async operations
✅ Unload assets in Dispose
✅ TheOne.Logging.ILogger for runtime (no guards, no prefixes, no constructor logs), Debug.Log for editor only
Brief Examples
🔴 Code Quality First
// ✅ EXCELLENT: Quality rules enforced
#nullable enable

public sealed class PlayerController
{
    private readonly TheOne.Logging.ILogger logger;
    private const int MaxRetries = 3;

    public PlayerController(TheOne.Logging.ILogger logger)
    {
        this.logger = logger;
    }

    public Player LoadPlayer(string id)
    {
        if (!File.Exists(id))
            throw new FileNotFoundException($"Player file not found: {id}");

        this.logger.Info($"Loading player {id}");
        return DeserializePlayer(id);
    }
}

#if UNITY_EDITOR
public class EditorHelper
{
    public void Log() => Debug.Log("Editor only"); // Debug.Log OK in editor
}
#endif

🟡 Modern C# Patterns
// ✅ GOOD: LINQ instead of loops
var activeEnemies = allEnemies.Where(e => e.IsActive).ToList();

// ✅ GOOD: Expression bodies
public int Health => this.currentHealth;

// ✅ GOOD: Null-coalescing
var name = playerName ?? "Unknown";

// ✅ GOOD: Pattern matching
if (obj is Player player) player.TakeDamage(10);

Unity Architecture (VContainer)
using UnityEngine.Scripting;
using VContainer.Unity;

public sealed class GameService : IInitializable, IDisposable
{
    private readonly SignalBus signalBus;
    private readonly LevelDataController levelController;

    [Preserve]
    public GameService(SignalBus signalBus, LevelDataController levelController)
    {
        this.signalBus = signalBus;
        this.levelController = levelController;
    }

    void IInitializable.Initialize()
    {
        this.signalBus.Subscribe<WonSignal>(this.OnWon);
    }

    void IDisposable.Dispose()
    {
        this.signalBus.TryUnsubscribe<WonSignal>(this.OnWon);
    }
}

Unity Architecture (TheOne.DI)
public sealed class GameService : IAsyncEarlyLoadable, IDisposable
{
    private readonly IPublisher<WonSignal> publisher;
    private IDisposable? subscription;

    [Inject]
    public GameService(
        IPublisher<WonSignal> publisher,
        ISubscriber<WonSignal> subscriber)
    {
        this.publisher = publisher;
        this.subscription = subscriber.Subscribe(this.OnWon);
    }

    public void Dispose()
    {
        this.subscription?.Dispose();
    }
}

Code Review Checklist
Quick Validation (before committing)

🔴 Code Quality (CHECK FIRST):

 Nullable reference types enabled (#nullable enable)
 All access modifiers correct (private by default)
 Zero compiler warnings
 Exceptions thrown for errors (no error logging)
 TheOne.Logging (runtime) vs Debug.Log (editor only)
 readonly used for non-reassigned fields
 const used for constants
 nameof used instead of string literals
 Using directives in deepest scope
 No inline comments (self-explanatory code)

🟡 Modern C# Patterns:

 LINQ used instead of manual loops
 Expression bodies for simple members
 Null-coalescing operators used
 Pattern matching for type checks
 Modern C# features used where appropriate

🟢 Unity Architecture:

 VContainer/TheOne.DI used correctly
 SignalBus/Publisher-Subscriber used correctly
 Data accessed through Controllers only
 All signals unsubscribed in Dispose
 [Preserve] or [Inject] attribute on constructors

🟢 Unity Specifics:

 Assets loaded are unloaded in Dispose
 No Find/GetComponent in Update/runtime loops
 TryGetComponent used instead of GetComponent + null check
 Lifecycle methods in correct order

🔵 Performance:

 No allocations in Update/FixedUpdate
 LINQ avoided in hot paths
 .ToArray() used instead of .ToList() when not modified
Common Mistakes to Avoid
❌ DON'T:
Ignore nullable warnings → Enable #nullable and fix all warnings
Log errors instead of throwing → Throw exceptions for errors
Use Debug.Log in runtime code → Use TheOne.Logging.ILogger (Debug.Log is editor only)
Add conditional guards to logs → ILogger handles #if internally
Add manual log prefixes → ILogger handles [prefix] automatically
Log in constructors → Never log in constructors (keep fast/side-effect free)
Use logger?.Method() → Use logger.Method() (DI guarantees non-null)
Add verbose logs → Keep only necessary logs
Skip access modifiers → Always use least accessible (private default)
Hardcode strings → Use nameof() for property/parameter names
Leave fields mutable → Use readonly/const where possible
Use Zenject → Use VContainer
Use MessagePipe directly → Use SignalBus
Access data models directly → Use Controllers
Forget to unsubscribe from signals → Implement IDisposable
Add inline comments → Use descriptive names instead
✅ DO:
Enable nullable reference types (#nullable enable)
Throw exceptions for errors (never log errors)
Use TheOne.Logging.ILogger for runtime (no guards, no prefixes, no constructor logs)
Use logger.Method() directly (no null-conditional, DI guarantees non-null)
Debug.Log for editor only (#if UNITY_EDITOR)
Use least accessible modifiers (private by default)
Use descriptive names (no inline comments)
Use nameof() for string literals
Use readonly/const for immutable fields
Use VContainer or TheOne.DI for dependency injection
Use SignalBus or Publisher/Subscriber for all events
Use Controllers for all data access
Always implement IDisposable and unsubscribe
Add [Preserve] or [Inject] to prevent code stripping
Use LINQ for collection operations
Review Severity Levels
🔴 Critical (Must Fix)
Nullable warnings not fixed - Enable #nullable and fix all warnings
Logging errors instead of throwing - Use throw, not log for errors
Debug.Log in runtime code - Must use TheOne.Logging.ILogger (Debug.Log = editor only)
Conditional guards on logs - ILogger handles #if internally, remove guards
Manual log prefixes - ILogger handles [prefix] automatically, remove prefixes
Logging in constructors - Never log in constructors (keep fast/side-effect free)
Null-conditional on logger - Use logger.Method() not logger?.Method()
Missing access modifiers - All members must have explicit modifiers
Compiler warnings ignored - Zero tolerance for warnings
Inline comments - Use descriptive names instead
Using Zenject instead of VContainer
Using MessagePipe instead of SignalBus
Direct data access (not using Controllers)
Memory leaks (not unsubscribing)
Missing IDisposable implementation
🟡 Important (Should Fix)
Missing readonly/const - Fields should be readonly/const when possible
Hardcoded strings - Use nameof() for property/parameter names
Using directives not in deepest scope - Method-level using when possible
Verbose unnecessary logs - Keep only necessary logs
Verbose code instead of LINQ
Missing [Preserve] or [Inject] attribute
Performance issues in hot paths
Missing unit tests for business logic
No XML documentation on public APIs
🟢 Nice to Have (Suggestion)
Could use expression body
Could use null-conditional
Could use pattern matching
Could improve naming
Could simplify with modern C# features
Detailed References
C# Coding Standards
LINQ Patterns - LINQ, extension methods, var usage
Modern C# Features - Expression bodies, null-coalescing, pattern matching, records
Quality & Hygiene - Nullable types, access modifiers, logging, exceptions
Performance Optimizations - Unity patterns, LINQ performance
Unity Architecture
VContainer DI - Complete VContainer dependency injection guide
SignalBus Events - SignalBus event system patterns
Data Controllers - Data Controller implementation
Integration Patterns - Service/Bridge/Adapter for third-party SDKs
TheOne Framework - TheOne.DI + Publisher/Subscriber alternative
UniTask Patterns - Async/await with UniTask
Code Review
Architecture Review - VContainer, SignalBus, Controllers violations
C# Quality Review - LINQ, expression bodies, null handling
Unity Specifics Review - Component access, lifecycle, cleanup
Performance Review - Allocations, LINQ in hot paths
Summary

This skill provides comprehensive Unity development standards for TheOne Studio:

C# Excellence: Modern, concise, professional C# code
Unity Architecture: VContainer+SignalBus OR TheOne.DI+Publisher patterns
Code Quality: Enforced quality, hygiene, and performance rules
Code Review: Complete checklist for pull request reviews

Use the Quick Reference Guide above to navigate to the specific pattern you need.

Weekly Installs
37
Repository
the1studio/theo…g-skills
GitHub Stars
71
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass