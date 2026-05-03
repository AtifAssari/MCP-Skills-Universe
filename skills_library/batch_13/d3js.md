---
title: d3js
url: https://skills.sh/vamseeachanta/workspace-hub/d3js
---

# d3js

skills/vamseeachanta/workspace-hub/d3js
d3js
Installation
$ npx skills add https://github.com/vamseeachanta/workspace-hub --skill d3js
SKILL.md
D3Js
When to Use This Skill

Use D3.js when you need:

Complete customization - Every aspect of the visualization controlled
Complex interactions - Advanced user interactions and transitions
Unique visualizations - Bespoke charts not available in other libraries
Data-driven DOM manipulation - Direct binding of data to DOM elements
Custom animations - Sophisticated transitions and effects

Avoid when:

Simple charts with default styling are sufficient (use Chart.js)
Quick implementation is priority (use Plotly or Chart.js)
Team lacks JavaScript expertise
Complete Examples
Example 1: Interactive Bar Chart
<!DOCTYPE html>
<html>
<head>
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <style>
    .bar { fill: steelblue; cursor: pointer; }
    .bar:hover { fill: orange; }
    .tooltip {
      position: absolute;

*See sub-skills for full details.*
### Example 2: Animated Line Chart with CSV Data

```javascript
// Load and visualize CSV data
d3.csv('../data/timeseries.csv').then(data => {
  // Parse dates and values
  const parseDate = d3.timeParse('%Y-%m-%d');
  data.forEach(d => {
    d.date = parseDate(d.date);
    d.value = +d.value;
  });


*See sub-skills for full details.*
### Example 3: Force-Directed Network Graph

```javascript
// Network data
const nodes = [
  { id: 'A', group: 1 },
  { id: 'B', group: 1 },
  { id: 'C', group: 2 },
  { id: 'D', group: 2 },
  { id: 'E', group: 3 }
];


*See sub-skills for full details.*

## Common Patterns

### Update Pattern (Enter, Update, Exit)

```javascript
function update(data) {
  // Bind data
  const circles = svg.selectAll('circle')
    .data(data, d => d.id);

  // EXIT: Remove old elements
  circles.exit()
    .transition()
    .duration(500)

*See sub-skills for full details.*
### Brush and Zoom

```javascript
// Add zoom behavior
const zoom = d3.zoom()
  .scaleExtent([1, 10])
  .on('zoom', zoomed);

svg.call(zoom);

function zoomed(event) {
  const transform = event.transform;

*See sub-skills for full details.*

## Installation & Setup

### CDN (Quick Start)

```html
<script src="https://d3js.org/d3.v7.min.js"></script>

NPM (Production)
npm install d3

import * as d3 from 'd3';
// Or import specific modules
import { select, scaleLinear, axisBottom } from 'd3';

Performance Tips
Minimize DOM operations - Batch updates when possible
Use canvas for large datasets - Switch to canvas for >1000 points
Throttle events - Debounce mousemove/scroll events
Optimize transitions - Limit concurrent animations
Use web workers - Offload heavy computations
Resources
Official Docs: https://d3js.org/
Observable: https://observablehq.com/@d3 (Interactive examples)
GitHub: https://github.com/d3/d3
Gallery: https://observablehq.com/@d3/gallery
Integration with Other Tools
With React
import { useEffect, useRef } from 'react';
import * as d3 from 'd3';

function D3Chart({ data }) {
  const svgRef = useRef();

  useEffect(() => {
    const svg = d3.select(svgRef.current);
    // D3 code here
  }, [data]);

  return <svg ref={svgRef}></svg>;
}

With CSV/JSON Data
// Load from relative path
d3.csv('../data/data.csv').then(data => {
  // Process and visualize
});

d3.json('../data/data.json').then(data => {
  // Visualize JSON
});


Use this skill when you need maximum control and customization in your data visualizations!

Sub-Skills
1. Data Binding (+3)
1. Use Proper Margins Convention (+3)
Weekly Installs
29
Repository
vamseeachanta/w…pace-hub
GitHub Stars
8
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass