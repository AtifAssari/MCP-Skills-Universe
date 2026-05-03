---
rating: ⭐⭐⭐
title: graphql-operations
url: https://skills.sh/apollographql/skills/graphql-operations
---

# graphql-operations

skills/apollographql/skills/graphql-operations
graphql-operations
Installation
$ npx skills add https://github.com/apollographql/skills --skill graphql-operations
Summary

Best practices guide for writing efficient, type-safe GraphQL operations and organizing them with fragments.

Covers queries, mutations, subscriptions, and fragments with naming conventions, variable syntax, and directive usage
Emphasizes core principles: request only needed fields, name all operations, use variables instead of hardcoded values, and include id fields for cacheability
Recommends colocating fragments with components and using @include/@skip directives for conditional field selection
Compatible with any GraphQL client (Apollo Client, urql, Relay) and includes reference documentation for queries, mutations, fragments, variables, and tooling
SKILL.md
GraphQL Operations Guide

This guide covers best practices for writing GraphQL operations (queries, mutations, subscriptions) as a client developer. Well-written operations are efficient, type-safe, and maintainable.

Operation Basics
Query Structure
query GetUser($id: ID!) {
  user(id: $id) {
    id
    name
    email
  }
}

Mutation Structure
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    id
    title
    createdAt
  }
}

Subscription Structure
subscription OnMessageReceived($channelId: ID!) {
  messageReceived(channelId: $channelId) {
    id
    content
    sender {
      id
      name
    }
  }
}

Quick Reference
Operation Naming
Pattern	Example
Query	GetUser, ListPosts, SearchProducts
Mutation	CreateUser, UpdatePost, DeleteComment
Subscription	OnMessageReceived, OnUserStatusChanged
Variable Syntax
# Required variable
query GetUser($id: ID!) { ... }

# Optional variable with default
query ListPosts($first: Int = 20) { ... }

# Multiple variables
query SearchPosts($query: String!, $status: PostStatus, $first: Int = 10) { ... }

Fragment Syntax
# Define fragment
fragment UserBasicInfo on User {
  id
  name
  avatarUrl
}

# Use fragment
query GetUser($id: ID!) {
  user(id: $id) {
    ...UserBasicInfo
    email
  }
}

Directives
query GetUser($id: ID!, $includeEmail: Boolean!) {
  user(id: $id) {
    id
    name
    email @include(if: $includeEmail)
  }
}

query GetPosts($skipDrafts: Boolean!) {
  posts {
    id
    title
    draft @skip(if: $skipDrafts)
  }
}

Key Principles
1. Request Only What You Need
# Good: Specific fields
query GetUserName($id: ID!) {
  user(id: $id) {
    id
    name
  }
}

# Avoid: Over-fetching
query GetUser($id: ID!) {
  user(id: $id) {
    id
    name
    email
    bio
    posts {
      id
      title
      content
      comments {
        id
      }
    }
    followers {
      id
      name
    }
    # ... many unused fields
  }
}

2. Name All Operations
# Good: Named operation
query GetUserPosts($userId: ID!) {
  user(id: $userId) {
    posts {
      id
      title
    }
  }
}

# Avoid: Anonymous operation
query {
  user(id: "123") {
    posts {
      id
      title
    }
  }
}

3. Use Variables, Not Inline Values
# Good: Variables
query GetUser($id: ID!) {
  user(id: $id) {
    id
    name
  }
}

# Avoid: Hardcoded values
query {
  user(id: "123") {
    id
    name
  }
}

4. Colocate Fragments with Components
// UserAvatar.tsx
export const USER_AVATAR_FRAGMENT = gql`
  fragment UserAvatar on User {
    id
    name
    avatarUrl
  }
`;

function UserAvatar({ user }) {
  return <img src={user.avatarUrl} alt={user.name} />;
}

Reference Files

Detailed documentation for specific topics:

Queries - Query patterns and optimization
Mutations - Mutation patterns and error handling
Fragments - Fragment organization and reuse
Variables - Variable usage and types
Tooling - Code generation and linting
Ground Rules
ALWAYS name your operations (no anonymous queries/mutations)
ALWAYS use variables for dynamic values
ALWAYS request only the fields you need
ALWAYS include id field for cacheable types
NEVER hardcode values in operations
NEVER duplicate field selections across files
PREFER fragments for reusable field selections
PREFER colocating fragments with components
USE descriptive operation names that reflect purpose
USE @include/@skip for conditional fields
Weekly Installs
1.4K
Repository
apollographql/skills
GitHub Stars
56
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass