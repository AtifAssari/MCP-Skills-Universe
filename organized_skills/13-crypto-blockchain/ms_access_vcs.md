---
rating: ⭐⭐
title: ms-access-vcs
url: https://skills.sh/paramountsoftware/ms-access-ai-skill/ms-access-vcs
---

# ms-access-vcs

skills/paramountsoftware/ms-access-ai-skill/ms-access-vcs
ms-access-vcs
Installation
$ npx skills add https://github.com/paramountsoftware/ms-access-ai-skill --skill ms-access-vcs
SKILL.md
Microsoft Access VCS Project Guide

Rules and gotchas for programmatically editing Access objects exported by VCS 4.x. Violations cause silent corruption or Error 2128 on import via LoadComponentFromText.

Reference Files

Read the relevant reference file before working on a specific object type:

When working on...	Read this reference
Form .bas layout or form controls	references/forms.md
Report .bas layout, sections, or sorting/grouping	references/reports.md
Images in forms or reports (add, replace, convert from OLE)	references/images.md
Conditional formatting (forms or reports)	references/conditional-formatting.md
Queries (.bas + .sql)	references/queries.md
Tables, relationships, or ODBC connections	references/tables-and-relationships.md
VBA modules (.bas) or code-behind (.cls)	references/vba.md
Project config files (vcs-options, vcs-index, etc.)	references/project-config.md
Macros, shared images, or import/export specs	references/other-objects.md
Project Overview

A VCS-exported Access project lives in <DatabaseName>.accdb.src/. The directory name must match the .accdb filename with .src appended.

File Pairing Rules
Object Type	Files	Notes
Form	.bas + optional .cls + optional .json	.bas = layout, .cls = VBA code-behind (omitted if no code), .json = print settings
Report	.bas + optional .cls + optional .json	Same binary text format as forms, .cls = VBA code-behind (uncommon but valid), .json = print settings
Query	.bas + .sql	.bas = metadata/designer state, .sql = SQL text. Always paired
Module	.bas	Standard VBA module
Relationship	.json	Foreign key definition, join type, referential integrity
Linked Table	.json	Connection string, source table, attributes
Local Table	.xml	XSD schema defining columns, data types, indexes. For tables stored inside the .accdb
Macro	.bas	Access macro actions (not VBA). Simpler binary text format
Shared Image	.json + image file	.json = metadata (name, extension, hash), paired with actual image file (.png, .jpg, etc.)
Import/Export Spec	.json	Column definitions, delimiters, data types
Theme	.thmx	Office theme (binary OOXML archive — do not edit)

When deleting an object, delete ALL its associated files plus its entry in vcs-index.json.

Encoding

All JSON configuration files and .sql files use UTF-8 with BOM (byte order mark EF BB BF). The BOM must be preserved when editing. Binary text .bas files (forms, reports, macros) also use UTF-8 with BOM.

Safe Deletion Checklist

Before deleting any Access object:

Search for references in all .cls, .bas, .sql files. Objects may be referenced by:
VBA code (DoCmd.OpenForm, DoCmd.OpenReport, DoCmd.OutputTo)
Query SQL (FROM tableName, subreport SourceObject)
Form RecordSource properties
DLookup expressions
Check for name collisions. Objects with similar names may serve completely different purposes (e.g., rInvoice_EXTERNALSYSTEM = active invoice report vs EXTERNALSYSTEM_Accounts = dead integration table).
Delete all paired files (.bas + .sql, .bas + .cls + .json, etc.)
Remove from config files: vcs-index.json, db-connection.json, hidden-attributes.json
Renumber TabIndex values in any form/report section where a control was removed
Test import in Access after changes
Common Pitfalls
Commented-out code referencing kept objects: Leave commented VBA lines alone if they reference objects you're keeping.
db-connection.json: Must contain only one connection entry matching the canonical ODBC connection string used by all linked tables and pass-through queries. Never introduce plaintext passwords or user-specific credentials.
Weekly Installs
11
Repository
paramountsoftwa…ai-skill
GitHub Stars
9
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass