---
title: graphql-implementation
url: https://skills.sh/aj-geddes/useful-ai-prompts/graphql-implementation
---

# graphql-implementation

skills/aj-geddes/useful-ai-prompts/graphql-implementation
graphql-implementation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill graphql-implementation
SKILL.md
GraphQL Implementation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement GraphQL APIs with proper schema design, resolver patterns, error handling, and performance optimization for flexible client-server communication.

When to Use
Designing new GraphQL APIs
Creating GraphQL schemas and types
Implementing resolvers and mutations
Adding subscriptions for real-time data
Migrating from REST to GraphQL
Optimizing GraphQL performance
Quick Start

Minimal working example:

type User {
  id: ID!
  email: String!
  firstName: String!
  lastName: String!
  role: UserRole!
  posts: [Post!]!
  createdAt: DateTime!
  updatedAt: DateTime!
}

enum UserRole {
  ADMIN
  USER
  MODERATOR
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  comments: [Comment!]!
  publishedAt: DateTime
  createdAt: DateTime!
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
GraphQL Schema Design	GraphQL Schema Design
Node.js Apollo Server Implementation	Node.js Apollo Server Implementation
Python GraphQL Implementation (Graphene)	Python GraphQL Implementation (Graphene)
Query Examples	Query Examples
Error Handling	Error Handling
Best Practices
✅ DO
Use clear, descriptive field names
Design schemas around client needs
Implement proper error handling
Use input types for mutations
Add subscriptions for real-time data
Cache resolvers efficiently
Validate input data
Use federation for scalability
❌ DON'T
Over-nest queries deeply
Expose internal database IDs
Return sensitive data without authorization
Create overly complex schemas
Forget to handle null values
Ignore N+1 query problems
Skip error messages
Weekly Installs
261
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