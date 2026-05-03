---
title: wcag-audit-operable-keyboard-focus
url: https://skills.sh/jkense/agent-skills-wcag/wcag-audit-operable-keyboard-focus
---

# wcag-audit-operable-keyboard-focus

skills/jkense/agent-skills-wcag/wcag-audit-operable-keyboard-focus
wcag-audit-operable-keyboard-focus
Installation
$ npx skills add https://github.com/jkense/agent-skills-wcag --skill wcag-audit-operable-keyboard-focus
SKILL.md
When to Use

Use this tool when designing keyboard navigation flows, testing tab order, or ensuring logical focus progression through interactive elements.

Usage
Command Line
node scripts/validate.js --elements "header, nav, main, button, button, footer"
node scripts/validate.js --tab-order "1,2,3,4,5" --expected "1,2,3,4,5"
node scripts/validate.js --json '{"elements": ["header", "nav", "main", "button#submit"], "tabOrder": [1,2,3,4]}'

JSON Input
node scripts/validate.js --json '{
  "elements": ["header", "nav", "button#menu", "main", "button#submit", "footer"],
  "tabOrder": [1, 2, 3, 4, 5, 6],
  "expectedOrder": [1, 2, 4, 5, 3, 6]
}'

Parameters
--elements: Comma-separated list of element identifiers
--tab-order: Comma-separated list of tab order indices
--expected: Expected logical order (optional)
--json: JSON input with elements and tab order properties
Output

Returns JSON with validation results and issues:

{
  "elements": ["header", "nav", "main", "button", "footer"],
  "tabOrder": [1, 2, 3, 4, 5],
  "validation": {
    "logical": true,
    "complete": true,
    "issues": []
  },
  "recommendations": [
    "Consider moving primary action button before secondary navigation"
  ]
}

Examples
Validate simple tab order
$ node scripts/validate.js --elements "header, nav, main, button, footer" --tab-order "1,2,3,4,5"
✅ Logical order: PASS
✅ Complete coverage: PASS
✅ No focus traps: PASS
Focus order follows logical reading sequence

Detect focus order issues
$ node scripts/validate.js --elements "header, nav, button, main, footer" --tab-order "1,2,4,3,5"
❌ Logical order: FAIL
⚠️  Tab order issue: "main" (position 3) appears before "button" (position 4)
Recommendations:
- Move main content before secondary buttons
- Consider semantic HTML structure for better default tab order

WCAG Standards
Logical Order: Focus order should follow logical reading sequence
No Traps: Users should not get trapped in focus loops
Complete Coverage: All interactive elements should be keyboard accessible
Skip Links: Provide mechanisms to skip repeated navigation sections
Modal Focus: Modal dialogs should manage focus appropriately
Best Practices
Follow reading order: Tab order should match visual reading sequence
Use semantic HTML: Proper heading hierarchy and landmarks improve default tab order
Provide skip links: Allow users to skip navigation sections
Test with keyboard: Verify all interactions work without mouse
Avoid focus traps: Ensure users can always move forward and backward
Focus Order Patterns
Good Order:
Header/Skip links
Main navigation
Main content
Footer links
Footer
Problematic Order:
Header
Footer links
Main navigation
Main content
Learn More

For more information about Agent Skills and how they extend AI capabilities.

Weekly Installs
11
Repository
jkense/agent-skills-wcag
GitHub Stars
1
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass