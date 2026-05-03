---
title: mobile-app-interface
url: https://skills.sh/qodex-ai/ai-agent-skills/mobile-app-interface
---

# mobile-app-interface

skills/qodex-ai/ai-agent-skills/mobile-app-interface
mobile-app-interface
Installation
$ npx skills add https://github.com/qodex-ai/ai-agent-skills --skill mobile-app-interface
SKILL.md

Expo iOS Designer Core Design Prompt “Design a modern, clean iOS app using Expo and React Native that follows Apple’s Human Interface Guidelines: prioritize clear hierarchy and harmony; respect safe areas; use responsive Flexbox layouts and Dynamic Type with SF Pro; support dark mode with semantic system-friendly colors; keep minimum 44pt touch targets; use native navigation patterns (tabs, stacks, modals) and standard gestures; apply Liquid Glass materials sparingly for overlays like bars, sheets, and popovers with AA contrast; add purposeful motion and gentle haptics; honor Reduce Motion and Reduce Transparency; deliver icons/splash and store assets per Apple guidance.”.​

Design Rules

Safe Areas Rule Wrap screens with SafeAreaProvider/SafeAreaView to avoid notches and the home indicator; never hard‑code insets.​

tsx import { SafeAreaView } from "react-native-safe-area-context";

export function Screen({ children }) { return <SafeAreaView style={{ flex: 1 }}>{children}; } 2) Typography Rule Use SF Pro Text/Display (or system) with a documented type ramp; support Dynamic Type so text scales with user settings.​

tsx <Text style={{ fontSize: 17, fontWeight: "600" }} accessibilityRole="header"> Title <Text style={{ fontSize: 15, color: "#6b7280" }}>Secondary text 3) Touch Target Rule Ensure interactive controls are at least 44×44pt, with adequate spacing between targets for accurate taps.​

tsx <TouchableOpacity style={{ minHeight: 44, minWidth: 44, justifyContent: "center", alignItems: "center" }} accessibilityRole="button"

Action 4) Color & Theming Rule Use semantic roles and support light/dark with AA contrast for text and essential UI; prefer system-friendly palettes that adapt across appearances.​

tsx const scheme = useColorScheme(); const bg = scheme === "dark" ? "#0B0B0B" : "#FFFFFF"; const fg = scheme === "dark" ? "#E5E7EB" : "#111827"; 5) Navigation Rule Use tab bars for top-level sections, stack for drill-ins, and modals for short tasks; align back navigation with iOS gestures and conventions.​

IMPORTANT: For Tab Bars with Liquid Glass ALWAYS use NativeTabs from Expo Router instead of custom tab bars. NativeTabs provides native iOS UITabBarController with built-in Liquid Glass effect - no manual implementation needed!

tsx // ✅ CORRECT: Native tab bar with built-in Liquid Glass import { NativeTabs, Icon, Label } from "expo-router/unstable-native-tabs";

export default function TabLayout() { return ( <NativeTabs.Trigger name="index"> <Icon sf={{ default: 'house', selected: 'house.fill' }} /> Home </NativeTabs.Trigger> <NativeTabs.Trigger name="settings"> <Icon sf={{ default: 'gearshape', selected: 'gearshape.fill' }} /> Settings </NativeTabs.Trigger> ); }

// ❌ WRONG: Custom tab bars - requires manual Liquid Glass implementation import { createBottomTabNavigator } from "@react-navigation/bottom-tabs"; const Tab = createBottomTabNavigator();

NativeTabs Features:

Built-in Liquid Glass blur (automatic on iOS 26+)
SF Symbols for icons (sf prop with default/selected states)
Native iOS animations and haptics
Automatic light/dark mode adaptation
System-native behavior (matches Safari, Apple Music, etc.)
No custom styling required

SF Symbols Icon Examples:

Home: house / house.fill
Settings: gearshape / gearshape.fill
Messages: message / message.fill
Profile: person / person.fill
Search: magnifyingglass
Calendar: calendar / calendar.fill
Star: star / star.fill

Find more at: https://developer.apple.com/sf-symbols/ 6) Motion & Haptics Rule Keep transitions 200–400ms with native-feeling ease or spring; pair key state changes and confirmations with gentle haptics.​

tsx import * as Haptics from "expo-haptics"; const onPress = async () => { await Haptics.selectionAsync(); /* action */ }; 7) Accessibility Rule Provide accessibilityLabel, Role, Hint, and state; verify logical focus order and complete VoiceOver announcements across flows.​

tsx <Switch value={isOn} onValueChange={setOn} accessibilityRole="switch" accessibilityLabel="Notifications" accessibilityState={{ checked: isOn }} /> 8) List & Performance Rule Use FlatList/SectionList with keyExtractor, optional getItemLayout, and memoized rows; avoid re-render churn for smooth 60fps scrolling.​

tsx <FlatList data={items} keyExtractor={(it) => it.id} renderItem={memo(({ item }) => )} /> 9) Assets & App Store Rule Create icons and splash per Expo docs; verify in an EAS build, not Expo Go; keep store metadata and permissions aligned to behavior.​

json // app.json (excerpt) { "expo": { "icon": "./assets/icon.png", "splash": { "image": "./assets/splash.png", "resizeMode": "contain", "backgroundColor": "#000000" } } } 10) Layout & Spacing Rule Compose with Flexbox and a consistent spacing scale; adapt padding to dynamic type and safe areas for balanced, accessible layouts.​

tsx <View style={{ padding: 16, gap: 12, flex: 1 }}> {/* content */} 11) Liquid Glass Materials Rule Use Liquid Glass on overlay surfaces (navigation/tab bars, large headers, sheets, popovers, floating cards) to add depth without distracting from content; verify AA contrast over dynamic backdrops in light and dark modes.​

Respect Reduce Transparency and provide solid/tinted fallbacks; avoid placing dense text over highly saturated or high-frequency backdrops.​

Keep materials subtle: modest opacity/blur, applied sparingly to chrome rather than full-screen backgrounds for readability and performance.​

Expo Glass Modules Rule Official module: expo-glass-effect. Provides GlassView, GlassContainer, and isLiquidGlassAvailable() to detect capability and compose grouped glass surfaces.​

Community SwiftUI module: expo-liquid-glass-view. Fine control over corner radius, styles, and tints; iOS-only; ensure platform fallbacks.​

Install and basic usage:

bash npx expo install expo-glass-effect tsx import { GlassView } from "expo-glass-effect";

bash npx expo install expo-liquid-glass-view tsx import { ExpoLiquidGlassView } from "expo-liquid-glass-view"; These render native iOS Liquid Glass via UIVisualEffectView/SwiftUI, and gracefully fall back to a regular View on unsupported platforms.​

Availability & Fallbacks Rule Check availability on iOS 26+ with isLiquidGlassAvailable(); also honor AccessibilityInfo.isReduceTransparencyEnabled() for fallbacks to solid/tinted surfaces.​

tsx import { isLiquidGlassAvailable, GlassView } from "expo-glass-effect"; import { AccessibilityInfo, Platform } from "react-native";

const useGlass = async () => { const supported = Platform.OS === "ios" && (await isLiquidGlassAvailable()); const reduceTransparency = await AccessibilityInfo.isReduceTransparencyEnabled(); return { supported, reduceTransparency }; }; 14) Materials Performance Rule Avoid full-screen realtime blur on animated scenes; scope glass to small overlays, cache where possible, and profile on device; fall back to static blur or solids when FPS dips.​

Icon Variants Rule Provide dark and tinted icon variants following updated Apple resources for consistent appearance with system tints and wallpapers.​

Workflow

Interview User Scope: screen, flow, or component; target file/repo path; materials use-cases (bars, sheets, overlays); accessibility/performance targets.​

Design & Implement Match HIG patterns and the existing design system; compose UI first; define component variants/states.​

Apply all rules (safe area, type, touch, color, nav, motion, a11y, performance, materials, icons). Test Dynamic Type, dark mode, VoiceOver, Reduce Transparency/Motion, and iOS 26 availability.​

Validate on device for performance, notch layouts, and readability over moving content and wallpapers.​

Component Structure Pattern tsx import { View, Text } from "react-native"; import { SafeAreaView } from "react-native-safe-area-context";

export function ScreenTemplate({ title, children }) { return ( <SafeAreaView style={{ flex: 1 }}> <View style={{ padding: 20, gap: 16 }}> <Text style={{ fontSize: 28, fontWeight: "700" }} accessibilityRole="header"> {title} <View style={{ gap: 12 }}>{children} ); } Quality Checklist Safe areas respected across edges and orientations.​

SF Pro/system fonts with Dynamic Type verified at larger sizes.​

44×44pt touch targets and adequate spacing confirmed on device.​

Light/dark with semantic colors and WCAG AA contrast for text and core UI.​

Native navigation patterns and back gestures consistent with iOS.​

Purposeful motion with gentle haptics; honors Reduce Motion.​

Accessibility labels/roles/hints/states and logical focus order; VoiceOver validated.​

Lists are smooth and jank-free; renders and images optimized.​

Icons/splash configured via Expo and tested in an EAS build.​

Store metadata and permissions aligned with behavior.​

Liquid Glass used for overlays only; AA contrast verified over dynamic backdrops.​

Availability checks with isLiquidGlassAvailable(); fallbacks for Reduce Transparency.​

Materials performance profiled; fallbacks applied if FPS drops.​

Icon dark/tinted variants per updated resources.​

References Apple HIG: layout, navigation, materials, typography.​

Expo GlassEffect API and install guides; SwiftUI module references.​

Expo docs: safe areas, splash/icon configuration, project setup and device testing.​

Accessibility: React Native docs and testing guidance for roles, labels, focus order, touch targets.​

Weekly Installs
88
Repository
qodex-ai/ai-agent-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass