---
title: react-spectrum-s2
url: https://skills.sh/site/react-spectrum.adobe.com/react-spectrum-s2
---

# react-spectrum-s2

skills/react-spectrum.adobe.com/react-spectrum-s2
react-spectrum-s2
$ npx skills add https://react-spectrum.adobe.com
SKILL.md
React Spectrum S2 (Spectrum 2)

React Spectrum S2 is Adobe's implementation of the Spectrum 2 design system in React. It provides a collection of accessible, adaptive, and high-quality UI components.

If the requirements do not clearly specify which React Spectrum component to use, consult the Component Decision Tree before choosing a component.

Styling

Use React Spectrum S2 components and the S2 style macro as the default styling approach.

Import the style macro using the {type: 'macro'} import attribute: import {style} from '@react-spectrum/s2/style' with {type: 'macro'};
Remember that the style macro runs at build time and returns class names.
Avoid introducing Tailwind, radix-ui, shadcn/ui, or any other third-party design system components in S2 implementations.
Prefer S2 components first, and use their styles prop only for the supported layout-style properties.
For generic layouts (flex, grid, etc.), use native HTML elements with the style macro.
For card-style layouts, use the S2 Card component instead of building something custom.
IMPORTANT: Avoid using the UNSAFE_style and UNSAFE_className props.

For React Spectrum components, the styles prop is intentionally limited. Supported properties are:

margin, marginStart, marginEnd, marginTop, marginBottom, marginX, marginY
width, minWidth, maxWidth
flexGrow, flexShrink, flexBasis
justifySelf, alignSelf, order
gridArea, gridRow, gridRowStart, gridRowEnd, gridColumn, gridColumnStart, gridColumnEnd
position, zIndex, top, bottom, inset, insetX, insetY, insetStart, insetEnd
visibility
height, minHeight, maxHeight (only in specific components without an intrinsic height)

Example:

import {style} from '@react-spectrum/s2/style' with {type: 'macro'};
import {Button} from '@react-spectrum/s2';

<Button styles={style({marginStart: 8})}>Edit</Button>


When styling native HTML elements or React Aria Components, use className={style(...)} instead of the limited styles prop. In those cases, you are not limited to the React Spectrum component property subset.

Example:

import {style} from '@react-spectrum/s2/style' with {type: 'macro'};
import {Checkbox} from 'react-aria-components';

<div className={style({display: 'grid', gap: 12, padding: 16, backgroundColor: 'gray-75'})}>
  <h2 className={style({font: 'heading-sm'})}>Preferences</h2>
  <Checkbox
    className={style({
      display: 'flex',
      alignItems: 'center',
      gap: 8,
      color: {
        default: 'neutral',
        isSelected: 'blue-900'
      }
    })}
  />
</div>


The style macro supports runtime conditions:

import {style} from '@react-spectrum/s2/style' with {type: 'macro'};

const styles = style({
  backgroundColor: {
    variant: {
      primary: 'accent',
      secondary: 'neutral'
    }
  }
});

function MyComponent({variant}: {variant: 'primary' | 'secondary'}) {
  return <div className={styles({variant})} />
}


Boolean conditions starting with is or allows can be used directly without nesting:

const styles = style({
  backgroundColor: {
    default: 'gray-100',
    isSelected: 'gray-900',
    allowsRemoving: 'gray-400'
  }
});

<div className={styles({isSelected: true})} />


Note:

Base spacing values (for margin, gap, etc.): Use pixels following a 4px grid (0, 2, 4, 8, 12, 16...)

See Styling for the full guide and Style Macro for the full property and utility reference.

If you encounter issues related to the style macro import, see the 'Framework setup' section of the Getting started guide.

Typography

Avoid using Text/Heading/Content as standalone typography primitives. These should only be used inside specific React Spectrum components where they inherit the intended slots and default styles.

Use Text/Heading/Content inside components like cards, lists, pickers, menus, tabs, and other Spectrum composition APIs where slot="label", slot="description", or default/implicit Text slots are used. Component docs will have examples of these.
For standalone headings, body copy, captions, and other page-level typography, use native HTML elements plus the style macro.

Example:

import {style} from '@react-spectrum/s2/style' with {type: 'macro'};

<section>
  <h1 className={style({font: 'heading-xl', marginBottom: 8})}>
    Project overview
  </h1>
  <p className={style({font: 'body', color: 'neutral-subdued'})}>
    Review status, owners, and upcoming milestones.
  </p>
  <p className={style({font: 'body-sm', marginTop: 12})}>
    Last updated 2 hours ago
  </p>
</section>


See Style Macro for the available typography tokens and related text styling options.

Icons

Use React Spectrum's built-in icons and illustrations.

Import icons from @react-spectrum/s2/icons/...
Import illustrations from @react-spectrum/s2/illustrations/...
Avoid introducing third-party icon libraries such as lucide-react, phosphor-icons, or heroicons

Commonly used icons include AlertTriangle, Close, ChevronDown, Checkmark, Preview, CheckmarkCircle, Add, ChevronUp, Data, FileText, InfoCircle, OpenIn, Chat, and Code.

Example icon:

import AlertTriangle from '@react-spectrum/s2/icons/AlertTriangle';

<AlertTriangle />


Example illustrations:

import DropToUpload from '@react-spectrum/s2/illustrations/gradient/generic1/DropToUpload';

<DropToUpload />

Note that illustrations can be in a Gradient or Linear style.
Gradient illustrations can include Generic 1 and Generic 2 variants.

See Icons and Illustrations for the full catalogs and usage guidance.

Documentation Structure

The references/ directory contains detailed documentation organized as follows:

Guides
Component Decision Tree: How to choose the right S2 component when requirements do not name one explicitly.
Collections: Many components display a collection of items, and provide functionality such as keyboard navigation, and selection. Learn how to load and render collections using React Spectrum's compositional API.
Forms: Learn how to integrate with HTML forms, validate and submit data, and use React Spectrum with form libraries.
Getting started: ## Installation
Migrating to Spectrum 2: Learn how to migrate from React Spectrum v3 to Spectrum 2.
Selection: Many collection components support selecting items by clicking or tapping them, or by using the keyboard. Learn how to handle selection events, how to control selection programmatically, and the data structures used to represent a selection.
Style Macro: The macro supports a constrained set of values per property that conform to Spectrum 2.
Styling: Learn how to use the macro to apply Spectrum tokens directly in your components with type-safe autocompletion.
Testing: Learn how to test an application built with React Spectrum using test utilities to simulate common user interactions.
Working with AI: Learn how to use the React Spectrum MCP Server, Agent Skills, and more to help you build with AI.
Components
Accordion: An accordion is a container for multiple accordion items.
ActionBar: Action bars are used for single and bulk selection patterns when a user needs to perform actions on one or more items at the same time.
ActionButton: ActionButtons allow users to perform an action.
ActionButtonGroup: An ActionButtonGroup is a grouping of related ActionButtons.
ActionMenu: ActionMenu combines an ActionButton with a Menu for simple "more actions" use cases.
Avatar: An avatar is a thumbnail representation of an entity, such as a user or an organization.
AvatarGroup: An avatar group is a grouping of avatars that are related to each other.
Badge: Badges are used for showing a small amount of color-categorized metadata, ideal for getting a user's attention.
Breadcrumbs: Breadcrumbs show hierarchy and navigational context for a user's location within an application.
Button: Buttons allow users to perform an action.
ButtonGroup: ButtonGroup handles overflow for a grouping of buttons whose actions are related to each other.
Calendar: Calendars display a grid of days in one or more months and allow users to select a single date.
Card: A Card summarizes an object that a user can select or navigate to.
CardView: A CardView displays a group of related objects, with support for selection and bulk actions.
Checkbox: Checkboxes allow users to select multiple items from a list of individual items,
CheckboxGroup: A CheckboxGroup allows users to select one or more items from a list of choices.
ColorArea: A ColorArea allows users to adjust two channels of an RGB, HSL or HSB color value against a two-dimensional gradient background.
ColorField: A color field allows users to edit a hex color or individual color channel value.
ColorSlider: A ColorSlider allows users to adjust an individual channel of a color value.
ColorSwatch: A ColorSwatch displays a preview of a selected color.
ColorSwatchPicker: A ColorSwatchPicker displays a list of color swatches and allows a user to select one of them.
ColorWheel: A ColorWheel allows users to adjust the hue of an HSL or HSB color value on a circular track.
ComboBox: ComboBox allow users to choose a single option from a collapsible list of options when space is limited.
ContextualHelp: Contextual help shows a user extra information about the state of an adjacent component, or a total view.
DateField: DateFields allow users to enter and edit date and time values using a keyboard.
DatePicker: DatePickers combine a DateField and a Calendar popover to allow users to enter or select a date and time value.
DateRangePicker: DateRangePickers combine two DateFields and a RangeCalendar popover to allow users
Dialog: Dialogs are windows containing contextual information, tasks, or workflows that appear over the user interface.
Disclosure: A disclosure is a collapsible section of content. It is composed of a header with a heading and trigger button, and a panel that contains the content.
Divider: Dividers bring clarity to a layout by grouping and dividing content in close proximity.
DropZone: A drop zone is an area into which one or multiple objects can be dragged and dropped.
Form: Forms allow users to enter data that can be submitted while providing alignment and styling for form fields.
Icons: React Spectrum offers a set of open source icons that can be imported from .
IllustratedMessage: An IllustratedMessage displays an illustration and a message, usually
Illustrations: React Spectrum offers a collection of illustrations that can be imported from .
Image: An image with support for skeleton loading and custom error states.
InlineAlert: Inline alerts display a non-modal message associated with objects in a view.
Link: Links allow users to navigate to a different location.
LinkButton: A LinkButton combines the functionality of a link with the appearance of a button. Useful for allowing users to navigate to another page.
ListView: A ListView displays a list of interactive items, and allows a user to navigate, select, or perform an action.
mcp
Menu: Menus display a list of actions or options that a user can choose.
Meter: Meters are visual representations of a quantity or an achievement.
NumberField: NumberFields allow users to input number values with a keyboard or increment/decrement with step buttons.
Picker: Pickers allow users to choose a single option from a collapsible list of options when space is limited.
Popover: A popover is an overlay element positioned relative to a trigger.
ProgressBar: ProgressBars show the progression of a system operation: downloading, uploading, processing, etc., in a visual way.
ProgressCircle: ProgressCircles show the progression of a system operation such as downloading, uploading, or processing, in a visual way.
Provider: Provider is the container for all React Spectrum components.
RadioGroup: Radio groups allow users to select a single option from a list of mutually exclusive options.
RangeCalendar: RangeCalendars display a grid of days in one or more months and allow users to select a contiguous range of dates.
RangeSlider: RangeSliders allow users to quickly select a subset range. They should be used when the upper and lower bounds to the range are invariable.
SearchField: A SearchField is a text field designed for searches.
SegmentedControl: A SegmentedControl is a mutually exclusive group of buttons used for view switching.
SelectBoxGroup: SelectBoxGroup allows users to select one or more options from a list.
Skeleton: A Skeleton wraps around content to render it as a placeholder.
Slider: Sliders allow users to quickly select a value within a range. They should be used when the upper and lower bounds to the range are invariable.
StatusLight: Status lights are used to color code categories and labels commonly found in data visualization.
Switch: Switches allow users to turn an individual option on or off.
TableView: Tables are containers for displaying information. They allow users to quickly scan, sort, compare, and take action on large amounts of data.
Tabs: Tabs organize content into multiple sections and allow users to navigate between them. The content under the set of tabs should be related and form a coherent unit.
TagGroup: Tags allow users to categorize content. They can represent keywords or people, and are grouped to describe an item or a search request.
TextArea: A textarea allows a user to input mult-line text.
TextField: TextFields are text inputs that allow users to input custom text entries
TimeField: TimeFields allow users to enter and edit time values using a keyboard.
Toast: A ToastContainer renders the queued toasts in an application. It should be placed
ToggleButton: ToggleButtons allow users to toggle a selection on or off, for example
ToggleButtonGroup: A ToggleButtonGroup is a grouping of related ToggleButtons, with single or multiple selection.
Tooltip: Display container for Tooltip content. Has a directional arrow dependent on its placement.
TreeView: A tree view provides users with a way to navigate nested hierarchical information.
Testing
Testing CheckboxGroup
Testing ComboBox
Testing Dialog
Testing ListView
Testing Menu
Testing Picker
Testing RadioGroup
Testing TableView
Testing Tabs
Testing TreeView
Weekly Installs
421
Source
react-spectrum.adobe.com
First Seen
Feb 28, 2026
Security Audits
SocketPass