---
rating: ⭐⭐⭐
title: add-excel
url: https://skills.sh/microsoft/power-platform-skills/add-excel
---

# add-excel

skills/microsoft/power-platform-skills/add-excel
add-excel
Installation
$ npx skills add https://github.com/microsoft/power-platform-skills --skill add-excel
SKILL.md

📋 Shared Instructions: shared-instructions.md - Cross-cutting concerns.

Add Excel Online
Workflow
Check Memory Bank → 2. Gather → 3. Add Connector → 4. Configure → 5. Build → 6. Update Memory Bank
Step 1: Check Memory Bank

Check for memory-bank.md per shared-instructions.md.

Step 2: Gather

Ask the user:

Where is the workbook? (OneDrive or SharePoint)
Workbook file name
Which table(s) in the workbook to access
Step 3: Add Connector

First, find the connection ID (see connector-reference.md):

Run the /list-connections skill. Find the Excel Online (Business) connection in the output. If none exists, direct the user to create one using the environment-specific Connections URL — construct it from the active environment ID in context (from power.config.json or a prior step): https://make.powerapps.com/environments/<environment-id>/connections → + New connection → search for the connector → Create.

Excel Online is a tabular datasource -- requires -c (connection ID), -d (drive), and -t (table name in workbook):

# OneDrive workbook
npx power-apps add-data-source -a excelonlinebusiness -c <connection-id> -d 'me' -t 'Table1'

# SharePoint workbook -- dataset is the document library path
npx power-apps add-data-source -a excelonlinebusiness -c <connection-id> -d 'sites/your-site' -t 'Table1'


Run for each table the user needs.

Step 4: Configure

AddRowIntoTable -- adds a row to an Excel table:

// OneDrive workbook
await ExcelOnlineBusinessService.AddRowIntoTable({
  source: "me",
  drive: "me",
  file: "MyWorkbook.xlsx",
  table: "Table1",
  body: { column1: "value1", column2: "value2" } // Flat object, NO "items" wrapper
});

// SharePoint workbook
await ExcelOnlineBusinessService.AddRowIntoTable({
  source: "sites/your-site",
  drive: "drive-id",
  file: "SharedWorkbook.xlsx",
  table: "Table1",
  body: { column1: "value1", column2: "value2" }
});


Key points:

source: "me" and drive: "me" for OneDrive personal files
For SharePoint, use the site path and drive ID
The body is a flat key-value object matching column headers -- do NOT wrap in { items: ... }

Use Grep to find specific methods in src/generated/services/ExcelOnlineBusinessService.ts (generated files can be very large -- see connector-reference.md).

Step 5: Build
npm run build


Fix TypeScript errors before proceeding. Do NOT deploy yet.

Step 6: Update Memory Bank

Update memory-bank.md with: connector added, workbook/table configured, build status.

Weekly Installs
25
Repository
microsoft/power…m-skills
GitHub Stars
240
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass