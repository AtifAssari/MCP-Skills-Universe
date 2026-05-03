---
rating: ⭐⭐
title: ef-core
url: https://skills.sh/github/awesome-copilot/ef-core
---

# ef-core

skills/github/awesome-copilot/ef-core
ef-core
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill ef-core
Summary

Entity Framework Core best practices guide covering design, performance, security, and testing patterns.

Covers eight core areas: DbContext design, entity modeling, performance optimization, migrations, querying strategies, change tracking, security, and testing approaches
Emphasizes practical patterns like DbContextFactory, IEntityTypeConfiguration separation, AsNoTracking() for read-only queries, and compiled queries for frequently executed operations
Includes migration best practices such as descriptive naming, SQL verification before production, and data seeding through migrations
Addresses common pitfalls: N+1 query problems, SQL injection prevention, appropriate DbContext lifetimes, and concurrency control for multi-user scenarios
Recommends testing strategies using in-memory providers for unit tests and SQLite for integration tests
SKILL.md
Entity Framework Core Best Practices

Your goal is to help me follow best practices when working with Entity Framework Core.

Data Context Design
Keep DbContext classes focused and cohesive
Use constructor injection for configuration options
Override OnModelCreating for fluent API configuration
Separate entity configurations using IEntityTypeConfiguration
Consider using DbContextFactory pattern for console apps or tests
Entity Design
Use meaningful primary keys (consider natural vs surrogate keys)
Implement proper relationships (one-to-one, one-to-many, many-to-many)
Use data annotations or fluent API for constraints and validations
Implement appropriate navigational properties
Consider using owned entity types for value objects
Performance
Use AsNoTracking() for read-only queries
Implement pagination for large result sets with Skip() and Take()
Use Include() to eager load related entities when needed
Consider projection (Select) to retrieve only required fields
Use compiled queries for frequently executed queries
Avoid N+1 query problems by properly including related data
Migrations
Create small, focused migrations
Name migrations descriptively
Verify migration SQL scripts before applying to production
Consider using migration bundles for deployment
Add data seeding through migrations when appropriate
Querying
Use IQueryable judiciously and understand when queries execute
Prefer strongly-typed LINQ queries over raw SQL
Use appropriate query operators (Where, OrderBy, GroupBy)
Consider database functions for complex operations
Implement specifications pattern for reusable queries
Change Tracking & Saving
Use appropriate change tracking strategies
Batch your SaveChanges() calls
Implement concurrency control for multi-user scenarios
Consider using transactions for multiple operations
Use appropriate DbContext lifetimes (scoped for web apps)
Security
Avoid SQL injection by using parameterized queries
Implement appropriate data access permissions
Be careful with raw SQL queries
Consider data encryption for sensitive information
Use migrations to manage database user permissions
Testing
Use in-memory database provider for unit tests
Create separate testing contexts with SQLite for integration tests
Mock DbContext and DbSet for pure unit tests
Test migrations in isolated environments
Consider snapshot testing for model changes

When reviewing my EF Core code, identify issues and suggest improvements that follow these best practices.

Weekly Installs
8.6K
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