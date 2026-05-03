---
rating: ⭐⭐
title: syncfusion-winforms-comboboxbase
url: https://skills.sh/syncfusion/winforms-ui-components-skills/syncfusion-winforms-comboboxbase
---

# syncfusion-winforms-comboboxbase

skills/syncfusion/winforms-ui-components-skills/syncfusion-winforms-comboboxbase
syncfusion-winforms-comboboxbase
Installation
$ npx skills add https://github.com/syncfusion/winforms-ui-components-skills --skill syncfusion-winforms-comboboxbase
SKILL.md
Implementing ComboBoxBase

Guides the implementation of the Syncfusion ComboBoxBase control for Windows Forms applications. ComboBoxBase provides a flexible alternative to the standard combo box by separating the edit portion from the drop-down list, enabling pluggable ListControl architecture.

When to Use This Skill

Use this skill when you need to:

Implement a flexible combo box with separated edit and dropdown architecture
Use custom ListControl-derived controls in dropdown areas
Integrate CheckedListBox for multi-select combo boxes
Create multi-column dropdowns using GridListControl
Handle complex selection events and dropdown behaviors
Need more control than standard Framework combo box provides
Build combo boxes with custom popup containers
Implement quick selection capability with mouse interactions

Note: If you need a Framework combo box-like object model, consider using ComboBoxAdv (based on ComboBoxBase but with identical object model).

Component Overview

The ComboBoxBase control separates the edit (TextBox) portion from the drop-down list portion, making the architecture powerful and flexible. You can plug in any ListControl-derived class (ListBox, CheckedListBox, GridListControl) using the ListControl property.

Key Capabilities:

Pluggable ListControl architecture
Support for ListBox, CheckedListBox, custom ListControls
Multi-column dropdowns with GridListControl
Comprehensive event handling for selection scenarios
Style and appearance customization
PopupControlContainer integration
QuickSelection with mouse interactions

Architecture Differences:

Unlike standard combo box, edit and list portions are separate
Different object model from Framework combo box
Properties like DataSource, ItemHeight set on ListControl, not ComboBoxBase
Events like SelectedIndexChanged handled on ListControl
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Installation and assembly references
Designer-based setup (drag-and-drop)
Code-based instantiation
Connecting ListBox to ComboBoxBase
DataSource configuration
Complete setup examples
ListControl Architecture

📄 Read: references/listcontrol-architecture.md

ListControl property explained
Creating custom ListControl-derived controls
Required properties and methods (Items, IndexFromPoint, TopIndex)
Collection classes (ObjectCollection, SelectedObjectCollection, SelectedIndexCollection)
QuickSelection capability implementation
GridListControl for multi-column dropdowns
Integration with various list controls
Event Handling

📄 Read: references/event-handling.md

Selection events (SelectionChangedCommitted, SelectedValueChanged, SelectedIndexChanged)
Event order and scenarios
DropDownCloseOnClick event for CheckedListBox
DropDown event for PopupControlContainer
Validating/Validated events
Complete CheckedListBox integration example
Appearance and Behavior

📄 Read: references/appearance-behavior.md

Style and FlatStyle properties
Border drawing customization
TextBox and dropdown window styling
Properties vs Framework combo box
ComboBoxAdv comparison
Visual styling examples
Advanced Scenarios

📄 Read: references/advanced-scenarios.md

CheckedListBox multi-select pattern
Custom PopupControlContainer derivation
OnPopup override for focus management
Nesting ComboBoxBase in PopupControlContainer
PopupParent and CurrentPopupChild relationships
Complex dropdown scenarios
Quick Start
Designer Setup

Step 1: Add ComboBoxBase to Form

1. Open your WinForms project in Visual Studio
2. Drag ComboBoxBase from Toolbox to Form
3. Drag ListBox from Toolbox to Form
4. In ComboBoxBase Properties, set ListControl = listBox1

Code Setup

Basic Implementation:

using Syncfusion.Windows.Forms.Tools;
using System.Windows.Forms;

public partial class Form1 : Form
{
    private ComboBoxBase comboBoxBase1;
    private ListBox listBox1;
    
    public Form1()
    {
        InitializeComponent();
        SetupComboBoxBase();
    }
    
    private void SetupComboBoxBase()
    {
        // Create ComboBoxBase and ListBox
        comboBoxBase1 = new ComboBoxBase();
        listBox1 = new ListBox();
        
        // Configure ComboBoxBase
        comboBoxBase1.Size = new Size(200, 25);
        comboBoxBase1.Location = new Point(20, 20);
        comboBoxBase1.ListControl = listBox1; // Connect ListBox
        
        // Add items to ListBox
        listBox1.Items.AddRange(new object[] {
            "Option 1",
            "Option 2",
            "Option 3",
            "Option 4"
        });
        
        // Add to form
        this.Controls.Add(listBox1);
        this.Controls.Add(comboBoxBase1);
    }
}


VB.NET:

Imports Syncfusion.Windows.Forms.Tools
Imports System.Windows.Forms

Public Class Form1
    Private comboBoxBase1 As ComboBoxBase
    Private listBox1 As ListBox
    
    Public Sub New()
        InitializeComponent()
        SetupComboBoxBase()
    End Sub
    
    Private Sub SetupComboBoxBase()
        ' Create ComboBoxBase and ListBox
        comboBoxBase1 = New ComboBoxBase()
        listBox1 = New ListBox()
        
        ' Configure ComboBoxBase
        comboBoxBase1.Size = New Size(200, 25)
        comboBoxBase1.Location = New Point(20, 20)
        comboBoxBase1.ListControl = listBox1 ' Connect ListBox
        
        ' Add items to ListBox
        listBox1.Items.AddRange(New Object() {
            "Option 1",
            "Option 2",
            "Option 3",
            "Option 4"
        })
        
        ' Add to form
        Me.Controls.Add(listBox1)
        Me.Controls.Add(comboBoxBase1)
    End Sub
End Class

Common Patterns
Pattern 1: ComboBoxBase with DataSource
// Create data source
List<string> states = new List<string> 
{ 
    "California", "Texas", "Florida", "New York" 
};

// Set DataSource on ListBox (not ComboBoxBase)
listBox1.DataSource = states;
comboBoxBase1.ListControl = listBox1;

Pattern 2: CheckedListBox Integration
// Use CheckedListBox for multi-select
CheckedListBox checkedListBox1 = new CheckedListBox();
checkedListBox1.Items.AddRange(new object[] {
    "Item 1", "Item 2", "Item 3", "Item 4"
});

comboBoxBase1.ListControl = checkedListBox1;

// Handle DropDownCloseOnClick to prevent premature closing
comboBoxBase1.DropDownCloseOnClick += (sender, e) => {
    e.Cancel = true; // Keep dropdown open while selecting
};

// Update text with checked items
checkedListBox1.ItemCheck += (sender, e) => {
    // Build text from checked items
    var checkedItems = checkedListBox1.CheckedItems.Cast<object>();
    comboBoxBase1.TextBox.Text = string.Join(", ", checkedItems);
};

Pattern 3: Custom Object DataSource
public class Employee
{
    public int Id { get; set; }
    public string Name { get; set; }
    public override string ToString() => Name;
}

// Create employee list
List<Employee> employees = new List<Employee>
{
    new Employee { Id = 1, Name = "John Doe" },
    new Employee { Id = 2, Name = "Jane Smith" },
    new Employee { Id = 3, Name = "Bob Johnson" }
};

listBox1.DataSource = employees;
listBox1.DisplayMember = "Name"; // Display property
listBox1.ValueMember = "Id";     // Value property

comboBoxBase1.ListControl = listBox1;

Key Properties
ComboBoxBase Properties
Property	Type	Description
ListControl	IListControl	Gets or sets the ListControl-derived control for dropdown
TextBox	TextBox	Gets the TextBox portion of the control
PopupContainer	PopupControlContainer	Gets the popup container for dropdown
Style	ComboBoxStyle	Gets or sets the visual style
FlatStyle	FlatStyle	Gets or sets the flat style appearance
Size	Size	Gets or sets the control size
ListControl Properties (Set on ListBox/CheckedListBox)
Property	Type	Description
Items	ObjectCollection	Collection of items in the list
DataSource	object	Data source for the list
DisplayMember	string	Property to display for objects
ValueMember	string	Property to use as value
SelectedItem	object	Currently selected item
SelectedIndex	int	Currently selected index
SelectionMode	SelectionMode	Single or multiple selection
Important Events
Event	Description
SelectionChangedCommitted	Fires when selection is committed by user action
DropDownCloseOnClick	Fires when dropdown is about to close on click (cancellable)
DropDown	Fires when dropdown is opening

Note: Events like SelectedIndexChanged are handled on the ListControl (ListBox), not ComboBoxBase.

Use Cases
Use Case 1: Simple Dropdown List

When you need a basic dropdown with items, use standard ListBox:

Display list of options
Single selection
Simple text items or object binding
Use Case 2: Multi-Select Dropdown

When users need to select multiple items, use CheckedListBox:

Filter selection (multiple categories)
Tag selection
Permission checkboxes
Multi-value inputs
Use Case 3: Multi-Column Dropdown

When displaying tabular data in dropdown, use GridListControl:

Employee selection with ID, Name, Department
Product selection with Code, Name, Price
Database record selection with multiple fields
Use Case 4: Custom List Controls

When built-in controls are insufficient, create custom ListControl:

Custom rendering with images/icons
Complex layouts
Specialized interaction patterns
Decision Guide

Choose ComboBoxBase over standard combo box when:

Need pluggable ListControl architecture
Want to use CheckedListBox or custom controls
Require multi-column dropdowns with GridListControl
Need fine-grained control over edit and list portions
Building complex dropdown scenarios

Choose standard combo box when:

Simple dropdown list is sufficient
Framework object model is preferred
No custom ListControl needed
Basic selection scenarios only

Choose ComboBoxAdv when:

Need ComboBoxBase flexibility
Prefer Framework combo box object model
Want both power and familiar API
Next Steps
Start with getting-started.md for basic setup
Read listcontrol-architecture.md for ListControl concepts
Review event-handling.md for selection events
Explore advanced-scenarios.md for complex use cases
Weekly Installs
30
Repository
syncfusion/winf…s-skills
GitHub Stars
1
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass