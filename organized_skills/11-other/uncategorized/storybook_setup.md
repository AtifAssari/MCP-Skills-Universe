---
rating: ⭐⭐⭐⭐⭐
title: storybook-setup
url: https://skills.sh/patricio0312rev/skills/storybook-setup
---

# storybook-setup

skills/patricio0312rev/skills/storybook-setup
storybook-setup
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill storybook-setup
SKILL.md
Storybook Setup

Configure Storybook for comprehensive component documentation and testing.

Core Workflow
Initialize Storybook: Setup with framework
Configure addons: Controls, actions, a11y
Write stories: Document components
Add documentation: MDX pages
Setup testing: Visual regression
Deploy docs: Static hosting
Installation
# Initialize Storybook
npx storybook@latest init

# Or with specific framework
npx storybook@latest init --type react
npx storybook@latest init --type nextjs
npx storybook@latest init --type vue3

Configuration
Main Configuration
// .storybook/main.ts
import type { StorybookConfig } from '@storybook/react-vite';

const config: StorybookConfig = {
  stories: [
    '../src/**/*.mdx',
    '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)',
  ],

  addons: [
    '@storybook/addon-onboarding',
    '@storybook/addon-links',
    '@storybook/addon-essentials',
    '@chromatic-com/storybook',
    '@storybook/addon-interactions',
    '@storybook/addon-a11y',
    '@storybook/addon-designs',
    '@storybook/addon-coverage',
  ],

  framework: {
    name: '@storybook/react-vite',
    options: {},
  },

  docs: {
    autodocs: 'tag',
  },

  staticDirs: ['../public'],

  typescript: {
    reactDocgen: 'react-docgen-typescript',
    reactDocgenTypescriptOptions: {
      shouldExtractLiteralValuesFromEnum: true,
      shouldRemoveUndefinedFromOptional: true,
      propFilter: (prop) =>
        prop.parent ? !/node_modules/.test(prop.parent.fileName) : true,
    },
  },

  viteFinal: async (config) => {
    // Customize Vite config
    return config;
  },
};

export default config;

Preview Configuration
// .storybook/preview.ts
import type { Preview } from '@storybook/react';
import { themes } from '@storybook/theming';
import '../src/styles/globals.css';

const preview: Preview = {
  parameters: {
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/i,
      },
    },
    backgrounds: {
      default: 'light',
      values: [
        { name: 'light', value: '#ffffff' },
        { name: 'dark', value: '#1a1a1a' },
        { name: 'gray', value: '#f5f5f5' },
      ],
    },
    layout: 'centered',
    docs: {
      theme: themes.light,
    },
    a11y: {
      config: {
        rules: [
          { id: 'color-contrast', enabled: true },
          { id: 'label', enabled: true },
        ],
      },
    },
    viewport: {
      viewports: {
        mobile: {
          name: 'Mobile',
          styles: { width: '375px', height: '667px' },
        },
        tablet: {
          name: 'Tablet',
          styles: { width: '768px', height: '1024px' },
        },
        desktop: {
          name: 'Desktop',
          styles: { width: '1440px', height: '900px' },
        },
      },
    },
  },
  globalTypes: {
    theme: {
      description: 'Global theme',
      defaultValue: 'light',
      toolbar: {
        title: 'Theme',
        icon: 'circlehollow',
        items: ['light', 'dark'],
        dynamicTitle: true,
      },
    },
  },
  decorators: [
    (Story, context) => {
      const theme = context.globals.theme;
      return (
        <div className={theme === 'dark' ? 'dark' : ''}>
          <div className="bg-white dark:bg-gray-900 p-4">
            <Story />
          </div>
        </div>
      );
    },
  ],
};

export default preview;

Writing Stories
Component Story Format (CSF3)
// src/components/Button/Button.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { fn } from '@storybook/test';
import { Button } from './Button';

const meta = {
  title: 'Components/Button',
  component: Button,
  parameters: {
    layout: 'centered',
    docs: {
      description: {
        component: 'A versatile button component with multiple variants and sizes.',
      },
    },
  },
  tags: ['autodocs'],
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'outline', 'ghost'],
      description: 'Visual style variant',
      table: {
        type: { summary: 'string' },
        defaultValue: { summary: 'primary' },
      },
    },
    size: {
      control: 'radio',
      options: ['sm', 'md', 'lg'],
      description: 'Button size',
    },
    disabled: {
      control: 'boolean',
      description: 'Disable the button',
    },
    loading: {
      control: 'boolean',
      description: 'Show loading state',
    },
    children: {
      control: 'text',
      description: 'Button content',
    },
  },
  args: {
    onClick: fn(),
    children: 'Button',
  },
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

// Basic stories
export const Primary: Story = {
  args: {
    variant: 'primary',
  },
};

export const Secondary: Story = {
  args: {
    variant: 'secondary',
  },
};

export const Outline: Story = {
  args: {
    variant: 'outline',
  },
};

export const Ghost: Story = {
  args: {
    variant: 'ghost',
  },
};

// Size variants
export const Small: Story = {
  args: {
    size: 'sm',
  },
};

export const Large: Story = {
  args: {
    size: 'lg',
  },
};

// States
export const Disabled: Story = {
  args: {
    disabled: true,
  },
};

export const Loading: Story = {
  args: {
    loading: true,
  },
};

// With icons
export const WithIcon: Story = {
  args: {
    children: (
      <>
        <PlusIcon className="mr-2 h-4 w-4" />
        Add Item
      </>
    ),
  },
};

// All variants showcase
export const AllVariants: Story = {
  render: () => (
    <div className="flex flex-wrap gap-4">
      <Button variant="primary">Primary</Button>
      <Button variant="secondary">Secondary</Button>
      <Button variant="outline">Outline</Button>
      <Button variant="ghost">Ghost</Button>
    </div>
  ),
};

Interactive Stories
// src/components/Form/Form.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { within, userEvent, expect, fn } from '@storybook/test';
import { Form } from './Form';

const meta: Meta<typeof Form> = {
  title: 'Components/Form',
  component: Form,
  args: {
    onSubmit: fn(),
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

export const FilledForm: Story = {
  play: async ({ canvasElement, args }) => {
    const canvas = within(canvasElement);

    // Fill out the form
    const emailInput = canvas.getByLabelText('Email');
    await userEvent.type(emailInput, 'test@example.com', { delay: 50 });

    const passwordInput = canvas.getByLabelText('Password');
    await userEvent.type(passwordInput, 'password123', { delay: 50 });

    // Submit the form
    const submitButton = canvas.getByRole('button', { name: /submit/i });
    await userEvent.click(submitButton);

    // Assert the form was submitted
    await expect(args.onSubmit).toHaveBeenCalled();
  },
};

export const ValidationError: Story = {
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);

    // Submit without filling
    const submitButton = canvas.getByRole('button', { name: /submit/i });
    await userEvent.click(submitButton);

    // Check for error messages
    await expect(canvas.getByText('Email is required')).toBeInTheDocument();
  },
};

MDX Documentation
{/* src/components/Button/Button.mdx */}
import { Meta, Story, Canvas, Controls, ArgTypes } from '@storybook/blocks';
import * as ButtonStories from './Button.stories';
import { Button } from './Button';

<Meta of={ButtonStories} />

# Button

The Button component is used to trigger actions or navigation.

## Import

```tsx
import { Button } from '@/components/Button';

Usage
Variants

Buttons come in four variants to communicate different levels of emphasis.

Primary

Use for primary actions that are the main call to action on a page.

Secondary

Use for secondary actions that complement the primary action.

Outline

Use for tertiary actions or when you want less visual emphasis.

Ghost

Use for navigation or very subtle actions.

Sizes
States
Disabled
Loading
Props
Accessibility
Buttons use the native <button> element
Loading state announces to screen readers
Focus states are clearly visible
Disabled buttons maintain proper ARIA attributes
Design Guidelines
Use descriptive button text
Limit to one primary button per section
Keep button text concise (2-4 words)
Use icons to reinforce meaning, not replace text

## Testing Integration

### Visual Regression with Chromatic

```typescript
// .storybook/main.ts
const config: StorybookConfig = {
  addons: [
    '@chromatic-com/storybook',
  ],
};

// package.json
{
  "scripts": {
    "chromatic": "chromatic --project-token=$CHROMATIC_PROJECT_TOKEN"
  }
}

Test Runner
npm install @storybook/test-runner -D

// .storybook/test-runner.ts
import type { TestRunnerConfig } from '@storybook/test-runner';
import { getStoryContext } from '@storybook/test-runner';
import { injectAxe, checkA11y } from 'axe-playwright';

const config: TestRunnerConfig = {
  async preVisit(page) {
    await injectAxe(page);
  },
  async postVisit(page, context) {
    // Run accessibility tests
    const storyContext = await getStoryContext(page, context);
    if (!storyContext.parameters?.a11y?.disable) {
      await checkA11y(page, '#storybook-root', {
        detailedReport: true,
        detailedReportOptions: { html: true },
      });
    }
  },
};

export default config;

// package.json
{
  "scripts": {
    "test-storybook": "test-storybook",
    "test-storybook:ci": "test-storybook --ci"
  }
}

Design Tokens Integration
// .storybook/preview.ts
import { ThemeProvider } from 'styled-components';
import { theme } from '../src/styles/theme';

const preview: Preview = {
  decorators: [
    (Story) => (
      <ThemeProvider theme={theme}>
        <Story />
      </ThemeProvider>
    ),
  ],
};

// src/styles/theme.ts (document in Storybook)
export const theme = {
  colors: {
    primary: {
      50: '#eff6ff',
      500: '#3b82f6',
      900: '#1e3a8a',
    },
  },
  spacing: {
    xs: '0.25rem',
    sm: '0.5rem',
    md: '1rem',
    lg: '1.5rem',
    xl: '2rem',
  },
  radii: {
    sm: '0.25rem',
    md: '0.375rem',
    lg: '0.5rem',
    full: '9999px',
  },
};

Publishing
Static Export
// package.json
{
  "scripts": {
    "build-storybook": "storybook build",
    "storybook:serve": "npx http-server storybook-static"
  }
}

GitHub Pages
# .github/workflows/storybook.yml
name: Deploy Storybook

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - run: npm ci
      - run: npm run build-storybook

      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./storybook-static

Best Practices
One component per file: Clear organization
Use autodocs: Generate documentation
Add controls: Interactive exploration
Include a11y addon: Accessibility testing
Write play functions: Interactive tests
Document with MDX: Rich documentation
Use decorators: Consistent context
Visual regression: Catch UI changes
Output Checklist

Every Storybook setup should include:

 Main configuration with addons
 Preview with global decorators
 Stories in CSF3 format
 Autodocs enabled
 Controls for all props
 Accessibility addon
 Dark mode support
 Viewport presets
 MDX documentation
 Test runner setup
 CI deployment
 Static build script
Weekly Installs
135
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass