---
rating: ⭐⭐⭐
title: ui-design-system
url: https://skills.sh/alirezarezvani/claude-skills/ui-design-system
---

# ui-design-system

skills/alirezarezvani/claude-skills/ui-design-system
ui-design-system
Installation
$ npx skills add https://github.com/alirezarezvani/claude-skills --skill ui-design-system
SKILL.md
UI Design System

Generate design tokens, create color palettes, calculate typography scales, build component systems, and prepare developer handoff documentation.

Table of Contents
Trigger Terms
Workflows
Workflow 1: Generate Design Tokens
Workflow 2: Create Component System
Workflow 3: Responsive Design
Workflow 4: Developer Handoff
Tool Reference
Quick Reference Tables
Knowledge Base
Trigger Terms

Use this skill when you need to:

"generate design tokens"
"create color palette"
"build typography scale"
"calculate spacing system"
"create design system"
"generate CSS variables"
"export SCSS tokens"
"set up component architecture"
"document component library"
"calculate responsive breakpoints"
"prepare developer handoff"
"convert brand color to palette"
"check WCAG contrast"
"build 8pt grid system"
Workflows
Workflow 1: Generate Design Tokens

Situation: You have a brand color and need a complete design token system.

Steps:

Identify brand color and style

Brand primary color (hex format)
Style preference: modern | classic | playful

Generate tokens using script

python scripts/design_token_generator.py "#0066CC" modern json


Review generated categories

Colors: primary, secondary, neutral, semantic, surface
Typography: fontFamily, fontSize, fontWeight, lineHeight
Spacing: 8pt grid-based scale (0-64)
Borders: radius, width
Shadows: none through 2xl
Animation: duration, easing
Breakpoints: xs through 2xl

Export in target format

# CSS custom properties
python scripts/design_token_generator.py "#0066CC" modern css > design-tokens.css

# SCSS variables
python scripts/design_token_generator.py "#0066CC" modern scss > _design-tokens.scss

# JSON for Figma/tooling
python scripts/design_token_generator.py "#0066CC" modern json > design-tokens.json


Validate accessibility

Check color contrast meets WCAG AA (4.5:1 normal, 3:1 large text)
Verify semantic colors have contrast colors defined
Workflow 2: Create Component System

Situation: You need to structure a component library using design tokens.

Steps:

Define component hierarchy

Atoms: Button, Input, Icon, Label, Badge
Molecules: FormField, SearchBar, Card, ListItem
Organisms: Header, Footer, DataTable, Modal
Templates: DashboardLayout, AuthLayout

Map tokens to components

Component	Tokens Used
Button	colors, sizing, borders, shadows, typography
Input	colors, sizing, borders, spacing
Card	colors, borders, shadows, spacing
Modal	colors, shadows, spacing, z-index, animation

Define variant patterns

Size variants:

sm: height 32px, paddingX 12px, fontSize 14px
md: height 40px, paddingX 16px, fontSize 16px
lg: height 48px, paddingX 20px, fontSize 18px


Color variants:

primary: background primary-500, text white
secondary: background neutral-100, text neutral-900
ghost: background transparent, text neutral-700


Document component API

Props interface with types
Variant options
State handling (hover, active, focus, disabled)
Accessibility requirements

Reference: See references/component-architecture.md

Workflow 3: Responsive Design

Situation: You need breakpoints, fluid typography, or responsive spacing.

Steps:

Define breakpoints

Name	Width	Target
xs	0	Small phones
sm	480px	Large phones
md	640px	Tablets
lg	768px	Small laptops
xl	1024px	Desktops
2xl	1280px	Large screens

Calculate fluid typography

Formula: clamp(min, preferred, max)

/* 16px to 24px between 320px and 1200px viewport */
font-size: clamp(1rem, 0.5rem + 2vw, 1.5rem);


Pre-calculated scales:

--fluid-h1: clamp(2rem, 1rem + 3.6vw, 4rem);
--fluid-h2: clamp(1.75rem, 1rem + 2.3vw, 3rem);
--fluid-h3: clamp(1.5rem, 1rem + 1.4vw, 2.25rem);
--fluid-body: clamp(1rem, 0.95rem + 0.2vw, 1.125rem);


Set up responsive spacing

Token	Mobile	Tablet	Desktop
--space-md	12px	16px	16px
--space-lg	16px	24px	32px
--space-xl	24px	32px	48px
--space-section	48px	80px	120px

Reference: See references/responsive-calculations.md

Workflow 4: Developer Handoff

Situation: You need to hand off design tokens to development team.

Steps:

Export tokens in required formats

# For CSS projects
python scripts/design_token_generator.py "#0066CC" modern css

# For SCSS projects
python scripts/design_token_generator.py "#0066CC" modern scss

# For JavaScript/TypeScript
python scripts/design_token_generator.py "#0066CC" modern json


Prepare framework integration

React + CSS Variables:

import './design-tokens.css';

<button className="btn btn-primary">Click</button>


Tailwind Config:

const tokens = require('./design-tokens.json');

module.exports = {
  theme: {
    colors: tokens.colors,
    fontFamily: tokens.typography.fontFamily
  }
};


styled-components:

import tokens from './design-tokens.json';

const Button = styled.button`
  background: ${tokens.colors.primary['500']};
  padding: ${tokens.spacing['2']} ${tokens.spacing['4']};
`;


Sync with Figma

Install Tokens Studio plugin
Import design-tokens.json
Tokens sync automatically with Figma styles

Handoff checklist

 Token files added to project
 Build pipeline configured
 Theme/CSS variables imported
 Component library aligned
 Documentation generated

Reference: See references/developer-handoff.md

Tool Reference
design_token_generator.py

Generates complete design token system from brand color.

Argument	Values	Default	Description
brand_color	Hex color	#0066CC	Primary brand color
style	modern, classic, playful	modern	Design style preset
format	json, css, scss, summary	json	Output format

Examples:

# Generate JSON tokens (default)
python scripts/design_token_generator.py "#0066CC"

# Classic style with CSS output
python scripts/design_token_generator.py "#8B4513" classic css

# Playful style summary view
python scripts/design_token_generator.py "#FF6B6B" playful summary


Output Categories:

Category	Description	Key Values
colors	Color palettes	primary, secondary, neutral, semantic, surface
typography	Font system	fontFamily, fontSize, fontWeight, lineHeight
spacing	8pt grid	0-64 scale, semantic (xs-3xl)
sizing	Component sizes	container, button, input, icon
borders	Border values	radius (per style), width
shadows	Shadow styles	none through 2xl, inner
animation	Motion tokens	duration, easing, keyframes
breakpoints	Responsive	xs, sm, md, lg, xl, 2xl
z-index	Layer system	base through notification
Quick Reference Tables
Color Scale Generation
Step	Brightness	Saturation	Use Case
50	95% fixed	30%	Subtle backgrounds
100	95% fixed	38%	Light backgrounds
200	95% fixed	46%	Hover states
300	95% fixed	54%	Borders
400	95% fixed	62%	Disabled states
500	Original	70%	Base/default color
600	Original × 0.8	78%	Hover (dark)
700	Original × 0.6	86%	Active states
800	Original × 0.4	94%	Text
900	Original × 0.2	100%	Headings
Typography Scale (1.25x Ratio)
Size	Value	Calculation
xs	10px	16 ÷ 1.25²
sm	13px	16 ÷ 1.25¹
base	16px	Base
lg	20px	16 × 1.25¹
xl	25px	16 × 1.25²
2xl	31px	16 × 1.25³
3xl	39px	16 × 1.25⁴
4xl	49px	16 × 1.25⁵
5xl	61px	16 × 1.25⁶
WCAG Contrast Requirements
Level	Normal Text	Large Text
AA	4.5:1	3:1
AAA	7:1	4.5:1

Large text: ≥18pt regular or ≥14pt bold

Style Presets
Aspect	Modern	Classic	Playful
Font Sans	Inter	Helvetica	Poppins
Font Mono	Fira Code	Courier	Source Code Pro
Radius Default	8px	4px	16px
Shadows	Layered, subtle	Single layer	Soft, pronounced
Knowledge Base

Detailed reference guides in references/:

File	Content
token-generation.md	Color algorithms, HSV space, WCAG contrast, type scales
component-architecture.md	Atomic design, naming conventions, props patterns
responsive-calculations.md	Breakpoints, fluid typography, grid systems
developer-handoff.md	Export formats, framework setup, Figma sync
Validation Checklist
Token Generation
 Brand color provided in hex format
 Style matches project requirements
 All token categories generated
 Semantic colors include contrast values
Component System
 All sizes implemented (sm, md, lg)
 All variants implemented (primary, secondary, ghost)
 All states working (hover, active, focus, disabled)
 Uses only design tokens (no hardcoded values)
Accessibility
 Color contrast meets WCAG AA
 Focus indicators visible
 Touch targets ≥ 44×44px
 Semantic HTML elements used
Developer Handoff
 Tokens exported in required format
 Framework integration documented
 Design tool synced
 Component documentation complete
Weekly Installs
238
Repository
alirezarezvani/…e-skills
GitHub Stars
13.4K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass