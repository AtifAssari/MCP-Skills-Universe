---
rating: ⭐⭐⭐
title: structurizr-architecture-sync
url: https://skills.sh/site/smithery.ai/structurizr-architecture-sync
---

# structurizr-architecture-sync

skills/smithery.ai/structurizr-architecture-sync
structurizr-architecture-sync
$ npx skills add https://smithery.ai/skills/VilnaCRM-Org/structurizr-architecture-sync
SKILL.md
Structurizr Architecture Synchronization
Context (Input)

Use this skill when:

Adding new components (controllers, handlers, services, repositories)
Creating new entities or aggregates
Modifying component relationships or dependencies
Implementing new architectural patterns (CQRS, events, subscribers)
Adding infrastructure components (databases, caches, message brokers)
Refactoring that changes component structure
After fixing Deptrac violations (may indicate architecture drift)
Creating new bounded contexts or modules
Implementing new API endpoints with significant handlers
Task (Function)

Keep the Structurizr workspace (workspace.dsl) synchronized with codebase changes, ensuring C4 model diagrams accurately represent the current system architecture.

Success Criteria:

workspace.dsl contains all significant components
Component relationships match actual code dependencies
Layer groupings (Application/Domain/Infrastructure) are accurate
Component descriptions reflect current purpose
All infrastructure dependencies are documented
C4 diagrams render without errors (check at http://localhost:${STRUCTURIZR_PORT:-8080})
Quick Start: Update Architecture in 5 Steps

Complete Template: See reference/workspace-template.md for full workspace.dsl structure.

Step 1: Identify Architectural Changes

Determine if your code changes are architecturally significant:

✅ DO update workspace.dsl when adding:

Processors (HTTP/GraphQL handlers)
Command Handlers (CQRS pattern)
Event Subscribers (event-driven patterns)
Entities (core domain objects)
Domain Events (significant business events)
Repositories (data access)
Event Bus or infrastructure services
External dependencies (DB, Cache, Message Broker)

❌ DON'T update for:

Factory classes
Transformer classes (unless critical)
Value objects (unless architecturally significant)
Interface definitions (except hexagonal ports)
Base classes
DTOs and input/output objects
Utility classes and helpers

Target: 15-25 components per diagram for clarity.

Step 2: Add Component to Appropriate Group

Edit workspace.dsl and add component in the correct layer group:

group "Application" {
    newProcessor = component "NewProcessor" "Handles new requests" "RequestProcessor" {
        tags "Item"
    }
}


Layers:

group "Application" - Controllers, Processors, Handlers, Subscribers
group "Domain" - Entities, Domain Events
group "Infrastructure" - Repositories, Event Bus, Infrastructure services

External dependencies (database, cache, messageBroker) go OUTSIDE groups at container level.

See: reference/dsl-syntax.md for complete syntax.

Step 3: Define Relationships

Add relationships showing how your component interacts:

// After all component definitions
newProcessor -> commandHandler "dispatches NewCommand"
commandHandler -> repository "uses"
repository -> database "accesses data"


Common patterns: See reference/relationship-patterns.md

Step 4: Verify Diagram Renders

View the updated diagram:

# Refresh browser (Structurizr Lite auto-reloads)
# Port is configurable via STRUCTURIZR_PORT in .env (default: 8080)
open http://localhost:${STRUCTURIZR_PORT:-8080}
# Navigate to "Diagrams" → "Components_All"


Check for:

No syntax errors displayed
New component appears
Relationships are visible
Component is in correct layer group
Step 5: Position and Commit
Drag components in the UI to improve layout
Click "Save workspace" button (saves to workspace.json)
Commit both files:
git add workspace.dsl workspace.json
git commit -m "feat: update architecture with new processor"

Diagram as Code Workflow
Setup (Already Configured)

Docker: Structurizr Lite runs in docker-compose.override.yml:

structurizr:
  image: structurizr/lite:2024.07.02
  ports:
    - '${STRUCTURIZR_PORT}:8080'
  volumes:
    - ./:/usr/local/structurizr


Access: http://localhost:${STRUCTURIZR_PORT:-8080} (port configurable via .env)

Standard Development Flow
Implement code changes → Add handler, entity, repository
Update workspace.dsl → Add component + relationships
View locally → Refresh browser at configured port
Position components → Drag in UI, click "Save workspace"
Commit together → Code + workspace.dsl + workspace.json in same PR
Manual Positioning in UI

Automatic layout doesn't work well - use manual positioning:

Open Structurizr UI in browser
Navigate to "Diagrams" → "Components_All"
Drag components to arrange (left-to-right flow recommended)
Click "Save workspace" button in top-right
Positions saved to workspace.json in project root
Commit workspace.json with workspace.dsl

Layout best practices:

Processors/Controllers on the left (entry points)
Command Handlers in the middle (business logic)
Repositories to the right of handlers
Database/Cache/Message Broker on far right (external)

Common mistakes: See reference/common-mistakes.md for complete guide.

Reference Documentation
Detailed Guides
C4 Model Fundamentals - Understanding C4 modeling
DSL Syntax Reference - Complete Structurizr DSL syntax
Component Identification - What to document
Relationship Patterns - Common relationship types
Workspace Template - Complete workspace.dsl template
Common Mistakes - Pitfalls and solutions
Examples
Adding CQRS Pattern - Command handlers, events, subscribers
Adding API Endpoint - Controllers, processors, transformers
Adding Domain Entity - Entities, value objects, factories
Refactoring Components - Updating relationships during refactoring
Critical Principles
What Makes a Good Architecture Diagram

Clarity over Completeness:

15-25 components (optimal readability)
Focus on architectural significance
Clear left-to-right or top-to-bottom flow
External dependencies clearly visible

Layer Separation:

Application: Entry points and orchestration
Domain: Business logic and entities
Infrastructure: Technical implementation

Meaningful Relationships:

Show actual code dependencies
Use descriptive labels
Avoid circular dependencies
Alignment with Deptrac

Layer groupings in workspace.dsl MUST match Deptrac configuration:

group "Application"     ↔  Application layer in deptrac.yaml
group "Domain"          ↔  Domain layer in deptrac.yaml
group "Infrastructure"  ↔  Infrastructure layer in deptrac.yaml


This ensures architecture documentation matches enforced boundaries.

Integration with Other Skills

Use this skill after:

implementing-ddd-architecture - After creating domain model
api-platform-crud - After adding API endpoints
deptrac-fixer - After fixing layer violations

Use this skill before:

documentation-sync - Update docs with architecture
ci-workflow - Validate all changes
Troubleshooting
Common Issues

Issue: Structurizr UI shows "Element does not exist" error

Solution: Check component variable names in relationships match the component definitions exactly. See common-mistakes.md.

Issue: Diagram shows components in wrong positions after pull

Solution: Ensure workspace.json is committed along with workspace.dsl. The JSON file stores manual positions.

Issue: DSL syntax validation fails

Solution:

Check balanced braces {}
Verify all components are defined before relationships
Ensure no duplicate variable names
Compare with workspace-template.md

Issue: Too many components (30+), diagram is cluttered

Solution: Follow component-identification.md - aim for 15-25 components. Omit DTOs, utilities, and factories.

Issue: Can't determine if component should be documented

Solution: Use the decision matrix in component-identification.md or the TL;DR section.

External Resources
Structurizr DSL Documentation: https://docs.structurizr.com/dsl
C4 Model: https://c4model.com/
Structurizr Lite: https://docs.structurizr.com/lite
User Service Example (VilnaCRM organization reference): https://github.com/VilnaCRM-Org/user-service/wiki/Design-and-Architecture-Documentation
Weekly Installs
13
Source
smithery.ai/ski…ure-sync
First Seen
Mar 11, 2026