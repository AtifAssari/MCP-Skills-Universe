---
title: openpyxl
url: https://skills.sh/vamseeachanta/workspace-hub/openpyxl
---

# openpyxl

skills/vamseeachanta/workspace-hub/openpyxl
openpyxl
Installation
$ npx skills add https://github.com/vamseeachanta/workspace-hub --skill openpyxl
SKILL.md
Openpyxl
Overview

Openpyxl is a Python library for reading and writing Excel 2010+ xlsx/xlsm files. This skill covers comprehensive patterns for spreadsheet automation including:

Workbook creation with multiple worksheets
Cell operations including formatting, merging, and data validation
Formula support for calculations and dynamic content
Chart generation for data visualization within Excel
Conditional formatting for visual data analysis
Large dataset handling with optimized read/write modes
Pivot table creation for data summarization
Style management for professional appearances
When to Use This Skill
USE when:
Creating Excel reports with formulas and calculations
Generating spreadsheets from database queries
Automating financial reports and dashboards
Building Excel templates with formatting
Processing and transforming existing Excel files
Creating charts and visualizations in Excel
Applying conditional formatting rules
Building data entry forms with validation
Handling large datasets (100k+ rows)
Creating pivot tables programmatically
DON'T USE when:
Only need to read data into pandas (use pandas.read_excel directly)
Need real-time Excel manipulation (use xlwings on Windows)
Working with .xls format (use xlrd/xlwt)
Creating complex macros (requires VBA)
Need Excel-specific features like Power Query
Prerequisites
Installation
# Basic installation
pip install openpyxl

# Using uv (recommended)
uv pip install openpyxl

# With image support
pip install openpyxl Pillow


*See sub-skills for full details.*
### Verify Installation

```python
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border
from openpyxl.chart import BarChart, LineChart, PieChart
from openpyxl.utils.dataframe import dataframe_to_rows

print("openpyxl installed successfully!")

Version History
1.0.0 (2026-01-17)
Initial skill creation
Core capabilities documentation
6 complete code examples
Large dataset handling patterns
Integration with pandas
Resources
Official Documentation: https://openpyxl.readthedocs.io/
GitHub Repository: https://github.com/theorchard/openpyxl
PyPI Package: https://pypi.org/project/openpyxl/
Related Skills
pandas-data-processing - Data analysis and transformation
python-docx - Word document generation
plotly - Interactive chart generation
pypdf - PDF manipulation

This skill provides comprehensive patterns for Excel automation refined from production data processing systems.

Sub-Skills
1. Basic Workbook Creation
2. Advanced Cell Formatting
3. Chart Generation
4. Conditional Formatting
5. Large Dataset Handling with Streaming
6. Pivot Table Creation
Pandas Integration (+1)
1. Memory Management (+2)
Common Issues
Weekly Installs
36
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