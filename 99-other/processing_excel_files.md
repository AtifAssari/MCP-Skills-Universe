---
title: processing-excel-files
url: https://skills.sh/zgldh/xlsx-populate-skill/processing-excel-files
---

# processing-excel-files

skills/zgldh/xlsx-populate-skill/processing-excel-files
processing-excel-files
Installation
$ npx skills add https://github.com/zgldh/xlsx-populate-skill --skill processing-excel-files
SKILL.md
Processing Excel Files

Edit and manipulate Excel files using the xlsx-populate library while perfectly preserving original formatting.

When to Use
User wants to edit existing Excel files without destroying formatting
Working with .xlsx files that have complex layouts or merged cells
Need to add formulas, styling, or new worksheets to existing files
Creating Excel reports from templates
When NOT to Use
Only need to read data from Excel (use xlsx library instead for better performance)
Creating simple Excel files from scratch without formatting concerns
Quick Start
const XlsxPopulate = require('xlsx-populate');

// Load and edit
const workbook = await XlsxPopulate.fromFileAsync('input.xlsx');
workbook.sheet(0).cell('A1').value('Updated');
await workbook.toFileAsync('output.xlsx');

Installation
npm install xlsx-populate

Core Operations
1. Load and Preserve Formatting
const workbook = await XlsxPopulate.fromFileAsync('file.xlsx');
const sheet = workbook.sheet(0);

// All original formatting is preserved automatically
sheet.cell('A1').value('New Value');
await workbook.toFileAsync('output.xlsx');

2. Add Formulas
// Use formulas, not hardcoded values
sheet.cell('D10').formula('=SUM(D2:D9)');
sheet.cell('E5').formula('=(C5-B5)/B5');  // Growth rate

3. Apply Styles
sheet.cell('A1').style({
  bold: true,
  fontSize: 14,
  fill: '4472C4',
  fontColor: 'FFFFFF'
});

4. Manage Worksheets
// Add new sheet
const newSheet = workbook.addSheet('Summary');

// Reorder sheets
workbook.sheets()[2].move(0);

// Rename sheet
workbook.sheet(0).name('Cover Page');

5. Merge Cells
sheet.range('A1:D1').merged(true);
sheet.range('A1:D1').style({
  horizontalAlignment: 'center'
});

Advanced Patterns

Batch Data Writing: See [BATCH-OPERATIONS.md] for large dataset handling Formula Patterns: See [FORMULAS.md] for financial modeling standards
Style Guide: See [STYLES.md] for color schemes and formatting Complete Examples: See [EXAMPLES.md] for real-world scenarios

Best Practices

Always preserve originals: Never overwrite source files

await workbook.toFileAsync('output.xlsx');  // ✅ New file
// NOT: await workbook.toFileAsync('input.xlsx');  // ❌ Don't overwrite


Use formulas for calculations: Let Excel do the math

sheet.cell('B10').formula('=SUM(B2:B9)');  // ✅
// NOT: sheet.cell('B10').value(calculateSum());  // ❌


Handle errors gracefully:

try {
  const workbook = await XlsxPopulate.fromFileAsync('file.xlsx');
  // ... operations
  await workbook.toFileAsync('output.xlsx');
} catch (error) {
  console.error('Excel operation failed:', error.message);
}

Common Issues

Q: File size increased significantly?
A: Normal - xlsx-populate preserves more metadata. Use xlsx library if file size is critical.

Q: Formulas not calculating?
A: Formulas are preserved but calculated when opened in Excel. Use data_only=True to read calculated values.

Q: How to check merged cells?
A: const merges = sheet._mergeCells;

Reference
xlsx-populate GitHub
Library documentation: node_modules/xlsx-populate/docs/
Weekly Installs
121
Repository
zgldh/xlsx-popu…te-skill
GitHub Stars
5
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass