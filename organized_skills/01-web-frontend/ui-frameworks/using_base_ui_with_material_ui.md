---
rating: ⭐⭐
title: using-base-ui-with-material-ui
url: https://skills.sh/siriwatknp/mui-treasury/using-base-ui-with-material-ui
---

# using-base-ui-with-material-ui

skills/siriwatknp/mui-treasury/using-base-ui-with-material-ui
using-base-ui-with-material-ui
Installation
$ npx skills add https://github.com/siriwatknp/mui-treasury --skill using-base-ui-with-material-ui
SKILL.md

Announce on start: You must announce "Using Base UI with Material UI skill" when this skill is invoked.

Always have enough context from the Base UI documentation to build the component requested by the user.

Base UI as the foundation

Render Base UI components as a foundation for the UI and then pass render prop using proper Material UI components.

For example, a Navigation Menu, should use Link from Material UI as the render element for NavigationMenu.Link.:

import { NavigationMenu } from '@base-ui-components/react/navigation-menu';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';

function MenuLink({
  icon,
  title,
  description,
  ...props
}: NavigationMenu.Link.Props & {
  icon?: React.ReactNode;
  title: string;
  description: string;
}) {
  return (
    <NavigationMenu.Link
      href="#"
      {...props}
      render={
        <Link
          underline="none"
          sx={{
            display: 'flex',
            gap: 1,
            p: 1.5,
            borderRadius: 0.5,
            cursor: 'pointer',
            transition: 'background-color 0.2s',
            '@media (hover: hover)': {
              '&:hover': {
                bgcolor: 'action.hover',
              },
            },
          }}
        />
      }
    >
      <Box sx={{ color: 'primary.main', display: 'flex', mt: 0.25 }}>
        {icon}
      </Box>
      <Box>
        <Typography variant="subtitle2" sx={{ fontWeight: 600, mb: 0.25 }}>
          {title}
        </Typography>
        <Typography
          variant="body2"
          sx={{ color: 'text.secondary', lineHeight: 1.4 }}
        >
          {description}
        </Typography>
      </Box>
    </NavigationMenu.Link>
  );
}


For full example, see nav-menu-01.tsx

Another example, using Button from Material UI as the render element for Base UI Trigger component:

import { Menu } from '@base-ui-components/react/menu';
import Button from '@mui/material/Button';

<Menu.Trigger render={<Button />}>File</Menu.Trigger>;

Styling

To style Base UI components, use <Box /> as a render element and pass sx prop to it. Always keep in mind that the sx values should be minimum since Material UI components already have default styling.

import { NavigationMenu } from '@base-ui-components/react/navigation-menu';
import Box from '@mui/material/Box';

<NavigationMenu.List
  render={
    <Box
      component="ul"
      sx={{
        display: 'flex',
        justifyContent: 'center',
        gap: 2,
        listStyle: 'none',
        '& .MuiButton-root[data-popup-open]': {
          bgcolor: 'action.selected',
        },
      }}
    />
  }
></NavigationMenu.List>;

Primitive/Non-interactive Components

For non-interactive Base UI components like Meter, Progress, Slider (read-only), etc. that don't have direct semantic Material UI equivalents, always use the render prop pattern with Box.

CRITICAL: Never use component={BaseUIComponent} - this is incorrect and causes issues. Always use Base UI components as the foundation with the render prop.

✅ Correct Pattern
import { Meter } from '@base-ui-components/react/meter';
import Box from '@mui/material/Box';

<Meter.Track
  render={
    <Box
      sx={{
        height: 8,
        width: '100%',
        bgcolor: 'action.disabledBackground',
        borderRadius: 1,
        overflow: 'hidden',
        position: 'relative',
      }}
    />
  }
>
  <Meter.Indicator
    render={
      <Box
        sx={{
          height: '100%',
          bgcolor: 'text.primary',
          transition: 'width 0.3s ease',
        }}
      />
    }
  />
</Meter.Track>;

❌ Incorrect Pattern
// ❌ NEVER do this - Base UI should be the foundation, not MUI Box
<Box component={Meter.Track} sx={{ ... }}>
  <Box component={Meter.Indicator} sx={{ ... }} />
</Box>

// ❌ NEVER do this - Using asChild prop (not a React pattern)
<Meter.Track asChild>
  <Box sx={{ ... }}>
    <Meter.Indicator asChild>
      <Box sx={{ ... }} />
    </Meter.Indicator>
  </Box>
</Meter.Track>

Key Points
Base UI First: Always render Base UI components as the outer wrapper
render Prop: Use render={<Box sx={{ ... }} />} to apply Material UI styling
Theme Tokens: Use MUI theme tokens in sx prop (e.g., bgcolor: "action.hover", color: "text.primary")
Minimal Styling: Keep sx props minimal - only add what's necessary for the design
Reduce duplication

If the same styles are used multiple times for the same Base UI components, create wrapper components to reduce duplication.

import { NavigationMenu } from '@base-ui-components/react/navigation-menu';

function Content(props: BoxProps) {
  return (
    <Box
      sx={{
        padding: 1,
        width: 'calc(100vw - 40px)',
        height: '100%',
        '@media (min-width: 500px)': {
          width: 'max-content',
          minWidth: '400px',
        },
      }}
      {...props}
    />
  );
}

<NavigationMenu.List>
  <NavigationMenu.Item>
    <NavigationMenu.Content render={<Content />}></NavigationMenu.Content>
  </NavigationMenu.Item>
  <NavigationMenu.Item>
    <NavigationMenu.Content render={<Content />}></NavigationMenu.Content>
  </NavigationMenu.Item>
  <NavigationMenu.Item>
    <NavigationMenu.Content render={<Content />}></NavigationMenu.Content>
  </NavigationMenu.Item>
</NavigationMenu.List>;

TypeScript Props Interface

CRITICAL: When creating wrapper components around Base UI primitives, NEVER duplicate props that are already provided by the Base UI component.

❌ Incorrect - Duplicating Base UI Props
import { PreviewCard } from '@base-ui-components/react/preview-card';

// ❌ BAD: Manually duplicating delay, closeDelay, defaultOpen, etc.
export interface CardPreview01Props {
  trigger: React.ReactNode;
  href: string;
  delay?: number; // Already in PreviewCard.Root.Props
  closeDelay?: number; // Already in PreviewCard.Root.Props
  defaultOpen?: boolean; // Already in PreviewCard.Root.Props
  open?: boolean; // Already in PreviewCard.Root.Props
  onOpenChange?: (open: boolean) => void; // Already in PreviewCard.Root.Props
}

✅ Correct - Extending Base UI Props
import { PreviewCard } from '@base-ui-components/react/preview-card';

// ✅ GOOD: Extend the Base UI component props
export interface CardPreview01Props extends PreviewCard.Root.Props {
  trigger: React.ReactNode;
  href: string;
  imageSrc: string;
  imageAlt: string;
  heading: string;
  description: string;
}

export function CardPreview01({
  trigger,
  href,
  imageSrc,
  imageAlt,
  heading,
  description,
  ...props // This spreads all Base UI props (delay, closeDelay, defaultOpen, etc.)
}: CardPreview01Props) {
  return (
    <PreviewCard.Root {...props}>{/* component content */}</PreviewCard.Root>
  );
}

Key Benefits
Type Safety: Automatically get all Base UI prop types without manual maintenance
Future-Proof: New Base UI props automatically available in your component
No Duplication: Single source of truth for prop definitions
Better DX: TypeScript autocomplete shows all available props
When to Define Custom Props

Only define props that are:

Specific to your wrapper component (like imageSrc, heading)
Not part of the underlying Base UI component
Required for your custom implementation logic
Weekly Installs
28
Repository
siriwatknp/mui-treasury
GitHub Stars
2.4K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn