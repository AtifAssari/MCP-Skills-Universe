---
rating: ⭐⭐
title: syncfusion-wpf-navigation-pane
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-navigation-pane
---

# syncfusion-wpf-navigation-pane

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-navigation-pane
syncfusion-wpf-navigation-pane
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-navigation-pane
SKILL.md
Implementing WPF GroupBar (Navigation Pane)

The GroupBar control implements a navigation pane similar to the Microsoft Outlook Bar. It hosts categorized collections of items and custom controls in expandable/collapsible sections. Supports multiple visual modes, data binding, drag-and-drop reordering, context menus, toolbars, and full theme support.

Assemblies: Syncfusion.Tools.WPF + Syncfusion.Shared.WPF
Namespace: Syncfusion.Windows.Tools.Controls
XAML Schema: xmlns:syncfusion="http://schemas.syncfusion.com/wpf"

Control Hierarchy
GroupBar                    ← Root navigation container
└── GroupBarItem            ← Category tab/header (e.g., "Mailbox", "Contacts")
    ├── GroupView           ← List container for link-style items
    │   └── GroupViewItem   ← Clickable item with text and icon
    └── Panel / any UIElement ← Or use any WPF panel as content

When to Use This Skill
User wants an Outlook-style navigation sidebar or accordion panel
User needs expandable/collapsible sections with content inside
User asks about GroupBar, GroupBarItem, GroupView, GroupViewItem
User needs StackMode (Outlook bar), MultipleExpansion (tree-view), or Default mode
User needs data-bound navigation items using MVVM
User asks about drag-and-drop reordering of navigation items
User asks about Navigation Pane popup, gripper, or resize behavior
Quick Start
xmlns:syncfusion="http://schemas.syncfusion.com/wpf"

<syncfusion:GroupBar Height="300" Width="230" VisualMode="StackMode" Name="groupBar">
    <syncfusion:GroupBarItem Header="Mailbox" HeaderImageSource="Images/mail.png">
        <syncfusion:GroupView>
            <syncfusion:GroupViewItem Text="Inbox"     ImageSource="Images/inbox.png"/>
            <syncfusion:GroupViewItem Text="Sent Items" ImageSource="Images/sent.png"/>
            <syncfusion:GroupViewItem Text="Deleted"   ImageSource="Images/trash.png"/>
        </syncfusion:GroupView>
    </syncfusion:GroupBarItem>
    <syncfusion:GroupBarItem Header="Contacts">
        <syncfusion:GroupView>
            <syncfusion:GroupViewItem Text="All Contacts"/>
            <syncfusion:GroupViewItem Text="Favorites"/>
        </syncfusion:GroupView>
    </syncfusion:GroupBarItem>
</syncfusion:GroupBar>

using Syncfusion.Windows.Tools.Controls;

GroupBar groupBar = new GroupBar();
groupBar.VisualMode = VisualMode.StackMode;

GroupBarItem item = new GroupBarItem { Header = "Mailbox" };
GroupView view = new GroupView();
view.Items.Add(new GroupViewItem { Text = "Inbox" });
item.Content = view;
groupBar.Items.Add(item);
this.Content = groupBar;

Common Patterns
Goal	Approach
Outlook-style navigation	VisualMode="StackMode"
Tree-style multi-expand	VisualMode="MultipleExpansion"
One-at-a-time expand	VisualMode="Default"
Collapsible bar	AllowCollapse="True" + VisualMode="StackMode"
Data-bound items	ItemsSource + ItemContainerStyle with HeaderText/Content setters
Custom item content	Place any Panel or UIElement as GroupBarItem.Content
List-view style items	GroupView with IsListViewMode="True"
Drag-reorder items	DragItemVisibility="True"
Resize navigation popup	PopupResizeDirection="Both"
Gripper for StackMode	ShowGripper="True" + VisualMode="StackMode"
Save/restore bar state	SaveBarState() / LoadBarState() / ResetBarState()
Key Properties
Property	Type	Description
VisualMode	VisualMode	Default / MultipleExpansion / StackMode
AllowCollapse	bool	Allow collapsing (StackMode)
ShowGripper	bool	Show resize gripper (StackMode)
ItemsSource	IEnumerable	Data-bound items
ItemContainerStyle	Style	Style applied to each GroupBarItem
DragItemVisibility	bool	Enable drag-and-drop reordering
DragMarkerBrush	Brush	Color of drag insertion marker
PopupResizeDirection	PopupResizeDirection	Navigation pane popup resize (Both/H/V/None)
ItemContentLength	double	Height/width of selected item content area
GroupBarHeaderStyle	Style	Style for GroupBar header border
GroupBarItem.Header	string	Display text for item header
GroupBarItem.HeaderImageSource	ImageSource	Icon in item header
GroupBarItem.IsSelected	bool	Expand this item initially
GroupBarItem.GroupBarItemCornerRadius	CornerRadius	Rounded corners on item header
GroupView.IsListViewMode	bool	List-view style (vs icon style)
GroupViewItem.Text	string	Text label for view item
GroupViewItem.ImageSource	ImageSource	Icon for view item
SaveOriginalState	bool	Auto-save state on load
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Assembly references (Tools.WPF + Shared.WPF)
Add via designer, XAML, or C#
Declarative GroupBarItems with GroupView content
Adding panel content to GroupBarItem
Basic VisualMode overview
Themes with SfSkinManager
GroupBar Items

📄 Read: references/groupbar-items.md

GroupBarItem properties (Header, HeaderText, HeaderImageSource)
IsSelected, ShowInGroupBar, GroupBarItemCornerRadius
GroupBarItemCursorType (Default/Hand)
ItemContentLength (content area height/width)
DraggingItemInProgress, HiddenItemsCount
GroupBarItemAdded / GroupBarItemRemoved events
GroupView and Content

📄 Read: references/groupview-and-content.md

GroupView as item container with GroupViewItem elements
GroupViewItem (Text, ImageSource, tooltip)
IsListViewMode (list vs icon display)
Default image for GroupViewItem
Adding panels and custom UIElements as content
Rotating item content
Visual Modes

📄 Read: references/visual-modes.md

Default mode (one item expanded at a time)
MultipleExpansion mode (tree-view style)
StackMode (Outlook bar style, popup menu at bottom)
AllowCollapse, ShowGripper
ThemeStudio vs classic theme layout difference in StackMode
Data Binding

📄 Read: references/data-binding.md

ItemsSource + ItemContainerStyle with HeaderText/Content setters
Model + ViewModel with ObservableCollection
DataContext binding pattern
Data binding with XML (XmlDataProvider)
HeaderTemplate and ContentTemplate customization
ItemContainerStyleSelector for conditional styles
Orientation and Layout

📄 Read: references/orientation-and-layout.md

GroupBar orientation (Horizontal/Vertical)
GroupView and GroupViewItem orientation
Adjusting GroupBar width, changing header height
Rotating the GroupBar
FlowDirection for RTL support
Navigation Pane: PopupResizeDirection, ShowGripper
Behavior and Features

📄 Read: references/behavior-and-features.md

Drag-and-drop reordering (DragItemVisibility, DragMarkerBrush)
Built-in context menu (sort, add, rename, move)
Toolbars inside GroupBar
Tooltip for GroupViewItems
Animation for expand/collapse
Collapsing and closing in StackMode
State persistence (SaveBarState/LoadBarState/ResetBarState)
Localization
Appearance

📄 Read: references/appearance.md

GroupBarHeaderStyle (background, corner radius, height)
CollapseButtonTemplate and CollapseButtonBackground
ItemContainerStyle (HeaderTemplate + ContentTemplate)
ItemContainerStyleSelector
DragMarkerBrush
SfSkinManager themes table
ThemeStudio custom themes
Weekly Installs
48
Repository
syncfusion/wpf-…s-skills
GitHub Stars
2
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass