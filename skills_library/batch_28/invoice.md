---
title: invoice
url: https://skills.sh/nexu-io/open-design/invoice
---

# invoice

skills/nexu-io/open-design/invoice
invoice
Installation
$ npx skills add https://github.com/nexu-io/open-design --skill invoice
SKILL.md
Invoice Skill

Produce a single-page printable invoice.

Workflow
Read DESIGN.md.
Layout:
Top band: studio brand on the left, "INVOICE" + number + date + due date on the right.
Two columns: From (sender) / Bill to (recipient) with addresses.
Project ref + payment-terms strip.
Line items table: description / qty / unit / amount.
Right-aligned totals block: subtotal, retainer, tax, total due.
Payment instructions (bank, wire, ACH).
Thank-you note + signature line.
Print stylesheet @media print to remove backgrounds.
Output contract
<artifact identifier="invoice-name" type="text/html" title="Invoice">
<!doctype html>...</artifact>

Weekly Installs
68
Repository
nexu-io/open-design
GitHub Stars
14.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass