---
rating: ⭐⭐
title: react19-test-patterns
url: https://skills.sh/github/awesome-copilot/react19-test-patterns
---

# react19-test-patterns

skills/github/awesome-copilot/react19-test-patterns
react19-test-patterns
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill react19-test-patterns
SKILL.md
React 19 Test Migration Patterns

Reference for all test file migrations required by React 19.

Priority Order

Fix test files in this order; each layer depends on the previous:

act import fix first, it unblocks everything else
Simulate → fireEvent fix immediately after act
Full react-dom/test-utils cleanup remove remaining imports
StrictMode call counts measure actual, don't guess
Async act wrapping for remaining "not wrapped in act" warnings
Custom render helper verify once per codebase, not per test
1. act() Import Fix
// Before  REMOVED in React 19:
import { act } from 'react-dom/test-utils';

// After:
import { act } from 'react';


If mixed with other test-utils imports:

// Before:
import { act, Simulate, renderIntoDocument } from 'react-dom/test-utils';

// After  split the imports:
import { act } from 'react';
import { fireEvent, render } from '@testing-library/react'; // replaces Simulate + renderIntoDocument

2. Simulate → fireEvent
// Before  Simulate REMOVED in React 19:
import { Simulate } from 'react-dom/test-utils';
Simulate.click(element);
Simulate.change(input, { target: { value: 'hello' } });
Simulate.submit(form);
Simulate.keyDown(element, { key: 'Enter', keyCode: 13 });

// After:
import { fireEvent } from '@testing-library/react';
fireEvent.click(element);
fireEvent.change(input, { target: { value: 'hello' } });
fireEvent.submit(form);
fireEvent.keyDown(element, { key: 'Enter', keyCode: 13 });

3. react-dom/test-utils Full API Map
Old (react-dom/test-utils)	New location
act	import { act } from 'react'
Simulate	fireEvent from @testing-library/react
renderIntoDocument	render from @testing-library/react
findRenderedDOMComponentWithTag	getByRole, getByTestId from RTL
findRenderedDOMComponentWithClass	getByRole or container.querySelector
scryRenderedDOMComponentsWithTag	getAllByRole from RTL
isElement, isCompositeComponent	Remove not needed with RTL
isDOMComponent	Remove
4. StrictMode Call Count Fixes

React 19 StrictMode no longer double-invokes useEffect in development. Spy assertions counting effect calls must be updated.

Strategy always measure, never guess:

# Run the failing test, read the actual count from the error:
npm test -- --watchAll=false --testPathPattern="[filename]" --forceExit 2>&1 | grep -E "Expected|Received"

// Before (React 18 StrictMode  effects ran twice):
expect(mockFn).toHaveBeenCalledTimes(2);  // 1 call × 2 (strict double-invoke)

// After (React 19 StrictMode  effects run once):
expect(mockFn).toHaveBeenCalledTimes(1);

// Render-phase calls (component body)  still double-invoked in React 19 StrictMode:
expect(renderSpy).toHaveBeenCalledTimes(2);  // stays at 2 for render body calls

Weekly Installs
538
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass