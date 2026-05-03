---
title: database-schema-design
url: https://skills.sh/aj-geddes/useful-ai-prompts/database-schema-design
---

# database-schema-design

skills/aj-geddes/useful-ai-prompts/database-schema-design
database-schema-design
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill database-schema-design
SKILL.md
Database Schema Design
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Design scalable, normalized database schemas with proper relationships, constraints, and data types. Includes normalization techniques, relationship patterns, and constraint strategies.

When to Use
New database schema design
Data model planning
Table structure definition
Relationship design (1:1, 1:N, N:N)
Normalization analysis
Constraint and trigger planning
Performance optimization at schema level
Quick Start

PostgreSQL - Eliminate Repeating Groups:

-- NOT 1NF: repeating group in single column
CREATE TABLE orders_bad (
  id UUID PRIMARY KEY,
  customer_name VARCHAR(255),
  product_ids VARCHAR(255)  -- "1,2,3" - repeating group
);

-- 1NF: separate table for repeating data
CREATE TABLE orders (
  id UUID PRIMARY KEY,
  customer_name VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE order_items (
  id UUID PRIMARY KEY,
  order_id UUID NOT NULL,
  product_id UUID NOT NULL,
  quantity INTEGER NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
);

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
First Normal Form (1NF)	First Normal Form (1NF)
Second Normal Form (2NF)	Second Normal Form (2NF)
Third Normal Form (3NF)	Third Normal Form (3NF)
Entity-Relationship Patterns	Entity-Relationship Patterns
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
347
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