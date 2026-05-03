---
title: storybook-story-writing
url: https://skills.sh/thebushidocollective/han/storybook-story-writing
---

# storybook-story-writing

skills/thebushidocollective/han/storybook-story-writing
storybook-story-writing
Installation
$ npx skills add https://github.com/thebushidocollective/han --skill storybook-story-writing
Summary

CSF3-compliant Storybook stories that showcase component variations with type safety and consistent structure.

Enforces Component Story Format 3 with TypeScript type annotations, default meta exports, and story object syntax
Covers story organization patterns for buttons, forms, layouts, data-driven components, and responsive designs
Includes best practices for extending stories, using decorators for context, and adding descriptive parameters for documentation
Identifies anti-patterns like CSF2 template binding, hardcoded repetitive props, and logic mixing to avoid common mistakes
SKILL.md
Storybook - Story Writing

Write well-structured, maintainable Storybook stories using Component Story Format 3 (CSF3) that showcase component variations and ensure consistent rendering.

Key Concepts
Component Story Format 3 (CSF3)

CSF3 is the modern Storybook format that uses object syntax for stories:

import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta = {
  title: 'Components/Button',
  component: Button,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
    backgroundColor: { control: 'color' },
  },
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
  args: {
    primary: true,
    label: 'Button',
  },
};

export const Secondary: Story = {
  args: {
    label: 'Button',
  },
};

Story Organization
One story file per component: Component.stories.tsx
Use descriptive story names: Primary, Secondary, Large, Disabled
Group related stories under a title hierarchy: Components/Forms/Input
Default Export (Meta)

The default export defines metadata for all stories:

const meta = {
  title: 'Components/Button',        // Navigation path
  component: Button,                  // Component reference
  parameters: {},                     // Story-level config
  tags: ['autodocs'],                // Enable auto-documentation
  argTypes: {},                       // Control types
  decorators: [],                     // Wrappers for stories
} satisfies Meta<typeof Button>;

Best Practices
1. Use TypeScript for Type Safety
import type { Meta, StoryObj } from '@storybook/react';

const meta = {
  component: Button,
} satisfies Meta<typeof Button>;

type Story = StoryObj<typeof meta>;

2. Show All Component States

Create stories for each meaningful state:

export const Default: Story = {
  args: {
    label: 'Click me',
  },
};

export const Loading: Story = {
  args: {
    label: 'Loading...',
    loading: true,
  },
};

export const Disabled: Story = {
  args: {
    label: 'Disabled',
    disabled: true,
  },
};

export const WithIcon: Story = {
  args: {
    label: 'Download',
    icon: 'download',
  },
};

3. Use Sensible Defaults
export const Primary: Story = {
  args: {
    primary: true,
    label: 'Button',
    size: 'medium',
  },
};

// Extend existing stories
export const PrimaryLarge: Story = {
  ...Primary,
  args: {
    ...Primary.args,
    size: 'large',
  },
};

4. Add Descriptive Parameters
export const WithTooltip: Story = {
  args: {
    label: 'Hover me',
    tooltip: 'Click to submit',
  },
  parameters: {
    docs: {
      description: {
        story: 'Shows a tooltip on hover to provide additional context.',
      },
    },
  },
};

5. Use Decorators for Context
import { RouterDecorator } from '../decorators';

const meta = {
  component: Navigation,
  decorators: [
    (Story) => (
      <div style={{ padding: '3rem' }}>
        <Story />
      </div>
    ),
    RouterDecorator,
  ],
} satisfies Meta<typeof Navigation>;

Common Patterns
Form Components
export const EmptyForm: Story = {
  args: {
    onSubmit: (data) => console.log(data),
  },
};

export const PrefilledForm: Story = {
  args: {
    defaultValues: {
      email: 'user@example.com',
      name: 'John Doe',
    },
  },
};

export const WithValidationErrors: Story = {
  args: {
    errors: {
      email: 'Invalid email format',
      name: 'Name is required',
    },
  },
};

Layout Components
export const WithSidebar: Story = {
  args: {
    sidebar: <Sidebar items={sidebarItems} />,
    children: <Content />,
  },
  parameters: {
    layout: 'fullscreen',
  },
};

Data-Driven Components
const mockData = [
  { id: 1, name: 'Item 1' },
  { id: 2, name: 'Item 2' },
  { id: 3, name: 'Item 3' },
];

export const WithData: Story = {
  args: {
    items: mockData,
  },
};

export const Empty: Story = {
  args: {
    items: [],
    emptyMessage: 'No items found',
  },
};

Responsive Components
export const Mobile: Story = {
  args: {
    variant: 'mobile',
  },
  parameters: {
    viewport: {
      defaultViewport: 'mobile1',
    },
  },
};

export const Desktop: Story = {
  args: {
    variant: 'desktop',
  },
  parameters: {
    viewport: {
      defaultViewport: 'desktop',
    },
  },
};

Anti-Patterns
❌ Don't Use Template Binding (CSF2)
// Bad - Old CSF2 format
const Template = (args) => <Button {...args} />;
export const Primary = Template.bind({});
Primary.args = { label: 'Button' };

// Good - CSF3 format
export const Primary: Story = {
  args: { label: 'Button' },
};

❌ Don't Mix Logic in Stories
// Bad
export const Complex: Story = {
  render: (args) => {
    const [state, setState] = useState(false);
    useEffect(() => {
      // Complex side effects
    }, []);
    return <Component {...args} />;
  },
};

// Good - Move logic to component or use play functions
export const Complex: Story = {
  args: { initialState: false },
};

❌ Don't Hardcode Repetitive Props
// Bad
export const Story1: Story = {
  args: { label: 'Button', size: 'medium', theme: 'light' },
};
export const Story2: Story = {
  args: { label: 'Submit', size: 'medium', theme: 'light' },
};

// Good - Use meta-level defaults
const meta = {
  component: Button,
  args: {
    size: 'medium',
    theme: 'light',
  },
} satisfies Meta<typeof Button>;

export const Story1: Story = {
  args: { label: 'Button' },
};
export const Story2: Story = {
  args: { label: 'Submit' },
};

❌ Don't Skip Story Types
// Bad - Missing type annotation
export const Primary = {
  args: { label: 'Button' },
};

// Good - With type
export const Primary: Story = {
  args: { label: 'Button' },
};

Related Skills
storybook-args-controls: Advanced arg configuration and interactive controls
storybook-play-functions: Automated interaction testing within stories
storybook-component-documentation: Auto-generating component documentation
Weekly Installs
446
Repository
thebushidocollective/han
GitHub Stars
145
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass