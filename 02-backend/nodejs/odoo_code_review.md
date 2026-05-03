---
title: odoo-code-review
url: https://skills.sh/nguyenhuy158/skills/odoo-code-review
---

# odoo-code-review

skills/nguyenhuy158/skills/odoo-code-review
odoo-code-review
Installation
$ npx skills add https://github.com/nguyenhuy158/skills --skill odoo-code-review
SKILL.md
Odoo Code Reviewer
Python Guidelines
General
PEP8: Strictly follow PEP8 (120 chars line length is often acceptable in Odoo).
Imports:
odoo imports first.
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
ORM Methods
Search: Use search_count() instead of len(search()).
Filtered: Use filtered() for in-memory filtering of recordsets.
Mapped: Use mapped() to extract values.
Write/Create: Batch operations where possible.
SQL: Avoid direct SQL (self.env.cr.execute) unless absolutely necessary for performance. If used, never inject variables directly; use parameters.
Fields & Models
Naming:
Fields: snake_case. Many2one fields usually end with _id (e.g., partner_id).
One2many/Many2many: usually plural (e.g., line_ids, tag_ids).
Computed Fields: Always add @api.depends.
Constrains: Use @api.constrains for data integrity checks.
Translations: Wrap user-facing strings in _().
XML Guidelines
Views
Records: Use <record id="..." model="ir.ui.view">.
Arch: All views must have an <arch type="xml"> block.
XPath: Use concise XPath expressions. Prefer name attributes over indices.
Bad: //field[3]
Good: //field[@name='description']
Attributes:
invisible: Use strictly for hiding.
readonly: For uneditable fields.
required: For mandatory fields.
Noids: Avoid hardcoded database IDs. Use ref="module.xml_id".
Data Files
NoUpdate: Use noupdate="1" in <data> for data that shouldn't be reset on upgrade (like sequence numbers or cron jobs).
Manifest (manifest.py)
Ensure depends lists all required modules.
Ensure data lists all XML/CSV files in correct order (security -> views -> data).
Ensure license is specified (e.g., LGPL-3).
Review Checklist
Security: Are access rights (ir.model.access.csv) defined?
Performance: Are there loops doing SQL queries inside? (N+1 problem).
Upgrade: Will this code break on module update?
Idempotency: Can this XML be loaded multiple times without duplicating data?
Weekly Installs
44
Repository
nguyenhuy158/skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass