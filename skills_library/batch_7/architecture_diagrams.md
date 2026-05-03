---
title: architecture-diagrams
url: https://skills.sh/aj-geddes/useful-ai-prompts/architecture-diagrams
---

# architecture-diagrams

skills/aj-geddes/useful-ai-prompts/architecture-diagrams
architecture-diagrams
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill architecture-diagrams
Summary

Generate system architecture diagrams using Mermaid, PlantUML, C4 models, and flowcharts for technical documentation.

Supports multiple diagram types: system architecture, sequence diagrams, C4 context and component diagrams, deployment diagrams, data flows, and class diagrams
Text-based, version-control-friendly formats that integrate directly into documentation and code repositories
Includes best practices for consistent notation, meaningful color coding, logical grouping with subgraphs, and keeping diagrams synchronized with evolving systems
Reference guides and templates for common patterns like microservices architecture, integration flows, and infrastructure design
SKILL.md
Architecture Diagrams
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create clear, maintainable architecture diagrams using code-based diagramming tools like Mermaid and PlantUML for system design, data flows, and technical documentation.

When to Use
System architecture documentation
C4 model diagrams
Data flow diagrams
Sequence diagrams
Component relationships
Deployment diagrams
Infrastructure architecture
Microservices architecture
Database schemas (visual)
Integration patterns
Quick Start

Minimal working example:

graph TB
    subgraph "Client Layer"
        Web[Web App]
        Mobile[Mobile App]
        CLI[CLI Tool]
    end

    subgraph "API Gateway Layer"
        Gateway[API Gateway<br/>Rate Limiting<br/>Authentication]
    end

    subgraph "Service Layer"
        Auth[Auth Service]
        User[User Service]
        Order[Order Service]
        Payment[Payment Service]
        Notification[Notification Service]
    end

    subgraph "Data Layer"
        UserDB[(User DB<br/>PostgreSQL)]
        OrderDB[(Order DB<br/>PostgreSQL)]
        Cache[(Redis Cache)]
        Queue[Message Queue<br/>RabbitMQ]
    end
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
System Architecture Diagram	System Architecture Diagram
Sequence Diagram	Sequence Diagram
C4 Context Diagram	C4 Context Diagram
Component Diagram	Component Diagram
Deployment Diagram	Deployment Diagram
Data Flow Diagram	Data Flow Diagram
Class Diagram	Class Diagram
Component Diagram	Component Diagram
Deployment Diagram	Deployment Diagram
Best Practices
✅ DO
Use consistent notation and symbols
Include legends for complex diagrams
Keep diagrams focused on one aspect
Use color coding meaningfully
Include titles and descriptions
Version control your diagrams
Use text-based formats (Mermaid, PlantUML)
Show data flow direction clearly
Include deployment details
Document diagram conventions
Keep diagrams up-to-date with code
Use subgraphs for logical grouping
❌ DON'T
Overcrowd diagrams with details
Use inconsistent styling
Skip diagram legends
Create binary image files only
Forget to document relationships
Mix abstraction levels in one diagram
Use proprietary formats
Weekly Installs
898
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass