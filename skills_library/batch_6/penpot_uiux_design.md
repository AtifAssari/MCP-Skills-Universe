---
title: penpot-uiux-design
url: https://skills.sh/github/awesome-copilot/penpot-uiux-design
---

# penpot-uiux-design

skills/github/awesome-copilot/penpot-uiux-design
penpot-uiux-design
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill penpot-uiux-design
Summary

Professional UI/UX design creation in Penpot with MCP tools, design systems, and accessibility standards.

Four MCP tools enable design creation, modification, export, and API access within Penpot's plugin context
Includes discovery workflow to identify existing design systems, components, and tokens before building new designs
Covers responsive layouts for mobile (375×812), desktop (1440×900), and platform-specific guidelines (iOS, Android, Material Design)
Provides default design tokens (spacing scale, typography, colors) and component patterns (buttons, forms, navigation) when no design system exists
Built-in accessibility validation, visual hierarchy principles, and design review checklist for WCAG compliance and usability
SKILL.md
Penpot UI/UX Design Guide

Create professional, user-centered designs in Penpot using the penpot/penpot-mcp MCP server and proven UI/UX principles.

Available MCP Tools
Tool	Purpose
mcp__penpot__execute_code	Run JavaScript in Penpot plugin context to create/modify designs
mcp__penpot__export_shape	Export shapes as PNG/SVG for visual inspection
mcp__penpot__import_image	Import images (icons, photos, logos) into designs
mcp__penpot__penpot_api_info	Retrieve Penpot API documentation
MCP Server Setup

The Penpot MCP tools require the penpot/penpot-mcp server running locally. For detailed installation and troubleshooting, see setup-troubleshooting.md.

Before Setup: Check If Already Running

Always check if the MCP server is already available before attempting setup:

Try calling a tool first: Attempt mcp__penpot__penpot_api_info - if it succeeds, the server is running and connected. No setup needed.

If the tool fails, ask the user:

"The Penpot MCP server doesn't appear to be connected. Is the server already installed and running? If so, I can help troubleshoot. If not, I can guide you through the setup."

Only proceed with setup instructions if the user confirms the server is not installed.

Quick Start (Only If Not Installed)
# Clone and install
git clone https://github.com/penpot/penpot-mcp.git
cd penpot-mcp
npm install

# Build and start servers
npm run bootstrap


Then in Penpot:

Open a design file
Go to Plugins → Load plugin from URL
Enter: http://localhost:4400/manifest.json
Click "Connect to MCP server" in the plugin UI
VS Code Configuration

Add to settings.json:

{
  "mcp": {
    "servers": {
      "penpot": {
        "url": "http://localhost:4401/sse"
      }
    }
  }
}

Troubleshooting (If Server Is Installed But Not Working)
Issue	Solution
Plugin won't connect	Check servers are running (npm run start:all in penpot-mcp dir)
Browser blocks localhost	Allow local network access prompt, or disable Brave Shield, or try Firefox
Tools not appearing in client	Restart VS Code/Claude completely after config changes
Tool execution fails/times out	Ensure Penpot plugin UI is open and shows "Connected"
"WebSocket connection failed"	Check firewall allows ports 4400, 4401, 4402
Quick Reference
Task	Reference File
MCP server installation & troubleshooting	setup-troubleshooting.md
Component specs (buttons, forms, nav)	component-patterns.md
Accessibility (contrast, touch targets)	accessibility.md
Screen sizes & platform specs	platform-guidelines.md
Core Design Principles
The Golden Rules
Clarity over cleverness: Every element must have a purpose
Consistency builds trust: Reuse patterns, colors, and components
User goals first: Design for tasks, not features
Accessibility is not optional: Design for everyone
Test with real users: Validate assumptions early
Visual Hierarchy (Priority Order)
Size: Larger = more important
Color/Contrast: High contrast draws attention
Position: Top-left (LTR) gets seen first
Whitespace: Isolation emphasizes importance
Typography weight: Bold stands out
Design Workflow
Check for design system first: Ask user if they have existing tokens/specs, or discover from current Penpot file
Understand the page: Call mcp__penpot__execute_code with penpotUtils.shapeStructure() to see hierarchy
Find elements: Use penpotUtils.findShapes() to locate elements by type or name
Create/modify: Use penpot.createBoard(), penpot.createRectangle(), penpot.createText() etc.
Apply layout: Use addFlexLayout() for responsive containers
Validate: Call mcp__penpot__export_shape to visually check your work
Design System Handling

Before creating designs, determine if the user has an existing design system:

Ask the user: "Do you have a design system or brand guidelines to follow?"
Discover from Penpot: Check for existing components, colors, and patterns
// Discover existing design patterns in current file
const allShapes = penpotUtils.findShapes(() => true, penpot.root);

// Find existing colors in use
const colors = new Set();
allShapes.forEach(s => {
  if (s.fills) s.fills.forEach(f => colors.add(f.fillColor));
});

// Find existing text styles (font sizes, weights)
const textStyles = allShapes
  .filter(s => s.type === 'text')
  .map(s => ({ fontSize: s.fontSize, fontWeight: s.fontWeight }));

// Find existing components
const components = penpot.library.local.components;

return { colors: [...colors], textStyles, componentCount: components.length };


If user HAS a design system:

Use their specified colors, spacing, typography
Match their existing component patterns
Follow their naming conventions

If user has NO design system:

Use the default tokens below as a starting point
Offer to help establish consistent patterns
Reference specs in component-patterns.md
Key Penpot API Gotchas
width/height are READ-ONLY → use shape.resize(w, h)
parentX/parentY are READ-ONLY → use penpotUtils.setParentXY(shape, x, y)
Use insertChild(index, shape) for z-ordering (not appendChild)
Flex children array order is REVERSED for dir="column" or dir="row"
After text.resize(), reset growType to "auto-width" or "auto-height"
Positioning New Boards

Always check existing boards before creating new ones to avoid overlap:

// Find all existing boards and calculate next position
const boards = penpotUtils.findShapes(s => s.type === 'board', penpot.root);
let nextX = 0;
const gap = 100; // Space between boards

if (boards.length > 0) {
  // Find rightmost board edge
  boards.forEach(b => {
    const rightEdge = b.x + b.width;
    if (rightEdge + gap > nextX) {
      nextX = rightEdge + gap;
    }
  });
}

// Create new board at calculated position
const newBoard = penpot.createBoard();
newBoard.x = nextX;
newBoard.y = 0;
newBoard.resize(375, 812);


Board spacing guidelines:

Use 100px gap between related screens (same flow)
Use 200px+ gap between different sections/flows
Align boards vertically (same y) for visual organization
Group related screens horizontally in user flow order
Default Design Tokens

Use these defaults only when user has no design system. Always prefer user's tokens if available.

Spacing Scale (8px base)
Token	Value	Usage
spacing-xs	4px	Tight inline elements
spacing-sm	8px	Related elements
spacing-md	16px	Default padding
spacing-lg	24px	Section spacing
spacing-xl	32px	Major sections
spacing-2xl	48px	Page-level spacing
Typography Scale
Level	Size	Weight	Usage
Display	48-64px	Bold	Hero headlines
H1	32-40px	Bold	Page titles
H2	24-28px	Semibold	Section headers
H3	20-22px	Semibold	Subsections
Body	16px	Regular	Main content
Small	14px	Regular	Secondary text
Caption	12px	Regular	Labels, hints
Color Usage
Purpose	Recommendation
Primary	Main brand color, CTAs
Secondary	Supporting actions
Success	#22C55E range (confirmations)
Warning	#F59E0B range (caution)
Error	#EF4444 range (errors)
Neutral	Gray scale for text/borders
Common Layouts
Mobile Screen (375×812)
┌─────────────────────────────┐
│ Status Bar (44px)           │
├─────────────────────────────┤
│ Header/Nav (56px)           │
├─────────────────────────────┤
│                             │
│ Content Area                │
│ (Scrollable)                │
│ Padding: 16px horizontal    │
│                             │
├─────────────────────────────┤
│ Bottom Nav/CTA (84px)       │
└─────────────────────────────┘


Desktop Dashboard (1440×900)
┌──────┬──────────────────────────────────┐
│      │ Header (64px)                    │
│ Side │──────────────────────────────────│
│ bar  │ Page Title + Actions             │
│      │──────────────────────────────────│
│ 240  │ Content Grid                     │
│ px   │ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ │
│      │ │Card │ │Card │ │Card │ │Card │ │
│      │ └─────┘ └─────┘ └─────┘ └─────┘ │
│      │                                  │
└──────┴──────────────────────────────────┘


Component Checklist
Buttons
 Clear, action-oriented label (2-3 words)
 Minimum touch target: 44×44px
 Visual states: default, hover, active, disabled, loading
 Sufficient contrast (3:1 against background)
 Consistent border radius across app
Forms
 Labels above inputs (not just placeholders)
 Required field indicators
 Error messages adjacent to fields
 Logical tab order
 Input types match content (email, tel, etc.)
Navigation
 Current location clearly indicated
 Consistent position across screens
 Maximum 7±2 top-level items
 Touch-friendly on mobile (48px targets)
Accessibility Quick Checks
Color contrast: Text 4.5:1, Large text 3:1
Touch targets: Minimum 44×44px
Focus states: Visible keyboard focus indicators
Alt text: Meaningful descriptions for images
Hierarchy: Proper heading levels (H1→H2→H3)
Color independence: Never rely solely on color
Design Review Checklist

Before finalizing any design:

 Visual hierarchy is clear
 Consistent spacing and alignment
 Typography is readable (16px+ body text)
 Color contrast meets WCAG AA
 Interactive elements are obvious
 Mobile-friendly touch targets
 Loading/empty/error states considered
 Consistent with design system
Validating Designs

Use these validation approaches with mcp__penpot__execute_code:

Check	Method
Elements outside bounds	penpotUtils.analyzeDescendants() with isContainedIn()
Text too small (<12px)	penpotUtils.findShapes() filtering by fontSize
Missing contrast	Call mcp__penpot__export_shape and visually inspect
Hierarchy structure	penpotUtils.shapeStructure() to review nesting
Export CSS

Use penpot.generateStyle(selection, { type: 'css', includeChildren: true }) via mcp__penpot__execute_code to extract CSS from designs.

Tips for Great Designs
Start with content: Real content reveals layout needs
Design mobile-first: Constraints breed creativity
Use a grid: 8px base grid keeps things aligned
Limit colors: 1 primary + 1 secondary + neutrals
Limit fonts: 1-2 typefaces maximum
Embrace whitespace: Breathing room improves comprehension
Be consistent: Same action = same appearance everywhere
Provide feedback: Every action needs a response
Weekly Installs
9.9K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass