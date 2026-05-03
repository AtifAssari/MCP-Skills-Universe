---
rating: ⭐⭐
title: syncfusion-angular-pivot-table
url: https://skills.sh/syncfusion/angular-ui-components-skills/syncfusion-angular-pivot-table
---

# syncfusion-angular-pivot-table

skills/syncfusion/angular-ui-components-skills/syncfusion-angular-pivot-table
syncfusion-angular-pivot-table
Installation
$ npx skills add https://github.com/syncfusion/angular-ui-components-skills --skill syncfusion-angular-pivot-table
SKILL.md
Implementing Angular Pivot Grid

The Syncfusion Angular Pivot Grid is a powerful data visualization and analysis component for creating interactive pivot tables, aggregating multidimensional data, and performing advanced analytics operations.

Important: Always verify API class names, properties, and method signatures by consulting the reference files in this skill (references/*.md). These are maintained with verified, working examples. Do not assume API details from other sources.

⚠️ Security Warning: Data Source Validation

CRITICAL SECURITY NOTICE: When implementing pivot tables, always use trusted data sources. Never fetch or bind data from untrusted or user-provided URLs without proper validation and sanitization.

Security Best Practices:
Use Local Data: Prefer local, in-memory data sources for maximum security
Validate Remote Sources: Only connect to authenticated and authorized API endpoints under your control
Sanitize User Input: Never allow users to specify arbitrary URLs or data sources
Implement Authentication: Always use authentication headers and secure API endpoints
Content Validation: Validate and sanitize all data received from external sources before binding
Use HTTPS: Always use HTTPS for remote data connections
Rate Limiting: Implement rate limiting on API endpoints to prevent abuse
Security Risks:
Indirect Prompt Injection: Untrusted third-party data can contain malicious content that manipulates AI agent behavior
Data Exfiltration: Malicious data sources could attempt to extract sensitive information
Code Injection: Untrusted data may contain scripts or harmful content
Recommended Approach:

✅ DO: Use controlled, authenticated backend APIs ✅ DO: Implement server-side data validation ✅ DO: Use environment variables for API endpoints ✅ DO: Whitelist allowed data sources

❌ DON'T: Accept user-provided URLs ❌ DON'T: Bind to public, untrusted endpoints ❌ DON'T: Skip data validation and sanitization ❌ DON'T: Use HTTP for sensitive data

When to Use This Skill

Use this skill when users need to:

Create and configure pivot tables from multidimensional data
Bind data from OLAP or relational data sources
Aggregate data with multiple aggregation functions (Sum, Avg, Count, etc.)
Group data by number ranges, dates, or custom categories
Create and manage calculated fields with formulas
Enable drill-down and drill-through operations
Visualize data with integrated pivot charts
Apply custom formatting and conditional styling
Optimize large dataset performance
Export pivot grid data to Excel or PDF
Persist and restore pivot grid state
Customize UI with field lists, grouping bars, and toolbars
Documentation Guide
Getting Started

📄 Read: references/getting-started.md

Installation and package setup
Basic Angular Pivot Grid implementation
CSS imports and theme configuration
RTL (Right-to-Left) support
Component initialization
Aggregation

📄 Read: references/aggregation.md

Aggregation functions: Sum, Avg, Count, Min, Max, Product, Median, DistinctCount
Advanced aggregations: DifferenceFrom, PercentageOfDifferenceFrom, PercentageOfParentTotal
Base field configuration with baseField and baseItem properties
Multiple aggregations on same field
Customizing aggregation dropdown and UI
Runtime aggregation type changes
Events: aggregateCellInfo, actionBegin, actionComplete
Grouping

📄 Read: references/grouping.md

Enable grouping with allowGrouping: true and inject GroupingService
Number grouping: Configure ranges with rangeInterval, startingAt, endingAt
Date grouping: Organize by Years, Quarters, Months, Days, Hours, Minutes, Seconds
Custom grouping: Group data by business-defined categories
UI-based grouping through context menu
Ungrouping and programmatic ungrouping
Common grouping patterns and troubleshooting
Calculated Fields

📄 Read: references/calculated-field.md

Creating calculated fields interactively and programmatically
Enabling with allowCalculatedField: true, injecting CalculatedFieldService
Defining with calculatedFieldSettings (name, formula)
Adding to values array with type: 'CalculatedField'
Editing/renaming fields through UI (Field List, Grouping Bar)
Formula syntax: Operators (+, -, , /, ^, <, >, ==, !=, &, |, ?), Functions (abs, min, max, isNaN, Math.)
Aggregation functions in formulas: Sum, Count, Avg, Min, Max
Formatting with separate formatSettings array: Currency (C), Number (N), Percentage (P)
Events: calculatedFieldCreate (validation), actionBegin/actionComplete (control operations)
Pivot Chart Integration

📄 Read: references/pivot-chart-integration.md

Inject PivotChartService provider to enable chart functionality
Chart types: 21+ types including Line, Column, Area, Bar, StepArea, Pie, Doughnut, Funnel, Pyramid, Radar, Polar, Pareto, Bubble, Scatter, Spline
Display options: Configure with displayOption property to show Table, Chart, or Both with view and primary settings
Series customization: Customize charts via chartSeries in chartSettings (type, marker, dataLabel)
Field list integration: Enable with showFieldList: true for dynamic field manipulation
Grouping bar support: Enable with showGroupingBar: true for axis field switching
Axis configuration: Customize X/Y axes via primaryXAxis and primaryYAxis in chartSettings
Multiple axes: Configure enableMultipleAxis for multi-value visualization with multipleAxisMode
Accumulation chart drill: Support drill-down/up on Pie, Doughnut, Funnel, Pyramid via context menu
Filtering & Sorting

📄 Read: references/filtering-and-sorting.md

Member filtering: Include or exclude specific field members
Label filtering: Filter based on header text or member names
Value filtering: Filter based on aggregated values meeting conditions
Member sorting: Arrange field members in ascending/descending order
Custom member sorting: Sort field members in user-defined order using membersOrder
Value sorting: Sort pivot table values and aggregated data with enableValueSorting
Programmatic value sorting: Configure with valueSortSettings
Data Formatting & Conditional Formatting

📄 Read: references/data-formatting.md

Number formatting: Apply Currency (C), Percentage (P), Number (N), Scientific (E) formats
Custom format strings: Define format strings with placeholders for calculated fields
Conditional formatting: Apply colors/styles based on cell values using conditionalFormatSettings
Format settings configuration: Configure in separate formatSettings array in dataSourceSettings
Export & Printing

📄 Read: references/export-and-print.md

Excel export: excelExport() with custom properties, themes
PDF export: pdfExport() with headers, footers, page orientation
CSV export: csvExport() for large datasets (1M+ rows)
Print functionality: print() method for table and chart
Multi-table export: Combine multiple pivot tables in single file
Export customization: Cell styling, color themes, branding
UI Customization

📄 Read: references/ui-customization.md

Toolbar configuration: Show/hide built-in toolbar items
Report management: New, Save, Load, Delete reports
View switching: Toggle between Grid and Chart modes
Export options: Quick export buttons
Grand totals/Subtotals: Show/hide and customize positioning
Custom templates: Build custom toolbar or field list
Grouping Bar UI Operations

📄 Read: references/grouping-bar-ui-operations.md

Enable grouping bar: Set showGroupingBar: true on component
Drag-and-drop reorganization: Move fields between Row, Column, Value, Filter axes
Filter operations: Access filters from grouping bar field buttons
Sort operations: Configure sort options via grouping bar interface
Remove operations: Remove fields directly from grouping bar
Value field management: Switch between value fields in accumulation charts
Hide specific icons: Control visibility of filter, sort, remove icons per field
Grouping bar customization: Configure via groupingBarSettings
Tooltips Customization

📄 Read: references/tooltips-customization.md

Enable/disable tooltips: Configure tooltip visibility on cells and charts
Custom tooltip templates: Define dynamic tooltip content with placeholders
Available placeholders: Row headers, column headers, value, and other cell metadata
Pivot chart tooltip customization: Customize tooltip appearance for chart data points
CSS styling: Style tooltip appearance with custom CSS
Dynamic tooltip content: Configure based on cell values and context
Editing & Drill Operations

📄 Read: references/editing-drill-operations.md

Enable editing: Set allowEditing: true on component (relational data only)
Edit modes: Normal (inline), Dialog (popup), Batch (multiple), Command Column (dedicated)
Edit settings: Configure via editSettings with allowAdding, allowDeleting, allowCommandColumns
Edit events: Monitor editCompleted, actionBegin, actionComplete, actionFailure
CRUD operations: Create, Read, Update, Delete records via editing interface
Drill-through operations: View raw underlying data for aggregated values via context menu
Drill-down operations: Click cells to navigate hierarchical data deeper
Cell selection: Configure via selectionSettings
Save data: Updated records persist via event handlers and data binding
OLAP Data Sources

📄 Read: references/olap-data-sources.md

Connection configuration: Set url, catalog, cube, providerType: 'SSAS' in dataSourceSettings
OLAP cube elements: Measures (numeric aggregates), Dimensions (hierarchical groupings), Hierarchies, Named Sets
MDX support: Configure using MDX (Multidimensional Expressions) syntax for queries
Hierarchies: Access via [Dimension].[Hierarchy] notation (e.g., [Date].[Date Hierarchy])
Calculated fields: Create Calculated Measures and Dimensions in OLAP cubes
Authentication: Configure via connection string or backend authentication headers
Named sets: Predefined member groups for analysis
Advanced features: Drill-down, virtual scrolling, value filtering with OLAP
Paging Configuration

📄 Read: references/paging-configuration.md

Enable paging with enablePaging: true and inject PagerService
Page settings: rowPageSize, columnPageSize, currentRowPage, currentColumnPage
Pager UI configuration and positioning (Top/Bottom)
Row vs column paging
Compact view and inverse pager layout
Custom page size options in dropdown
Paging with virtual scrolling for optimization
Server-side paging for huge datasets
Mobile-optimized paging
Virtual Scrolling

📄 Read: references/virtual-scrolling.md

Enable virtual scrolling with enableVirtualization: true for large datasets
Single page mode: Use allowSinglePage: true to render only current view page
Limitations: pixel-based columnWidth, avoid runtime sizing changes
Static FieldList synchronization using enginePopulated events and update/updateView methods
Performance optimization for 100K+ rows on client-side
Drill-Down & Drill-Through Operations

📄 Read: references/drill-down.md

Drill-down: Navigate hierarchical data by clicking cells
Drill-up: Navigate back to higher levels
Drill-through: View raw underlying data for aggregated values
Events: cellClick, fieldDrop, fieldsUpdated for drill interactions
Context menu: Built-in drill operations
Database Connections

📄 Read: references/database-connections.md

SQL Server: Connect via connection strings with SQL authentication
MySQL: Configure with host, port, user, password, and database
PostgreSQL: Connection configuration for PostgreSQL databases
Oracle: Oracle database connectivity with named parameters
MongoDB: Connect to MongoDB collections and query documents
Elasticsearch: Big data analytics via Elasticsearch indices
Snowflake: Cloud data warehouse integration
Server-side processing: Use ASP.NET Core backend with database queries
Server-Side Pivot Engine

📄 Read: references/server-side-pivot-engine.md

Server-side aggregation: Delegate heavy processing to ASP.NET Core backend
Client configuration: Set mode: 'Server' with url endpoint in dataSourceSettings
ASP.NET Core setup: Download and configure PivotController with Syncfusion.Pivot.Engine NuGet
Data sources: Support Collection, JSON, CSV, DataTable, Dynamic objects on server
Large datasets: Handle 100K+ rows with server-side processing
Virtual scrolling: Combine with server mode for optimal performance
Export operations: Excel/CSV export of server-processed data
Authentication: Configure via beforeServiceInvoke event or headers
Performance Optimization

📄 Read: references/performance-optimization.md

Virtual scrolling: Enable with enableVirtualization: true for 100K+ rows
Single page mode: Use allowSinglePage: true for better performance
Paging: Configure with pageSettings for row/column pagination
Data compression: Enable allowDataCompression: true for duplicate record summarization
Deferred updates: Use allowDeferLayoutUpdate: true to batch field operations
Large dataset handling: Server-side processing with mode: 'Server'
Best practices: Pre-filtering, optimized sorting, member filtering limits, avoiding built-in grouping
State Persistence & Hyperlinks

📄 Read: references/state-persistence-hyperlinks.md

State persistence: Save and restore pivot configuration using getPersistData()
Local storage: Persist report state in browser localStorage for user sessions
Report management: Save, load, and delete named reports
JSON serialization: Export/import report configurations as JSON
Hyperlinks: Enable clickable hyperlinks in pivot cells via hyperlinkSettings
Hyperlink events: Handle hyperlink clicks with appropriate event handlers
Drill-through hyperlinks: Links to detailed data sources for aggregates
Quick Start Example
import { PivotViewAllModule, CalculatedFieldService } from '@syncfusion/ej2-angular-pivotview';
import { Component, OnInit, ViewChild } from '@angular/core';
import { PivotViewComponent, IDataSet } from '@syncfusion/ej2-angular-pivotview';
import { DataSourceSettingsModel } from '@syncfusion/ej2-pivotview/src/model/datasourcesettings-model';

@Component({
  imports: [PivotViewAllModule],
  providers: [CalculatedFieldService],
  standalone: true,
  selector: 'app-pivot-grid',
  template: `
    <ejs-pivotview #pivotview id='PivotView' 
      [dataSourceSettings]="dataSourceSettings"
      [height]="'500px'"
      [width]="'100%'"
      [allowCalculatedField]="true" 
      [allowGrouping]="true"
      [toolbar]="toolbarItems">
    </ejs-pivotview>
  `
})
export class AppComponent implements OnInit {
    @ViewChild('pivotview') pivotViewComponent!: PivotViewComponent;
    
    public pivotData!: IDataSet[];
    public dataSourceSettings!: DataSourceSettingsModel;
    public toolbarItems: string[] = ['New', 'Save', 'SaveAs', 'Rename', 'Remove', 'Load', 'Export'];

    ngOnInit(): void {
        this.pivotData = [
            { 'Sold': 31, 'Amount': 52824, 'Country': 'France', 'Products': 'Mountain Bikes', 'Year': 'FY 2015', 'Quarter': 'Q1' },
            { 'Sold': 51, 'Amount': 86904, 'Country': 'France', 'Products': 'Mountain Bikes', 'Year': 'FY 2015', 'Quarter': 'Q2' },
            { 'Sold': 90, 'Amount': 153360, 'Country': 'France', 'Products': 'Mountain Bikes', 'Year': 'FY 2015', 'Quarter': 'Q3' },
            { 'Sold': 25, 'Amount': 42500, 'Country': 'France', 'Products': 'Road Bikes', 'Year': 'FY 2015', 'Quarter': 'Q1' },
            { 'Sold': 40, 'Amount': 68000, 'Country': 'Germany', 'Products': 'Mountain Bikes', 'Year': 'FY 2015', 'Quarter': 'Q2' }
        ];

        this.dataSourceSettings = {
            dataSource: this.pivotData,
            expandAll: false,
            rows: [{ name: 'Country' }, { name: 'Products' }],
            columns: [{ name: 'Year' }, { name: 'Quarter' }],
            values: [
                { name: 'AvgAmount', type: 'CalculatedField' },
                { name: 'Sold', type: 'Count' }
            ],
            calculatedFieldSettings: [
                {
                    name: 'AvgAmount',
                    formula: '"Sum(Amount)"/"Count(Sold)"'  // Calculated field: Average
                }
            ],
            formatSettings: [
                { name: 'Amount', format: 'C2' },             // Currency format
                { name: 'AvgAmount', format: 'C2' }           // Format calculated field
            ]
        };
    }
}

Common Patterns
Pattern 1: Multiple Fields with Different Aggregation Types

Each field supports only ONE aggregation type. To analyze different aspects, use different fields with their respective aggregation functions:

values: [
    { name: 'Amount', type: 'Sum' },      // Total sales amount
    { name: 'Quantity', type: 'Avg' },    // Average quantity sold
    { name: 'Sold', type: 'Count' },      // Number of transactions
    { name: 'Price', type: 'Min' },       // Minimum price
]


Note: Each field in the values array can only have ONE type. To get multiple aggregation types for analysis, use different fields or create calculated fields combining aggregations.

Pattern 2: Hierarchical Grouping

Organize data with multi-level grouping:

rows: [
    { name: 'Country' },    // Primary level
    { name: 'Region' },     // Secondary level
    { name: 'City' }        // Tertiary level
],
columns: [
    { name: 'Year' },       // Year level
    { name: 'Quarter' }     // Quarter level
]

Pattern 3: Using Calculated Fields with Aggregations

Combine calculated fields with multiple aggregation types for advanced analysis:

values: [
    { name: 'Amount', type: 'Sum' },       // Total amount
    { name: 'Quantity', type: 'Avg' },     // Average quantity
    { name: 'AvgRevenue', type: 'CalculatedField' }  // Custom calculation
],
calculatedFieldSettings: [
    {
        name: 'AvgRevenue',
        formula: '"Sum(Amount)" / "Count(Quantity)"'  // Revenue per unit
    }
],
formatSettings: [
    { name: 'Amount', format: 'C2' },      // Currency format for Amount
    { name: 'AvgRevenue', format: 'C2' }   // Currency format for calculated field
]

Pattern 4: Number Range Grouping

Group numeric fields into ranges:

groupSettings: [
    {
        name: 'ProductID',
        type: 'Number',
        rangeInterval: 5,
        startingAt: 1000,
        endingAt: 1010
    }
]

Pattern 5: Date Hierarchy Grouping

Organize dates with time-based hierarchies:

groupSettings: [
    {
        name: 'OrderDate',
        type: 'Date',
        groupInterval: ['Years', 'Months'],  // Year then month hierarchy
        startingAt: new Date(2020, 0, 1),
        endingAt: new Date(2023, 11, 31)
    }
]

Key Configuration Properties
Property	Type	Location	Purpose
rows	Array	dataSourceSettings	Fields organized vertically for grouping data
columns	Array	dataSourceSettings	Fields organized horizontally for grouping data
values	Array	dataSourceSettings	Fields to aggregate with type (Sum, Avg, Count, CalculatedField, etc.)
filters	Array	dataSourceSettings	Fields used to filter data across both axes
type	String	values field	Aggregation type: Sum, Avg, Count, Min, Max, Product, DistinctCount, Median, RunningTotals, DifferenceFrom, PercentageOfDifferenceFrom, PercentageOfGrandTotal, PercentageOfColumnTotal, PercentageOfRowTotal, PercentageOfParentTotal, PopulationStDev, SampleStDev, PopulationVar, SampleVar, Index, CalculatedField
baseField	String	values field	Field reference for DifferenceFrom/Percentage-based comparisons (base field aggregation)
baseItem	String	values field	Specific member for base field comparisons
allowCalculatedField	Boolean	Component	Enable calculated field feature (requires CalculatedFieldService provider)
calculatedFieldSettings	Array	dataSourceSettings	Define calculated field name and formula properties
formula	String	calculatedFieldSettings	Mathematical expression using aggregation functions (Sum, Count, Avg, Min, Max) and operators (+, -, *, /, ^, <, >, ==, !=, &, |, ?)
formatSettings	Array	dataSourceSettings	SEPARATE array for number formatting (C, N, P, E) of value fields and calculated fields
allowGrouping	Boolean	Component	Enable grouping feature (requires GroupingService provider)
groupSettings	Array	dataSourceSettings	Configure number, date, or custom grouping with name, type, rangeInterval, groupInterval
groupInterval	Array	groupSettings	Grouping hierarchy (Years, Quarters, Months, Days, Hours, Minutes, Seconds)
aggregateTypes	Array	Component	Restrict aggregation dropdown to specific types (array of AggregateTypes)
showAggregationOnValueField	Boolean	dataSourceSettings	Display aggregation type in grouping bar button text (e.g., "Sum of Amount" vs "Amount")
sortSettings	Array	dataSourceSettings	Configure field sorting with order, membersOrder, name properties
enableValueSorting	Boolean	Component	Enable sorting by aggregated values

Important: When adding calculated fields to values, use type: 'CalculatedField' to distinguish them from regular aggregations. Format settings must be applied in a separate formatSettings array, not within the value field object.

Next Steps

Foundation (Start here):

Read Getting Started for setup and initialization
Read Aggregation to implement aggregation functions and base field aggregations
Read Grouping to configure number, date, and custom grouping

Data Manipulation: 4. Read Calculated Fields for complex calculations and custom field formulas 5. Read Filtering & Sorting for label/value filtering and custom sorting 6. Read Data Formatting for number formats and conditional formatting

Visualization & Interaction: 7. Read Pivot Chart Integration for charting and drill operations 8. Read UI Customization for toolbars and custom interfaces 9. Read Drill-Down & Drill-Through for hierarchical data exploration

Advanced Features: 10. Read Export & Printing for multi-format export (Excel, PDF, CSV) 11. Read State Persistence for saving and restoring configurations 12. Read Database Connections for SQL/NoSQL/big data integration 13. Read Server-Side Pivot Engine for processing 100K+ rows on backend 14. Read Performance Optimization for large datasets, deferred updates, and virtual scrolling

Foundational References

These files provide foundational knowledge and may be referenced by feature guides:

📄 references/core-concepts.md - Data binding types (JSON, CSV, OLAP), client-side vs server-side comparison, choosing appropriate data sources

📄 references/layout-and-columns.md - Classic layout, row/column sizing, column features, cell selection and customization

📄 references/field-list.md - Field list UI (popup/fixed modes), field organization, deferred updates patterns

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