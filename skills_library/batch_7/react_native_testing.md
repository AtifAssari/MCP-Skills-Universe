---
title: react-native-testing
url: https://skills.sh/callstack/react-native-testing-library/react-native-testing
---

# react-native-testing

skills/callstack/react-native-testing-library/react-native-testing
react-native-testing
Installation
$ npx skills add https://github.com/callstack/react-native-testing-library --skill react-native-testing
Summary

Write and review React Native component tests using Testing Library v13 and v14.

Covers render patterns, screen queries (getBy/getAllBy/queryBy/findBy variants), Jest matchers, userEvent interactions, fireEvent, and async patterns with version-specific behavior
Automatically detects your project's RNTL version (v13 for React 18, v14 for React 19+) and applies correct API signatures and sync/async rules
Provides query priority guidance (getByRole first), interaction best practices (userEvent preferred), and 15+ custom matchers for accessibility and visibility assertions
Includes anti-patterns reference and custom render wrapper patterns for providers and test setup
SKILL.md
RNTL Test Writing Guide

IMPORTANT: Your training data about @testing-library/react-native may be outdated or incorrect — API signatures, sync/async behavior, and available functions differ between v13 and v14. Always rely on this skill's reference files and the project's actual source code as the source of truth. Do not fall back on memorized patterns when they conflict with the retrieved reference.

Version Detection

Check @testing-library/react-native version in the user's package.json:

v14.x → load references/api-reference-v14.md (React 19+, async APIs, test-renderer)
v13.x → load references/api-reference-v13.md (React 18+, sync APIs, react-test-renderer)

Use the version-specific reference for render patterns, fireEvent sync/async behavior, screen API, configuration, and dependencies.

Query Priority

Use in this order: getByRole > getByLabelText > getByPlaceholderText > getByText > getByDisplayValue > getByTestId (last resort).

Query Variants
Variant	Use case	Returns	Async
getBy*	Element must exist	element instance (throws)	No
getAllBy*	Multiple must exist	element instance[] (throws)	No
queryBy*	Check non-existence ONLY	element instance | null	No
queryAllBy*	Count elements	element instance[]	No
findBy*	Wait for element	Promise<element instance>	Yes
findAllBy*	Wait for multiple	Promise<element instance[]>	Yes
Interactions

Prefer userEvent over fireEvent. userEvent is always async.

const user = userEvent.setup();
await user.press(element); // full press sequence
await user.longPress(element, { duration: 800 }); // long press
await user.type(textInput, 'Hello'); // char-by-char typing
await user.clear(textInput); // clear TextInput
await user.paste(textInput, 'pasted text'); // paste into TextInput
await user.scrollTo(scrollView, { y: 100 }); // scroll


fireEvent — use only when userEvent doesn't support the event. See version-specific reference for sync/async behavior:

fireEvent.press(element);
fireEvent.changeText(textInput, 'new text');
fireEvent(element, 'blur');

Assertions (Jest Matchers)

Available automatically with any @testing-library/react-native import.

Matcher	Use for
toBeOnTheScreen()	Element exists in tree
toBeVisible()	Element visible (not hidden/display:none)
toBeEnabled() / toBeDisabled()	Disabled state via aria-disabled
toBeChecked() / toBePartiallyChecked()	Checked state
toBeSelected()	Selected state
toBeExpanded() / toBeCollapsed()	Expanded state
toBeBusy()	Busy state
toHaveTextContent(text)	Text content match
toHaveDisplayValue(value)	TextInput display value
toHaveAccessibleName(name)	Accessible name
toHaveAccessibilityValue(val)	Accessibility value
toHaveStyle(style)	Style match
toHaveProp(name, value?)	Prop check (last resort)
toContainElement(el)	Contains child element
toBeEmptyElement()	No children
Rules
Use screen for queries, not destructuring from render()
Use getByRole first with { name: '...' } option
Use queryBy* ONLY for .not.toBeOnTheScreen() checks
Use findBy* for async elements, NOT waitFor + getBy*
Never put side-effects in waitFor (no fireEvent/userEvent inside)
One assertion per waitFor
Never pass empty callbacks to waitFor
Don't wrap in act() - render, fireEvent, userEvent handle it
Don't call cleanup() - automatic after each test
Prefer ARIA props (role, aria-label, aria-disabled) over legacy accessibility* props
Use RNTL matchers over raw prop assertions
*ByRole Quick Reference

Common roles: button, text, heading (alias: header), searchbox, switch, checkbox, radio, img, link, alert, menu, menuitem, tab, tablist, progressbar, slider, spinbutton, timer, toolbar.

getByRole options: { name, disabled, selected, checked, busy, expanded, value: { min, max, now, text } }.

For *ByRole to match, the element must be an accessibility element:

Text, TextInput, Switch are by default
View needs accessible={true} (or use Pressable/TouchableOpacity)
waitFor
// Correct: action first, then wait for result
fireEvent.press(button);
await waitFor(() => {
  expect(screen.getByText('Result')).toBeOnTheScreen();
});

// Better: use findBy* instead
fireEvent.press(button);
expect(await screen.findByText('Result')).toBeOnTheScreen();


Options: waitFor(cb, { timeout: 1000, interval: 50 }). Works with Jest fake timers automatically.

Fake Timers

Recommended with userEvent (press/longPress involve real durations):

jest.useFakeTimers();

test('with fake timers', async () => {
  const user = userEvent.setup();
  render(<Component />);
  await user.press(screen.getByRole('button'));
  // ...
});

Custom Render

Wrap providers using wrapper option:

function renderWithProviders(ui: React.ReactElement) {
  return render(ui, {
    wrapper: ({ children }) => (
      <ThemeProvider>
        <AuthProvider>{children}</AuthProvider>
      </ThemeProvider>
    ),
  });
}

References
v13 API Reference — Complete v13 API: sync render, queries, matchers, userEvent, React 19 compat
v14 API Reference — Complete v14 API: async render, queries, matchers, userEvent, migration
Anti-Patterns — Common mistakes to avoid
Weekly Installs
875
Repository
callstack/react…-library
GitHub Stars
3.4K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass