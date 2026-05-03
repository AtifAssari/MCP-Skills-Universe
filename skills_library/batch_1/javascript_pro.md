---
title: javascript-pro
url: https://skills.sh/jeffallan/claude-skills/javascript-pro
---

# javascript-pro

skills/jeffallan/claude-skills/javascript-pro
javascript-pro
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill javascript-pro
Summary

Modern ES2023+ JavaScript implementation with async/await, ESM modules, and Node.js best practices.

Covers vanilla JavaScript, Promise-based async flows, Web Workers, Fetch API, and browser performance optimization
Enforces ES2023+ syntax, optional chaining, nullish coalescing, and functional programming patterns
Includes comprehensive error handling, memory leak detection, and Jest test coverage validation (85%+ target)
Provides reference guides for async patterns, module systems (ESM/CJS), browser APIs, and Node.js essentials
SKILL.md
JavaScript Pro
When to Use This Skill
Building vanilla JavaScript applications
Implementing async/await patterns and Promise handling
Working with modern module systems (ESM/CJS)
Optimizing browser performance and memory usage
Developing Node.js backend services
Implementing Web Workers, Service Workers, or browser APIs
Core Workflow
Analyze requirements — Review package.json, module system, Node version, browser targets; confirm .js/.mjs/.cjs conventions
Design architecture — Plan modules, async flows, and error handling strategies
Implement — Write ES2023+ code with proper patterns and optimisations
Validate — Run linter (eslint --fix); if linter fails, fix all reported issues and re-run before proceeding. Check for memory leaks with DevTools or --inspect, verify bundle size; if leaks are found, resolve them before continuing
Test — Write comprehensive tests with Jest achieving 85%+ coverage; if coverage falls short, add missing cases and re-run. Confirm no unhandled Promise rejections
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Modern Syntax	references/modern-syntax.md	ES2023+ features, optional chaining, private fields
Async Patterns	references/async-patterns.md	Promises, async/await, error handling, event loop
Modules	references/modules.md	ESM vs CJS, dynamic imports, package.json exports
Browser APIs	references/browser-apis.md	Fetch, Web Workers, Storage, IntersectionObserver
Node Essentials	references/node-essentials.md	fs/promises, streams, EventEmitter, worker threads
Constraints
MUST DO
Use ES2023+ features exclusively
Use X | null or X | undefined patterns
Use optional chaining (?.) and nullish coalescing (??)
Use async/await for all asynchronous operations
Use ESM (import/export) for new projects
Implement proper error handling with try/catch
Add JSDoc comments for complex functions
Follow functional programming principles
MUST NOT DO
Use var (always use const or let)
Use callback-based patterns (prefer Promises)
Mix CommonJS and ESM in the same module
Ignore memory leaks or performance issues
Skip error handling in async functions
Use synchronous I/O in Node.js
Mutate function parameters
Create blocking operations in the browser
Key Patterns with Examples
Async/Await Error Handling
// ✅ Correct — always handle async errors explicitly
async function fetchUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (err) {
    console.error("fetchUser failed:", err);
    return null;
  }
}

// ❌ Incorrect — unhandled rejection, no null guard
async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

Optional Chaining & Nullish Coalescing
// ✅ Correct
const city = user?.address?.city ?? "Unknown";

// ❌ Incorrect — throws if address is undefined
const city = user.address.city || "Unknown";

ESM Module Structure
// ✅ Correct — named exports, no default-only exports for libraries
// utils/math.mjs
export const add = (a, b) => a + b;
export const multiply = (a, b) => a * b;

// consumer.mjs
import { add } from "./utils/math.mjs";

// ❌ Incorrect — mixing require() with ESM
const { add } = require("./utils/math.mjs");

Avoid var / Prefer const
// ✅ Correct
const MAX_RETRIES = 3;
let attempts = 0;

// ❌ Incorrect
var MAX_RETRIES = 3;
var attempts = 0;

Output Templates

When implementing JavaScript features, provide:

Module file with clean exports
Test file with comprehensive coverage
JSDoc documentation for public APIs
Brief explanation of patterns used

Documentation

Weekly Installs
2.2K
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