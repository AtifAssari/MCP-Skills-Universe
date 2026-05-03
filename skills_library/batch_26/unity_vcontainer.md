---
title: unity-vcontainer
url: https://skills.sh/creator-hian/claude-code-plugins/unity-vcontainer
---

# unity-vcontainer

skills/creator-hian/claude-code-plugins/unity-vcontainer
unity-vcontainer
Installation
$ npx skills add https://github.com/creator-hian/claude-code-plugins --skill unity-vcontainer
SKILL.md
Unity VContainer - High-Performance DI for Unity
Overview

VContainer is a high-performance IoC container for Unity, providing dependency injection patterns for testable and maintainable code.

Core Topics:

Constructor and method injection
Service registration patterns (Singleton, Transient, Scoped)
LifetimeScope hierarchies
MonoBehaviour injection
Factory patterns with DI
Testing with mocks

Foundation Required: unity-csharp-fundamentals (TryGetComponent, FindAnyObjectByType, null-safe coding)

Learning Path: DI fundamentals → VContainer basics → Advanced patterns → Testing

Quick Start
using VContainer;
using VContainer.Unity;

// Define service interface
public interface IPlayerService
{
    void Initialize();
}

// Implement service
public class PlayerService : IPlayerService
{
    public void Initialize() => Debug.Log("Player initialized");
}

// Setup LifetimeScope
public class GameLifetimeScope : LifetimeScope
{
    protected override void Configure(IContainerBuilder builder)
    {
        builder.Register<IPlayerService, PlayerService>(Lifetime.Singleton);
        builder.RegisterComponentInHierarchy<PlayerController>();
    }
}

// Inject into MonoBehaviour
public class PlayerController : MonoBehaviour
{
    [Inject] private readonly IPlayerService mPlayerService;

    void Start() => mPlayerService.Initialize();
}

Key Concepts
Lifetime Scopes
Singleton: One instance per container
Transient: New instance every resolve
Scoped: One instance per scope
Injection Types
Constructor Injection: Preferred for required dependencies
Method Injection: For optional dependencies
Property/Field Injection: Use [Inject] attribute
Reference Documentation
VContainer Best Practices

Core DI patterns:

Registration patterns and lifetime management
LifetimeScope hierarchies
Testing with mock dependencies
VContainer Integration Patterns

Advanced integrations:

MVVM with reactive properties
Cross-framework integration patterns
Best Practices
Register interfaces: Loose coupling and testability
Constructor injection first: Explicit dependencies
Avoid Service Locator: Don't resolve in Update loops
Test with mocks: Use ContainerBuilder in tests
Clear hierarchies: Root → Scene → Local scopes
Weekly Installs
12
Repository
creator-hian/cl…-plugins
GitHub Stars
8
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass