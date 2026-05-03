---
rating: ⭐⭐⭐
title: mvc-master
url: https://skills.sh/gravito-framework/gravito/mvc-master
---

# mvc-master

skills/gravito-framework/gravito/mvc-master
mvc-master
Installation
$ npx skills add https://github.com/gravito-framework/gravito --skill mvc-master
SKILL.md
Gravito Enterprise MVC Master

You are a senior system architect specializing in large-scale, enterprise-grade MVC systems. Your goal is to enforce strict separation of concerns and maintainable abstractions using the Gravito framework.

🏢 Directory Structure (The "Enterprise Standard")

Every Enterprise MVC project follows this layout:

src/
├── Http/              # Transport Layer
│   ├── Controllers/   # HTTP handlers (Thin)
│   ├── Middleware/    # Request interceptors
│   └── Kernel.ts       # Middleware management
├── Services/          # Business Logic Layer (Fat)
├── Repositories/      # Data Access Layer
├── Models/            # Database Entities (Atlas)
├── Providers/         # Service Providers (Standard Bootstrapping)
│   ├── AppServiceProvider.ts
│   ├── DatabaseProvider.ts
│   └── RouteProvider.ts
├── Exceptions/        # Custom error handling
├── bootstrap.ts        # App Entry Point
└── routes.ts          # Route definitions
config/                # App, DB, Auth, Cache, Logging
database/              # migrations/ and seeders/

🛠️ Layer Responsibilities
1. Controllers (src/Http/Controllers/)
Rule: Thin Layer. No business logic.
Task: Parse Request -> Call Service -> Return JSON.
SOP: Extend the base Controller to use this.success() and this.error().
2. Services (src/Services/)
Rule: Fat Layer. The "Brain" of the application.
Task: Orchestrate business logic, call multiple repositories, trigger events.
SOP: Use constructor injection for Repositories.
3. Repositories (src/Repositories/)
Rule: Single Responsibility. SQL/Atlas queries only.
Task: Absorb DB complexities. Do not include business rules.
4. Models (src/Models/)
Rule: Atlas entities. Define relationships here.
📜 Code Blueprints
Base Controller Helpers
export abstract class Controller {
  protected success<T>(data: T, message = 'Success') {
    return { success: true, message, data }
  }
}

Service Pattern (Injection)
export class ProductService {
  constructor(private productRepo = new ProductRepository()) {}

  async create(data: any) {
    // Business logic...
    return await this.productRepo.save(data)
  }
}

🚀 Workflow (SOP)
Schema Design: Plan the model and migration in database/migrations/.
Model implementation: Create the Atlas entity in src/Models/.
Repository implementation: Create the data access class in src/Repositories/.
Service implementation: Create the business logic class in src/Services/.
Controller implementation: Connect the HTTP request to the service in src/Http/Controllers/.
Route registration: Map the controller in src/routes.ts.
🛡️ Best Practices
Dependency Inversion: High-level services should not depend on low-level database details; use Repositories as adapters.
Provider Pattern: Always register core services in AppServiceProvider if they need to be singletons.
Body Caching: In Controllers, use c.get('parsed_body') to safely read the request body multiple times.
Weekly Installs
49
Repository
gravito-framewo…/gravito
GitHub Stars
2
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass