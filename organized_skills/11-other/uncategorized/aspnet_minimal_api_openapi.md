---
rating: ⭐⭐
title: aspnet-minimal-api-openapi
url: https://skills.sh/github/awesome-copilot/aspnet-minimal-api-openapi
---

# aspnet-minimal-api-openapi

skills/github/awesome-copilot/aspnet-minimal-api-openapi
aspnet-minimal-api-openapi
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill aspnet-minimal-api-openapi
Summary

ASP.NET Minimal API endpoints with automatic OpenAPI/Swagger documentation and strong typing.

Organize endpoints using MapGroup(), endpoint filters, and feature-based folder structures for scalability
Define explicit request/response DTOs with validation attributes; use record types and TypedResults for type safety
Leverage .NET 9 built-in OpenAPI support with operation summaries, descriptions, operationIds, and property-level documentation via [Description()]
Apply document and schema transformers to customize OpenAPI output with servers, tags, security schemes, and standardized error responses
SKILL.md
ASP.NET Minimal API with OpenAPI

Your goal is to help me create well-structured ASP.NET Minimal API endpoints with correct types and comprehensive OpenAPI/Swagger documentation.

API Organization
Group related endpoints using MapGroup() extension
Use endpoint filters for cross-cutting concerns
Structure larger APIs with separate endpoint classes
Consider using a feature-based folder structure for complex APIs
Request and Response Types
Define explicit request and response DTOs/models
Create clear model classes with proper validation attributes
Use record types for immutable request/response objects
Use meaningful property names that align with API design standards
Apply [Required] and other validation attributes to enforce constraints
Use the ProblemDetailsService and StatusCodePages to get standard error responses
Type Handling
Use strongly-typed route parameters with explicit type binding
Use Results<T1, T2> to represent multiple response types
Return TypedResults instead of Results for strongly-typed responses
Leverage C# 10+ features like nullable annotations and init-only properties
OpenAPI Documentation
Use the built-in OpenAPI document support added in .NET 9
Define operation summary and description
Add operationIds using the WithName extension method
Add descriptions to properties and parameters with [Description()]
Set proper content types for requests and responses
Use document transformers to add elements like servers, tags, and security schemes
Use schema transformers to apply customizations to OpenAPI schemas
Weekly Installs
8.5K
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