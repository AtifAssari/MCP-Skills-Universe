---
title: accessibility
url: https://skills.sh/exceptionless/exceptionless/accessibility
---

# accessibility

skills/exceptionless/exceptionless/accessibility
accessibility
Installation
$ npx skills add https://github.com/exceptionless/exceptionless --skill accessibility
SKILL.md
Accessibility (WCAG 2.2 AA)
Core Principles
Semantic HTML elements and ARIA landmarks
Keyboard-first navigation with visible focus states
Skip links for main content in layouts
Inclusive, people-first language
Semantic HTML

Use <header>, <nav aria-label="...">, <main id="main-content">, <section aria-labelledby="...">, <footer>. Always use heading hierarchy (h1 → h2 → h3).

Skip Links
<a href="#main-content" class="sr-only focus:not-sr-only focus:absolute ...">
    Skip to main content
</a>

Form Accessibility
Label every control: <label for="email"> or aria-label for icon-only inputs
Required fields: Use required aria-required="true" with visual * (aria-hidden="true")
Error messages: Link via aria-describedby, set aria-invalid={hasError}
On validation failure: Focus first invalid input
Never disable submit just to block validation
<input id="email" aria-invalid={hasError} aria-describedby={hasError ? 'email-error' : undefined} />
{#if hasError}
    <p id="email-error" class="text-destructive">Please enter a valid email address</p>
{/if}

Keyboard Navigation
Natural tab order follows DOM order — avoid positive tabindex
Use tabindex="-1" for hidden/inactive elements
Dialogs: Focus first interactive element on open, return focus to trigger on close
Interactive non-button elements must handle Enter and Space key events
Icon Buttons

Always add aria-label and hide the icon from assistive technology:

<button aria-label="Delete event">
    <TrashIcon aria-hidden="true" />
</button>


When icons accompany visible text, just hide the icon: <PlusIcon aria-hidden="true" />.

ARIA Patterns

Live regions for dynamic updates:

<div aria-live="polite" aria-atomic="true">{#if loading}Loading events...{/if}</div>
<div role="alert">Error: Failed to save changes</div>


Expandable content: Use aria-expanded and aria-controls on the trigger, hidden on the panel.

Color and Contrast
Minimum contrast ratio: 4.5:1 for normal text, 3:1 for large text and UI components
Don't rely on color alone — combine with icons or text
<!-- ✅ Good: Icon + color + text -->
<span class="text-destructive"><AlertIcon aria-hidden="true" /> Error: Invalid input</span>

Testing

Use axe-playwright in E2E tests (AxeBuilder({ page }).analyze()) to catch accessibility violations.

Weekly Installs
55
Repository
exceptionless/e…tionless
GitHub Stars
2.5K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass