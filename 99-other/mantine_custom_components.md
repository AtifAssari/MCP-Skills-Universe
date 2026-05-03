---
rating: ⭐⭐
title: mantine-custom-components
url: https://skills.sh/mantinedev/skills/mantine-custom-components
---

# mantine-custom-components

skills/mantinedev/skills/mantine-custom-components
mantine-custom-components
Installation
$ npx skills add https://github.com/mantinedev/skills --skill mantine-custom-components
SKILL.md
Mantine Custom Components Skill
Component template
import {
  Box, BoxProps, createVarsResolver, ElementProps,
  factory, Factory, getRadius, MantineRadius,
  StylesApiProps, useProps, useStyles,
} from '@mantine/core';
import classes from './MyComponent.module.css';

export type MyComponentStylesNames = 'root' | 'inner';
export type MyComponentVariant = 'filled' | 'outline';
export type MyComponentCssVariables = { root: '--my-radius' };

export interface MyComponentProps
  extends BoxProps, StylesApiProps<MyComponentFactory>, ElementProps<'div'> {
  radius?: MantineRadius;
}

export type MyComponentFactory = Factory<{
  props: MyComponentProps;
  ref: HTMLDivElement;
  stylesNames: MyComponentStylesNames;
  vars: MyComponentCssVariables;
  variant: MyComponentVariant;
}>;

const defaultProps = { radius: 'md' } satisfies Partial<MyComponentProps>;

const varsResolver = createVarsResolver<MyComponentFactory>((_theme, { radius }) => ({
  root: { '--my-radius': getRadius(radius) },
}));

export const MyComponent = factory<MyComponentFactory>((_props) => {
  const props = useProps('MyComponent', defaultProps, _props);
  const { classNames, className, style, styles, unstyled, vars, attributes, radius, ...others } = props;

  const getStyles = useStyles<MyComponentFactory>({
    name: 'MyComponent', classes, props,
    className, style, classNames, styles, unstyled, vars, attributes, varsResolver,
  });

  return <Box {...getStyles('root')} {...others} />;
});

MyComponent.displayName = '@mantine/core/MyComponent';
MyComponent.classes = classes;

Factory variant — which to use
Scenario	Factory function	Type
Standard component	factory()	Factory<{}>
Supports component prop (polymorphic)	polymorphicFactory()	PolymorphicFactory<{}> — add defaultComponent and defaultRef
Props change based on a generic (e.g. multiple)	genericFactory()	Factory<{ signature: ... }>

Use polymorphicFactory sparingly — it adds TypeScript overhead and slows IDE autocomplete.

Factory type fields
Factory<{
  props: MyComponentProps;       // required
  ref: HTMLDivElement;           // element type for the forwarded ref
  stylesNames: 'root' | 'inner'; // union of Styles API selectors
  vars: { root: '--my-var' };    // CSS variable map per selector
  variant: 'filled' | 'outline'; // accepted variant strings
  staticComponents: {            // sub-components (compound pattern)
    Item: typeof MyComponentItem;
  };
  compound?: boolean;            // true = sub-component; disables theme classNames/styles/vars
  ctx?: MyContextType;           // passed to styles/vars resolvers as third arg
  signature?: (...) => JSX.Element; // only for genericFactory
}>

Theme integration

Users and the theme can override defaults via Component.extend():

const theme = createTheme({
  components: {
    MyComponent: MyComponent.extend({
      defaultProps: { radius: 'xl' },
      classNames: { root: 'my-root' },
      styles: { root: { color: 'red' } },
      vars: (_theme, props) => ({ root: { '--my-radius': getRadius(props.radius) } }),
    }),
  },
});

References
references/api.md — All imports: factory, useProps, useStyles, createVarsResolver, createSafeContext, StylesApiProps, CompoundStylesApiProps, BoxProps, ElementProps, theme helpers (getSize, getRadius, etc.)
references/patterns.md — Full examples: compound components with context, polymorphic component, generic component, theme integration
Weekly Installs
587
Repository
mantinedev/skills
GitHub Stars
40
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass