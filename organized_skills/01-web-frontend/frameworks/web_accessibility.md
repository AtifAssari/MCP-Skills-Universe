---
rating: ⭐⭐⭐⭐⭐
title: web-accessibility
url: https://skills.sh/89jobrien/steve/web-accessibility
---

# web-accessibility

skills/89jobrien/steve/web-accessibility
web-accessibility
Installation
$ npx skills add https://github.com/89jobrien/steve --skill web-accessibility
SKILL.md
Web Accessibility

This skill provides comprehensive web accessibility analysis and remediation, focusing on WCAG compliance, screen reader compatibility, and inclusive design.

When to Use This Skill
When conducting WCAG compliance audits
When testing screen reader compatibility
When validating keyboard navigation
When analyzing color contrast
When ensuring inclusive design
When remediating accessibility issues
What This Skill Does
WCAG Compliance: Assesses compliance with WCAG 2.1/2.2 (A, AA, AAA)
Screen Reader Testing: Validates semantic HTML and ARIA usage
Keyboard Navigation: Tests keyboard accessibility and focus management
Color Contrast: Analyzes color contrast ratios
Alternative Text: Evaluates alt text and media accessibility
Form Accessibility: Validates form labels and error handling
How to Use
Audit Accessibility
Conduct a WCAG compliance audit of this website

Test keyboard navigation and screen reader compatibility

Specific Analysis
Check color contrast ratios and suggest improvements

WCAG Standards
Level A (Minimum)
Text alternatives for images
Captions for videos
Keyboard accessible
No seizure-inducing content
Proper heading structure
Level AA (Recommended)
Color contrast ratio 4.5:1 (text)
Resizable text up to 200%
Multiple navigation methods
Consistent navigation
Error identification
Level AAA (Enhanced)
Color contrast ratio 7:1 (text)
Sign language interpretation
Extended audio descriptions
No timing restrictions
Context-sensitive help
Examples
Example 1: WCAG Audit

Input: Audit homepage for WCAG compliance

Output:

## Accessibility Audit: Homepage

### Critical Issues (Level A)

**1. Missing Alt Text**
- **Location**: Hero image (line 45)
- **Issue**: Image has no alt attribute
- **Fix**: Add descriptive alt text
```html
<!-- Before -->
<img src="hero.jpg">

<!-- After -->
<img src="hero.jpg" alt="Team collaborating on project management dashboard">


2. Missing Form Labels

Location: Email input (line 78)
Issue: Input has no associated label
Fix: Add proper label
<!-- Before -->
<input type="email" id="email">

<!-- After -->
<label for="email">Email Address</label>
<input type="email" id="email" aria-required="true">

Warnings (Level AA)

3. Color Contrast

Location: Button text (line 92)
Issue: Contrast ratio 3.2:1 (needs 4.5:1)
Fix: Darken text color

## Best Practices

### Accessibility Guidelines

1. **Semantic HTML**: Use proper HTML elements
2. **ARIA When Needed**: Use ARIA for complex interactions
3. **Keyboard Access**: Ensure all functionality is keyboard accessible
4. **Color Contrast**: Meet WCAG contrast requirements
5. **Testing**: Test with screen readers and keyboard only

## Related Use Cases

- WCAG compliance audits
- Screen reader testing
- Keyboard navigation validation
- Color contrast analysis
- Inclusive design implementation

Weekly Installs
25
Repository
89jobrien/steve
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass