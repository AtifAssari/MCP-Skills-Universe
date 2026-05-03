---
rating: ⭐⭐
title: chrome-extension-ui
url: https://skills.sh/pproenca/dot-skills/chrome-extension-ui
---

# chrome-extension-ui

skills/pproenca/dot-skills/chrome-extension-ui
chrome-extension-ui
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill chrome-extension-ui
SKILL.md
Chrome Extensions UX/UI Best Practices

Comprehensive UX/UI design guide for Chrome Extensions, optimized for Manifest V3. Contains 42 rules across 8 categories, prioritized by impact to guide extension UI development and code review.

When to Apply

Reference these guidelines when:

Building new Chrome extension user interfaces
Choosing between popup, side panel, or content script UI
Implementing accessible, keyboard-navigable interfaces
Designing loading states, error handling, and feedback patterns
Creating options pages and settings persistence
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Component Selection	CRITICAL	comp-
2	Accessibility & Navigation	CRITICAL	access-
3	Popup Design	HIGH	popup-
4	Side Panel UX	HIGH	panel-
5	Content Script UI	MEDIUM-HIGH	inject-
6	Visual Feedback	MEDIUM	feedback-
7	Options & Settings	MEDIUM	options-
8	Icons & Branding	LOW-MEDIUM	brand-
Quick Reference
1. Component Selection (CRITICAL)
comp-popup-vs-sidepanel - Choose Side Panel for Persistent Tasks
comp-content-script-ui - Use Content Scripts for In-Page UI
comp-single-purpose - Design for Single Purpose
comp-minimal-permissions - Request Minimal Permissions
comp-action-tooltip - Provide Descriptive Action Tooltips
2. Accessibility & Navigation (CRITICAL)
access-keyboard-navigation - Enable Complete Keyboard Navigation
access-focus-visible - Maintain Visible Focus Indicators
access-aria-labels - Use ARIA Labels for Icon-Only Buttons
access-color-contrast - Ensure Sufficient Color Contrast
access-focus-trap - Avoid Keyboard Focus Traps
access-semantic-html - Use Semantic HTML Elements
3. Popup Design (HIGH)
popup-size-constraints - Design Within Popup Size Limits
popup-instant-render - Render Popup Content Instantly
popup-primary-action - Make the Primary Action Obvious
popup-auto-close - Handle Popup Auto-Close Gracefully
popup-external-js - Keep JavaScript in External Files
popup-dynamic-switch - Use Dynamic Popups for State-Based UI
4. Side Panel UX (HIGH)
panel-non-distracting - Design Non-Distracting Side Panels
panel-tab-vs-window - Choose Tab-Specific vs Window-Wide Panels
panel-responsive-width - Design for Variable Panel Widths
panel-page-context - Sync Panel Content with Page Context
panel-lazy-sections - Lazy Load Panel Sections
5. Content Script UI (MEDIUM-HIGH)
inject-shadow-dom - Use Shadow DOM for Style Isolation
inject-z-index - Use Maximum Z-Index for Overlays
inject-document-ready - Inject UI After DOM Ready
inject-unique-ids - Use Unique IDs to Prevent Conflicts
inject-cleanup - Clean Up Injected Elements on Removal
6. Visual Feedback (MEDIUM)
feedback-loading-states - Show Loading States for Async Operations
feedback-error-messages - Write Actionable Error Messages
feedback-badge-status - Use Badge for At-a-Glance Status
feedback-success-confirmation - Confirm Successful Actions
feedback-notifications - Use Notifications Sparingly
feedback-progress-indication - Show Progress for Long Operations
7. Options & Settings (MEDIUM)
options-embedded-page - Use Embedded Options for Simple Settings
options-sync-storage - Sync Settings Across Devices
options-auto-save - Auto-Save Settings on Change
options-sensible-defaults - Provide Sensible Default Settings
8. Icons & Branding (LOW-MEDIUM)
brand-icon-sizes - Provide All Required Icon Sizes
brand-distinctive-icon - Design a Distinctive Toolbar Icon
brand-badge-text - Keep Badge Text Under 4 Characters
brand-consistent-styling - Maintain Consistent Visual Style
brand-web-store-assets - Create Quality Web Store Assets
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
380
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn