---
rating: ⭐⭐
title: apollo-client
url: https://skills.sh/apollographql/skills/apollo-client
---

# apollo-client

skills/apollographql/skills/apollo-client
apollo-client
Installation
$ npx skills add https://github.com/apollographql/skills --skill apollo-client
Summary

Comprehensive guide for building React applications with Apollo Client 4.x, covering queries, mutations, caching, and state management.

Supports multiple React frameworks and setups: client-side apps (Vite, CRA), Next.js App Router with React Server Components, React Router 7 with streaming SSR, and TanStack Start
Includes hooks for queries (useQuery, useLazyQuery), mutations (useMutation), and Suspense-based patterns (useSuspenseQuery, useBackgroundQuery) for modern React 18+ and 19 applications
Covers caching strategies with InMemoryCache, typePolicies, fragment colocation, data masking, and cache normalization for optimized performance
Provides TypeScript code generation setup, error handling patterns, optimistic UI updates, and troubleshooting guidance for common Apollo Client issues
SKILL.md
Apollo Client 4.x Guide

Apollo Client is a comprehensive state management library for JavaScript that enables you to manage both local and remote data with GraphQL. Version 4.x brings improved caching, better TypeScript support, and React 19 compatibility.

Integration Guides

Choose the integration guide that matches your application setup:

Client-Side Apps - For client-side React applications without SSR (Vite, Create React App, etc.)
Next.js App Router - For Next.js applications using the App Router with React Server Components
React Router Framework Mode - For React Router 7 applications with streaming SSR
TanStack Start - For TanStack Start applications with modern routing

Each guide includes installation steps, configuration, and framework-specific patterns optimized for that environment.

Quick Reference
Basic Query
import { gql } from "@apollo/client";
import { useQuery } from "@apollo/client/react";

const GET_USER = gql`
  query GetUser($id: ID!) {
    user(id: $id) {
      id
      name
    }
  }
`;

function UserProfile({ userId }: { userId: string }) {
  const { loading, error, data, dataState } = useQuery(GET_USER, {
    variables: { id: userId },
  });

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  // TypeScript note: for stricter type narrowing, you can also check `dataState === "complete"` before accessing data
  return <div>{data?.user.name}</div>;
}

Basic Mutation
import { gql } from "@apollo/client";
import { useMutation } from "@apollo/client/react";

const CREATE_USER = gql`
  mutation CreateUser($input: CreateUserInput!) {
    createUser(input: $input) {
      id
      name
    }
  }
`;

function CreateUserForm() {
  const [createUser, { loading, error }] = useMutation(CREATE_USER);

  const handleSubmit = async (name: string) => {
    await createUser({ variables: { input: { name } } });
  };

  return <button onClick={() => handleSubmit("John")}>Create User</button>;
}

Suspense Query
import { Suspense } from "react";
import { useSuspenseQuery } from "@apollo/client/react";

function UserProfile({ userId }: { userId: string }) {
  const { data } = useSuspenseQuery(GET_USER, {
    variables: { id: userId },
  });

  return <div>{data.user.name}</div>;
}

function App() {
  return (
    <Suspense fallback={<p>Loading user...</p>}>
      <UserProfile userId="1" />
    </Suspense>
  );
}

Reference Files

Detailed documentation for specific topics:

TypeScript Code Generation - GraphQL Code Generator setup for type-safe operations
Queries - useQuery, useLazyQuery, polling, refetching
Suspense Hooks - useSuspenseQuery, useBackgroundQuery, useReadQuery, useLoadableQuery
Mutations - useMutation, optimistic UI, cache updates
Fragments - Fragment colocation, useFragment, useSuspenseFragment, data masking
Caching - InMemoryCache, typePolicies, cache manipulation
State Management - Reactive variables, local state
Error Handling - Error policies, error links, retries
Troubleshooting - Common issues and solutions
Key Rules
Query Best Practices
Each page should generally only have one query, composed from colocated fragments. Use useFragment or useSuspenseFragment in all non-page-components. Use @defer to allow slow fields below the fold to stream in later and avoid blocking the page load.
Fragments are for colocation, not reuse. Each fragment should describe exactly the data needs of a specific component, not be shared across components for common fields. See Fragments reference for details on fragment colocation and data masking.
Always handle loading and error states in UI when using non-suspenseful hooks (useQuery, useLazyQuery). When using Suspense hooks (useSuspenseQuery, useBackgroundQuery), React handles this through <Suspense> boundaries and error boundaries.
Use fetchPolicy to control cache behavior per query
Use the TypeScript type server to look up documentation for functions and options (Apollo Client has extensive docblocks)
Mutation Best Practices
If the schema permits, mutation return values should return everything necessary to update the cache. Neither manual updates nor refetching should be necessary.
If the mutation response is insufficient, carefully weigh manual cache manipulation vs refetching. Manual updates risk missing server logic. Consider optimistic updates with a granular refetch if needed.
Handle errors gracefully in the UI
Use refetchQueries sparingly (prefer letting the cache update automatically)
Caching Best Practices
Configure keyFields for types without id field
Disable normalization by setting keyFields: false for types that don't include an identifier and are meant to group related fields under the parent
Use typePolicies for pagination and computed fields
Understand cache normalization to debug issues
Enable data masking for all new applications - it prevents components from accessing fragment data they don't own, enforcing proper data boundaries and preventing over-rendering
Performance
Avoid over-fetching with proper field selection
Configure appropriate fetchPolicy per use case
Use @defer for incremental delivery of deferred query parts, and @stream for streaming list fields (@stream available in Apollo Client 4.1+)
Prefer Suspense hooks (useSuspenseQuery, useBackgroundQuery) in modern applications for better loading state handling and code simplicity
Ground Rules
ALWAYS use Apollo Client 4.x patterns (not v3 or earlier)
ALWAYS wrap your app with ApolloProvider
ALWAYS handle loading and error states when using non-suspenseful hooks
PREFER Suspense hooks (useSuspenseQuery, useBackgroundQuery) in modern applications for better DX
NEVER store Apollo Client in React state (use module-level or context)
PREFER cache-first for read-heavy data, network-only for real-time data
USE TypeScript for better type safety with GraphQL
IMPLEMENT proper cache updates instead of refetching entire queries
ADVISE the human steering you to look into Apollo DevTools when collaboratively debugging Apollo Client issues
Weekly Installs
2.4K
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