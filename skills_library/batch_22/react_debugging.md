---
title: react-debugging
url: https://skills.sh/serkan-ozal/browser-devtools-skills/react-debugging
---

# react-debugging

skills/serkan-ozal/browser-devtools-skills/react-debugging
react-debugging
Installation
$ npx skills add https://github.com/serkan-ozal/browser-devtools-skills --skill react-debugging
SKILL.md
React Debugging Skill

Debug React applications by inspecting components, props, and the component tree.

When to Use

This skill activates when:

User is debugging a React application
User wants to inspect React component props/state
User needs to find which component renders an element
User asks about React DevTools
User mentions React Fiber or component tree
Capabilities
Component Inspection
browser-devtools-cli react get-component-for-element --selector ".user-card"
browser-devtools-cli --json react get-component-for-element --selector "#root > div"

Element Mapping
browser-devtools-cli react get-element-for-component --component-name "UserCard"
browser-devtools-cli --json react get-element-for-component --component-name "Button"

Prerequisites

Important: React tools work best with:

Persistent Browser Context: Enable BROWSER_PERSISTENT_ENABLE=true
React DevTools Extension: Manually install in browser profile
Chrome Web Store

Without the extension, tools use best-effort DOM scanning which is less reliable.

Debugging Workflow
Find Component for Element
SESSION="--session-id react-debug"

# Navigate to React app
browser-devtools-cli $SESSION navigation go-to --url "http://localhost:3000"
browser-devtools-cli $SESSION sync wait-for-network-idle

# Find component for a DOM element
browser-devtools-cli $SESSION --json react get-component-for-element \
  --selector ".user-profile-card"

# Cleanup
browser-devtools-cli session delete react-debug

Find Elements for Component
SESSION="--session-id react-debug"

# Navigate to React app
browser-devtools-cli $SESSION navigation go-to --url "http://localhost:3000"
browser-devtools-cli $SESSION sync wait-for-network-idle

# Find all DOM elements rendered by a component
browser-devtools-cli $SESSION --json react get-element-for-component \
  --component-name "UserCard"

# Cleanup
browser-devtools-cli session delete react-debug

Common Use Cases
Debugging Props Issues
# Find component and check its props
browser-devtools-cli --json react get-component-for-element --selector ".broken-component"

Understanding Render Boundaries
# See what DOM elements a component renders
browser-devtools-cli --json react get-element-for-component --component-name "DataTable"

Identifying Component Names
# Click on an element to find its component name
browser-devtools-cli --json react get-component-for-element --selector "#unknown-element"

Combined with DOM Inspection
SESSION="--session-id react-debug"

# Get component info
browser-devtools-cli $SESSION --json react get-component-for-element --selector ".card"

# Also check DOM structure
browser-devtools-cli $SESSION content get-as-html --selector ".card"

# And accessibility
browser-devtools-cli $SESSION a11y take-aria-snapshot --selector ".card"

Combined with Console Inspection
SESSION="--session-id react-debug"

# Check for React errors in console
browser-devtools-cli $SESSION --json o11y get-console-messages --type warning

# Look for component info
browser-devtools-cli $SESSION --json react get-component-for-element --selector ".error-boundary"

Limitations
Development builds only: Best results with React dev mode
Component names: May be minified in production
Source info: Best-effort, depends on source maps
State access: Limited without DevTools extension
Best Practices
Use persistent context for React DevTools extension
Install extension manually in browser profile
Test in development mode for better component names
Combine with DOM inspection for full picture
Use console inspection for runtime state
Check for React warnings in console messages
Weekly Installs
42
Repository
serkan-ozal/bro…s-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass