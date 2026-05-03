---
rating: ⭐⭐
title: vitest-testing
url: https://skills.sh/existential-birds/beagle/vitest-testing
---

# vitest-testing

skills/existential-birds/beagle/vitest-testing
vitest-testing
Installation
$ npx skills add https://github.com/existential-birds/beagle --skill vitest-testing
SKILL.md
Vitest Best Practices
Quick Reference
import { describe, it, expect, beforeEach, vi } from 'vitest'

describe('feature name', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('should do something specific', () => {
    expect(actual).toBe(expected)
  })

  it.todo('planned test')
  it.skip('temporarily disabled')
  it.only('run only this during dev')
})

Common Assertions
// Equality
expect(value).toBe(42)                    // Strict (===)
expect(obj).toEqual({ a: 1 })             // Deep equality
expect(obj).toStrictEqual({ a: 1 })       // Strict deep (checks types)

// Truthiness
expect(value).toBeTruthy()
expect(value).toBeFalsy()
expect(value).toBeNull()
expect(value).toBeUndefined()

// Numbers
expect(0.1 + 0.2).toBeCloseTo(0.3)
expect(value).toBeGreaterThan(5)

// Strings/Arrays
expect(str).toMatch(/pattern/)
expect(str).toContain('substring')
expect(array).toContain(item)
expect(array).toHaveLength(3)

// Objects
expect(obj).toHaveProperty('key')
expect(obj).toHaveProperty('nested.key', 'value')
expect(obj).toMatchObject({ subset: 'of properties' })

// Exceptions
expect(() => fn()).toThrow()
expect(() => fn()).toThrow('error message')
expect(() => fn()).toThrow(/pattern/)

Async Testing
// Async/await (preferred)
it('fetches data', async () => {
  const data = await fetchData()
  expect(data).toEqual({ id: 1 })
})

// Promise matchers - ALWAYS await these
await expect(fetchData()).resolves.toEqual({ id: 1 })
await expect(fetchData()).rejects.toThrow('Error')

// Wrong - creates false positive
expect(promise).resolves.toBe(value)  // Missing await!

Quick Mock Reference
const mockFn = vi.fn()
mockFn.mockReturnValue(42)
mockFn.mockResolvedValue({ data: 'value' })

expect(mockFn).toHaveBeenCalled()
expect(mockFn).toHaveBeenCalledWith('arg1', 'arg2')
expect(mockFn).toHaveBeenCalledTimes(2)

Additional Documentation
Mocking: See references/mocking.md for module mocking, spying, cleanup
Configuration: See references/config.md for vitest.config, setup files, coverage
Patterns: See references/patterns.md for timers, snapshots, anti-patterns
Test Methods Quick Reference
Method	Purpose
it() / test()	Define test
describe()	Group tests
beforeEach() / afterEach()	Per-test hooks
beforeAll() / afterAll()	Per-suite hooks
.skip	Skip test/suite
.only	Run only this
.todo	Placeholder
.concurrent	Parallel execution
.each([...])	Parameterized tests
Weekly Installs
345
Repository
existential-birds/beagle
GitHub Stars
56
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass