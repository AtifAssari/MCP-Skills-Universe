---
title: apollo-kotlin
url: https://skills.sh/apollographql/skills/apollo-kotlin
---

# apollo-kotlin

skills/apollographql/skills/apollo-kotlin
apollo-kotlin
Installation
$ npx skills add https://github.com/apollographql/skills --skill apollo-kotlin
SKILL.md
Apollo Kotlin Guide

Apollo Kotlin is a strongly typed GraphQL client that generates Kotlin models from your GraphQL operations and schema, that can be used in Android, JVM, and Kotlin Multiplatform projects.

Process

Follow this process when adding or working with Apollo Kotlin:

 Confirm target platforms (Android, JVM, KMP), GraphQL endpoint(s), and how schemas are sourced.
 Configure Gradle and code generation, including custom scalars
 Create a shared ApolloClient with auth, logging, and caching.
 Implement operations.
 Validate behavior with tests and error handling.
Reference Files
Setup - Gradle plugin, schema download, codegen config (including scalars), client configuration (auth, logging, interceptors)
Operations - Queries, mutations, subscriptions, and how to execute them
Caching - Setup and use the normalized cache
Scripts
list-apollo-kotlin-versions.sh - List versions of Apollo Kotlin
list-apollo-kotlin-normalized-cache-versions.sh - List versions of the Apollo Kotlin Normalized Cache library
Key Rules
Use Apollo Kotlin v4+, do not use v3 or older versions.
Keep schema and operations in source control to make builds reproducible.
Weekly Installs
574
Repository
apollographql/skills
GitHub Stars
56
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass