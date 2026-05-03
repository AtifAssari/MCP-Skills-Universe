---
rating: ⭐⭐
title: syncfusion-maui-listview
url: https://skills.sh/syncfusion/maui-ui-components-skills/syncfusion-maui-listview
---

# syncfusion-maui-listview

skills/syncfusion/maui-ui-components-skills/syncfusion-maui-listview
syncfusion-maui-listview
Installation
$ npx skills add https://github.com/syncfusion/maui-ui-components-skills --skill syncfusion-maui-listview
SKILL.md
Implementing .NET MAUI ListView

A comprehensive skill for implementing, customizing, and optimizing the Syncfusion .NET MAUI ListView (SfListView) component. The ListView displays collections of data with support for layouts, sorting, filtering, grouping, selection, and rich customization options.

When to Use This Skill

Use this skill when you need to:

Display Collections: Show lists of data items from any data source (ObservableCollection, List, etc.)
Data Operations: Implement sorting, filtering, or grouping of list items
Custom Layouts: Create linear or grid layouts with single or multiple columns
User Interaction: Enable item selection (single/multiple), tapping, long-press, or double-tap
Advanced Features: Add swipe actions, drag-and-drop reordering, pull-to-refresh, or load more
Customization: Design custom item templates, headers, footers, or group headers
Performance: Optimize list rendering for large datasets with virtualization
MVVM Patterns: Implement ListView with data binding, commands, and ViewModels

Common Scenarios:

Product catalogs, contact lists, inbox/email lists
News feeds, social media posts, photo galleries
Settings pages, navigation menus, file browsers
Task lists, order history, transaction records
Any scrollable collection of similar items
Component Overview

SfListView is a high-performance, feature-rich list control that:

Renders data items using built-in or custom templates
Supports optimized view reusing strategy for smooth scrolling
Provides linear and grid layouts with orientation support
Enables data operations (sort, filter, group) without re-binding
Offers multiple selection modes and gestures
Includes sticky headers, footers, and group headers
Supports item swipe actions and drag-and-drop
Handles large datasets efficiently with virtualization
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

NuGet package setup (Syncfusion.Maui.ListView)
Registering handlers in MauiProgram.cs
Creating your first ListView
Data models and ViewModels
Basic data binding and item templates
Layout Options

📄 Read: references/layouts.md

Linear layout (vertical/horizontal)
Grid layout with SpanCount
Changing layouts dynamically
Responsive column count based on screen size
Layout best practices
Data Operations

📄 Read: references/data-operations.md

Sorting with SortDescriptor (ascending/descending, custom comparers)
Filtering with predicates and RefreshFilter
Grouping with GroupDescriptor and sticky group headers
Combining multiple operations
Performance considerations
Selection

📄 Read: references/selection.md

Selection modes (None, Single, SingleDeselect, Multiple, Extended)
Selection gestures (Tap, DoubleTap, Hold)
SelectedItem and SelectedItems properties
Selection events (SelectionChanging, SelectionChanged)
Programmatic selection
Customizing selection appearance
Item Customization

📄 Read: references/item-customization.md

Custom item templates with ItemTemplate
DataTemplateSelector for dynamic templates
Item sizing (fixed, auto-fit, dynamic)
Item appearance (borders, spacing, visual effects)
Liquid glass effect
Advanced customization techniques
Headers and Footers

📄 Read: references/headers-footers.md

Adding HeaderTemplate and FooterTemplate
Sticky headers and footers (IsStickyHeader, IsStickyFooter)
Group headers with GroupHeaderTemplate
Dynamic header/footer content
Common header/footer patterns
Interactive Features

📄 Read: references/interactive-features.md

Swipe actions (StartSwipeTemplate, EndSwipeTemplate)
Swipe events and common patterns (delete, archive)
Drag and drop (DragStartMode, drag/drop events)
Reordering items within list
Cross-list drag and drop
Load More and Pull to Refresh

📄 Read: references/load-more-pull-refresh.md

Load more options (auto/manual)
LoadMoreCommand and LoadMoreTemplate
Pull to refresh
Best practices for large datasets
Scrolling

📄 Read: references/scrolling.md

Scroll methods (ScrollTo, ScrollToRowIndex)
ScrollBarVisibility property
Programmatic scrolling
ListView without virtualization
Performance optimization for scrolling
Right-to-Left (RTL) Support

📄 Read: references/rtl.md

Right-to-Left (RTL) layout support
FlowDirection property
Testing RTL layouts
MVVM Patterns

📄 Read: references/mvvm-patterns.md

MVVM architecture with ListView
INotifyPropertyChanged and ObservableCollection
Commands (TapCommand, LongPressCommand)
Data binding patterns
Handling user actions in MVVM
Complete MVVM example
Events and Performance

📄 Read: references/events-performance.md

Lifecycle events (Loaded)
Interaction events (ItemTapped, ItemDoubleTapped, ItemLongPress)
ItemAppearing and ItemDisappearing events
Performance optimization techniques
Using BeginInit/EndInit for batch updates
RefreshView method
Troubleshooting performance issues
Weekly Installs
35
Repository
syncfusion/maui…s-skills
GitHub Stars
54
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass