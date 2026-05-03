---
rating: ⭐⭐
title: fluxwing library browser
url: https://skills.sh/jackspace/claudeskillz/fluxwing-library-browser
---

# fluxwing library browser

skills/jackspace/claudeskillz/Fluxwing Library Browser
Fluxwing Library Browser
Installation
$ npx skills add https://github.com/jackspace/claudeskillz --skill 'Fluxwing Library Browser'
SKILL.md
Fluxwing Library Browser

Browse all available uxscii components: bundled templates, user-created components, and complete screens.

Data Location Rules

READ from (bundled templates - reference only):

{SKILL_ROOT}/../uxscii-component-creator/templates/ - 11 component templates
{SKILL_ROOT}/../uxscii-screen-scaffolder/templates/ - 2 screen examples (if available)
{SKILL_ROOT}/docs/ - Documentation

READ from (project workspace):

./fluxwing/components/ - Your created components
./fluxwing/screens/ - Your created screens
./fluxwing/library/ - Customized template copies

NEVER write to skill directories - they are read-only!

Your Task

Show the user what uxscii components are available across four sources:

Bundled Templates - 11 curated examples from skill templates (read-only reference)
Project Components - User/agent-created reusable components in ./fluxwing/components/ (editable)
Project Library - Customized template copies in ./fluxwing/library/ (editable)
Project Screens - Complete screen compositions in ./fluxwing/screens/ (editable)

Key Distinction: Bundled templates are READ-ONLY reference materials. To customize them, copy to your project workspace first.

Fast Browsing with Pre-Built Index

IMPORTANT: Use the pre-built template index for instant browsing (10x faster than globbing):

// Load the pre-built index (1 file read = instant results!)
const index = JSON.parse(read('{SKILL_ROOT}/data/template-index.json'));

// Browse by type
const buttons = index.by_type.button; // ["primary-button", "secondary-button"]
const inputs = index.by_type.input; // ["email-input"]

// Search by tag
const formComponents = index.by_tag.form; // All form-related components
const interactiveComponents = index.by_tag.interactive; // All interactive components

// Get component info instantly (no file reads needed!)
const buttonInfo = index.bundled_templates.find(t => t.id === "primary-button");
console.log(buttonInfo.name); // "Primary Button"
console.log(buttonInfo.description); // Full description
console.log(buttonInfo.preview); // ASCII preview already extracted!
console.log(buttonInfo.states); // ["default", "hover", "active", "disabled"]
console.log(buttonInfo.props); // ["text", "variant", "size"]
console.log(buttonInfo.tags); // ["button", "primary", "action", "interactive"]


Performance Benefits:

✅ 1 file read vs 11+ file reads (10x faster!)
✅ Instant type/tag filtering (no parsing needed)
✅ Pre-extracted ASCII previews (show immediately)
✅ Metadata summary (no JSON parsing per component)

Index Structure:

{
  "version": "1.0.0",
  "generated": "2025-10-18T12:00:00Z",
  "template_count": 11,
  "bundled_templates": [ /* array of component metadata */ ],
  "by_type": { /* components grouped by type */ },
  "by_tag": { /* components grouped by tags */ }
}


When to use full file reads:

User requests detailed view of a specific component
User wants to copy a template (need full .uxm and .md content)
User searches for a very specific property not in the index
Display Format

Present in a clear, hierarchical structure:

🎁 BUNDLED TEMPLATES
📁 Component Creator Templates
─────────────────────────────────────────────────────
These are starter templates you can copy and customize.

Buttons (2 variants)
  ├─ primary-button.uxm
  │  └─ Standard clickable button with hover, focus, and disabled states
  │     ▓▓▓▓▓▓▓▓▓▓▓▓
  │     ▓ Click Me ▓
  │     ▓▓▓▓▓▓▓▓▓▓▓▓
  │
  └─ icon-button.uxm
     └─ Button with icon support for visual emphasis
        [🔍 Search]

Inputs (2 variants)
  ├─ text-input.uxm
  │  └─ Basic text input with validation states
  │     [________________]
  │
  └─ email-input.uxm
     └─ Email-specific input with format validation
        [user@example.com  ]

Cards (1 variant)
  └─ card.uxm
     └─ Container for grouping related content
        ╭─────────────╮
        │ Card Title  │
        ├─────────────┤
        │ Content...  │
        ╰─────────────╯

Modals (1 variant)
  └─ modal.uxm
     └─ Overlay dialog for focused interactions
        ╔═══════════════╗
        ║ Modal Title   ║
        ╠═══════════════╣
        ║ Content...    ║
        ╚═══════════════╝

Navigation (1 variant)
  └─ navigation.uxm
     └─ Primary navigation menu
        • Home  • About  • Contact

Feedback (2 variants)
  ├─ alert.uxm
  │  └─ User notification with severity levels
  │     ⚠️ Warning: Action required
  │
  └─ badge.uxm
     └─ Small status indicator or label
        ● New

Lists (1 variant)
  └─ list.uxm
     └─ Vertical list for displaying data
        • Item 1
        • Item 2
        • Item 3

─────────────────────────────────────────────────────

🎨 YOUR COMPONENTS
📁 ./fluxwing/components/
─────────────────────────────────────────────────────
Components you've created for your project.

✓ submit-button.uxm
  └─ Custom submit button for forms
     Modified: 2024-10-11 14:23:00
     [    Submit Form    ]

✓ password-input.uxm
  └─ Password input with show/hide toggle
     Modified: 2024-10-11 14:25:00
     [••••••••] 👁️

✓ user-card.uxm
  └─ Card displaying user profile information
     Modified: 2024-10-11 15:10:00
     ╭──────────────────╮
     │ John Doe         │
     │ @johndoe         │
     ╰──────────────────╯

─────────────────────────────────────────────────────

🖥️ YOUR SCREENS
📁 ./fluxwing/screens/
─────────────────────────────────────────────────────
Complete screen compositions.

✓ login-screen.uxm
  └─ User authentication screen
     Components used: email-input, password-input, submit-button, error-alert
     Modified: 2024-10-11 15:45:00

✓ dashboard.uxm
  └─ Main application dashboard
     Components used: navigation, metric-card, data-table, sidebar
     Modified: 2024-10-11 16:20:00

─────────────────────────────────────────────────────
Total: 10 templates, 3 components, 2 screens

Interactive Options

After displaying the library, offer these actions:

What would you like to do?

1️⃣ View component details (ask me to "show me [name]")
2️⃣ Copy a template to your project
3️⃣ Create a new component (ask me to "create a [type]")
4️⃣ Scaffold a new screen (ask me to "build a [screen type] screen")
5️⃣ Search for a specific pattern (e.g., "button", "input", "card")

Detailed View

If user wants to see details of a specific component:

User: Show me primary-button

You: 📄 PRIMARY-BUTTON.UXM
─────────────────────────────────────────────────────
ID: primary-button
Type: button
Version: 1.0.0
Description: Standard clickable button with hover, focus, and disabled states

Props:
  - text: "Click me"
  - variant: "primary"
  - disabled: false

States:
  - default (solid border, white background)
  - hover (highlighted background)
  - focus (outline indicator)
  - disabled (grayed out)

Accessibility:
  - Role: button
  - Focusable: true
  - Keyboard: Space, Enter

ASCII Preview:

Default State:
▓▓▓▓▓▓▓▓▓▓▓▓
▓ Click Me ▓
▓▓▓▓▓▓▓▓▓▓▓▓

Hover State:
█████████████
█ Click Me █
█████████████

Location: {SKILL_ROOT}/../uxscii-component-creator/templates/primary-button.uxm

To customize: Copy to ./fluxwing/library/ for editing

Copy Template to Project

If user wants to customize a bundled template:

User: Copy primary-button to my project

You: I'll copy primary-button to your library for customization.

[Copies .uxm and .md files]

✓ Copied to ./fluxwing/library/
  - primary-button.uxm
  - primary-button.md

You can now edit these files safely. Changes won't affect the original template.

Next steps:
- Edit: Modify ./fluxwing/library/primary-button.uxm
- Expand: Ask me to "add hover state to primary-button"
- Use: Reference it in screens or other components

Search Functionality

Support component search:

User: Find all button components

You: Found 3 button components:

🎁 Bundled Templates:
  - primary-button.uxm (standard clickable button)
  - icon-button.uxm (button with icon support)

🎨 Your Components:
  - submit-button.uxm (custom submit button for forms)

Would you like details on any of these?

Empty Library Handling

If user has no components yet:

🎁 BUNDLED TEMPLATES
📁 Component Creator Templates
─────────────────────────────────────────────────────
11 starter templates available

🎨 YOUR COMPONENTS
📁 ./fluxwing/components/
─────────────────────────────────────────────────────
No components yet. Create your first component!

Try: "Create a submit button" or "Create an email input"

🖥️ YOUR SCREENS
📁 ./fluxwing/screens/
─────────────────────────────────────────────────────
No screens yet. Scaffold your first screen!

Try: "Build a login screen" or "Create a dashboard"

─────────────────────────────────────────────────────
Total: 11 templates, 0 components, 0 screens

Resources
Examples Guide: See {SKILL_ROOT}/docs/07-examples-guide.md for detailed template documentation
Component Creator: Use when you want to create new components
Screen Scaffolder: Use when you want to build complete screens
Component Viewer: Use for detailed component information
Important Notes
Read-only templates: Bundled templates cannot be modified directly
Copy before customize: Copy templates to ./fluxwing/library/ to customize
Search: Use Glob and Grep to find components by name or pattern
Organization: Keep components in ./fluxwing/components/, customized templates in ./fluxwing/library/
Screens: Screen files include .uxm, .md, and .rendered.md (three files)

You're helping users discover and navigate their uxscii component library!

Weekly Installs
–
Repository
jackspace/claudeskillz
GitHub Stars
14
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass