---
title: webman-best-practices
url: https://skills.sh/kitephp/webman-design-skills/webman-best-practices
---

# webman-best-practices

skills/kitephp/webman-design-skills/webman-best-practices
webman-best-practices
Installation
$ npx skills add https://github.com/kitephp/webman-design-skills --skill webman-best-practices
SKILL.md

Webman framework best practices following DDD architecture, dependency rules, and PER Coding Style.

Architecture & Dependencies
Controller directly depends on Model, skipping Service layer → See controller-skip-service
Domain layer depends on framework classes (Request, DB, etc.) → See domain-framework-dependency
Service layer has circular dependencies with another Service → See service-circular-dependency
Infrastructure layer not implementing Contract interface → See infrastructure-without-contract
Using Model directly in Service instead of Repository → See service-direct-model-access
Naming Conventions
Using camelCase or PascalCase for directories → See directory-lowercase
Interface without Interface suffix → See interface-naming
Service not following VerbNounService pattern → See service-naming-pattern
Repository implementation without descriptive prefix → See repository-implementation-naming
Namespace not matching directory structure → See namespace-directory-mismatch
Code Style (PER Coding Style)
Missing declare(strict_types=1) at file start → See strict-types-declaration
Not using final class by default → See prefer-final-classes
Not using readonly for immutable properties → See readonly-properties
Missing type declarations for parameters or return types → See complete-type-declarations
Not using constructor property promotion → See constructor-property-promotion
Domain Patterns
Entity without unique identity → See entity-identity
Value object that is mutable → See value-object-immutability
Business logic in Service instead of Domain → See business-logic-in-domain
Not using domain events for side effects → See domain-events
Anemic domain model with only getters/setters → See rich-domain-model
Dependency Injection
Using static methods instead of dependency injection → See avoid-static-methods
Not using constructor injection → See constructor-injection
Service locator pattern instead of dependency injection → See no-service-locator
Weekly Installs
40
Repository
kitephp/webman-…n-skills
GitHub Stars
6
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass