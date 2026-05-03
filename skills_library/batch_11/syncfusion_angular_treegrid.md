---
title: syncfusion-angular-treegrid
url: https://skills.sh/syncfusion/angular-ui-components-skills/syncfusion-angular-treegrid
---

# syncfusion-angular-treegrid

skills/syncfusion/angular-ui-components-skills/syncfusion-angular-treegrid
syncfusion-angular-treegrid
Installation
$ npx skills add https://github.com/syncfusion/angular-ui-components-skills --skill syncfusion-angular-treegrid
SKILL.md
Syncfusion Angular TreeGrid

Complete guide to implementing and customizing the Syncfusion Angular TreeGrid component for hierarchical data visualization.

⚠️ Security & Trust Boundary
The TreeGrid skill does not perform any remote data access.
All external API interaction is handled by a separate DataManager skill outside this skill’s trust boundary.
Table of Contents
When to Use This Skill
Data Structure Rules
Documentation Navigation Guide
Quick Start Example
Common Patterns
Best Practices
Key Props Summary
Module Injection
When to Use This Skill

Use this skill when you need to:

Display hierarchical or tree-structured data in a grid format
Implement advanced data manipulation (sorting, filtering, searching, editing)
Configure pagination, virtual scrolling for large datasets
Add export functionality (PDF, Excel)
Customize appearance with themes and CSS
Handle selection, aggregates, and state management
Support mobile/responsive design
Implement row/column freezing
Data Structure Rules
Rule 1: childMapping is MANDATORY for Hierarchical Data

Severity: 🔴 CRITICAL - Grid will not expand/collapse without this

Requirement:

// ✅ REQUIRED - Must match data property name exactly
<ejs-treegrid 
  [dataSource]='data'
  childMapping='subtasks'>  // Property name is case-sensitive
</ejs-treegrid>

// ❌ WRONG - Will not work
<ejs-treegrid 
  [dataSource]='data'>
  <!-- No expansion possible without childMapping -->
</ejs-treegrid>


Data Format:

// ✅ CORRECT - childMapping matches 'subtasks' property
public data = [
  {
    TaskID: 1,
    TaskName: 'Parent',
    subtasks: [  // Must match childMapping value
      { TaskID: 2, TaskName: 'Child' }
    ]
  }
];


Exception: Use idMapping + parentIdMapping for flat parent-child structure:

// Alternative: Flat structure with parent IDs
<ejs-treegrid 
  [dataSource]='flatData'
  idMapping='TaskID'
  parentIdMapping='ParentID'
  hasChildMapping='isParent'>
</ejs-treegrid>

Rule 2: Data Type Matching is MANDATORY

Severity: 🟠 IMPORTANT - Type mismatches cause rendering/sorting issues

Requirement:

// ✅ CORRECT - Type matches column definition
public data = [
  {
    TaskID: 1,              // number type
    TaskName: 'Planning',   // string type
    StartDate: new Date(),  // Date object for date columns
  }
];

// Column definition must match data types
<e-columns>
  <e-column field='TaskID' headerText='ID' type='number'></e-column>
  <e-column field='TaskName' headerText='Task' type='text'></e-column>
  <e-column field='StartDate' headerText='Date' type='date' format='yMd'></e-column>
</e-columns>

// ❌ WRONG - Type mismatch
public data = [
  {
    TaskID: '1',            // String instead of number
    StartDate: '02/03/2024' // String instead of Date object
  }
];

Documentation Navigation Guide
Getting Started & Setup

📄 Read: references/getting-started-guide.md

Complete installation and setup
Module configuration
Project initialization
First TreeGrid component
API Quick Reference

📄 Read: references/properties.md

70+ properties in organized tables
Data binding, display, behavior, features
Settings objects and modules
Column properties quick reference

📄 Read: references/methods.md

60+ methods in organized tables
Data management, selection, expand/collapse
Filtering, sorting, export, editing
DOM access and utility methods

📄 Read: references/events.md

56+ events in organized tables
Cancelable events and async patterns
Data, action, selection, edit events
Export, print, and query events

Recommended for developers who need quick property/method/event lookup

Data Binding

📄 Read: references/data-binding.md

Local and remote data binding
ORM and custom adaptor implementation
Loading data from various sources
Adaptors for Remote Data

📄 Read: references/adaptors.md

7 adaptor types for backend integration
UrlAdaptor, ODataV4Adaptor, WebApiAdaptor, GraphQLAdaptor
Custom adaptors and RemoteSaveAdaptor
Backend configuration examples (C#, Node.js)
Request/response format specifications
Error handling and adaptor comparison
Observables Data

📄 Read: references/observables.md

RxJS observables integration
Async data binding patterns
Observable-based event handling
Async operators and pipelines
Column Configuration

📄 Read: references/column.md

Column definition and width management
Custom column templates and rendering
Column reordering and freezing
Column Spanning

📄 Read: references/column-spanning.md

Multi-column spanning configuration
Cell spanning across columns
Dynamic span calculation
Command Columns

📄 Read: references/command-column.md

Command column with action buttons
Edit, Delete, and Cancel buttons
Custom command implementations
Column Menu

📄 Read: references/column-menu.md

Column header context menu
Sort, group, and filter menu items
Custom column menu options
Column Chooser

📄 Read: references/column-chooser.md

Column visibility toggle UI
Show/hide columns dynamically
Column chooser dialog configuration
Row Configuration

📄 Read: references/row.md

Row templates and detail rows
Row drag-drop functionality
Row spanning and customization
Cell-Level Features

📄 Read: references/cell.md

Cell styling and formatting
Cell templates and tooltips
Custom CSS and HTML content
Module System & Architecture

📄 Read: references/modules.md

Module imports and dependencies
Required service providers
Angular version compatibility
Library setup and initialization
Editing

📄 Read: references/editing.md

Cell, inline, dialog, row, and batch editing
Data validation and error handling
Custom editors and validation rules
Sorting

📄 Read: references/sorting.md

Single and multi-column sorting
Custom sort comparers
Sort order and keyboard navigation
Filtering

📄 Read: references/filtering.md

Filter bar and menu modes
Excel-like filtering
Custom filters and predicates
Searching

📄 Read: references/searching.md

Global and column-level search
Case-sensitive searching
Text highlighting
Selection

📄 Read: references/selection.md

Row, cell, and checkbox selection modes
Selection events and APIs
Programmatic selection
Paging

📄 Read: references/paging.md

Pagination configuration
Server-side paging
Page navigation APIs
Scrolling

📄 Read: references/scrolling.md

Virtual scrolling for large datasets
Infinite scroll and lazy loading
Height/width management and scroll positioning
Frozen Columns

📄 Read: references/frozen-columns.md

Freeze rows and columns
Fixed visibility configuration
Performance optimization
Aggregations

📄 Read: references/aggregates.md

Summary calculations (Sum, Avg, Min, Max, Count)
Footer templates and child aggregates
Aggregate events
Export & Print

📄 Read: references/print.md

Print functionality and modes
Page setup and column visibility
Custom print templates

📄 Read: references/pdf-export.md

PDF export with styling
Headers, footers, and watermarks
Server-side export

📄 Read: references/excel-export.md

Excel export configuration
Cell styling and formatting
Merged cells and custom data

📄 Read: references/csv-export.md

CSV export configuration
Custom data formatting for export
Dynamic file naming
Export events and callbacks
Selected records export
User Interface & Interaction

📄 Read: references/toolbar.md

Built-in toolbar items
Custom toolbar items and alignment
Toolbar event handling

📄 Read: references/clipboard.md

Copy/paste operations
Custom clipboard formats
Clipboard event handling

📄 Read: references/context-menu.md

Context menu configuration
Built-in and custom menu items
Menu event handling
Appearance & Responsiveness

📄 Read: references/adaptive.md

Responsive and adaptive design
Mobile optimization
Breakpoints and device detection

📄 Read: references/styling.md

Built-in themes (Material, Bootstrap, Fabric, Tailwind)
CSS customization and overrides
Row/cell conditional styling
Performance

📄 Read: references/performance-optimization.md

Virtual scrolling and lazy loading
Pagination for large datasets
Column virtualization and rendering optimization
Query optimization strategies
State Management

📄 Read: references/state-persistence.md

Save and restore grid state
LocalStorage integration
Custom state management
Foreign-key

📄 Read: references/foreign-keys.md

Foreign key column configuration
Display text mapping for FK values
Dropdown editors for FK fields
Cascading foreign key relationships
Remote data binding for FK data
Row Drag and Drop

📄 Read: references/row-drag-drop.md

Hierarchical drag-and-drop operations
Parent-child relationship updates
Circular hierarchy prevention
Drop event validation and constraints
Visual feedback during drag operations
Validation

📄 Read: references/validation.md

Built-in and custom validation rules
Async validation against server
Cross-field validation patterns
Server-side validation strategies
Error display and highlighting
Conditional validation rules
Globalization

📄 Read: references/globalization.md

Localization and language support
RTL (Right-to-Left) support
Cultural formatting and date/number formats
Loading Animation

📄 Read: references/loading-animation.md

Loading spinner configuration
Custom loading templates
Loading animation customization
Accessibility & Compliance

📄 Read: references/accessibility.md

WCAG 2.1 Level AA conformance
ARIA labels and attributes
Keyboard navigation and screen reader support
Focus management and visual indicators
Accessibility testing guidance
Quick Start Example
import { Component, ViewChild } from '@angular/core';
import { TreeGridComponent } from '@syncfusion/ej2-angular-treegrid';
import { PageService, SortService, FilterService, EditService } from '@syncfusion/ej2-angular-treegrid';

@Component({
  selector: 'app-treegrid',
  template: `
    <ejs-treegrid 
      #treegrid
      [dataSource]='data'
      [childMapping]='childMapping'
      [allowPaging]='true'
      [allowSorting]='true'
      [allowFiltering]='true'
      <e-columns>
        <e-column field='TaskID' headerText='Task ID' width='90' isPrimaryKey='true'></e-column>
        <e-column field='TaskName' headerText='Task Name' width='200'></e-column>
      </e-columns>
    </ejs-treegrid>
  `,
  providers: [PageService, SortService, FilterService, EditService]
})
export class AppComponent {
  @ViewChild('treegrid') treegrid!: TreeGridComponent;

  public data: Object[] = [
    {
      TaskID: 1,
      TaskName: 'Planning',
      subtasks: [
        { TaskID: 2, TaskName: 'Scope', Duration: 4, Progress: 100 },
        { TaskID: 3, TaskName: 'Budget', Duration: 4, Progress: 100 }
      ]
    }
  ];
  
  public childMapping: string = 'subtasks';
  
  public editSettings = { mode: 'Cell', allowEditing: true, allowDeleting: true, allowAdding: true };
}

Best Practices

Performance Optimization

Use virtual scrolling for large datasets (10,000+ records)
Implement server-side operations (sorting, filtering, paging)
Use frozen columns sparingly to avoid layout shifts

Data Management

Always provide a primary key (isPrimaryKey='true')
Use ChildMapping for hierarchical data
Implement proper error handling for API calls

User Experience

Provide loading indicators during data fetch
Implement search and filter for data discovery
Show validation messages for editing errors
Support keyboard navigation and accessibility

Customization

Use themes for consistent styling
Create reusable cell templates for common patterns
Style conditional rows for user guidance
Implement responsive design for mobile devices

State Management

Enable state persistence for user preferences
Save sort, filter, and column settings
Key Props Summary
Prop	Type	Default	Use Case
dataSource	DataManager|Object[]	null	Set grid data source
childMapping	string	null	Property for child records (must be explicitly set)
allowPaging	boolean	false	Enable pagination
allowSorting	boolean	false	Enable sorting
allowFiltering	boolean	false	Enable filtering
editSettings	EditSettings	{}	Configure edit mode
enableVirtualization	boolean	false	Enable virtual scrolling
Module Injection

Must inject required services:

import { PageService, SortService, FilterService, EditService, ExcelExportService, PdfExportService,
  PrintService, AggregateService, ToolbarService } from '@syncfusion/ej2-angular-treegrid';

@Component({
  providers: [
    PageService, 
    SortService, 
    FilterService, 
    EditService,
    ExcelExportService,
    PdfExportService,
    PrintService,
    AggregateService,
    ToolbarService
  ]
})

Weekly Installs
48
Repository
syncfusion/angu…s-skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn