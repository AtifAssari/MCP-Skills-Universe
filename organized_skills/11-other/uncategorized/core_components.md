---
rating: ⭐⭐⭐
title: core-components
url: https://skills.sh/sickn33/antigravity-awesome-skills/core-components
---

# core-components

skills/sickn33/antigravity-awesome-skills/core-components
core-components
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill core-components
SKILL.md
Core Components
Design System Overview

Use components from your core library instead of raw platform components. This ensures consistent styling and behavior.

Design Tokens

NEVER hard-code values. Always use design tokens.

Spacing Tokens
// CORRECT - Use tokens
<Box padding="$4" marginBottom="$2" />

// WRONG - Hard-coded values
<Box padding={16} marginBottom={8} />

Token	Value
$1	4px
$2	8px
$3	12px
$4	16px
$6	24px
$8	32px
Color Tokens
// CORRECT - Semantic tokens
<Text color="$textPrimary" />
<Box backgroundColor="$backgroundSecondary" />

// WRONG - Hard-coded colors
<Text color="#333333" />
<Box backgroundColor="rgb(245, 245, 245)" />

Semantic Token	Use For
$textPrimary	Main text
$textSecondary	Supporting text
$textTertiary	Disabled/hint text
$primary500	Brand/accent color
$statusError	Error states
$statusSuccess	Success states
Typography Tokens
<Text fontSize="$lg" fontWeight="$semibold" />

Token	Size
$xs	12px
$sm	14px
$md	16px
$lg	18px
$xl	20px
$2xl	24px
Core Components
Box

Base layout component with token support:

<Box
  padding="$4"
  backgroundColor="$backgroundPrimary"
  borderRadius="$lg"
>
  {children}
</Box>

HStack / VStack

Horizontal and vertical flex layouts:

<HStack gap="$3" alignItems="center">
  <Icon name="user" />
  <Text>Username</Text>
</HStack>

<VStack gap="$4" padding="$4">
  <Heading>Title</Heading>
  <Text>Content</Text>
</VStack>

Text

Typography with token support:

<Text
  fontSize="$lg"
  fontWeight="$semibold"
  color="$textPrimary"
>
  Hello World
</Text>

Button

Interactive button with variants:

<Button
  onPress={handlePress}
  variant="solid"
  size="md"
  isLoading={loading}
  isDisabled={disabled}
>
  Click Me
</Button>

Variant	Use For
solid	Primary actions
outline	Secondary actions
ghost	Tertiary/subtle actions
link	Inline actions
Input

Form input with validation:

<Input
  value={value}
  onChangeText={setValue}
  placeholder="Enter text"
  error={touched ? errors.field : undefined}
  label="Field Name"
/>

Card

Content container:

<Card padding="$4" gap="$3">
  <CardHeader>
    <Heading size="sm">Card Title</Heading>
  </CardHeader>
  <CardBody>
    <Text>Card content</Text>
  </CardBody>
</Card>

Layout Patterns
Screen Layout
const MyScreen = () => (
  <Screen>
    <ScreenHeader title="Page Title" />
    <ScreenContent padding="$4">
      {/* Content */}
    </ScreenContent>
  </Screen>
);

Form Layout
<VStack gap="$4" padding="$4">
  <Input label="Name" {...nameProps} />
  <Input label="Email" {...emailProps} />
  <Button isLoading={loading}>Submit</Button>
</VStack>

List Item Layout
<HStack
  padding="$4"
  gap="$3"
  alignItems="center"
  borderBottomWidth={1}
  borderColor="$borderLight"
>
  <Avatar source={{ uri: imageUrl }} size="md" />
  <VStack flex={1}>
    <Text fontWeight="$semibold">{title}</Text>
    <Text color="$textSecondary" fontSize="$sm">{subtitle}</Text>
  </VStack>
  <Icon name="chevron-right" color="$textTertiary" />
</HStack>

Anti-Patterns
// WRONG - Hard-coded values
<View style={{ padding: 16, backgroundColor: '#fff' }}>

// CORRECT - Design tokens
<Box padding="$4" backgroundColor="$backgroundPrimary">


// WRONG - Raw platform components
import { View, Text } from 'react-native';

// CORRECT - Core components
import { Box, Text } from 'components/core';


// WRONG - Inline styles
<Text style={{ fontSize: 18, fontWeight: '600' }}>

// CORRECT - Token props
<Text fontSize="$lg" fontWeight="$semibold">

Component Props Pattern

When creating components, use token-based props:

interface CardProps {
  padding?: '$2' | '$4' | '$6';
  variant?: 'elevated' | 'outlined' | 'filled';
  children: React.ReactNode;
}

const Card = ({ padding = '$4', variant = 'elevated', children }: CardProps) => (
  <Box
    padding={padding}
    backgroundColor="$backgroundPrimary"
    borderRadius="$lg"
    {...variantStyles[variant]}
  >
    {children}
  </Box>
);

Integration with Other Skills
react-ui-patterns: Use core components for UI states
testing-patterns: Mock core components in tests
storybook: Document component variants
When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
431
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass