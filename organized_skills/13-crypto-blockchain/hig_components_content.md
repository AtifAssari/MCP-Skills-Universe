---
rating: ⭐⭐
title: hig-components-content
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-components-content
---

# hig-components-content

skills/raintree-technology/apple-hig-skills/hig-components-content
hig-components-content
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-components-content
SKILL.md
Apple HIG: Content Components

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Adapt to different sizes and contexts. Content components must work across screen sizes, orientations, and multitasking configurations. Use Auto Layout and size classes.

Make content accessible. Charts need audio graph support. Images need alt text. Collections need proper VoiceOver navigation order. All content components need labels and descriptions.

Maintain visual hierarchy. Use spacing, sizing, and grouping to establish clear information hierarchy. Primary content should be visually prominent.

Use system components first. Evaluate UICollectionView, SwiftUI Charts, WKWebView before building custom. System components come with built-in accessibility and platform adaptation.

Respect platform conventions. A collection on tvOS uses large lockups with parallax. The same collection on iOS uses compact cells with touch targets. On visionOS, content gains depth and hover effects.

Handle empty states. Show a meaningful empty state with guidance on how to populate it, not a blank screen.

Optimize for performance. Use lazy loading, cell reuse, pagination, and prefetching for large datasets.

Reference Index
Reference	Topic	Key content
charts.md	Charts	Swift Charts, bar/line/area/point marks, chart accessibility, audio graphs
collections.md	Collections	Grid/list layouts, compositional layout, selection, reordering, diffable data sources
image-views.md	Image Views	Aspect ratio handling, content modes, SF Symbol images, accessibility
image-wells.md	Image Wells	Drag-and-drop image selection, macOS-specific, placeholder content
color-wells.md	Color Wells	Color selection UI, system color picker, custom color spaces
web-views.md	Web Views	WKWebView, SFSafariViewController, navigation controls, content restrictions
activity-views.md	Activity Views	Share sheets, activity items, custom activities, action extensions
lockups.md	Lockups	Image+text elements, tvOS card layouts, focus effects, shelf layouts
Component Selection Guide
Content Need	Recommended Component	Platform Notes
Visualizing quantitative data	Charts (Swift Charts)	iOS 16+, macOS 13+, watchOS 9+
Browsing a grid or list of items	Collection View	Compositional layout for complex arrangements
Displaying a single image	Image View	Support aspect ratio fitting; provide accessibility description
Selecting an image via drag or browse	Image Well	macOS primarily; use image pickers on iOS
Selecting a color	Color Well	Triggers system color picker; macOS, iOS 14+
Showing web content inline	Web View (WKWebView)	Use SFSafariViewController for external browsing
Sharing content to other apps	Activity View	System share sheet with configurable activity types
Content card (image + text)	Lockup	Primarily tvOS; adaptable to other platforms
Output Format
Component recommendation with rationale, referencing the relevant HIG reference file.
Configuration guidance -- key properties and setup.
Accessibility requirements for the recommended component.
Platform-specific notes for targeted platforms.
Questions to Ask
What type of content? (Quantitative data, images, web content, browsable collection, share action?)
Which platforms?
Static or dynamic content?
How much content? (Few items vs hundreds/thousands affects component choice and optimization.)
Related Skills
hig-foundations -- Color, typography, accessibility, and image guidelines
hig-patterns -- Data visualization, sharing, and loading patterns
hig-components-layout -- Structural containers (scroll views, lists, split views) hosting content
hig-platforms -- Platform-specific component behavior (lockups on tvOS, web views on macOS)

Built by Raintree Technology · More developer tools

Weekly Installs
152
Repository
raintree-techno…g-skills
GitHub Stars
45
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass