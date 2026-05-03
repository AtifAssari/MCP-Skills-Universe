---
title: shadcn-vue-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/shadcn-vue-skilld
---

# shadcn-vue-skilld

skills/harlan-zw/vue-ecosystem-skills/shadcn-vue-skilld
shadcn-vue-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill shadcn-vue-skilld
SKILL.md
unovue/shadcn-vue shadcn-vue@2.6.2

Tags: radix: 0.11.4, latest: 2.6.2

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

BREAKING: Separator label props removed — labels in Separator are no longer supported in Tailwind v3 configurations since v2.2.0 source

BREAKING: vue-sonner v2 update — requires manual update of Toaster component for compatibility with the latest version source

BREAKING: HSL colors converted to OKLCH — default color space changed to OKLCH in v2.0.0, affecting custom CSS variable logic source

BREAKING: NavigationMenuLink state change — now uses data-active instead of previous state indicators to match reka-ui source

BREAKING: Chart showGradient prop — corrected typo in prop name from showGradiant to showGradient in v2.3.0 source

DEPRECATED: toast component — officially deprecated in favor of sonner; current toast implementations should be migrated source

DEPRECATED: default style — phased out in v2.0.0; new projects are initialized with new-york by default source

NEW: Tailwind v4 support — introduces full integration with the Tailwind v4 engine and @theme directive source

NEW: NativeSelect modelValue — provides native v-model support for the NativeSelect component source

NEW: Kbd component — keyboard key display component for shortcuts and UI documentation source

NEW: Button-group component — new layout component specifically for grouping related button actions source

NEW: Spinner component — added dedicated loading spinner component to the registry source

NEW: PinInput generic types — enhanced type safety for PinInput allowing custom value types source

NEW: data-slot attributes — added to all primitives to simplify granular styling in complex components source

Also changed: Stepper slot props binding fix · Sidebar cookie state · size-* utility support · phosphor and tabler icon support

Best Practices

Prefer CSS variables over utility classes for theming to enable dynamic runtime adjustments and easier maintenance of complex color schemes source

Omit the background suffix when using variables for background colors in utility classes; for example, bg-primary automatically maps to the --primary variable source

Build sidebars by composing sub-components (SidebarProvider, SidebarContent, SidebarGroup, etc.) rather than a single monolithic component to maintain flexibility and customization source

Avoid the legacy Form component; use VeeValidate or TanStack Form integrations for more robust, actively maintained form handling and validation patterns source

Utilize the valueUpdater helper when managing TanStack Table state in Vue to correctly handle both direct value assignments and functional state transformations source

export function valueUpdater<T extends Updater<any>>(updaterOrValue: T, ref: Ref) {
  ref.value = typeof updaterOrValue === 'function'
    ? updaterOrValue(ref.value)
    : updaterOrValue
}


Enable automatic sidebar state persistence across page reloads by providing a storageKey prop to the SidebarProvider component source

Leverage the default cmd+b or ctrl+b keyboard shortcuts provided by SidebarProvider to toggle sidebar visibility without manual event listeners source

Treat the code in Sidebar*.vue (and other added UI components) as your own project code; you are explicitly encouraged to modify the source to suit specific design needs source

Build custom data tables from headless primitives and the basic <Table /> component instead of looking for a pre-built, configuration-heavy "DataTable" component source

(experimental) Use the build command and registry.json schema to create and share your own custom component registries for internal or community use source

Weekly Installs
103
Repository
harlan-zw/vue-e…m-skills
GitHub Stars
158
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn