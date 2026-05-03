---
rating: ⭐⭐⭐
title: react-vite-expert
url: https://skills.sh/questfortech-investments/claude-code-skills/react-vite-expert
---

# react-vite-expert

skills/questfortech-investments/claude-code-skills/react-vite-expert
react-vite-expert
Installation
$ npx skills add https://github.com/questfortech-investments/claude-code-skills --skill react-vite-expert
SKILL.md
React + Vite Expert
Overview

Transform into a React + Vite expert with deep knowledge of modern React development patterns, optimal project organization, performance optimization techniques, and production-ready configurations. This skill provides everything needed to build fast, maintainable, and scalable React applications using Vite as the build tool.

Core Capabilities
1. Project Architecture & Organization

Guide users in structuring React applications for maximum maintainability and scalability.

Reference: references/project_architecture.md

This comprehensive guide covers:

Folder structure patterns: Feature-based, atomic design, domain-driven
File organization: Colocation strategies, naming conventions
Import strategies: Path aliases, barrel exports, tree-shaking
State management organization: Local vs global, where to put state
Scaling guidelines: How to evolve structure as app grows

When to consult:

User asks "how should I organize my React project?"
Starting a new project
Refactoring existing project structure
App is becoming hard to navigate
Need to establish team conventions

Key Decision Trees:

Feature-based vs Component-based: Read section "Optimal Folder Structure"
State management strategy: Read section "State Management Strategies"
Import organization: Read section "Import Strategies"
2. Code Generation & Scaffolding

Automate component, hook, and feature creation with production-ready templates.

Scripts available:

scripts/create_component.py Generates complete component with all necessary files:

Component file (.tsx)
TypeScript types (.types.ts)
CSS Module (.module.css)
Tests (.test.tsx)
Storybook story (.stories.tsx) [optional]
Index file for clean imports
# Create a basic component
python scripts/create_component.py Button --type component

# Create a page component with lazy loading
python scripts/create_component.py Dashboard --type page

# Create component with children prop
python scripts/create_component.py Card --children

# Create component with Storybook story
python scripts/create_component.py Button --story

# Without tests
python scripts/create_component.py SimpleComponent --no-tests


When to use:

Creating any new component
Setting up new feature modules
Need consistent component structure
Want to speed up development

scripts/create_hook.py Generates custom hooks with templates for common patterns:

State management hooks
Effect hooks
Data fetching hooks
LocalStorage hooks
Debounce hooks
Interval hooks
# Create custom hook
python scripts/create_hook.py useAuth --type custom

# Create data fetching hook
python scripts/create_hook.py useUserData --type fetch

# Create localStorage hook
python scripts/create_hook.py useSettings --type localStorage

# Create debounce hook
python scripts/create_hook.py useSearchDebounce --type debounce


When to use:

Extracting reusable logic
Creating custom state management
Need common hook patterns
Want hook with tests automatically
3. Performance Optimization

Optimize React applications for maximum performance and minimal bundle size.

Reference: references/performance_optimization.md

This guide covers:

React rendering optimization: React.memo(), useMemo(), useCallback()
Code splitting: React.lazy(), route-based splitting, component splitting
Virtualization: Long list optimization with react-window
Debouncing & throttling: Input optimization, scroll handling
Vite build optimization: Chunk splitting, minification, compression
Image optimization: WebP/AVIF, lazy loading, responsive images
Network optimization: API request optimization, prefetching
CSS performance: CSS Modules vs CSS-in-JS, critical CSS
Web Vitals tracking: Measuring LCP, FID, CLS

When to consult:

App feels slow or laggy
Large bundle sizes
Long initial load time
User asks about optimization
Preparing for production deployment
Performance audit reveals issues

Quick Performance Checklist:

Run python scripts/analyze_bundle.py to identify large dependencies
Check references/performance_optimization.md for optimization strategies
Apply code splitting for routes: React.lazy(() => import('./Page'))
Memoize expensive components: React.memo(Component)
Use useMemo() for expensive calculations
Implement virtualization for long lists (react-window)
Optimize images (WebP, lazy loading)
Review Vite config in assets/vite.config.optimized.ts

scripts/analyze_bundle.py Analyzes build output and provides optimization recommendations:

# Run bundle analysis
python scripts/analyze_bundle.py


What it analyzes:

Package.json dependencies (identifies large libraries)
Import patterns (suggests better imports for tree-shaking)
Build output (bundle sizes, chunk distribution)
Provides specific optimization recommendations

When to run:

Before production deployment
After adding new dependencies
When bundle size increases unexpectedly
Regular monthly audits
Performance optimization sessions
4. Production-Ready Configuration

Deploy optimized Vite configurations and project setups.

Assets available:

assets/vite.config.optimized.ts Fully optimized Vite configuration with:

Path aliases: Clean imports (@/components, @/hooks, etc.)
Manual chunk splitting: Vendor, feature-based chunks for better caching
Minification: Terser with console.log removal in production
Bundle analyzer: Visualize bundle composition
Asset optimization: Image handling, font loading
Development proxy: API proxy configuration
Source maps: Conditional source map generation
CSS code splitting: Automatic CSS chunking

When to use:

Starting new project
Optimizing existing build
Setting up production pipeline
Need better caching strategy
Want to analyze bundle

How to use:

Copy assets/vite.config.optimized.ts to project root
Install dependencies: npm install -D rollup-plugin-visualizer
Customize manual chunks for your features
Run build with analyzer: npm run build:analyze

assets/tsconfig.optimized.json TypeScript configuration with:

Strict mode enabled: Catch more errors at compile time
Path aliases: Matching Vite config
Optimal compiler options: For Vite and modern React
Unused code detection: noUnusedLocals, noUnusedParameters
Type safety: noImplicitReturns, noUncheckedIndexedAccess

When to use:

Starting new TypeScript project
Want stricter type checking
Need path aliases
Improving type safety

assets/package.json.example Complete package.json with:

All recommended scripts: dev, build, test, lint, format
Essential dependencies: React, React DOM, Router
Dev dependencies: TypeScript, ESLint, Prettier, Vitest
Recommended optional dependencies: Categorized by use case
Husky & lint-staged setup: Pre-commit hooks
CI/CD scripts: For automated pipelines

When to use:

Starting new project
Need script recommendations
Setting up CI/CD
Want git hooks
Need package reference

assets/project-structure-example.md Complete project structure with:

Full directory tree: Feature-based architecture
Key file examples: App.tsx, router, providers, API setup
Configuration examples: vitest, eslint, prettier
Test setup: Testing utilities and mocks
Scaling guidelines: How to grow the structure

When to use:

Starting new project from scratch
Need structure reference
Refactoring existing project
Teaching team about organization
Creating project templates
5. React Best Practices & Patterns

Implement modern React patterns and avoid common pitfalls.

Reference: references/best_practices.md

This guide covers:

Component patterns: Compound components, render props, HOC, custom hooks
TypeScript best practices: Typing components, hooks, events, generic components
Error handling: Error boundaries, async error handling
Form handling: Controlled components, validation, form libraries
Testing: Component testing, hook testing, mocking
Common anti-patterns: What to avoid and why
Accessibility: a11y best practices, ARIA, keyboard navigation

When to consult:

Implementing complex component patterns
Need TypeScript guidance
Setting up error handling
Creating forms
Writing tests
User asks "what's the best way to...?"
Code review requests
Teaching React patterns

Pattern Decision Guide:

Compound Components: For flexible, composable UI (Tabs, Accordion)
Custom Hooks: Extract and reuse logic (useAuth, useDebounce)
Context + Hook: Share state across tree (Theme, Auth)
Render Props: Share code with render control (rare, mostly replaced by hooks)
HOC: Add cross-cutting concerns (rare, mostly replaced by hooks)
6. TypeScript Excellence

Write type-safe React code with proper TypeScript patterns.

Key TypeScript patterns in references/best_practices.md:

Component prop typing (interfaces vs types)
Event handler typing
Ref typing
Generic component typing
Hook typing
Type guards and narrowing
Utility types

When user asks about TypeScript:

Read relevant section in references/best_practices.md
Provide type-safe examples
Explain the "why" behind the pattern
Show both the wrong and right way

Common TypeScript Questions:

"How do I type this component?" → Component Props Typing section
"How do I type an event handler?" → Hooks Typing section
"How do I make a generic component?" → Generic Components section
"How do I type a ref?" → Hooks Typing section
7. Testing Strategy

Implement comprehensive testing for React applications.

Testing patterns in references/best_practices.md:

Component testing with React Testing Library
Custom hook testing
Test utilities and setup
Mocking strategies
Integration testing

Testing Philosophy:

Test user behavior, not implementation
Test what the user sees and does
Mock external dependencies
Use descriptive test names
Arrange-Act-Assert pattern

When user needs testing help:

Check if component generator created tests: scripts/create_component.py
Reference testing section in references/best_practices.md
Show test setup in assets/project-structure-example.md
Provide specific test examples for their use case
8. State Management Guidance

Choose and implement the right state management solution.

State management decision tree (from references/project_architecture.md):

Is it server data (from API)?
└─ Yes → TanStack Query (React Query)

Is it local to a component?
└─ Yes → useState

Is it shared between 2-3 components?
└─ Yes → Lift state up (props)

Is it global but simple (theme, auth)?
└─ Yes → Context + useState

Is it global and complex?
├─ Small/medium app → Zustand
└─ Large app with complex async → Redux Toolkit


When to consult references/project_architecture.md:

Choosing state management solution
Need code examples for each approach
Understanding trade-offs
Migrating state management
Performance issues with re-renders
Workflow Examples
Example 1: "Help me start a new React project with best practices"

Understand requirements:

Ask about: Project size, features, state needs, team size
Determine: Which patterns to use, structure complexity

Provide structure:

Show assets/project-structure-example.md
Explain feature-based vs simpler architecture
Recommend based on project size

Set up configuration:

Copy assets/vite.config.optimized.ts
Copy assets/tsconfig.optimized.json
Reference assets/package.json.example for scripts

Generate initial components:

# Create basic UI components
python scripts/create_component.py Button --type component --story
python scripts/create_component.py Input --type component

# Create pages
python scripts/create_component.py HomePage --type page

# Create hooks
python scripts/create_hook.py useAuth --type custom


Explain next steps:

Set up git hooks (husky)
Configure ESLint and Prettier
Set up testing
Create initial routes
Example 2: "My React app is slow, how do I optimize it?"

Analyze current state:

# Run bundle analyzer
python scripts/analyze_bundle.py


Review analysis output:

Identify large dependencies
Check for duplicates
Review import patterns

Consult optimization guide:

Read references/performance_optimization.md
Focus on relevant sections based on analysis

Apply optimizations (in order of impact):

Code splitting: Implement lazy loading for routes
Remove large dependencies: Suggest lighter alternatives
Memoization: Add React.memo() to expensive components
Virtualization: If rendering long lists
Image optimization: Implement lazy loading, WebP format
Build optimization: Apply assets/vite.config.optimized.ts

Measure improvement:

Run build before and after
Compare bundle sizes
Test Web Vitals
Example 3: "How should I organize my growing React project?"

Assess current size:

Ask: How many components? How many features?
Determine: Current pain points

Reference architecture guide:

Read references/project_architecture.md
Section: "Optimal Folder Structure"

Recommend structure:

Small (<10 components): Flat structure
Medium (10-50): Feature folders + shared components
Large (50+): Full feature-based architecture

Show concrete example:

Display relevant section from assets/project-structure-example.md
Explain each folder's purpose

Provide migration path:

Don't refactor everything at once
Start with new features in new structure
Gradually migrate old code
Example 4: "I need to create many similar components"

Use component generator:

# Generate multiple components at once
python scripts/create_component.py UserCard --type component
python scripts/create_component.py ProductCard --type component
python scripts/create_component.py OrderCard --type component


Explain structure:

Show generated files
Explain each file's purpose
Customize as needed

Create shared patterns:

Extract common props to shared type
Create base Card component
Use composition pattern

Reference patterns guide:

Show compound component pattern from references/best_practices.md
Demonstrate component composition
Example 5: "Help me set up testing for my React app"

Reference testing setup:

Show assets/project-structure-example.md
Section: "src/test/" folder structure

Set up test utilities:

Copy test setup from example
Configure vitest.config.ts
Create test utilities (render with providers)

Generate components with tests:

# Components come with tests by default
python scripts/create_component.py Button


Explain testing patterns:

Reference references/best_practices.md
Section: "Testing Best Practices"
Show component and hook testing examples

Set up CI/CD:

Add test scripts from assets/package.json.example
Configure pre-commit hooks
Set up GitHub Actions
Best Practices for Using This Skill
Be Comprehensive
Don't just answer questions - provide complete solutions
Show file structure, configuration, and examples
Explain the "why" behind recommendations
Use All Resources
Scripts: Generate code for consistency
References: Deep dives into concepts
Assets: Production-ready configs and examples
Follow This Order
Understand: Ask clarifying questions
Reference: Consult relevant documentation
Generate: Use scripts when applicable
Explain: Teach the pattern/concept
Provide: Give complete working examples
Prioritize Performance
Proactively suggest optimizations
Run bundle analyzer regularly
Recommend lazy loading by default
Use optimized configurations
Teach Best Practices
Show the wrong way vs the right way
Explain trade-offs
Reference TypeScript strict mode
Encourage testing
Stay Organized
Recommend feature-based structure early
Use path aliases from the start
Establish naming conventions
Plan for scale
Reference Documentation
references/project_architecture.md

Read when:

Structuring new project
Organizing existing project
Choosing state management
Setting up imports
User asks "how should I organize...?"

Key sections:

Optimal Folder Structure (2 patterns)
Naming Conventions
Component Organization Patterns
State Management Strategies
Import Strategies
Decision Matrix
references/performance_optimization.md

Read when:

App is slow
Large bundle sizes
Optimizing for production
User asks about performance
Before deployment

Key sections:

React Rendering Optimization (memo, useMemo, useCallback)
Code Splitting
Virtualization
Vite Build Optimization
Image Optimization
Network Performance
CSS Performance
Web Vitals Tracking
references/best_practices.md

Read when:

Implementing patterns
TypeScript questions
Error handling setup
Form implementation
Testing questions
Code review

Key sections:

Component Patterns (5 patterns)
TypeScript Best Practices
Error Handling Patterns
Form Handling
Testing Best Practices
Common Anti-Patterns
Accessibility
Quick Reference
Common Commands
# Generate component
python scripts/create_component.py ComponentName --type component

# Generate page
python scripts/create_component.py PageName --type page

# Generate hook
python scripts/create_hook.py useHookName --type custom

# Analyze bundle
python scripts/analyze_bundle.py

Common Questions
"How do I structure my project?" → references/project_architecture.md
"How do I optimize performance?" → references/performance_optimization.md + run analyze_bundle.py
"What pattern should I use?" → references/best_practices.md
"How do I configure Vite?" → assets/vite.config.optimized.ts
"What should my package.json look like?" → assets/package.json.example
File Structure Priority
Feature-based (large apps) - See references/project_architecture.md
Component-based (medium apps) - See simpler structure
Flat (small apps) - Minimal organization
Performance Priority
Code splitting (routes first)
Remove large dependencies
Lazy loading (images, components)
Memoization (expensive components)
Virtualization (long lists)
State Management Priority
Server data → React Query
Local state → useState
Shared simple state → Context
Global complex state → Zustand or Redux Toolkit
When NOT to Use This Skill
Non-React frameworks: Next.js has its own patterns (use Next.js skill)
React Native: Mobile has different patterns
Class components: Focus is on modern functional components
Non-Vite build tools: Webpack/Parcel have different configs
Backend development: This is frontend-focused

For these topics, provide general React guidance but acknowledge limitations.

Success Metrics

Your React + Vite project should achieve:

✅ Bundle size < 200KB (initial, gzipped)
✅ Lighthouse score > 90
✅ All tests passing
✅ No ESLint errors
✅ Consistent file structure
✅ Type-safe (TypeScript strict mode)
✅ Fast build times (< 30s for production)
✅ Fast HMR (< 100ms)
Weekly Installs
224
Repository
questfortech-in…e-skills
GitHub Stars
4
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass