---
rating: ⭐⭐⭐
title: recipe-generate-report-from-sheet
url: https://skills.sh/googleworkspace/cli/recipe-generate-report-from-sheet
---

# recipe-generate-report-from-sheet

skills/googleworkspace/cli/recipe-generate-report-from-sheet
recipe-generate-report-from-sheet
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-generate-report-from-sheet
Summary

Extract Google Sheet data and generate a formatted Google Docs report with sharing.

Requires three Google Workspace skills: gws-sheets for data reading, gws-docs for document creation and formatting, and gws-drive for permission management
Workflow chains four operations: read sheet ranges, create a new Doc, write formatted content with headers and sections, and share with specified stakeholders
Supports markdown-style formatting in the report output and role-based access control for sharing
SKILL.md
Generate a Google Docs Report from Sheet Data

PREREQUISITE: Load the following skills to execute this recipe: gws-sheets, gws-docs, gws-drive

Read data from a Google Sheet and create a formatted Google Docs report.

Steps
Read the data: gws sheets +read --spreadsheet SHEET_ID --range "Sales!A1:D"
Create the report doc: gws docs documents create --json '{"title": "Sales Report - January 2025"}'
Write the report: `gws docs +write --document-id DOC_ID --text '## Sales Report - January 2025
Summary

Total deals: 45 Revenue: $125,000

Top Deals
Acme Corp - $25,000
Widget Inc - $18,000'`
Share with stakeholders: gws drive permissions create --params '{"fileId": "DOC_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "cfo@company.com"}'
Weekly Installs
11.5K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass