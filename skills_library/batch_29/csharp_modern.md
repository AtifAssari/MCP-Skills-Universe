---
title: csharp-modern
url: https://skills.sh/phrazzld/claude-config/csharp-modern
---

# csharp-modern

skills/phrazzld/claude-config/csharp-modern
csharp-modern
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill csharp-modern
SKILL.md
Modern C#

.NET 8+, nullable enabled, async-first, records for data.

Async Patterns

Always use async/await for I/O. Always pass CancellationToken:

public async Task<User?> GetUserAsync(
    int id,
    CancellationToken cancellationToken = default)
{
    using var connection = await _factory
        .CreateConnectionAsync(cancellationToken)
        .ConfigureAwait(false);

    return await connection
        .QuerySingleOrDefaultAsync<User>(sql, cancellationToken: cancellationToken)
        .ConfigureAwait(false);
}


ConfigureAwait(false) in library code. Never block on async (.Result, .Wait()).

Nullable Reference Types

Enable project-wide. Treat warnings as errors:

<Nullable>enable</Nullable>
<TreatWarningsAsErrors>true</TreatWarningsAsErrors>


Explicit nullability:

// Nullable when user might not exist
Task<User?> GetByIdAsync(int id);

// Non-nullable with exception on not found
Task<User> GetRequiredByIdAsync(int id);

// Handle nulls explicitly
if (user is not null) { ProcessUser(user); }
var name = user?.Name ?? "Anonymous";

Records & Immutability

Records for DTOs and value types:

// DTO
public record CreateOrderRequest(
    string CustomerId,
    IReadOnlyList<OrderItemDto> Items);

// Domain entity
public record class Order
{
    public string Id { get; init; }
    public OrderStatus Status { get; init; }

    public Order Ship() => this with { Status = OrderStatus.Shipped };
}

// Value type (<16 bytes)
public readonly record struct Money(decimal Amount, string Currency);


Never expose mutable collections. Use IReadOnlyList<T>.

Pattern Matching

Switch expressions over if-else chains:

public decimal CalculateDiscount(object discount) => discount switch
{
    decimal amount => amount,
    int percentage => percentage / 100m,
    string code => GetDiscountForCode(code),
    _ => throw new ArgumentException("Unsupported type")
};

public string GetShipping(Order order) => order switch
{
    { TotalAmount: > 100, Customer.IsPremium: true } => "Free Express",
    { TotalAmount: > 100 } => "Free Standard",
    _ => "Standard"
};

Project Setup
<!-- Directory.Build.props -->
<PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <LangVersion>12.0</LangVersion>
    <Nullable>enable</Nullable>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
    <EnableNETAnalyzers>true</EnableNETAnalyzers>
    <AnalysisLevel>latest-recommended</AnalysisLevel>
</PropertyGroup>

Anti-Patterns
Blocking on async (.Result, .Wait())
async void outside event handlers
Missing ConfigureAwait(false) in libraries
null! without documented justification
Mutable DTOs with public setters
Switch statements over switch expressions
Legacy .csproj or packages.config
Weekly Installs
23
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass