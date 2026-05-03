---
title: syncfusion-wpf-card-view
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-card-view
---

# syncfusion-wpf-card-view

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-card-view
syncfusion-wpf-card-view
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-card-view
SKILL.md
Implementing CardView (WPF)

A panel control that organizes items as visual cards with built-in grouping, sorting, filtering, and inline editing.

When to Use This Skill

Use this skill when the user needs to:

Display a collection of data items as cards in a WPF application
Enable grouping, sorting, or filtering of card items
Add inline editing to card items (F2 / double-click)
Customize card header, body, or edit UI via templates
Bind card items to an ObservableCollection (MVVM)
Apply themes or localize CardView strings

Note: Grouping, sorting, filtering, and editing require ItemsSource data binding. These features do not work with declarative CardViewItem children.

Component Overview
Class	Namespace	Purpose
CardView	Syncfusion.Windows.Tools.Controls	Container panel for card items
CardViewItem	Syncfusion.Windows.Tools.Controls	Individual card (declarative use)

Required Assemblies: Syncfusion.Shared.WPF + Syncfusion.Tools.WPF

XAML Namespace:

xmlns:syncfusion="http://schemas.syncfusion.com/wpf"

Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Assembly and namespace setup
Add CardView via designer, XAML, or C#
Declarative CardViewItem approach
ItemsSource data binding approach
SelectedItem, IsSelected, SelectedItemChanged
Orientation (Horizontal / Vertical)
SfSkinManager theme setup
Data Binding & Templates

📄 Read: references/data-binding-and-templates.md

Full Model + ViewModel + ObservableCollection pattern
HeaderTemplate — card header display
ItemTemplate — card body in view mode
EditItemTemplate — card body in edit mode
ItemContainerStyle and ItemContainerStyleSelector
FlowDirection for RTL layouts
SfSkinManager visual styles reference
Grouping

📄 Read: references/grouping.md

CanGroup enable/disable
Drag-drop fields to group header
GroupCards(string) programmatic grouping
Nested / multi-level grouping
ShowHeader to hide the grouping region
Sorting & Filtering

📄 Read: references/sorting-and-filtering.md

CanSort enable/disable; click field name to cycle sort order
Sorting grouped items via drop region
Filtering via popup-based field value selection (enabled when ShowHeader="True")
Clear Filter button behavior
ShowHeader to hide sorting/filtering header
Editing

📄 Read: references/editing.md

CanEdit enable/disable (default false)
F2 / double-click to enter edit mode; Esc/Enter to exit
EditItemTemplate requirement and pattern
BeginEdit() / EndEdit() programmatic control
Custom edit UI styling
Localization

📄 Read: references/localization.md

CurrentUICulture setup
Resource file naming convention
Name/Value pair configuration
French culture example
Quick Start Example

Minimal CardView with data binding and grouping/sorting:

<!-- MainWindow.xaml -->
<Window xmlns:syncfusion="http://schemas.syncfusion.com/wpf">
    <Window.DataContext>
        <local:ViewModel/>
    </Window.DataContext>
    <syncfusion:CardView ItemsSource="{Binding CardViewItems}"
                         CanGroup="True"
                         CanSort="True"
                         Name="cardView">
        <syncfusion:CardView.HeaderTemplate>
            <DataTemplate>
                <TextBlock Text="{Binding FirstName}"/>
            </DataTemplate>
        </syncfusion:CardView.HeaderTemplate>
        <syncfusion:CardView.ItemTemplate>
            <DataTemplate>
                <ListBox ScrollViewer.HorizontalScrollBarVisibility="Disabled">
                    <ListBoxItem>
                        <StackPanel Orientation="Horizontal">
                            <TextBlock Text="Name: " FontWeight="Bold"/>
                            <TextBlock Text="{Binding FirstName}"/>
                        </StackPanel>
                    </ListBoxItem>
                    <ListBoxItem>
                        <StackPanel Orientation="Horizontal">
                            <TextBlock Text="Age: " FontWeight="Bold"/>
                            <TextBlock Text="{Binding Age}"/>
                        </StackPanel>
                    </ListBoxItem>
                </ListBox>
            </DataTemplate>
        </syncfusion:CardView.ItemTemplate>
    </syncfusion:CardView>
</Window>

// ViewModel.cs
public class ViewModel : NotificationObject
{
    private ObservableCollection<Person> _items;
    public ObservableCollection<Person> CardViewItems
    {
        get => _items;
        set { _items = value; RaisePropertyChanged(nameof(CardViewItems)); }
    }
    public ViewModel()
    {
        CardViewItems = new ObservableCollection<Person>
        {
            new Person { FirstName = "Alice", LastName = "Smith", Age = 30 },
            new Person { FirstName = "Bob",   LastName = "Jones", Age = 25 },
            new Person { FirstName = "Carol", LastName = "Smith", Age = 28 },
        };
    }
}

Common Patterns
Scenario	Properties / Methods
Enable all interactive modes	CanGroup="True" CanSort="True" CanEdit="True"
Programmatic group by field	cardView.GroupCards("LastName")
Programmatic edit control	cardView.BeginEdit() / cardView.EndEdit()
Hide group/sort/filter header	ShowHeader="False"
RTL layout	FlowDirection="RightToLeft"
React to selection	Handle SelectedItemChanged event
Apply theme	SfSkinManager.SetVisualStyle(cardView, VisualStyles.FluentLight)
Key Properties
Property	Type	Default	Description
ItemsSource	IEnumerable	null	Data collection to bind
SelectedItem	object	null	Currently selected card
Orientation	Orientation	Horizontal	Card layout direction
CanGroup	bool	false	Enable drag-drop grouping
CanSort	bool	true	Enable field click sorting
CanEdit	bool	false	Enable inline editing
ShowHeader	bool	true	Show/hide group/sort/filter header
HeaderTemplate	DataTemplate	—	Card header display template
ItemTemplate	DataTemplate	—	Card body in view mode
EditItemTemplate	DataTemplate	—	Card body in edit mode
ItemContainerStyle	Style	—	Style applied to each card container
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