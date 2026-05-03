---
title: typescript-react-patterns
url: https://skills.sh/asyrafhussin/agent-skills/typescript-react-patterns
---

# typescript-react-patterns

skills/asyrafhussin/agent-skills/typescript-react-patterns
typescript-react-patterns
Installation
$ npx skills add https://github.com/asyrafhussin/agent-skills --skill typescript-react-patterns
SKILL.md
TypeScript React Patterns

Type-safe React with TypeScript. Contains 33 rules across 7 categories covering component typing, hooks, event handling, refs, generics, context, and utility types.

Metadata
Version: 2.0.0
Rule Count: 33 rules across 7 categories
License: MIT
When to Apply

Reference these guidelines when:

Typing React component props
Creating custom hooks with TypeScript
Handling events with proper types
Working with refs (DOM, mutable, imperative)
Building generic, reusable components
Setting up typed Context providers
Fixing TypeScript errors in React code
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Component Typing	CRITICAL	comp-
2	Hook Typing	CRITICAL	hook-
3	Event Handling	HIGH	event-
4	Ref Typing	HIGH	ref-
5	Generic Components	MEDIUM	generic-
6	Context & State	MEDIUM	ctx-
7	Utility Types	LOW	util-
Quick Reference
1. Component Typing (CRITICAL)
comp-props-interface - Use interface for props, type for unions
comp-children-types - Correct children typing (ReactNode, ReactElement)
comp-default-props - Default props with destructuring defaults
comp-forward-ref - Typing forwardRef components
comp-polymorphic - Polymorphic "as" prop typing
comp-fc-vs-function - Function declaration vs React.FC
comp-display-name - Display names for debugging
comp-rest-props - Spreading rest props with proper types
2. Hook Typing (CRITICAL)
hook-usestate - useState with proper generic types
hook-useref - useRef for DOM elements and mutable values
hook-use-reducer - useReducer with discriminated union actions
hook-use-callback - useCallback with typed parameters
hook-use-memo - useMemo with typed return values
hook-use-context - useContext with null checking
hook-custom-hooks - Custom hook return types
hook-generic-hooks - Generic custom hooks
3. Event Handling (HIGH)
event-handler-types - Event handler type patterns
event-click-handler - Click event typing
event-form - Form event handling (submit, change, select)
event-keyboard - Keyboard event types
4. Ref Typing (HIGH)
ref-dom-elements - useRef with specific HTML element types
ref-callback - Callback ref pattern for DOM measurement
ref-imperative-handle - useImperativeHandle typing
5. Generic Components (MEDIUM)
generic-list - Generic list components
generic-select - Generic select/dropdown
generic-table - Generic table with typed columns
generic-constraints - Generic constraints with extends
6. Context & State (MEDIUM)
ctx-create - Creating typed context
ctx-provider - Provider pattern with null check hook
ctx-reducer - Context with useReducer
7. Utility Types (LOW)
util-component-props - ComponentPropsWithoutRef for HTML props
util-pick-omit - Pick, Omit, Partial for prop derivation
util-discriminated-unions - Discriminated unions for state machines
Essential Patterns
Component Props
interface ButtonProps {
  variant: 'primary' | 'secondary' | 'danger'
  size?: 'sm' | 'md' | 'lg'
  children: React.ReactNode
  onClick?: () => void
}

function Button({ variant, size = 'md', children, onClick }: ButtonProps) {
  return (
    <button className={`btn-${variant} btn-${size}`} onClick={onClick}>
      {children}
    </button>
  )
}

Typed Context with Null Check
interface AuthContextType {
  user: User | null
  login: (credentials: Credentials) => Promise<void>
  logout: () => void
}

const AuthContext = createContext<AuthContextType | null>(null)

function useAuth() {
  const context = useContext(AuthContext)
  if (!context) throw new Error('useAuth must be used within AuthProvider')
  return context
}

Generic Component
interface ListProps<T> {
  items: T[]
  renderItem: (item: T) => React.ReactNode
  keyExtractor: (item: T) => string
}

function List<T>({ items, renderItem, keyExtractor }: ListProps<T>) {
  return <ul>{items.map(item => <li key={keyExtractor(item)}>{renderItem(item)}</li>)}</ul>
}

How to Use

Read individual rule files for detailed explanations:

rules/comp-props-interface.md
rules/hook-usestate.md
rules/event-form.md
rules/ref-dom-elements.md
rules/util-discriminated-unions.md

References
React TypeScript Cheatsheet
React + TypeScript Guide
TypeScript Handbook
Full Compiled Document

For the complete guide with all rules expanded: AGENTS.md

Weekly Installs
234
Repository
asyrafhussin/ag…t-skills
GitHub Stars
34
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass