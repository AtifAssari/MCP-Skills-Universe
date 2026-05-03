---
rating: ⭐⭐
title: mermaid-diagrams
url: https://skills.sh/davila7/claude-code-templates/mermaid-diagrams
---

# mermaid-diagrams

skills/davila7/claude-code-templates/mermaid-diagrams
mermaid-diagrams
Originally fromsoftaworks/agent-toolkit
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill mermaid-diagrams
Summary

Text-based software diagrams for domain modeling, architecture, flows, and database schemas.

Supports nine diagram types: class diagrams, sequence diagrams, flowcharts, entity relationship diagrams, C4 architecture diagrams, state diagrams, git graphs, Gantt charts, and pie/bar charts
All diagrams render from plain-text syntax, making them version-controllable and easy to maintain alongside code
Native support in GitHub, GitLab, VS Code, Notion, Obsidian, and Confluence; exportable to PNG/SVG via Mermaid Live Editor or CLI
Includes detailed references for each diagram type, configuration options for themes and layout, and best practices for keeping diagrams focused and maintainable
SKILL.md
Mermaid Diagramming

Create professional software diagrams using Mermaid's text-based syntax. Mermaid renders diagrams from simple text definitions, making diagrams version-controllable, easy to update, and maintainable alongside code.

Core Syntax Structure

All Mermaid diagrams follow this pattern:

diagramType
  definition content


Key principles:

First line declares diagram type (e.g., classDiagram, sequenceDiagram, flowchart)
Use %% for comments
Line breaks and indentation improve readability but aren't required
Unknown words break diagrams; parameters fail silently
Diagram Type Selection Guide

Choose the right diagram type:

Class Diagrams - Domain modeling, OOP design, entity relationships

Domain-driven design documentation
Object-oriented class structures
Entity relationships and dependencies

Sequence Diagrams - Temporal interactions, message flows

API request/response flows
User authentication flows
System component interactions
Method call sequences

Flowcharts - Processes, algorithms, decision trees

User journeys and workflows
Business processes
Algorithm logic
Deployment pipelines

Entity Relationship Diagrams (ERD) - Database schemas

Table relationships
Data modeling
Schema design

C4 Diagrams - Software architecture at multiple levels

System Context (systems and users)
Container (applications, databases, services)
Component (internal structure)
Code (class/interface level)

State Diagrams - State machines, lifecycle states

Git Graphs - Version control branching strategies

Gantt Charts - Project timelines, scheduling

Pie/Bar Charts - Data visualization

Quick Start Examples
Class Diagram (Domain Model)
classDiagram
    Title -- Genre
    Title *-- Season
    Title *-- Review
    User --> Review : creates
    
    class Title {
        +string name
        +int releaseYear
        +play()
    }
    
    class Genre {
        +string name
        +getTopTitles()
    }

Sequence Diagram (API Flow)
sequenceDiagram
    participant User
    participant API
    participant Database
    
    User->>API: POST /login
    API->>Database: Query credentials
    Database-->>API: Return user data
    alt Valid credentials
        API-->>User: 200 OK + JWT token
    else Invalid credentials
        API-->>User: 401 Unauthorized
    end

Flowchart (User Journey)
flowchart TD
    Start([User visits site]) --> Auth{Authenticated?}
    Auth -->|No| Login[Show login page]
    Auth -->|Yes| Dashboard[Show dashboard]
    Login --> Creds[Enter credentials]
    Creds --> Validate{Valid?}
    Validate -->|Yes| Dashboard
    Validate -->|No| Error[Show error]
    Error --> Login

ERD (Database Schema)
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    PRODUCT ||--o{ LINE_ITEM : includes
    
    USER {
        int id PK
        string email UK
        string name
        datetime created_at
    }
    
    ORDER {
        int id PK
        int user_id FK
        decimal total
        datetime created_at
    }

Detailed References

For in-depth guidance on specific diagram types, see:

references/class-diagrams.md - Domain modeling, relationships (association, composition, aggregation, inheritance), multiplicity, methods/properties
references/sequence-diagrams.md - Actors, participants, messages (sync/async), activations, loops, alt/opt/par blocks, notes
references/flowcharts.md - Node shapes, connections, decision logic, subgraphs, styling
references/erd-diagrams.md - Entities, relationships, cardinality, keys, attributes
references/c4-diagrams.md - System context, container, component diagrams, boundaries
references/advanced-features.md - Themes, styling, configuration, layout options
Best Practices
Start Simple - Begin with core entities/components, add details incrementally
Use Meaningful Names - Clear labels make diagrams self-documenting
Comment Extensively - Use %% comments to explain complex relationships
Keep Focused - One diagram per concept; split large diagrams into multiple focused views
Version Control - Store .mmd files alongside code for easy updates
Add Context - Include titles and notes to explain diagram purpose
Iterate - Refine diagrams as understanding evolves
Configuration and Theming

Configure diagrams using frontmatter:

---
config:
  theme: base
  themeVariables:
    primaryColor: "#ff6b6b"
---
flowchart LR
    A --> B


Available themes: default, forest, dark, neutral, base

Layout options:

layout: dagre (default) - Classic balanced layout
layout: elk - Advanced layout for complex diagrams (requires integration)

Look options:

look: classic - Traditional Mermaid style
look: handDrawn - Sketch-like appearance
Exporting and Rendering

Native support in:

GitHub/GitLab - Automatically renders in Markdown
VS Code - With Markdown Mermaid extension
Notion, Obsidian, Confluence - Built-in support

Export options:

Mermaid Live Editor - Online editor with PNG/SVG export
Mermaid CLI - npm install -g @mermaid-js/mermaid-cli then mmdc -i input.mmd -o output.png
Docker - docker run --rm -v $(pwd):/data minlag/mermaid-cli -i /data/input.mmd -o /data/output.png
Common Pitfalls
Breaking characters - Avoid {} in comments, use proper escape sequences for special characters
Syntax errors - Misspellings break diagrams; validate syntax in Mermaid Live
Overcomplexity - Split complex diagrams into multiple focused views
Missing relationships - Document all important connections between entities
When to Create Diagrams

Always diagram when:

Starting new projects or features
Documenting complex systems
Explaining architecture decisions
Designing database schemas
Planning refactoring efforts
Onboarding new team members

Use diagrams to:

Align stakeholders on technical decisions
Document domain models collaboratively
Visualize data flows and system interactions
Plan before coding
Create living documentation that evolves with code
Weekly Installs
439
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass