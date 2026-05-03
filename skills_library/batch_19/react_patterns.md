---
title: react-patterns
url: https://skills.sh/dralgorhythm/claude-agentic-framework/react-patterns
---

# react-patterns

skills/dralgorhythm/claude-agentic-framework/react-patterns
react-patterns
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill react-patterns
SKILL.md
React Patterns

Platform: Web and Mobile (shared React patterns). For React Native-specific patterns (Pressable, ScrollView, FlashList, safe areas), see the react-native-patterns skill.

Overview

Patterns for building maintainable React applications with TypeScript, leveraging React 19 features and composition patterns.

API Reference: Use Context7 MCP for full React API reference (mcp__context7__resolve-library-id → react).

Workflows
 Choose appropriate component composition pattern
 Apply TypeScript types for props and events
 Implement custom hooks for shared logic
 Add performance optimizations where needed
 Handle loading and error states with Suspense/boundaries
 Validate component render behavior
Feedback Loops
 Components render without TypeScript errors
 Props are properly typed and validated
 Custom hooks have clear return types
 No unnecessary re-renders (use React DevTools Profiler)
 Error boundaries catch component errors
 Loading states work with Suspense
Reference Implementation
1. Component Composition
Compound Components
// Shares implicit state between parent and children
const TabsContext = createContext<{ activeTab: string; setActiveTab: (id: string) => void } | null>(null);

function Tabs({ children, defaultTab }: { children: ReactNode; defaultTab: string }) {
  const [activeTab, setActiveTab] = useState(defaultTab);
  return <TabsContext.Provider value={{ activeTab, setActiveTab }}>{children}</TabsContext.Provider>;
}

function Tab({ id, children }: { id: string; children: ReactNode }) {
  const ctx = use(TabsContext);
  if (!ctx) throw new Error('Tab must be used within Tabs');
  return (
    <button role="tab" aria-selected={ctx.activeTab === id} onClick={() => ctx.setActiveTab(id)}>
      {children}
    </button>
  );
}

Slot Pattern
// Named slots for flexible composition
interface CardProps { header?: ReactNode; footer?: ReactNode; children: ReactNode; }

function Card({ header, footer, children }: CardProps) {
  return (
    <div className="card">
      {header && <div className="card-header">{header}</div>}
      <div className="card-body">{children}</div>
      {footer && <div className="card-footer">{footer}</div>}
    </div>
  );
}

2. React 19 Features
use() Hook
// Unwrap promises and context — simpler than useContext
function UserProfile({ userPromise }: { userPromise: Promise<User> }) {
  const user = use(userPromise); // Suspends until resolved
  return <div>{user.name}</div>;
}

useActionState
async function updateUser(prevState: { error?: string }, formData: FormData) {
  'use server';
  return { error: undefined };
}

function UserForm() {
  const [state, formAction, isPending] = useActionState(updateUser, {});
  return (
    <form action={formAction}>
      <input name="name" disabled={isPending} />
      {state.error && <p className="error">{state.error}</p>}
      <button disabled={isPending}>{isPending ? 'Saving...' : 'Save'}</button>
    </form>
  );
}

useOptimistic
function TodoList({ todos }: { todos: Todo[] }) {
  const [optimisticTodos, addOptimisticTodo] = useOptimistic(
    todos,
    (state, newTodo: Todo) => [...state, newTodo]
  );
  async function handleAdd(formData: FormData) {
    const todo = { id: crypto.randomUUID(), text: formData.get('text') as string };
    addOptimisticTodo(todo);
    await saveTodo(todo);
  }
  return (
    <form action={handleAdd}>
      {optimisticTodos.map(todo => <li key={todo.id}>{todo.text}</li>)}
      <input name="text" /><button>Add</button>
    </form>
  );
}

3. Custom Hooks
// Object return for multiple named values
function useAuth() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const login = async (credentials: Credentials) => { setUser(await api.login(credentials)); };
  return { user, loading, login };
}

// Tuple return for positional access (like useState)
function useToggle(initial = false): [boolean, () => void] {
  const [value, setValue] = useState(initial);
  return [value, useCallback(() => setValue(v => !v), [])];
}

// Composing hooks
function useLocalStorage<T>(key: string, initial: T) {
  const [value, setValue] = useState<T>(() => {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initial;
  });
  useEffect(() => { localStorage.setItem(key, JSON.stringify(value)); }, [key, value]);
  return [value, setValue] as const;
}

4. TypeScript + React
// Extend HTML element props
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary';
  loading?: boolean;
}
function Button({ variant = 'primary', loading, children, ...props }: ButtonProps) {
  return <button className={variant} disabled={loading} {...props}>{loading ? 'Loading...' : children}</button>;
}

// Generic components with full type inference
interface ListProps<T> { items: T[]; renderItem: (item: T) => ReactNode; keyExtractor: (item: T) => string; }
function List<T>({ items, renderItem, keyExtractor }: ListProps<T>) {
  return <ul>{items.map(item => <li key={keyExtractor(item)}>{renderItem(item)}</li>)}</ul>;
}

// Refs as props (React 19+) — forwardRef is deprecated
interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  ref?: React.Ref<HTMLInputElement>;
}
function Input({ label, ref, ...props }: InputProps) {
  return <label>{label}<input ref={ref} {...props} /></label>;
}

5. State Management
useReducer for Complex State
type Action =
  | { type: 'FETCH_START' }
  | { type: 'FETCH_SUCCESS'; payload: User[] }
  | { type: 'FETCH_ERROR'; payload: string };

function reducer(state: { data: User[]; loading: boolean; error: string | null }, action: Action) {
  switch (action.type) {
    case 'FETCH_START': return { ...state, loading: true, error: null };
    case 'FETCH_SUCCESS': return { ...state, loading: false, data: action.payload };
    case 'FETCH_ERROR': return { ...state, loading: false, error: action.payload };
  }
}

6. Performance Patterns
// memo + useCallback prevent unnecessary re-renders
const ListItem = memo(function ListItem({ item, onDelete }: ItemProps) {
  return <li>{item.name}<button onClick={() => onDelete(item.id)}>Delete</button></li>;
});

function List() {
  const [items, setItems] = useState<Item[]>([]);
  const handleDelete = useCallback((id: string) => {
    setItems(items => items.filter(item => item.id !== id));
  }, []);
  return <>{items.map(item => <ListItem key={item.id} item={item} onDelete={handleDelete} />)}</>;
}

// Lazy loading with Suspense
const Dashboard = lazy(() => import('./Dashboard'));
function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Routes><Route path="/dashboard" element={<Dashboard />} /></Routes>
    </Suspense>
  );
}

7. Error Handling
class ErrorBoundary extends Component<{ children: ReactNode; fallback?: ReactNode }, { hasError: boolean }> {
  state = { hasError: false };
  static getDerivedStateFromError(): { hasError: boolean } { return { hasError: true }; }
  componentDidCatch(error: Error, info: ErrorInfo) { console.error(error, info); }
  render() {
    return this.state.hasError ? (this.props.fallback ?? <div>Something went wrong</div>) : this.props.children;
  }
}

// Wrap async data loading with Suspense
function UserProfile({ userId }: { userId: string }) {
  const user = use(fetchUser(userId)); // Suspends
  return <div>{user.name}</div>;
}

Best Practices
Composition over inheritance - Use composition patterns for flexibility
Type everything - Leverage TypeScript for compile-time safety
Colocate state - Keep state as close to where it's used as possible
Extract custom hooks - Share logic across components with hooks
Stable references - Use useCallback/useMemo to prevent unnecessary re-renders
Error boundaries - Wrap component trees to catch rendering errors
Suspense for loading - Use Suspense instead of manual loading states
Avoid prop drilling - Use context or composition for deeply nested props
Anti-Patterns
Using forwardRef in React 19 - Use ref as a regular prop instead
Class components for new code - Use function components and hooks
Mutating state directly - Always use setState or reducer actions
Missing dependency arrays - Include all dependencies in useEffect/useMemo/useCallback
Overusing useMemo/useCallback - Only optimize when necessary (profile first)
Context for everything - Use context sparingly; prefer props or state management library
Derived state in useState - Compute derived values during render instead
useEffect for derived state - Use useMemo or compute directly in render
Index as key - Use stable unique IDs for list keys
Ignoring TypeScript errors - Never use 'any' or '// @ts-ignore' as shortcuts
Weekly Installs
40
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass