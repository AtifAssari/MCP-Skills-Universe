---
rating: ⭐⭐⭐
title: frappe-syntax-reports
url: https://skills.sh/openaec-foundation/erpnext_anthropic_claude_development_skill_package/frappe-syntax-reports
---

# frappe-syntax-reports

skills/openaec-foundation/erpnext_anthropic_claude_development_skill_package/frappe-syntax-reports
frappe-syntax-reports
Installation
$ npx skills add https://github.com/openaec-foundation/erpnext_anthropic_claude_development_skill_package --skill frappe-syntax-reports
SKILL.md
Reports: Query, Script & Report Builder
Quick Reference
Report Types at a Glance
Type	Code Required	Use Case	Permission
Report Builder	None	Simple single-DocType listing with filters, group by	Any user
Query Report	SQL only	Direct SQL queries, legacy column format	System Manager
Script Report (Standard)	Python + JS	Complex logic, charts, summaries, trees	Administrator + Developer Mode
Script Report (Custom)	Python in UI	Quick custom reports without app deployment	System Manager
Script Report execute() Return Values
def execute(filters=None):
    columns = [...]   # List of dicts
    data = [...]      # List of dicts or lists
    message = "..."   # Optional: HTML message above report
    chart = {...}     # Optional: chart configuration
    report_summary = [...]  # Optional: summary cards
    skip_total_row = False  # Optional: suppress auto-total
    return columns, data, message, chart, report_summary, skip_total_row

Column Definition (Dict Format)
columns = [
    {
        "fieldname": "customer",
        "label": _("Customer"),
        "fieldtype": "Link",
        "options": "Customer",
        "width": 200
    },
    {
        "fieldname": "amount",
        "label": _("Amount"),
        "fieldtype": "Currency",
        "options": "currency",  # field in row holding currency code
        "width": 120
    }
]

Query Report Column Format (Legacy String)
SELECT
  name as "Sales Order:Link/Sales Order:200",
  customer as "Customer:Link/Customer:180",
  grand_total as "Total:Currency:120",
  transaction_date as "Date:Date:100"
FROM `tabSales Order`
WHERE docstatus = 1


Format: "Label:Fieldtype/Options:Width" — Options only needed for Link, Dynamic Link, Currency.

Filter Definition (JS)
frappe.query_reports["My Report"] = {
    filters: [
        {
            fieldname: "company",
            label: __("Company"),
            fieldtype: "Link",
            options: "Company",
            default: frappe.defaults.get_user_default("company"),
            reqd: 1
        },
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            default: frappe.datetime.add_months(frappe.datetime.get_today(), -1)
        },
        {
            fieldname: "status",
            label: __("Status"),
            fieldtype: "Select",
            options: "\nDraft\nSubmitted\nCancelled"
        }
    ]
};

Decision Tree: Which Report Type?
Need a report?
├─ Simple list/group of one DocType → Report Builder
│   (no code, UI-only, supports Group By with Count/Sum/Avg)
├─ Direct SQL query, no Python logic needed → Query Report
│   (SQL in Report doc, column format in aliases)
├─ Complex logic, calculations, charts → Script Report (Standard)
│   (Python .py + JS .js files, requires Developer Mode)
└─ Quick one-off with Python but no app deploy → Script Report (Custom)
    (Python in Report doc UI, System Manager can create)

Script Report returns what?
├─ Just data → return columns, data
├─ Data + chart → return columns, data, None, chart
├─ Data + summary → return columns, data, None, None, report_summary
├─ Data + message → return columns, data, message
└─ Everything → return columns, data, message, chart, report_summary, skip_total_row

Supported Fieldtypes for Columns
Fieldtype	Options Required	Notes
Data	No	Plain text
Link	DocType name	Clickable link to document
Dynamic Link	Fieldname holding DocType	Pair with a column containing DocType
Currency	Currency field or code	Fieldname in row that holds currency
Float	No	Decimal number
Int	No	Integer
Percent	No	Shows percentage bar
Date	No	Date display
Datetime	No	Date + time
Check	No	Boolean checkbox
Select	No	Dropdown value
Text	No	Long text
HTML	No	Raw HTML rendering
Supported Filter Fieldtypes
Fieldtype	Options	Behavior
Link	DocType name	Autocomplete from DocType
Select	Newline-separated values	Dropdown with fixed options
Date	—	Date picker
DateRange	—	Returns [from_date, to_date] list
Check	—	Boolean toggle
Dynamic Link	Fieldname of Link filter	Depends on another filter value
Data	—	Free text input
Int	—	Numeric input
MultiSelectList	DocType name	Multiple value selection
Chart Data Format
chart = {
    "data": {
        "labels": ["Jan", "Feb", "Mar", "Apr"],
        "datasets": [
            {"name": _("Revenue"), "values": [100, 200, 150, 300]},
            {"name": _("Expense"), "values": [80, 150, 120, 250]}
        ]
    },
    "type": "bar",        # bar, line, pie, donut, percentage
    "fieldtype": "Currency",
    "options": "currency",
    "currency": "USD",
    "colors": ["#5e64ff", "#ffa00a"]  # Optional custom colors
}

Report Summary Format
report_summary = [
    {
        "value": total_revenue,
        "label": _("Total Revenue"),
        "datatype": "Currency",
        "currency": "USD",
        "indicator": "Green"   # Green, Blue, Orange, Red
    },
    {
        "value": total_count,
        "label": _("Total Orders"),
        "datatype": "Int",
        "indicator": "Blue"
    }
]

Prepared Reports

For reports processing large datasets, enable Prepared Report to run asynchronously:

Set prepared_report = 1 in the Report document
User clicks "Generate New Report" — runs in background via enqueue()
Results stored in file; user downloads or views when ready
ALWAYS use for reports that query > 100k rows or take > 30 seconds
Number Cards
Source Type	Required Fields	How It Works
Document Type	document_type, function, aggregate_function_based_on	SQL aggregate on DocType
Report	report_name, report_field, function	Pulls value from a report column
Custom Method	method	Calls a whitelisted Python method

Custom method signature:

@frappe.whitelist()
def get_total_active_users(filters=None):
    return frappe.db.count("User", {"enabled": 1})

Dashboard Charts
Source	Configuration	Data Format
Report	Set chart_type = "Report", select report	Uses report's chart data
Custom	Set chart_type = "Custom", define source	Hook returns {"labels": [...], "datasets": [...]}
Group By	Set chart_type = "Group By", pick field	Auto-aggregates by field

Dashboard Chart Source hook in hooks.py:

dashboard_chart_source = [
    "myapp.dashboard_chart_source.get_chart_data"
]

Critical Rules
ALWAYS define columns as list of dicts with fieldname, label, fieldtype. The legacy string format is ONLY for Query Report SQL aliases.
NEVER return None for columns or data in execute() — ALWAYS return empty lists [].
ALWAYS use _(...) for translatable labels in columns and report_summary.
NEVER use frappe.db.sql with user-supplied filter values directly in f-strings — ALWAYS pass as parameters: frappe.db.sql(query, filters, as_dict=True).
ALWAYS set Reference DocType on the Report document — it controls user access permissions.
NEVER omit width in column definitions — columns without width render poorly.
ALWAYS match datasets[].values length to labels length in chart data — mismatched lengths cause chart rendering errors.
See Also
references/query-report.md — Complete Query Report API
references/script-report.md — Script Report JS API
references/examples.md — Working report examples
references/anti-patterns.md — Common report mistakes
references/dashboard.md — Number Cards, Dashboard Charts
Weekly Installs
26
Repository
openaec-foundat…_package
GitHub Stars
92
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass