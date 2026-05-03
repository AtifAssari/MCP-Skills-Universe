---
rating: ⭐⭐⭐
title: sap-cap-capire
url: https://skills.sh/secondsky/sap-skills/sap-cap-capire
---

# sap-cap-capire

skills/secondsky/sap-skills/sap-cap-capire
sap-cap-capire
Installation
$ npx skills add https://github.com/secondsky/sap-skills --skill sap-cap-capire
SKILL.md
SAP CAP-Capire Development Skill
Related Skills
sap-fiori-tools: Use for UI layer development, Fiori Elements integration, and frontend application generation
sapui5: Use for custom UI development, advanced UI patterns, and freestyle application building
sap-btp-cloud-platform: Use for deployment options, Cloud Foundry/Kyma configuration, and BTP service integration
sap-hana-cli: Use for database management, schema inspection, and HDI container administration
sap-abap: Use for ABAP system integration, external service consumption, and SAP extensions
sap-btp-best-practices: Use for production deployment patterns and architectural guidance
sap-ai-core: Use when adding AI capabilities to CAP applications or integrating with SAP AI services
sap-api-style: Use when documenting CAP OData services or following API documentation standards
Table of Contents
Quick Start
Project Structure
Core Concepts
Database Setup
Deployment
Bundled Resources
Quick Start
Project Initialization
# Install CAP development kit
npm i -g @sap/cds-dk @sap/cds-lsp

# Create new project
cds init <project-name>
cds init <project-name> --add sample,hana

# Start development server with live reload
cds watch

# Add capabilities
cds add hana          # SAP HANA database
cds add sqlite        # SQLite for development
cds add xsuaa         # Authentication
cds add mta           # Cloud Foundry deployment
cds add multitenancy  # SaaS multitenancy
cds add typescript    # TypeScript support

Basic Entity Example
using { cuid, managed } from '@sap/cds/common';

namespace my.bookshop;

entity Books : cuid, managed {
  title       : String(111) not null;
  author      : Association to Authors;
  stock       : Integer;
  price       : Decimal(9,2);
}

entity Authors : cuid, managed {
  name        : String(111);
  books       : Association to many Books on books.author = $self;
}

Basic Service
using { my.bookshop as my } from '../db/schema';

service CatalogService @(path: '/browse') {
  @readonly entity Books as projection on my.Books;
  @readonly entity Authors as projection on my.Authors;
  
  @requires: 'authenticated-user'
  action submitOrder(book: Books:ID, quantity: Integer) returns String;
}

MCP Integration

This skill integrates with the official CAP MCP (Model Context Protocol) server, providing AI agents with live access to your project's compiled CDS model and CAP documentation.

Available MCP Tools:

search_model - Fuzzy search for CDS entities, services, actions, and relationships in your compiled CSN model
search_docs - Semantic search through CAP documentation for syntax, patterns, and best practices

Key Benefits:

Instant Model Discovery: Query your project's entities, associations, and services without reading files
Context-Aware Documentation: Find relevant CAP documentation based on semantic similarity, not keywords
Zero Configuration: No credentials or environment variables required
Offline-Capable: All searches are local (model) or cached (docs)

Setup: See MCP Integration Guide for configuration with Claude Code, opencode, or GitHub Copilot.

Use Cases: See MCP Use Cases for real-world examples with quantified ROI (~$131K/developer/year time savings).

Agent Integration: The specialized agents (cap-cds-modeler, cap-service-developer, cap-project-architect, cap-performance-debugger) automatically use these MCP tools as part of their workflows.

Project Structure
project/
├── app/              # UI content (Fiori, UI5)
├── srv/              # Service definitions (.cds, .js/.ts)
├── db/               # Data models and schema
│   ├── schema.cds    # Entity definitions
│   └── data/         # CSV seed data
├── package.json      # Dependencies and CDS config
└── .cdsrc.json       # CDS configuration (optional)

Core Concepts
CDS Built-in Types
CDS Type	SQL Mapping	Common Use
UUID	NVARCHAR(36)	Primary keys
String(n)	NVARCHAR(n)	Text fields
Integer	INTEGER	Whole numbers
Decimal(p,s)	DECIMAL(p,s)	Monetary values
Boolean	BOOLEAN	True/false
Date	DATE	Calendar dates
Timestamp	TIMESTAMP	Date/time
Common Aspects
using { cuid, managed, temporal } from '@sap/cds/common';
// cuid = UUID key
// managed = createdAt, createdBy, modifiedAt, modifiedBy
// temporal = validFrom, validTo

Event Handlers (Node.js)
// srv/cat-service.js
module.exports = class CatalogService extends cds.ApplicationService {
  init() {
    const { Books } = this.entities;
    
    // Before handlers - validation
    this.before('CREATE', Books, req => {
      if (!req.data.title) req.error(400, 'Title required');
    });
    
    // On handlers - custom logic
    this.on('submitOrder', async req => {
      const { book, quantity } = req.data;
      // Custom business logic
      return { success: true };
    });
    
    return super.init();
  }
}

Basic CQL Queries
const { Books } = cds.entities;

// SELECT with conditions
const books = await SELECT.from(Books)
  .where({ stock: { '>': 0 } })
  .orderBy('title');

// INSERT
await INSERT.into(Books)
  .entries({ title: 'New Book', stock: 10 });

// UPDATE
await UPDATE(Books, bookId)
  .set({ stock: { '-=': 1 } });

Database Setup
Development (SQLite)
// package.json
{
  "cds": {
    "requires": {
      "db": {
        "[development]": { 
          "kind": "sqlite", 
          "credentials": { "url": ":memory:" } 
        },
        "[production]": { "kind": "hana" }
      }
    }
  }
}

Production (SAP HANA)
cds add hana
cds deploy --to hana

Initial Data (CSV)
File location: db/data/my.bookshop-Books.csv
Format: <namespace>-<EntityName>.csv
Auto-loaded on deployment
Deployment
Cloud Foundry
# Add CF deployment support
cds add hana,xsuaa,mta,approuter

# Build and deploy
npm install --package-lock-only
mbt build
cf deploy mta_archives/<project>_<version>.mtar

Multitenancy (SaaS)
cds add multitenancy


Configuration:

{
  "cds": {
    "requires": {
      "multitenancy": true
    }
  }
}

Authorization Examples
// Service-level
@requires: 'authenticated-user'
service CatalogService { ... }

// Entity-level
@restrict: [
  { grant: 'READ' },
  { grant: 'WRITE', to: 'admin' }
]
entity Books { ... }

Bundled Resources
Reference Documentation (22 files)
references/annotations-reference.md - Complete UI annotations reference (10K lines)
references/cdl-syntax.md - Complete CDL syntax reference (503 lines)
references/cql-queries.md - CQL query language guide
references/csn-cqn-cxn.md - Core Schema Notation and query APIs
references/data-privacy-security.md - GDPR and security implementation
references/databases.md - Database configuration and deployment
references/deployment-cf.md - Cloud Foundry deployment details
references/event-handlers-nodejs.md - Node.js event handler patterns
references/extensibility-multitenancy.md - SaaS multitenancy implementation
references/fiori-integration.md - Fiori Elements and UI integration
references/java-runtime.md - Java runtime support
references/localization-temporal.md - i18n and temporal data
references/nodejs-runtime.md - Node.js runtime reference
references/plugins-reference.md - CAP plugins and extensions
references/tools-complete.md - Complete CLI tools reference
references/consuming-services-deployment.md - Service consumption patterns
references/service-definitions.md - Service definition patterns
references/event-handlers-patterns.md - Event handling patterns
references/cql-patterns.md - CQL usage patterns
references/cli-complete.md - Complete CLI reference
references/mcp-integration.md - MCP server setup and usage guide (new)
references/mcp-use-cases.md - Real-world MCP scenarios with quantified ROI (new)
Templates (8 files)
templates/bookshop-schema.cds - Complete data model example
templates/catalog-service.cds - Service definition template
templates/fiori-annotations.cds - UI annotations example
templates/mta.yaml - Multi-target application descriptor
templates/package.json - Project configuration template
templates/service-handler.js - Node.js handler template
templates/service-handler.ts - TypeScript handler template
templates/xs-security.json - XSUAA security configuration
Quick References
CAP Documentation: https://cap.cloud.sap/docs/
CDS Language: https://cap.cloud.sap/docs/cds/
Node.js Runtime: https://cap.cloud.sap/docs/node.js/
Java Runtime: https://cap.cloud.sap/docs/java/
Best Practices: https://cap.cloud.sap/docs/about/best-practices
GitHub Repository: https://github.com/cap-js/docs
Common CLI Commands
cds init [name]           # Create project
cds add <feature>         # Add capability
cds watch                 # Dev server with live reload
cds serve                 # Start server
cds compile <model>       # Compile CDS to CSN/SQL/EDMX
cds deploy --to hana      # Deploy to HANA
cds build                 # Build for deployment
cds env                   # Show configuration
cds repl                  # Interactive REPL
cds version               # Show version info

Best Practices
DO ✓
Use cuid and managed aspects from @sap/cds/common
Keep domain models in db/, services in srv/, UI in app/
Use managed associations (let CAP handle foreign keys)
Design single-purpose services per use case
Start with SQLite, switch to HANA for production
DON'T ✗
Don't use SELECT * - be explicit about projections
Don't bypass CAP's query API with raw SQL
Don't create microservices prematurely
Don't hardcode credentials in config files
Don't write custom OData providers
Version Information
Skill Version: 2.1.2
CAP Version: @sap/cds 9.7.x
MCP Version: @cap-js/mcp-server 0.0.3+
LSP Version: @sap/cds-lsp 9.7.x
Last Verified: 2026-02-22
License: GPL-3.0
Weekly Installs
179
Repository
secondsky/sap-skills
GitHub Stars
241
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass