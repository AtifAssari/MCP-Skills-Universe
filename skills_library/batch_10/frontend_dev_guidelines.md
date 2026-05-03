---
title: frontend-dev-guidelines
url: https://skills.sh/bbeierle12/skill-mcp-claude/frontend-dev-guidelines
---

# frontend-dev-guidelines

skills/bbeierle12/skill-mcp-claude/frontend-dev-guidelines
frontend-dev-guidelines
Installation
$ npx skills add https://github.com/bbeierle12/skill-mcp-claude --skill frontend-dev-guidelines
SKILL.md
Frontend Development Guidelines
Project Structure
src/
├── features/           # Feature-based organization
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── api/
│   │   └── index.ts
│   ├── dashboard/
│   └── settings/
├── components/         # Shared/common components
│   ├── ui/            # Base UI components
│   └── layout/        # Layout components
├── hooks/             # Shared hooks
├── utils/             # Utility functions
├── types/             # TypeScript types
├── api/               # API layer
└── styles/            # Global styles

Component Patterns
Functional Components with TypeScript
interface Props {
  title: string;
  onAction: (id: string) => void;
  isLoading?: boolean;
}

export function MyComponent({ title, onAction, isLoading = false }: Props) {
  // Component logic
  return (
    <div>
      {isLoading ? <Spinner /> : <Content title={title} />}
    </div>
  );
}

Suspense for Data Fetching
import { Suspense } from 'react';

function ParentComponent() {
  return (
    <Suspense fallback={<LoadingSkeleton />}>
      <DataComponent />
    </Suspense>
  );
}

function DataComponent() {
  // useSuspenseQuery automatically suspends
  const { data } = useSuspenseQuery({
    queryKey: ['items'],
    queryFn: fetchItems,
  });
  
  return <ItemList items={data} />;
}

Lazy Loading Routes
import { lazy, Suspense } from 'react';

const Dashboard = lazy(() => import('./features/dashboard'));
const Settings = lazy(() => import('./features/settings'));

function App() {
  return (
    <Suspense fallback={<PageLoader />}>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Suspense>
  );
}

State Management
Local State
const [value, setValue] = useState<string>('');
const [items, setItems] = useState<Item[]>([]);

Server State (TanStack Query)
// Queries
const { data, isLoading, error } = useQuery({
  queryKey: ['users', userId],
  queryFn: () => fetchUser(userId),
});

// Mutations
const mutation = useMutation({
  mutationFn: updateUser,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['users'] });
  },
});

Global State (Zustand or Context)
// Simple global state with Zustand
const useStore = create<Store>((set) => ({
  theme: 'light',
  setTheme: (theme) => set({ theme }),
}));

Styling Best Practices
Tailwind CSS
<div className="flex items-center gap-4 p-4 bg-white rounded-lg shadow-md">
  <span className="text-lg font-semibold text-gray-900">
    {title}
  </span>
</div>

CSS Modules (when needed)
import styles from './Component.module.css';

<div className={styles.container}>
  <span className={styles.title}>{title}</span>
</div>

Styled Components / Emotion (if used)
const Container = styled.div`
  display: flex;
  align-items: center;
  padding: ${({ theme }) => theme.spacing.md};
`;

Performance Optimization
Memoization
// Memoize expensive computations
const expensiveValue = useMemo(() => {
  return computeExpensiveValue(data);
}, [data]);

// Memoize callbacks
const handleClick = useCallback((id: string) => {
  onAction(id);
}, [onAction]);

// Memoize components
const MemoizedComponent = memo(function Component({ data }: Props) {
  return <div>{data.value}</div>;
});

Code Splitting
// Route-based splitting
const Page = lazy(() => import('./Page'));

// Component-based splitting
const HeavyComponent = lazy(() => import('./HeavyComponent'));

Virtual Lists
import { useVirtualizer } from '@tanstack/react-virtual';

function VirtualList({ items }: { items: Item[] }) {
  const parentRef = useRef<HTMLDivElement>(null);
  
  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
  });
  
  return (
    <div ref={parentRef} style={{ height: '400px', overflow: 'auto' }}>
      <div style={{ height: virtualizer.getTotalSize() }}>
        {virtualizer.getVirtualItems().map((virtualItem) => (
          <div key={virtualItem.key} style={{
            position: 'absolute',
            top: virtualItem.start,
            height: virtualItem.size,
          }}>
            {items[virtualItem.index].name}
          </div>
        ))}
      </div>
    </div>
  );
}

TypeScript Best Practices
Type Definitions
// Props interfaces
interface ButtonProps {
  variant: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  onClick: () => void;
  children: React.ReactNode;
}

// API response types
interface ApiResponse<T> {
  data: T;
  meta: {
    page: number;
    total: number;
  };
}

// Utility types
type PartialUser = Partial<User>;
type RequiredUser = Required<User>;
type UserKeys = keyof User;

Strict Null Checks
// Handle potentially null values
const user = useUser();

if (!user) {
  return <NotFound />;
}

// Now TypeScript knows user is defined
return <UserProfile user={user} />;

Error Handling
Error Boundaries
import { ErrorBoundary } from 'react-error-boundary';

function ErrorFallback({ error, resetErrorBoundary }: FallbackProps) {
  return (
    <div role="alert">
      <p>Something went wrong:</p>
      <pre>{error.message}</pre>
      <button onClick={resetErrorBoundary}>Try again</button>
    </div>
  );
}

<ErrorBoundary FallbackComponent={ErrorFallback}>
  <MyComponent />
</ErrorBoundary>

Testing
Component Tests
import { render, screen, fireEvent } from '@testing-library/react';

describe('Button', () => {
  it('calls onClick when clicked', () => {
    const onClick = vi.fn();
    render(<Button onClick={onClick}>Click me</Button>);
    
    fireEvent.click(screen.getByRole('button'));
    
    expect(onClick).toHaveBeenCalledOnce();
  });
});

Hook Tests
import { renderHook, act } from '@testing-library/react';

describe('useCounter', () => {
  it('increments count', () => {
    const { result } = renderHook(() => useCounter());
    
    act(() => {
      result.current.increment();
    });
    
    expect(result.current.count).toBe(1);
  });
});

Resource Files

For detailed patterns, see:

component-patterns.md
state-management.md
performance.md
testing.md
Weekly Installs
84
Repository
bbeierle12/skil…p-claude
GitHub Stars
8
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass