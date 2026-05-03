---
rating: ⭐⭐
title: reactive-dashboard-performance
url: https://skills.sh/erichowens/some_claude_skills/reactive-dashboard-performance
---

# reactive-dashboard-performance

skills/erichowens/some_claude_skills/reactive-dashboard-performance
reactive-dashboard-performance
Installation
$ npx skills add https://github.com/erichowens/some_claude_skills --skill reactive-dashboard-performance
SKILL.md
Reactive Dashboard Performance

Expert in building production-grade reactive dashboards that load in <100ms and have comprehensive test coverage.

Core Expertise
Performance Patterns (Linear, Vercel, Notion-grade)

Skeleton-First Loading

Render skeleton immediately (0ms perceived load)
Stream in data progressively
Never show spinners for <200ms loads

Aggressive Caching

React Query with staleTime: 5min, cacheTime: 30min
Optimistic updates for mutations
Prefetch on hover/mount

Code Splitting

Route-based splitting (Next.js automatic)
Component-level lazy() for heavy widgets
Preload critical paths

Memoization Strategy

useMemo for expensive computations
React.memo for pure components
useCallback for stable references
Testing Reactive Dashboards

Mock Strategy

Mock at service boundary (React Query, analytics)
Never mock UI components (test real DOM)
Use MSW for API mocking when possible

Async Handling

// WRONG - races with React
render(<Dashboard />);
const element = screen.getByText('Welcome');

// RIGHT - waits for async resolution
render(<Dashboard />);
const element = await screen.findByText('Welcome');


Timeout Debugging

Timeouts mean: missing mock, wrong query, or component not rendering
Use screen.debug() to see actual DOM
Check console for unmocked errors

Test Wrapper Pattern

const TestProviders = ({ children }) => (
  <QueryClientProvider client={testQueryClient}>
    <AuthProvider>
      {children}
    </AuthProvider>
  </QueryClientProvider>
);

Real-World Examples
Linear Dashboard: Skeleton → Stale data → Fresh data (perceived <50ms)
Vercel Dashboard: Prefetch on nav hover, optimistic deploys
Notion Pages: Infinite cache, local-first, sync in background
Diagnostic Protocol
Integration Test Timeouts

Check what's actually rendering

render(<Component />);
screen.debug(); // See actual DOM


Find unmocked dependencies

Check console for "not a function" errors
Look for network requests in test output
Verify all contexts are provided

Fix async queries

Use findBy* instead of getBy*
Increase timeout if needed: waitFor(() => {...}, { timeout: 3000 })
Mock React Query properly

Simplify component tree

Test widgets individually first
Add full integration tests last
Use data-testid for complex queries
Performance Optimization
Dashboard Load Budget
Phase	Target
Skeleton render	0-16ms (1 frame)
First data paint	<100ms
Full interactive	<200ms
Lazy widgets	<500ms
React Query Config
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000, // 5min
      cacheTime: 30 * 60 * 1000, // 30min
      refetchOnWindowFocus: false,
      refetchOnMount: false,
      retry: 1,
    },
  },
});

Skeleton Pattern
function Dashboard() {
  const { data, isLoading } = useQuery('dashboard', fetchDashboard);

  // Show skeleton immediately, no loading check
  return (
    <div>
      {data ? <RealWidget data={data} /> : <SkeletonWidget />}
    </div>
  );
}

Common Pitfalls
Spinners for fast loads - Use skeletons instead
Unmemoized expensive computations - Wrap in useMemo
Testing implementation details - Test user behavior
Mocking too much - Mock at boundaries only
Synchronous test expectations - Everything is async

When debugging test timeouts, ALWAYS start with screen.debug() to see what actually rendered.

Weekly Installs
116
Repository
erichowens/some…e_skills
GitHub Stars
98
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass