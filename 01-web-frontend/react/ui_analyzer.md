---
title: ui-analyzer
url: https://skills.sh/smallnest/langgraphgo/ui-analyzer
---

# ui-analyzer

skills/smallnest/langgraphgo/ui-analyzer
ui-analyzer
Installation
$ npx skills add https://github.com/smallnest/langgraphgo --skill ui-analyzer
SKILL.md
UI Analyzer

This skill provides a systematic approach to analyzing UI design screenshots and translating them into production-ready React components using TypeScript and Tailwind CSS.

Purpose

Transform UI design screenshots into well-structured, accessible, and maintainable React components. The skill guides through analyzing layouts, extracting design tokens, identifying components, and generating clean code that matches the design while following best practices.

When to Use This Skill

Use this skill when:

The user provides a UI design screenshot, mockup, or Figma export
The user requests "implement this design" or "build this UI"
The user asks to "analyze this screenshot"
The user wants to convert a design to code
The user needs help understanding a UI's structure
The user requests matching an existing design
Analysis Workflow

Follow these steps systematically when analyzing a UI screenshot:

Step 1: Initial Observation and Screenshot Reading

Read the provided screenshot first using the Read tool if a file path is provided, or if the user has shared an image in the conversation.

After viewing the screenshot:

Describe what you see in the UI
Identify the screen/page type (login, dashboard, form, etc.)
Determine the target device (desktop, mobile, responsive)
Note the overall aesthetic (modern, minimal, colorful, etc.)
Confirm understanding with the user before proceeding
Step 2: Layout Analysis

Identify the high-level layout structure:

Main layout type - Consult references/layout-patterns.md to identify:

Single column
Sidebar layout
Header + content
Grid layout
Split screen
Dashboard
Master-detail
Other patterns

Layout hierarchy - Break down into sections:

Header/navigation
Main content area
Sidebar (if present)
Footer (if present)
Nested structures

Responsive considerations:

How should layout adapt to mobile?
Which elements stack or hide?
Breakpoint strategy

Reference references/layout-patterns.md for Tailwind implementation patterns.

Step 3: Component Identification

Systematically identify all UI components using references/ui-analysis-checklist.md:

Navigation Components:

Top nav, sidebar nav, breadcrumbs, tabs, etc.

Data Display Components:

Cards, tables, lists, stats, badges, avatars, icons, etc.

Input Components:

Text inputs, selects, checkboxes, radios, switches, date pickers, etc.

Action Components:

Buttons (primary, secondary, etc.), icon buttons, links, etc.

Feedback Components:

Alerts, toasts, progress bars, loading states, etc.

Overlay Components:

Modals, drawers, tooltips, popovers, dropdowns, etc.

List all identified components with:

Component type and purpose
Location in the layout
Approximate size and styling
Interactive states (if visible)
Step 4: Design Token Extraction

Extract design system values using references/design-tokens.md:

Color Palette:

Identify all unique colors in the design
Categorize by usage:
Primary brand color
Secondary/accent colors
Background colors (main, secondary)
Text colors (primary, secondary, muted)
Border colors
State colors (success, warning, error, info)
Map each color to nearest Tailwind color or note custom color needed
Create a color reference table

Typography:

Identify font family (serif, sans-serif, monospace)
List all text sizes observed
Map to Tailwind typography scale (text-xs to text-6xl)
Note font weights used (normal, medium, semibold, bold)
Identify heading hierarchy (H1-H6)

Spacing:

Observe padding patterns (card padding, button padding, etc.)
Observe margin/gap patterns (between sections, between items)
Map to Tailwind spacing scale (p-4, m-6, gap-8, etc.)
Note the spacing unit (usually 4px or 8px base)

Other Tokens:

Border radius (rounded-none to rounded-full)
Shadows (shadow-sm to shadow-2xl)
Border widths
Icon sizes

Reference references/design-tokens.md for complete mapping tables.

Step 5: Detailed Component Analysis

For each major component identified:

Component boundaries - Where does it start/end?
Props/data - What data does it receive?
Internal structure - Sub-components and elements
Styling details:
Background color
Text color and size
Padding and margins
Border and radius
Shadow
Interactive states (if visible or inferable):
Hover
Active/pressed
Focused
Disabled
Loading
Error
Accessibility needs:
ARIA labels
Semantic HTML
Keyboard navigation
Step 6: Implementation Strategy

Plan the implementation approach:

Component hierarchy - Which components to build first?
Reusability - Which patterns repeat? Extract to reusable components
State management - Does any component need Zustand or just local state?
Integration with react-component-generator - Can existing templates be used?
File structure - Where should components live?

If the react-component-generator skill is available:

Reference its templates for common components (forms, cards, buttons, modals, etc.)
Use its best practices for component structure
Follow its naming conventions
Step 7: Code Generation

Generate React components following these principles:

Structure:

Start with TypeScript interfaces for props
Use functional components with React.FC
Include JSDoc comments
Export both named and default exports

Styling:

Use Tailwind CSS exclusively for styling
Apply extracted design tokens
Organize classes logically (layout → spacing → colors → effects → states)
Use responsive classes where needed (sm:, md:, lg:, xl:)

Best Practices:

Use semantic HTML elements
Include ARIA attributes for accessibility
Handle loading and error states
Support keyboard navigation
Use proper TypeScript types (no any)
Keep components focused and composable

Example Component Template:

import React from 'react';

interface ComponentNameProps {
  // Props based on analysis
  title: string;
  description?: string;
  onClick?: () => void;
  className?: string;
}

/**
 * ComponentName - Brief description based on UI purpose
 *
 * @param props - Component props
 * @returns JSX.Element
 */
export const ComponentName: React.FC<ComponentNameProps> = ({
  title,
  description,
  onClick,
  className = ''
}) => {
  return (
    <div className={`/* Tailwind classes from design */ ${className}`}>
      {/* Implementation based on screenshot */}
    </div>
  );
};

export default ComponentName;

Step 8: Verification and Refinement

After generating code:

Review against screenshot - Does it match the design?
Check responsiveness - Will it work on different screen sizes?
Verify accessibility - Are ARIA labels and semantic HTML present?
Validate design tokens - Are colors, spacing, typography correct?
Consider edge cases - Long text, empty states, loading states
Note assumptions - Clearly state what was assumed vs confirmed
Step 9: Deliverables

Provide the user with:

Analysis Summary:

Layout description
Component breakdown
Design tokens extracted

Generated Code:

Complete React component(s)
TypeScript interfaces
Tailwind classes applied

Implementation Notes:

Installation requirements (if any packages needed)
Usage examples
Customization suggestions
Responsive behavior notes

Next Steps:

Suggest improvements or variations
Note areas that might need refinement
Offer to generate additional related components
Common Scenarios
Scenario 1: Simple Form Screenshot

User: "Implement this login form design [screenshot]"

Approach:

Read screenshot
Identify: Centered card layout with form inputs and button
Extract: Colors, input styling, button styling, spacing
Reference layout-patterns.md → "Centered Modal/Card" pattern
Reference react-component-generator → FormComponent template
Generate: LoginForm.tsx with proper validation structure
Apply Tailwind classes matching the design
Scenario 2: Dashboard Screenshot

User: "Build this dashboard UI [screenshot]"

Approach:

Read screenshot
Identify: Header + sidebar layout with grid of stat cards
Break down into components:
Header component
Sidebar navigation
StatCard component (repeated)
Main dashboard layout
Extract design tokens for consistency
Reference layout-patterns.md → "Dashboard Layout" pattern
Generate components starting with reusable StatCard
Compose into main Dashboard component
Scenario 3: Complex Page with Multiple Sections

User: "Implement this landing page [screenshot]"

Approach:

Read screenshot
Identify sections: Hero, features grid, testimonials, CTA
Analyze each section separately using checklist
Extract shared design tokens
Generate section components one by one
Show how sections compose into the full page
Provide responsive behavior notes
Scenario 4: Component Library Screenshot

User: "Create components from this design system screenshot [screenshot]"

Approach:

Read screenshot
Identify: Multiple variations of buttons, inputs, cards shown
Extract design tokens for the system
Generate each component variant
Document the prop variations
Create a usage guide
Suggest how to organize in the project
Reference Files Usage
references/ui-analysis-checklist.md
When to use: During Step 3 (Component Identification) and as a comprehensive analysis guide
Purpose: Ensures no components or details are missed
How: Work through checklist sections systematically
references/layout-patterns.md
When to use: During Step 2 (Layout Analysis) and Step 7 (Code Generation)
Purpose: Quickly identify common patterns and get implementation code
How: Match observed layout to pattern, adapt provided code
references/design-tokens.md
When to use: During Step 4 (Design Token Extraction) and Step 7 (Code Generation)
Purpose: Map visual elements to Tailwind classes accurately
How: Use color tables, spacing scale, and component size guides
Tips for Accurate Analysis
Be systematic - Follow the workflow steps in order, don't skip ahead
Take measurements - Estimate sizes and spacing carefully
Look for patterns - Repeated elements indicate design system consistency
Note uncertainties - Clearly mark assumptions vs confirmed details
Think responsive - Always consider mobile behavior
Prioritize accessibility - Include ARIA labels and semantic HTML from the start
Stay DRY - Extract reusable components when patterns repeat
Consult references - Use the reference files liberally for accuracy
Verify with user - Confirm understanding before extensive code generation
Iterate - Expect refinement based on user feedback
Integration with Other Skills
With react-component-generator skill

When both skills are available:

Use ui-analyzer to understand the design and extract requirements
Reference react-component-generator templates for similar components
Apply ui-analyzer's extracted design tokens to the templates
Follow react-component-generator's naming and structure conventions

This creates a powerful workflow: analyze → identify template → customize → implement.

Example Full Workflow

User provides login page screenshot

✅ Read screenshot and describe the UI
✅ Identify: Centered card layout, split-screen with image
✅ Extract design tokens:
Primary blue: #3B82F6 → bg-blue-500
Text: #1F2937 → text-gray-800
Background: #F9FAFB → bg-gray-50
Card padding: ~32px → p-8
Input height: ~40px → h-10
Button: blue background, white text, rounded-md
✅ Identify components:
Logo/brand element
Heading and subheading
Email input (with label)
Password input (with label, show/hide icon)
"Remember me" checkbox
"Forgot password?" link
Submit button
Sign up link at bottom
✅ Reference layout-patterns.md → Split Screen + Centered Card patterns
✅ Generate LoginForm.tsx:
TypeScript interfaces for props
Form validation structure
Tailwind classes matching design
Accessibility attributes
Responsive behavior (stacked on mobile)
✅ Provide usage example and notes
✅ Offer to generate the accompanying image section or adjust styling
Notes
Always read the screenshot first before any analysis
Prioritize user confirmation of understanding before extensive code generation
When in doubt about colors or spacing, choose the closest Tailwind default
Document all assumptions clearly
Provide complete, runnable code, not pseudocode
Consider suggesting improvements while matching the design
Be prepared to iterate based on user feedback
Weekly Installs
48
Repository
smallnest/langgraphgo
GitHub Stars
240
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass