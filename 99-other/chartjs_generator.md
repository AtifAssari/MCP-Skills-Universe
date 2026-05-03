---
title: chartjs-generator
url: https://skills.sh/vishalsachdev/claude-skills/chartjs-generator
---

# chartjs-generator

skills/vishalsachdev/claude-skills/chartjs-generator
chartjs-generator
Installation
$ npx skills add https://github.com/vishalsachdev/claude-skills --skill chartjs-generator
SKILL.md
Chart.js Generator
Overview

This skill generates professional, interactive charts using Chart.js, supporting all major chart types. Chart.js is a powerful, flexible JavaScript library for creating responsive data visualizations. The skill creates a complete MicroSim package suitable for embedding in educational content or documentation sites built with MkDocs. The default placement in a intelligent book uses an iframe with minimal padding and margins. Do not add any analysis or supporting documentation above or below the chart region.

Supported Chart Types

Chart.js supports the following chart types:

Line - Time series, trends, continuous data
Bar - Comparisons, categorical data, horizontal or vertical
Pie - Proportions, percentages, part-to-whole relationships
Doughnut - Similar to pie with central space for labels
Radar - Multi-dimensional data, spider/web charts
Polar Area - Similar to pie but with varying radius
Bubble - Three-dimensional data (x, y, size)
Scatter - Correlations, distributions, relationships
When to Use This Skill

Use this skill when users request:

Data visualizations: Any chart or graph for presenting data
Comparisons: Bar charts, grouped bars, stacked bars
Trends: Line charts, area charts, multi-line charts
Proportions: Pie charts, doughnut charts
Distributions: Scatter plots, bubble charts
Multi-dimensional data: Radar charts, bubble charts
Interactive charts: Hover tooltips, clickable elements, animations

Common trigger phrases:

"Create a [chart type] showing..."
"Visualize [data] as a [chart type]..."
"Build an interactive chart for..."
"Generate a graph showing..."
Workflow
Step 1: Determine Chart Type

If the user doesn't specify a chart type, ask them to select from the supported types:

Use the AskUserQuestion tool with these options:

Line Chart - Best for trends over time, continuous data
Bar Chart - Best for comparing categories, discrete data
Pie/Doughnut Chart - Best for showing proportions and percentages
Bubble/Scatter Chart - Best for multi-dimensional or correlation data
Radar Chart - Best for comparing multiple variables across categories
Polar Area Chart - Best for showing proportions with emphasis on differences
Step 2: Gather Data and Requirements

Before generating the chart, gather information about:

Data structure: What data needs to be visualized?

Data points/values
Labels/categories
Multiple datasets (if applicable)
Time periods or categories
Units of measurement

Chart configuration:

Chart title
Axis labels (for bar, line, scatter, bubble charts)
Legend requirements
Color scheme preferences
Special features (stacked, grouped, filled areas, etc.)

Context: What is the purpose of the visualization?

Educational content
Data analysis
Report or presentation
Dashboard component

Integration: Where will the chart be used?

Standalone page
Embedded in documentation
MkDocs site integration
Step 3: Create Directory Structure

Create a new directory for the MicroSim following this pattern:

docs/sims/<chart-name>/
├── main.html         # Main visualization file
├── style.css         # Styling
└── index.md          # Documentation (if part of MkDocs)


Naming convention: Use kebab-case (lowercase with hyphens) for directory names that are descriptive and URL-friendly (e.g., sales-trend-chart, market-share-pie, student-performance-radar).

Step 4: Create main.html with Chart.js

Generate the main HTML file with the following structure:

HTML boilerplate with proper meta tags
Chart.js CDN import: https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js
Canvas element for the chart
Optional analysis/legend section do not any analysis or documentation unless requested
JavaScript implementation:
Data array/object
Color scheme configuration
Chart.js configuration for the selected chart type
Custom plugins (if needed)
Interactive features (tooltips, legends, animations)
Tooltips should always be used

Key Chart.js configuration by type:

Line Chart
{
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', ...],
        datasets: [{
            label: 'Dataset 1',
            data: [12, 19, 3, 5, 2, 3],
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            tension: 0.1  // Curve smoothness
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: { beginAtZero: true }
        }
    }
}

Bar Chart
{
    type: 'bar',
    data: {
        labels: ['Category A', 'Category B', ...],
        datasets: [{
            label: 'Dataset 1',
            data: [65, 59, 80, 81, 56, 55],
            backgroundColor: 'rgba(54, 162, 235, 0.8)',
            borderColor: 'rgb(54, 162, 235)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: { beginAtZero: true }
        }
    }
}

Pie/Doughnut Chart
{
    type: 'pie',  // or 'doughnut'
    data: {
        labels: ['Red', 'Blue', 'Yellow', ...],
        datasets: [{
            data: [300, 50, 100],
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 206, 86, 0.8)'
            ]
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { position: 'top' }
        }
    }
}

Radar Chart
{
    type: 'radar',
    data: {
        labels: ['Strength', 'Speed', 'Intelligence', ...],
        datasets: [{
            label: 'Player 1',
            data: [65, 59, 90, 81, 56],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            pointBackgroundColor: 'rgb(255, 99, 132)'
        }]
    },
    options: {
        responsive: true,
        scales: {
            r: {
                beginAtZero: true,
                max: 100
            }
        }
    }
}

Bubble Chart
{
    type: 'bubble',
    data: {
        datasets: [{
            label: 'Dataset 1',
            data: [
                { x: 20, y: 30, r: 15 },  // r = bubble radius
                { x: 40, y: 10, r: 10 }
            ],
            backgroundColor: 'rgba(255, 99, 132, 0.8)'
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: { min: 0, max: 100 },
            y: { min: 0, max: 100 }
        }
    }
}

Scatter Chart
{
    type: 'scatter',
    data: {
        datasets: [{
            label: 'Dataset 1',
            data: [
                { x: -10, y: 0 },
                { x: 0, y: 10 },
                { x: 10, y: 5 }
            ],
            backgroundColor: 'rgba(255, 99, 132, 0.8)'
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: { type: 'linear', position: 'bottom' }
        }
    }
}


Important considerations:

Responsive design: Set responsive: true and appropriate aspect ratio
Color accessibility: Use distinguishable colors with good contrast
Tooltips: Customize tooltips to show relevant information
Legends: Position legends appropriately (top, bottom, left, right)
Animations: Enable/disable based on use case
Data labels: Use Chart.js plugins for data labels if needed
Step 5: Create style.css

Generate CSS with professional styling:

Reset and base styles: Clean defaults for cross-browser consistency
Chart container: Appropriate sizing, padding, box-shadow
Legend/analysis container: Styling for supplementary information
Interactive elements: Hover effects, transitions
Responsive design: Media queries for mobile/tablet
Print styles: Do not add additional CSS for printing

Key design principles:

Use clean, modern aesthetics
Assume placement of the chart in a book with narrow margins using a iframe
Provide clear visual hierarchy
Add subtle shadows and borders
Include smooth transitions
Ensure accessibility with sufficient contrast
Make text readable at all sizes
Step 6: Create index.md Documentation

If the chart is part of a MkDocs site, create comprehensive documentation:

YML Metadata: Add title, and description
Title and overview: Brief description of the visualization
Embedded iframe: Display the chart inline
Link to fullscreen: Markdown link to main.html with button "View MicroSim Fullscreen"
Interpretation guide: Explain how to read the chart
Features section: List interactive elements
Customization guide: Detailed instructions for modifying:
Data structure
Colors and styling
Chart options
Responsive behavior
Animations
Technical details: Dependencies, browser compatibility, file structure
Use cases: Other applications for this chart type
References: Links to Chart.js docs and related resources

Documentation structure template:

---
title: [Chart Title]
description: [brief description of chart]
---

# [Chart Title]

[Brief description]

## Interactive Chart

<iframe src="main.html" width="100%" height="500" scrolling="no"></iframe>

[View Fullscreen](main.html){ .md-button .md-button--primary }

## Overview

[Detailed explanation of what the chart shows]

## Features

### Interactive Elements
- Hover tooltips showing detailed data
- Clickable legend items to show/hide datasets
- Smooth animations on load and update

### Visual Design
- Color-coded categories
- Clear axis labels and grid lines
- Responsive layout

## Customization Guide

### Changing the Data

To modify the chart data, edit the `data` object in `main.html`:

```javascript
const data = {
    labels: ['Your', 'Labels', 'Here'],
    datasets: [{
        label: 'Your Dataset',
        data: [10, 20, 30, 40]
    }]
};

Adjusting Colors

Customize the color scheme by modifying the backgroundColor and borderColor properties:

backgroundColor: [
    'rgba(255, 99, 132, 0.8)',
    'rgba(54, 162, 235, 0.8)',
    // Add more colors...
]

Chart Options

Modify chart behavior in the options object:

options: {
    responsive: true,
    maintainAspectRatio: true,
    aspectRatio: 2,  // Width:height ratio
    plugins: {
        title: { display: true, text: 'Your Title' },
        legend: { position: 'top' }
    }
}

Technical Details
Library: Chart.js 4.4.0
Browser Compatibility: All modern browsers (Chrome, Firefox, Safari, Edge)
Dependencies: Chart.js (loaded from CDN)
Responsive: Yes, adapts to container width
Use Cases

This chart type is useful for:

[List relevant use cases]
References
- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [Chart Type Guide](https://www.chartjs.org/docs/latest/charts/[type].html)

Step 7: Integrate into Navigation (MkDocs)

Always add the chart to the navigation in mkdocs.yml:

- MicroSims:
    - Introduction: sims/index.md
    - [Chart Name]: sims/[chart-name]/index.md
    - [Other sims...]: ...


Place the entry in a alphabetical order.

Step 8: Test and Validate

Before considering the chart complete:

Visual testing:

Open main.html in a browser directly
Test with mkdocs serve if applicable
Check all breakpoints (desktop, tablet, mobile)
Verify data displays correctly
Confirm labels and legends are readable

Interactive testing:

Hover over chart elements to verify tooltips
Click legend items to show/hide datasets
Test animations (reload page)
Test on different browsers

Documentation review:

Verify all code examples are accurate
Test customization instructions
Check all internal and external links

Data validation:

Confirm all data points are plotted correctly
Verify calculations if applicable
Check that chart accurately represents the data
Best Practices
Data Preparation
Consistent formatting: Use consistent data types and formats
Meaningful labels: Use clear, descriptive labels
Appropriate scale: Choose scales that show data effectively
Complete data: Ensure all required fields are present
Visual Design
Color coding: Use intuitive, accessible color schemes
Contrast: Ensure sufficient contrast for readability
Labels: Make all text readable at different sizes
Spacing: Prevent overlap with appropriate padding
Consistency: Use consistent styling across charts
Documentation
Code examples: Provide exact, testable code snippets
Before/after: Show the effect of customizations
Parameter ranges: Suggest appropriate value ranges
Common issues: Address typical problems and solutions
MkDocs Integration
Iframe sizing: Use appropriate height for chart type (typically 500-900px)
Path references: Use relative paths (../sims/...)
Navigation placement: Group with related MicroSims
Responsive embedding: Ensure iframe is responsive
Chart Type Selection Guide

Help users choose the right chart type:

Chart Type	Best For	Not Suitable For
Line	Trends over time, continuous data	Categorical comparisons
Bar	Comparing categories, discrete data	Trends, continuous data
Pie/Doughnut	Part-to-whole, proportions (≤6 slices)	Precise comparisons, many categories
Radar	Comparing multiple variables, profiles	Single variable, continuous data
Polar Area	Proportions with emphasis on differences	Precise comparisons
Bubble	Three dimensions (x, y, size)	Simple 1D or 2D data
Scatter	Correlations, distributions	Categorical data
Common Variations
Stacked Bar Chart
options: {
    scales: {
        x: { stacked: true },
        y: { stacked: true }
    }
}

Horizontal Bar Chart
{
    type: 'bar',
    options: {
        indexAxis: 'y'  // Makes bars horizontal
    }
}

Multi-Line Chart

Add multiple datasets to a line chart:

data: {
    datasets: [
        { label: 'Series 1', data: [...], borderColor: 'red' },
        { label: 'Series 2', data: [...], borderColor: 'blue' }
    ]
}

Filled Area Chart
{
    type: 'line',
    data: {
        datasets: [{
            fill: true,  // Fill area under line
            backgroundColor: 'rgba(75, 192, 192, 0.2)'
        }]
    }
}

Troubleshooting
Chart Not Displaying

Solution: Check that Chart.js CDN is loading correctly and canvas element has an ID.

Data Not Updating

Solution: Ensure chart.update() is called after modifying data:

chart.data.datasets[0].data = newData;
chart.update();

Labels Overlapping

Solution: Rotate labels or reduce font size:

scales: {
    x: {
        ticks: {
            maxRotation: 45,
            minRotation: 45
        }
    }
}

Colors Not Showing

Solution: Verify color format (rgba, rgb, hex) and ensure arrays match data length.

Responsive Issues

Solution: Set container dimensions and use maintainAspectRatio:

options: {
    responsive: true,
    maintainAspectRatio: true,
    aspectRatio: 2
}

Advanced Features
Data Labels Plugin

To show values on chart elements, use the Chart.js Data Labels plugin:

<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2"></script>

Animations

Customize animation timing and easing:

options: {
    animation: {
        duration: 2000,
        easing: 'easeInOutQuart'
    }
}

Custom Tooltips

Create fully custom tooltip content:

plugins: {
    tooltip: {
        callbacks: {
            label: function(context) {
                return 'Custom: ' + context.parsed.y;
            }
        }
    }
}

Click Events

Handle click events on chart elements:

options: {
    onClick: (event, elements) => {
        if (elements.length > 0) {
            const dataIndex = elements[0].index;
            console.log('Clicked:', chart.data.labels[dataIndex]);
        }
    }
}

References

This skill uses the following assets and references:

Assets
Chart.js CDN: https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js
Optional Data Labels Plugin: https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2
No local assets required (Chart.js loaded from CDN)
References
Chart.js Documentation
Chart.js Samples
Chart.js GitHub
Chart Types Guide
Example Implementations

See example charts in /docs/sims/ directory for reference implementations of different chart types.

Weekly Installs
35
Repository
vishalsachdev/c…e-skills
GitHub Stars
2
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass