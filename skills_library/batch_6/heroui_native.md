---
title: heroui-native
url: https://skills.sh/heroui-inc/heroui/heroui-native
---

# heroui-native

skills/heroui-inc/heroui/heroui-native
heroui-native
Installation
$ npx skills add https://github.com/heroui-inc/heroui --skill heroui-native
Summary

React Native component library with Uniwind styling, semantic variants, and compound component patterns.

Built on Uniwind (Tailwind CSS for React Native) with HSL color format; do not apply web HeroUI patterns or colors
Includes accessible, customizable components (Button, Card, TextField, Dialog) using compound component structure accessed via dot notation
Provides semantic variants (primary, secondary, tertiary, danger, ghost, outline) that adapt to light/dark themes via CSS variables
Requires GestureHandlerRootView and HeroUINativeProvider wrapping; uses onPress event handlers instead of onClick
Fetch component MDX docs before implementing for complete props, anatomy, and examples
SKILL.md
HeroUI Native Development Guide

HeroUI Native is a component library built on Uniwind (Tailwind CSS for React Native) and React Native, providing accessible, customizable UI components for mobile applications.

Installation
curl -fsSL https://heroui.com/install | bash -s heroui-native

CRITICAL: Native Only - Do Not Use Web Patterns

This guide is for HeroUI Native ONLY. Do NOT apply HeroUI React (web) patterns — the package, styling engine, and color format all differ:

Feature	React (Web)	Native (Mobile)
Styling	Tailwind CSS v4	Uniwind (Tailwind for React Native)
Colors	oklch format	HSL format
Package	@heroui/react	heroui-native
Platform	Web browsers	iOS & Android
// CORRECT — Native pattern
import { Button } from "heroui-native";

<Button variant="primary" onPress={() => console.log("Pressed!")}>
	Click me
</Button>;


Always fetch Native docs before implementing.

Core Principles
Semantic variants (primary, secondary, tertiary) over visual descriptions
Composition over configuration (compound components)
Theme variables with HSL color format
React Native StyleSheet patterns with Uniwind utilities
Accessing Documentation & Component Information

For component details, examples, props, and implementation patterns, always fetch documentation:

Using Scripts
# List all available components
node scripts/list_components.mjs

# Get component documentation (MDX)
node scripts/get_component_docs.mjs Button
node scripts/get_component_docs.mjs Button Card TextField

# Get theme variables
node scripts/get_theme.mjs

# Get non-component docs (guides, releases)
node scripts/get_docs.mjs /docs/native/getting-started/theming

Direct MDX URLs

Component docs: https://heroui.com/docs/native/components/{component-name}.mdx

Examples:

Button: https://heroui.com/docs/native/components/button.mdx
Dialog: https://heroui.com/docs/native/components/dialog.mdx
TextField: https://heroui.com/docs/native/components/text-field.mdx

Getting started guides: https://heroui.com/docs/native/getting-started/{topic}.mdx

Important: Always fetch component docs before implementing. The MDX docs include complete examples, props, anatomy, and API references.

Installation Essentials
Quick Install
npm i heroui-native react-native-reanimated react-native-gesture-handler react-native-safe-area-context @gorhom/bottom-sheet react-native-svg react-native-worklets tailwind-merge tailwind-variants

Framework Setup (Expo - Recommended)
Install dependencies:
npx create-expo-app MyApp
cd MyApp
npm i heroui-native uniwind tailwindcss
npm i react-native-reanimated react-native-gesture-handler react-native-safe-area-context @gorhom/bottom-sheet react-native-svg react-native-worklets tailwind-merge tailwind-variants

Create global.css:
@import "tailwindcss";
@import "uniwind";
@import "heroui-native/styles";

@source "./node_modules/heroui-native/lib";

Wrap app with providers:
import { GestureHandlerRootView } from "react-native-gesture-handler";
import { HeroUINativeProvider } from "heroui-native";
import "./global.css";

export default function Layout() {
	return (
		<GestureHandlerRootView style={{ flex: 1 }}>
			<HeroUINativeProvider>
				<App />
			</HeroUINativeProvider>
		</GestureHandlerRootView>
	);
}

Critical Setup Requirements
Uniwind is Required - HeroUI Native uses Uniwind (Tailwind CSS for React Native)
HeroUINativeProvider Required - Wrap your app with HeroUINativeProvider
GestureHandlerRootView Required - Wrap with GestureHandlerRootView from react-native-gesture-handler
Use Compound Components - Components use compound structure (e.g., Card.Header, Card.Body)
Use onPress, not onClick - React Native uses onPress event handlers
Platform-Specific Code - Use Platform.OS for iOS/Android differences
Component Patterns

HeroUI Native uses compound component patterns. Each component has subcomponents accessed via dot notation.

Example - Card:

<Card>
	<Card.Header>{/* Icons, badges */}</Card.Header>
	<Card.Body>
		<Card.Title>Title</Card.Title>
		<Card.Description>Description</Card.Description>
	</Card.Body>
	<Card.Footer>{/* Actions */}</Card.Footer>
</Card>


Key Points:

Always use compound structure - don't flatten to props
Subcomponents are accessed via dot notation (e.g., Card.Header)
Native Card uses Card.Body (not Card.Content); Title and Description go inside Body
Fetch component docs for complete anatomy and examples
Semantic Variants

HeroUI uses semantic naming to communicate functional intent:

Variant	Purpose	Usage
primary	Main action to move forward	1 per context
secondary	Alternative actions	Multiple
tertiary	Dismissive actions (cancel, skip)	Sparingly
danger	Destructive actions	When needed
danger-soft	Soft destructive actions	Less prominent
ghost	Low-emphasis actions	Minimal weight
outline	Secondary actions	Bordered style

Don't use raw colors - semantic variants adapt to themes and accessibility.

Theming

HeroUI Native uses CSS variables via Tailwind/Uniwind for theming. Theme colors are defined in global.css:

@theme {
	--color-accent: hsl(260, 100%, 70%);
	--color-accent-foreground: hsl(0, 0%, 100%);
}


Get current theme variables:

node scripts/get_theme.mjs


Access theme colors programmatically:

import { useThemeColor } from "heroui-native";

const accentColor = useThemeColor("accent");


Theme switching (Light/Dark Mode):

import { Uniwind, useUniwind } from "uniwind";

const { theme } = useUniwind();
Uniwind.setTheme(theme === "light" ? "dark" : "light");


For detailed theming, fetch: https://heroui.com/docs/native/getting-started/theming.mdx

Weekly Installs
4.7K
Repository
heroui-inc/heroui
GitHub Stars
29.1K
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn