---
rating: ⭐⭐⭐
title: syncfusion-wpf-dropdownbuttonadv
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-dropdownbuttonadv
---

# syncfusion-wpf-dropdownbuttonadv

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-dropdownbuttonadv
syncfusion-wpf-dropdownbuttonadv
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-dropdownbuttonadv
SKILL.md
Implementing WPF DropDownButtonAdv

The DropDownButtonAdv is a WPF dropdown button control that displays a popup menu when the arrow is clicked. It supports menu items with icons, data binding, command binding, configurable popup direction, resizing, multiline text, and full theme support.

Assembly: Syncfusion.Shared.WPF
Namespace: Syncfusion.Windows.Tools.Controls
XAML Schema: xmlns:syncfusion="http://schemas.syncfusion.com/wpf"

When to Use This Skill
User wants a button that opens a dropdown list of options
User needs a WPF dropdown button with icons, checkable items, or grouped items
User asks about DropDownButtonAdv, DropDownMenuGroup, DropDownMenuItem
User needs MVVM binding for dropdown menu items or command binding
User needs to control popup direction, resizing, or multiline label
User asks how to handle dropdown open/close events or item click events
Quick Start
xmlns:syncfusion="http://schemas.syncfusion.com/wpf"

<syncfusion:DropDownButtonAdv Label="Country" SizeMode="Normal" SmallIcon="Images/flag.png">
    <syncfusion:DropDownMenuGroup>
        <syncfusion:DropDownMenuItem HorizontalAlignment="Left" Header="India">
            <syncfusion:DropDownMenuItem.Icon>
                <Image Source="Images/india.png"/>
            </syncfusion:DropDownMenuItem.Icon>
        </syncfusion:DropDownMenuItem>
        <syncfusion:DropDownMenuItem HorizontalAlignment="Left" Header="France"/>
        <syncfusion:DropDownMenuItem HorizontalAlignment="Left" Header="Germany"/>
    </syncfusion:DropDownMenuGroup>
</syncfusion:DropDownButtonAdv>

// C# equivalent
DropDownButtonAdv button = new DropDownButtonAdv();
button.Label = "Country";
button.SizeMode = SizeMode.Normal;
button.SmallIcon = new BitmapImage(new Uri("Images/flag.png", UriKind.RelativeOrAbsolute));
DropDownMenuGroup menu = new DropDownMenuGroup();
menu.Items.Add(new DropDownMenuItem { Header = "India", HorizontalAlignment = HorizontalAlignment.Left });
button.Content = menu;

Common Patterns
Goal	Approach
Static menu items	Declare DropDownMenuItem directly inside DropDownMenuGroup
Dynamic items from data	Bind DropDownMenuGroup.ItemsSource + use ItemTemplate
MVVM command on item click	Set Command + CommandParameter on DropDownMenuItem
Popup opens below-left	DropDirection="BottomLeft" (default)
Large button with label wrapping	SizeMode="Large" + IsMultiLine="True"
Checkable items	IsCheckable="True" on DropDownMenuItem
Custom UIElement in menu	Use DropDownMenuGroup.MoreItems property
Scrollable long list	Set MaxHeight + ScrollBarVisibility="Visible" on group
Resizable popup	IsResizable="True" on DropDownMenuGroup
Key Properties
Property	Type	Description
Label	string	Button text label
SizeMode	SizeMode	Small / Normal / Large
SmallIcon	ImageSource	Icon for Small and Normal modes
LargeIcon	ImageSource	Icon for Large mode
IconTemplate	DataTemplate	Vector/path icon template (overrides image icons)
IconTemplateSelector	DataTemplateSelector	Conditionally select icon template
IconWidth / IconHeight	double	Icon dimensions
DropDirection	DropDirection	Popup position (default: BottomLeft)
IsMultiLine	bool	Multi-line label (Large mode only)
DropDownMenuGroup.ItemsSource	IEnumerable	Data-bound menu items
DropDownMenuGroup.IconBarEnabled	bool	Show vertical icon bar
DropDownMenuGroup.ScrollBarVisibility	ScrollBarVisibility	Scrollbar in popup
DropDownMenuGroup.IsResizable	bool	Resize gripper on popup
DropDownMenuGroup.MoreItems	ObservableCollection<UIElement>	Custom bottom items
DropDownMenuItem.IsCheckable	bool	Allow check/uncheck
DropDownMenuItem.Command	ICommand	MVVM command
DropDownMenuItem.CommandParameter	object	Command parameter
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Assembly reference (Syncfusion.Shared.WPF)
Add via designer, XAML, or C#
Setting Label, SizeMode (Small/Normal/Large)
SmallIcon, LargeIcon, IconWidth/IconHeight
IconTemplate and IconTemplateSelector
Basic menu items inline
Applying themes with SfSkinManager
Dropdown Menu Items

📄 Read: references/dropdown-menu-items.md

DropDownMenuGroup as the container element
Declarative DropDownMenuItem with Header and Icon
IconBarEnabled (vertical icon strip)
ScrollBarVisibility for long item lists
IsResizable gripper for popup resize
IsCheckable / IsChecked for checkable items
MoreItems for custom UIElement additions
IsMoreItemsIconTrayEnabled
Data Binding

📄 Read: references/data-binding.md

Model and ViewModel pattern
Binding DropDownMenuGroup.ItemsSource
ItemTemplate with DataTemplate
Binding DropDownMenuItem.Command from ViewModel via x:Reference
Full MVVM example with DelegateCommand<T>
When to use data binding vs declarative items
Command Binding

📄 Read: references/command-binding.md

Command and CommandParameter on DropDownMenuItem
DelegateCommand<T> implementation
CanExecute and CanPerformAction toggle pattern
Binding to ViewModel commands in declarative XAML
Gotchas: scoping commands in DataTemplates
Dropdown Behavior

📄 Read: references/dropdown-behavior.md

DropDirection enum: Left, Right, BottomLeft, BottomRight, TopLeft, TopRight
Default direction is BottomLeft
IsMultiLine for wrapping long labels (Large mode only)
FlowDirection for RTL support
Events & Appearance

📄 Read: references/events-and-appearance.md

DropDownOpening / DropDownOpened events (cancel support)
DropDownClosing / DropDownClosed events
DropDownMenuItem.Click event
DropDownMenuItem.IsCheckedChanged event
Editing control template in Expression Blend or Visual Studio
SfSkinManager themes + ThemeStudio custom themes
Weekly Installs
46
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