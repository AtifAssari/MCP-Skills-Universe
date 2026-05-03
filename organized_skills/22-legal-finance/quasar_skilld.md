---
rating: ⭐⭐
title: quasar-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/quasar-skilld
---

# quasar-skilld

skills/harlan-zw/vue-ecosystem-skills/quasar-skilld
quasar-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill quasar-skilld
SKILL.md
quasarframework/quasar quasar@2.19.3

Tags: legacy: 1.22.10, latest: 2.19.3

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

BREAKING: v-model -> uses model-value + @update:model-value instead of value + @input in Vue 3 source

BREAKING: QDrawer/QDialog/QMenu/QTooltip -> use class and style attributes instead of content-class/content-style props source

BREAKING: QImg -> completely redesigned, removed transition and basic props; renamed no-default-spinner to no-spinner source

BREAKING: QScrollArea -> methods getScrollPosition returns { top, left }; setScrollPosition and setScrollPercentage require axis parameter source

BREAKING: QTable -> renamed data prop to rows to avoid TS naming conflicts source

BREAKING: Platform.is -> all boolean properties now explicitly false instead of undefined since v2.17.0 source

BREAKING: colors utils -> getBrand and setBrand replaced by getCssVar and setCssVar respectively source

BREAKING: Scroll utils -> renamed getScrollPosition to getVerticalScrollPosition, animScrollTo to animVerticalScrollTo, and setScrollPosition to setVerticalScrollPosition source

BREAKING: date utils -> addToDate and subtractFromDate property names normalized (e.g., year -> years, month -> months) source

BREAKING: QPopupEdit -> must now use the default slot with v-slot="scope" for performance source

BREAKING: GoBack directive -> removed; use router reference ($router.back() or $router.go(-1)) instead source

NEW: useQuasar composable -> primary method for accessing the $q object within Composition API components

NEW: useMeta composable -> new way to define meta tags, replacing the now deprecated meta component property source

NEW: QTable props -> added table-row-style-fn, table-row-class-fn, grid-style-fn, and grid-class-fn in v2.18.0 source

Also changed: useFormChild() new composable · QOptionsGroup props option-value, option-label, option-disable new v2.17.0 · QUploader prop thumbnail-fit new v2.17.0 · QSelect prop disable-tab-select new v2.17.0 · QMenu/QBtnDropdown no-esc-dismiss new v2.18.0 · evt.qAvoidFocus new flag v2.18.0 · QDate model-value no longer contains changed prop · QPagination prop gutter new · QImg props loading, crossorigin, fit new · Dialog plugin custom component props moved to componentProps · Loading plugin uses html: true for HTML content instead of sanitize · App.vue wrapper <div id="q-app"> removed · .sync modifier replaced by v-model:propName

Best Practices

Use #q-app/wrappers instead of quasar/wrappers for defining configurations and boot files — provides superior type inference and alignment with modern Quasar CLI source

Use Regle as the recommended validation library for QInput and QField — provides a robust, externalized validation logic compared to inline rules source

Prefer responsive CSS classes (e.g., gt-sm, lt-md) over the Screen plugin in JavaScript — minimizes re-renders and layout shifts by leveraging CSS media queries directly source

Bootstrap custom dialog components with the useDialogPluginComponent composable — handles the complex internal communication and lifecycle requirements of the Dialog plugin automatically source

Enable the no-transition prop on QTree when rendering large datasets — significantly improves runtime performance by skipping expensive expansion/collapse animations source

Use Quasar's useInterval and useTimeout composables over native browser timers — ensures automatic cancellation and memory cleanup when the component is unmounted source

Place QPullToRefresh as a direct child of QPage when using QLayout — ensures correct scroll event interception and native-like pull behavior within the layout container source

Avoid setting Dark mode to auto in SSR applications — prevents the "flicker" effect where the server renders light mode before the client synchronizes with system preferences source

Do not use v-model with QRouteTab components — the active state is derived directly from the current route, and manual model updates will not trigger navigation source

Prefer the Loading Bar Plugin over manual QAjaxBar component instances — provides a simpler, globally managed progress indicator for all Ajax calls without per-page wiring source

Weekly Installs
188
Repository
harlan-zw/vue-e…m-skills
GitHub Stars
158
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass