---
rating: ⭐⭐
title: react-aria
url: https://skills.sh/site/react-aria.adobe.com/react-aria
---

# react-aria

skills/react-aria.adobe.com/react-aria
react-aria
$ npx skills add https://react-aria.adobe.com
SKILL.md
React Aria Components

React Aria Components is a library of unstyled, accessible UI components that you can style with any CSS solution. Built on top of React Aria hooks, it provides the accessibility and behavior without prescribing any visual design.

Documentation Structure

The references/ directory contains detailed documentation organized as follows:

Guides
Collections: Many components display a collection of items, and provide functionality such as keyboard navigation, and selection. Learn how to load and render collections using React Aria's compositional API.
Customization: React Aria is built using a flexible and composable API. Learn how to use contexts and slots to create custom component patterns, or mix and match with the lower level Hook-based API for even more control over rendering and behavior.
Drag and Drop: React Aria collection components support drag and drop with mouse and touch interactions, and full keyboard and screen reader accessibility. Learn how to provide drag data and handle drop events to move, insert, or reorder items.
Forms: Learn how to integrate with HTML forms, validate and submit data, and use React Aria with form libraries.
Framework setup: Learn how to integrate React Aria with your framework.
Getting started: How to install React Aria and build your first component.
Quality: React Aria is built around three core principles: , , and . Learn how to apply these tools to build high quality UIs that work for everyone, everywhere, and on every device.
Selection: Many collection components support selecting items by clicking or tapping them, or by using the keyboard. Learn how to handle selection events, how to control selection programmatically, and the data structures used to represent a selection.
Styling: React Aria does not include any styles by default. Learn how to build custom designs to fit your application or design system using any styling solution.
Testing: Learn how to test components and applications built with React Aria using test utilities to simulate common user interactions.
Working with AI: Learn how to use the React Aria MCP Server, Agent Skills, and more to help you build with AI.
Components
Autocomplete: An autocomplete allows users to search or filter a list of suggestions.
Breadcrumbs: Breadcrumbs display a hierarchy of links to the current page or resource in an application.
Button: A button allows a user to perform an action, with mouse, touch, and keyboard interactions.
Calendar: A calendar displays one or more date grids and allows users to select a single date.
Checkbox: A checkbox allows a user to select multiple items from a list of individual items, or
CheckboxGroup: A CheckboxGroup allows users to select one or more items from a list of choices.
ColorArea: A color area allows users to adjust two channels of an RGB, HSL or HSB color value against a two-dimensional gradient background.
ColorField: A color field allows users to edit a hex color or individual color channel value.
ColorPicker: A ColorPicker synchronizes a color value between multiple React Aria color components.
ColorSlider: A color slider allows users to adjust an individual channel of a color value.
ColorSwatch: A ColorSwatch displays a preview of a selected color.
ColorSwatchPicker: A ColorSwatchPicker displays a list of color swatches and allows a user to select one of them.
ColorWheel: A color wheel allows users to adjust the hue of an HSL or HSB color value on a circular track.
ComboBox: A combo box combines a text input with a listbox, allowing users to filter a list of options to items matching a query.
DateField: A date field allows users to enter and edit date and time values using a keyboard.
DatePicker: A date picker combines a DateField and a Calendar popover to allow users to enter or select a date and time value.
DateRangePicker: DateRangePickers combine two DateFields and a RangeCalendar popover to allow users
Disclosure: A disclosure is a collapsible section of content. It is composed of a a header with a heading and trigger button, and a panel that contains the content.
DisclosureGroup: A DisclosureGroup is a grouping of related disclosures, sometimes called an accordion.
DropZone: A drop zone is an area into which one or multiple objects can be dragged and dropped.
FileTrigger: A FileTrigger allows a user to access the file system with any pressable React Aria or React Spectrum component, or custom components built with usePress.
Form: A form is a group of inputs that allows users to submit data to a server,
GridList: A grid list displays a list of interactive items, with support for keyboard navigation,
Group: A group represents a set of related UI controls, and supports interactive states for styling.
Link: A link allows a user to navigate to another page or resource within a web page
ListBox: A listbox displays a list of options and allows a user to select one or more of them.
mcp
Menu: A menu displays a list of actions or options that a user can choose.
Meter: A meter represents a quantity within a known range, or a fractional value.
Modal: A modal is an overlay element which blocks interaction with elements outside it.
NumberField: A number field allows a user to enter a number, and increment or decrement the value using stepper buttons.
Popover: A popover is an overlay element positioned relative to a trigger.
ProgressBar: Progress bars show either determinate or indeterminate progress of an operation
RadioGroup: A radio group allows a user to select a single item from a list of mutually exclusive options.
RangeCalendar: RangeCalendars display a grid of days in one or more months and allow users to select a contiguous range of dates.
SearchField: A search field allows a user to enter and clear a search query.
Select: A select displays a collapsible list of options and allows a user to select one of them.
Separator: A separator is a visual divider between two groups of content, e.g. groups of menu items or sections of a page.
Slider: A slider allows a user to select one or more values within a range.
Switch: A switch allows a user to turn a setting on or off.
Table: A table displays data in rows and columns and enables a user to navigate its contents via directional navigation keys,
Tabs: Tabs organize content into multiple sections and allow users to navigate between them.
TagGroup: A tag group is a focusable list of labels, categories, keywords, filters, or other items, with support for keyboard navigation, selection, and removal.
TextField: A text field allows a user to enter a plain text value with a keyboard.
TimeField: TimeFields allow users to enter and edit time values using a keyboard.
Toast
ToggleButton: A toggle button allows a user to toggle a selection on or off, for example switching between two states or modes.
ToggleButtonGroup: A toggle button group allows a user to toggle multiple options, with single or multiple selection.
Toolbar: A toolbar is a container for a set of interactive controls, such as buttons, dropdown menus, or checkboxes,
Tooltip: A tooltip displays a description of an element on hover or focus.
Tree: A tree provides users with a way to navigate nested hierarchical information, with support for keyboard navigation
Virtualizer: A Virtualizer renders a scrollable collection of data using customizable layouts.
Interactions
FocusRing: A utility component that applies a CSS class when an element has keyboard focus.
FocusScope: A FocusScope manages focus for its descendants. It supports containing focus inside
useClipboard: Handles clipboard interactions for a focusable element. Supports items of multiple
useDrag: Handles drag interactions for an element, with support for traditional mouse and touch
useDrop: Handles drop interactions for an element, with support for traditional mouse and touch
useFocus: Handles focus events for the immediate target.
useFocusRing: Determines whether a focus ring should be shown to indicate keyboard focus.
useFocusVisible: Manages focus visible state for the page, and subscribes individual components for updates.
useFocusWithin: Handles focus events for the target and its descendants.
useHover: Handles pointer hover interactions for an element. Normalizes behavior
useKeyboard: Handles keyboard interactions for a focusable element.
useLandmark: Provides landmark navigation in an application. Call this with a role and label to register a landmark navigable with F6.
useLongPress: Handles long press interactions across mouse and touch devices. Supports a customizable time threshold,
useMove: Handles move interactions across mouse, touch, and keyboard, including dragging with
usePress: Handles press interactions across mouse, touch, keyboard, and screen readers.
Utilities
I18nProvider: Provides the locale for the application to all child components.
mergeProps: Merges multiple props objects together. Event handlers are chained,
PortalProvider: Sets the portal container for all overlay elements rendered by its children.
SSRProvider: When using SSR with React Aria in React 16 or 17, applications must be wrapped in an SSRProvider.
useCollator: Provides localized string collation for the current locale. Automatically updates when the locale changes,
useDateFormatter: Provides localized date formatting for the current locale. Automatically updates when the locale changes,
useField: Provides the accessibility implementation for input fields.
useFilter: Provides localized string search functionality that is useful for filtering or matching items
useId: If a default is not provided, generate an id.
useIsSSR: Returns whether the component is currently being server side rendered or
useLabel: Provides the accessibility implementation for labels and their associated elements.
useLocale: Returns the current locale and layout direction.
useNumberFormatter: Provides localized number formatting for the current locale. Automatically updates when the locale changes,
useObjectRef: Offers an object ref for a given callback ref or an object ref. Especially
VisuallyHidden: VisuallyHidden hides its children visually, while keeping content visible
Internationalization
Calendar
CalendarDate
CalendarDateTime
DateFormatter
Internationalized Date
Internationalized Number
NumberFormatter
NumberParser
Time
ZonedDateTime
Testing
Testing CheckboxGroup
Testing ComboBox
Testing GridList
Testing ListBox
Testing Menu
Testing RadioGroup
Testing Select
Testing Table
Testing Tabs
Testing Tree
Weekly Installs
881
Source
react-aria.adobe.com
First Seen
1 day ago
Security Audits
SocketPass