---
title: senior-frontend
url: https://skills.sh/alirezarezvani/claude-skills/senior-frontend
---

# senior-frontend

skills/alirezarezvani/claude-skills/senior-frontend
senior-frontend
Installation
$ npx skills add https://github.com/alirezarezvani/claude-skills --skill senior-frontend
Summary

Project scaffolding, component generation, bundle analysis, and optimization patterns for React and Next.js applications.

Scaffolds new Next.js or React projects with TypeScript, Tailwind CSS, and optional features (auth, API client, forms, testing, Storybook)
Generates typed React components, server components, custom hooks, and associated test and story files
Analyzes bundle size and identifies heavy dependencies with lighter alternatives (moment → dayjs, lodash → lodash-es, @mui/material → shadcn/ui)
Covers React patterns (compound components, custom hooks, render props) and Next.js best practices (Server vs Client Components, image optimization, data fetching with Suspense)
Includes accessibility checklist and testing strategies using React Testing Library and Vitest
SKILL.md
Senior Frontend

Frontend development patterns, performance optimization, and automation tools for React/Next.js applications.

Table of Contents
Project Scaffolding
Component Generation
Bundle Analysis
React Patterns
Next.js Optimization
Accessibility and Testing
Project Scaffolding

Generate a new Next.js or React project with TypeScript, Tailwind CSS, and best practice configurations.

Workflow: Create New Frontend Project

Run the scaffolder with your project name and template:

python scripts/frontend_scaffolder.py my-app --template nextjs


Add optional features (auth, api, forms, testing, storybook):

python scripts/frontend_scaffolder.py dashboard --template nextjs --features auth,api


Navigate to the project and install dependencies:

cd my-app && npm install


Start the development server:

npm run dev

Scaffolder Options
Option	Description
--template nextjs	Next.js 14+ with App Router and Server Components
--template react	React + Vite with TypeScript
--features auth	Add NextAuth.js authentication
--features api	Add React Query + API client
--features forms	Add React Hook Form + Zod validation
--features testing	Add Vitest + Testing Library
--dry-run	Preview files without creating them
Generated Structure (Next.js)
my-app/
├── app/
│   ├── layout.tsx        # Root layout with fonts
│   ├── page.tsx          # Home page
│   ├── globals.css       # Tailwind + CSS variables
│   └── api/health/route.ts
├── components/
│   ├── ui/               # Button, Input, Card
│   └── layout/           # Header, Footer, Sidebar
├── hooks/                # useDebounce, useLocalStorage
├── lib/                  # utils (cn), constants
├── types/                # TypeScript interfaces
├── tailwind.config.ts
├── next.config.js
└── package.json

Component Generation

Generate React components with TypeScript, tests, and Storybook stories.

Workflow: Create a New Component

Generate a client component:

python scripts/component_generator.py Button --dir src/components/ui


Generate a server component:

python scripts/component_generator.py ProductCard --type server


Generate with test and story files:

python scripts/component_generator.py UserProfile --with-test --with-story


Generate a custom hook:

python scripts/component_generator.py FormValidation --type hook

Generator Options
Option	Description
--type client	Client component with 'use client' (default)
--type server	Async server component
--type hook	Custom React hook
--with-test	Include test file
--with-story	Include Storybook story
--flat	Create in output dir without subdirectory
--dry-run	Preview without creating files
Generated Component Example
'use client';

import { useState } from 'react';
import { cn } from '@/lib/utils';

interface ButtonProps {
  className?: string;
  children?: React.ReactNode;
}

export function Button({ className, children }: ButtonProps) {
  return (
    <div className={cn('', className)}>
      {children}
    </div>
  );
}

Bundle Analysis

Analyze package.json and project structure for bundle optimization opportunities.

Workflow: Optimize Bundle Size

Run the analyzer on your project:

python scripts/bundle_analyzer.py /path/to/project


Review the health score and issues:

Bundle Health Score: 75/100 (C)

HEAVY DEPENDENCIES:
  moment (290KB)
    Alternative: date-fns (12KB) or dayjs (2KB)

  lodash (71KB)
    Alternative: lodash-es with tree-shaking


Apply the recommended fixes by replacing heavy dependencies.

Re-run with verbose mode to check import patterns:

python scripts/bundle_analyzer.py . --verbose

Bundle Score Interpretation
Score	Grade	Action
90-100	A	Bundle is well-optimized
80-89	B	Minor optimizations available
70-79	C	Replace heavy dependencies
60-69	D	Multiple issues need attention
0-59	F	Critical bundle size problems
Heavy Dependencies Detected

The analyzer identifies these common heavy packages:

Package	Size	Alternative
moment	290KB	date-fns (12KB) or dayjs (2KB)
lodash	71KB	lodash-es with tree-shaking
axios	14KB	Native fetch or ky (3KB)
jquery	87KB	Native DOM APIs
@mui/material	Large	shadcn/ui or Radix UI
React Patterns

Reference: references/react_patterns.md

Compound Components

Share state between related components:

const Tabs = ({ children }) => {
  const [active, setActive] = useState(0);
  return (
    <TabsContext.Provider value={{ active, setActive }}>
      {children}
    </TabsContext.Provider>
  );
};

Tabs.List = TabList;
Tabs.Panel = TabPanel;

// Usage
<Tabs>
  <Tabs.List>
    <Tabs.Tab>One</Tabs.Tab>
    <Tabs.Tab>Two</Tabs.Tab>
  </Tabs.List>
  <Tabs.Panel>Content 1</Tabs.Panel>
  <Tabs.Panel>Content 2</Tabs.Panel>
</Tabs>

Custom Hooks

Extract reusable logic:

function useDebounce<T>(value: T, delay = 500): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}

// Usage
const debouncedSearch = useDebounce(searchTerm, 300);

Render Props

Share rendering logic:

function DataFetcher({ url, render }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(url).then(r => r.json()).then(setData).finally(() => setLoading(false));
  }, [url]);

  return render({ data, loading });
}

// Usage
<DataFetcher
  url="/api/users"
  render={({ data, loading }) =>
    loading ? <Spinner /> : <UserList users={data} />
  }
/>

Next.js Optimization

Reference: references/nextjs_optimization_guide.md

Server vs Client Components

Use Server Components by default. Add 'use client' only when you need:

Event handlers (onClick, onChange)
State (useState, useReducer)
Effects (useEffect)
Browser APIs
// Server Component (default) - no 'use client'
async function ProductPage({ params }) {
  const product = await getProduct(params.id);  // Server-side fetch

  return (
    <div>
      <h1>{product.name}</h1>
      <AddToCartButton productId={product.id} />  {/* Client component */}
    </div>
  );
}

// Client Component
'use client';
function AddToCartButton({ productId }) {
  const [adding, setAdding] = useState(false);
  return <button onClick={() => addToCart(productId)}>Add</button>;
}

Image Optimization
import Image from 'next/image';

// Above the fold - load immediately
<Image
  src="/hero.jpg"
  alt="Hero"
  width={1200}
  height={600}
  priority
/>

// Responsive image with fill
<div className="relative aspect-video">
  <Image
    src="/product.jpg"
    alt="Product"
    fill
    sizes="(max-width: 768px) 100vw, 50vw"
    className="object-cover"
  />
</div>

Data Fetching Patterns
// Parallel fetching
async function Dashboard() {
  const [user, stats] = await Promise.all([
    getUser(),
    getStats()
  ]);
  return <div>...</div>;
}

// Streaming with Suspense
async function ProductPage({ params }) {
  return (
    <div>
      <ProductDetails id={params.id} />
      <Suspense fallback={<ReviewsSkeleton />}>
        <Reviews productId={params.id} />
      </Suspense>
    </div>
  );
}

Accessibility and Testing

Reference: references/frontend_best_practices.md

Accessibility Checklist
Semantic HTML: Use proper elements (<button>, <nav>, <main>)
Keyboard Navigation: All interactive elements focusable
ARIA Labels: Provide labels for icons and complex widgets
Color Contrast: Minimum 4.5:1 for normal text
Focus Indicators: Visible focus states
// Accessible button
<button
  type="button"
  aria-label="Close dialog"
  onClick={onClose}
  className="focus-visible:ring-2 focus-visible:ring-blue-500"
>
  <XIcon aria-hidden="true" />
</button>

// Skip link for keyboard users
<a href="#main-content" className="sr-only focus:not-sr-only">
  Skip to main content
</a>

Testing Strategy
// Component test with React Testing Library
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('button triggers action on click', async () => {
  const onClick = vi.fn();
  render(<Button onClick={onClick}>Click me</Button>);

  await userEvent.click(screen.getByRole('button'));
  expect(onClick).toHaveBeenCalledTimes(1);
});

// Test accessibility
test('dialog is accessible', async () => {
  render(<Dialog open={true} title="Confirm" />);

  expect(screen.getByRole('dialog')).toBeInTheDocument();
  expect(screen.getByRole('dialog')).toHaveAttribute('aria-labelledby');
});

Quick Reference
Common Next.js Config
// next.config.js
const nextConfig = {
  images: {
    remotePatterns: [{ hostname: "cdnexamplecom" }],
    formats: ['image/avif', 'image/webp'],
  },
  experimental: {
    optimizePackageImports: ['lucide-react', '@heroicons/react'],
  },
};

Tailwind CSS Utilities
// Conditional classes with cn()
import { cn } from '@/lib/utils';

<button className={cn(
  'px-4 py-2 rounded',
  variant === 'primary' && 'bg-blue-500 text-white',
  disabled && 'opacity-50 cursor-not-allowed'
)} />

TypeScript Patterns
// Props with children
interface CardProps {
  className?: string;
  children: React.ReactNode;
}

// Generic component
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return <ul>{items.map(renderItem)}</ul>;
}

Resources
React Patterns: references/react_patterns.md
Next.js Optimization: references/nextjs_optimization_guide.md
Best Practices: references/frontend_best_practices.md
Weekly Installs
338
Repository
alirezarezvani/…e-skills
GitHub Stars
13.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass