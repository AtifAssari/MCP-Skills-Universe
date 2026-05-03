---
rating: ⭐⭐⭐
title: design-system-creation
url: https://skills.sh/secondsky/claude-skills/design-system-creation
---

# design-system-creation

skills/secondsky/claude-skills/design-system-creation
design-system-creation
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill design-system-creation
SKILL.md
Design System Creation

Build comprehensive design systems for consistent UI development across teams.

Design System Layers
Foundation: Colors, typography, spacing, elevation
Components: Buttons, inputs, cards, navigation
Patterns: Forms, layouts, empty states
Foundation - Design Tokens
:root {
  /* Colors */
  --color-primary-50: #eff6ff;
  --color-primary-500: #3b82f6;
  --color-primary-900: #1e3a8a;

  /* Semantic colors */
  --color-success: #22c55e;
  --color-warning: #f59e0b;
  --color-error: #ef4444;

  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'Fira Code', monospace;

  /* Type scale */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;

  /* Spacing (4px base) */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --space-8: 2rem;

  /* Elevation */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
}

Component Documentation
## Button

### Anatomy
- Container (padding, background)
- Label (text)
- Icon (optional)

### Variants
- Primary: Main actions
- Secondary: Alternative actions
- Ghost: Subtle actions

### States
- Default, Hover, Active, Disabled, Loading

### Accessibility
- Role: button
- Keyboard: Enter/Space to activate
- Focus: Visible focus ring

Component Example (React)
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  disabled?: boolean;
  children: React.ReactNode;
}

function Button({ variant = 'primary', size = 'md', loading, disabled, children }: ButtonProps) {
  return (
    <button
      className={`btn btn-${variant} btn-${size}`}
      disabled={disabled || loading}
      aria-busy={loading}
    >
      {loading ? <Spinner /> : children}
    </button>
  );
}

Governance
Review Committee: Approves new components
Contribution Process: RFC → Review → Implementation
Versioning: Semantic versioning for releases
Deprecation: 3-month notice with migration guide
Best Practices
Start with foundational tokens
Document every component thoroughly
Ensure WCAG 2.1 AA compliance
Support dark mode from the start
Include usage guidelines with do/don't examples
Weekly Installs
176
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass