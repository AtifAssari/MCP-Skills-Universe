---
rating: ⭐⭐⭐
title: testing
url: https://skills.sh/bumgeunsong/daily-writing-friends/testing
---

# testing

skills/bumgeunsong/daily-writing-friends/testing
testing
Installation
$ npx skills add https://github.com/bumgeunsong/daily-writing-friends --skill testing
SKILL.md
Output-Based Testing for Pure Functions

Test pure functions with input/output assertions. Never unit test hooks, components, or side effects.

When to Use
User asks to "write tests" or "add coverage"
New business logic is being implemented
TDD requested for new feature
Coverage report shows untested utils/
Core Pattern
TESTABLE (Functional Core)     │  NOT UNIT TESTED (Imperative Shell)
───────────────────────────────│────────────────────────────────────
Pure functions in utils/       │  React hooks (useX)
Calculations, transformations  │  Components (*.tsx)
Validators, formatters         │  API calls, Firebase operations
State machines, reducers       │  localStorage, Date.now(), Math.random()

Implementation
What to Test
// ✅ TESTABLE: Pure function
export const calculateStreak = (dates: Date[], today: Date): number => {
  // Pure transformation: dates → number
};

// Test with simple input/output
describe('calculateStreak', () => {
  it('returns 0 for empty dates', () => {
    expect(calculateStreak([], new Date('2024-01-15'))).toBe(0);
  });

  it('returns consecutive days count', () => {
    const dates = [new Date('2024-01-14'), new Date('2024-01-15')];
    expect(calculateStreak(dates, new Date('2024-01-15'))).toBe(2);
  });
});

What NOT to Test
// ❌ DON'T TEST: Hook with side effects
export function useStreak(userId: string) {
  const { data } = useQuery(['streak', userId], () => fetchStreak(userId));
  return calculateStreak(data?.dates ?? [], new Date());
}

// ❌ DON'T TEST: Component
const StreakBadge = ({ userId }) => {
  const streak = useStreak(userId);
  return <Badge>{streak} days</Badge>;
};

TDD Workflow
1. Write failing test for pure function
2. Implement pure function to pass test
3. Create thin hook/component that calls pure function
4. Skip unit tests for hook/component (E2E covers integration)

Test File Location
src/
├── feature/
│   ├── utils/
│   │   ├── calculations.ts      # Pure functions
│   │   └── calculations.test.ts # Tests here
│   ├── hooks/
│   │   └── useFeature.ts        # NO unit tests
│   └── components/
│       └── Feature.tsx          # NO unit tests

Common Mistakes
Mistake	Symptom	Fix
Testing hooks	renderHook(), QueryClientProvider in test	Extract logic to pure function
Mocking time	vi.useFakeTimers(), mockDate	Inject timestamp as parameter
Mocking internals	vi.mock('../api/firebase')	Test pure logic, not integration
Testing UI	render(), screen.getByText()	Only E2E tests for UI
Red Flags

Stop and refactor if your test file has:

vi.mock() for anything except external APIs
renderHook() or render() from testing-library
QueryClient, Provider, or wrapper setup
More than 5 lines of test setup
Naming Convention
describe('FeatureName', () => {
  describe('when [condition]', () => {
    it('[expected outcome]', () => {
      // Arrange - Act - Assert (max 3-5 lines)
    });
  });
});

Weekly Installs
27
Repository
bumgeunsong/dai…-friends
GitHub Stars
9
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass