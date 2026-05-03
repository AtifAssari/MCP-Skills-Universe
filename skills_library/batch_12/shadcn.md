---
title: shadcn
url: https://skills.sh/thongdn-it/react-agent-skills/shadcn
---

# shadcn

skills/thongdn-it/react-agent-skills/shadcn
shadcn
Installation
$ npx skills add https://github.com/thongdn-it/react-agent-skills --skill shadcn
SKILL.md
shadcn/ui Community Best Practices

Comprehensive best practices guide for shadcn/ui applications, maintained by the shadcn/ui community. Contains 42 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Writing new shadcn/ui components or composing primitives
Implementing forms with React Hook Form and Zod validation
Building data tables or handling large dataset displays
Customizing themes or adding dark mode support
Reviewing code for accessibility compliance
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Component Architecture	CRITICAL	arch-
2	Accessibility Preservation	CRITICAL	ally-
3	Styling & Theming	HIGH	style-
4	Form Patterns	HIGH	form-
5	Data Display	MEDIUM-HIGH	data-
6	Component Composition	MEDIUM	comp-
7	Performance Optimization	MEDIUM	perf-
8	State Management	LOW-MEDIUM	state-
Quick Reference
1. Component Architecture (CRITICAL)
arch-use-asChild-for-custom-triggers - Use asChild prop for custom trigger elements
arch-preserve-radix-primitive-structure - Maintain Radix compound component hierarchy
arch-extend-variants-with-cva - Use Class Variance Authority for type-safe variants
arch-use-cn-for-class-merging - Use cn() utility for safe Tailwind class merging
arch-forward-refs-for-composable-components - Forward refs for form and focus integration
arch-isolate-component-variants - Separate base styles from variant-specific styles
2. Accessibility Preservation (CRITICAL)
ally-preserve-aria-attributes - Keep Radix ARIA attributes intact
ally-provide-sr-only-labels - Add screen reader labels for icon buttons
ally-maintain-focus-management - Preserve focus trapping in modals
ally-preserve-keyboard-navigation - Keep WAI-ARIA keyboard patterns
ally-ensure-color-contrast - Maintain WCAG color contrast ratios
3. Styling & Theming (HIGH)
style-use-css-variables-for-theming - Use CSS variables for theme colors
style-avoid-important-overrides - Never use !important for style overrides
style-use-tailwind-theme-extend - Extend Tailwind theme for design tokens
style-consistent-spacing-scale - Use consistent Tailwind spacing scale
style-responsive-design-patterns - Apply mobile-first responsive design
style-dark-mode-support - Support dark mode with CSS variables
4. Form Patterns (HIGH)
form-use-react-hook-form-integration - Integrate with React Hook Form
form-use-zod-for-schema-validation - Use Zod for type-safe validation
form-show-validation-errors-correctly - Show errors at appropriate times
form-handle-async-validation - Debounce async validation calls
form-reset-form-state-correctly - Reset form state after submission
5. Data Display (MEDIUM-HIGH)
data-use-tanstack-table-for-complex-tables - Use TanStack Table for sorting/filtering
data-virtualize-large-lists - Virtualize lists with 100+ items
data-use-skeleton-loading-states - Use Skeleton for loading states
data-paginate-server-side - Paginate large datasets server-side
data-empty-states-with-guidance - Provide actionable empty states
6. Component Composition (MEDIUM)
comp-compose-with-compound-components - Use compound component patterns
comp-use-drawer-for-mobile-modals - Use Drawer on mobile devices
comp-combine-command-with-popover - Create searchable selects with Command
comp-nest-dialogs-correctly - Manage nested dialog focus correctly
comp-create-reusable-form-fields - Extract reusable form field components
comp-use-slot-pattern-for-flexibility - Use slot pattern for flexible content
7. Performance Optimization (MEDIUM)
perf-lazy-load-heavy-components - Lazy load components over 50KB
perf-memoize-expensive-renders - Memoize list items and expensive components
perf-optimize-icon-imports - Use direct imports for Lucide icons
perf-avoid-unnecessary-rerenders-in-forms - Isolate form field watching
perf-debounce-search-inputs - Debounce search and filter inputs
8. State Management (LOW-MEDIUM)
state-prefer-uncontrolled-for-simple-inputs - Use uncontrolled for simple forms
state-lift-state-to-appropriate-level - Lift state to lowest common ancestor
state-use-controlled-dialog-state - Control dialogs for programmatic access
state-colocate-state-with-components - Keep state close to where it's used
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Full Compiled Document

For a single-file reference containing all rules, see AGENTS.md.

Reference Files
File	Description
AGENTS.md	Complete compiled guide with all rules
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
16
Repository
thongdn-it/reac…t-skills
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass