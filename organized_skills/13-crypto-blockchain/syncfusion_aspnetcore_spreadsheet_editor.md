---
rating: ⭐⭐⭐
title: syncfusion-aspnetcore-spreadsheet-editor
url: https://skills.sh/syncfusion/spreadsheet-editor-sdk-skills/syncfusion-aspnetcore-spreadsheet-editor
---

# syncfusion-aspnetcore-spreadsheet-editor

skills/syncfusion/spreadsheet-editor-sdk-skills/syncfusion-aspnetcore-spreadsheet-editor
syncfusion-aspnetcore-spreadsheet-editor
Installation
$ npx skills add https://github.com/syncfusion/spreadsheet-editor-sdk-skills --skill syncfusion-aspnetcore-spreadsheet-editor
SKILL.md
Syncfusion ASP.NET Core Spreadsheet Editor
Overview

This skill helps developers generate ASP.NET Core (cshtml) code for integrating the Syncfusion Spreadsheet Editor into their applications. It provides ready-to-use code snippets, API guidance, and best practices for building Excel-like functionality in ASP.NET Core projects.

Key Capabilities
File Operations: Import/export Excel files (xlsx, xls, xlsb), CSV files, and PDF export
Data Management: Data binding, editing, sorting, filtering, and validation
Cell Operations: Formatting (fonts, colors, borders, alignment), merge cells, wrap text
Formulas & Calculations: Built-in Excel formulas, custom functions, named ranges
Collaboration: Notes, comments, and threaded discussions
Advanced Features: Charts, images, hyperlinks, conditional formatting, freeze panes, sheet protection, virtualization for large datasets
Quick Start Examples
Example 1: Generate Spreadsheet with Formatting

User: "Create a Spreadsheet with data and apply cell styles"

Result: A ASP.NET Core (cshtml) code snippet is generated that loads provide data into the Spreadsheet and applies basic cell formatting.

Example 2: Generate Code for Loading a File

User: "Create a Spreadsheet and load an Excel file initially"

Result: A ASP.NET Core (cshtml) code snippet is generated that initializes the Spreadsheet and programmatically opens an Excel file on startup.

Getting Started — Minimal ASP.NET Core Code

Minimal ASP.NET Core Spreadsheet setup for a plain ASP.NET Core project:

Controller (HomeController.cs):

using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Syncfusion.EJ2.Spreadsheet;

namespace YourApp.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Open(IFormCollection openRequest)
        {
            OpenRequest open = new OpenRequest();
            open.File = openRequest.Files[0];
            return Content(Workbook.Open(open));
        }
 
        public IActionResult Save(SaveSettings saveSettings)
        {
            if (saveSettings != null && saveSettings.JSONData != null)
            {
                return Workbook.Save(saveSettings);
            }
            return View();
        }
 
    }
}


View (Index.cshtml):

@using Syncfusion.EJ2.Spreadsheet

<div class="control-pane">
    <div class="control-section spreadsheet-control">
        <ejs-spreadsheet id="spreadsheet" openUrl="Home/Open" saveUrl="Home/Save">
            <e-spreadsheet-sheets>
                <e-spreadsheet-sheet name="Sheet1">
                    <e-spreadsheet-rows>
                        <e-spreadsheet-row>
                            <e-spreadsheet-cells>
                                <e-spreadsheet-cell value="Hello, Spreadsheet!"></e-spreadsheet-cell>
                            </e-spreadsheet-cells>
                        </e-spreadsheet-row>
                    </e-spreadsheet-rows>
                </e-spreadsheet-sheet>
            </e-spreadsheet-sheets>
        </ejs-spreadsheet>
    </div>
</div>


Generate ASP.NET Core (cshtml) Code for the User's Project

Trigger keywords: "aspnet-core spreadsheet", "spreadsheet editor", "syncfusion spreadsheet", "excel component", "load excel file", "open excel file", "import excel", "export excel file", "save excel", "export to pdf", "export to csv", "view excel", "configure spreadsheet", "create spreadsheet", "add spreadsheet", "spreadsheet data", "cell formatting", "apply formulas", "insert chart", "data binding", "spreadsheet validation", "freeze panes", "protect sheet"

Workflow:

Identify the requested Spreadsheet feature (data binding, formulas, charts, export, etc.).

Read the relevant references/*.md file(s) to understand the APIs and code patterns for the requested feature.

STOP before generating code. Check if the user has already chosen a delivery mode.

If no delivery mode is chosen yet, you MUST ask the user first using this concise multiple-choice question:

"How would you like to receive the generated Spreadsheet code?"

Option 1: Replace the code in a specific project file (you'll need to provide the file path and confirm)
Option 2: Save the code in this skill's output folder at {skill-root}/syncfusion-aspnetcore-spreadsheet-editor/output/index.cshtml
Option 3: Share the code directly in the chat window

Only after the user selects a delivery mode, proceed to generate ASP.NET Core(cshtml) code using the APIs and snippets from references/*.md, substituting concrete placeholders from the user's project.

Do NOT make changes to workspace project files unless the user explicitly chose Option 1 and provided the file path with permission.

Provide complete ASP.NET Core snippets and concise integration steps after delivering the code.

Refer to ## Rules section for operational constraints (output directory, temporary files, allowed libraries, etc.)

Code References

All code snippets and examples are in the references/ folder. Each file contains:

Minimal ASP.NET Core(cshtml) Code — a working, ready-to-use snippet
Placeholders — values the user must customize
Notes — ASP.NET Core best practices and constraints
File	Topic
initialization.md	Basic ASP.NET Core setup and options
data-binding.md	Local arrays, JSON, remote (DataManager)
formulas.md	Formulas, aggregates, named ranges
formatting.md	Cell formatting, borders, wrap text
number-formatting.md	Number formatting, decimals, currency, date
conditional-formatting.md	Rules, highlights based on conditions
data-validation.md	Validation rules, invalid highlights
sorting-filtering.md	Sorting, filtering
find-replace.md	Find, replace
import-export.md	Save (XLSX/CSV/PDF), open, openFromJson
charts.md	Insert, edit, delete charts
images.md	Insert, modify pictures
hyperlink.md	Add, remove hyperlinks
comments.md	Threaded comments, replies, resolve threads
notes.md	Simple cell notes, sticky visibility, add/edit/delete
protection.md	Sheet protection, cell locking, permissions
edit-cell.md	startEdit, endEdit, updateCell, edit modes
freeze-panes.md	Freeze rows/columns, split panes
row-column.md	Insert, delete, resize rows/columns, hide
merge-cells.md	Merge, unmerge cells, spanning
print.md	Page setup, headers/footers, scaling, margins
misc-operations.md	Autofill, clear, sheet management, goTo
clipboard.md	Copy, cut, paste with different paste types
selection.md	Select cells/ranges, multi-select, getSelectedRange
scrolling-virtualization.md	Virtual scrolling, large datasets, performance
wrap.md	Text wrapping, multi-line display, row height
defined-names.md	Named ranges, define names, refersTo format
custom-functions.md	Custom calculation functions, addCustomFunction
ribbon-customization.md	Ribbon tabs, toolbar items, file menu customization
context-menu.md	Right-click context menu, contextMenuBeforeOpen
localization.md	Multi-language, locale, RTL, number/date formats
events.md	Event handling, event properties, event patterns
autofill.md	Autofill patterns, fill types, series
Key Rules for Code Generation (ASP.NET Core (cshtml)-first)

ASP.NET Core (cshtml)-first snippets — All examples and snippets must be written in ASP.NET Core cshtml and compile with the current npm package. If the user asks for providing ASP.NET Core cshtml, provide ASP.NET Core cshtml codes.

No inline code in this manifest — Refer to references/*.md for runnable snippets; keep this file as the concise policy and index.

Reference file requirements — Each reference must include:

Minimal ASP.NET Core (cshtml) Code (complete, runnable)
Placeholders (clearly marked values to replace)
Notes (ASP.NET Core integration steps and best practices)

License handling — Do not hardcode license keys; refer users to env variables or project config.

Preserve data integrity — Preserve existing formulas, references, and formatting when generating or editing sheets.

No hallucinated APIs — Use verified Syncfusion Spreadsheet Editor method names only.

Read references first — For any requested feature, always read the relevant references/*.md file(s) first before generating code.

Build strictly from references — Build ASP.NET Core code strictly from the APIs, methods, properties, events, and snippets found in the reference files. Do NOT invent, guess, or suggest any API, method, property, or event not explicitly present in the reference files.

Rules
Output files must go in {skill-root}/syncfusion-aspnetcore-spreadsheet-editor/output/ directory when user selects Option 2
Only use Syncfusion Spreadsheet APIs — never recommend or use alternative spreadsheet libraries (e.g., aspnet-core-spreadsheet, handsontable, ag-grid)
No temporary files — never create temporary scripts, intermediate files, or scaffolding outside the output directory
ASP.NET Core-only code — all generated code must be valid ASP.NET Core (cshtml), never generate vanilla JavaScript, jQuery, or non-ASP.NET Core patterns
Security
Docs-only: This skill contains only documentation and reference snippets — no bundled runtime code. Treat this as documentation unless runtime files are explicitly added.
Official assets only: Examples may reference Syncfusion official domains (syncfusion.com, ej2.syncfusion.com, document.syncfusion.com). For production, prefer pinned NuGet packages (Syncfusion.EJ2.AspNet.Core) or validated CDN artifacts with Subresource Integrity (SRI) and vendor approval.
Data exfiltration: Remote endpoint examples use placeholders. Never send sensitive data to sample/demo endpoints - use mocked or local endpoints for samples.
Untrusted input: Examples advise validating and whitelisting user-supplied URLs, sanitizing uploads, and encoding output before rendering.
Weekly Installs
45
Repository
syncfusion/spre…k-skills
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass