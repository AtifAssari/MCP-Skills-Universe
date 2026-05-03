---
title: react18-enzyme-to-rtl
url: https://skills.sh/github/awesome-copilot/react18-enzyme-to-rtl
---

# react18-enzyme-to-rtl

skills/github/awesome-copilot/react18-enzyme-to-rtl
react18-enzyme-to-rtl
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill react18-enzyme-to-rtl
SKILL.md
React 18 Enzyme → RTL Migration

Enzyme has no React 18 adapter and no React 18 support path. All Enzyme tests must be rewritten using React Testing Library.

The Philosophy Shift (Read This First)

Enzyme tests implementation. RTL tests behavior.

// Enzyme: tests that the component has the right internal state
expect(wrapper.state('count')).toBe(3);
expect(wrapper.instance().handleClick).toBeDefined();
expect(wrapper.find('Button').prop('disabled')).toBe(true);

// RTL: tests what the user actually sees and can do
expect(screen.getByText('Count: 3')).toBeInTheDocument();
expect(screen.getByRole('button', { name: /submit/i })).toBeDisabled();


This is not a 1:1 translation. Enzyme tests that verify internal state or instance methods don't have RTL equivalents - because RTL intentionally doesn't expose internals. Rewrite the test to assert the visible outcome instead.

API Map

For complete before/after code for each Enzyme API, read:

references/enzyme-api-map.md - full mapping: shallow, mount, find, simulate, prop, state, instance, configure
references/async-patterns.md - waitFor, findBy, act(), Apollo MockedProvider, loading states, error states
Core Rewrite Template
// Every Enzyme test rewrites to this shape:
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import MyComponent from './MyComponent';

describe('MyComponent', () => {
  it('does the thing', async () => {
    // 1. Render (replaces shallow/mount)
    render(<MyComponent prop="value" />);

    // 2. Query (replaces wrapper.find())
    const button = screen.getByRole('button', { name: /submit/i });

    // 3. Interact (replaces simulate())
    await userEvent.setup().click(button);

    // 4. Assert on visible output (replaces wrapper.state() / wrapper.prop())
    expect(screen.getByText('Submitted!')).toBeInTheDocument();
  });
});

RTL Query Priority (use in this order)
getByRole - matches accessible roles (button, textbox, heading, checkbox, etc.)
getByLabelText - form fields linked to labels
getByPlaceholderText - input placeholders
getByText - visible text content
getByDisplayValue - current value of input/select/textarea
getByAltText - image alt text
getByTitle - title attribute
getByTestId - data-testid attribute (last resort)

Prefer getByRole over getByTestId. It tests accessibility too.

Wrapping with Providers
// Enzyme with context:
const wrapper = mount(
  <ApolloProvider client={client}>
    <ThemeProvider theme={theme}>
      <MyComponent />
    </ThemeProvider>
  </ApolloProvider>
);

// RTL equivalent (use your project's customRender or wrap inline):
import { render } from '@testing-library/react';
render(
  <MockedProvider mocks={mocks} addTypename={false}>
    <ThemeProvider theme={theme}>
      <MyComponent />
    </ThemeProvider>
  </MockedProvider>
);
// Or use the project's customRender helper if it wraps providers

Weekly Installs
517
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass