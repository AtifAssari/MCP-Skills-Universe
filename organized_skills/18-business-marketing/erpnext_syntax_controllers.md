---
rating: ⭐⭐⭐
title: erpnext-syntax-controllers
url: https://skills.sh/openaec-foundation/erpnext_anthropic_claude_development_skill_package/erpnext-syntax-controllers
---

# erpnext-syntax-controllers

skills/openaec-foundation/erpnext_anthropic_claude_development_skill_package/erpnext-syntax-controllers
erpnext-syntax-controllers
Installation
$ npx skills add https://github.com/openaec-foundation/erpnext_anthropic_claude_development_skill_package --skill erpnext-syntax-controllers
SKILL.md
ERPNext Syntax: Document Controllers

Document Controllers are Python classes that implement the server-side logic of a DocType.

Quick Reference
Controller Basic Structure
import frappe
from frappe.model.document import Document

class SalesOrder(Document):
    def validate(self):
        """Main validation - runs on every save."""
        if not self.items:
            frappe.throw(_("Items are required"))
        self.total = sum(item.amount for item in self.items)
    
    def on_update(self):
        """After save - changes to self are NOT saved."""
        self.update_linked_docs()

Location and Naming
DocType	Class	File
Sales Order	SalesOrder	selling/doctype/sales_order/sales_order.py
Custom Doc	CustomDoc	module/doctype/custom_doc/custom_doc.py

Rule: DocType name → PascalCase (remove spaces) → snake_case filename

Most Used Hooks
Hook	When	Typical Use
validate	Before every save	Validation, calculations
on_update	After every save	Notifications, linked docs
after_insert	After new doc	Creation-only actions
on_submit	After submit	Ledger entries, stock
on_cancel	After cancel	Reverse ledger entries
on_trash	Before delete	Cleanup related data
autoname	On naming	Custom document name

Complete list and execution order: See lifecycle-methods.md

Hook Selection Decision Tree
What do you want to do?
│
├─► Validate or calculate fields?
│   └─► validate
│
├─► Action after save (emails, linked docs)?
│   └─► on_update
│
├─► Only for NEW docs?
│   └─► after_insert
│
├─► On SUBMIT?
│   ├─► Check beforehand? → before_submit
│   └─► Action afterwards? → on_submit
│
├─► On CANCEL?
│   ├─► Check beforehand? → before_cancel
│   └─► Cleanup? → on_cancel
│
├─► Custom document name?
│   └─► autoname
│
└─► Cleanup before delete?
    └─► on_trash

Critical Rules
1. Changes after on_update are NOT saved
# ❌ WRONG - change is lost
def on_update(self):
    self.status = "Completed"  # NOT saved

# ✅ CORRECT - use db_set
def on_update(self):
    frappe.db.set_value(self.doctype, self.name, "status", "Completed")

2. No commits in controllers
# ❌ WRONG - Frappe handles commits
def on_update(self):
    frappe.db.commit()  # DON'T DO THIS

# ✅ CORRECT - no commit needed
def on_update(self):
    self.update_related()  # Frappe commits automatically

3. Always call super() when overriding
# ❌ WRONG - parent logic is skipped
def validate(self):
    self.custom_check()

# ✅ CORRECT - parent logic is preserved
def validate(self):
    super().validate()
    self.custom_check()

4. Use flags for recursion prevention
def on_update(self):
    if self.flags.get('from_linked_doc'):
        return
    
    linked = frappe.get_doc("Linked Doc", self.linked_doc)
    linked.flags.from_linked_doc = True
    linked.save()

Document Naming (autoname)
Available Naming Options
Option	Example	Result	Version
field:fieldname	field:customer_name	ABC Company	All
naming_series:	naming_series:	SO-2024-00001	All
format:PREFIX-{##}	format:INV-{YYYY}-{####}	INV-2024-0001	All
hash	hash	a1b2c3d4e5	All
Prompt	Prompt	User enters name	All
UUID	UUID	01948d5f-...	v16+
Custom method	Controller autoname()	Any pattern	All
UUID Naming (v16+)

New in v16: UUID-based naming for globally unique identifiers.

{
  "doctype": "DocType",
  "autoname": "UUID"
}


Benefits:

Globally unique across systems
Better data integrity and traceability
Reduced database storage
Faster bulk record creation
Link fields store UUID in native format

Implementation:

# Frappe automatically generates UUID7
# In naming.py:
if meta.autoname == "UUID":
    doc.name = str(uuid_utils.uuid7())


Validation:

# UUID names are validated on import
from uuid import UUID
try:
    UUID(doc.name)
except ValueError:
    frappe.throw(_("Invalid UUID: {}").format(doc.name))

Custom autoname Method
from frappe.model.naming import getseries

class Project(Document):
    def autoname(self):
        # Custom naming based on customer
        prefix = f"P-{self.customer}-"
        self.name = getseries(prefix, 3)
        # Result: P-ACME-001, P-ACME-002, etc.

Format Patterns
Pattern	Description	Example
{#}	Counter	1, 2, 3
{##}	Zero-padded counter	01, 02, 03
{####}	4-digit counter	0001, 0002
{YYYY}	Full year	2024
{YY}	2-digit year	24
{MM}	Month	01-12
{DD}	Day	01-31
{fieldname}	Field value	(value)
Controller Override
Via hooks.py (override_doctype_class)
# hooks.py
override_doctype_class = {
    "Sales Order": "custom_app.overrides.CustomSalesOrder"
}

# custom_app/overrides.py
from erpnext.selling.doctype.sales_order.sales_order import SalesOrder

class CustomSalesOrder(SalesOrder):
    def validate(self):
        super().validate()
        self.custom_validation()

Via doc_events (hooks.py)
# hooks.py
doc_events = {
    "Sales Order": {
        "validate": "custom_app.events.validate_sales_order",
        "on_submit": "custom_app.events.on_submit_sales_order"
    }
}

# custom_app/events.py
def validate_sales_order(doc, method):
    if doc.total > 100000:
        doc.requires_approval = 1


Choice: override_doctype_class for full control, doc_events for individual hooks.

Submittable Documents

Documents with is_submittable = 1 have a docstatus lifecycle:

docstatus	Status	Editable	Can go to
0	Draft	✅ Yes	1 (Submit)
1	Submitted	❌ No	2 (Cancel)
2	Cancelled	❌ No	-
class StockEntry(Document):
    def on_submit(self):
        """After submit - create stock ledger entries."""
        self.update_stock_ledger()
    
    def on_cancel(self):
        """After cancel - reverse the entries."""
        self.reverse_stock_ledger()

Virtual DocTypes

For external data sources (no database table):

class ExternalCustomer(Document):
    @staticmethod
    def get_list(args):
        return external_api.get_customers(args.get("filters"))
    
    @staticmethod
    def get_count(args):
        return external_api.count_customers(args.get("filters"))
    
    @staticmethod
    def get_stats(args):
        return {}

Inheritance Patterns
Standard Controller
from frappe.model.document import Document

class MyDocType(Document):
    pass

Tree DocType
from frappe.utils.nestedset import NestedSet

class Department(NestedSet):
    pass

Extend Existing Controller
from erpnext.selling.doctype.sales_order.sales_order import SalesOrder

class CustomSalesOrder(SalesOrder):
    def validate(self):
        super().validate()
        self.custom_validation()

Type Annotations (v15+)
class Person(Document):
    if TYPE_CHECKING:
        from frappe.types import DF
        first_name: DF.Data
        last_name: DF.Data
        birth_date: DF.Date


Enable in hooks.py:

export_python_type_annotations = True

Reference Files
File	Contents
lifecycle-methods.md	All hooks, execution order, examples
methods.md	All doc.* methods with signatures
flags.md	Flags system documentation
examples.md	Complete working controller examples
anti-patterns.md	Common mistakes and corrections
Version Differences
Feature	v14	v15	v16
Type annotations	❌	✅ Auto-generated	✅
before_discard hook	❌	✅	✅
on_discard hook	❌	✅	✅
flags.notify_update	❌	✅	✅
UUID autoname	❌	❌	✅
UUID in Link fields (native)	❌	❌	✅
v16-Specific Notes

UUID Naming:

Set autoname = "UUID" in DocType definition
Uses uuid7() for time-ordered UUIDs
Link fields store UUIDs in native format (not text)
Improves performance for bulk operations

Choosing UUID vs Traditional Naming:

When to use UUID:
├── Cross-system data synchronization
├── Bulk record creation
├── Global uniqueness required
└── No human-readable name needed

When to use traditional naming:
├── User-facing document references (SO-00001)
├── Sequential numbering required
├── Auditing requires readable names
└── Integration with legacy systems

Anti-Patterns
❌ Direct field change after on_update
def on_update(self):
    self.status = "Done"  # Will be lost!

❌ frappe.db.commit() in controller
def validate(self):
    frappe.db.commit()  # Breaks transaction!

❌ Forgetting to call super()
def validate(self):
    self.my_check()  # Parent validate is skipped


→ See anti-patterns.md for complete list.

Related Skills
erpnext-syntax-serverscripts – Server Scripts (sandbox alternative)
erpnext-syntax-hooks – hooks.py configuration
erpnext-impl-controllers – Implementation workflows
Weekly Installs
43
Repository
openaec-foundat…_package
GitHub Stars
92
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn