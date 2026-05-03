---
title: frappe-impl-customapp
url: https://skills.sh/openaec-foundation/erpnext_anthropic_claude_development_skill_package/frappe-impl-customapp
---

# frappe-impl-customapp

skills/openaec-foundation/erpnext_anthropic_claude_development_skill_package/frappe-impl-customapp
frappe-impl-customapp
Installation
$ npx skills add https://github.com/openaec-foundation/erpnext_anthropic_claude_development_skill_package --skill frappe-impl-customapp
SKILL.md
Frappe Custom App - Implementation

Workflow for building a custom Frappe app from scratch. For exact syntax, see frappe-syntax-customapp.

Version: v14/v15/v16 compatible

Main Decision: Do You Need a Custom App?
WHAT CHANGES DO YOU NEED?
|
+-- Add fields to existing DocType?
|   +-- NO APP NEEDED: Custom Field + Property Setter
|
+-- Simple automation/validation (<50 lines)?
|   +-- NO APP NEEDED: Server Script or Client Script
|
+-- Complex business logic, new DocTypes, or Python code?
|   +-- YES: Create custom app
|
+-- Integration with external system (needs imports)?
|   +-- YES: Custom app REQUIRED (Server Scripts block imports)
|
+-- Custom reports with complex queries?
|   +-- Script Report (no app) vs Query Report (app optional)


Rule: ALWAYS start with the simplest solution. Server Scripts + Custom Fields solve 70% of needs without a custom app.

Step 1: Create App Structure
cd ~/frappe-bench
bench new-app my_app
# Prompts: Title, Description, Publisher, Email, License


ALWAYS verify immediately:

# my_app/my_app/__init__.py MUST have:
__version__ = "0.0.1"

Step 2: Configure pyproject.toml (v15+)
[build-system]
requires = ["flit_core >=3.4,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "my_app"
authors = [{ name = "Your Company", email = "dev@example.com" }]
description = "Your app description"
requires-python = ">=3.10"
readme = "README.md"
dynamic = ["version"]
dependencies = [
    "requests>=2.28.0"   # Only PyPI packages here
]

[tool.bench.frappe-dependencies]
frappe = ">=15.0.0,<16.0.0"
# erpnext = ">=15.0.0,<16.0.0"  # Only if needed


Rule: NEVER put frappe or erpnext in [project].dependencies -- they are NOT on PyPI.

Step 3: Configure hooks.py
app_name = "my_app"
app_title = "My App"
app_publisher = "Your Company"
app_description = "Description"
app_email = "dev@example.com"
app_license = "MIT"

required_apps = ["frappe"]  # Or ["frappe", "erpnext"]

fixtures = []  # Configured later


Rule: ALWAYS declare required_apps with all dependencies.

Step 4: Define Modules
# my_app/my_app/modules.txt
My App

App Size	Module Strategy
1-5 DocTypes	ONE module with app name
6-15 DocTypes	2-4 modules by functional area
15+ DocTypes	Modules by business domain

Rule: Each DocType belongs to EXACTLY one module. Module name in modules.txt maps to directory: My Custom App --> my_custom_app/.

Adding a Module
mkdir -p my_app/my_app/new_module/doctype
touch my_app/my_app/new_module/__init__.py
# Add "New Module" to modules.txt
bench --site mysite migrate

Step 5: Install and Create DocTypes
# Install app on site
bench --site mysite install-app my_app

# Create DocType (via UI recommended, or CLI)
bench --site mysite new-doctype "My Document" --module "My App"


This creates:

my_app/my_app/doctype/my_document/
+-- my_document.json    # DocType definition
+-- my_document.py      # Controller
+-- my_document.js      # Client script
+-- test_my_document.py # Tests

Step 6: Add Hooks
doc_events (v14/v15/v16)
doc_events = {
    "Sales Invoice": {
        "validate": "my_app.events.sales_invoice.validate",
        "on_submit": "my_app.events.sales_invoice.on_submit"
    }
}

extend_doctype_class (v16 ONLY -- preferred)
extend_doctype_class = {
    "Sales Invoice": "my_app.overrides.sales_invoice.CustomSalesInvoice"
}


Rule: ALWAYS call super().method() when overriding lifecycle methods in v16.

Scheduler Events
scheduler_events = {
    "daily": ["my_app.tasks.daily_cleanup"],
    "cron": {"0 9 * * 1-5": ["my_app.tasks.morning_report"]}
}


See frappe-impl-hooks and frappe-impl-scheduler for complete patterns.

Step 7: Add Patches
Create Patch File
mkdir -p my_app/my_app/patches/v1_0
touch my_app/my_app/patches/__init__.py
touch my_app/my_app/patches/v1_0/__init__.py

# my_app/my_app/patches/v1_0/populate_defaults.py
import frappe

def execute():
    if not frappe.db.has_column("My DocType", "target_field"):
        return  # Skip if not applicable

    batch_size = 1000
    offset = 0
    while True:
        records = frappe.get_all("My DocType",
            limit_page_length=batch_size, limit_start=offset)
        if not records:
            break
        for r in records:
            frappe.db.set_value("My DocType", r.name,
                "target_field", "default", update_modified=False)
        frappe.db.commit()
        offset += batch_size

Register in patches.txt
[pre_model_sync]
# Patches that run BEFORE schema changes (backup data from deleted fields)

[post_model_sync]
# Patches that run AFTER schema changes (populate new fields)
my_app.patches.v1_0.populate_defaults


Rules:

ALWAYS check if patch is needed (guard clause)
ALWAYS batch process 1000+ records
ALWAYS commit after each batch
NEVER run untested patches on production
Step 8: Fixtures Management
Configure in hooks.py
fixtures = [
    {"dt": "Custom Field", "filters": [["module", "=", "My App"]]},
    {"dt": "Property Setter", "filters": [["module", "=", "My App"]]},
    {"dt": "Role", "filters": [["name", "in", ["My App User", "My App Manager"]]]},
    {"dt": "Workflow", "filters": [["document_type", "=", "My DocType"]]},
    "My Category",  # All records of your own config DocType
]

Export and Verify
bench --site mysite export-fixtures --app my_app
ls my_app/my_app/fixtures/
# custom_field.json, property_setter.json, etc.


Rules:

ALWAYS filter fixtures to YOUR app's customizations
NEVER include transactional data (invoices, orders)
NEVER export without filters for shared DocTypes (Custom Field, Workflow)
Fixtures auto-import during bench migrate
Step 9: Development Workflow
Essential Commands
# After schema changes (DocType fields, hooks.py, patches)
bench --site mysite migrate

# After JS/CSS changes
bench build --app my_app

# After Python changes (controllers, events)
bench --site mysite clear-cache

# Full restart (production)
bench restart

# Watch mode (development)
bench watch  # Auto-rebuilds on file changes

Development Cycle
1. Edit code/DocType
2. bench --site mysite migrate (if schema changed)
3. bench build --app my_app (if JS/CSS changed)
4. bench --site mysite clear-cache (if Python changed)
5. Test in browser
6. Repeat

Step 10: Testing the App
# Run all tests
bench --site mysite run-tests --app my_app

# Run specific test
bench --site mysite run-tests --module my_app.my_module.doctype.my_doctype.test_my_doctype

# Run with verbose output
bench --site mysite run-tests --app my_app -v


See frappe-testing-unit for writing test cases.

Step 11: Packaging for Distribution
Via Git (standard method)
cd apps/my_app
git init && git add . && git commit -m "Initial commit"
git remote add origin https://github.com/org/my_app.git
git push -u origin main

Install on Another Site
# On target bench
bench get-app https://github.com/org/my_app.git
bench --site target-site install-app my_app
bench --site target-site migrate

Version Management
# my_app/my_app/__init__.py
__version__ = "1.0.0"  # Semantic versioning: MAJOR.MINOR.PATCH

Change Type	Version Bump	Example
Breaking changes	MAJOR	1.x -> 2.0.0
New features	MINOR	1.1.x -> 1.2.0
Bug fixes	PATCH	1.2.0 -> 1.2.1
Step 12: App Dependencies
Frappe/ERPNext Dependencies
# hooks.py
required_apps = ["frappe", "erpnext"]  # Install order matters

# pyproject.toml
[tool.bench.frappe-dependencies]
frappe = ">=15.0.0,<16.0.0"
erpnext = ">=15.0.0,<16.0.0"

Python Package Dependencies
[project]
dependencies = ["requests>=2.28.0", "pandas>=1.5.0"]


Rule: NEVER create circular dependencies between apps.

Version-Specific Considerations
Aspect	v14	v15	v16
Build config	setup.py	pyproject.toml	pyproject.toml
DocType extension	doc_events	doc_events	extend_doctype_class preferred
Python minimum	3.10	3.10	3.11
Patch format	INI sections	INI sections	INI sections
v16 Breaking Changes to Know
extend_doctype_class hook: Cleaner extension via mixins
Data masking: Field-level privacy configuration
UUID naming: New naming rule option
Chrome PDF: wkhtmltopdf deprecated
Critical Rules Summary
ALWAYS
Start with bench new-app - NEVER create structure manually
Define __version__ in __init__.py
Use dynamic = ["version"] in pyproject.toml
Test patches on database copy before production
Filter fixtures to your app's customizations only
Version your patches (v1_0, v2_0 directories)
Test installation on a fresh site
NEVER
Put frappe/erpnext in [project].dependencies
Include transactional data in fixtures
Hardcode site-specific values (use settings DocTypes)
Skip frappe.db.commit() in large patches
Delete fields without backup patch
Modify core ERPNext files directly
Reference Files
File	Contents
workflows.md	8 step-by-step implementation guides
decision-tree.md	Complete decision flowcharts
examples.md	5 complete working app examples
anti-patterns.md	Common mistakes to avoid
See Also
frappe-syntax-customapp - Exact syntax reference
frappe-syntax-hooks - Hooks configuration syntax
frappe-impl-hooks - Hook implementation patterns
frappe-core-database - Database operations for patches
frappe-impl-scheduler - Scheduled task implementation
frappe-ops-bench - Bench commands reference
frappe-ops-app-lifecycle - App versioning and release management
frappe-testing-unit - Writing tests for your app
frappe-testing-cicd - CI/CD pipeline for app testing
Weekly Installs
27
Repository
openaec-foundat…_package
GitHub Stars
92
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn