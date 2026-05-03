---
title: tailwind-4
url: https://skills.sh/prowler-cloud/prowler/tailwind-4
---

# tailwind-4

skills/prowler-cloud/prowler/tailwind-4
tailwind-4
Installation
$ npx skills add https://github.com/prowler-cloud/prowler --skill tailwind-4
SKILL.md
Styling Decision Tree
Tailwind class exists?  → className="..."
Dynamic value?          → style={{ width: `${x}%` }}
Conditional styles?     → cn("base", condition && "variant")
Static only?            → className="..." (no cn() needed)
Library can't use class?→ style prop with var() constants

Critical Rules
Never Use var() in className
// ❌ NEVER: var() in className
<div className="bg-[var(--color-primary)]" />
<div className="text-[var(--text-color)]" />

// ✅ ALWAYS: Use Tailwind semantic classes
<div className="bg-primary" />
<div className="text-slate-400" />

Never Use Hex Colors
// ❌ NEVER: Hex colors in className
<p className="text-[#ffffff]" />
<div className="bg-[#1e293b]" />

// ✅ ALWAYS: Use Tailwind color classes
<p className="text-white" />
<div className="bg-slate-800" />

The cn() Utility
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

When to Use cn()
// ✅ Conditional classes
<div className={cn("base-class", isActive && "active-class")} />

// ✅ Merging with potential conflicts
<button className={cn("px-4 py-2", className)} />  // className might override

// ✅ Multiple conditions
<div className={cn(
  "rounded-lg border",
  variant === "primary" && "bg-blue-500 text-white",
  variant === "secondary" && "bg-gray-200 text-gray-800",
  disabled && "opacity-50 cursor-not-allowed"
)} />

When NOT to Use cn()
// ❌ Static classes - unnecessary wrapper
<div className={cn("flex items-center gap-2")} />

// ✅ Just use className directly
<div className="flex items-center gap-2" />

Style Constants for Charts/Libraries

When libraries don't accept className (like Recharts):

// ✅ Constants with var() - ONLY for library props
const CHART_COLORS = {
  primary: "var(--color-primary)",
  secondary: "var(--color-secondary)",
  text: "var(--color-text)",
  gridLine: "var(--color-border)",
};

// Usage with Recharts (can't use className)
<XAxis tick={{ fill: CHART_COLORS.text }} />
<CartesianGrid stroke={CHART_COLORS.gridLine} />

Dynamic Values
// ✅ style prop for truly dynamic values
<div style={{ width: `${percentage}%` }} />
<div style={{ opacity: isVisible ? 1 : 0 }} />

// ✅ CSS custom properties for theming
<div style={{ "--progress": `${value}%` } as React.CSSProperties} />

Common Patterns
Flexbox
<div className="flex items-center justify-between gap-4" />
<div className="flex flex-col gap-2" />
<div className="inline-flex items-center" />

Grid
<div className="grid grid-cols-3 gap-4" />
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" />

Spacing
// Padding
<div className="p-4" />           // All sides
<div className="px-4 py-2" />     // Horizontal, vertical
<div className="pt-4 pb-2" />     // Top, bottom

// Margin
<div className="m-4" />
<div className="mx-auto" />       // Center horizontally
<div className="mt-8 mb-4" />

Typography
<h1 className="text-2xl font-bold text-white" />
<p className="text-sm text-slate-400" />
<span className="text-xs font-medium uppercase tracking-wide" />

Borders & Shadows
<div className="rounded-lg border border-slate-700" />
<div className="rounded-full shadow-lg" />
<div className="ring-2 ring-blue-500 ring-offset-2" />

States
<button className="hover:bg-blue-600 focus:ring-2 active:scale-95" />
<input className="focus:border-blue-500 focus:outline-none" />
<div className="group-hover:opacity-100" />

Responsive
<div className="w-full md:w-1/2 lg:w-1/3" />
<div className="hidden md:block" />
<div className="text-sm md:text-base lg:text-lg" />

Dark Mode
<div className="bg-white dark:bg-slate-900" />
<p className="text-gray-900 dark:text-white" />

Arbitrary Values (Escape Hatch)
// ✅ OK for one-off values not in design system
<div className="w-[327px]" />
<div className="top-[117px]" />
<div className="grid-cols-[1fr_2fr_1fr]" />

// ❌ Don't use for colors - use theme instead
<div className="bg-[#1e293b]" />  // NO

Weekly Installs
320
Repository
prowler-cloud/prowler
GitHub Stars
13.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass