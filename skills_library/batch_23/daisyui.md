---
title: daisyui
url: https://skills.sh/pzyyll/ai-agents/daisyui
---

# daisyui

skills/pzyyll/ai-agents/daisyui
daisyui
Installation
$ npx skills add https://github.com/pzyyll/ai-agents --skill daisyui
SKILL.md
daisyUI 5

daisyUI 5 is a CSS library for Tailwind CSS 4 that provides class names for common UI components.

daisyUI 5 docs
daisyUI 5 release notes
When to use this skill

Use this skill when:

Building UI components with daisyUI 5
Need reference for daisyUI class names and usage rules
Customizing themes with daisyUI config
Understanding daisyUI color system
Following best practices for daisyUI component styling
Refactoring UI with daisyUI components
Learning how to use daisyUI 5 effectively in Tailwind CSS 4 projects
Installation

install guide

daisyUI 5 requires Tailwind CSS 4
tailwind.config.js is deprecated in Tailwind CSS v4. Use CSS file only.
Install: npm i -D daisyui@latest
CSS file setup:
@import "tailwindcss";
@plugin "daisyui";


CDN alternative:

<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>

Usage Rules
Style elements by adding component class + part classes + modifier classes
Customize with Tailwind CSS utility classes (e.g., btn px-10)
Use ! suffix to override specificity issues (e.g., btn bg-red-500!) - last resort
Create custom components with Tailwind utilities if daisyUI doesn't have it
Use Tailwind responsive prefixes for flex and grid layouts
Only use daisyUI class names or Tailwind CSS utility classes
Avoid custom CSS - prefer daisyUI/Tailwind classes
Placeholder images: https://picsum.photos/200/300
Don't add custom fonts unless necessary
Don't add bg-base-100 text-base-content to body unless necessary
Follow Refactoring UI best practices
Class Name Categories
component: required component class
part: child part of component
style: specific style modifier
behavior: behavior modifier
color: color modifier
size: size modifier
placement: placement modifier
direction: direction modifier
modifier: general modifier
variant: conditional prefix (syntax: variant:utility-class)
Config

config docs

Basic:

@plugin "daisyui";


Light theme only:

@plugin "daisyui" {
	themes: light --default;
}


Full config:

@plugin "daisyui" {
	themes:
		light --default,
		dark --prefersdark;
	root: ":root";
	include:;
	exclude:;
	prefix:;
	logs: true;
}

Colors
Color Names
Color	Description
primary	Primary brand color
primary-content	Foreground on primary
secondary	Secondary brand color
secondary-content	Foreground on secondary
accent	Accent brand color
accent-content	Foreground on accent
neutral	Neutral dark color
neutral-content	Foreground on neutral
base-100	Base surface color
base-200	Darker base shade
base-300	Even darker base shade
base-content	Foreground on base
info	Info messages
info-content	Foreground on info
success	Success messages
success-content	Foreground on success
warning	Warning messages
warning-content	Foreground on warning
error	Error messages
error-content	Foreground on error
Color Rules
Use in utility classes like bg-primary, text-base-content
Colors change automatically based on theme
No need for dark: prefix with daisyUI colors
Avoid Tailwind color names (e.g., red-500) - they don't adapt to themes
Use base-* colors for majority of page, primary for important elements
Custom Theme
@plugin "daisyui/theme" {
	name: "mytheme";
	default: true;
	prefersdark: false;
	color-scheme: light;

	--color-base-100: oklch(98% 0.02 240);
	--color-base-200: oklch(95% 0.03 240);
	--color-base-300: oklch(92% 0.04 240);
	--color-base-content: oklch(20% 0.05 240);
	--color-primary: oklch(55% 0.3 240);
	--color-primary-content: oklch(98% 0.01 240);
	--color-secondary: oklch(70% 0.25 200);
	--color-secondary-content: oklch(98% 0.01 200);
	--color-accent: oklch(65% 0.25 160);
	--color-accent-content: oklch(98% 0.01 160);
	--color-neutral: oklch(50% 0.05 240);
	--color-neutral-content: oklch(98% 0.01 240);
	--color-info: oklch(70% 0.2 220);
	--color-info-content: oklch(98% 0.01 220);
	--color-success: oklch(65% 0.25 140);
	--color-success-content: oklch(98% 0.01 140);
	--color-warning: oklch(80% 0.25 80);
	--color-warning-content: oklch(20% 0.05 80);
	--color-error: oklch(65% 0.3 30);
	--color-error-content: oklch(98% 0.01 30);

	--radius-selector: 1rem;
	--radius-field: 0.25rem;
	--radius-box: 0.5rem;
	--size-selector: 0.25rem;
	--size-field: 0.25rem;
	--border: 1px;
	--depth: 1;
	--noise: 0;
}


Theme generator: https://daisyui.com/theme-generator/

Component Index

Load component docs on-demand from components/ folder.

Component	File	Description
accordion	accordion.md	Show/hide content, one item open at a time
alert	alert.md	Inform users about important events
avatar	avatar.md	Show thumbnails/profile images
badge	badge.md	Status indicators on data
breadcrumbs	breadcrumbs.md	Navigation trail
button	button.md	User action triggers
calendar	calendar.md	Date picker styles (Cally/Pikaday/React Day Picker)
card	card.md	Group and display content
carousel	carousel.md	Scrollable image/content area
chat	chat.md	Conversation bubbles
checkbox	checkbox.md	Select/deselect values
collapse	collapse.md	Show/hide content (single)
countdown	countdown.md	Animated number transitions
diff	diff.md	Side-by-side comparison
divider	divider.md	Separate content
dock	dock.md	Bottom navigation bar
drawer	drawer.md	Sidebar layout
dropdown	dropdown.md	Menu on button click
fab	fab.md	Floating action button
fieldset	fieldset.md	Form element grouping
file-input	file-input.md	File upload field
filter	filter.md	Radio button filter group
footer	footer.md	Page footer
hero	hero.md	Large display box with title
hover-3d	hover-3d.md	3D hover effect wrapper
hover-gallery	hover-gallery.md	Image gallery on hover
indicator	indicator.md	Corner element placement
input	input.md	Text input field
join	join.md	Group items together
kbd	kbd.md	Keyboard shortcut display
label	label.md	Input field labels
link	link.md	Styled anchor links
list	list.md	Vertical info rows
loading	loading.md	Loading animations
mask	mask.md	Shape cropping
menu	menu.md	Link list navigation
mockup-browser	mockup-browser.md	Browser window mockup
mockup-code	mockup-code.md	Code editor mockup
mockup-phone	mockup-phone.md	iPhone mockup
mockup-window	mockup-window.md	OS window mockup
modal	modal.md	Dialog/popup box
navbar	navbar.md	Top navigation bar
pagination	pagination.md	Page navigation buttons
progress	progress.md	Progress bar
radial-progress	radial-progress.md	Circular progress
radio	radio.md	Single option selection
range	range.md	Slider input
rating	rating.md	Star rating
select	select.md	Dropdown selection
skeleton	skeleton.md	Loading placeholder
stack	stack.md	Stacked elements
stat	stat.md	Number/data display
status	status.md	Small status icon
steps	steps.md	Process steps
swap	swap.md	Toggle visibility
tab	tab.md	Tabbed navigation
table	table.md	Data table
text-rotate	text-rotate.md	Rotating text animation
textarea	textarea.md	Multi-line text input
theme-controller	theme-controller.md	Theme switcher
timeline	timeline.md	Chronological events
toast	toast.md	Corner notifications
toggle	toggle.md	Switch button
tooltip	tooltip.md	Hover message
validator	validator.md	Form validation styles
Weekly Installs
12
Repository
pzyyll/ai-agents
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass