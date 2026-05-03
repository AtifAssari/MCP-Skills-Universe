---
title: frontend-engineer
url: https://skills.sh/siviter-xyz/dot-agent/frontend-engineer
---

# frontend-engineer

skills/siviter-xyz/dot-agent/frontend-engineer
frontend-engineer
Installation
$ npx skills add https://github.com/siviter-xyz/dot-agent --skill frontend-engineer
SKILL.md
Frontend Engineer

Comprehensive guide for modern React development, emphasizing Suspense-based data fetching, lazy loading, proper file organization, and performance optimization.

When to Use
Creating new components or pages
Building new features
Fetching data with TanStack Query
Setting up routing with TanStack Router
Styling components
Performance optimization
Organizing frontend code
TypeScript best practices
Quick Start
New Component Checklist
 Use React.FC<Props> pattern with TypeScript
 Lazy load if heavy component: React.lazy(() => import())
 Wrap in <SuspenseLoader> for loading states
 Use useSuspenseQuery for data fetching
 Import aliases: @/, ~types, ~components, ~features
 Styles: Inline if <100 lines, separate file if >100 lines
 Use useCallback for event handlers passed to children
 Default export at bottom
 No early returns with loading spinners
 Use notification system for user feedback
New Feature Checklist
 Create features/{feature-name}/ directory
 Create subdirectories: api/, components/, hooks/, helpers/, types/
 Create API service file: api/{feature}Api.ts
 Set up TypeScript types in types/
 Create route in routes/{feature-name}/index.tsx
 Lazy load feature components
 Use Suspense boundaries
 Export public API from feature index.ts
Core Principles
Lazy Load Everything Heavy: Routes, DataGrid, charts, editors
Suspense for Loading: Use SuspenseLoader, not early returns
useSuspenseQuery: Primary data fetching pattern for new code
Features are Organized: api/, components/, hooks/, helpers/ subdirs
Styles Based on Size: <100 inline, >100 separate
Import Aliases: Use @/, ~types, ~components, ~features
No Early Returns: Prevents layout shift
TypeScript First: Strict mode, no any type
Implementation Workflow

When implementing frontend code:

Check for existing workflow patterns (spec-first, TDD, etc.) and follow them
Ensure code passes CI checks (types, tests, lint) before committing
Group related changes with tests in atomic commits
References

For detailed guidance, see:

references/component-patterns.md - Modern React component patterns
references/data-fetching.md - Suspense-based data fetching
references/file-organization.md - Feature-based organization
references/styling-guide.md - Styling patterns and best practices
references/routing-guide.md - TanStack Router patterns
references/performance.md - Performance optimization
references/typescript-standards.md - TypeScript best practices
Weekly Installs
189
Repository
siviter-xyz/dot-agent
GitHub Stars
11
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass