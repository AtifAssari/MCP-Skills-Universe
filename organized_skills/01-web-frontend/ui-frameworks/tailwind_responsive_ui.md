---
rating: ⭐⭐
title: tailwind-responsive-ui
url: https://skills.sh/pproenca/dot-skills/tailwind-responsive-ui
---

# tailwind-responsive-ui

skills/pproenca/dot-skills/tailwind-responsive-ui
tailwind-responsive-ui
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill tailwind-responsive-ui
SKILL.md
Community Responsive UI Tailwind CSS Best Practices

Comprehensive responsive transformation guide for Tailwind CSS applications, based on Refactoring UI by Adam Wathan & Steve Schoger and modern responsive design patterns. Contains 49 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Making an existing UI responsive across screen sizes
Building new responsive layouts with Tailwind CSS
Refactoring desktop-only interfaces for mobile support
Reviewing responsive code for breakpoint, spacing, and typography issues
Adapting navigation, forms, and data tables for touch devices
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Breakpoint Strategy	CRITICAL	bp-
2	Layout Transformation	CRITICAL	layout-
3	Responsive Spacing	HIGH	rspac-
4	Fluid Typography	HIGH	fluid-
5	Navigation Patterns	MEDIUM-HIGH	nav-
6	Touch & Interaction	MEDIUM	touch-
7	Responsive Media	MEDIUM	rmedia-
8	Data Adaptation	LOW-MEDIUM	data-
Quick Reference
1. Breakpoint Strategy (CRITICAL)
bp-mobile-first-default - Use Mobile-First Breakpoint Direction
bp-content-driven-breakpoints - Set Breakpoints Where Content Breaks
bp-avoid-device-widths - Avoid Device-Specific Breakpoint Values
bp-consolidate-breakpoints - Consolidate Breakpoints to Three or Four
bp-min-width-over-max - Use min-width Over max-width for Breakpoints
bp-debug-breakpoints - Use Visual Breakpoint Indicators During Development
2. Layout Transformation (CRITICAL)
layout-stack-to-row - Stack Elements on Mobile, Row on Desktop
layout-sidebar-collapse - Collapse Sidebar to Top or Bottom on Mobile
layout-grid-column-reduction - Reduce Grid Columns at Narrower Breakpoints
layout-holy-grail-responsive - Use Responsive Holy Grail Layout with Grid
layout-sticky-to-static - Convert Sticky Elements to Static on Mobile
layout-fixed-to-relative - Replace Fixed Positioning with Relative on Mobile
layout-aspect-ratio-containers - Use Aspect Ratio for Responsive Containers
3. Responsive Spacing (HIGH)
rspac-scale-padding-per-bp - Scale Padding Independently Per Breakpoint
rspac-responsive-gap - Use Responsive Gap for Grid and Flex Spacing
rspac-compact-mobile-generous-desktop - Use Compact Spacing on Mobile, Generous on Desktop
rspac-section-spacing - Scale Section Dividers with Viewport
rspac-inline-to-stack-spacing - Convert Inline Spacing to Stack Spacing on Mobile
rspac-container-padding - Use Responsive Container Padding
4. Fluid Typography (HIGH)
fluid-clamp-font-size - Use clamp() for Fluid Font Sizing
fluid-responsive-line-height - Tighten Line Height as Font Size Increases
fluid-responsive-measure - Constrain Line Length to 45-75 Characters
fluid-scale-headings-independently - Scale Heading Sizes Independently Across Breakpoints
fluid-responsive-letter-spacing - Adjust Letter Spacing for Responsive Headlines
fluid-type-scale - Use a Responsive Type Scale
5. Navigation Patterns (MEDIUM-HIGH)
nav-horizontal-to-hamburger - Collapse Horizontal Nav to Hamburger on Mobile
nav-tab-bar-mobile - Use Bottom Tab Bar for Primary Mobile Navigation
nav-breadcrumb-collapse - Truncate Breadcrumbs on Mobile
nav-sidebar-drawer - Convert Sidebar Nav to Off-Canvas Drawer on Mobile
nav-dropdown-to-fullscreen - Expand Dropdown Menus to Full-Width on Mobile
nav-sticky-header-compact - Compact the Header on Scroll for Mobile
6. Touch & Interaction (MEDIUM)
touch-min-touch-target - Ensure Minimum 44px Touch Targets on Mobile
touch-hover-to-tap - Replace Hover Interactions with Tap-Friendly Alternatives
touch-swipe-affordance - Add Visual Swipe Affordances for Horizontal Scrolling
touch-scroll-snap-mobile - Use Scroll Snap for Carousel-Like Mobile Interfaces
touch-input-sizing-mobile - Size Form Inputs to Prevent iOS Zoom
touch-focus-visible-touch - Use focus-visible for Touch-Friendly Focus Styles
7. Responsive Media (MEDIUM)
rmedia-responsive-images - Use Responsive Image Sizing with Object-Fit
rmedia-video-aspect-ratio - Maintain Video Aspect Ratio Across Breakpoints
rmedia-icon-size-scaling - Scale Icons Per Breakpoint, Not with Font Size
rmedia-avatar-responsive - Scale Avatar Sizes Per Context and Breakpoint
rmedia-background-image-bp - Swap Background Images at Breakpoints
rmedia-embed-responsive - Make Embedded Content Responsive with Container Constraints
8. Data Adaptation (LOW-MEDIUM)
data-table-to-cards - Transform Tables to Cards on Mobile
data-horizontal-scroll-table - Use Horizontal Scroll for Dense Data Tables
data-responsive-data-grid - Adapt Data Grid Density for Screen Size
data-list-density-mobile - Increase List Item Density on Mobile
data-truncate-overflow - Truncate Overflowing Text on Mobile
data-responsive-form-layout - Stack Form Fields on Mobile, Use Grid on Desktop
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
177
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass