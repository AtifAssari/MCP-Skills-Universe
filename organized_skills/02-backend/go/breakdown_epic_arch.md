---
rating: ⭐⭐
title: breakdown-epic-arch
url: https://skills.sh/github/awesome-copilot/breakdown-epic-arch
---

# breakdown-epic-arch

skills/github/awesome-copilot/breakdown-epic-arch
breakdown-epic-arch
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill breakdown-epic-arch
Summary

Architectural planning prompt for translating product requirements into modular, scalable technical specifications.

Generates comprehensive Epic Architecture Specifications in Markdown, including system diagrams, feature lists, and technology stack recommendations
Enforces domain-driven design patterns with Docker containerization, TypeScript/Next.js, Turborepo monorepos, tRPC APIs, and Stack Auth authentication
Produces Mermaid diagrams spanning user, application, service, data, and infrastructure layers with synchronous and asynchronous flow visualization
Includes technical value assessment and t-shirt sizing estimates to guide development planning and resource allocation
SKILL.md
Epic Architecture Specification Prompt
Goal

Act as a Senior Software Architect. Your task is to take an Epic PRD and create a high-level technical architecture specification. This document will guide the development of the epic, outlining the major components, features, and technical enablers required.

Context Considerations
The Epic PRD from the Product Manager.
Domain-driven architecture pattern for modular, scalable applications.
Self-hosted and SaaS deployment requirements.
Docker containerization for all services.
TypeScript/Next.js stack with App Router.
Turborepo monorepo patterns.
tRPC for type-safe APIs.
Stack Auth for authentication.

Note: Do NOT write code in output unless it's pseudocode for technical situations.

Output Format

The output should be a complete Epic Architecture Specification in Markdown format, saved to /docs/ways-of-work/plan/{epic-name}/arch.md.

Specification Structure
1. Epic Architecture Overview
A brief summary of the technical approach for the epic.
2. System Architecture Diagram

Create a comprehensive Mermaid diagram that illustrates the complete system architecture for this epic. The diagram should include:

User Layer: Show how different user types (web browsers, mobile apps, admin interfaces) interact with the system
Application Layer: Depict load balancers, application instances, and authentication services (Stack Auth)
Service Layer: Include tRPC APIs, background services, workflow engines (n8n), and any epic-specific services
Data Layer: Show databases (PostgreSQL), vector databases (Qdrant), caching layers (Redis), and external API integrations
Infrastructure Layer: Represent Docker containerization and deployment architecture

Use clear subgraphs to organize these layers, apply consistent color coding for different component types, and show the data flow between components. Include both synchronous request paths and asynchronous processing flows where relevant to the epic.

3. High-Level Features & Technical Enablers
A list of the high-level features to be built.
A list of technical enablers (e.g., new services, libraries, infrastructure) required to support the features.
4. Technology Stack
A list of the key technologies, frameworks, and libraries to be used.
5. Technical Value
Estimate the technical value (e.g., High, Medium, Low) with a brief justification.
6. T-Shirt Size Estimate
Provide a high-level t-shirt size estimate for the epic (e.g., S, M, L, XL).
Context Template
Epic PRD: [The content of the Epic PRD markdown file]
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