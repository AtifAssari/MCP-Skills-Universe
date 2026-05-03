---
title: nosql-database-design
url: https://skills.sh/aj-geddes/useful-ai-prompts/nosql-database-design
---

# nosql-database-design

skills/aj-geddes/useful-ai-prompts/nosql-database-design
nosql-database-design
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill nosql-database-design
SKILL.md
NoSQL Database Design
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Design scalable NoSQL schemas for MongoDB (document) and DynamoDB (key-value). Covers data modeling patterns, denormalization strategies, and query optimization for NoSQL systems.

When to Use
MongoDB collection design
DynamoDB table and index design
Document structure modeling
Embedding vs. referencing decisions
Query pattern optimization
NoSQL indexing strategies
Data denormalization planning
Quick Start

Minimal working example:

// Single document with embedded arrays
db.createCollection("users");

db.users.insertOne({
  _id: ObjectId("..."),
  email: "john@example.com",
  name: "John Doe",
  createdAt: new Date(),

  // Embedded address
  address: {
    street: "123 Main St",
    city: "New York",
    state: "NY",
    zipCode: "10001",
  },

  // Embedded array of items
  orders: [
    {
      orderId: ObjectId("..."),
      date: new Date(),
      total: 149.99,
    },
    {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Document Structure Design	Document Structure Design
Indexing in MongoDB	Indexing in MongoDB
Schema Validation	Schema Validation
Table Structure	Table Structure
Global Secondary Indexes (GSI)	Global Secondary Indexes (GSI)
DynamoDB Item Operations	DynamoDB Item Operations
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
296
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