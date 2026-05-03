---
rating: ⭐⭐
title: shadcn-vue
url: https://skills.sh/ycs77/skills/shadcn-vue
---

# shadcn-vue

skills/ycs77/skills/shadcn-vue
shadcn-vue
Installation
$ npx skills add https://github.com/ycs77/skills --skill shadcn-vue
SKILL.md

The skill is based on shadcn-vue (latest, Reka UI v2 + Tailwind CSS v4), generated at 2026-02-14.

shadcn-vue is a code distribution system for Vue components. Instead of installing a package, you copy component source code into your project for full control. Components are built on Reka UI (headless primitives) and styled with Tailwind CSS.

Key conventions:

Install components via npx shadcn-vue@latest add <component>
Components live in @/components/ui/<component>
Utilities in @/lib/utils (provides cn class merge helper)
Composables in @/composables/
Uses new-york style (default style is deprecated)
Reka UI provides the headless primitive layer
Core References
Topic	Description	Reference
Project Setup & CLI	CLI commands, components.json config, project initialization	core-setup
Theming & Dark Mode	CSS variables, color conventions, dark mode setup	core-theming
Components
Data Entry
Topic	Description	Reference
Button & ButtonGroup	Button variants, ButtonGroup, split buttons	components-button
Input Components	Input, InputGroup, Textarea, NumberField, InputOTP, PinInput, TagsInput	components-input
Selection Controls	Checkbox, RadioGroup, Switch, Toggle, ToggleGroup, Slider	components-selection-controls
Select & Command	Select, NativeSelect, Combobox, Command palette	components-select
Date Components	Calendar, DatePicker, RangeCalendar	components-date-picker
Data Display
Topic	Description	Reference
Display Components	Card, Table, Avatar, Item, Empty, Badge, Kbd, Label, Spinner, Skeleton, Progress	components-data-display
Overlays
Topic	Description	Reference
Dialog & Panels	Dialog, AlertDialog, Sheet, Drawer, Popover, HoverCard, Tooltip	components-overlay
Menus	DropdownMenu, ContextMenu, Menubar	components-menu
Navigation & Layout
Topic	Description	Reference
Navigation	Breadcrumb, NavigationMenu, Tabs, Pagination, Stepper	components-navigation
Layout & Feedback	Accordion, Collapsible, Separator, AspectRatio, Resizable, ScrollArea, Carousel, Alert, Toast/Sonner	components-layout
Features
Topic	Description	Reference
Field Component	Accessible form field system with labels, descriptions, errors, groups	features-field
Forms: VeeValidate	Form validation with VeeValidate + Zod + Field component	features-form-vee-validate
Forms: TanStack Form	Form validation with TanStack Form + Zod + Field component	features-form-tanstack
Data Table	TanStack Table with sorting, filtering, pagination, selection, expanding	features-data-table
Sidebar	Composable sidebar with menus, collapsible groups, theming	features-sidebar
Charts	Unovis-based charts with ChartConfig, tooltips, legends	features-charts
Advanced
Topic	Description	Reference
Custom Registry	Building and distributing custom component registries	advanced-registry
Weekly Installs
20
Repository
ycs77/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn