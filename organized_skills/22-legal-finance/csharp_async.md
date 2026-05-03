---
rating: ⭐⭐⭐
title: csharp-async
url: https://skills.sh/github/awesome-copilot/csharp-async
---

# csharp-async

skills/github/awesome-copilot/csharp-async
csharp-async
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill csharp-async
Summary

Best practices guide for C# asynchronous programming patterns and pitfalls.

Covers naming conventions (Async suffix), return types (Task, ValueTask, avoid void), and exception handling strategies including ConfigureAwait and Task.FromException
Highlights performance optimization techniques: Task.WhenAll for parallel execution, Task.WhenAny for timeouts, and cancellation token usage
Documents critical pitfalls to avoid: blocking calls like .Wait() and .Result, async void methods outside event handlers, and mixing blocking with async code
Recommends implementation patterns including async command pattern, async streams (IAsyncEnumerable), and task-based asynchronous pattern (TAP) for public APIs
SKILL.md
C# Async Programming Best Practices

Your goal is to help me follow best practices for asynchronous programming in C#.

Naming Conventions
Use the 'Async' suffix for all async methods
Match method names with their synchronous counterparts when applicable (e.g., GetDataAsync() for GetData())
Return Types
Return Task<T> when the method returns a value
Return Task when the method doesn't return a value
Consider ValueTask<T> for high-performance scenarios to reduce allocations
Avoid returning void for async methods except for event handlers
Exception Handling
Use try/catch blocks around await expressions
Avoid swallowing exceptions in async methods
Use ConfigureAwait(false) when appropriate to prevent deadlocks in library code
Propagate exceptions with Task.FromException() instead of throwing in async Task returning methods
Performance
Use Task.WhenAll() for parallel execution of multiple tasks
Use Task.WhenAny() for implementing timeouts or taking the first completed task
Avoid unnecessary async/await when simply passing through task results
Consider cancellation tokens for long-running operations
Common Pitfalls
Never use .Wait(), .Result, or .GetAwaiter().GetResult() in async code
Avoid mixing blocking and async code
Don't create async void methods (except for event handlers)
Always await Task-returning methods
Implementation Patterns
Implement the async command pattern for long-running operations
Use async streams (IAsyncEnumerable) for processing sequences asynchronously
Consider the task-based asynchronous pattern (TAP) for public APIs

When reviewing my C# code, identify these issues and suggest improvements that follow these best practices.

Weekly Installs
8.8K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass