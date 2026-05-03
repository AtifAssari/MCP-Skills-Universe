---
title: sgds-data-visualisation
url: https://skills.sh/govtechsg/sgds-web-component/sgds-data-visualisation
---

# sgds-data-visualisation

skills/govtechsg/sgds-web-component/sgds-data-visualisation
sgds-data-visualisation
Installation
$ npx skills add https://github.com/govtechsg/sgds-web-component --skill sgds-data-visualisation
SKILL.md
SGDS Data Visualisation Pattern

SGDS does not bundle a charting library. For data visualisation, use Apache ECharts and apply the SGDS colour palette so charts remain visually consistent with your design system.

Prerequisites
Complete base project setup per sgds-getting-started.
Install and configure ECharts independently — see https://echarts.apache.org/.
Installing ECharts

ECharts is not included in @govtechsg/sgds-web-component. Install it separately:

npm install echarts


Then import and initialise per the ECharts getting started guide:

import * as echarts from "echarts";

const chart = echarts.init(document.getElementById("chart"));
chart.setOption(option);

SGDS Colour Palette for ECharts

Apply the SGDS palette by setting the color array in your chart option. The values below are the raw hex values of the SGDS data-visualisation primitive tokens:

Token	Hex
--sgds-purple-600	#ac1cdb
--sgds-cyan-600	#00758d
--sgds-green-600	#0e7c3d
--sgds-blue-600	#0269d0
--sgds-yellow-600	#7e6917
Per-chart (recommended)

Set color directly in the chart option. ECharts cycles through the colours sequentially across series:

const option = {
  color: ["#ac1cdb", "#00758d", "#0e7c3d", "#0269d0", "#7e6917"],
  // ... rest of chart option
};

Global theme (all charts on the page)

Register a named theme once at app startup, then pass the theme name when initialising each chart:

import * as echarts from "echarts";

echarts.registerTheme("sgds", {
  color: ["#ac1cdb", "#00758d", "#0e7c3d", "#0269d0", "#7e6917"],
});

const chart = echarts.init(document.getElementById("chart"), "sgds");

For AI Agents
ECharts is not provided by SGDS — always tell users to install it separately from https://echarts.apache.org/.
The five SGDS palette colours are fixed hex values taken from the primitive tokens. Do not reference CSS variables inside the ECharts color array — ECharts does not resolve CSS custom properties.
For a single chart, set color in the option object. For multiple charts sharing the same palette, use echarts.registerTheme() once at app startup.
Palette order: purple → cyan → green → blue → yellow. ECharts cycles through them automatically across series.
Weekly Installs
49
Repository
govtechsg/sgds-…omponent
GitHub Stars
12
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass