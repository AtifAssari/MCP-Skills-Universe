---
title: accessibility-audit
url: https://skills.sh/serkan-ozal/browser-devtools-skills/accessibility-audit
---

# accessibility-audit

skills/serkan-ozal/browser-devtools-skills/accessibility-audit
accessibility-audit
Installation
$ npx skills add https://github.com/serkan-ozal/browser-devtools-skills --skill accessibility-audit
SKILL.md
Accessibility Audit Skill

Audit web accessibility using ARIA snapshots, AX tree analysis, and WCAG validation.

When to Use

This skill activates when:

User asks about accessibility or a11y
User mentions WCAG compliance
User wants to check screen reader compatibility
User needs to audit ARIA roles and labels
User asks about keyboard navigation
Capabilities
ARIA Snapshots
browser-devtools-cli a11y take-aria-snapshot
browser-devtools-cli a11y take-aria-snapshot --selector ".main-content"

AX Tree Analysis
browser-devtools-cli --json a11y take-ax-tree-snapshot
browser-devtools-cli --json a11y take-ax-tree-snapshot --roles button,link,textbox
browser-devtools-cli --json a11y take-ax-tree-snapshot --check-occlusion
browser-devtools-cli --json a11y take-ax-tree-snapshot --only-visible

Keyboard Navigation Testing
browser-devtools-cli interaction press-key --key "Tab"
browser-devtools-cli interaction press-key --key "Tab" --selector "body"
browser-devtools-cli interaction press-key --key "Enter"
browser-devtools-cli interaction press-key --key "Escape"

WCAG Checklist
Perceivable
 Images have alt text
 Videos have captions
 Color is not the only indicator
 Text has sufficient contrast
Operable
 All functionality via keyboard
 No keyboard traps
 Skip links present
 Focus visible
Understandable
 Language specified
 Labels on form inputs
 Error messages clear
 Consistent navigation
Robust
 Valid HTML
 ARIA used correctly
 Works with assistive tech
Audit Workflow
SESSION="--session-id a11y-audit"

# 1. Navigate to page
browser-devtools-cli $SESSION navigation go-to --url "https://example.com"
browser-devtools-cli $SESSION sync wait-for-network-idle

# 2. Get ARIA snapshot (quick overview, returns refs e1,e2,...)
browser-devtools-cli $SESSION a11y take-aria-snapshot

# Optional: include custom clickable elements (div/span with cursor:pointer)
browser-devtools-cli $SESSION a11y take-aria-snapshot --cursor-interactive

# 3. Get detailed AX tree
browser-devtools-cli $SESSION --json a11y take-ax-tree-snapshot \
  --roles button,link,textbox,checkbox,radio,combobox

# 4. Check for interactive elements with occlusion
browser-devtools-cli $SESSION --json a11y take-ax-tree-snapshot \
  --roles button,link \
  --check-occlusion

# 5. Test keyboard navigation
browser-devtools-cli $SESSION interaction press-key --key "Tab"
browser-devtools-cli $SESSION content take-screenshot --name "first-focus"

# 6. Cleanup
browser-devtools-cli session delete a11y-audit

Common Issues
Missing Alt Text
# Check images in AX tree
browser-devtools-cli --json a11y take-ax-tree-snapshot --roles image

Missing Form Labels
# Check form elements
browser-devtools-cli --json a11y take-ax-tree-snapshot --roles textbox,checkbox,radio,combobox

Empty Buttons/Links
# Check for buttons and links with no accessible name
browser-devtools-cli --json a11y take-ax-tree-snapshot --roles button,link

Hidden but Focusable Elements
# Check for visibility issues
browser-devtools-cli --json a11y take-ax-tree-snapshot --check-occlusion

Specific Audits
Heading Hierarchy
browser-devtools-cli --json a11y take-ax-tree-snapshot --roles heading

Form Accessibility
browser-devtools-cli --json a11y take-ax-tree-snapshot \
  --roles textbox,checkbox,radio,combobox,button

Navigation Elements
browser-devtools-cli --json a11y take-ax-tree-snapshot \
  --roles navigation,link,menu,menuitem

Interactive Elements
browser-devtools-cli --json a11y take-ax-tree-snapshot \
  --roles button,link,tab,switch,slider

Best Practices
Always use ARIA snapshot first for quick overview
Use AX tree with occlusion check for layout issues
Filter by roles to focus on interactive elements
Check both visible and hidden elements
Test with keyboard only before reporting
Take screenshots to document focus states
Test at different viewport sizes for responsive a11y
Weekly Installs
28
Repository
serkan-ozal/bro…s-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn