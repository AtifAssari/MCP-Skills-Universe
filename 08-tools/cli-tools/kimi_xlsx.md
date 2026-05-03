---
title: kimi-xlsx
url: https://skills.sh/thvroyal/kimi-skills/kimi-xlsx
---

# kimi-xlsx

skills/thvroyal/kimi-skills/kimi-xlsx
kimi-xlsx
Installation
$ npx skills add https://github.com/thvroyal/kimi-skills --skill kimi-xlsx
SKILL.md
You must eventually deliver an Excel file, one or more depending on the task, but what must be delivered must include a .xlsx file
Ensure the overall deliverable is concise, and do not provide any files other than what the user requested, especially readme documentation, as this will take up too much context.
Excel File Creation: Python + openpyxl/pandas

✅ REQUIRED Technology Stack for Excel Creation:

Runtime: Python 3
Primary Library: openpyxl (for Excel file creation, styling, formulas)
Data Processing: pandas (for data manipulation, then export via openpyxl)
Execution: Use ipython tool for Python code

✅ Validation & PivotTable Tools:

Tool: KimiXlsx (unified CLI tool for validation, recheck, pivot, etc.)
Execution: Use shell tool for CLI commands

🔧 Execution Environment:

Use ipython tool for Excel creation with openpyxl/pandas
Use shell tool for validation commands

Python Excel Creation Pattern:

from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Border, Side, Alignment
import pandas as pd

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = "Data"

# Add data
ws['A1'] = "Header1"
ws['B1'] = "Header2"

# Apply styling
ws['A1'].font = Font(bold=True, color="FFFFFF")
ws['A1'].fill = PatternFill(start_color="333333", end_color="333333", fill_type="solid")

# Save
wb.save('output.xlsx')


</Technology Stack>

When creating Excel files with externally fetched data:

Source Citation (MANDATORY):

ALL external data MUST have source citations in final Excel
🚨 This applies to ALL external tools: datasource, web_search, API calls, or any fetched data
Use two separate columns: Source Name | Source URL
Do NOT use HYPERLINK function (use plain text to avoid formula errors)
⛔ FORBIDDEN: Delivering Excel with external data but NO source citations
Example:
Data Content	Source Name	Source URL
Apple Revenue	Yahoo Finance	https://finance.yahoo.com/...
China GDP	World Bank API	world_bank_open_data
If citation per-row is impractical, create a dedicated "Sources" sheet

</External Data in Excel>

1. Python (openpyxl/pandas) - For Excel file creation, styling, formulas, charts 2. KimiXlsx CLI Tool - For validation, error checking, and PivotTable creation

The KimiXlsx tool has 6 commands that can be called using the shell tool:

Executable Path: /app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx

Base Command: /app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx <command> [arguments]

recheck ⚠️ RUN FIRST for formula errors

description：This tool detects:

Formula errors: #VALUE!, #DIV/0!, #REF!, #NAME?, #NULL!, #NUM!, #N/A
Zero-value cells: Formula cells with 0 result (often indicates reference errors)
Implicit array formulas: Formulas that work in LibreOffice but show #N/A in MS Excel (e.g., MATCH(TRUE(), range>0, 0))

Implicit Array Formula Detection:

Patterns like MATCH(TRUE(), range>0, 0) require CSE (Ctrl+Shift+Enter) in MS Excel
LibreOffice handles these automatically, so they pass LibreOffice recalculation but fail in Excel
When detected, rewrite the formula using alternatives:
❌ =MATCH(TRUE(), A1:A10>0, 0) → shows #N/A in Excel
✅ =SUMPRODUCT((A1:A10>0)*ROW(A1:A10))-ROW(A1)+1 → works in all Excel versions
✅ Or use helper column with explicit TRUE/FALSE values

how to use:

/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx recheck output.xlsx

reference-check (alias: refcheck)
description: This tool is used to Detect potential reference errors and pattern anomalies in Excel formulas. It can identify 4 common issues when AI generates formulas:

Out-of-range references - Formulas reference a range far exceeding the actual number of data rows. Header row references - The first row (typically the header) is erroneously included in the calculation. Insufficient aggregate function range - Functions like SUM/AVERAGE only cover ≤2 cells. Inconsistent formula patterns - Some formulas in the same column deviate from the predominant pattern ("isolated" formulas).

how to use:
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx reference-check output.xlsx

inspect
description: This command analyzes Excel file structure and outputs JSON describing all sheets, tables, headers, and data ranges. Use this to understand an Excel file's structure before processing.
how to use:
# Analyze and output JSON
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx inspect input.xlsx --pretty

pivot 🚨 REQUIRES pivot-table.md
description: Create PivotTable with optional chart using pure OpenXML SDK. This is the ONLY supported method for PivotTable creation. Automatically creates a chart (bar/line/pie) alongside the PivotTable.
⚠️ CRITICAL: Before using this command, you MUST read /app/.kimi/skills/kimi-xlsx/pivot-table.md for full documentation.
required parameters:
input.xlsx - Input Excel file (positional)
output.xlsx - Output Excel file (positional)
--source "Sheet!A1:Z100" - Source data range
--location "Sheet!A3" - Where to place PivotTable
--values "Field:sum" - Value fields with aggregation (sum/count/avg/max/min)
optional parameters:
--rows "Field1,Field2" - Row fields
--cols "Field1" - Column fields
--filters "Field1" - Filter/page fields
--name "PivotName" - PivotTable name (default: PivotTable1)
--style "monochrome" - Style theme: monochrome (default) or finance
--chart "bar" - Chart type: bar (default), line, or pie
how to use:
# First: inspect to get sheet names and headers
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx inspect data.xlsx --pretty

# Then: create PivotTable with chart
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx pivot \
    data.xlsx output.xlsx \
    --source "Sales!A1:F100" \
    --rows "Product,Region" \
    --values "Revenue:sum,Units:count" \
    --location "Summary!A3" \
    --chart "bar"

chart-verify
description: Verify that all charts have actual data content. Use this after creating charts to ensure they are not empty.
how to use:
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx chart-verify output.xlsx

exit codes:
0 = All charts have data, safe to deliver
1 = Charts are empty or broken - MUST FIX
validate ⚠️ MANDATORY - MUST RUN BEFORE DELIVERY

description: OpenXML structure validation. Files that fail this validation CANNOT be opened by Microsoft Excel. You MUST run this command before delivering any Excel file.

What it checks:

OpenXML schema compliance (Office 2013 standard)
PivotTable and Chart structure integrity
Incompatible functions (FILTER, UNIQUE, XLOOKUP, etc. - not supported in Excel 2019 and earlier)
.rels file path format (absolute paths cause Excel to crash)

exit codes:

0 = Validation passed, safe to deliver
Non-zero = Validation failed - DO NOT DELIVER, regenerate the file

how to use:

/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx validate output.xlsx

If validation fails: Do NOT attempt to "fix" the file. Regenerate it from scratch with corrected code.

</Tool script list>

<Excel Creation Workflow - MUST FOLLOW>

📋 Excel Creation Workflow (Per-Sheet Validation)

🚨 CRITICAL: Validate EACH sheet immediately after creation, NOT after all sheets are done!

For each sheet in workbook:
    1. PLAN   → Design this sheet's structure, formulas, references
    2. CREATE → Write data, formulas, styling for this sheet
    3. SAVE   → Save the workbook (wb.save())
    4. CHECK  → Run recheck + reference-check → Fix until 0 errors
    5. NEXT   → Only proceed to next sheet after current sheet has 0 errors

After ALL sheets pass:
    6. VALIDATE → Run `validate` command → Fix until exit code 0
    7. DELIVER  → Only deliver files that passed ALL validations

Per-Sheet Check Commands
# After creating/modifying EACH sheet, save and run:
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx recheck output.xlsx
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx reference-check output.xlsx
# Fix ALL errors before creating the next sheet!

Final Validation (after all sheets complete)
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx validate output.xlsx


Why Per-Sheet Validation?

Errors in Sheet 1 propagate to Sheet 2, Sheet 3... causing cascading failures
Fixing 3 errors per sheet is easier than fixing 30 errors at the end
Cross-sheet references can be validated immediately

</Excel Creation Workflow - MUST FOLLOW>

⚠️ CRITICAL: Excel Formulas Are ALWAYS the First Choice

For ANY analysis task, using Excel formulas is the default and preferred approach. Wherever a formula CAN be used, it MUST be used.

✅ CORRECT - Use Excel formulas:

ws['C2'] = '=A2+B2'           # Sum
ws['D2'] = '=C2/B2*100'       # Percentage
ws['E2'] = '=SUM(A2:A100)'    # Aggregation


❌ FORBIDDEN - Pre-calculate in Python and paste static values:

result = value_a + value_b
ws['C2'] = result    # BAD: Static value, not a formula


Only use static values when:

Data is fetched from external sources (web search, API)
Values are constants that never change
Formula would create circular reference

Follow this workflow::

Sheet 1: Plan (write detailed design) → Create → Save → Run Recheck → Run ReferenceCheck → Fix errors → Zero errors ✓
Sheet 2: Plan (write detailed design) → Create → Save → Run Recheck → Run ReferenceCheck → Fix errors → Zero errors ✓
Sheet 3: Plan (write detailed design) → Create → Save → Run Recheck → Run ReferenceCheck → Fix errors → Zero errors ✓
...


🚨 CRITICAL: Recheck Results Are FINAL - NO EXCEPTIONS

The recheck command detects formula errors (#VALUE!, #DIV/0!, #REF!, #NAME?, #N/A, etc.) and zero-value cells. You MUST follow these rules strictly:

ZERO TOLERANCE for errors: If recheck reports ANY errors, you MUST fix them before delivery. There are NO exceptions.

DO NOT assume errors will "auto-resolve":

❌ WRONG: "These errors will disappear when the user opens the file in Excel"
❌ WRONG: "Excel will recalculate and fix these errors automatically"
✅ CORRECT: Fix ALL errors reported by recheck until error_count = 0

Errors detected = Errors to fix:

If recheck shows error_count: 5, you have 5 errors to fix
If recheck shows zero_value_count: 3, you have 3 suspicious cells to verify
Only when error_count: 0 can you proceed to the next step

Common mistakes to avoid:

❌ "The #REF! error is because openpyxl doesn't evaluate formulas" - WRONG, fix it!
❌ "The #VALUE! will resolve when opened in Excel" - WRONG, fix it!
❌ "Zero values are expected" - VERIFY each one, many are reference errors!

Delivery gate: Files with ANY recheck errors CANNOT be delivered to users.

Forbidden Patterns ❌:

1. Create Sheet 1 → Create Sheet 2 → Create Sheet 3 → Run Recheck once at end
   ❌ WRONG: Errors accumulate, debugging becomes exponentially harder
   ✅ CORRECT: Check after EACH sheet, fix before moving to next

2. Skip planning for any sheet
   ❌ WRONG: Causes 80%+ of reference errors
   ✅ CORRECT: Plan each sheet's structure before creating it

3. Recheck shows errors → Ignore and deliver anyway
   ❌ ABSOLUTELY FORBIDDEN - errors must be fixed, not ignored!

4. Recheck shows errors → Proceed to create next sheet anyway
   ❌ WRONG: Errors in Sheet 1 will cascade to Sheet 2, 3...
   ✅ CORRECT: Fix ALL errors in current sheet before creating next sheet


</Analyze loop>

Syntax: =VLOOKUP(lookup_value, table_array, col_index_num, FALSE) — lookup column MUST be leftmost in table_array Best Practices: Use FALSE for exact match; Lock range with $A$2:$D$100; Wrap with IFERROR(...,"N/A"); Cross-sheet: Sheet2!$A$2:$C$100 Errors: #N/A=not found; #REF!=col_index exceeds columns. Alt: INDEX/MATCH when lookup column not leftmost

ws['D2'] = '=IFERROR(VLOOKUP(A2,$G$2:$I$50,3,FALSE),"N/A")'


</VLOOKUP Usage Rules>

🚨 CRITICAL: PivotTable Creation Requires Reading pivot-table.md

When to Trigger: Detect ANY of these user intents:

User explicitly requests "pivot table", "data pivot", "数据透视表"
Task requires data summarization by categories
Keywords: summarize, aggregate, group by, categorize, breakdown, statistics, distribution, count by, total by
Dataset has 50+ rows with grouping needs
Cross-tabulation or multi-dimensional analysis needed

⚠️ MANDATORY ACTION: When PivotTable need is detected, you MUST:

READ /app/.kimi/skills/kimi-xlsx/pivot-table.md FIRST
Follow the execution order and workflow in that document
Use the pivot command (NOT manual code construction)

Why This Is Required:

PivotTable creation uses pure OpenXML SDK (C# tool)
The pivot command provides stable, tested implementation
Manual pivot construction in openpyxl is NOT supported and forbidden
Chart types (bar/line/pie) are automatically created with PivotTable

Quick Reference (Details in pivot-table.md):

# Step 1: Inspect data structure
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx inspect data.xlsx --pretty

# Step 2: Create PivotTable with chart
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx pivot \
    data.xlsx output.xlsx \
    --source "Sheet!A1:F100" \
    --rows "Category" \
    --values "Revenue:sum" \
    --location "Summary!A3" \
    --chart "bar"

# Step 3: Validate
/app/.kimi/skills/kimi-xlsx/scripts/KimiXlsx validate output.xlsx


⛔ FORBIDDEN:

Creating PivotTable manually with openpyxl code
Skipping the inspect step
Not reading pivot-table.md before creating PivotTable
🚨 NEVER modify pivot output file with openpyxl - openpyxl will corrupt pivotCache paths!

⚠️ CRITICAL: Workflow Order for PivotTable If you need to add extra sheets (Cover, Summary, etc.) to a file that will have PivotTable:

FIRST: Create ALL sheets with openpyxl (data sheets, cover sheet, styling, etc.)
THEN: Run pivot command as the FINAL STEP
NEVER: Open the pivot output file with openpyxl again - this corrupts the file!
✅ CORRECT ORDER:
   openpyxl creates base.xlsx (with Cover, Data sheets)
   → pivot command: base.xlsx → final.xlsx (adds PivotTable)
   → validate final.xlsx
   → DELIVER final.xlsx (do NOT modify again)

❌ WRONG ORDER (WILL CORRUPT FILE):
   pivot command creates pivot.xlsx
   → openpyxl opens pivot.xlsx to add Cover sheet  ← CORRUPTS FILE!
   → File cannot be opened in MS Excel


</PivotTable Module>

🚨 FORBIDDEN FUNCTIONS (Incompatible with older Excel versions):

The following functions are NOT supported in Excel 2019 and earlier. Files using these functions will FAIL to open in older Excel versions. Use traditional alternatives instead.

❌ Forbidden Function	✅ Alternative
FILTER()	Use AutoFilter, or SUMIF/COUNTIF/INDEX-MATCH
UNIQUE()	Use Remove Duplicates feature, or helper column with COUNTIF
SORT(), SORTBY()	Use Excel's Sort feature (Data → Sort)
XLOOKUP()	Use INDEX() + MATCH() combination
XMATCH()	Use MATCH()
SEQUENCE()	Use ROW() or manual fill
LET()	Define intermediate calculations in helper cells
LAMBDA()	Use named ranges or VBA
RANDARRAY()	Use RAND() with fill-down
ARRAYFORMULA()	Google Sheets only - use Ctrl+Shift+Enter array formulas
QUERY()	Google Sheets only - use SUMIF/COUNTIF/PivotTable
IMPORTRANGE()	Google Sheets only - copy data manually

Why these are forbidden:

These are Excel 365/2021+ dynamic array functions or Google Sheets functions
Older Excel versions (2019, 2016, etc.) cannot parse these formulas
The file will crash or show errors when opened in older Excel
The validate command will detect and reject files using these functions

Example - Converting FILTER to INDEX-MATCH:

❌ WRONG: =FILTER(A2:C100, B2:B100="Active")
✅ CORRECT: Use AutoFilter on the data range, or create a PivotTable


⚠️ Off-By-One Prevention: Before saving, verify each formula references correct cells. Run reference-check tool. Common errors: referencing headers, wrong row/column offset. If result is 0 or unexpected → check references first.

💰 Financial Values: Store in smallest unit (15000000 not 1.5M). Use Excel format for display: "¥#,##0". Never use scaled units requiring conversion in formulas.

</Baseline error>

</Analyze rule>

Weekly Installs
196
Repository
thvroyal/kimi-skills
GitHub Stars
147
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass