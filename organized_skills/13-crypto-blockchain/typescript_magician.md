---
rating: ⭐⭐
title: typescript-magician
url: https://skills.sh/mcollina/skills/typescript-magician
---

# typescript-magician

skills/mcollina/skills/typescript-magician
typescript-magician
Installation
$ npx skills add https://github.com/mcollina/skills --skill typescript-magician
Summary

Advanced TypeScript type design, generic resolution, and strict typing for complex type challenges.

Eliminates any types by crafting precise generics, conditional types, and type guards tailored to your codebase
Handles complex inference patterns including template literal types, mapped types, branded types, and utility type composition
Diagnoses and resolves TypeScript compiler errors by identifying root causes (unsound inference, missing constraints, implicit any) and validating fixes with tsc --noEmit
Covers advanced patterns: conditional types with infer, function overloads, type narrowing, module augmentation, and variance rules
SKILL.md
When to use

Use this skill for:

TypeScript errors and type challenges
Eliminating any types from codebases
Complex generics and type inference issues
When strict typing is needed
Instructions

When invoked:

Run tsc --noEmit to capture the full error output before making changes
Identify the root cause of type issues (unsound inference, missing constraints, implicit any, etc.)
Craft precise, type-safe solutions using advanced TypeScript features
Eliminate all any types with proper typing — validate each replacement still satisfies call sites
Confirm the fix compiles cleanly with a second tsc --noEmit pass

Capabilities include:

Advanced generics and conditional types
Template literal types and mapped types
Utility types and type manipulation
Brand types and nominal typing
Complex inference patterns
Variance and distribution rules
Module augmentation and declaration merging

For every TypeScript challenge:

Explain the type theory behind the problem
Provide multiple solution approaches when applicable
Show before/after type representations
Include comprehensive type tests
Ensure full IntelliSense support
Quick Examples
Eliminating any with generics

Before

function getProperty(obj: any, key: string): any {
  return obj[key];
}


After

function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
// getProperty({ name: "Alice" }, "name") → inferred as string ✓

Narrowing an unknown API response

Before

async function fetchUser(): Promise<any> {
  const res = await fetch("/api/user");
  return res.json();
}


After

interface User { id: number; name: string }

function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  );
}

async function fetchUser(): Promise<User> {
  const res = await fetch("/api/user");
  const data: unknown = await res.json();
  if (!isUser(data)) throw new Error("Invalid user shape");
  return data;
}

Reference

Read individual rule files for detailed explanations and code examples:

Core Patterns
rules/as-const-typeof.md - Deriving types from runtime values using as const and typeof
rules/array-index-access.md - Accessing array element types using [number] indexing
rules/utility-types.md - Built-in utility types: Parameters, ReturnType, Awaited, Omit, Partial, Record
Advanced Generics
rules/generics-basics.md - Fundamentals of generic types, constraints, and inference
rules/builder-pattern.md - Type-safe builder pattern with chainable methods
rules/deep-inference.md - Achieving deep type inference with F.Narrow and const type parameters
Type-Level Programming
rules/conditional-types.md - Conditional types for type-level if/else logic
rules/infer-keyword.md - Using infer to extract types within conditional types
rules/template-literal-types.md - String manipulation at the type level
rules/mapped-types.md - Creating new types by transforming existing type properties
Type Safety Patterns
rules/opaque-types.md - Brand types and opaque types for type-safe identifiers
rules/type-narrowing.md - Narrowing types through control flow analysis
rules/function-overloads.md - Using function overloads for complex function signatures
Debugging
rules/error-diagnosis.md - Strategies for diagnosing and understanding TypeScript type errors
Weekly Installs
1.1K
Repository
mcollina/skills
GitHub Stars
1.8K
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass