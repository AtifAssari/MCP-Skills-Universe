---
rating: ⭐⭐⭐
title: syncfusion-wpf-tabcontrol
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-tabcontrol
---

# syncfusion-wpf-tabcontrol

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-tabcontrol
syncfusion-wpf-tabcontrol
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-tabcontrol
SKILL.md
Implementing WPF TabControl (TabControlExt)

The TabControl (TabControlExt) is a powerful component for organizing application content into multiple tabs. It provides features like tab orientation, editable headers, pin/unpin functionality, context menus, and customizable close buttons, enabling developers to create flexible, organized tabbed interfaces.

When to Use This Skill
Creating tabbed interfaces: When you need to organize multiple content areas into a tab-based layout
Tab management: For handling tab item creation, deletion, selection, and manipulation
User interactions: When you need to respond to tab selection changes, tab closing, or tab navigation
Customization: For styling tabs (orientation, placement, themes), configuring close buttons, or adding icons
Data binding: When binding tab items to data sources or observable collections
Advanced features: For implementing context menus, drag-drop reordering, pin/unpin, or keyboard navigation
Component Overview

Key Capabilities:

Tab Orientation - Position tabs horizontally (top/bottom) or vertically (left/right)
Flexible Closing - Configure close button display (Common, Individual, Both, Extended, Hidden)
Tab Selection - Support for mouse, keyboard (Ctrl+Tab, Arrow keys), and programmatic selection
Editable Headers - Allow users to edit tab headers interactively
Pin/Unpin - Enable quick access to frequently used tabs
Context Menus - Built-in and custom context menu support
Data Binding - Bind tab items to data sources
Drag and Drop - Reorder tabs by dragging
Navigation - Tab list menu and scroll buttons for navigation
Theming - Rich set of built-in themes and customization options
Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Installation and assembly references
Basic TabControl creation (XAML and C# approaches)
Adding TabItems with headers and content
Tab placement and orientation options
Assembly dependencies
Tab Interactions & Selection

📄 Read: references/tab-interactions.md

Tab selection (mouse, keyboard, programmatic)
SelectedItemChangedEvent for monitoring changes
Keyboard navigation (Ctrl+Tab, Arrow keys)
Tab list context menu for quick navigation
Getting selected item properties
Tab Closing & Button Configuration

📄 Read: references/closing-tabs.md

CloseButtonType options and display modes
Individual vs common close buttons
Disabling close on specific tabs (CanClose)
Hiding close buttons for particular tabs
Close button visibility states
Customization & Styling

📄 Read: references/customization.md

Editable tab headers
Tab orientation and placement variations
Layout modes (SingleLine, MultiLine, MultiLineWithFillWidth)
Pin/unpin functionality
Tab scrolling configuration
Built-in themes and theming support
Data Binding

📄 Read: references/data-binding.md

Binding TabControl items to data sources
Creating TabItems from data collections
Header and content templates
Observable collection patterns
TabItem data binding
Advanced Features

📄 Read: references/advanced-features.md

Context menu customization (tab-level and item-level)
Custom menu items and handlers
Tab reordering via drag and drop
New button feature (IsNewButtonEnabled)
Tab scrolling with navigation buttons
Localization support
New tab button events
Quick Start Example
Basic XAML TabControl
<Window x:Class="TabControlApp.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:syncfusion="http://schemas.syncfusion.com/wpf"
        Title="TabControl Example" Height="450" Width="800">

    <Grid>
        <syncfusion:TabControlExt Name="tabControl" Height="100" Width="280">
            <syncfusion:TabItemExt Header="Tab 1">
                <TextBlock Text="Content of Tab 1" />
            </syncfusion:TabItemExt>
            <syncfusion:TabItemExt Header="Tab 2">
                <TextBlock Text="Content of Tab 2" />
            </syncfusion:TabItemExt>
            <syncfusion:TabItemExt Header="Tab 3">
                <TextBlock Text="Content of Tab 3" />
            </syncfusion:TabItemExt>
        </syncfusion:TabControlExt>
    </Grid>
</Window>

Basic C# Creation
using Syncfusion.Windows.Tools.Controls;

public partial class MainWindow : Window {
    public MainWindow() {
        InitializeComponent();

        // Create TabControl instance
        TabControlExt tabControlExt = new TabControlExt();
        tabControlExt.Height = 100;
        tabControlExt.Width = 280;

        // Create and add TabItems
        TabItemExt tabItem1 = new TabItemExt() 
        {
            Header = "Tab 1",
            Content = new TextBlock() { Text = "Content of Tab 1" }
        };

        TabItemExt tabItem2 = new TabItemExt() 
        {
            Header = "Tab 2",
            Content = new TextBlock() { Text = "Content of Tab 2" }
        };

        tabControlExt.Items.Add(tabItem1);
        tabControlExt.Items.Add(tabItem2);

        this.Content = tabControlExt;
    }
}

Common Patterns
Pattern 1: Responding to Tab Selection Changes
// Handle tab selection changes
tabControl.SelectedItemChangedEvent += TabControl_SelectedItemChangedEvent;

private void TabControl_SelectedItemChangedEvent(object sender, SelectedItemChangedEventArgs e)
{
    var newTabItem = e.NewSelectedItem.Header;
    var oldTabItem = e.OldSelectedItem?.Header ?? "None";
    MessageBox.Show($"Changed from {oldTabItem} to {newTabItem}");
}

Pattern 2: Configuring Close Buttons
<!-- Enable close buttons on both TabControl and TabItems -->
<syncfusion:TabControlExt CloseButtonType="Both" Name="tabControl">
    <syncfusion:TabItemExt Header="Tab 1" />
    <syncfusion:TabItemExt Header="Tab 2" CanClose="False" />
</syncfusion:TabControlExt>

Pattern 3: Changing Tab Orientation
<!-- Position tabs at the bottom -->
<syncfusion:TabControlExt TabStripPlacement="Bottom" Name="tabControl">
    <syncfusion:TabItemExt Header="Tab 1" />
    <syncfusion:TabItemExt Header="Tab 2" />
</syncfusion:TabControlExt>

Pattern 4: Adding a New Tab Button
<syncfusion:TabControlExt IsNewButtonEnabled="True" 
                          NewButtonClick="TabControl_NewButtonClick"
                          Name="tabControl" />

private void TabControl_NewButtonClick(object sender, EventArgs e)
{
    TabItemExt newItem = new TabItemExt() 
    {
        Header = $"Tab {tabControl.Items.Count + 1}",
        Content = new TextBlock() { Text = "New tab content" }
    };
    tabControl.Items.Add(newItem);
}

Pattern 5: Enabling Navigation with Scroll Buttons
<syncfusion:TabControlExt TabScrollButtonVisibility="Visible"
                          TabScrollStyle="Extended"
                          Name="tabControl" />

Key Properties
Items — Collection of TabItemExt objects
SelectedItem — Currently selected tab
TabStripPlacement — Position (Top, Bottom, Left, Right)
CloseButtonType — Close button display mode
IsNewButtonEnabled — Show/hide new tab button
ShowTabListContextMenu — Tab list navigation menu
Key Events
SelectedItemChangedEvent — Tab selection changed
TabItemClosing — Before tab closes (can cancel)
TabItemClosed — After tab closes
Weekly Installs
50
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