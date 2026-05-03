---
title: dotnet
url: https://skills.sh/stuartf303/sorcha/dotnet
---

# dotnet

skills/stuartf303/sorcha/dotnet
dotnet
Installation
$ npx skills add https://github.com/stuartf303/sorcha --skill dotnet
SKILL.md
.NET 10 / C# 13 Skill

This codebase uses .NET 10 (LTS) with C# 13, configured with strict nullable reference types, implicit usings, and XML documentation. All services follow the same project configuration patterns and share infrastructure through Sorcha.ServiceDefaults.

Quick Start
Project Configuration
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
    <NoWarn>$(NoWarn);CS1591</NoWarn>
  </PropertyGroup>
</Project>

Service Setup Pattern
var builder = WebApplication.CreateBuilder(args);

// Always call AddServiceDefaults first
builder.AddServiceDefaults();

// Add service-specific dependencies
builder.Services.AddScoped<IMyService, MyService>();

// Add JWT authentication (shared from ServiceDefaults)
builder.AddJwtAuthentication();

var app = builder.Build();
app.MapDefaultEndpoints();
app.UseAuthentication();
app.UseAuthorization();

Key Concepts
Concept	Usage	Example
Primary constructors	Services with DI	class MyService(IRepo repo)
Collection expressions	Default values	List<T> Items = []
Required members	DTOs/contracts	public required string Id { get; set; }
Records	Value objects, DTOs	public record PagedResult<T>(...)
Raw string literals	Multi-line docs	"""Markdown content"""
Common Patterns
Global Usings
// GlobalUsings.cs
global using System;
global using System.Collections.Generic;
global using System.Linq;
global using System.Threading;
global using System.Threading.Tasks;
global using Sorcha.MyProject.Domain;  // Project-specific

Test Project Setup
<ItemGroup>
  <Using Include="Xunit" />
  <Using Include="Moq" />
  <Using Include="FluentAssertions" />
</ItemGroup>

See Also
patterns - C# 13 features and code patterns
workflows - Build, test, and deployment workflows
Related Skills
aspire - .NET Aspire orchestration and service defaults
minimal-apis - Endpoint configuration with MapGet/MapPost
xunit - Test project configuration and patterns
entity-framework - EF Core integration with repositories
Documentation Resources

Fetch latest .NET documentation with Context7.

How to use Context7:

Use mcp__context7__resolve-library-id to search for "dotnet"
Prefer website documentation (IDs starting with /websites/) over source code repositories when available
Query with mcp__context7__query-docs using the resolved library ID

Library ID: /websites/learn_microsoft_en-us_dotnet (high reputation, 42K+ snippets)

Recommended Queries:

"C# 13 new features primary constructors"
"collection expressions syntax"
"required members properties"
"nullable reference types"
Weekly Installs
22
Repository
stuartf303/sorcha
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass