---
title: apollo-federation
url: https://skills.sh/apollographql/skills/apollo-federation
---

# apollo-federation

skills/apollographql/skills/apollo-federation
apollo-federation
Installation
$ npx skills add https://github.com/apollographql/skills --skill apollo-federation
SKILL.md
Apollo Federation Schema Authoring

Apollo Federation enables composing multiple GraphQL APIs (subgraphs) into a unified supergraph.

Federation 2 Schema Setup

Every Federation 2 subgraph must opt-in via @link:

extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.12",
        import: ["@key", "@shareable", "@external", "@requires", "@provides"])


Import only the directives your subgraph uses.

Core Directives Quick Reference
Directive	Purpose	Example
@key	Define entity with unique key	type Product @key(fields: "id")
@shareable	Allow multiple subgraphs to resolve field	type Position @shareable { x: Int! }
@external	Reference field from another subgraph	weight: Int @external
@requires	Computed field depending on external fields	shippingCost: Int @requires(fields: "weight")
@provides	Conditionally resolve external field	@provides(fields: "name")
@override	Migrate field to this subgraph	@override(from: "Products")
@inaccessible	Hide from API schema	internalId: ID! @inaccessible
@interfaceObject	Add fields to entity interface	type Media @interfaceObject
Reference Files

Detailed documentation for specific topics:

Directives - All federation directives with syntax, examples, and rules
Schema Patterns - Multi-subgraph patterns and recipes
Composition - Composition rules, error codes, and debugging
Key Patterns
Entity Definition
type Product @key(fields: "id") {
  id: ID!
  name: String!
  price: Int
}

Entity Contributions Across Subgraphs
# Products subgraph
type Product @key(fields: "id") {
  id: ID!
  name: String!
  price: Int
}

# Reviews subgraph
type Product @key(fields: "id") {
  id: ID!
  reviews: [Review!]!
  averageRating: Float
}

Computed Fields with @requires
type Product @key(fields: "id") {
  id: ID!
  size: Int @external
  weight: Int @external
  shippingEstimate: String @requires(fields: "size weight")
}

Value Types with @shareable
type Money @shareable {
  amount: Int!
  currency: String!
}

Entity Stub (Reference Without Contributing)
type Product @key(fields: "id", resolvable: false) {
  id: ID!
}

Ground Rules
ALWAYS use Federation 2.x syntax with @link directive
ALWAYS import only the directives your subgraph uses
NEVER use @shareable without ensuring all subgraphs return identical values for that field
PREFER @key with single ID field for simple entity identification
USE rover supergraph compose to validate composition locally
USE rover subgraph check to validate against production supergraph
Weekly Installs
624
Repository
apollographql/skills
GitHub Stars
56
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass