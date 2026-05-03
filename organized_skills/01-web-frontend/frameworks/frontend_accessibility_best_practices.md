---
rating: ⭐⭐
title: frontend-accessibility-best-practices
url: https://skills.sh/sergiodxa/agent-skills/frontend-accessibility-best-practices
---

# frontend-accessibility-best-practices

skills/sergiodxa/agent-skills/frontend-accessibility-best-practices
frontend-accessibility-best-practices
Installation
$ npx skills add https://github.com/sergiodxa/agent-skills --skill frontend-accessibility-best-practices
SKILL.md
Accessibility Best Practices

Accessibility patterns for building inclusive React applications following WCAG standards. Contains 7 rules across 4 categories focused on semantic HTML, screen reader support, keyboard navigation, and user preferences.

When to Apply

Reference these guidelines when:

Creating new UI components
Building forms and interactive elements
Adding dynamic content or notifications
Implementing navigation patterns
Reviewing code for accessibility
Rules Summary
Semantic HTML & Structure (HIGH)
semantic-html-landmarks - @rules/semantic-html-landmarks.md

Use semantic HTML elements for page structure.

// Bad: divs with class names
<div className="header">...</div>
<div className="nav">...</div>
<div className="content">...</div>

// Good: semantic elements
<header>...</header>
<nav aria-label={t("Primary")}>...</nav>
<main>...</main>
<footer>...</footer>

Screen Readers (MEDIUM)
screen-reader-sr-only - @rules/screen-reader-sr-only.md

Use sr-only class for visually hidden text.

// Icon-only buttons need accessible labels
<Button variant="icon" onPress={onClose}>
  <XMarkIcon aria-hidden="true" />
  <span className="sr-only">{t("Close")}</span>
</Button>

// Visually hidden section headings
<section>
  <h2 className="sr-only">{t("Search results")}</h2>
  <SearchResultsList />
</section>

aria-live-regions - @rules/aria-live-regions.md

Announce dynamic content changes to screen readers.

// Error messages - announced immediately
{
  error && (
    <p role="alert" className="text-failure-600">
      {error}
    </p>
  );
}

// Status updates - announced politely
<div role="status" aria-live="polite">
  {t("{{count}} results found", { count })}
</div>;

Keyboard & Focus (HIGH)
keyboard-navigation - @rules/keyboard-navigation.md

Use semantic elements for built-in keyboard support.

// Bad: div with onClick not keyboard accessible
<div onClick={handleClick}>Click me</div>

// Good: button has Enter/Space support
<button onClick={handleClick}>Click me</button>

// Good: react-aria Button handles everything
import { Button } from "react-aria-components";
<Button onPress={handlePress}>Click me</Button>

focus-management - @rules/focus-management.md

Show visible focus indicators and trap focus in modals.

// Always use focus-visible for focus styles
<button className="focus-visible:ring-2 focus-visible:ring-teal-600">
  Click me
</button>;

// react-aria Modal handles focus trapping automatically
import { Modal, Dialog } from "react-aria-components";
<Modal isOpen={isOpen}>
  <Dialog>{/* Focus automatically trapped here */}</Dialog>
</Modal>;

User Preferences (MEDIUM)
reduced-motion - @rules/reduced-motion.md

Respect prefers-reduced-motion setting.

import { usePrefersReducedMotion } from "~/hooks/use-prefers-reduced-motion";

// CSS approach
<div className="animate-bounce motion-reduce:animate-none">
  Bouncing content
</div>;

// JS approach
function AnimatedCounter({ value }) {
  let prefersReducedMotion = usePrefersReducedMotion();
  if (prefersReducedMotion) return <span>{value}</span>;
  return <CountUp target={value} />;
}

touch-targets - @rules/touch-targets.md

Ensure 44x44px minimum touch targets.

// Icon buttons need explicit sizing
<Button variant="icon" className="h-11 w-11">
  <XMarkIcon className="h-5 w-5" />
  <span className="sr-only">{t("Close")}</span>
</Button>

// Links need padding for tappable area
<Link to={href} className="block py-3 px-4">
  {label}
</Link>

Key Files
app/components/heading.tsx - Region, Heading, Main components
app/hooks/use-prefers-reduced-motion.ts - Reduced motion hook
app/components/field/field.tsx - Accessible form field component
Weekly Installs
325
Repository
sergiodxa/agent-skills
GitHub Stars
83
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass