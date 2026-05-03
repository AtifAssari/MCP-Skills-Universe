---
title: syncfusion-react-3d-chart
url: https://skills.sh/syncfusion/react-ui-components-skills/syncfusion-react-3d-chart
---

# syncfusion-react-3d-chart

skills/syncfusion/react-ui-components-skills/syncfusion-react-3d-chart
syncfusion-react-3d-chart
Installation
$ npx skills add https://github.com/syncfusion/react-ui-components-skills --skill syncfusion-react-3d-chart
SKILL.md
Syncfusion React 3D Chart

A comprehensive skill for implementing and customizing Syncfusion's 3D Chart component in React applications. This skill helps you create interactive 3D visualizations with column, bar, and stacked chart types.

When to Use This Skill

Use this skill when you need to:

Implement Syncfusion 3D charts in React applications
Create column, bar, or stacked 3D charts
Configure category, numeric, datetime, or logarithmic axes
Bind and manage chart data sources
Customize 3D chart appearance (rotation, depth, walls)
Add data labels, legends, or tooltips to 3D charts
Implement chart selection and interaction
Export or print 3D charts
Support accessibility in 3D visualizations
Troubleshoot 3D chart rendering or performance issues
Component Overview

Package: @syncfusion/ej2-react-charts

Main Components:

Chart3DComponent - Root 3D chart container
Chart3DSeriesCollectionDirective - Series collection wrapper
Chart3DSeriesDirective - Individual series configuration
Chart3DAxesDirective - Multiple axes configuration

Chart Types: Column, Bar, Stacked Column, Stacked Bar, 100% Stacked Column, 100% Stacked Bar

Axis Types: Category, Numeric, DateTime, Logarithmic

Documentation and Navigation Guide
API Reference

📄 Read: references/api-reference.md

Concise list of public props, methods, events, child directives, and a usage snippet. Use this as the canonical in-repo API summary.
Getting Started

📄 Read: references/getting-started.md

Installing @syncfusion/ej2-react-charts package
Setting up dependencies and CSS themes
Creating your first 3D chart
Basic Chart3DComponent usage
TypeScript configuration
Chart Types

📄 Read: references/chart-types.md

Column chart (vertical 3D bars)
Bar chart (horizontal 3D bars)
Stacked Column chart
Stacked Bar chart
100% Stacked Column chart
100% Stacked Bar chart
When to use each chart type
Series type configuration
Working with Data

📄 Read: references/working-with-data.md

Data binding approaches
Data source structure requirements
Series configuration (xName, yName)
Multiple series handling
Dynamic data updates
Empty points handling
Category Axis

📄 Read: references/category-axis.md

Category axis configuration
Label formatting and placement
Category grouping
Interval settings
Use cases for categorical data
Numeric Axis

📄 Read: references/numeric-axis.md

Numeric axis setup
Range configuration (minimum, maximum)
Interval and step size
Label formatting (decimals, currency)
Starting from zero vs auto-range
DateTime Axis

📄 Read: references/datetime-axis.md

DateTime axis configuration
Date format options
Interval types (days, months, years)
Date range settings
Skeleton formats
Timezone considerations
Logarithmic Axis

📄 Read: references/logarithmic-axis.md

Logarithmic scale overview
Base configuration (log10, log2, etc.)
Use cases for exponential data
Label formatting for log scales
Range and interval settings
Axis Customization

📄 Read: references/axis-customization.md

Axis titles and labels
Multiple axes (secondary Y-axis)
Axis line styling
Grid lines configuration
Tick marks customization
Label rotation and formatting
Axis crossing values
Inversed axis
Multiple Panes

📄 Read: references/multiple-panes.md

Multiple pane overview
Row configuration and distribution
Pane height settings
Series assignment to different panes
Axis binding per pane
Use cases for multi-metric comparison
Data Labels, Legend, and Tooltip

📄 Read: references/data-labels-legend-tooltip.md

Data labels configuration and positioning
Label templates and formatting
Legend position and customization
Legend toggle visibility
Tooltip enabling and formatting
Custom tooltip templates
Shared tooltips
Selection and Interaction

📄 Read: references/selection-interaction.md

Selection modes (Point, Series, Cluster)
Single and multi-selection
Selection events and handlers
Highlight on hover
Selection styling
Interactive features
Print and Export

📄 Read: references/print-export.md

Print functionality
Export as PNG, JPEG, SVG
Export as PDF
Export configuration options
File naming conventions
Export events
Appearance and Theming
Built-in themes (Material, Bootstrap, Fluent, Tailwind)
Custom theme creation
Color palettes
3D rotation and tilt angles
3D depth configuration
Wall customization
Chart background and borders
Animation settings
Accessibility
WCAG 2.1 compliance
Keyboard navigation support
ARIA attributes
Screen reader compatibility
High contrast mode
Focus management
Accessible color schemes
Quick Start Example
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { 
  Chart3DComponent, 
  Chart3DSeriesCollectionDirective, 
  Chart3DSeriesDirective,
  Inject,
  Category3D,
  ColumnSeries3D,
  Legend3D,
  DataLabel3D,
  Tooltip3D
} from '@syncfusion/ej2-react-charts';

function SalesChart() {
  const data = [
    { month: 'Jan', sales: 35 },
    { month: 'Feb', sales: 28 },
    { month: 'Mar', sales: 34 },
    { month: 'Apr', sales: 32 },
    { month: 'May', sales: 40 }
  ];

  return (
    <Chart3DComponent
      id='chart'
      title='Monthly Sales'
      primaryXAxis={{ valueType: 'Category' }}
      primaryYAxis={{ title: 'Sales (K)' }}
      enableRotation={true}
      rotation={7}
      tilt={10}
      depth={100}
    >
      <Inject services={[ColumnSeries3D, Category3D, Legend3D, DataLabel3D, Tooltip3D]} />
      <Chart3DSeriesCollectionDirective>
        <Chart3DSeriesDirective
          dataSource={data}
          xName='month'
          yName='sales'
          type='Column'
          name='Sales'
        />
      </Chart3DSeriesCollectionDirective>
    </Chart3DComponent>
  );
}

export default SalesChart;
ReactDOM.render(<SalesChart />, document.getElementById('charts'));

Common Patterns
Basic Column Chart
<Chart3DComponent primaryXAxis={{ valueType: 'Category' }}>
  <Inject services={[ColumnSeries3D, Category3D]} />
  <Chart3DSeriesCollectionDirective>
    <Chart3DSeriesDirective
      dataSource={data}
      xName='category'
      yName='value'
      type='Column'
    />
  </Chart3DSeriesCollectionDirective>
</Chart3DComponent>

Stacked Column Chart
<Chart3DComponent primaryXAxis={{ valueType: 'Category' }}>
  <Inject services={[StackingColumnSeries3D, Category3D]} />
  <Chart3DSeriesCollectionDirective>
    <Chart3DSeriesDirective
      dataSource={data1}
      xName='x'
      yName='y'
      type='StackingColumn'
      name='Product A'
    />
    <Chart3DSeriesDirective
      dataSource={data2}
      xName='x'
      yName='y'
      type='StackingColumn'
      name='Product B'
    />
  </Chart3DSeriesCollectionDirective>
</Chart3DComponent>

Bar Chart (Horizontal)
<Chart3DComponent primaryXAxis={{ valueType: 'Category' }}>
  <Inject services={[BarSeries3D, Category3D]} />
  <Chart3DSeriesCollectionDirective>
    <Chart3DSeriesDirective
      dataSource={data}
      xName='category'
      yName='value'
      type='Bar'
    />
  </Chart3DSeriesCollectionDirective>
</Chart3DComponent>

With Data Labels and Legend
<Chart3DComponent
  primaryXAxis={{ valueType: 'Category' }}
  legendSettings={{ visible: true }}
>
  <Inject services={[ColumnSeries3D, Category3D, Legend3D, DataLabel3D]} />
  <Chart3DSeriesCollectionDirective>
    <Chart3DSeriesDirective
      dataSource={data}
      xName='x'
      yName='y'
      type='Column'
      name='Sales'
      dataLabel={{ visible: true }}
    />
  </Chart3DSeriesCollectionDirective>
</Chart3DComponent>

Custom 3D Rotation
<Chart3DComponent
  primaryXAxis={{ valueType: 'Category' }}
  enableRotation={true}
  rotation={15}
  tilt={5}
  depth={120}
  wallColor='transparent'
  wallSize={1}
>
  <Inject services={[ColumnSeries3D, Category3D]} />
  <Chart3DSeriesCollectionDirective>
    <Chart3DSeriesDirective
      dataSource={data}
      xName='x'
      yName='y'
      type='Column'
    />
  </Chart3DSeriesCollectionDirective>
</Chart3DComponent>

Multiple Series with Different Colors
<Chart3DComponent
  primaryXAxis={{ valueType: 'Category' }}
  palettes={['#E94649', '#F6B53F', '#6FAAB0']}
>
  <Inject services={[ColumnSeries3D, Category3D, Legend3D]} />
  <Chart3DSeriesCollectionDirective>
    <Chart3DSeriesDirective
      dataSource={data1}
      xName='x'
      yName='y'
      type='Column'
      name='Product A'
    />
    <Chart3DSeriesDirective
      dataSource={data2}
      xName='x'
      yName='y'
      type='Column'
      name='Product B'
    />
    <Chart3DSeriesDirective
      dataSource={data3}
      xName='x'
      yName='y'
      type='Column'
      name='Product C'
    />
  </Chart3DSeriesCollectionDirective>
</Chart3DComponent>

Key Props Reference
Chart3DComponent Props
Prop	Type	Description
primaryXAxis	Object	Configuration for X-axis (type, title, labels)
primaryYAxis	Object	Configuration for Y-axis (range, title, format)
rotation	number	Horizontal rotation angle (0-360)
tilt	number	Vertical tilt angle (0-90)
depth	number	Depth of 3D chart (0-100)
enableRotation	boolean	Enable mouse rotation interaction
wallColor	string	Color of 3D walls
wallSize	number	Thickness of wall borders
title	string	Chart title text
legendSettings	Object	Legend configuration
tooltip	Object	Tooltip settings
palettes	string[]	Array of colors for series
Chart3DSeriesDirective Props
Prop	Type	Description
dataSource	any[]	Array of data points
xName	string	Property name for X-axis values
yName	string	Property name for Y-axis values
type	string	Chart type: 'Column', 'Bar', 'StackingColumn', 'StackingBar', 'StackingColumn100', 'StackingBar100'
name	string	Series name (shown in legend)
dataLabel	Object	Data label configuration
fill	string	Series color
opacity	number	Series opacity (0-1)
Common Use Cases
Sales Comparison: Column charts comparing monthly/quarterly sales across products
Survey Results: Bar charts showing survey responses or rankings
Market Share: Stacked column charts displaying market distribution
Time Series: DateTime axis for temporal data visualization
Financial Data: Logarithmic axis for stock prices or exponential growth
Multi-Metric Dashboards: Multiple panes showing different KPIs
Performance Tracking: Stacked 100% charts showing percentage contributions
Category Analysis: Category axis for discrete data grouping
Interactive Reports: Selection and export for user-driven exploration
Accessible Visualizations: WCAG-compliant charts for all users
TypeScript Support

All components are fully typed. Import types as needed:

import { 
  Chart3DComponent,
  IChart3DLoadedEventArgs,
  IChart3DPointRenderEventArgs,
  Chart3DModel
} from '@syncfusion/ej2-react-charts';

Troubleshooting Quick Reference

Chart not rendering?

Verify @syncfusion/ej2-react-charts is installed
Check CSS theme imports
Ensure required services are injected

Data not showing?

Verify xName/yName match data property names
Check axis valueType matches data type
Validate data source structure

Performance issues?

Reduce data point count (aggregate if needed)
Disable animations
Optimize data structure

3D effect not working?

Set enableRotation={true}
Configure rotation, tilt, and depth props
Check if series type supports 3D

For detailed troubleshooting, refer to the specific reference files above.

Weekly Installs
29
Repository
syncfusion/reac…s-skills
GitHub Stars
1
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass