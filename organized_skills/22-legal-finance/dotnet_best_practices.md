---
rating: ⭐⭐⭐
title: dotnet-best-practices
url: https://skills.sh/github/awesome-copilot/dotnet-best-practices
---

# dotnet-best-practices

skills/github/awesome-copilot/dotnet-best-practices
dotnet-best-practices
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill dotnet-best-practices
Summary

Validate .NET/C# code against comprehensive best practices for your solution and project.

Covers 10+ practice areas including XML documentation, design patterns, dependency injection, async/await, testing standards, and error handling
Enforces specific patterns: primary constructors for DI, Command Handler pattern with generics, interface segregation, and Factory pattern for object creation
Includes resource management with ResourceManager for localization, structured logging via Microsoft.Extensions.Logging, and Semantic Kernel integration for AI operations
Requires MSTest with FluentAssertions for testing, strongly-typed configuration with data annotations, and C# 12+ / .NET 8 feature adoption
SKILL.md
.NET/C# Best Practices

Your task is to ensure .NET/C# code in ${selection} meets the best practices specific to this solution/project. This includes:

Documentation & Structure
Create comprehensive XML documentation comments for all public classes, interfaces, methods, and properties
Include parameter descriptions and return value descriptions in XML comments
Follow the established namespace structure: {Core|Console|App|Service}.{Feature}
Design Patterns & Architecture
Use primary constructor syntax for dependency injection (e.g., public class MyClass(IDependency dependency))
Implement the Command Handler pattern with generic base classes (e.g., CommandHandler<TOptions>)
Use interface segregation with clear naming conventions (prefix interfaces with 'I')
Follow the Factory pattern for complex object creation.
Dependency Injection & Services
Use constructor dependency injection with null checks via ArgumentNullException
Register services with appropriate lifetimes (Singleton, Scoped, Transient)
Use Microsoft.Extensions.DependencyInjection patterns
Implement service interfaces for testability
Resource Management & Localization
Use ResourceManager for localized messages and error strings
Separate LogMessages and ErrorMessages resource files
Access resources via _resourceManager.GetString("MessageKey")
Async/Await Patterns
Use async/await for all I/O operations and long-running tasks
Return Task or Task from async methods
Use ConfigureAwait(false) where appropriate
Handle async exceptions properly
Testing Standards
Use MSTest framework with FluentAssertions for assertions
Follow AAA pattern (Arrange, Act, Assert)
Use Moq for mocking dependencies
Test both success and failure scenarios
Include null parameter validation tests
Configuration & Settings
Use strongly-typed configuration classes with data annotations
Implement validation attributes (Required, NotEmptyOrWhitespace)
Use IConfiguration binding for settings
Support appsettings.json configuration files
Semantic Kernel & AI Integration
Use Microsoft.SemanticKernel for AI operations
Implement proper kernel configuration and service registration
Handle AI model settings (ChatCompletion, Embedding, etc.)
Use structured output patterns for reliable AI responses
Error Handling & Logging
Use structured logging with Microsoft.Extensions.Logging
Include scoped logging with meaningful context
Throw specific exceptions with descriptive messages
Use try-catch blocks for expected failure scenarios
Performance & Security
Use C# 12+ features and .NET 8 optimizations where applicable
Implement proper input validation and sanitization
Use parameterized queries for database operations
Follow secure coding practices for AI/ML operations
Code Quality
Ensure SOLID principles compliance
Avoid code duplication through base classes and utilities
Use meaningful names that reflect domain concepts
Keep methods focused and cohesive
Implement proper disposal patterns for resources
Weekly Installs
10.8K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass