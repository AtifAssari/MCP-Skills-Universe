---
rating: ⭐⭐
title: syncfusion-wpf-propertygrid
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-propertygrid
---

# syncfusion-wpf-propertygrid

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-propertygrid
syncfusion-wpf-propertygrid
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-propertygrid
SKILL.md
Implementing PropertyGrid

Guide for implementing Syncfusion® WPF PropertyGrid control — a powerful property inspector for browsing and editing object properties with support for custom editors, category editors, collection editing, grouping, sorting, filtering, and nested properties.

When to Use This Skill

Use this skill when you need to:

Display object properties for browsing and editing
Create property inspectors similar to Visual Studio's Properties window
Implement custom value editors for specific property types
Group and categorize properties for better organization
Edit collection properties with add/remove/edit capabilities
Filter and search properties dynamically
Support nested properties with expandable property items
Customize property display with descriptions, display names, and tooltips
Implement design-time editors for visual configuration tools
Build configuration panels for application settings

This skill covers the complete PropertyGrid implementation including basic setup, property binding, editors, organization, and advanced customization.

Component Overview

Required assemblies:

Syncfusion.PropertyGrid.WPF
Syncfusion.SfInput.WPF
Syncfusion.SfShared.WPF
Syncfusion.Shared.WPF
Syncfusion.Tools.WPF

XAML namespace:

xmlns:syncfusion="http://schemas.syncfusion.com/wpf"


The PropertyGrid control provides an interface for browsing and editing properties of any object with:

Automatic Property Discovery - Reflects properties from any object automatically
Custom Value Editors - Assign custom controls for editing specific properties
Category Editors - Group related properties with custom editing UI
Collection Editor - Built-in dialog for editing collection properties (List, ObservableCollection)
Grouping & Sorting - Organize properties by category with multiple sort options
Filtering - Hide properties and search with built-in SearchBox
Nested Properties - Expand complex objects to show nested properties
Blendability - Design-time support in Blend and Visual Studio
Theming - Built-in theme support for consistent styling
MVVM Support - Full data binding and property change notification
Control Structure
PropertyGrid
├── SearchBox (optional) - Filter properties by name
├── Sort/Group Buttons - Toggle between sorted and categorized views
├── Property List
│   ├── Property Name Column
│   └── Value Editor Column (context-sensitive editors)
└── Description Panel (optional) - Shows property description

Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Installation and assembly deployment
Adding PropertyGrid via designer, XAML, and C#
Binding with SelectedObject
Populating properties automatically
Basic configuration and setup
Theme support

📄 Read: references/overview.md

Control structure and architecture
Feature overview and capabilities
Use cases and scenarios
When to use PropertyGrid

📄 Read: references/property-binding.md

SelectedObject binding
Data context configuration
INotifyPropertyChanged implementation
ObservableCollection usage
Dynamic property updates
Binding multiple objects
Editors and Customization

📄 Read: references/custom-editors.md

Creating custom editors (ITypeEditor interface)
Assigning editors via Editor attribute
CustomEditorCollection usage
Assigning by property name vs property type
EditorType vs Editor property
Constructor with parameters
Attach/Create/Detach methods
Custom editor controls

📄 Read: references/category-editors.md

CategoryEditor concept
Grouping related properties
EditorTemplate customization
Multiple property categorization
Visibility converters
Custom category layouts

📄 Read: references/collection-editor.md

Editing collection properties (List, ObservableCollection)
Add/remove items dialog
Editing collection as SelectedObject
Nested collection editing
Readonly mode configuration
CollectionEditorOpening event
IList type requirements

📄 Read: references/custom-property-definition.md

Manual PropertyItem definition
PropertyGridItem configuration
AutoGenerateItems property
Add/remove items at runtime
Custom DisplayName, Description, CategoryName
Custom editors and nested properties
Description panel templates
Organization Features

📄 Read: references/grouping.md

EnableGrouping property
Grouping by Category attribute
Group appearance customization
Expand/collapse behavior
Group button visibility

📄 Read: references/sorting.md

SortDirection property (Ascending, Descending, Null)
Sorting properties by name
Sorting categories
Order attribute for custom ordering
ButtonPanelVisibility for sort buttons
Disabling sort

📄 Read: references/filtering.md

HidePropertiesCollection for hiding properties
Browsable attribute (hide with false)
Bindable attribute (hide with false)
Display.AutoGenerateField attribute
AutoGeneratingPropertyGridItem event
SearchBox for filtering by name
SearchBoxVisibility property

📄 Read: references/nested-properties.md

PropertyExpandMode (FlatMode vs NestedMode)
NestedPropertyDisplayMode property
Expanding complex object properties
Update value on lost focus
Manual nested property definition
Appearance and Behavior

📄 Read: references/appearance.md

Visual styling and themes
Property name/value appearance
Description panel customization
DescriptionPanelVisibility property
Grid lines and spacing
Color customization

📄 Read: references/attached-properties.md

Using WPF attached properties
PropertyGrid-specific attached properties
Configuration examples

📄 Read: references/keyboard-navigation.md

Keyboard shortcuts
Tab navigation between properties
Enter/Escape behavior
Focus management

📄 Read: references/localization.md

Localization support
Resource file configuration
Culture-specific strings
Customizing built-in text

📄 Read: references/virtualization.md

VirtualizingMode property
Performance optimization for large property sets
Memory management
Scrolling behavior
Quick Start Example
Basic PropertyGrid Setup
<Window x:Class="PropertyGridSample.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:syncfusion="http://schemas.syncfusion.com/wpf">
    <Grid>
        <syncfusion:PropertyGrid Name="propertyGrid1" 
                                 SelectedObject="{Binding SelectedEmployee}"
                                 Width="400" Height="500">
            <syncfusion:PropertyGrid.DataContext>
                <local:ViewModel/>
            </syncfusion:PropertyGrid.DataContext>
        </syncfusion:PropertyGrid>
    </Grid>
</Window>

// Employee class to be explored in PropertyGrid
public class Employee : INotifyPropertyChanged
{
    private string name;
    public string Name 
    { 
        get => name; 
        set { name = value; OnPropertyChanged(nameof(Name)); } 
    }
    
    [Display(Name = "Employee ID")]
    [Description("Unique identifier for the employee")]
    public string ID { get; set; }
    
    [Category("Personal Info")]
    [DisplayName("Date of Birth")]
    public DateTime DOB { get; set; }
    
    [Category("Personal Info")]
    [Range(18, 65)]
    public int Age { get; set; }
    
    [Browsable(false)] // Hide this property
    public string InternalCode { get; set; }
    
    public event PropertyChangedEventHandler PropertyChanged;
    protected void OnPropertyChanged(string propertyName) =>
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
}

// ViewModel
public class ViewModel
{
    public object SelectedEmployee { get; set; }
    
    public ViewModel()
    {
        SelectedEmployee = new Employee
        {
            Name = "Johnson",
            Age = 25,
            ID = "EMP001",
            DOB = new DateTime(1999, 5, 15)
        };
    }
}

Common Patterns
Pattern 1: Custom Editor for Email Property
// Custom Editor with email validation mask
public class EmailEditor : ITypeEditor
{
    SfMaskedEdit maskedEdit;
    
    public object Create(PropertyInfo propertyInfo)
    {
        maskedEdit = new SfMaskedEdit
        {
            MaskType = MaskType.RegEx,
            Mask = "[A-Za-z0-9._%-]+@[A-Za-z0-9]+.[A-Za-z]{2,3}"
        };
        return maskedEdit;
    }
    
    public void Attach(PropertyViewItem property, PropertyItem info)
    {
        var binding = new Binding("Value")
        {
            Mode = BindingMode.TwoWay,
            Source = info,
            ValidatesOnExceptions = true,
            ValidatesOnDataErrors = true
        };
        BindingOperations.SetBinding(maskedEdit, SfMaskedEdit.ValueProperty, binding);
    }
    
    public void Detach(PropertyViewItem property) { }
}

// Apply to property
public class Employee
{
    [Editor("EmailID", typeof(EmailEditor))]
    public string EmailID { get; set; }
}

Pattern 2: Grouping Properties by Category
public class Employee
{
    [Category("Basic Info")]
    public string Name { get; set; }
    
    [Category("Basic Info")]
    public string ID { get; set; }
    
    [Category("Contact Details")]
    public string Email { get; set; }
    
    [Category("Contact Details")]
    public string Phone { get; set; }
}

<syncfusion:PropertyGrid SelectedObject="{Binding Employee}"
                         EnableGrouping="True"/>

Pattern 3: Editing Collection Properties
public class Product
{
    public string ProductName { get; set; }
    
    // Collection property - automatically gets collection editor
    public ObservableCollection<Customer> Customers { get; set; }
    
    public Product()
    {
        Customers = new ObservableCollection<Customer>
        {
            new Customer { ID = 1, Name = "John" },
            new Customer { ID = 2, Name = "Jane" }
        };
    }
}

public class Customer
{
    public int ID { get; set; }
    public string Name { get; set; }
}

Pattern 4: Override Property Items at Runtime
private void PropertyGrid_AutoGeneratingPropertyGridItem(
    object sender, AutoGeneratingPropertyGridItemEventArgs e)
{
    // Hide specific properties
    if (e.DisplayName == "InternalCode")
    {
        e.Cancel = true;
    }
    
    // Make property readonly
    if (e.DisplayName == "ID")
    {
        e.ReadOnly = true;
    }
    
    // Change display name
    if (e.DisplayName == "DOB")
    {
        e.DisplayName = "Date of Birth";
    }
    
    // Change category
    if (e.DisplayName == "Age")
    {
        e.Category = "Personal Information";
    }
}

Pattern 5: Property Value Changed Notification
private void PropertyGrid_ValueChanged(object sender, ValueChangedEventArgs e)
{
    var changedProperty = e.Property;
    var oldValue = e.OldValue;
    var newValue = e.NewValue;
    
    // Log the change
    Console.WriteLine($"{changedProperty.Name} changed from {oldValue} to {newValue}");
    
    // React to specific property changes
    if (changedProperty.Name == "Age")
    {
        // Validate or update related properties
    }
}

Key Properties
Core Properties
Property	Type	Description
SelectedObject	object	The object whose properties are displayed
SelectedObjects	object[]	Multiple objects for common property editing
EnableGrouping	bool	Groups properties by category
SortDirection	ListSortDirection?	Sorts properties (Ascending, Descending, null)
PropertyExpandMode	PropertyExpandModes	FlatMode or NestedMode for complex objects
AutoGenerateItems	bool	Auto-generates property items (default: true)
UI Configuration
Property	Type	Description
SearchBoxVisibility	Visibility	Shows/hides the search box
ButtonPanelVisibility	Visibility	Shows/hides sort/group buttons
DescriptionPanelVisibility	Visibility	Shows/hides description panel
EnableToolTip	bool	Enables tooltips on property items
DisableAnimationOnObjectSelection	bool	Disables loading animation
Collections
Property	Type	Description
HidePropertiesCollection	ObservableCollection	Property names to hide
CustomEditorCollection	CustomEditorCollection	Custom editors for properties
Items	PropertyGridItemCollection	Manually defined property items
Events
Event	Description
AutoGeneratingPropertyGridItem	Fired when a property item is being created (can cancel or modify)
ValueChanged	Fired when a property value changes
SelectedPropertyItemChanged	Fired when the selected property changes
CollectionEditorOpening	Fired before collection editor opens (can cancel or set readonly)
Common Use Cases
1. Application Settings Editor

Display and edit application configuration with grouped categories (Appearance, Behavior, Performance).

2. Design-Time Property Inspector

Create visual designers for custom controls or components with property editing.

3. Object Inspector in Development Tools

Build debugging or inspection tools to view and modify object properties at runtime.

4. Dynamic Configuration Panels

Generate configuration UI automatically from data model classes without manual form design.

5. Data Entry Forms with Complex Objects

Display nested object properties with collections, allowing users to edit hierarchical data.

6. Report Parameter Configuration

Allow users to configure report parameters with appropriate editors for each data type.

7. Game/Application Asset Editor

Edit properties of game objects, scenes, or assets with custom editors for vectors, colors, resources.

8. Business Rule Configuration

Define and edit business rules with property-based configuration and validation.

Related Components
PropertyGridItem - Individual property item representation
CustomEditor - Custom value editor configuration
CategoryEditor - Category-based property grouping
Collection Editor - Built-in collection editing dialog
Best Practices

Use Attributes for Metadata

Apply [Category], [Description], [DisplayName] attributes to properties
Use [Browsable(false)] to hide properties instead of code-based filtering

Implement INotifyPropertyChanged

Ensure your data objects implement property change notification
Use ObservableCollection for collection properties

Custom Editors for Complex Types

Create custom editors for types that don't have suitable default editors
Consider user experience when designing custom editor UI

Performance with Large Objects

Use virtualization for objects with many properties
Consider lazy loading for nested properties
Filter unnecessary properties early

Validation

Use data annotations for validation ([Required], [Range], etc.)
Handle validation errors gracefully in custom editors

Accessibility

Ensure custom editors support keyboard navigation
Provide meaningful descriptions for screen readers
Test with high contrast themes
Troubleshooting
Properties Not Showing
Verify [Browsable] attribute is not false
Check if property is in HidePropertiesCollection
Ensure property has public getter
Verify AutoGenerateItems is true
Custom Editor Not Applied
Check editor is properly registered in CustomEditorCollection
Verify property name/type matches
Ensure editor implements ITypeEditor correctly
Check Create method returns valid control
Collection Editor Not Opening
Verify collection type derives from IList
Ensure collection property has setter
Check collection type has parameterless constructor
Verify CollectionEditorOpening event doesn't cancel
Performance Issues
Enable virtualization for large property sets
Reduce nested property depth
Filter unnecessary properties
Consider manual property definition instead of auto-generation

Next Steps: Navigate to specific reference documents above based on your implementation needs. Start with getting-started.md for initial setup, then explore editors and organization features as needed.

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