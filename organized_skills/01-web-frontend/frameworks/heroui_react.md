---
rating: ⭐⭐⭐
title: heroui-react
url: https://skills.sh/heroui-inc/heroui/heroui-react
---

# heroui-react

skills/heroui-inc/heroui/heroui-react
heroui-react
Installation
$ npx skills add https://github.com/heroui-inc/heroui --skill heroui-react
Summary

Accessible React component library built on Tailwind CSS v4 and React Aria with compound component patterns.

Provides 20+ pre-built components (Button, Modal, Form, Card, TextField, etc.) using compound composition syntax (Card.Header, Card.Content)
Requires Tailwind CSS v4 and uses CSS variables with oklch color space for theme customization; no provider wrapper needed in v3
Semantic variant system (primary, secondary, tertiary, danger, ghost, outline) for consistent intent-driven styling across components
Currently in beta; fetch component MDX docs from v3.heroui.com/docs/react/components/{name}.mdx for complete props, examples, and anatomy before implementing
SKILL.md
HeroUI v3 React Development Guide

HeroUI v3 is a component library built on Tailwind CSS v4 and React Aria Components, providing accessible, customizable UI components for React applications.

Installation
curl -fsSL https://heroui.com/install | bash -s heroui-react

CRITICAL: v3 Only - Ignore v2 Knowledge

This guide is for HeroUI v3 ONLY. Do NOT apply v2 patterns — the provider, styling, and component API all changed:

Feature	v2 (DO NOT USE)	v3 (USE THIS)
Provider	<HeroUIProvider> required	No Provider needed
Animations	framer-motion package	CSS-based, no extra deps
Component API	Flat props: <Card title="x">	Compound: <Card><Card.Header>
Styling	Tailwind v3 + @heroui/theme	Tailwind v4 + @heroui/styles
Packages	@heroui/system, @heroui/theme	@heroui/react, @heroui/styles
// DO NOT DO THIS - v2 pattern
import { HeroUIProvider } from "@heroui/react";
import { motion } from "framer-motion";

<HeroUIProvider>
	<Card title="Product" description="A great product" />
</HeroUIProvider>;

CORRECT (v3 patterns)
// DO THIS - v3 pattern (no provider, compound components)
import { Card } from "@heroui/react";

<Card>
	<Card.Header>
		<Card.Title>Product</Card.Title>
		<Card.Description>A great product</Card.Description>
	</Card.Header>
</Card>;


Always fetch v3 docs before implementing.

Core Principles
Semantic variants (primary, secondary, tertiary) over visual descriptions
Composition over configuration (compound components)
CSS variable-based theming with oklch color space
BEM naming convention for predictable styling
Accessing Documentation & Component Information

For component details, examples, props, and implementation patterns, always fetch documentation:

Using Scripts
# List all available components
node scripts/list_components.mjs

# Get component documentation (MDX)
node scripts/get_component_docs.mjs Button
node scripts/get_component_docs.mjs Button Card TextField

# Get component source code
node scripts/get_source.mjs Button

# Get component CSS styles (BEM classes)
node scripts/get_styles.mjs Button

# Get theme variables
node scripts/get_theme.mjs

# Get non-component docs (guides, releases)
node scripts/get_docs.mjs /docs/react/getting-started/theming

Direct MDX URLs

Component docs: https://heroui.com/docs/react/components/{component-name}.mdx

Examples:

Button: https://heroui.com/docs/react/components/button.mdx
Modal: https://heroui.com/docs/react/components/modal.mdx
Form: https://heroui.com/docs/react/components/form.mdx

Getting started guides: https://heroui.com/docs/react/getting-started/{topic}.mdx

Important: Always fetch component docs before implementing. The MDX docs include complete examples, props, anatomy, and API references.

Installation Essentials
Quick Install
npm i @heroui/styles @heroui/react tailwind-variants

Framework Setup (Next.js App Router - Recommended)
Install dependencies:
npm i @heroui/styles @heroui/react tailwind-variants tailwindcss @tailwindcss/postcss postcss

Create/update app/globals.css:
/* Tailwind CSS v4 - Must be first */
@import "tailwindcss";

/* HeroUI v3 styles - Must be after Tailwind */
@import "@heroui/styles";

Import in app/layout.tsx:
import "./globals.css";

export default function RootLayout({
	children,
}: {
	children: React.ReactNode;
}) {
	return (
		<html lang="en" suppressHydrationWarning>
			<body>
				{/* No Provider needed in HeroUI v3! */}
				{children}
			</body>
		</html>
	);
}

Configure PostCSS (postcss.config.mjs):
export default {
	plugins: {
		"@tailwindcss/postcss": {},
	},
};

Critical Setup Requirements
Tailwind CSS v4 is MANDATORY - HeroUI v3 will NOT work with Tailwind CSS v3
Use Compound Components - Components use compound structure (e.g., Card.Header, Card.Content)
Use onPress, not onClick - For better accessibility, use onPress event handlers
Import Order Matters - Always import Tailwind CSS before HeroUI styles
Component Patterns

All components use the compound pattern shown above (dot-notation subcomponents like Card.Header, Card.Content). Don't flatten to props — always compose with subcomponents. Fetch component docs for complete anatomy and examples.

Semantic Variants

HeroUI uses semantic naming to communicate functional intent:

Variant	Purpose	Usage
primary	Main action to move forward	1 per context
secondary	Alternative actions	Multiple
tertiary	Dismissive actions (cancel, skip)	Sparingly
danger	Destructive actions	When needed
ghost	Low-emphasis actions	Minimal weight
outline	Secondary actions	Bordered style

Don't use raw colors - semantic variants adapt to themes and accessibility.

Theming

HeroUI v3 uses CSS variables with oklch color space:

:root {
	--accent: oklch(0.6204 0.195 253.83);
	--accent-foreground: var(--snow);
	--background: oklch(0.9702 0 0);
	--foreground: var(--eclipse);
}


Get current theme variables:

node scripts/get_theme.mjs


Color naming:

Without suffix = background (e.g., --accent)
With -foreground = text color (e.g., --accent-foreground)

Theme switching:

<html class="dark" data-theme="dark"></html>


For detailed theming, fetch: https://heroui.com/docs/react/getting-started/theming.mdx

Weekly Installs
4.6K
Repository
heroui-inc/heroui
GitHub Stars
29.1K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn