---
rating: ⭐⭐
title: expo-react-native-coder
url: https://skills.sh/pproenca/dot-skills/expo-react-native-coder
---

# expo-react-native-coder

skills/pproenca/dot-skills/expo-react-native-coder
expo-react-native-coder
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill expo-react-native-coder
SKILL.md
Expo React Native Coder Best Practices

Comprehensive feature development guide for Expo React Native applications. Contains 50 rules across 10 categories, covering everything from project setup to testing. Includes production-ready code templates for common features.

When to Apply

Reference these guidelines when:

Setting up a new Expo project with TypeScript
Building navigation with Expo Router (tabs, stacks, drawers, modals)
Creating screens (list, detail, form, settings)
Implementing authentication flows with protected routes
Configuring deep linking and universal links
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Project Setup & Configuration	CRITICAL	setup-
2	Routing & Navigation	CRITICAL	route-
3	Screen Patterns & Layouts	HIGH	screen-
4	Data Fetching & State	HIGH	data-
5	Authentication & Security	HIGH	auth-
6	Deep Linking & Universal Links	HIGH	link-
7	Native UX Patterns	MEDIUM-HIGH	ux-
8	Forms & User Input	MEDIUM	form-
9	Assets & Theming	MEDIUM	asset-
10	Error Handling & Testing	MEDIUM	test-
Quick Reference
1. Project Setup & Configuration (CRITICAL)
setup-typescript-config - Configure TypeScript with strict mode
setup-app-config-typescript - Use typed app.config.ts
setup-environment-variables - EXPO_PUBLIC_ prefix for client vars
setup-eas-build-profiles - EAS build profiles per environment
setup-development-build - Development builds vs Expo Go
2. Routing & Navigation (CRITICAL)
route-file-based-routing - File-based routing with Expo Router
route-tab-navigator - Tab navigator with route groups
route-dynamic-segments - Dynamic route segments [param]
route-stack-within-tabs - Nested stack in tabs
route-modal-presentation - Modal screen presentation
route-typed-routes - Enable typed routes
route-drawer-navigator - Drawer navigator setup
3. Screen Patterns & Layouts (HIGH)
screen-list-flashlist - FlashList for large lists
screen-detail-params - Pass minimal data via params
screen-loading-state - Loading and error states
screen-pull-to-refresh - Pull-to-refresh pattern
screen-header-options - Configure screen headers
screen-settings-list - Settings screen with SectionList
4. Data Fetching & State (HIGH)
data-api-routes - Server-side API routes
data-secure-store - SecureStore for sensitive data
data-sqlite-local - SQLite for complex local data
data-fetch-on-focus - Refetch on screen focus
data-async-storage-simple - AsyncStorage for preferences
data-abort-controller - Cancel fetch on unmount
5. Authentication & Security (HIGH)
auth-protected-routes - Stack.Protected guards
auth-context-provider - Auth context with session
auth-oauth-flow - OAuth with AuthSession
auth-login-form - Login form with validation
auth-splash-loading - Splash screen during auth check
6. Deep Linking & Universal Links (HIGH)
link-deep-linking-scheme - Custom URL scheme
link-universal-links-ios - iOS Universal Links
link-android-app-links - Android App Links
link-handle-incoming - Handle incoming URLs
7. Native UX Patterns (MEDIUM-HIGH)
ux-safe-area-insets - SafeAreaView for notches
ux-status-bar - Status bar styling
ux-haptic-feedback - Haptic feedback on actions
ux-gesture-handler - Gesture handler for swipes
ux-keyboard-avoiding - KeyboardAvoidingView
8. Forms & User Input (MEDIUM)
form-text-input-config - TextInput keyboard types
form-controlled-inputs - Controlled inputs with useState
form-submit-button-state - Disable button during submit
form-dismiss-keyboard - Dismiss keyboard on tap outside
9. Assets & Theming (MEDIUM)
asset-image-optimization - expo-image for caching
asset-font-loading - Load fonts with useFonts
asset-vector-icons - @expo/vector-icons
asset-splash-screen - Splash screen configuration
10. Error Handling & Testing (MEDIUM)
test-jest-setup - Jest with jest-expo preset
test-component-testing - Testing Library for components
test-error-boundary - Error boundaries
test-e2e-maestro - Maestro E2E testing
Code Templates

Production-ready templates are available in assets/templates/:

Template	Description
layouts/tab-layout.tsx	Bottom tab navigator with icons
layouts/auth-layout.tsx	Root layout with protected routes
screens/list-screen.tsx	List with FlashList, refresh, states
screens/detail-screen.tsx	Detail screen with param handling
screens/form-screen.tsx	Form with validation, keyboard handling
hooks/use-auth.tsx	Auth context with SecureStore
components/error-boundary.tsx	Error boundary component
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Full Compiled Document

For a single comprehensive document with all rules, see AGENTS.md.

Reference Files
File	Description
AGENTS.md	Complete compiled guide with all rules
references/_sections.md	Category definitions and ordering
assets/templates/	Production-ready code templates
metadata.json	Version and reference information
Weekly Installs
196
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