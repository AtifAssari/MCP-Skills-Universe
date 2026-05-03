---
title: unit-testing-expert
url: https://skills.sh/anton-abyzov/specweave/unit-testing-expert
---

# unit-testing-expert

skills/anton-abyzov/specweave/unit-testing-expert
unit-testing-expert
Installation
$ npx skills add https://github.com/anton-abyzov/specweave --skill unit-testing-expert
SKILL.md
Unit Testing Expert

Self-contained unit testing expertise for Vitest/Jest in ANY user project.

Test-Driven Development (TDD)

Red-Green-Refactor Cycle:

// 1. RED: Write failing test
describe('Calculator', () => {
  it('should add two numbers', () => {
    const calc = new Calculator();
    expect(calc.add(2, 3)).toBe(5);
  });
});

// 2. GREEN: Minimal implementation
class Calculator {
  add(a: number, b: number): number {
    return a + b;
  }
}

// 3. REFACTOR: Improve code
class Calculator {
  add(...numbers: number[]): number {
    return numbers.reduce((sum, n) => sum + n, 0);
  }
}


TDD Benefits:

Better design (testable code)
Living documentation
Faster debugging
Higher confidence
Vitest/Jest Fundamentals
Basic Test Structure
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { UserService } from './UserService';

describe('UserService', () => {
  let service: UserService;

  beforeEach(() => {
    service = new UserService();
  });

  afterEach(() => {
    vi.clearAllMocks();
  });

  it('should create user', () => {
    const user = service.create({ name: 'John', email: 'john@test.com' });

    expect(user).toMatchObject({
      id: expect.any(String),
      name: 'John',
      email: 'john@test.com'
    });
  });

  it('should throw for invalid email', () => {
    expect(() => {
      service.create({ name: 'John', email: 'invalid' });
    }).toThrow('Invalid email');
  });
});

Async Testing
it('should fetch user from API', async () => {
  const user = await api.fetchUser('user-123');

  expect(user).toEqual({
    id: 'user-123',
    name: 'John Doe'
  });
});

// Testing async errors
it('should handle API errors', async () => {
  await expect(api.fetchUser('invalid')).rejects.toThrow('User not found');
});

Mocking Strategies
1. Mock Functions
// Mock a function
const mockFn = vi.fn();
mockFn.mockReturnValue(42);
expect(mockFn()).toBe(42);

// Mock with implementation
const mockAdd = vi.fn((a, b) => a + b);
expect(mockAdd(2, 3)).toBe(5);

// Verify calls
expect(mockFn).toHaveBeenCalledTimes(1);
expect(mockFn).toHaveBeenCalledWith(expected);

2. Mock Modules
// Mock entire module
vi.mock('./database', () => ({
  query: vi.fn().mockResolvedValue([{ id: 1, name: 'Test' }])
}));

import { query } from './database';

it('should fetch users from database', async () => {
  const users = await query('SELECT * FROM users');
  expect(users).toHaveLength(1);
});

3. Spies
// Spy on existing method
const spy = vi.spyOn(console, 'log');

myFunction();

expect(spy).toHaveBeenCalledWith('Expected message');
spy.mockRestore();

4. Mock Dependencies
class UserService {
  constructor(private db: Database) {}

  async getUser(id: string) {
    return this.db.query('SELECT * FROM users WHERE id = ?', [id]);
  }
}

// Test with mock
const mockDb = {
  query: vi.fn().mockResolvedValue({ id: '123', name: 'John' })
};

const service = new UserService(mockDb);
const user = await service.getUser('123');

expect(mockDb.query).toHaveBeenCalledWith(
  'SELECT * FROM users WHERE id = ?',
  ['123']
);

Test Patterns
AAA Pattern (Arrange-Act-Assert)
it('should calculate total price', () => {
  // Arrange
  const cart = new ShoppingCart();
  cart.addItem({ price: 10, quantity: 2 });
  cart.addItem({ price: 5, quantity: 3 });

  // Act
  const total = cart.getTotal();

  // Assert
  expect(total).toBe(35);
});

Given-When-Then (BDD)
describe('Shopping Cart', () => {
  it('should apply discount when total exceeds $100', () => {
    // Given: A cart with items totaling $120
    const cart = new ShoppingCart();
    cart.addItem({ price: 120, quantity: 1 });

    // When: Getting the total
    const total = cart.getTotal();

    // Then: 10% discount applied
    expect(total).toBe(108); // $120 - $12 (10%)
  });
});

Parametric Testing
describe.each([
  [2, 3, 5],
  [10, 5, 15],
  [-1, 1, 0],
  [0, 0, 0]
])('Calculator.add(%i, %i)', (a, b, expected) => {
  it(`should return ${expected}`, () => {
    const calc = new Calculator();
    expect(calc.add(a, b)).toBe(expected);
  });
});

Test Doubles
Mocks vs Stubs vs Spies vs Fakes

Mock: Verifies behavior (calls, arguments)

const mock = vi.fn();
mock('test');
expect(mock).toHaveBeenCalledWith('test');


Stub: Returns predefined values

const stub = vi.fn().mockReturnValue(42);
expect(stub()).toBe(42);


Spy: Observes real function

const spy = vi.spyOn(obj, 'method');
obj.method();
expect(spy).toHaveBeenCalled();


Fake: Working implementation (simplified)

class FakeDatabase {
  private data = new Map();

  async save(key, value) {
    this.data.set(key, value);
  }

  async get(key) {
    return this.data.get(key);
  }
}

Coverage Analysis
Running Coverage
# Vitest
vitest --coverage

# Jest
jest --coverage

Coverage Thresholds
// vitest.config.ts
export default {
  test: {
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html', 'lcov'],
      lines: 80,
      functions: 80,
      branches: 80,
      statements: 80
    }
  }
};

Coverage Best Practices

✅ DO:

Aim for 80-90% coverage
Focus on business logic
Test edge cases
Test error paths

❌ DON'T:

Chase 100% coverage
Test getters/setters only
Test framework code
Write tests just for coverage
Snapshot Testing
When to Use Snapshots

Good use cases:

UI component output
API responses
Configuration objects
Error messages
it('should render user card', () => {
  const card = renderUserCard({ name: 'John', role: 'Admin' });
  expect(card).toMatchSnapshot();
});

// Update snapshots: vitest -u


Avoid snapshots for:

Dates/timestamps
Random values
Large objects (prefer specific assertions)
Test Organization
File Structure
src/
├── services/
│   ├── UserService.ts
│   └── UserService.test.ts      ← Co-located
tests/
├── unit/
│   └── utils.test.ts
├── integration/
│   └── api.test.ts
└── fixtures/
    └── users.json

Test Naming

✅ GOOD:

describe('UserService.create', () => {
  it('should create user with valid email', () => {});
  it('should throw error for invalid email', () => {});
  it('should generate unique ID', () => {});
});


❌ BAD:

describe('UserService', () => {
  it('test1', () => {});
  it('should work', () => {});
});

Error Handling Tests
// Synchronous errors
it('should throw for negative numbers', () => {
  expect(() => sqrt(-1)).toThrow('Cannot compute square root of negative');
});

// Async errors
it('should reject for invalid ID', async () => {
  await expect(fetchUser('invalid')).rejects.toThrow('Invalid ID');
});

// Error types
it('should throw TypeError', () => {
  expect(() => doSomething()).toThrow(TypeError);
});

// Custom errors
it('should throw ValidationError', () => {
  expect(() => validate()).toThrow(ValidationError);
});

Test Isolation
Reset State Between Tests
let service: UserService;

beforeEach(() => {
  service = new UserService();
  vi.clearAllMocks();
});

afterEach(() => {
  vi.restoreAllMocks();
});

Avoid Test Interdependence

❌ BAD:

let user;

it('should create user', () => {
  user = createUser(); // Shared state
});

it('should update user', () => {
  updateUser(user); // Depends on previous test
});


✅ GOOD:

it('should update user', () => {
  const user = createUser();
  updateUser(user);
  expect(user.updated).toBe(true);
});

VSCode Debug Mode & Child Process Testing

CRITICAL: When tests spawn child processes (like CLI tools, hooks, or external commands), they may fail in VSCode debug mode due to NODE_OPTIONS inheritance.

Problem: NODE_OPTIONS Breaks Child Processes

VSCode debugger sets NODE_OPTIONS=--inspect-brk=<port> which child processes inherit, causing them to try to attach to the same debugger port and fail with exit code 1.

Symptoms:

Tests pass with "Run Test" but fail with "Debug Test"
Spawned processes exit with code 1 and empty output
spawnSync/execFileSync calls fail silently
Solution: getCleanEnv() Pattern
// src/utils/clean-env.ts
export function getCleanEnv(): NodeJS.ProcessEnv {
  const cleanEnv = { ...process.env };

  // Debugger flags (VSCode, WebStorm, IntelliJ)
  delete cleanEnv.NODE_OPTIONS;
  delete cleanEnv.NODE_INSPECT;
  delete cleanEnv.NODE_INSPECT_RESUME_ON_START;

  // Coverage/instrumentation (CI/CD pipelines)
  delete cleanEnv.NODE_V8_COVERAGE;
  delete cleanEnv.VSCODE_INSPECTOR_OPTIONS;

  return cleanEnv;
}

Usage in Tests
import { getCleanEnv } from '../test-utils/clean-env.js';
import { execSync, spawnSync } from 'child_process';

it('should execute CLI command', () => {
  const result = execSync('node my-cli.js', {
    encoding: 'utf-8',
    env: getCleanEnv(),  // ← CRITICAL for debug mode + CI/CD
  });
  expect(result).toContain('expected output');
});

it('should spawn child process', () => {
  const result = spawnSync('npm', ['run', 'build'], {
    encoding: 'utf-8',
    env: getCleanEnv(),  // ← CRITICAL
  });
  expect(result.status).toBe(0);
});

When to Use getCleanEnv

✅ ALWAYS USE when spawning:

CLI tools (node, npm, npx, claude, etc.)
External commands (git, gh, etc.)
Test hooks that spawn processes
Integration tests with real processes

❌ NOT NEEDED for:

Pure unit tests (no child processes)
Mocked dependencies
In-process testing
ESM Module Mocking with vi.hoisted()

CRITICAL: In ESM (ECMAScript Modules), imports are hoisted. Use vi.hoisted() to ensure mocks are defined before imports.

Problem: Mock Defined After Import
// ❌ WRONG: vi.mock hoisted, but mockFn not defined yet
vi.mock('./module', () => ({
  myFunc: mockFn  // ReferenceError: mockFn is not defined
}));

const mockFn = vi.fn();
import { myFunc } from './module';

Solution: vi.hoisted() Pattern
import { describe, it, expect, vi } from 'vitest';

// ✅ Define mocks in hoisted context FIRST
const { mockFn } = vi.hoisted(() => ({
  mockFn: vi.fn()
}));

// Now vi.mock can use the hoisted mock
vi.mock('./module', () => ({
  myFunc: mockFn
}));

// Import AFTER mock setup
import { myFunc } from './module';

describe('Module', () => {
  it('should use mocked function', () => {
    mockFn.mockReturnValue('mocked');
    expect(myFunc()).toBe('mocked');
    expect(mockFn).toHaveBeenCalled();
  });
});

Complete ESM Mocking Example
import { describe, it, expect, vi, beforeEach } from 'vitest';

// 1. Hoisted mock definitions
const { mockReadFile, mockWriteFile } = vi.hoisted(() => ({
  mockReadFile: vi.fn(),
  mockWriteFile: vi.fn()
}));

// 2. Mock the module using hoisted mocks
vi.mock('fs/promises', () => ({
  readFile: mockReadFile,
  writeFile: mockWriteFile
}));

// 3. Import AFTER mock setup (imports are automatically hoisted in Vitest)
import { readFile, writeFile } from 'fs/promises';

describe('FileService', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should read file', async () => {
    mockReadFile.mockResolvedValue('file content');

    const content = await readFile('/path/to/file', 'utf-8');

    expect(content).toBe('file content');
    expect(mockReadFile).toHaveBeenCalledWith('/path/to/file', 'utf-8');
  });
});

vi.hoisted() vs Traditional Mocking
Approach	ESM Compatible	Jest Compatible
vi.hoisted() + vi.mock()	✅ Yes	❌ No (Vitest only)
jest.mock() with factory	⚠️ Partial	✅ Yes
Manual module replacement	✅ Yes	✅ Yes
Testing with Isolated Temp Directories

CRITICAL: Integration tests should NEVER operate on project directories. Always use isolated temp directories.

Problem: Tests Affecting Project State
// ❌ DANGEROUS: Can corrupt project state
const testDir = path.join(process.cwd(), '.specweave/test');

Solution: Isolated Temp Directories
import * as os from 'os';
import * as path from 'path';
import * as fs from 'fs/promises';

// ✅ SAFE: Unique temp directory per test run
const TEST_ROOT = path.join(
  os.tmpdir(),
  `my-test-${Date.now()}-${Math.random().toString(36).slice(2)}`
);

describe('Integration Test', () => {
  beforeEach(async () => {
    await fs.mkdir(TEST_ROOT, { recursive: true });
  });

  afterEach(async () => {
    await fs.rm(TEST_ROOT, { recursive: true, force: true });
  });

  it('should work in isolated directory', async () => {
    const testFile = path.join(TEST_ROOT, 'test.json');
    await fs.writeFile(testFile, '{"test": true}');
    // Test logic...
  });
});

CWD Restoration Pattern

When tests change working directory, always restore it to prevent affecting other tests:

describe('Tests that change CWD', () => {
  let originalCwd: string;

  beforeEach(() => {
    originalCwd = process.cwd();  // ← Save BEFORE changing
    process.chdir(TEST_ROOT);
  });

  afterEach(() => {
    process.chdir(originalCwd);   // ← Restore BEFORE cleanup
    // Now safe to delete TEST_ROOT
  });
});

Best Practices Summary

✅ DO:

Write tests before code (TDD)
Test behavior, not implementation
One assertion per test (when possible)
Clear test names (should...)
Mock external dependencies
Test edge cases and errors
Keep tests fast (<100ms each)
Use descriptive variable names
Clean up after tests

❌ DON'T:

Test private methods directly
Share state between tests
Use real databases/APIs
Test framework code
Write fragile tests (implementation-dependent)
Skip error cases
Use magic numbers
Leave commented-out tests
Quick Reference
Assertions
expect(value).toBe(expected);              // ===
expect(value).toEqual(expected);           // Deep equality
expect(value).toBeTruthy();                // Boolean true
expect(value).toBeFalsy();                 // Boolean false
expect(array).toHaveLength(3);             // Array length
expect(array).toContain(item);             // Array includes
expect(string).toMatch(/pattern/);         // Regex match
expect(fn).toThrow(Error);                 // Throws error
expect(obj).toHaveProperty('key');         // Has property
expect(value).toBeCloseTo(0.3, 5);        // Float comparison

Lifecycle Hooks
beforeAll(() => {});      // Once before all tests
beforeEach(() => {});     // Before each test
afterEach(() => {});      // After each test
afterAll(() => {});       // Once after all tests

Mock Utilities
vi.fn()                           // Create mock
vi.fn().mockReturnValue(x)        // Return value
vi.fn().mockResolvedValue(x)      // Async return
vi.fn().mockRejectedValue(e)      // Async error
vi.mock('./module')               // Mock module
vi.spyOn(obj, 'method')           // Spy on method
vi.clearAllMocks()                // Clear call history
vi.resetAllMocks()                // Reset + clear
vi.restoreAllMocks()              // Restore originals


This skill is self-contained and works in ANY user project with Vitest/Jest.

Weekly Installs
20
Repository
anton-abyzov/specweave
GitHub Stars
134
First Seen
Jan 22, 2026