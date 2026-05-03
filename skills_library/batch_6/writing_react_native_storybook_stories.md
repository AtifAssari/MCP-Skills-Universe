---
title: writing-react-native-storybook-stories
url: https://skills.sh/storybookjs/react-native/writing-react-native-storybook-stories
---

# writing-react-native-storybook-stories

skills/storybookjs/react-native/writing-react-native-storybook-stories
writing-react-native-storybook-stories
Installation
$ npx skills add https://github.com/storybookjs/react-native --skill writing-react-native-storybook-stories
SKILL.md
React Native Storybook Stories

Write stories for React Native components using @storybook/react-native v10 and Component Story Format (CSF).

Quick Start

Minimal story file:

import type { Meta, StoryObj } from '@storybook/react-native';
import { MyComponent } from './MyComponent';

const meta = {
  component: MyComponent,
} satisfies Meta<typeof MyComponent>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Basic: Story = {
  args: {
    label: 'Hello',
  },
};

File Conventions
Name: ComponentName.stories.tsx colocated with the component
Import Meta and StoryObj from @storybook/react-native
Default export: meta object with satisfies Meta<typeof Component>
Named exports: UpperCamelCase story names, typed as StoryObj<typeof meta>
Use args for props, argTypes for control config, parameters for addon config
Use render for custom render functions, decorators for wrappers
Story Patterns
Multiple stories with shared args
export const Primary: Story = {
  args: { variant: 'primary', title: 'Click me' },
};

export const Secondary: Story = {
  args: { ...Primary.args, variant: 'secondary' },
};

Custom render function
export const WithScrollView: Story = {
  render: (args) => (
    <ScrollView>
      <MyComponent {...args} />
    </ScrollView>
  ),
};

Render with hooks (must be a named function)
export const Interactive: Story = {
  render: function InteractiveRender() {
    const [count, setCount] = useReducer((s) => s + 1, 0);
    return <Counter count={count} onPress={setCount} />;
  },
};

Actions (mock callbacks)
import { fn } from 'storybook/test';

const meta = {
  component: Button,
  args: { onPress: fn() },
} satisfies Meta<typeof Button>;


Or via argTypes:

argTypes: { onPress: { action: 'pressed' } },

Custom story name
export const MyStory: Story = {
  storyName: 'Custom Display Name',
  args: { label: 'Hello' },
};

Custom title / nesting
const meta = {
  title: 'NestingExample/Message/Bubble',
  component: MyComponent,
} satisfies Meta<typeof MyComponent>;

Controls & ArgTypes

For the full control type reference, see references/controls.md.

Common patterns:

const meta = {
  component: MyComponent,
  argTypes: {
    // Select dropdown
    size: {
      options: ['small', 'medium', 'large'],
      control: { type: 'select' },
    },
    // Range slider
    opacity: {
      control: { type: 'range', min: 0, max: 1, step: 0.1 },
    },
    // Color picker
    color: { control: { type: 'color' } },
    // Conditional control (shows only when `advanced` arg is true)
    padding: { control: 'number', if: { arg: 'advanced' } },
  },
} satisfies Meta<typeof MyComponent>;


Auto-detection: TypeScript prop types are automatically mapped to controls (string -> text, boolean -> boolean, union types -> select, number -> number).

Parameters
Addon parameters
parameters: {
  // Markdown docs in the Notes addon tab
  notes: `# MyComponent\nUsage: \`<MyComponent label="hi" />\``,
  // Background options for Backgrounds addon
  backgrounds: {
    default: 'dark',
    values: [
      { name: 'light', value: 'white' },
      { name: 'dark', value: '#333' },
    ],
  },
},

RN-specific UI parameters
Parameter	Type	Description
noSafeArea	boolean	Remove top safe area padding. When using this, the component itself must handle safe areas since Storybook will no longer provide safe area padding. Prefer useSafeAreaInsets() over SafeAreaView — apply insets as paddingTop/paddingBottom on the container, and for scrollable content use contentContainerStyle padding instead of wrapping in SafeAreaView.
storybookUIVisibility	'visible' | 'hidden'	Initial UI visibility
hideFullScreenButton	boolean	Hide fullscreen toggle
layout	'padded' | 'centered' | 'fullscreen'	Story container layout

Parameters can be set at story, meta (component), or global (preview.tsx) level.

Decorators

Wrap stories in providers, layouts, or context:

const meta = {
  component: MyComponent,
  decorators: [
    (Story) => (
      <View style={{ alignItems: 'center', justifyContent: 'center', flex: 1 }}>
        <Story />
      </View>
    ),
  ],
} satisfies Meta<typeof MyComponent>;


Global decorators go in .rnstorybook/preview.tsx:

import { withBackgrounds } from '@storybook/addon-ondevice-backgrounds';
import type { Preview } from '@storybook/react-native';

const preview: Preview = {
  decorators: [withBackgrounds],
  parameters: {
    actions: { argTypesRegex: '^on[A-Z].*' },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/,
      },
    },
    backgrounds: {
      default: 'plain',
      values: [
        { name: 'plain', value: 'white' },
        { name: 'dark', value: '#333' },
      ],
    },
  },
};

export default preview;

Configuration
.rnstorybook/main.ts
import type { StorybookConfig } from '@storybook/react-native';

const main: StorybookConfig = {
  stories: ['../components/**/*.stories.?(ts|tsx|js|jsx)'],
  addons: [
    '@storybook/addon-ondevice-controls',
    '@storybook/addon-ondevice-backgrounds',
    '@storybook/addon-ondevice-actions',
    '@storybook/addon-ondevice-notes',
  ],
  framework: '@storybook/react-native',
};

export default main;


Story globs also support the object form for multi-directory setups:

stories: [
  '../components/**/*.stories.?(ts|tsx|js|jsx)',
  { directory: '../other_components', files: '**/*.stories.?(ts|tsx|js|jsx)' },
],

Portable Stories (Testing)

Reuse stories in Jest tests:

import { render, screen } from '@testing-library/react-native';
import { composeStories } from '@storybook/react';
import * as stories from './Button.stories';

const { Primary, Secondary } = composeStories(stories);

test('renders primary button', () => {
  render(<Primary />);
  expect(screen.getByText('Click me')).toBeTruthy();
});

// Override args in tests
test('renders with custom props', () => {
  render(<Primary title="Custom" />);
  expect(screen.getByText('Custom')).toBeTruthy();
});


For single stories use composeStory:

import { composeStory } from '@storybook/react';
import meta, { Primary } from './Button.stories';

const PrimaryStory = composeStory(Primary, meta);


Setup global annotations for tests in a Jest setup file:

// setup-portable-stories.ts
import { setProjectAnnotations } from '@storybook/react';
import * as previewAnnotations from '../.rnstorybook/preview';
setProjectAnnotations(previewAnnotations);

Addons Summary
Addon	Package	Purpose
Controls	@storybook/addon-ondevice-controls	Edit props interactively
Actions	@storybook/addon-ondevice-actions	Log component interactions
Backgrounds	@storybook/addon-ondevice-backgrounds	Change story backgrounds
Notes	@storybook/addon-ondevice-notes	Add markdown documentation
Weekly Installs
261
Repository
storybookjs/react-native
GitHub Stars
1.3K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass