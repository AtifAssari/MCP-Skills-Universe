---
title: frappe-ops-app-lifecycle
url: https://skills.sh/openaec-foundation/erpnext_anthropic_claude_development_skill_package/frappe-ops-app-lifecycle
---

# frappe-ops-app-lifecycle

skills/openaec-foundation/erpnext_anthropic_claude_development_skill_package/frappe-ops-app-lifecycle
frappe-ops-app-lifecycle
Installation
$ npx skills add https://github.com/openaec-foundation/erpnext_anthropic_claude_development_skill_package --skill frappe-ops-app-lifecycle
SKILL.md
App Lifecycle Management
Quick Reference
Command	Purpose	When to Use
bench new-app	Scaffold new app	Starting a new project
bench get-app URL	Clone from Git	Installing existing app
bench --site SITE install-app	Install on site	After get-app or new-app
bench --site SITE remove-app	Uninstall from site	Removing app from site
bench remove-app	Remove from bench	Removing app entirely
bench --site SITE migrate	Run patches + sync	After code changes
bench build	Compile assets	After JS/CSS changes
bench --site SITE console	Python REPL	Debugging
bench start	Start dev server	Development
bench setup production	Configure nginx+supervisor	Deploying to production
1. Scaffolding: bench new-app
bench new-app my_custom_app


Interactive prompts:

App Title → Human-readable name
App Description → One-line summary
App Publisher → Company/author name
App Email → Contact email
App Icon → Default: octicon octicon-file-directory
App Color → Default: grey
App License → Default: MIT
Generated Directory Structure
apps/my_custom_app/
├── MANIFEST.in              # Files included in Python package
├── README.md                # Project readme
├── license.txt              # License file
├── requirements.txt         # Python dependencies
├── dev-requirements.txt     # Dev-only Python deps (v15+)
├── package.json             # Node.js dependencies
├── setup.py                 # Python package config (v14)
├── pyproject.toml           # Python package config (v15+)
├── my_custom_app/
│   ├── __init__.py          # App version string
│   ├── hooks.py             # Framework integration hooks
│   ├── modules.txt          # List of app modules
│   ├── patches.txt          # Migration patches list
│   ├── config/
│   │   ├── __init__.py
│   │   ├── desktop.py       # Desktop/workspace config
│   │   └── docs.py          # Documentation config
│   ├── public/              # Static assets → /assets/my_custom_app/
│   │   ├── css/
│   │   └── js/
│   ├── templates/           # Jinja templates
│   └── www/                 # Portal pages (URL = path)

What Each Core File Does
File	Purpose	NEVER Forget
__init__.py	Defines __version__	ALWAYS update before release
hooks.py	ALL framework integration	Entry point for everything
modules.txt	Declares app modules	ALWAYS add new modules here
patches.txt	Migration patch registry	ALWAYS add patches in order
requirements.txt	Python deps installed on setup	Add pip packages here
public/	Static files served by nginx	Accessible at /assets/app_name/
www/	Portal pages	Filename = URL path
2. Development Cycle
Code → Migrate → Build → Test → Commit

Step-by-Step
# 1. Make code changes (DocTypes, reports, APIs, etc.)

# 2. Migrate — sync DocType schema + run patches
bench --site mysite migrate

# 3. Build — compile JS/CSS assets
bench build --app my_custom_app

# 4. Test — run Python tests
bench --site mysite run-tests --app my_custom_app

# 5. Commit
git -C apps/my_custom_app add -A && git -C apps/my_custom_app commit -m "feat: add feature"


ALWAYS run bench migrate after modifying DocType JSON files. ALWAYS run bench build after modifying JS/CSS files.

3. Getting Apps from Git
# Public repo
bench get-app https://github.com/org/my_app

# Specific branch
bench get-app https://github.com/org/my_app --branch develop

# Private repo via SSH
bench get-app git@github.com:org/private_app.git

# Private repo via token (v15+)
bench get-app https://TOKEN@github.com/org/private_app.git


After get-app, ALWAYS install on the target site:

bench --site mysite install-app my_app


get-app clones to apps/ and adds to apps.txt. install-app creates database tables and runs after_install hooks.

4. Installing and Removing Apps
Installation Order Matters

Apps are installed in order listed in apps.txt. If App B depends on App A, App A MUST be listed first.

# Install
bench --site mysite install-app my_app

# Verify
bench --site mysite list-apps
# Output: frappe, erpnext, my_app

# Remove from site (keeps code in apps/)
bench --site mysite remove-app my_app

# Remove from bench entirely (deletes code)
bench remove-app my_app

App Dependencies (v14+)

Declare in hooks.py:

required_apps = ["frappe", "erpnext"]


Frappe ALWAYS checks required_apps during installation and blocks if dependencies are missing.

5. Debugging with bench console
bench --site mysite console


Opens an IPython REPL with Frappe context:

# Query data
frappe.db.sql("SELECT name, status FROM `tabSales Invoice` LIMIT 5", as_dict=True)

# Get a document
doc = frappe.get_doc("Sales Invoice", "SINV-00001")
print(doc.grand_total)

# Test a whitelisted method
from my_app.api import my_function
result = my_function(param="value")

# Check configuration
frappe.get_site_config()

# Auto-reload on code changes (v15+)
# Start with: bench --site mysite console --autoreload


ALWAYS use bench console for debugging — NEVER modify production data with raw SQL.

6. Development Mode vs Production Mode
Development Mode
# Enable
bench set-config -g developer_mode 1

# Start dev server (Procfile: web + worker + redis + socketio)
bench start


Development mode enables:

DocType editing in Desk
"Is Standard" option for reports/scripts
Auto-reload on Python file changes
Detailed error tracebacks in browser
dev-requirements.txt dependencies installed
Production Mode
# Disable developer mode
bench set-config -g developer_mode 0

# Setup production (nginx + supervisor)
sudo bench setup production USERNAME

# Restart
sudo supervisorctl restart all
# or
sudo systemctl restart supervisor


Production mode:

Serves via nginx (port 80/443)
Background workers via supervisor
Static files served directly by nginx
Errors logged to files, not browser
NEVER enable developer_mode on production sites
7. Asset Building
v15+ (esbuild)
# Build all apps
bench build

# Build specific app
bench build --app my_custom_app

# Watch mode (auto-rebuild on changes)
bench watch

v14 (build.json)

v14 uses build.json in the app root to map source files to bundles:

{
    "css/my_app.css": [
        "public/css/style.css"
    ],
    "js/my_app.js": [
        "public/js/main.js"
    ]
}

Asset Include in hooks.py
# Desk (backend UI)
app_include_js = "my_app.bundle.js"      # v15+ bundle syntax
app_include_css = "my_app.bundle.css"

# Portal (website)
web_include_js = "my_app_web.bundle.js"
web_include_css = "my_app_web.bundle.css"

# v14 legacy syntax
app_include_js = "/assets/my_app/js/my_app.js"
app_include_css = "/assets/my_app/css/my_app.css"


ALWAYS run bench build after changing JS/CSS files. ALWAYS run bench clear-cache if assets are not updating.

8. App Versioning
Version String in init.py
# my_custom_app/__init__.py
__version__ = "1.2.0"


ALWAYS use semantic versioning: MAJOR.MINOR.PATCH

MAJOR: Breaking changes
MINOR: New features (backward compatible)
PATCH: Bug fixes

The version is read by bench version, displayed in Desk, and used by the Marketplace.

Checking Versions
bench version
# frappe 15.23.0
# erpnext 15.18.0
# my_custom_app 1.2.0

9. Patches: Data Migrations
Writing a Patch
# my_app/patches/v1_2/update_customer_status.py
import frappe

def execute():
    frappe.reload_doc("module_name", "doctype", "customer_extension")

    frappe.db.sql("""
        UPDATE `tabCustomer Extension`
        SET status = 'Active'
        WHERE status IS NULL
    """)
    frappe.db.commit()

Registering in patches.txt
# patches.txt — v14+ supports sections

[pre_model_sync]
my_app.patches.v1_1.fix_old_data
my_app.patches.v1_2.rename_field_before_schema

[post_model_sync]
my_app.patches.v1_2.update_customer_status
my_app.patches.v1_2.migrate_settings


Section timing (v14+):

[pre_model_sync] — Runs BEFORE DocType schema changes are applied
[post_model_sync] — Runs AFTER schema changes (new fields available)
No section header — Runs in [pre_model_sync] by default
Patch Rules
ALWAYS add new patches at the END of their section
Patches run ONCE — tracked in tabPatch Log
To re-run a patch, append a comment: my_app.patches.v1_2.fix #2025-03-20
ALWAYS call frappe.reload_doc() before accessing new/modified DocTypes
ALWAYS use [post_model_sync] for patches that need new fields
One-liner patches: execute:frappe.delete_doc("Page", "old-page", ignore_missing=True)
Testing a Patch
# Run all pending patches
bench --site mysite migrate

# Run a specific patch manually in console
bench --site mysite console
>>> from my_app.patches.v1_2.update_customer_status import execute
>>> execute()
>>> frappe.db.commit()

10. Publishing to Frappe Marketplace
Prerequisites Checklist
App hosted on public GitHub repository
setup.py or pyproject.toml with correct metadata
Valid __version__ in __init__.py
README.md with installation instructions
All tests passing
setup.py (v14)
from setuptools import setup, find_packages

setup(
    name="my_custom_app",
    version="1.0.0",
    description="My Custom App for ERPNext",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
)

pyproject.toml (v15+)
[project]
name = "my_custom_app"
dynamic = ["version"]
requires-python = ">=3.10,<3.13"
dependencies = ["frappe"]

[build-system]
requires = ["flit_core >=3.4,<4"]
build-backend = "flit_core:buildapi"

Publishing Steps
Create account at https://frappecloud.com/marketplace
Add your GitHub repository
Configure supported versions (v14, v15)
Submit for review
After approval, app appears in Marketplace
11. App Update Lifecycle on Client Sites
# Pull latest code
bench update --pull

# Or update specific app
cd apps/my_custom_app && git pull origin main && cd ../..

# Then migrate (runs patches + syncs schema)
bench --site mysite migrate

# Rebuild assets
bench build --app my_custom_app

# Restart workers
bench restart


The bench update command wraps: backup → pull → requirements → migrate → build → restart.

ALWAYS take a backup before running bench update on production. ALWAYS test updates on staging before applying to production.

See Also
references/examples.md — Complete app scaffolding examples
references/anti-patterns.md — Common mistakes
references/workflows.md — Step-by-step workflows
references/module-workspace-shipping.md — Module Def, modules.txt, and workspace shipping
frappe-syntax-hooks — Complete hooks.py reference
frappe-core-database — Database and migration patterns
frappe-impl-workspace — Workspace builder, components, and customization
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
SnykFail