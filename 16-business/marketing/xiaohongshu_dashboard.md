---
title: xiaohongshu-dashboard
url: https://skills.sh/belljia95/xiaohongshu-dashboard-skill/xiaohongshu-dashboard
---

# xiaohongshu-dashboard

skills/belljia95/xiaohongshu-dashboard-skill/xiaohongshu-dashboard
xiaohongshu-dashboard
Installation
$ npx skills add https://github.com/belljia95/xiaohongshu-dashboard-skill --skill xiaohongshu-dashboard
SKILL.md
Xiaohongshu Dashboard Skill

Generate a tech-minimalist dark-mode analytics dashboard from Xiaohongshu creator center Excel exports.

Output

A single index.html file containing:

5 KPI metric cards (impressions, CTR, interactions, utility ratio, follower gain)
North Star trend chart (impressions vs followers over time)
Follower growth trend (cumulative + daily bar)
Follower conversion efficiency Top 10 (followers per 1K impressions)
Note ranking list with tabs (by impressions / interactions / followers)
Title keyword analysis (high-engagement + high-conversion keywords)
Date range filter (month picker)
Fully responsive (desktop / iPad / iPhone)

Tech stack: vanilla HTML/CSS/JS + Chart.js CDN. No build tools needed.

Workflow
Step 1: Collect the Excel file

Ask the user to provide their Xiaohongshu creator center data export Excel file (.xlsx).

The Excel typically contains columns like:

Title / Content title
Publish date
Content type (image-text / video)
Impressions / Views / CTR
Likes / Comments / Collects / Shares
Follower gain
Average view time
Step 2: Process the data

Run scripts/process_excel.py to read the Excel and output a JSON data blob.

python scripts/process_excel.py <path-to-excel-file>


The script handles:

Flexible column name matching (different Xiaohongshu export versions use different names)
Date parsing and month extraction
CTR normalization (percentage vs decimal)
Chinese keyword n-gram analysis for title keywords
Outputs JSON to stdout

If pandas/openpyxl are not installed, install them first:

pip install pandas openpyxl

Step 3: Generate the dashboard
Read assets/template.html
Replace the placeholder __RAW_DATA_PLACEHOLDER__ with the JSON output from Step 2
Write the result as index.html in the user's chosen output directory
Step 4: Open for preview

Open the generated index.html in the user's default browser so they can preview it immediately.

Design Specs
Theme: Tech-minimalist dark mode (inspired by Linear/Vercel/Raycast)
Background: zinc-950 (#09090b) with subtle grid pattern
Cards: Glass-morphism with backdrop-filter blur
Accent: Neon red (#FF4D6D) for primary metrics, neon green (#10B981) for growth metrics
Fonts: Inter (sans) + JetBrains Mono (mono) from Google Fonts CDN
Charts: Chart.js with gradient fills, custom tooltips, monospace axis labels
Customization

If the user wants to customize the dashboard:

Colors: Modify CSS variables in :root
Metrics: Add/remove metric cards in the metrics-grid section
Charts: Modify Chart.js config in the <script> section
Weekly Installs
53
Repository
belljia95/xiaoh…rd-skill
GitHub Stars
5
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass