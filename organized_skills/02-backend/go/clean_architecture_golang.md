---
rating: ⭐⭐
title: clean-architecture-golang
url: https://skills.sh/gabihert/finance-tracker-e2e/clean-architecture-golang
---

# clean-architecture-golang

skills/gabihert/finance-tracker-e2e/clean-architecture-golang
clean-architecture-golang
Installation
$ npx skills add https://github.com/gabihert/finance-tracker-e2e --skill clean-architecture-golang
SKILL.md
Custom Clean Architecture Implementation Guide

Expert guidance for implementing features using this project's custom Clean Architecture pattern with Golang. This is NOT Uncle Bob's standard Clean Architecture - it's a specialized adaptation.

Architecture Overview

Four layers with strict dependency rules:

Integration → Application → Domain ← Infrastructure


Dependency Rule: Inner layers NEVER depend on outer layers.

🚨 Critical Rules
MUST DO
START with BDD feature file - Never skip test-first development
Integration adapters MUST implement usecase interfaces - Enable type casting
Use context.Context as first parameter - Always
Convert at boundaries - DTO↔Entity↔Model
Follow error code format - PREFIX-XXYYYY
Type cast repositories to usecases - In dependency injection
NEVER DO
Skip BDD test creation - Tests come first
Create adapters without usecase interfaces - Will break dependency injection
Put business logic in controllers/repositories - Only in services
Use DTOs in domain/application - Only in integration layer
Access database from services - Only through usecases
Create circular dependencies - Dependencies flow inward only
Implementation Workflow
Step 1: Create BDD Test (MANDATORY)

Start here ALWAYS. Location: /test/integration/features/

Feature: Create entity functionality
  Scenario: Create entity success
    When I call "POST" "/v1/entities" with payload
    Then status should be 201
    And db should contain entity

Step 2: Domain Layer

Entity (/internal/domain/entity/)

Simple structs, NO logic
Audit fields (CreatedAt, UpdatedAt)

Errors (/internal/domain/error/)

Format: PREFIX-XXYYYY
One error per file

Enums (/internal/domain/enums/)

String types
SCREAMING_SNAKE_CASE values
Step 3: Application Layer

Adapter Interface (/internal/application/adapter/)

Service contracts
Use domain entities

UseCase Interfaces (/internal/application/usecase/)

Atomic operations
FindX, SaveX, UpdateX, DeleteX

Service Implementation (/internal/application/service/)

Business logic HERE
Orchestrate usecases
Step 4: Integration Layer

Adapter Interfaces (/internal/integration/adapter/)

type Repository interface {
    usecase.Find    // MUST embed
    usecase.Save    // MUST embed
}


DTOs (/internal/integration/entrypoint/dto/)

Request/Response structs
ToEntity() methods
Validation tags

Controller (/internal/integration/entrypoint/controller/)

Handle HTTP
DTO↔Entity conversion

Model (/internal/integration/persistence/model/)

GORM annotations
ToEntity() methods

Repository (/internal/integration/persistence/)

Implements usecase interfaces
Entity↔Model conversion
Step 5: Infrastructure Layer

Dependency Injection (/internal/infra/dependency/injector.go)

// Type cast repository to usecase
usecase.Find(i.GetRepository())


Router (/internal/infra/server/router/router.go)

Add routes
Validation middleware
Step 6: Run Tests
make test-integration

Quick Patterns
Integration Adapter Pattern (CRITICAL)
// Application defines need
type FindProduct interface {
    FindById(ctx, id) (*entity, error)
}

// Integration MUST implement
type ProductRepository interface {
    usecase.FindProduct  // EMBED!
}

// Type cast in DI
usecase.FindProduct(repository)

Error Codes
CLI-01409 = Client conflict (409)
USR-01404 = User not found (404)
PRD-02500 = Product server error (500)
Conversion Flow
Request → DTO → Entity → Model → DB
Response ← DTO ← Entity ← Model ← DB

Reference Documentation

Detailed guides in references/:

Layer Implementation - Complete layer examples
Critical Patterns - Must-know patterns
Implementation Workflow - Step-by-step guide
Templates

Ready-to-use templates in assets/:

entity-template.go - Domain entity template
service-template.go - Application service template
repository-template.go - Repository template
Implementation Checklist

Before starting any feature:

 BDD feature file exists
 Domain entity defined
 Domain errors created
 Application adapter interface defined
 Application usecases created
 Application service implemented
 Integration adapters created WITH usecase interfaces
 DTOs with ToEntity() methods
 Controller handling HTTP
 Model with ToEntity() method
 Repository implementing usecases
 Dependencies wired in injector
 Routes added to router
 Tests passing
Common Mistakes to Avoid
Forgetting usecase interfaces on adapters - Breaks type casting
Business logic in wrong layer - Only in services
Wrong dependency direction - Check imports
Missing BDD test - Always start with test
Wrong error code format - Use PREFIX-XXYYYY
Not converting at boundaries - DTO↔Entity↔Model
Example Implementations

Study these existing implementations:

Client: /internal/{domain,application,integration}/*/client*.go
User: /internal/{domain,application,integration}/*/user*.go
Forest: /internal/{domain,application,integration}/*/forest*.go
Weekly Installs
12
Repository
gabihert/financ…cker-e2e
First Seen
Feb 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass