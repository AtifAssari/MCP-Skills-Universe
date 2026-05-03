---
title: vitest
url: https://skills.sh/itechmeat/llm-code/vitest
---

# vitest

skills/itechmeat/llm-code/vitest
vitest
Installation
$ npx skills add https://github.com/itechmeat/llm-code --skill vitest
SKILL.md
Vitest

Next generation testing framework powered by Vite.

Quick Navigation
Test API - test, describe, hooks
Expect API - matchers and assertions
Mocking - vi.fn, vi.mock, fake timers
Configuration - vitest.config.ts options
CLI - command line reference
Browser Mode - real browser testing
When to Use
Testing Vite-based applications (shared config)
Need Jest-compatible API with native ESM support
Component testing in real browser
Fast watch mode with HMR
TypeScript testing without extra config
Parallel test execution
Installation

Install: npm install -D vitest. Requires Vite >=v6.0.0, Node >=v20.0.0.

Release Highlights (4.1.0 -> 4.1.4)
New control-flow hooks: aroundEach and aroundAll.
Test metadata expands with tags, meta, and improved test.extend type inference.
CLI adds --detect-async-leaks, richer --update modes, and static collection for vitest list.
Browser mode grows Playwright persistent contexts, userEvent.wheel, and stronger trace/artifact handling.
Mocking/timers add disposable doMock(), mockThrow / mockThrowOnce, and setTickMode.
4.1.4 adds experimental ARIA snapshots, filterMeta for the JSON reporter, and exposes assertion as a public experimental field.
Quick Start
// sum.js
export function sum(a, b) {
  return a + b;
}

// sum.test.js
import { expect, test } from "vitest";
import { sum } from "./sum.js";

test("adds 1 + 2 to equal 3", () => {
  expect(sum(1, 2)).toBe(3);
});

// package.json
{
  "scripts": {
    "test": "vitest",
    "test:run": "vitest run",
    "coverage": "vitest run --coverage"
  }
}

Configuration
// vitest.config.ts (recommended)
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    globals: true, // Enable global test APIs
    environment: "jsdom", // Browser-like environment
    include: ["**/*.{test,spec}.{js,ts,jsx,tsx}"],
    coverage: {
      provider: "v8",
      reporter: ["text", "html"],
    },
  },
});


Or extend Vite config:

// vite.config.ts
/// <reference types="vitest/config" />
import { defineConfig } from "vite";

export default defineConfig({
  test: {
    // test options
  },
});

Test File Naming

By default, tests must contain .test. or .spec. in filename:

sum.test.js
sum.spec.ts
__tests__/sum.js
Key Commands
# Watch mode (default)
vitest

# Single run
vitest run

# With coverage
vitest run --coverage

# Filter by file/test name
vitest sum
vitest -t "should add"

# UI mode
vitest --ui

# Browser tests
vitest --browser.enabled

Common Patterns
Basic Test
import { describe, it, expect, beforeEach } from "vitest";

describe("Calculator", () => {
  let calc: Calculator;

  beforeEach(() => {
    calc = new Calculator();
  });

  it("adds numbers", () => {
    expect(calc.add(1, 2)).toBe(3);
  });

  it("throws on invalid input", () => {
    expect(() => calc.add("a", 1)).toThrow();
  });
});

Mocking
import { vi, expect, test } from "vitest";
import { fetchUser } from "./api";

vi.mock("./api", () => ({
  fetchUser: vi.fn(),
}));

test("uses mocked API", async () => {
  vi.mocked(fetchUser).mockResolvedValue({ name: "John" });

  const user = await fetchUser(1);

  expect(fetchUser).toHaveBeenCalledWith(1);
  expect(user.name).toBe("John");
});

Snapshot Testing
import { expect, test } from "vitest";

test("matches snapshot", () => {
  const result = generateConfig();
  expect(result).toMatchSnapshot();
});

// Inline snapshot (auto-updates)
test("inline snapshot", () => {
  expect({ foo: "bar" }).toMatchInlineSnapshot();
});

Async Testing
import { expect, test } from "vitest";

test("async/await", async () => {
  const result = await fetchData();
  expect(result).toBeDefined();
});

test("resolves", async () => {
  await expect(Promise.resolve("ok")).resolves.toBe("ok");
});

test("rejects", async () => {
  await expect(Promise.reject(new Error())).rejects.toThrow();
});

Fake Timers
import { vi, expect, test, beforeEach, afterEach } from "vitest";

beforeEach(() => {
  vi.useFakeTimers();
});

afterEach(() => {
  vi.useRealTimers();
});

test("advances time", () => {
  const callback = vi.fn();
  setTimeout(callback, 1000);

  vi.advanceTimersByTime(1000);

  expect(callback).toHaveBeenCalled();
});

Jest Migration

Most Jest code works with minimal changes:

- import { jest } from '@jest/globals'
+ import { vi } from 'vitest'

- jest.fn()
+ vi.fn()

- jest.mock('./module')
+ vi.mock('./module')

- jest.useFakeTimers()
+ vi.useFakeTimers()


Key differences:

Use vi instead of jest
Globals not enabled by default (add globals: true)
vi.mock is hoisted (use vi.doMock for non-hoisted)
No jest.requireActual (use vi.importActual)
Environment Selection
// vitest.config.ts
{
  test: {
    environment: 'jsdom', // or 'happy-dom', 'node', 'edge-runtime'
  }
}

// Per-file (docblock at top)
/** @vitest-environment jsdom */

TypeScript
// tsconfig.json
{
  "compilerOptions": {
    "types": ["vitest/globals"]
  }
}

References

See references/ directory for detailed documentation on:

Test API and hooks
All expect matchers
Mocking functions and modules
Configuration options
CLI commands
Browser mode testing
Links
Documentation
API Reference
GitHub
VS Code Extension
Weekly Installs
114
Repository
itechmeat/llm-code
GitHub Stars
15
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass