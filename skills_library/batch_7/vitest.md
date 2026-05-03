---
title: vitest
url: https://skills.sh/onmax/nuxt-skills/vitest
---

# vitest

skills/onmax/nuxt-skills/vitest
vitest
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill vitest
Summary

Vite-native unit and integration testing framework with Jest-compatible API and parallel execution.

Supports testing Vue, React, and Svelte components with configurable environments (Node, jsdom, or browser mode)
Provides Jest-compatible API including describe/it blocks, hooks, fixtures, and globals configuration
Includes comprehensive mocking capabilities: vi.fn for function mocks, vi.mock for module mocking, and timer/date utilities
Offers code coverage thresholds, snapshot testing, and type testing support with TypeScript
Runs tests concurrently by default with workspace project support and CLI filtering options
SKILL.md
Vitest

Vite-native testing framework with Jest-compatible API.

When to Use
Writing unit/integration tests for Vite projects
Testing Vue/React/Svelte components
Mocking modules, timers, or dates
Running concurrent/parallel tests
Type testing with TypeScript
Quick Start
npm i -D vitest

// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',  // or 'jsdom' for DOM tests
  },
})

// example.test.ts
import { describe, expect, it, vi } from 'vitest'

describe('math', () => {
  it('adds numbers', () => {
    expect(1 + 1).toBe(2)
  })
})

Reference Files
Task	File
Configuration, CLI, projects	config.md
test/describe, hooks, fixtures	test-api.md
vi.fn, vi.mock, timers, spies	mocking.md
expect, snapshots, coverage, filtering	utilities.md
Environments, type testing, browser mode	advanced.md
Loading Files

Consider loading these reference files based on your task:

 references/config.md - if setting up vitest.config.ts, CLI, or workspace projects
 references/test-api.md - if writing test/describe blocks, using hooks, or test fixtures
 references/mocking.md - if mocking modules, timers, dates, or using spies
 references/utilities.md - if writing assertions, snapshots, or configuring coverage
 references/advanced.md - if configuring test environments, type testing, or browser mode

DO NOT load all files at once. Load only what's relevant to your current task.

Cross-Skill References
Vue component testing → Use vue skill for component patterns
Library testing → Use ts-library skill for library patterns
Vite configuration → Use vite skill for shared config
Weekly Installs
1.7K
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass