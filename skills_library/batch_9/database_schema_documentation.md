---
title: database-schema-documentation
url: https://skills.sh/aj-geddes/useful-ai-prompts/database-schema-documentation
---

# database-schema-documentation

skills/aj-geddes/useful-ai-prompts/database-schema-documentation
database-schema-documentation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill database-schema-documentation
SKILL.md
Database Schema Documentation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create comprehensive database schema documentation including entity relationship diagrams (ERD), table definitions, indexes, constraints, and data dictionaries.

When to Use
Database schema documentation
ERD (Entity Relationship Diagrams)
Data dictionary creation
Table relationship documentation
Index and constraint documentation
Migration documentation
Database design specs
Quick Start

Minimal working example:

# Database Schema Documentation

**Database:** PostgreSQL 14.x
**Version:** 2.0
**Last Updated:** 2025-01-15
**Schema Version:** 20250115120000

## Overview

This database supports an e-commerce application with user management, product catalog, orders, and payment processing.

## Entity Relationship Diagram

```mermaid
erDiagram
    users ||--o{ orders : places
    users ||--o{ addresses : has
    users ||--o{ payment_methods : has
    orders ||--|{ order_items : contains
    orders ||--|| payments : has
    products ||--o{ order_items : includes
    products }o--|| categories : belongs_to
    products ||--o{ product_images : has
    products ||--o{ inventory : tracks

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [users](references/users.md) | users |
| [products](references/products.md) | products |
| [orders](references/orders.md) | orders |
| [order_items](references/orderitems.md) | order_items |
| [Enum Types](references/enum-types.md) | Enum Types, JSONB Structures |

## Best Practices

### ✅ DO

- Document all tables and columns
- Create ERD diagrams
- Document indexes and constraints
- Include sample data
- Document foreign key relationships
- Show JSONB field structures
- Document triggers and functions
- Include migration scripts
- Specify data types precisely
- Document performance considerations

### ❌ DON'T

- Skip constraint documentation
- Forget to version schema changes
- Ignore performance implications
- Skip index documentation
- Forget to document enum values

Weekly Installs
341
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass