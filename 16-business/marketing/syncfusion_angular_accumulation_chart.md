---
rating: ⭐⭐⭐
title: syncfusion-angular-accumulation-chart
url: https://skills.sh/syncfusion/angular-ui-components-skills/syncfusion-angular-accumulation-chart
---

# syncfusion-angular-accumulation-chart

skills/syncfusion/angular-ui-components-skills/syncfusion-angular-accumulation-chart
syncfusion-angular-accumulation-chart
Installation
$ npx skills add https://github.com/syncfusion/angular-ui-components-skills --skill syncfusion-angular-accumulation-chart
SKILL.md
Implementing Syncfusion Angular Accumulation Chart

The Accumulation Chart component is a powerful visualization tool for displaying data distribution across categories using pie charts, doughnut charts, pyramids, and funnels. This skill guides you through creating, configuring, and customizing accumulation charts in Angular applications.

When to Use This Skill
Creating pie/doughnut charts - Display proportional data distribution
Building pyramid/funnel charts - Show hierarchical or step-wise data
Adding interactive elements - Implement tooltips, selection, and click events
Customizing appearance - Apply themes, colors, gradients, and animations
Handling data labels - Configure label positioning, formatting, and templates
Managing legends - Add and customize chart legends
Adding annotations - Insert titles, center labels, and custom annotations
Ensuring accessibility - Implement WCAG compliance and keyboard navigation
Dynamic updates - Handle real-time data changes and grouping
Export/Print - Export charts to PDF or print functionality
Component Overview

The Accumulation Chart supports multiple series types within a single component:

Pie Chart - Circular slices representing data proportions
Donut (Pie with innerRadius) Chart - Pie chart variant with hollow center (supports center label)
Pyramid Chart - Data stacked in pyramid shape
Funnel Chart - Data visualization in funnel shape
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Installation via ng add command
Basic chart creation with data binding
Array and JSON data formats
CSS imports and theme setup
Initial component configuration
Series Types and Configuration

📄 Read: references/series-and-types.md

Pie vs Doughnut vs Pyramid vs Funnel
Series properties and options
Multiple series rendering
Type-specific features and use cases
Data Labels and Legends

📄 Read: references/data-labels-and-legends.md

Data label positioning (inside, outside, auto)
Label formatting and custom templates
Label visibility and intersection handling
Legend placement and customization
Legend click events and interactions
Annotations and Titles

📄 Read: references/annotations-and-titles.md

Chart titles and subtitles
Center labels for doughnut charts
Text and image annotations
Annotation positioning and alignment
Appearance and Styling

📄 Read: references/appearance-and-styling.md

Color palettes and theme selection
Animation configuration and timing
Gradient and solid fills
Custom CSS styling
Print and export functionality
Interactive Features

📄 Read: references/interactive-features.md

Tooltip configuration and customization
Selection modes (single, multiple, none)
Point and series selection events
Click and hover event handlers
Selection styling
Accessibility and Responsive Design

📄 Read: references/accessibility-and-responsive.md

WCAG compliance requirements
Keyboard navigation patterns
ARIA attributes and labels
Screen reader support
Responsive chart sizing
Mobile and touch support
Advanced Scenarios

📄 Read: references/advanced-scenarios.md

Dynamic data updates and refresh
Data grouping and filtering
Empty point handling
Common patterns and workflows
EJ1 to EJ2 migration guide
Quick Start Example
Basic Pie Chart
import { Component } from '@angular/core';
import { AccumulationChartModule } from '@syncfusion/ej2-angular-charts';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [AccumulationChartModule],
  template: `
    <ejs-accumulationchart id="container" [tooltip]="{ enable: true }">
      <e-accumulation-series-collection>
        <e-accumulation-series
          [dataSource]="data"
          xName="x"
          yName="y"
          type="Pie">
        </e-accumulation-series>
      </e-accumulation-series-collection>
    </ejs-accumulationchart>
  `,
  styles: [`#container { height: 420px; width: 100%; }`]
})
export class AppComponent {
  data = [
    { x: 'Chrome', y: 37 },
    { x: 'Firefox', y: 28 },
    { x: 'Safari', y: 18 },
    { x: 'Others', y: 17 }
  ];
}

Basic Donut (Pie with innerRadius) Chart with Center Label
<ejs-accumulationchart id="container">
  <e-accumulation-series-collection>
    <e-accumulation-series
      [dataSource]="data"
      xName="x"
      yName="y"
      type="Pie" innerRadius="40%"
      [dataLabel]="{ visible: true, position: 'Inside', name: 'text' }">
    </e-accumulation-series>
  </e-accumulation-series-collection>
</ejs-accumulationchart>

<!-- Center label in template -->
<div style="font-size: 18px; text-align: center;">
  Total Sales: $45,000
</div>

Common Patterns
Pattern 1: Dynamic Data Update
updateData() {
  this.data = [
    { x: 'Q1', y: 25000 },
    { x: 'Q2', y: 35000 },
    { x: 'Q3', y: 42000 },
    { x: 'Q4', y: 50000 }
  ];
  // Chart automatically refreshes with new data
}

Pattern 2: Handling Selection Events
onPointSelected(args: any) {
  console.log('Selected point:', args.pointIndex);
  console.log('Selected value:', args.series.dataSource[args.pointIndex].y);
}

Pattern 3: Custom Color Palette
@Component({
  template: `
    <ejs-accumulationchart 
      [palette]="customPalette">
      ...
    </ejs-accumulationchart>
  `
})
export class ChartComponent {
  customPalette = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'];
}

Pattern 4: Legend with Position
<ejs-accumulationchart>
  <e-accumulation-legend
    [visible]="true"
    position="Right"
    [enableHighlight]="true">
  </e-accumulation-legend>
</ejs-accumulationchart>

Key Configuration Props
Property	Type	Purpose
type	string	Chart type: 'Pie', 'Doughnut', 'Pyramid', 'Funnel'
dataSource	object[]	Array of data points with x and y values
xName	string	Field name for category data
yName	string	Field name for value data
dataLabel	object	Label configuration (position, formatting)
tooltip	object	Tooltip settings (enable, template, formatting)
palette	string[]	Custom color array for series points
animation	object	Animation configuration (enable, duration)
startAngle	number	Starting angle for pie/doughnut (0-360)
explode	boolean	Enable point separation effect
Next Steps
Start with: references/getting-started.md to set up your first chart
Choose chart type: references/series-and-types.md for detailed type information
Customize: Use other references based on your specific needs (labels, legends, interactivity, styling)
Enhance: Refer to references/accessibility-and-responsive.md for production-ready implementations
API Reference Documentation
Comprehensive API Catalog

Complete API Guide: references/api-reference.md

All API documentation is available at https://ej2.syncfusion.com/angular/documentation/api/accumulation-chart/

Quick API Links

Core Components:

AccumulationChart - Main chart component
AccumulationSeries - Series configuration
AccumulationDataLabelSettings - Data label settings
LegendSettings - Legend configuration
TooltipSettings - Tooltip settings

Key Enumerations:

AccumulationType - Pie, Doughnut, Pyramid, Funnel
AccumulationLabelPosition - Inside, Outside
LegendPosition - Top, Bottom, Left, Right

Event Interfaces:

IAccLoadedEventArgs - Load event
IAccPointRenderEventArgs - Point render event
IAccLegendClickEventArgs - Legend click event

Each reference guide includes an "API Reference Summary" section at the end with relevant API links.

Related Skills
Implementing line/bar charts (for other chart types)
Working with Angular data binding
Angular component styling and theming
Weekly Installs
48
Repository
syncfusion/angu…s-skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass