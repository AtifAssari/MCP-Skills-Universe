---
rating: ⭐⭐
title: syncfusion-wpf-kanban-board
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-kanban-board
---

# syncfusion-wpf-kanban-board

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-kanban-board
syncfusion-wpf-kanban-board
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-kanban-board
SKILL.md
Implementing Syncfusion WPF Kanban (SfKanban)

This skill provides comprehensive guidance for implementing the Syncfusion® WPF Kanban (SfKanban) control, a powerful visual workflow management system that displays tasks as cards organized across columns representing different workflow stages.

When to Use This Skill

Use this skill immediately when:

User wants to create a Kanban board for task or project management
Building workflow visualization systems (to-do, in-progress, done)
Implementing agile project tracking boards
Need work-in-progress (WIP) limits per workflow stage
Creating task boards with drag-and-drop functionality
Organizing tasks by teams, projects, or custom criteria using swim lanes
Managing software development workflows or issue tracking systems
Need to visualize task status across multiple stages
Component Overview

The Syncfusion WPF Kanban (SfKanban) provides an efficient way to visualize workflows at each stage of completion. It offers:

Core Features:

Cards: Visual representation of tasks with title, description, tags, images, and priority indicators
Columns: Organize work into workflow stages (e.g., Open, In Progress, Done)
Swim Lanes: Group cards by projects, teams, users, or custom categories
Work-in-Progress (WIP) Limits: Set minimum/maximum task limits per column to prevent overload
Drag and Drop: Intuitive card movement between columns and swim lanes
Workflows: Define allowed card transitions between specific states
Sorting: Organize cards within columns by priority, date, or custom fields
Events: Rich event model for card interactions (tap, drag, drop)
Customization: Extensive template support for cards, headers, and swim lanes
Theming: Built-in light and dark themes with system integration
Localization & RTL: Support for multiple languages and right-to-left rendering
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Use when user needs:

Initial setup and installation via NuGet
Creating basic Kanban board
Understanding ItemsSource binding
Using default KanbanModel vs custom data models
Setting up auto-generated or manual columns
Applying themes, localization, and RTL support
Cards Configuration

📄 Read: references/cards.md

Use when user needs:

Understanding card structure and properties
Customizing card appearance with CardTemplate
Working with card indicators and tags
Implementing conditional card templates (CardTemplateSelector)
Enabling and customizing card tooltips
Troubleshooting card display issues
Columns Management

📄 Read: references/columns.md

Use when user needs:

Configuring column widths (minimum, maximum, exact)
Auto-generating vs manually defining columns
Mapping categories to columns
Customizing column headers
Expanding/collapsing columns programmatically
Enabling/disabling drag-and-drop per column
Setting up multi-category columns
Configuring WIP (Work-in-Progress) limits with visual indicators
Customizing drag/drop placeholder appearance
Swim Lanes Organization

📄 Read: references/swimlanes.md

Use when user needs:

Grouping cards by teams, projects, or users
Enabling and configuring swim lanes
Mapping swim lane properties (SwimlaneKey)
Customizing swim lane header appearance
Creating hierarchical card organization
Implementing team-based or project-based views
Workflows and Transitions

📄 Read: references/workflows.md

Use when user needs:

Defining allowed card transitions between columns
Restricting card movement between specific states
Implementing workflow validation rules
Preventing drag-and-drop to specific columns
Creating state machine-like workflows
Managing complex workflow transitions
Card Sorting

📄 Read: references/sorting.md

Use when user needs:

Sorting cards within columns by priority, date, or custom fields
Implementing custom field sorting (ascending/descending)
Setting up index-based sorting for precise positioning
Dynamically updating sort order after drag-and-drop
Refreshing column display after sorting changes
Understanding sorting with custom data models
Events and Interactions

📄 Read: references/events.md

Use when user needs:

Handling card tap events (CardTapped)
Responding to drag events (CardDragStarting, CardDragOver)
Processing card drop events (CardDrop)
Implementing MVVM commands (CardTappedCommand)
Accessing event arguments and card data
Preventing or customizing drag-and-drop behavior
Implementing business logic on card interactions
Quick Start Example
Basic Kanban Setup
<Window xmlns:kanban="clr-namespace:Syncfusion.UI.Xaml.Kanban;assembly=Syncfusion.SfKanban.WPF">
    <kanban:SfKanban x:Name="kanban" 
                     ItemsSource="{Binding TaskDetails}">
        <kanban:SfKanban.DataContext>
            <local:ViewModel/>
        </kanban:SfKanban.DataContext>
    </kanban:SfKanban>
</Window>

ViewModel with KanbanModel
using Syncfusion.UI.Xaml.Kanban;

public class ViewModel
{
    public ObservableCollection<KanbanModel> TaskDetails { get; set; }

    public ViewModel()
    {
        TaskDetails = new ObservableCollection<KanbanModel>
        {
            new KanbanModel
            {
                Title = "UWP Issue",
                ID = "651",
                Description = "Fix crosshair label template issue",
                Category = "Open",
                ColorKey = "High",
                Tags = new string[] { "Bug Fixing" }
            },
            new KanbanModel
            {
                Title = "Kanban Feature",
                ID = "25678",
                Description = "Implement drag and drop support",
                Category = "In Progress",
                ColorKey = "Normal",
                Tags = new string[] { "New Feature" }
            }
        };
    }
}

Manual Column Definition
<kanban:SfKanban AutoGenerateColumns="False" 
                 ItemsSource="{Binding TaskDetails}">
    <kanban:KanbanColumn Title="To Do" Categories="Open" />
    <kanban:KanbanColumn Title="In Progress" Categories="In Progress" />
    <kanban:KanbanColumn Title="Done" Categories="Done" />
</kanban:SfKanban>

Common Patterns
Pattern 1: Auto-Generated Columns

When: User wants quick setup with columns generated from data

// Columns automatically generated from Category property values
kanban.AutoGenerateColumns = true;
kanban.ItemsSource = viewModel.TaskDetails;


Result: Columns created automatically based on unique Category values in data

Pattern 2: WIP Limits with Visual Indicators

When: User needs to limit tasks per stage and show visual feedback

<kanban:KanbanColumn Title="In Progress" 
                     Categories="In Progress"
                     MinimumLimit="2" 
                     MaximumLimit="5" />


Result:

Error bar shows red when count exceeds MaximumLimit
Error bar shows yellow when count is below MinimumLimit
Helps prevent workflow bottlenecks
Pattern 3: Custom Card Template

When: User needs custom card appearance beyond default

<kanban:SfKanban.CardTemplate>
    <DataTemplate>
        <Border Background="#F3CFCE" 
                BorderThickness="1" 
                CornerRadius="3">
            <StackPanel Margin="10">
                <TextBlock Text="{Binding Title}" 
                          FontWeight="Bold" 
                          FontSize="14" />
                <TextBlock Text="{Binding Description}" 
                          FontSize="12" 
                          TextWrapping="Wrap" />
            </StackPanel>
        </Border>
    </DataTemplate>
</kanban:SfKanban.CardTemplate>


DataContext: KanbanModel instance

Pattern 4: Swim Lanes by Team

When: User wants to organize cards by teams or projects

<kanban:SfKanban SwimlaneKey="Assignee" 
                 ItemsSource="{Binding TaskDetails}">
    <!-- Cards grouped by Assignee property -->
</kanban:SfKanban>


Result: Horizontal swim lane rows, one per unique Assignee value

Pattern 5: Workflow Restrictions

When: User wants to enforce specific card transition rules

<kanban:SfKanban.Workflows>
    <kanban:KanbanWorkflow Category="Open">
        <kanban:KanbanWorkflow.AllowedTransitions>
            <x:String>In Progress</x:String>
        </kanban:KanbanWorkflow.AllowedTransitions>
    </kanban:KanbanWorkflow>
    <kanban:KanbanWorkflow Category="In Progress">
        <kanban:KanbanWorkflow.AllowedTransitions>
            <x:String>Done</x:String>
            <x:String>Won't Fix</x:String>
        </kanban:KanbanWorkflow.AllowedTransitions>
    </kanban:KanbanWorkflow>
</kanban:SfKanban.Workflows>


Result:

Cards in "Open" can only move to "In Progress"
Cards in "In Progress" can only move to "Done" or "Won't Fix"
Prevents invalid state transitions
Pattern 6: Custom Data Model

When: User has existing data model, not using KanbanModel

// Custom model
public class TaskDetails
{
    public string Title { get; set; }
    public string Description { get; set; }
    public string Status { get; set; }
}

// XAML
<kanban:SfKanban ItemsSource="{Binding Tasks}"
                 ColumnMappingPath="Status">
    <kanban:SfKanban.CardTemplate>
        <!-- Define custom template -->
    </kanban:SfKanban.CardTemplate>
</kanban:SfKanban>


Important: Must define CardTemplate when using custom model

Key Properties
SfKanban Properties
Property	Type	Purpose	When to Use
ItemsSource	object	Data source for cards	Always (required)
AutoGenerateColumns	bool	Auto-create columns from Category	Quick setup vs custom control
Columns	Collection	Manual column definitions	When AutoGenerateColumns = false
ColumnMappingPath	string	Property for column categorization	Custom models (default: "Category")
SwimlaneKey	string	Property for swim lane grouping	Organizing by teams/projects
CardTemplate	DataTemplate	Custom card appearance	Custom data models or styling
ColumnHeaderTemplate	DataTemplate	Custom column header	Branding or additional info
SwimlaneHeaderTemplate	DataTemplate	Custom swim lane header	Custom swim lane display
MinColumnWidth	double	Minimum column width	Responsive layouts
MaxColumnWidth	double	Maximum column width	Controlling column size
ColumnWidth	double	Fixed column width	Uniform column sizing
SortingMappingPath	string	Property for sorting cards	Ordering cards by priority/date
SortingOrder	enum	Ascending or Descending	Sort direction
Workflows	Collection	Allowed card transitions	Workflow validation
IndicatorColorPalette	Collection	Color mapping for indicators	Priority/status colors
IsToolTipEnabled	bool	Enable card tooltips	Additional card info on hover
KanbanColumn Properties
Property	Type	Purpose	When to Use
Title	string	Column display name	Custom column titles
Categories	string	Comma-separated categories	Mapping data to column
MinimumLimit	int	WIP minimum limit	Workflow management
MaximumLimit	int	WIP maximum limit	Preventing overload
AllowDrag	bool	Enable dragging from column	Controlling card movement
AllowDrop	bool	Enable dropping to column	Restricting drops
IsExpanded	bool	Column collapsed/expanded state	UI state control
KanbanModel Properties
Property	Type	Description	Display Location
Title	string	Card heading	Top, bold text
ID	object	Unique identifier	Not displayed in default UI
Description	string	Detailed text	Below title
Category	object	Column assignment	Determines column placement
Assignee	string	Assigned person	Used for swim lane grouping
ColorKey	object	Priority/status key	Color bar on card
Tags	string[]	Labels/categories	Bottom of card
ImageURL	Uri	Avatar/icon	Right side of card
Common Use Cases
1. Software Development Task Board

Scenario: Track bugs and features through development stages

<kanban:SfKanban ItemsSource="{Binding Issues}">
    <kanban:KanbanColumn Title="Backlog" Categories="Open,New" />
    <kanban:KanbanColumn Title="In Development" 
                         Categories="In Progress" 
                         MaximumLimit="3" />
    <kanban:KanbanColumn Title="Testing" 
                         Categories="Testing" 
                         MaximumLimit="5" />
    <kanban:KanbanColumn Title="Done" 
                         Categories="Closed,Resolved" />
</kanban:SfKanban>

2. Team-Based Project Management

Scenario: Organize tasks by team members with swim lanes

<kanban:SfKanban SwimlaneKey="Assignee" 
                 ItemsSource="{Binding ProjectTasks}">
    <kanban:SfKanban.SwimlaneHeaderTemplate>
        <DataTemplate>
            <StackPanel Orientation="Horizontal">
                <Image Source="{Binding Image}" Width="30" Height="30"/>
                <TextBlock Text="{Binding Title}" Margin="10,0"/>
            </StackPanel>
        </DataTemplate>
    </kanban:SfKanban.SwimlaneHeaderTemplate>
</kanban:SfKanban>

3. Priority-Based Sorting

Scenario: Sort cards by priority within each column

<kanban:SfKanban SortingMappingPath="Priority"
                 SortingOrder="Descending"
                 ItemsSource="{Binding Tasks}"
                 CardDragEnd="OnCardDrop">
    <!-- Columns -->
</kanban:SfKanban>

 private void OnCardDrop(object sender, KanbanDragEndEventArgs e)
 {
     kanban.RefreshKanbanColumn(e.TargetKey.ToString());
 }

4. Interactive Card Actions

Scenario: Handle card taps to show details dialog

kanban.CardTapped += (s, e) => {
    var card = e.SelectedCard.DataContext as KanbanModel;
    var dialog = new TaskDetailsDialog(card);
    await dialog.ShowAsync();
};

Troubleshooting
Issue: Columns Not Showing

Symptoms: Kanban board is empty, no columns visible

Solutions:

Verify AutoGenerateColumns is true OR Columns are manually defined
Check ItemsSource is bound correctly
Ensure Category property has values in data
If using ColumnMappingPath, verify property exists in model
Issue: Cards Not Displaying

Symptoms: Columns show but cards are missing

Solutions:

Check ItemsSource has data
Verify Category values match column Categories
If using custom model, ensure CardTemplate is defined
Check DataContext is set correctly
Issue: Drag-and-Drop Not Working

Symptoms: Cannot move cards between columns

Solutions:

Verify AllowDrag=true on source column (default is true)
Ensure Workflows don't restrict the transition
Check if columns have correct Categories mapping
Issue: WIP Limits Not Working

Symptoms: Visual indicators not showing for WIP limits

Solutions:

Verify MinimumLimit and/or MaximumLimit are set on columns
Check card count actually exceeds/is below limits
Ensure theme resources are loaded correctly
Issue: Swim Lanes Not Grouping

Symptoms: All cards in single row, no swim lanes

Solutions:

Verify SwimlaneKey property is set
Check mapped property exists in data model
Ensure property has varying values in data
If using KanbanModel, default is "Assignee"
Issue: Sorting Not Applied

Symptoms: Cards not sorted after drag-and-drop

Solutions:

Call RefreshKanbanColumn() in CardDrop event
Verify SortingMappingPath is set to valid property
Check property type is sortable (string, int, DateTime, etc.)
Ensure SortingOrder is specified (Ascending/Descending)
Best Practices
Use KanbanModel for Quick Start: Built-in model with default card UI saves development time
Custom Models Require Templates: Always define CardTemplate when using custom data models
Set WIP Limits: Implement MinimumLimit/MaximumLimit to prevent workflow bottlenecks
Handle CardDrop for Sorting: Call RefreshKanbanColumn() after drop when using sorting
Use Workflows for Validation: Prevent invalid state transitions with Workflows property
Optimize Column Width: Set MinColumnWidth/MaxColumnWidth for responsive layouts
Leverage Swim Lanes: Group cards by logical categories (teams, projects, priorities)
Customize Indicators: Define IndicatorColorPalette for clear visual prioritization
Enable Tooltips: Set IsToolTipEnabled=true for additional card information
Test Themes: Verify appearance in both light and dark modes
Edge Cases and Gotchas

Multiple Categories per Column:

Use comma-separated values: Categories="Open,New,Backlog"
All matching cards appear in single column

Custom Model Requirements:

MUST define CardTemplate (default template requires KanbanModel)
MUST set ColumnMappingPath if not using "Category" property name
DataContext for template is your custom model instance

Workflow Restrictions:

Empty AllowedTransitions = no drops allowed
Not defining workflow for a category = allows all transitions
Workflow Category must match exact Category value in data

Sorting with Drag-Drop:

Sorting doesn't auto-apply after drop
Must manually call RefreshKanbanColumn() in CardDrop event
Index-based sorting requires custom implementation in event handlers

Swim Lane Grouping:

Default swim lane key is "Assignee" for KanbanModel
Custom models must set SwimlaneKey explicitly
Null or empty values create single "ungrouped" swim lane
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