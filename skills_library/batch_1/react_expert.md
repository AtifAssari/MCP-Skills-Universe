---
title: react-expert
url: https://skills.sh/jeffallan/claude-skills/react-expert
---

# react-expert

skills/jeffallan/claude-skills/react-expert
react-expert
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill react-expert
Summary

Expert React 18+ and React 19 component development with Server Components, hooks, and state management.

Covers React 19 features including use() hook, useActionState forms, and Server Components in Next.js App Router
Implements custom hooks, state management patterns (Context, Zustand, Redux), and data fetching with TanStack Query
Enforces TypeScript strict mode, error boundaries, proper cleanup, and accessibility standards throughout
Includes performance optimization via memoization, lazy loading, and Suspense boundaries with structured validation workflows
SKILL.md
React Expert

Senior React specialist with deep expertise in React 19, Server Components, and production-grade application architecture.

When to Use This Skill
Building new React components or features
Implementing state management (local, Context, Redux, Zustand)
Optimizing React performance
Setting up React project architecture
Working with React 19 Server Components
Implementing forms with React 19 actions
Data fetching patterns with TanStack Query or use()
Core Workflow
Analyze requirements - Identify component hierarchy, state needs, data flow
Choose patterns - Select appropriate state management, data fetching approach
Implement - Write TypeScript components with proper types
Validate - Run tsc --noEmit; if it fails, review reported errors, fix all type issues, and re-run until clean before proceeding
Optimize - Apply memoization where needed, ensure accessibility; if new type errors are introduced, return to step 4
Test - Write tests with React Testing Library; if any assertions fail, debug and fix before submitting
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Server Components	references/server-components.md	RSC patterns, Next.js App Router
React 19	references/react-19-features.md	use() hook, useActionState, forms
State Management	references/state-management.md	Context, Zustand, Redux, TanStack
Hooks	references/hooks-patterns.md	Custom hooks, useEffect, useCallback
Performance	references/performance.md	memo, lazy, virtualization
Testing	references/testing-react.md	Testing Library, mocking
Class Migration	references/migration-class-to-modern.md	Converting class components to hooks/RSC
Key Patterns
Server Component (Next.js App Router)
// app/users/page.tsx — Server Component, no "use client"
import { db } from '@/lib/db';

interface User {
  id: string;
  name: string;
}

export default async function UsersPage() {
  const users: User[] = await db.user.findMany();

  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

React 19 Form with useActionState
'use client';
import { useActionState } from 'react';

async function submitForm(_prev: string, formData: FormData): Promise<string> {
  const name = formData.get('name') as string;
  // perform server action or fetch
  return `Hello, ${name}!`;
}

export function GreetForm() {
  const [message, action, isPending] = useActionState(submitForm, '');

  return (
    <form action={action}>
      <input name="name" required />
      <button type="submit" disabled={isPending}>
        {isPending ? 'Submitting…' : 'Submit'}
      </button>
      {message && <p>{message}</p>}
    </form>
  );
}

Custom Hook with Cleanup
import { useState, useEffect } from 'react';

function useWindowWidth(): number {
  const [width, setWidth] = useState(() => window.innerWidth);

  useEffect(() => {
    const handler = () => setWidth(window.innerWidth);
    window.addEventListener('resize', handler);
    return () => window.removeEventListener('resize', handler); // cleanup
  }, []);

  return width;
}

Constraints
MUST DO
Use TypeScript with strict mode
Implement error boundaries for graceful failures
Use key props correctly (stable, unique identifiers)
Clean up effects (return cleanup function)
Use semantic HTML and ARIA for accessibility
Memoize when passing callbacks/objects to memoized children
Use Suspense boundaries for async operations
MUST NOT DO
Mutate state directly
Use array index as key for dynamic lists
Create functions inside JSX (causes re-renders)
Forget useEffect cleanup (memory leaks)
Ignore React strict mode warnings
Skip error boundaries in production
Output Templates

When implementing React features, provide:

Component file with TypeScript types
Test file if non-trivial logic
Brief explanation of key decisions
Knowledge Reference

React 19, Server Components, use() hook, Suspense, TypeScript, TanStack Query, Zustand, Redux Toolkit, React Router, React Testing Library, Vitest/Jest, Next.js App Router, accessibility (WCAG)

Documentation

Weekly Installs
2.0K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass