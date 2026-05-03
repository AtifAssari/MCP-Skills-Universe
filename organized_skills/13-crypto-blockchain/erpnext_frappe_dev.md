---
rating: ⭐⭐⭐
title: erpnext-frappe-dev
url: https://skills.sh/6missedcalls/erpnext-skill/erpnext-frappe-dev
---

# erpnext-frappe-dev

skills/6missedcalls/erpnext-skill/erpnext-frappe-dev
erpnext-frappe-dev
Installation
$ npx skills add https://github.com/6missedcalls/erpnext-skill --skill erpnext-frappe-dev
SKILL.md
Frappe Framework Development Reference

Complete documentation for building applications on Frappe Framework / ERPNext. This skill contains comprehensive API documentation that Claude Code needs to build any Frappe app from scratch.

When to Use This Skill

Use this skill when:

Creating a new Frappe/ERPNext custom app
Building DocTypes and controllers
Writing hooks for customization
Implementing REST APIs
Creating form scripts (client-side JS)
Writing background jobs
Building integrations with external services
Any ERPNext/Frappe development work
Quick Start
Create an App
bench new-app my_app
bench --site mysite install-app my_app

Key Files
hooks.py — App-level configuration and event handlers
{doctype}.py — Python controller (server-side logic)
{doctype}.js — Form script (client-side logic)
{doctype}.json — DocType definition
Documentation Index
Reference	Contents
reference/frappe-framework-complete.md	MAIN REFERENCE — Full API docs for Document, Database, Controllers, Hooks, REST API, Form Scripts, Testing
reference/document-api.md	Document CRUD operations
reference/database-api.md	Database queries and transactions
reference/hooks-reference.md	hooks.py configuration
reference/rest-api.md	REST API endpoints
reference/form-scripts.md	Client-side JavaScript
reference/index.md	ERPNext module documentation index
reference/accounting/	Accounting module reference
reference/stock/	Inventory/Stock module reference
reference/manufacturing/	Manufacturing module reference
reference/crm/	CRM module reference
reference/hr-payroll/	HR & Payroll module reference
reference/api/	REST & Developer API reference
Core Concepts Summary
DocType = Model
# DocType "Customer" creates:
# - Database table `tabCustomer`
# - Python controller customer.py
# - Form script customer.js

Document = Instance
doc = frappe.get_doc("Customer", "CUST-001")
doc.customer_name = "Updated Name"
doc.save()

Controller = Business Logic
class Customer(Document):
    def validate(self):
        if not self.email:
            frappe.throw("Email required")
    
    def on_submit(self):
        self.create_linked_records()

Hooks = App Configuration
# hooks.py
doc_events = {
    "Sales Order": {
        "on_submit": "my_app.events.on_sales_order_submit"
    }
}

API Quick Reference
Document Operations
frappe.get_doc(doctype, name)           # Get document
frappe.new_doc(doctype)                 # Create new
doc.insert()                            # Insert to DB
doc.save()                              # Update in DB
doc.delete()                            # Delete
doc.db_set(field, value)               # Direct DB update

Database Queries
frappe.db.get_list(doctype, filters, fields)  # With permissions
frappe.db.get_all(doctype, filters, fields)   # All records
frappe.db.get_value(doctype, name, field)     # Single value
frappe.db.set_value(doctype, name, field, val) # Direct update
frappe.db.exists(doctype, name)               # Check exists
frappe.db.count(doctype, filters)             # Count records

Controller Hooks
autoname → before_insert → validate → before_save → 
on_update → after_insert → on_submit → on_cancel

REST API
GET    /api/resource/{doctype}           # List
GET    /api/resource/{doctype}/{name}    # Read
POST   /api/resource/{doctype}           # Create
PUT    /api/resource/{doctype}/{name}    # Update
DELETE /api/resource/{doctype}/{name}    # Delete
POST   /api/method/{dotted.path}         # Custom method

Form Scripts
frappe.ui.form.on('DocType', {
    refresh(frm) { },
    validate(frm) { },
    fieldname(frm) { }  // Field change
});

Read Full Documentation

Start with: reference/frappe-framework-complete.md

This file contains 20KB+ of comprehensive documentation covering all Frappe APIs with code examples.

Weekly Installs
49
Repository
6missedcalls/er…xt-skill
GitHub Stars
6
First Seen
Feb 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass