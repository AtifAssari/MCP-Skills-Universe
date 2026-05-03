---
title: dotnet-core-expert
url: https://skills.sh/jeffallan/claude-skills/dotnet-core-expert
---

# dotnet-core-expert

skills/jeffallan/claude-skills/dotnet-core-expert
dotnet-core-expert
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill dotnet-core-expert
Summary

Expert guidance for building .NET 8 applications with clean architecture, minimal APIs, and cloud-native patterns.

Covers minimal APIs, Entity Framework Core, CQRS with MediatR, JWT authentication, and AOT compilation for .NET 8
Enforces async/await patterns, nullable reference types, record DTOs, and clean architecture layer separation
Includes reference guides for minimal APIs, clean architecture, Entity Framework, authentication, and cloud-native deployment
Provides code examples for MediatR query handlers, DbContext setup, endpoint definitions, and integration testing with WebApplicationFactory
Requires dotnet build and dotnet test verification before proceeding; validates all endpoints and architectural constraints
SKILL.md
.NET Core Expert
Core Workflow
Analyze requirements — Identify architecture pattern, data models, API design
Design solution — Create clean architecture layers with proper separation
Implement — Write high-performance code with modern C# features; run dotnet build to verify compilation — if build fails, review errors, fix issues, and rebuild before proceeding
Secure — Add authentication, authorization, and security best practices
Test — Write comprehensive tests with xUnit and integration testing; run dotnet test to confirm all tests pass — if tests fail, diagnose failures, fix the implementation, and re-run before continuing; verify endpoints with curl or a REST client
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Minimal APIs	references/minimal-apis.md	Creating endpoints, routing, middleware
Clean Architecture	references/clean-architecture.md	CQRS, MediatR, layers, DI patterns
Entity Framework	references/entity-framework.md	DbContext, migrations, relationships
Authentication	references/authentication.md	JWT, Identity, authorization policies
Cloud-Native	references/cloud-native.md	Docker, health checks, configuration
Constraints
MUST DO
Use .NET 8 and C# 12 features
Enable nullable reference types: <Nullable>enable</Nullable> in the .csproj
Use async/await for all I/O operations — e.g., await dbContext.Users.ToListAsync()
Implement proper dependency injection
Use record types for DTOs — e.g., public record UserDto(int Id, string Name);
Follow clean architecture principles
Write integration tests with WebApplicationFactory<Program>
Configure OpenAPI/Swagger documentation
MUST NOT DO
Use synchronous I/O operations
Expose entities directly in API responses
Skip input validation
Use legacy .NET Framework patterns
Mix concerns across architectural layers
Use deprecated EF Core patterns
Code Examples
Minimal API Endpoint
// Program.cs
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddMediatR(cfg => cfg.RegisterServicesFromAssembly(typeof(Program).Assembly));

var app = builder.Build();
app.UseSwagger();
app.UseSwaggerUI();

app.MapGet("/users/{id}", async (int id, ISender sender, CancellationToken ct) =>
{
    var result = await sender.Send(new GetUserQuery(id), ct);
    return result is null ? Results.NotFound() : Results.Ok(result);
})
.WithName("GetUser")
.Produces<UserDto>()
.ProducesProblem(404);

app.Run();

MediatR Query Handler
// Application/Users/GetUserQuery.cs
public record GetUserQuery(int Id) : IRequest<UserDto?>;

public sealed class GetUserQueryHandler : IRequestHandler<GetUserQuery, UserDto?>
{
    private readonly AppDbContext _db;

    public GetUserQueryHandler(AppDbContext db) => _db = db;

    public async Task<UserDto?> Handle(GetUserQuery request, CancellationToken ct) =>
        await _db.Users
            .AsNoTracking()
            .Where(u => u.Id == request.Id)
            .Select(u => new UserDto(u.Id, u.Name))
            .FirstOrDefaultAsync(ct);
}

EF Core DbContext with Async Query
// Infrastructure/AppDbContext.cs
public sealed class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
    public DbSet<User> Users => Set<User>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.ApplyConfigurationsFromAssembly(typeof(AppDbContext).Assembly);
    }
}

// Usage in a service
public async Task<IReadOnlyList<UserDto>> GetAllAsync(CancellationToken ct) =>
    await _db.Users
        .AsNoTracking()
        .Select(u => new UserDto(u.Id, u.Name))
        .ToListAsync(ct);

DTO with Record Type
public record UserDto(int Id, string Name);
public record CreateUserRequest(string Name, string Email);

Output Templates

When implementing .NET features, provide:

Project structure (solution/project files)
Domain models and DTOs
API endpoints or service implementations
Database context and migrations if applicable
Brief explanation of architectural decisions

Documentation

Weekly Installs
2.0K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass