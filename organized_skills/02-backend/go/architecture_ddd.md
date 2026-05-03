---
rating: ⭐⭐
title: architecture-ddd
url: https://skills.sh/7spade/black-tortoise/architecture-ddd
---

# architecture-ddd

skills/7spade/black-tortoise/architecture-ddd
architecture-ddd
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill architecture-ddd
SKILL.md
SKILL: Architecture & DDD Master Guide

This document defines the Domain-Driven Design (DDD) architecture and strict layer boundaries for the project.

🏛️ 1. Layered Architecture (The Law)

Dependencies must flow inward: Presentation → Application → Domain ← Infrastructure.

🔴 Domain Layer (src/app/domain/)
Purity: Zero framework dependencies (No Angular, No Firebase, No RxJS).
Entities: Minimal, intention-free models.
Value Objects: Immutable, validated at creation.
Repositories: Interfaces ONLY (ports).
Aggregates: Transactional boundaries.
Domain Events: Immutable "facts" that have occurred.
🟡 Application Layer (src/app/application/)
Orchestration: Implements Use Cases (Handlers).
State: NgRx Signals (Store) is the source of truth.
Mappers: Domain ↔ DTO / ViewModel conversion.
Ports: Defines repository and service interfaces.
🔵 Infrastructure Layer (src/app/infrastructure/)
Adapters: Implements interfaces defined in the application/domain layers.
Technical: Firebase, HTTP, persistence, logging, external SDKs.
DTOs: Confined to this layer; never leaked to Presentation or Domain.
🟢 Presentation Layer (src/app/presentation/)
UI Only: No business logic.
Signals: Consumes signals from stores.
Standalone: All components are standalone + zone-less.
🧩 2. Tactical DDD Patterns
Repository Pattern
Interface defined in Domain or Application.
Implementation hidden in Infrastructure.
Injection via InjectionToken to ensure loose coupling.
Domain Service
Used when logic involves multiple entities or doesn't naturally fit into one.
Must remain pure (no I/O).
Event-Driven Flow
Append: Persist a command outcome to the store/database.
Publish: Emit event via the EventBus.
React: Other stores or capabilities listen and react.
📦 3. Project Structure & Naming
Layer	Type	Pattern
Domain	Entity	{name}.entity.ts
Application	Store	{name}.store.ts
Infrastructure	Repository	{name}-firestore.repository.ts
Presentation	Component	{name}.component.ts
Alias Imports: Use @domain/*, @application/*, @infrastructure/*.
No Relative Imports: Never import across layers using ../../.
🪒 4. Occam's Razor
Minimalism: Do not add layers or abstractions without necessity.
Cohesion: Keep related logic close.
Decoupling: Minimize dependencies between modules.

Adjudication: TypeScript errors (TS2339, TS2345) regarding cross-layer imports or invalid field access in the Domain are architectural violations—fix the design, do not suppress the error.

Weekly Installs
13
Repository
7spade/black-tortoise
First Seen
Feb 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass