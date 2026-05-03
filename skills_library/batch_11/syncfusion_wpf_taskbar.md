---
title: syncfusion-wpf-taskbar
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-taskbar
---

# syncfusion-wpf-taskbar

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-taskbar
syncfusion-wpf-taskbar
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-taskbar
SKILL.md
Implementing WPF TaskBar

The TaskBar control provides a Windows Explorer-style task panel UI — grouped collapsible sections (TaskBarItem) that can hold any WPF content. Ideal for action panels, property groups, navigation sidebars, and tool panels.

Assembly required:

Syncfusion.Tools.WPF
Syncfusion.Shared.WPF

XAML namespace:

xmlns:syncfusion="http://schemas.syncfusion.com/wpf"


C# namespace:

using Syncfusion.Windows.Tools.Controls;

When to Use This Skill
Scenario	Use TaskBar
Windows Explorer-style grouped action panel	✅ Yes
Collapsible sidebar with grouped items	✅ Yes
WPF tool panel with categorized sections	✅ Yes
Simple tab control	❌ Use TabControl
Navigation sidebar with drill-down	❌ Use GroupBar or SfTreeNavigator
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Assembly and NuGet setup
Adding TaskBar via XAML and C#
Adding a TaskBarItem with a Header
Adding content (text, panels) to TaskBarItem
Items and Content

📄 Read: references/items-and-content.md

TaskBarItem Items collection (any UIElement)
Custom header with image (DockPanel + Image + TextBlock)
Collapse/expand with IsOpened attached property
Animation speed (Speed attached property)
Expander button size (ButtonSize attached property)
Layout and Orientation

📄 Read: references/layout-and-orientation.md

GroupOrientation: Horizontal vs Vertical
GroupOrientationChanged event
GroupMargin: spacing between items
GroupPadding: internal content padding
GroupWidth: uniform item width
FlowDirection: LeftToRight / RightToLeft
Appearance and Visual Styles

📄 Read: references/appearance.md

SkinStorage.SetVisualStyle() — applying built-in visual styles
All available style names (Office2007, Blend, Metro, VS2010, etc.)
Quick Start Example

Minimal TaskBar with two groups (XAML):

<Window x:Class="MyApp.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:syncfusion="http://schemas.syncfusion.com/wpf"
        Title="MainWindow" Height="450" Width="300">
    <Grid>
        <syncfusion:TaskBar Name="taskBar" GroupMargin="5">

            <syncfusion:TaskBarItem Header="File Tasks">
                <StackPanel Margin="10">
                    <TextBlock Text="Open a file" />
                    <TextBlock Text="Save the file" />
                </StackPanel>
            </syncfusion:TaskBarItem>

            <syncfusion:TaskBarItem Header="Edit Tasks">
                <StackPanel Margin="10">
                    <TextBlock Text="Copy" />
                    <TextBlock Text="Paste" />
                </StackPanel>
            </syncfusion:TaskBarItem>

        </syncfusion:TaskBar>
    </Grid>
</Window>


C# equivalent:

TaskBar taskBar = new TaskBar();
taskBar.GroupMargin = new Thickness(5);

TaskBarItem item1 = new TaskBarItem() { Header = "File Tasks" };
item1.Items.Add(new TextBlock() { Text = "Open a file" });
taskBar.Items.Add(item1);

TaskBarItem item2 = new TaskBarItem() { Header = "Edit Tasks" };
item2.Items.Add(new TextBlock() { Text = "Copy" });
taskBar.Items.Add(item2);

this.Content = taskBar;

Common Patterns
Collapse all groups on load
<syncfusion:TaskBar Name="taskBar" syncfusion:TaskBar.IsOpened="False">
    <syncfusion:TaskBarItem Header="Tasks" />
</syncfusion:TaskBar>

Horizontal layout (groups side by side)
<syncfusion:TaskBar GroupOrientation="Horizontal" GroupMargin="5">
    ...
</syncfusion:TaskBar>

Custom header with icon
<syncfusion:TaskBarItem>
    <syncfusion:TaskBarItem.Header>
        <DockPanel>
            <Image Height="16" Width="16" Source="icon.png" />
            <TextBlock Foreground="White" Margin="5,0,0,0" Text="My Group" />
        </DockPanel>
    </syncfusion:TaskBarItem.Header>
    ...
</syncfusion:TaskBarItem>

Apply visual style
SkinStorage.SetVisualStyle(taskBar, "Office2007Blue");

Key Properties
Property	On	Type	Description
Header	TaskBarItem	object	Group header label (supports templates)
Items	TaskBarItem	collection	Content items in the group
GroupMargin	TaskBar	Thickness	Margin between all TaskBarItems
GroupWidth	TaskBar	double	Uniform width for all TaskBarItems
GroupOrientation	TaskBar	Orientation	Vertical (default) or Horizontal
FlowDirection	TaskBar	FlowDirection	LeftToRight or RightToLeft
IsOpened	attached on TaskBar	bool	Expand (true) or collapse (false) all items
TaskBar.Speed	attached	double	Animation speed for expand/collapse
TaskBar.ButtonSize	attached	double	Height of the expander button
TaskBar.GroupPadding	attached	Thickness	Padding inside each TaskBarItem
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