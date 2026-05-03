---
title: react-testing-library
url: https://skills.sh/pproenca/dot-skills/react-testing-library
---

# react-testing-library

skills/pproenca/dot-skills/react-testing-library
react-testing-library
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill react-testing-library
SKILL.md
React Testing Library Best Practices

Comprehensive testing guide for React components using Testing Library, designed for AI agents and LLMs. Contains 43 rules across 9 categories, prioritized by impact to guide test writing and code review.

When to Apply

Reference these guidelines when:

Writing new component tests with React Testing Library
Selecting queries (getByRole, getByLabelText, etc.)
Handling async operations in tests (findBy, waitFor)
Simulating user interactions (userEvent)
Reviewing tests for anti-patterns and implementation detail testing
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Query Selection	CRITICAL	query-
2	Async Handling	CRITICAL	async-
3	Common Anti-Patterns	CRITICAL	anti-
4	User Interaction	HIGH	user-
5	Assertions	HIGH	assert-
6	Component Setup	MEDIUM	setup-
7	Test Structure	MEDIUM	struct-
8	Debugging	LOW-MEDIUM	debug-
9	Accessibility Testing	LOW	a11y-
Quick Reference
1. Query Selection (CRITICAL)
query-prefer-role - Prefer getByRole over other queries
query-avoid-testid - Avoid getByTestId as primary query
query-use-screen - Use screen for queries
query-label-text-forms - Use getByLabelText for form fields
query-role-name-option - Use name option with getByRole
query-get-vs-query - Use getBy for present, queryBy for absent
query-within-scope - Use within() to scope queries
2. Async Handling (CRITICAL)
async-findby-over-waitfor - Use findBy instead of waitFor + getBy
async-await-findby - Always await findBy queries
async-single-assertion-waitfor - Single assertion in waitFor
async-no-side-effects-waitfor - Avoid side effects in waitFor
async-waitfor-disappear - Use waitForElementToBeRemoved
3. Common Anti-Patterns (CRITICAL)
anti-unnecessary-act - Avoid unnecessary act() wrapping
anti-manual-cleanup - Remove manual cleanup calls
anti-implementation-details - Avoid testing implementation details
anti-empty-waitfor - Avoid empty waitFor callbacks
anti-container-queries - Avoid using container for queries
anti-redundant-roles - Avoid adding redundant ARIA roles
4. User Interaction (HIGH)
user-prefer-userevent - Use userEvent over fireEvent
user-setup-before-render - Setup userEvent before render
user-await-interactions - Always await userEvent interactions
user-keyboard-for-special-keys - Use keyboard() for special keys
user-clear-before-type - Use clear() before retyping
5. Assertions (HIGH)
assert-jest-dom-matchers - Use jest-dom matchers
assert-visible-over-in-document - Use toBeVisible() for visibility
assert-text-content - Use toHaveTextContent() for text
assert-have-value - Use toHaveValue() for inputs
assert-accessible-description - Use toHaveAccessibleDescription()
6. Component Setup (MEDIUM)
setup-wrapper-providers - Use wrapper option for providers
setup-custom-render - Create custom render with providers
setup-mock-modules - Mock modules at module level
setup-fake-timers - Configure userEvent with fake timers
setup-render-hook - Use renderHook for testing hooks
7. Test Structure (MEDIUM)
struct-arrange-act-assert - Follow Arrange-Act-Assert pattern
struct-one-behavior-per-test - Test one behavior per test
struct-descriptive-names - Use descriptive test names
struct-avoid-beforeeach-render - Avoid render() in beforeEach
8. Debugging (LOW-MEDIUM)
debug-screen-debug - Use screen.debug() to inspect DOM
debug-logroles - Use logRoles to find available roles
debug-testing-playground - Use Testing Playground for queries
9. Accessibility Testing (LOW)
a11y-role-queries-verify - Role queries verify accessibility
a11y-verify-focus - Test focus management
a11y-test-aria-states - Test ARIA states and properties
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
163
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass