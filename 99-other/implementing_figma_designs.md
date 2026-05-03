---
title: implementing-figma-designs
url: https://skills.sh/onekeyhq/app-monorepo/implementing-figma-designs
---

# implementing-figma-designs

skills/onekeyhq/app-monorepo/implementing-figma-designs
implementing-figma-designs
Installation
$ npx skills add https://github.com/onekeyhq/app-monorepo --skill implementing-figma-designs
SKILL.md
Implementing Figma Designs

This skill helps you implement Figma designs 1:1 using the OneKey component library.

Core Principles
Focus on UI First, Data Later

When implementing Figma designs, prioritize pixel-perfect UI over data integration:

Use mock data - Hardcode data that matches the design exactly
Skip i18n - Use plain strings directly from the design, no intl.formatMessage
Skip API calls - No need to fetch real data at this stage
Match the design - Focus on visual accuracy, spacing, colors, and layout
What NOT to do
Don't worry about where data comes from
Don't add translation keys (ETranslations)
Don't create API integration or hooks for fetching
Don't add complex state management
What TO do
Hardcode text exactly as shown in Figma
Create mock data arrays/objects that match the design
Focus on component structure and styling
Match spacing, colors, and typography from design
Component Lookup (On-Demand)

When you need to use a component, look up its source and demo:

Source Code Location Pattern
packages/components/src/{category}/{ComponentName}/


Categories:

primitives/ - Button, Icon, Image, Skeleton, Spinner, Stack, Heading, SizeableText
forms/ - Input, TextArea, Select, Checkbox, Radio, Switch, Slider, Form, OTPInput
actions/ - IconButton, ActionList, Alert, Toast, Popover, SegmentControl, Pagination, Tooltip
composite/ - Dialog, Tabs, Banner, Carousel, Table, Stepper
content/ - Badge, Progress, Empty, Divider, QRCode, Markdown, LottieView, LinearGradient, BlurView
layouts/ - Page, ScrollView, ListView, SectionList, Accordion, Swiper, SearchBar
Demo Location Pattern
packages/kit/src/views/Developer/pages/Gallery/Components/stories/{ComponentName}.tsx


Note: Some demos have different names (e.g., AccordionGallery.tsx, NewTabsGallery.tsx)

How to Look Up a Component

Read the source to understand props and structure:

Read: packages/components/src/{category}/{ComponentName}/index.tsx


Read the demo for usage examples:

Glob: packages/kit/src/views/Developer/pages/Gallery/Components/stories/*{ComponentName}*.tsx

Quick Reference
All imports from @onekeyhq/components
import { Button, Stack, XStack, YStack, Icon, ... } from '@onekeyhq/components';

Spacing Tokens
$1 = 4px, $2 = 8px, $3 = 12px, $4 = 16px
$5 = 20px, $6 = 24px, $8 = 32px, $10 = 40px
Color Tokens
Text: $text, $textSubdued, $textDisabled
Background: $bg, $bgSubdued, $bgHover, $bgActive
Border: $border, $borderSubdued, $borderActive
Icon: $icon, $iconSubdued, $iconDisabled
Font Size Tokens

Headings (large to small):

$headingXxl, $headingXl, $headingLg, $headingMd, $headingSm, $headingXs

Body text (large to small):

$bodyLg, $bodyMd, $bodySm, $bodyXs

With medium weight (append Medium):

$bodyLgMedium, $bodyMdMedium, $bodySmMedium, $bodyXsMedium

Usage with SizableText:

<SizableText size="$bodyMd">Regular text</SizableText>
<SizableText size="$bodyMdMedium">Medium weight text</SizableText>
<SizableText size="$headingSm">Small heading</SizableText>

Common Patterns

Layout with Stack:

<YStack gap="$4">        {/* Vertical */}
<XStack gap="$4">        {/* Horizontal */}
<Stack gap="$4">         {/* Default vertical */}


Mock Data:

const mockItems = [
  { name: 'Bitcoin', symbol: 'BTC', value: '$21,432.50' },
  { name: 'Ethereum', symbol: 'ETH', value: '$5,892.30' },
];


Button Actions:

<Button onPress={() => console.log('clicked')}>Action</Button>

Workflow
Analyze the Figma design using Figma MCP
Identify which components are needed
Look up each component - read source and demo on-demand
Create mock data matching the design
Implement the UI with hardcoded values
Weekly Installs
77
Repository
onekeyhq/app-monorepo
GitHub Stars
2.4K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass