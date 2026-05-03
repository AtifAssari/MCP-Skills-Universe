---
title: tailwind-css
url: https://skills.sh/dralgorhythm/claude-agentic-framework/tailwind-css
---

# tailwind-css

skills/dralgorhythm/claude-agentic-framework/tailwind-css
tailwind-css
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill tailwind-css
SKILL.md
Tailwind CSS 4.x

Platform: Web (Tailwind CSS 4.x). For mobile styling, see the nativewind skill (Tailwind 3.x for React Native).

Overview

Utility-first CSS framework for rapid UI development. Tailwind CSS 4.x introduces a CSS-first configuration approach, automatic content detection, and improved performance with a new engine.

Install: pnpm add -D tailwindcss @tailwindcss/vite

API Reference: Use Context7 MCP for full utility class reference (mcp__context7__resolve-library-id → tailwindcss).

Key Changes in v4
CSS-first configuration - Use @theme in CSS instead of tailwind.config.js
Single import - Use @import "tailwindcss" instead of separate directives
Automatic content detection - No content array needed
New color system - OKLCH colors with wide gamut support
Built-in Vite plugin - @tailwindcss/vite for optimal integration
Workflows

Setting up Tailwind v4:

 Install dependencies: pnpm add -D tailwindcss @tailwindcss/vite
 Add Vite plugin to vite.config.ts
 Create index.css with @import "tailwindcss"
 Customize theme with @theme directive
 Test build process and verify styles load

Creating components:

 Start with semantic HTML structure
 Apply utility classes for layout (flex, grid)
 Add spacing utilities (p-, m-, gap-*)
 Style with color, typography, borders
 Add responsive variants (sm:, md:, lg:)
 Test in multiple viewports

Custom theme:

 Define design tokens using @theme in CSS
 Add custom colors, spacing, fonts
 Create semantic color aliases
 Verify tokens work across components
Configuration
Vite Configuration
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [react(), tailwindcss()],
});

CSS Entry Point
/* src/index.css */
@import "tailwindcss";

@theme {
  /* Brand colors (OKLCH for wide gamut) */
  --color-primary: oklch(0.6 0.2 250);
  --color-secondary: oklch(0.6 0.15 300);
  --color-success: oklch(0.7 0.2 150);
  --color-warning: oklch(0.8 0.15 85);
  --color-danger: oklch(0.6 0.25 25);

  /* Typography */
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "Fira Code", monospace;

  /* Custom spacing */
  --spacing-128: 32rem;

  /* Custom animations */
  --animate-fade-in: fade-in 0.3s ease-out;
}

@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Dark mode variant */
@variant dark (&:where(.dark, .dark *));

Responsive Design

Default breakpoints (mobile-first): sm: 640px | md: 768px | lg: 1024px | xl: 1280px | 2xl: 1536px

// Stack on mobile, grid on desktop
<div className="flex flex-col md:flex-row gap-4">
  <div className="w-full md:w-1/2">Left</div>
  <div className="w-full md:w-1/2">Right</div>
</div>

// Responsive grid
<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
  {items.map(item => <div key={item.id} className="rounded-lg border p-4">{item.content}</div>)}
</div>

// Responsive typography
<h1 className="text-2xl sm:text-3xl md:text-4xl lg:text-5xl">Scales with viewport</h1>

// Show/hide at breakpoints
<div className="hidden lg:block">Desktop only</div>
<div className="block lg:hidden">Mobile only</div>


Custom breakpoints: add --breakpoint-demo: 1440px; in @theme.

Dark Mode
function App() {
  const [isDark, setIsDark] = useState(false);
  useEffect(() => { document.documentElement.classList.toggle('dark', isDark); }, [isDark]);
  return (
    <div className="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
      <button onClick={() => setIsDark(!isDark)}>Toggle Dark Mode</button>
    </div>
  );
}

Component Patterns
Buttons
// Primary
<button className="rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors">
  Primary
</button>

// Secondary
<button className="rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-colors">
  Secondary
</button>

Cards
// Basic card
<div className="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
  <h3 className="text-lg font-semibold text-gray-900">Card Title</h3>
  <p className="mt-2 text-sm text-gray-600">Description</p>
</div>

// Card with header/footer
<div className="rounded-lg border border-gray-200 bg-white overflow-hidden">
  <div className="border-b border-gray-200 bg-gray-50 px-6 py-4">
    <h3 className="text-lg font-semibold text-gray-900">Header</h3>
  </div>
  <div className="p-6"><p className="text-sm text-gray-600">Content</p></div>
  <div className="border-t border-gray-200 bg-gray-50 px-6 py-4">
    <button className="text-sm font-medium text-blue-600 hover:text-blue-700">Action</button>
  </div>
</div>

Form Input
<div className="space-y-1">
  <label htmlFor="email" className="block text-sm font-medium text-gray-700">Email</label>
  <input
    type="email"
    id="email"
    className="block w-full rounded-md border border-gray-300 px-3 py-2 text-sm placeholder-gray-400 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
    placeholder="you@example.com"
  />
</div>

Advanced Patterns
Variant Modifiers
// Group hover — child reacts to parent hover
<div className="group hover:bg-gray-100">
  <h3 className="group-hover:text-blue-600">Changes on parent hover</h3>
</div>

// Peer — sibling state
<input type="checkbox" className="peer" />
<label className="peer-checked:text-blue-600">Changes when checked</label>

// Data attributes
<div data-state="active" className="data-[state=active]:bg-blue-100">Active state</div>

// Structural: first:, last:, odd:, even:
<li className="first:rounded-t-lg last:rounded-b-lg border-b last:border-b-0">Item</li>

Arbitrary Values and Custom Utilities
// Arbitrary values with []
<div className="top-[117px] bg-[#1da1f2] grid-cols-[1fr_500px_2fr]">Custom values</div>
<div className="w-[calc(100%-2rem)] bg-[var(--brand-color)]">CSS var + calc</div>

/* Custom utilities with @utility */
@utility scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
  &::-webkit-scrollbar { display: none; }
}

Migration from v3
v3 Pattern	v4 Pattern
tailwind.config.js	@theme in CSS
@tailwind base; etc.	@import "tailwindcss"
content: [...]	Automatic detection
PostCSS plugin	@tailwindcss/vite plugin

Steps: Install new packages → replace PostCSS config with Vite plugin → replace @tailwind directives → move theme to @theme → remove content array → test.

Best Practices
Mobile-first approach - Start with base styles, add responsive variants
Use semantic color names - primary, secondary, danger via @theme
Keep classes organized - Layout → Spacing → Colors → Typography → States
Use arbitrary values sparingly - Prefer theme tokens
Group hover/focus states with group-* and peer-* utilities
Use the Vite plugin - @tailwindcss/vite for best performance
Anti-Patterns
Using tailwind.config.js for customization (use @theme)
Using @tailwind directives (use @import "tailwindcss")
Manually configuring content array (auto-detected in v4)
Using PostCSS plugin with Vite (use @tailwindcss/vite)
Desktop-first responsive design (not mobile-friendly)
Hardcoding colors instead of using theme tokens
Ignoring accessibility (missing focus states)
Feedback Loops
# Check generated CSS size (target < 50KB)
pnpm build

# Watch for changes
pnpm dev


Test focus states by tabbing through interactive elements. Verify focus:ring-* utilities are visible. Check color contrast in browser devtools.

Weekly Installs
37
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