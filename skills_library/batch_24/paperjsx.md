---
title: paperjsx
url: https://skills.sh/composiohq/awesome-codex-skills/paperjsx
---

# paperjsx

skills/composiohq/awesome-codex-skills/paperjsx
paperjsx
Installation
$ npx skills add https://github.com/composiohq/awesome-codex-skills --skill paperjsx
SKILL.md
PaperJSX Document Generation

Generate professional documents from JSON layout specs. PaperJSX is generation-only — it creates new files, it does not edit existing ones.

Triggers

Use this skill when the user asks to:

Create a presentation or generate slides
Make a PPTX or PowerPoint file
Create a Word document or DOCX
Generate an Excel spreadsheet with charts
Create a JSON to PPTX, JSON to DOCX, or JSON to XLSX file
Generate a PDF invoice, report, or chart document
Install

Install the format-appropriate package:

# Presentations
npm install @paperjsx/json-to-pptx

# Word documents
npm install @paperjsx/json-to-docx

# Spreadsheets
npm install @paperjsx/json-to-xlsx

# PDF documents
npm install @paperjsx/json-to-pdf

How it works
Build a JSON layout spec matching the schema in references/json-schema.md
Write a Node.js script that passes the JSON to the PaperJSX engine
Run the script to generate the output file
Validate the output file exists and is non-zero bytes

Do not write imperative PaperJSX API code. The execution model is always: JSON spec in, document file out.

Example: PPTX generation
import { PaperEngine } from "@paperjsx/json-to-pptx";
import fs from "node:fs";

const spec = {
  type: "Document",
  meta: { title: "Q4 Review" },
  slides: [
    {
      type: "Slide",
      children: [
        { type: "Text", content: "Q4 2025 Business Review", style: { fontSize: 36, bold: true } }
      ]
    }
  ]
};

const buffer = await PaperEngine.render(spec);
fs.writeFileSync("presentation.pptx", buffer);
console.log("Generated presentation.pptx");

Example: DOCX generation
import { renderToDocx } from "@paperjsx/json-to-docx";
import fs from "node:fs";

const result = await renderToDocx({
  type: "DocxDocument",
  pageSize: "a4",
  orientation: "portrait",
  pages: [
    {
      elements: [
        { type: "heading", level: 1, text: "Quarterly Report" },
        { type: "paragraph", text: "Section content here." }
      ]
    }
  ]
});

fs.writeFileSync("report.docx", result.buffer);
console.log("Generated report.docx");

Example: XLSX generation
import { SpreadsheetEngine } from "@paperjsx/json-to-xlsx";
import fs from "node:fs";

const spec = {
  meta: { title: "Revenue Data", creator: "PaperJSX" },
  sheets: [{
    name: "Revenue",
    rows: [
      { cells: [{ value: "Quarter" }, { value: "Revenue" }] },
      { cells: [{ value: "Q1 2026" }, { value: 420000 }] },
      { cells: [{ value: "Q2 2026" }, { value: 510000 }] }
    ]
  }]
};

const buffer = await SpreadsheetEngine.render(spec);
fs.writeFileSync("revenue.xlsx", buffer);
console.log("Generated revenue.xlsx");

Validation

After generating any file, always verify:

import fs from "node:fs";

const stats = fs.statSync("output.pptx");
if (stats.size === 0) {
  throw new Error("Generated file is empty");
}
console.log(`Output file: ${stats.size} bytes`);


If the engine throws an error, surface the full error message to the user.

Schema reference

See references/json-schema.md for the complete JSON layout spec schema for all supported formats.

Weekly Installs
15
Repository
composiohq/awes…x-skills
GitHub Stars
5.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass