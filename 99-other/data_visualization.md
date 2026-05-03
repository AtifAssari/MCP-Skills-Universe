---
title: data_visualization
url: https://skills.sh/vuralserhat86/antigravity-agentic-skills/data_visualization
---

# data_visualization

skills/vuralserhat86/antigravity-agentic-skills/data_visualization
data_visualization
Installation
$ npx skills add https://github.com/vuralserhat86/antigravity-agentic-skills --skill data_visualization
SKILL.md
Overview

This skill empowers Claude to transform raw data into compelling visual representations. It leverages intelligent automation to select optimal visualization types and generate informative plots, charts, and graphs. This skill helps users understand complex data more easily.

How It Works
Data Analysis: Claude analyzes the provided data to understand its structure, type, and distribution.
Visualization Selection: Based on the data analysis, Claude selects the most appropriate visualization type (e.g., bar chart, scatter plot, line graph).
Visualization Generation: Claude generates the visualization using appropriate libraries and best practices for visual clarity and accuracy.
When to Use This Skill

This skill activates when you need to:

Create a visual representation of data.
Generate a specific type of plot, chart, or graph (e.g., "create a bar chart").
Explore data patterns and relationships through visualization.
Examples
Example 1: Visualizing Sales Data

User request: "Create a bar chart showing sales by region."

The skill will:

Analyze the sales data, identifying regions and corresponding sales figures.
Generate a bar chart with regions on the x-axis and sales on the y-axis.
Example 2: Plotting Stock Prices

User request: "Plot the stock price of AAPL over the last year."

The skill will:

Retrieve historical stock price data for AAPL.
Generate a line graph showing the stock price over time.
Best Practices
Specific Requests: Be specific about the desired visualization type and any relevant data filters.
Contextual Information: Provide context about the data and the purpose of the visualization.

Data Visualization v1.1 - Enhanced

🔄 Workflow

Kaynak: Financial Times Visual Vocabulary

Aşama 1: Data Profiling
 Type Check: Veri kategorik mi, sayısal mı, zaman serisi mi?
 Volume: Veri noktası sayısı (az ise Bar, çok ise Scatter/Line).
 Goal: Amaç karşılaştırma (Bar), dağılım (Hist), ilişki (Scatter) veya kompozisyon (Pie/Stack) mu?
Aşama 2: Drafting
 Library: Python için matplotlib/seaborn, Web için D3.js/Recharts.
 Mapping: X/Y eksenlerini ve renk kodlarını (hue) ata.
 Scale: Eksenleri sıfırdan başlat (Zorunlu olmayan durumlar hariç).
Aşama 3: Refinement (Design)
 Clutter: Gereksiz çizgileri (gridlines) ve çerçeveleri kaldır.
 Labels: Eksenleri ve başlığı net bir şekilde etiketle.
 Access: Renk körleri için uygun palet kullan (ColorOracle ile test et).
Kontrol Noktaları
Aşama	Doğrulama
1	Seçilen grafik türü veri tipine uygun mu? (Örn: Zaman serisi için Bar değil Line)
2	Veri "ink-to-data ratio" yüksek mi? (Gereksiz süsleme yok)
3	Eksenler manipülatif değil mi? (Truncated Y-axis uyarısı)
Integration

This skill can be integrated with other data processing and analysis tools within the Claude Code environment. It can receive data from other skills and provide visualizations for further analysis or reporting.

Weekly Installs
10
Repository
vuralserhat86/a…c-skills
GitHub Stars
42
First Seen
Jan 24, 2026