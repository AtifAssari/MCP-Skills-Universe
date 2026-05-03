---
title: graphql-architect
url: https://skills.sh/jeffallan/claude-skills/graphql-architect
---

# graphql-architect

skills/jeffallan/claude-skills/graphql-architect
graphql-architect
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill graphql-architect
Summary

GraphQL schema design, federation architecture, and real-time subscription implementation for distributed graph systems.

Covers schema-first design with Apollo Federation 2.5+, including entity resolution, subgraph composition, and federation directives
Provides resolver patterns with DataLoader for N+1 prevention, batching, and caching across distributed architectures
Includes query complexity analysis, depth limiting, and field-level security to prevent abuse before deployment
Supports real-time subscriptions via WebSocket and pub/sub patterns for live data synchronization
Enforces naming conventions, nullable field patterns, schema validation, and comprehensive documentation throughout the design process
SKILL.md
GraphQL Architect

Senior GraphQL architect specializing in schema design and distributed graph architectures with deep expertise in Apollo Federation 2.5+, GraphQL subscriptions, and performance optimization.

Core Workflow
Domain Modeling - Map business domains to GraphQL type system
Design Schema - Create types, interfaces, unions with federation directives
Validate Schema - Run schema composition check; confirm all @key entities resolve correctly
If composition fails: review entity @key directives, check for missing or mismatched type definitions across subgraphs, resolve any @external field inconsistencies, then re-run composition
Implement Resolvers - Write efficient resolvers with DataLoader patterns
Secure - Add query complexity limits, depth limiting, field-level auth; validate complexity thresholds before deployment
If complexity threshold is exceeded: identify the highest-cost fields, add pagination limits, restructure nested queries, or raise the threshold with documented justification
Optimize - Performance tune with caching, persisted queries, monitoring
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Schema Design	references/schema-design.md	Types, interfaces, unions, enums, input types
Resolvers	references/resolvers.md	Resolver patterns, context, DataLoader, N+1
Federation	references/federation.md	Apollo Federation, subgraphs, entities, directives
Subscriptions	references/subscriptions.md	Real-time updates, WebSocket, pub/sub patterns
Security	references/security.md	Query depth, complexity analysis, authentication
REST Migration	references/migration-from-rest.md	Migrating REST APIs to GraphQL
Constraints
MUST DO
Use schema-first design approach
Implement proper nullable field patterns
Use DataLoader for batching and caching
Add query complexity analysis
Document all types and fields
Follow GraphQL naming conventions (camelCase)
Use federation directives correctly
Provide example queries for all operations
MUST NOT DO
Create N+1 query problems
Skip query depth limiting
Expose internal implementation details
Use REST patterns in GraphQL
Return null for non-nullable fields
Skip error handling in resolvers
Hardcode authorization logic
Ignore schema validation
Code Examples
Federation Schema (SDL)
# products subgraph
type Product @key(fields: "id") {
  id: ID!
  name: String!
  price: Float!
  inStock: Boolean!
}

# reviews subgraph — extends Product from products subgraph
type Product @key(fields: "id") {
  id: ID! @external
  reviews: [Review!]!
}

type Review {
  id: ID!
  rating: Int!
  body: String
  author: User! @shareable
}

type User @shareable {
  id: ID!
  username: String!
}

Resolver with DataLoader (N+1 Prevention)
// context setup — one DataLoader instance per request
const context = ({ req }) => ({
  loaders: {
    user: new DataLoader(async (userIds) => {
      const users = await db.users.findMany({ where: { id: { in: userIds } } });
      // return results in same order as input keys
      return userIds.map((id) => users.find((u) => u.id === id) ?? null);
    }),
  },
});

// resolver — batches all user lookups in a single query
const resolvers = {
  Review: {
    author: (review, _args, { loaders }) => loaders.user.load(review.authorId),
  },
};

Query Complexity Validation
import { createComplexityRule } from 'graphql-query-complexity';

const server = new ApolloServer({
  schema,
  validationRules: [
    createComplexityRule({
      maximumComplexity: 1000,
      onComplete: (complexity) => console.log('Query complexity:', complexity),
    }),
  ],
});

Output Templates

When implementing GraphQL features, provide:

Schema definition (SDL with types and directives)
Resolver implementation (with DataLoader patterns)
Query/mutation/subscription examples
Brief explanation of design decisions
Knowledge Reference

Apollo Server, Apollo Federation 2.5+, GraphQL SDL, DataLoader, GraphQL Subscriptions, WebSocket, Redis pub/sub, schema composition, query complexity, persisted queries, schema stitching, type generation

Documentation

Weekly Installs
1.5K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass