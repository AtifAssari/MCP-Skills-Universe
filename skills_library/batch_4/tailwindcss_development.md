---
title: tailwindcss-development
url: https://skills.sh/laravel/boost/tailwindcss-development
---

# tailwindcss-development

skills/laravel/boost/tailwindcss-development
tailwindcss-development
Installation
$ npx skills add https://github.com/laravel/boost --skill tailwindcss-development
SKILL.md
Tailwind CSS Development
Documentation

Use search-docs for detailed Tailwind CSS v3 patterns and documentation.

Basic Usage
Use Tailwind CSS classes to style HTML. Check and follow existing Tailwind conventions in the project before introducing new patterns.
Offer to extract repeated patterns into components that match the project's conventions (e.g., Blade, JSX, Vue).
Consider class placement, order, priority, and defaults. Remove redundant classes, add classes to parent or child elements carefully to reduce repetition, and group elements logically.
Tailwind CSS v3 Specifics
Always use Tailwind CSS v3 and verify you're using only classes it supports.
Configuration is done in the tailwind.config.js file.
Import using @tailwind directives:
@tailwind base;
@tailwind components;
@tailwind utilities;

Spacing

When listing items, use gap utilities for spacing; don't use margins.

<div class="flex gap-8">
    <div>Item 1</div>
    <div>Item 2</div>
</div>

Dark Mode

If existing pages and components support dark mode, new pages and components must support it the same way, typically using the dark: variant:

<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-white">
    Content adapts to color scheme
</div>

Common Patterns
Flexbox Layout
<div class="flex items-center justify-between gap-4">
    <div>Left content</div>
    <div>Right content</div>
</div>

Grid Layout
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <div>Card 1</div>
    <div>Card 2</div>
    <div>Card 3</div>
</div>

Verification
Check browser for visual rendering
Test responsive breakpoints
Verify dark mode if project uses it
Common Pitfalls
Using margins for spacing between siblings instead of gap utilities
Forgetting to add dark mode variants when the project uses dark mode
Not checking existing project conventions before adding new utilities
Overusing inline styles when Tailwind classes would suffice
Weekly Installs
381
Repository
laravel/boost
GitHub Stars
3.4K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass