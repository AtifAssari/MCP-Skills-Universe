---
rating: ⭐⭐⭐
title: dotnet-10-csharp-14
url: https://skills.sh/mhagrelius/dotfiles/dotnet-10-csharp-14
---

# dotnet-10-csharp-14

skills/mhagrelius/dotfiles/dotnet-10-csharp-14
dotnet-10-csharp-14
Installation
$ npx skills add https://github.com/mhagrelius/dotfiles --skill dotnet-10-csharp-14
Summary

Modern .NET 10 and C# 14 patterns for minimal APIs, modular monoliths, and resilient applications.

Covers C# 14 syntax (extension blocks, field keyword, null-conditional assignment) and .NET 10 minimal APIs with validation, TypedResults, and modular architecture
Includes security patterns: JWT authentication, CORS, rate limiting, middleware ordering, and RFC 9457 problem details
Provides infrastructure guidance on Options pattern variants (IOptions, IOptionsSnapshot, IOptionsMonitor), HTTP resilience with standard handlers, Channels, health checks, and EF Core
Documents mandatory patterns (always use TypedResults, ValidateOnStart, UtcNow) and anti-patterns to avoid (manual HttpClient, blocking async, N+1 queries)
Includes integration testing with WebApplicationFactory and recommended libraries (MediatR, FluentValidation, Mapster, ErrorOr, Polly, Serilog)
SKILL.md
.NET 10 & C# 14 Best Practices

.NET 10 (LTS, Nov 2025) with C# 14. Covers minimal APIs, not MVC.

Official docs: .NET 10 | C# 14 | ASP.NET Core 10

Detail Files
File	Topics
csharp-14.md	Extension blocks, field keyword, null-conditional assignment
minimal-apis.md	Validation, TypedResults, filters, modular monolith, vertical slices
security.md	JWT auth, CORS, rate limiting, OpenAPI security, middleware order
infrastructure.md	Options, resilience, channels, health checks, caching, Serilog, EF Core, keyed services
testing.md	WebApplicationFactory, integration tests, auth testing
anti-patterns.md	HttpClient, DI captive, blocking async, N+1 queries
libraries.md	MediatR, FluentValidation, Mapster, ErrorOr, Polly, Aspire
Quick Start
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <LangVersion>14</LangVersion>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>

var builder = WebApplication.CreateBuilder(args);

// Core services
builder.Services.AddValidation();
builder.Services.AddProblemDetails();
builder.Services.AddOpenApi();

// Security
builder.Services.AddAuthentication().AddJwtBearer();
builder.Services.AddAuthorization();
builder.Services.AddRateLimiter(opts => { /* see security.md */ });

// Infrastructure
builder.Services.AddHealthChecks();
builder.Services.AddOutputCache();

// Modules
builder.Services.AddUsersModule();

var app = builder.Build();

// Middleware (ORDER MATTERS - see security.md)
app.UseExceptionHandler();
app.UseHttpsRedirection();
app.UseCors();
app.UseRateLimiter();
app.UseAuthentication();
app.UseAuthorization();
app.UseOutputCache();

app.MapOpenApi();
app.MapHealthChecks("/health");
app.MapUsersEndpoints();
app.Run();

Decision Flowcharts
Result vs Exception
digraph {
    "Error type?" [shape=diamond];
    "Expected?" [shape=diamond];
    "Result<T>/ErrorOr" [shape=box];
    "Exception" [shape=box];
    "Error type?" -> "Expected?" [label="domain"];
    "Error type?" -> "Exception" [label="infrastructure"];
    "Expected?" -> "Result<T>/ErrorOr" [label="yes"];
    "Expected?" -> "Exception" [label="no"];
}

IOptions Selection
digraph {
    "Runtime changes?" [shape=diamond];
    "Per-request?" [shape=diamond];
    "IOptions<T>" [shape=box];
    "IOptionsSnapshot<T>" [shape=box];
    "IOptionsMonitor<T>" [shape=box];
    "Runtime changes?" -> "IOptions<T>" [label="no"];
    "Runtime changes?" -> "Per-request?" [label="yes"];
    "Per-request?" -> "IOptionsSnapshot<T>" [label="yes"];
    "Per-request?" -> "IOptionsMonitor<T>" [label="no"];
}

Channel Type
digraph {
    "Trust producer?" [shape=diamond];
    "Can drop?" [shape=diamond];
    "Bounded+Wait" [shape=box,style=filled,fillcolor=lightgreen];
    "Bounded+Drop" [shape=box];
    "Unbounded" [shape=box];
    "Trust producer?" -> "Unbounded" [label="yes"];
    "Trust producer?" -> "Can drop?" [label="no"];
    "Can drop?" -> "Bounded+Drop" [label="yes"];
    "Can drop?" -> "Bounded+Wait" [label="no"];
}

Key Patterns Summary
C# 14 Extension Blocks
extension<T>(IEnumerable<T> source)
{
    public bool IsEmpty => !source.Any();
}

.NET 10 Built-in Validation
builder.Services.AddValidation();
app.MapPost("/users", (UserDto dto) => TypedResults.Ok(dto));

TypedResults (Always Use)
app.MapGet("/users/{id}", async (int id, IUserService svc) =>
    await svc.GetAsync(id) is { } user
        ? TypedResults.Ok(user)
        : TypedResults.NotFound());

Module Pattern
public static class UsersModule
{
    public static IServiceCollection AddUsersModule(this IServiceCollection s) => s
        .AddScoped<IUserService, UserService>();

    public static IEndpointRouteBuilder MapUsersEndpoints(this IEndpointRouteBuilder app)
    {
        var g = app.MapGroup("/api/users").WithTags("Users");
        g.MapGet("/{id}", GetUser.Handle);
        return app;
    }
}

HTTP Resilience
builder.Services.AddHttpClient<IApi, ApiClient>()
    .AddStandardResilienceHandler();

Error Handling (RFC 9457)
builder.Services.AddProblemDetails();
app.UseExceptionHandler();
app.UseStatusCodePages();

MANDATORY Patterns (Always Use These)
Task	✅ ALWAYS Use	❌ NEVER Use
Extension members	C# 14 extension<T>() blocks	Traditional this extension methods
Property validation	C# 14 field keyword	Manual backing fields
Null assignment	obj?.Prop = value	if (obj != null) obj.Prop = value
API returns	TypedResults.Ok()	Results.Ok()
Options validation	.ValidateOnStart()	Missing validation
HTTP resilience	AddStandardResilienceHandler()	Manual Polly configuration
Timestamps	DateTime.UtcNow	DateTime.Now
Quick Reference Card
┌─────────────────────────────────────────────────────────────────┐
│                    .NET 10 / C# 14 PATTERNS                      │
├─────────────────────────────────────────────────────────────────┤
│ EXTENSION PROPERTY:  extension<T>(IEnumerable<T> s) {           │
│                        public bool IsEmpty => !s.Any();         │
│                      }                                          │
├─────────────────────────────────────────────────────────────────┤
│ FIELD KEYWORD:       public string Name {                       │
│                        get => field;                            │
│                        set => field = value?.Trim();            │
│                      }                                          │
├─────────────────────────────────────────────────────────────────┤
│ OPTIONS VALIDATION:  .BindConfiguration(Section)                │
│                      .ValidateDataAnnotations()                 │
│                      .ValidateOnStart();   // CRITICAL!         │
├─────────────────────────────────────────────────────────────────┤
│ HTTP RESILIENCE:     .AddStandardResilienceHandler();           │
├─────────────────────────────────────────────────────────────────┤
│ TYPED RESULTS:       TypedResults.Ok(data)                      │
│                      TypedResults.NotFound()                    │
│                      TypedResults.Created(uri, data)            │
├─────────────────────────────────────────────────────────────────┤
│ ERROR PATTERN:       ErrorOr<User> or user?.Match(...)          │
├─────────────────────────────────────────────────────────────────┤
│ IOPTIONS:            IOptions<T>        → startup, no reload    │
│                      IOptionsSnapshot<T> → per-request reload   │
│                      IOptionsMonitor<T>  → live + OnChange()    │
└─────────────────────────────────────────────────────────────────┘

Anti-Patterns Quick Reference
Anti-Pattern	Fix
new HttpClient()	Inject HttpClient or IHttpClientFactory
Results.Ok()	TypedResults.Ok()
Manual Polly config	AddStandardResilienceHandler()
Singleton → Scoped	Use IServiceScopeFactory
GetAsync().Result	await GetAsync()
Exceptions for flow	Use ErrorOr<T> Result pattern
DateTime.Now	DateTime.UtcNow
Missing .ValidateOnStart()	Always add to Options registration

See anti-patterns.md for complete list.

Libraries Quick Reference
Library	Package	Purpose
MediatR	MediatR	CQRS
FluentValidation	FluentValidation.DependencyInjectionExtensions	Validation
Mapster	Mapster.DependencyInjection	Mapping
ErrorOr	ErrorOr	Result pattern
Polly	Microsoft.Extensions.Http.Resilience	Resilience
Serilog	Serilog.AspNetCore	Logging

See libraries.md for usage examples.

Weekly Installs
1.5K
Repository
mhagrelius/dotfiles
GitHub Stars
2
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass