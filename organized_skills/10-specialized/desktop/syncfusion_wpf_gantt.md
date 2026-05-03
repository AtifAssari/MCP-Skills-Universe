---
rating: ⭐⭐
title: syncfusion-wpf-gantt
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-gantt
---

# syncfusion-wpf-gantt

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-gantt
syncfusion-wpf-gantt
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-gantt
SKILL.md
Implementing WPF Gantt Control

Comprehensive guide for implementing the Syncfusion® Essential Gantt control for WPF applications. The Gantt control is an MS Project-like project management viewer with built-in grid, schedule, and resource assignment capabilities designed to help project managers develop plans, assign resources, track task progress, and manage project timelines.

When to Use This Skill

Use this skill when you need to:

Implement project management features in WPF applications
Visualize task timelines with Gantt chart representations
Create task hierarchies with parent-child relationships
Configure task dependencies with predecessor/successor relationships
Enable drag-and-drop for task scheduling and date adjustments
Track project progress with baselines and progress indicators
Manage resources and assign them to tasks
Customize Gantt visuals with custom nodes, tooltips, and styles
Import/export project data from/to XML format
Implement zooming and timeline navigation
Add filtering and sorting for task management
Support localization for international projects

This skill covers the complete Gantt control implementation from basic setup to advanced customization.

Component Overview
Architecture

The Essential Gantt control is composed of three main components:

GanttGrid - Table view displaying scheduled tasks with hierarchy and editable fields
GanttChart - Graphical representation showing task bars, milestones, and dependencies
ScheduleHeader - Timeline header for measuring and tracking progress
Key Capabilities

Task Management:

Hierarchical task structure (parent/child tasks)
Task properties (name, start/finish dates, duration, progress)
Milestone support for target dates
Task dependencies with connectors

Visual Features:

Progress indicators showing completion percentage
Custom node styles for different task types
Highlighting and strip lines for visual emphasis
Custom tooltips for detailed task information

Interactions:

Drag to adjust task start/finish dates
Drag-and-drop tasks within rows
Automatic synchronization between grid and chart
Zooming for different timeline scales

Data Operations:

MVVM-compatible data binding
ObservableCollection support
XML import/export for project data
Filtering and sorting capabilities
Data virtualization for large projects
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

When you need to:

Install and set up the Gantt control in your WPF project
Understand the Gantt control architecture and components
Add GanttControl programmatically or through XAML designer
Configure basic properties (ChartWidth, GridWidth)
Set schedule types and range padding
Configure auto-expand modes for task hierarchy
Apply themes to the Gantt control

Topics covered: Installation, control structure, class diagram, basic configuration, schedule types, auto-expand modes, theming

Data Binding & Task Management

📄 Read: references/data-binding.md

When you need to:

Create TaskDetails collections for project data
Bind data to GanttControl ItemsSource
Implement ViewModel pattern with ObservableCollection
Define task properties (ID, name, dates, progress)
Create parent-child task hierarchies
Configure external property binding
Assign resources to tasks
Follow data model best practices

Topics covered: TaskDetails binding, ObservableCollection, task properties, hierarchy creation, resource assignment, MVVM patterns

Scheduling & Time Management

📄 Read: references/task-scheduling.md

When you need to:

Configure schedule types (Hours, Days, Weeks, Months, Years)
Implement custom DateTime or numeric schedules
Customize calendars with working days and business hours
Define holidays and non-working days
Set schedule range padding for better visualization
Implement zooming functionality
Show date with time in GanttGrid
Manage timeline and schedule views

Topics covered: Schedule types, calendar customization, holidays, zooming, timeline management, schedule configuration

Task Relationships & Dependencies

📄 Read: references/task-relationships.md

When you need to:

Create dependency relationships between tasks
Configure predecessor and successor tasks
Implement connectors for visual dependencies
Enable auto-update hierarchy for cascading changes
Add baseline support for tracking original schedules
Track task progress against baselines
Implement milestones for project targets
Define different relationship types

Topics covered: Dependencies, connectors, auto-update hierarchy, baselines, milestones, relationship types, progress tracking

Visual Customization

📄 Read: references/customization.md

When you need to:

Apply custom node styles for different task types
Create custom tooltips with rich task information
Highlight specific tasks for emphasis
Add strip lines as visual guides on the timeline
Customize DateTime indicators
Style header nodes and task nodes
Customize progress indicators
Apply visual themes and templates
Implement conditional styling

Topics covered: Custom node styles, tooltips, highlighting, strip lines, DateTime indicators, themes, templates, conditional styling

Interactions & Drag-Drop

📄 Read: references/drag-drop-interaction.md

When you need to:

Enable drag support for adjusting task dates
Implement task bar dragging to change start/finish dates
Configure drag-and-drop for task reordering
Handle automatic data synchronization during drag operations
Respond to drag events
Configure drag behavior and constraints
Implement custom drag validation

Topics covered: Drag to resize, drag-and-drop reordering, event handling, synchronization, drag constraints

Data Operations

📄 Read: references/data-operations.md

When you need to:

Filter tasks based on criteria
Sort task lists by various properties
Implement data virtualization for large projects
Import project data from XML files
Export project data to XML format
Perform bulk operations on tasks
Search and filter task collections
Optimize performance with large datasets

Topics covered: Filtering, sorting, virtualization, XML import/export, bulk operations, search, performance optimization

Resource Management

📄 Read: references/resource-management.md

When you need to:

Implement resource view in Gantt
Configure Gantt inline items for resources
Assign resources to tasks
Create and manage resource collections
Track resource allocation across tasks
Implement multi-resource task assignments
Display resource information in the chart

Topics covered: Resource views, inline items, resource assignment, collections, allocation tracking, multi-resource tasks

Localization & Internationalization

📄 Read: references/localization.md

When you need to:

Configure flow direction (LTR/RTL) for different languages
Implement localization support
Apply culture-specific formatting
Manage multi-language resources
Format dates and times by locale
Localize resource strings and UI text
Support international project teams

Topics covered: Flow direction, localization, culture formatting, multi-language resources, date/time formatting, resource strings

Quick Start Example
Basic Gantt Control Implementation

Here's a minimal example to get started with the Gantt control:

XAML:

<Window x:Class="GanttDemo.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:syncfusion="http://schemas.syncfusion.com/wpf"
        Title="Project Management" Height="600" Width="1000">
    
    <syncfusion:GanttControl x:Name="ganttControl"
                             ItemsSource="{Binding TaskDetails}"
                             GridWidth="300"
                             ChartWidth="700">
        <syncfusion:GanttControl.DataContext>
            <local:ViewModel/>
        </syncfusion:GanttControl.DataContext>
    </syncfusion:GanttControl>
    
</Window>


ViewModel (C#):

using System;
using System.Collections.ObjectModel;
using Syncfusion.Windows.Controls.Gantt;

public class ViewModel
{
    public ObservableCollection<TaskDetails> TaskDetails { get; set; }

    public ViewModel()
    {
        TaskDetails = new ObservableCollection<TaskDetails>();
        
        // Create parent task
        var parentTask = new TaskDetails
        {
            TaskId = 1,
            TaskName = "Project Planning",
            StartDate = new DateTime(2024, 1, 1),
            FinishDate = new DateTime(2024, 1, 15),
            Progress = 40d
        };
        
        // Add child tasks
        parentTask.Child.Add(new TaskDetails
        {
            TaskId = 2,
            TaskName = "Define project scope",
            StartDate = new DateTime(2024, 1, 1),
            FinishDate = new DateTime(2024, 1, 5),
            Progress = 100d
        });
        
        parentTask.Child.Add(new TaskDetails
        {
            TaskId = 3,
            TaskName = "Gather requirements",
            StartDate = new DateTime(2024, 1, 6),
            FinishDate = new DateTime(2024, 1, 10),
            Progress = 50d
        });
        
        TaskDetails.Add(parentTask);
    }
}


Result: A functional Gantt control displaying project tasks with hierarchical structure, progress tracking, and timeline visualization.

Common Patterns
Pattern 1: Task Dependency Setup
// Create tasks with dependencies
var task1 = new TaskDetails 
{ 
    TaskId = 1, 
    TaskName = "Design", 
    StartDate = new DateTime(2024, 1, 1),
    FinishDate = new DateTime(2024, 1, 10)
};

var task2 = new TaskDetails 
{ 
    TaskId = 2, 
    TaskName = "Development",
    StartDate = new DateTime(2024, 1, 11),
    FinishDate = new DateTime(2024, 1, 25)
};

// Task2 depends on Task1 (Finish-to-Start)
task2.Predecessor.Add(new Predecessor { GanttTaskIndex = 1, GanttTaskRelationship = GanttTaskRelationship.FinishToStart });

TaskDetails.Add(task1);
TaskDetails.Add(task2);

Pattern 2: Resource Assignment
// Define resources
var resources = new ObservableCollection<Resource>
{
    new Resource { ID = 1, Name = "John Smith" },
    new Resource { ID = 2, Name = "Jane Doe" }
};

// Assign resources to task
var task = new TaskDetails
{
    TaskId = 1,
    TaskName = "Implementation",
    StartDate = new DateTime(2024, 1, 1),
    FinishDate = new DateTime(2024, 1, 15),
    Resources = resources
};

Pattern 3: Custom Schedule Type
<syncfusion:GanttControl x:Name="ganttControl"
                         ItemsSource="{Binding TaskDetails}"
                         ScheduleType="WeekWithDays"
                         ScheduleRangePadding="5">
</syncfusion:GanttControl>

// Or in code-behind
ganttControl.ScheduleType = ScheduleType.WeekWithDays;
ganttControl.ScheduleRangePadding = 5;

Pattern 4: Baseline Comparison
// Enable baseline support
var task = new TaskDetails
{
    TaskId = 1,
    TaskName = "Project Phase 1",
    StartDate = new DateTime(2024, 1, 1),
    FinishDate = new DateTime(2024, 2, 1),
    BaselineStart = new DateTime(2024, 1, 1),
    BaselineFinish = new DateTime(2024, 1, 25),  // Original plan
    Progress = 60d
};
// Actual finish extends beyond baseline - shows delay

Key Properties & API
Essential Properties
Property	Type	Description
ItemsSource	IEnumerable	Collection of TaskDetails to display
GridWidth	GridLength	Width of the Gantt grid section
ChartWidth	GridLength	Width of the Gantt chart section
ScheduleType	ScheduleType	Timeline scale (Hours, Days, Weeks, etc.)
ScheduleRangePadding	int	Padding in schedule units
AutoExpandMode	GanttAutoExpandMode	Initial expansion state of tasks
ShowDateWithTime	bool	Display time along with dates in grid
TaskDetails Properties
Property	Type	Description
TaskId	int	Unique identifier for the task
TaskName	string	Display name of the task
StartDate	DateTime	Task start date/time
FinishDate	DateTime	Task end date/time
Duration	TimeSpan	Task duration (calculated or set)
Progress	double	Completion percentage (0-100)
Child	Collection	Child tasks for hierarchy
Predecessor	Collection	Task dependencies
Resources	Collection	Assigned resources
Common Methods
ExpandAll() - Expand all task nodes
CollapseAll() - Collapse all task nodes
ExportToXML() - Export project to XML file
ImportFromXML() - Import project from XML file
Architecture Overview
┌─────────────────────────────────────────────────────────────┐
│                      GanttControl                            │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────────┐  ┌─────────────────────────────┐ │
│  │    GanttGrid         │  │   GanttChartVisualControl   │ │
│  │  ┌────────────────┐  │  │  ┌────────────────────────┐ │ │
│  │  │ Header         │  │  │  │  ScheduleHeader        │ │ │
│  │  ├────────────────┤  │  │  ├────────────────────────┤ │ │
│  │  │ Parent Task    │  │  │  │  ═══╗                  │ │ │
│  │  │  ├─ Child 1    │  │  │  │     ║═══════           │ │ │
│  │  │  └─ Child 2    │  │  │  │          ║═════════════║ │ │
│  │  │ Parent Task    │  │  │  │  ═══════════╗          │ │ │
│  │  │  ├─ Child 3    │  │  │  │            ║════       │ │ │
│  │  └────────────────┘  │  │  └────────────────────────┘ │ │
│  └──────────────────────┘  └─────────────────────────────┘ │
│                                                               │
│         Data: ObservableCollection<TaskDetails>              │
└─────────────────────────────────────────────────────────────┘

Common Use Cases
Software Project Management - Track development sprints, tasks, and milestones
Construction Planning - Manage construction phases, dependencies, and resources
Event Planning - Schedule event tasks, timelines, and resource allocation
Research Projects - Track research phases, experiments, and deliverables
Manufacturing Scheduling - Plan production tasks, dependencies, and resources
Marketing Campaigns - Manage campaign tasks, timelines, and team assignments
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