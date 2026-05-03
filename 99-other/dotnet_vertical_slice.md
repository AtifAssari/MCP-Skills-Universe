---
title: dotnet-vertical-slice
url: https://skills.sh/akires47/agent-skills/dotnet-vertical-slice
---

# dotnet-vertical-slice

skills/akires47/agent-skills/dotnet-vertical-slice
dotnet-vertical-slice
Installation
$ npx skills add https://github.com/akires47/agent-skills --skill dotnet-vertical-slice
SKILL.md
.NET 10 Vertical Slice Architecture

Organize code by feature, not by layer. Each feature is self-contained with its endpoint, request/response, validation, and handler in a single file.

Project Structure
src/
├── Features/
│   ├── Products/
│   │   ├── GetProduct.cs
│   │   ├── CreateProduct.cs
│   │   └── ProductMapper.cs
│   └── Orders/
│       └── ...
├── Shared/
│   ├── Results/
│   │   ├── Result.cs
│   │   └── Error.cs
│   └── Validation/
│       └── ValidationResult.cs
├── Entities/
└── Program.cs

Feature Slice Pattern

One file per operation containing everything needed:

// Features/Products/CreateProduct.cs
public static class CreateProduct
{
    public sealed record Request(string Name, decimal Price);
    public sealed record Response(int Id, string Name, decimal Price);

    public static async Task<Result<Response>> HandleAsync(
        Request request, AppDbContext db, CancellationToken ct)
    {
        var validation = Validate(request);
        if (!validation.IsValid)
            return validation.ToResult<Response>(null!);

        var product = new Product { Name = request.Name, Price = request.Price };
        db.Products.Add(product);
        await db.SaveChangesAsync(ct);

        return new Response(product.Id, product.Name, product.Price);
    }

    private static ValidationResult Validate(Request request) =>
        ValidationExtensions.Validate()
            .NotEmpty(request.Name, "Name")
            .GreaterThan(request.Price, 0, "Price");

    public static void MapEndpoint(IEndpointRouteBuilder app) => app
        .MapPost("/api/products", async (Request request, AppDbContext db, CancellationToken ct) =>
            (await HandleAsync(request, db, ct)).ToCreatedResponse(r => $"/api/products/{r.Id}"))
        .WithName("CreateProduct")
        .WithTags("Products");
}

Core Principles
Result pattern only - Never throw exceptions, return Result<T> or Result
Static handlers - Use public static async Task<Result<T>> HandleAsync(...)
Inline validation - Validate at handler start, return early on failure
Manual mapping - Use extension methods in *Mapper.cs files
Projections - Use .Select() for queries, avoid loading full entities
References

See detailed implementations in the references/ folder:

Result Pattern - Error types, Result class, HTTP mapping
Validation - ValidationResult, fluent extensions
Feature Examples - CRUD, filtering, pagination
Guidelines
One feature = one file (endpoint + request/response + validation + handler)
Name files by operation: CreateProduct.cs, GetProducts.cs
Keep entities in shared folder (only cross-cutting concern)
Use [AsParameters] for query parameters
Group endpoints with .WithTags() for OpenAPI
Weekly Installs
10
Repository
akires47/agent-skills
First Seen
Jan 24, 2026