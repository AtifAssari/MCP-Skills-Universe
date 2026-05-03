---
rating: ⭐⭐⭐
title: testing-patterns
url: https://skills.sh/chriswiles/claude-code-showcase/testing-patterns
---

# testing-patterns

skills/chriswiles/claude-code-showcase/testing-patterns
testing-patterns
Installation
$ npx skills add https://github.com/chriswiles/claude-code-showcase --skill testing-patterns
SKILL.md
Testing Patterns and Utilities
Testing Philosophy

Test-Driven Development (TDD):

Write failing test FIRST
Implement minimal code to pass
Refactor after green
Never write production code without a failing test

Behavior-Driven Testing:

Test behavior, not implementation
Focus on public APIs and business requirements
Avoid testing implementation details
Use descriptive test names that describe behavior

Factory Pattern:

Create getMockX(overrides?: Partial<X>) functions
Provide sensible defaults
Allow overriding specific properties
Keep tests DRY and maintainable
Test Utilities
Custom Render Function

Create a custom render that wraps components with required providers:

// src/utils/testUtils.tsx
import { render } from '@testing-library/react-native';
import { ThemeProvider } from './theme';

export const renderWithTheme = (ui: React.ReactElement) => {
  return render(
    <ThemeProvider>{ui}</ThemeProvider>
  );
};


Usage:

import { renderWithTheme } from 'utils/testUtils';
import { screen } from '@testing-library/react-native';

it('should render component', () => {
  renderWithTheme(<MyComponent />);
  expect(screen.getByText('Hello')).toBeTruthy();
});

Factory Pattern
Component Props Factory
import { ComponentProps } from 'react';

const getMockMyComponentProps = (
  overrides?: Partial<ComponentProps<typeof MyComponent>>
) => {
  return {
    title: 'Default Title',
    count: 0,
    onPress: jest.fn(),
    isLoading: false,
    ...overrides,
  };
};

// Usage in tests
it('should render with custom title', () => {
  const props = getMockMyComponentProps({ title: 'Custom Title' });
  renderWithTheme(<MyComponent {...props} />);
  expect(screen.getByText('Custom Title')).toBeTruthy();
});

Data Factory
interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user';
}

const getMockUser = (overrides?: Partial<User>): User => {
  return {
    id: '123',
    name: 'John Doe',
    email: 'john@example.com',
    role: 'user',
    ...overrides,
  };
};

// Usage
it('should display admin badge for admin users', () => {
  const user = getMockUser({ role: 'admin' });
  renderWithTheme(<UserCard user={user} />);
  expect(screen.getByText('Admin')).toBeTruthy();
});

Mocking Patterns
Mocking Modules
// Mock entire module
jest.mock('utils/analytics');

// Mock with factory function
jest.mock('utils/analytics', () => ({
  Analytics: {
    logEvent: jest.fn(),
  },
}));

// Access mock in test
const mockLogEvent = jest.requireMock('utils/analytics').Analytics.logEvent;

Mocking GraphQL Hooks
jest.mock('./GetItems.generated', () => ({
  useGetItemsQuery: jest.fn(),
}));

const mockUseGetItemsQuery = jest.requireMock(
  './GetItems.generated'
).useGetItemsQuery as jest.Mock;

// In test
mockUseGetItemsQuery.mockReturnValue({
  data: { items: [] },
  loading: false,
  error: undefined,
});

Test Structure
describe('ComponentName', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('Rendering', () => {
    it('should render component with default props', () => {});
    it('should render loading state when loading', () => {});
  });

  describe('User interactions', () => {
    it('should call onPress when button is clicked', async () => {});
  });

  describe('Edge cases', () => {
    it('should handle empty data gracefully', () => {});
  });
});

Query Patterns
// Element must exist
expect(screen.getByText('Hello')).toBeTruthy();

// Element should not exist
expect(screen.queryByText('Goodbye')).toBeNull();

// Element appears asynchronously
await waitFor(() => {
  expect(screen.findByText('Loaded')).toBeTruthy();
});

User Interaction Patterns
import { fireEvent, screen } from '@testing-library/react-native';

it('should submit form on button click', async () => {
  const onSubmit = jest.fn();
  renderWithTheme(<LoginForm onSubmit={onSubmit} />);

  fireEvent.changeText(screen.getByLabelText('Email'), 'user@example.com');
  fireEvent.changeText(screen.getByLabelText('Password'), 'password123');
  fireEvent.press(screen.getByTestId('login-button'));

  await waitFor(() => {
    expect(onSubmit).toHaveBeenCalled();
  });
});

Anti-Patterns to Avoid
Testing Mock Behavior Instead of Real Behavior
// Bad - testing the mock
expect(mockFetchData).toHaveBeenCalled();

// Good - testing actual behavior
expect(screen.getByText('John Doe')).toBeTruthy();

Not Using Factories
// Bad - duplicated, inconsistent test data
it('test 1', () => {
  const user = { id: '1', name: 'John', email: 'john@test.com', role: 'user' };
});
it('test 2', () => {
  const user = { id: '2', name: 'Jane', email: 'jane@test.com' }; // Missing role!
});

// Good - reusable factory
const user = getMockUser({ name: 'Custom Name' });

Best Practices
Always use factory functions for props and data
Test behavior, not implementation
Use descriptive test names
Organize with describe blocks
Clear mocks between tests
Keep tests focused - one behavior per test
Running Tests
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific file
npm test ComponentName.test.tsx

Integration with Other Skills
react-ui-patterns: Test all UI states (loading, error, empty, success)
systematic-debugging: Write test that reproduces bug before fixing
Weekly Installs
41
Repository
chriswiles/clau…showcase
GitHub Stars
5.9K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass